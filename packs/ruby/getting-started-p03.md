---
title: "Getting Started with Rails (part 3/3)"
source: https://guides.rubyonrails.org/getting_started.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 3/3
---

## 16. Action Mailer and Email Notifications

A common feature of e-commerce stores is an email subscription to get notified when a product is back in stock. Now that we've seen the basics of Rails, let's add this feature to our store.

### 16.1. Basic Inventory Tracking

First, let's add an inventory count to the Product model so we can keep track of stock. We can generate this migration using the following command:

```console
$ bin/rails generate migration AddInventoryCountToProducts inventory_count:integer
```

Rails infers that `AddInventoryCountToProducts` targets the `products` table because the name matches the `add_<columns>_to_<table>` convention. That pattern lets the generator pre-fill `add_column :products, ...`, so you only need to supply the column details. Run `bin/rails generate migration --help` to see more naming conventions.

This will generate a migration file. Open it and add a default value of `0` to ensure `inventory_count` is never `nil`:

```ruby
# db/migrate/<timestamp>_add_inventory_count_to_products.rb
class AddInventoryCountToProducts < ActiveRecord::Migration[8.1]
  def change
    add_column :products, :inventory_count, :integer, default: 0
  end
end
```

Then let's run the migration.

```console
$ bin/rails db:migrate
```

We'll need to add the inventory count to the product form in `app/views/products/_form.html.erb`.

```erb
<%# app/views/products/_form.html.erb %>
<%= form_with model: product do |form| %>
  <%# ... %>

  <div>
    <%= form.label :inventory_count, style: "display: block" %>
    <%= form.number_field :inventory_count %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

The controller also needs `:inventory_count` added to the permitted parameters.

```ruby
# app/controllers/products_controller.rb
    def product_params
      params.expect(product: [ :name, :description, :featured_image, :inventory_count ])
    end
```

It would also be helpful to validate that our inventory count is never a negative number, so let's also add a validation for that in our model.

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  has_one_attached :featured_image
  has_rich_text :description

  validates :name, presence: true
  validates :inventory_count, numericality: { greater_than_or_equal_to: 0 }
end
```

With these changes, we can now update the inventory count of products in our store.

### 16.2. Adding Subscribers to Products

In order to notify users that a product is back in stock, we need to keep track of these subscribers.

Let's generate a model called Subscriber to store these email addresses and associate them with the respective product.

Here we are not specifying a type for `email` as rails automatically defaults to a `string` when a type is not given for migrations.

```console
$ bin/rails generate model Subscriber product:belongs_to email
```

By including `product:belongs_to` above, we told Rails that subscribers and products have a one-to-many relationship, meaning a Subscriber "belongs to" a single Product instance.

Next, open the generated migration (`db/migrate/<timestamp>_create_subscribers.rb`) like we did for Product.

```ruby
# db/migrate/<timestamp>_create_subscribers.rb
class CreateSubscribers < ActiveRecord::Migration[8.1]
  def change
    create_table :subscribers do |t|
      t.belongs_to :product, null: false, foreign_key: true
      t.string :email

      t.timestamps
    end
  end
end
```

This looks quite similar to the migration for `Product`, the main new thing is `belongs_to` which adds a `product_id` foreign key column.

Then run the new migration:

```console
$ bin/rails db:migrate
```

A Product, however, can have many subscribers, so we then add `has_many :subscribers, dependent: :destroy` to our Product model to add the second part of this association between the two models. This tells Rails how to join queries between the two database tables.

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  has_many :subscribers, dependent: :destroy
  has_one_attached :featured_image
  has_rich_text :description

  validates :name, presence: true
  validates :inventory_count, numericality: { greater_than_or_equal_to: 0 }
end
```

Now we need a controller to create these subscribers. Let's create that in `app/controllers/subscribers_controller.rb` with the following code:

```ruby
# app/controllers/subscribers_controller.rb
class SubscribersController < ApplicationController
  allow_unauthenticated_access
  before_action :set_product

  def create
    @product.subscribers.where(subscriber_params).first_or_create
    redirect_to @product, notice: "You are now subscribed."
  end

  private
    def set_product
      @product = Product.find(params[:product_id])
    end

    def subscriber_params
      params.expect(subscriber: [ :email ])
    end
end
```

The `redirect_to` uses the `notice:` argument to set a "flash" message to tell the user they are subscribed.

The flash provides a way to pass temporary data between controller actions. Anything you place in the flash will be available to the very next action and then cleared. The flash is typically used for setting messages (e.g. notices and alerts) in a controller action before redirecting to an action that displays the message to the user.

To display the flash message, let's add the flash to `app/views/layouts/application.html.erb` inside the body:

```erb
<%# app/views/layouts/application.html.erb %>
<html>
  <%# ... %>
  <body>
    <div class="notice"><%= flash[:notice] %></div>
    <div class="alert"><%= flash[:alert] %></div>
    <%# ... %>
  </body>
</html>
```

Learn more about the Flash in the Action Controller Overview

To subscribe users to a specific product, we'll use a nested route so we know which product the subscriber belongs to. In `config/routes.rb` change `resources :products` to the following:

```ruby
# config/routes.rb
Rails.application.routes.draw do
  # ...
  resources :products do
    resources :subscribers, only: [ :create ]
  end
end
```

On the product show page, we can check if there is inventory and display the amount in stock. Otherwise, we can display an out of stock message with the subscribe form to get notified when it is back in stock.

Create a new partial at `app/views/products/_inventory.html.erb` and add the following:

```erb
<%# app/views/products/_inventory.html.erb %>
<% if product.inventory_count.positive? %>
  <p><%= product.inventory_count %> in stock</p>
<% else %>
  <p>Out of stock</p>
  <p>Email me when available.</p>

  <%= form_with model: [product, Subscriber.new] do |form| %>
    <%= form.email_field :email, placeholder: "you@example.com", required: true %>
    <%= form.submit "Submit" %>
  <% end %>
<% end %>
```

Then update `app/views/products/show.html.erb` to render this partial after the `cache` block.

```erb
<%# app/views/products/show.html.erb %>
<%= render "inventory", product: @product %>
```

### 16.3. In Stock Email Notifications

Action Mailer is a feature of Rails that allows you to send emails. We'll use it to notify subscribers when a product is back in stock.

We can generate a mailer with the following command:

```console
$ bin/rails g mailer Product in_stock
```

This generates a class at `app/mailers/product_mailer.rb` with an `in_stock` method.

Update this method to mail to a subscriber's email address.

```ruby
# app/mailers/product_mailer.rb
class ProductMailer < ApplicationMailer
  # Subject can be set in your I18n file at config/locales/en.yml
  # with the following lookup:
  #
  #   en.product_mailer.in_stock.subject
  #
  def in_stock
    @product = params[:product]
    mail to: params[:subscriber].email
  end
end
```

The mailer generator also generates two email templates in our views folder: one for HTML and one for Text. We can update those to include a message and link to the product.

Change `app/views/product_mailer/in_stock.html.erb` to:

```erb
<%# app/views/product_mailer/in_stock.html.erb %>
<h1>Good news!</h1>

<p><%= link_to @product.name, product_url(@product) %> is back in stock.</p>
```

And `app/views/product_mailer/in_stock.text.erb` to:

```erb
<%# app/views/product_mailer/in_stock.text.erb %>
Good news!

<%= @product.name %> is back in stock.
<%= product_url(@product) %>
```

We use `product_url` instead of `product_path` in mailers because email clients need to know the full URL to open in the browser when the link is clicked.

We can test an email by opening the Rails console and loading a product and subscriber to send to:

```irb
store(dev)> product = Product.first
store(dev)> subscriber = product.subscribers.find_or_create_by(email: "subscriber@example.org")
store(dev)> ProductMailer.with(product: product, subscriber: subscriber).in_stock.deliver_later
```

You'll see that it prints out an email in the logs.

```plaintext
ProductMailer#in_stock: processed outbound mail in 63.0ms
Delivered mail 66a3a9afd5d4a_108b04a4c41443@local.mail (33.1ms)
Date: Fri, 26 Jul 2024 08:50:39 -0500
From: from@example.com
To: subscriber@example.com
Message-ID: <66a3a9afd5d4a_108b04a4c41443@local.mail>
Subject: In stock
Mime-Version: 1.0
Content-Type: multipart/alternative;
 boundary="--==_mimepart_66a3a9afd235e_108b04a4c4136f";
 charset=UTF-8
Content-Transfer-Encoding: 7bit

----==_mimepart_66a3a9afd235e_108b04a4c4136f
Content-Type: text/plain;
 charset=UTF-8
Content-Transfer-Encoding: 7bit

Good news!

T-Shirt is back in stock.
http://localhost:3000/products/1

----==_mimepart_66a3a9afd235e_108b04a4c4136f
Content-Type: text/html;
 charset=UTF-8
Content-Transfer-Encoding: 7bit

<!-- BEGIN app/views/layouts/mailer.html.erb --><!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
      /* Email styles need to be inline */
    </style>
  </head>

  <body>
    <!-- BEGIN app/views/product_mailer/in_stock.html.erb --><h1>Good news!</h1>

<p><a href="http://localhost:3000/products/1">T-Shirt</a> is back in stock.</p>
<!-- END app/views/product_mailer/in_stock.html.erb -->
  </body>
</html>
<!-- END app/views/layouts/mailer.html.erb -->
----==_mimepart_66a3a9afd235e_108b04a4c4136f--

Performed ActionMailer::MailDeliveryJob (Job ID: 5e2bd5f2-f54f-4088-ace3-3f6eb15aaf46) from Async(default) in 111.34ms
```

To trigger these emails, we can use a callback in the Product model to send emails anytime the inventory count changes from 0 to a positive number.

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  has_many :subscribers, dependent: :destroy
  has_one_attached :featured_image
  has_rich_text :description

  validates :name, presence: true
  validates :inventory_count, numericality: { greater_than_or_equal_to: 0 }

  after_update_commit :notify_subscribers, if: :back_in_stock?

  def back_in_stock?
    inventory_count_previously_was.zero? && inventory_count.positive?
  end

  def notify_subscribers
    subscribers.each do |subscriber|
      ProductMailer.with(product: self, subscriber: subscriber).in_stock.deliver_later
    end
  end
end
```

`after_update_commit` is an Active Record callback that is fired after changes are saved to the database. `if: :back_in_stock?` tells the callback to run only if the `back_in_stock?` method returns true.

Active Record keeps track of changes to attributes so `back_in_stock?` checks the previous value of `inventory_count` using `inventory_count_previously_was`. Then we can compare that against the current inventory count to determine if the product is back in stock.

`notify_subscribers` uses the Active Record association to query the `subscribers` table for all subscribers for this specific product and then queues up the `in_stock` email to be sent to each of them.

### 16.4. Extracting a Concern

The Product model now has a decent amount of code for handling notifications. To better organize our code, we can extract this to an `ActiveSupport::Concern`. A Concern is a Ruby module with some syntactic sugar to make using them easier.

First let’s create the Notifications module.

Create a file at `app/models/product/notifications.rb` with the following:

```ruby
# app/models/product/notifications.rb
module Product::Notifications
  extend ActiveSupport::Concern

  included do
    has_many :subscribers, dependent: :destroy
    after_update_commit :notify_subscribers, if: :back_in_stock?
  end

  def back_in_stock?
    inventory_count_previously_was.zero? && inventory_count.positive?
  end

  def notify_subscribers
    subscribers.each do |subscriber|
      ProductMailer.with(product: self, subscriber: subscriber).in_stock.deliver_later
    end
  end
end
```

When you include a module in a class, any code inside the `included` block runs as if it’s part of that class. At the same time, the methods defined in the module become regular methods you can call on objects (instances) of that class.

Now that the code triggering the notification has been extracted into the Notifications module, the Product model can be simplified to include the Notifications module.

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  include Notifications

  has_one_attached :featured_image
  has_rich_text :description

  validates :name, presence: true
  validates :inventory_count, numericality: { greater_than_or_equal_to: 0 }
end
```

Concerns are a great way to organize features of your Rails application. As you add more features to the Product, the class will become messy. Instead, we can use Concerns to extract each feature out into a self-contained module like `Product::Notifications` which contains all the functionality for handling subscribers and how notifications are sent.

Extracting code into concerns also helps make features reusable. For example, we could introduce a new model that also needs subscriber notifications. This module could be used in multiple models to provide the same functionality.

### 16.5. Unsubscribe Links

A subscriber may want to unsubscribe at some point, so let's build that next.

First, we need a route for unsubscribing that will be the URL we include in emails.

```ruby
# config/routes.rb
Rails.application.routes.draw do
  # ...
  resources :products do
    resources :subscribers, only: [ :create ]
  end
  resource :unsubscribe, only: [ :show ]
```

The unsubscribe route is added at the top level and uses the singular `resource` in order to handle routes like `/unsubscribe?token=xyz`.

Active Record has a feature called `generates_token_for` that can generate unique tokens to find database records for different purposes. We can use this for generating a unique unsubscribe token to use in the email's unsubscribe URL.

```ruby
# app/models/subscriber.rb
class Subscriber < ApplicationRecord
  belongs_to :product
  generates_token_for :unsubscribe
end
```

Our controller will first look up the Subscriber record from the token in the URL. Once the subscriber is found, it will destroy the record and redirect to the homepage. Create `app/controllers/unsubscribes_controller.rb` and add the following code:

```ruby
# app/controllers/unsubscribes_controller.rb
class UnsubscribesController < ApplicationController
  allow_unauthenticated_access
  before_action :set_subscriber

  def show
    @subscriber&.destroy
    redirect_to root_path, notice: "Unsubscribed successfully."
  end

  private
    def set_subscriber
      @subscriber = Subscriber.find_by_token_for(:unsubscribe, params[:token])
    end
end
```

Last but not least, let's add the unsubscribe link to our email templates.

In `app/views/product_mailer/in_stock.html.erb`, add a `link_to`:

```erb
<%# app/views/product_mailer/in_stock.html.erb %>
<h1>Good news!</h1>

<p><%= link_to @product.name, product_url(@product) %> is back in stock.</p>

<%= link_to "Unsubscribe", unsubscribe_url(token: params[:subscriber].generate_token_for(:unsubscribe)) %>
```

In `app/views/product_mailer/in_stock.text.erb`, add the URL in plain text:

```erb
<%# app/views/product_mailer/in_stock.text.erb %>
Good news!

<%= @product.name %> is back in stock.
<%= product_url(@product) %>

Unsubscribe: <%= unsubscribe_url(token: params[:subscriber].generate_token_for(:unsubscribe)) %>
```

When the unsubscribe link is clicked, the subscriber record will be deleted from the database. The controller also safely handles invalid or expired tokens without raising any errors.

Use the Rails console to send another email and test the unsubscribe link in the logs.


## 17. Adding CSS & JavaScript

CSS & JavaScript are core to building web applications, so let's learn how to use them with Rails.

### 17.1. Propshaft

Rails' asset pipeline is called Propshaft. It takes your CSS, JavaScript, images, and other assets and serves them to your browser. In production, Propshaft keeps track of each version of your assets so they can be cached to make your pages faster. Check out the Asset Pipeline guide to learn more about how this works.

Let's modify `app/assets/stylesheets/application.css` and change our font to sans-serif.

```css
/* app/assets/stylesheets/application.css */
body {
  font-family: Arial, Helvetica, sans-serif;
  padding: 1rem;
}

nav {
  justify-content: flex-end;
  display: flex;
  font-size: 0.875em;
  gap: 0.5rem;
  max-width: 1024px;
  margin: 0 auto;
  padding: 1rem;
}

nav a {
  display: inline-block;
}

main {
  max-width: 1024px;
  margin: 0 auto;
}

.alert,
.error {
  color: red;
}

.notice {
  color: green;
}

section.product {
  display: flex;
  gap: 1rem;
  flex-direction: row;
}

section.product img {
  border-radius: 8px;
  flex-basis: 50%;
  max-width: 50%;
}
```

Then we'll update `app/views/products/show.html.erb` to use these new styles.

```erb
<%# app/views/products/show.html.erb %>
<p><%= link_to "Back", products_path %></p>

<section class="product">
  <%= image_tag @product.featured_image if @product.featured_image.attached? %>

  <section class="product-info">
    <% cache @product do %>
      <h1><%= @product.name %></h1>
      <%= @product.description %>
    <% end %>

    <%= render "inventory", product: @product %>

    <% if authenticated? %>
      <%= link_to "Edit", edit_product_path(@product) %>
      <%= button_to "Delete", @product, method: :delete, data: { turbo_confirm: "Are you sure?" } %>
    <% end %>
  </section>
</section>
```

Refresh your page and you'll see the CSS has been applied.

### 17.2. Import Maps

Rails uses import maps for JavaScript by default. This allows you to write modern JavaScript modules with no build steps.

You can find the JavaScript pins in `config/importmap.rb`. This file maps the JavaScript package names with the source file which is used to generate the importmap tag in the browser.

```ruby
# config/importmap.rb
# Pin npm packages by running ./bin/importmap

pin "application"
pin "@hotwired/turbo-rails", to: "turbo.min.js"
pin "@hotwired/stimulus", to: "stimulus.min.js"
pin "@hotwired/stimulus-loading", to: "stimulus-loading.js"
pin_all_from "app/javascript/controllers", under: "controllers"
pin "trix"
pin "@rails/actiontext", to: "actiontext.esm.js"
```

Each pin maps a JavaScript package name (e.g., `"@hotwired/turbo-rails"`) to a specific file or URL (e.g., `"turbo.min.js"`). `pin_all_from` maps all files in a directory (e.g., `app/javascript/controllers`) to a namespace (e.g., `"controllers"`).

Import maps keep the setup clean and minimal, while still supporting modern JavaScript features.

What are these JavaScript files already in our import map? They are a frontend framework called Hotwire that Rails uses by default.

### 17.3. Hotwire

Hotwire is a JavaScript framework designed to take full advantage of server-side generated HTML. It is comprised of 3 core components:

1. **Turbo** handles navigation, form submissions, page components, and updates without writing any custom JavaScript.
2. **Stimulus** provides a framework for when you need custom JavaScript to add functionality to the page.
3. **Native** allows you to make hybrid mobile apps by embedding your web app and progressively enhancing it with native mobile features.

We haven't written any JavaScript yet, but we have been using Hotwire on the frontend. For instance, the form you created to add and edit a product was powered by Turbo.

Learn more in the Asset Pipeline and Working with JavaScript in Rails guides.


## 18. Testing

Rails comes with a robust test suite. Let's write a test to ensure that the correct number of emails are sent when a product is back in stock.

### 18.1. Fixtures

When you generate a model using Rails, it automatically creates a corresponding fixture file in the `test/fixtures` directory.

Fixtures are predefined sets of data that populate your test database before running tests. They allow you to define records with easy-to-remember names, making it simple to access them in your tests.

This file will be empty by default - you need to populate it with fixtures for your tests.

Let’s update the product fixtures file at `test/fixtures/products.yml` with the following:

```yaml
# test/fixtures/products.yml
tshirt:
  name: T-Shirt
  inventory_count: 15
```

And for subscribers, let's add these two fixtures to `test/fixtures/subscribers.yml`:

```yaml
# test/fixtures/subscribers.yml
david:
  product: tshirt
  email: david@example.org

chris:
  product: tshirt
  email: chris@example.org
```

You'll notice that we can reference the `Product` fixture by name here. Rails associates this automatically for us in the database so we don't have to manage record IDs and associations in tests.

These fixtures will be automatically inserted into the database when we run our test suite.

### 18.2. Testing Emails

In `test/models/product_test.rb`, let's add a test:

```ruby
# test/models/product_test.rb
require "test_helper"

class ProductTest < ActiveSupport::TestCase
  include ActionMailer::TestHelper

  test "sends email notifications when back in stock" do
    product = products(:tshirt)

    # Set product out of stock
    product.update(inventory_count: 0)

    assert_emails 2 do
      product.update(inventory_count: 99)
    end
  end
end
```

Let's break down what this test is doing.

First, we include the Action Mailer test helpers so we can monitor emails sent during the test.

The `tshirt` fixture is loaded using the `products()` fixture helper and returns the Active Record object for that record. Each fixture generates a helper in the test suite to make it easy to reference fixtures by name since their database IDs may be different each run.

Then we ensure the tshirt is out of stock by updating it's inventory to 0.

Next, we use `assert_emails` to ensure 2 emails were generated by the code inside the block. To trigger the emails, we update the product's inventory count inside the block. This triggers the `notify_subscribers` callback in the Product model to send emails. Once that's done executing, `assert_emails` counts the emails and ensures it matches the expected count.

We can run the test suite with `bin/rails test` or an individual test file by passing the filename.

```console
$ bin/rails test test/models/product_test.rb
Running 1 tests in a single process (parallelization threshold is 50)
Run options: --seed 3556

# Running:

.

Finished in 0.343842s, 2.9083 runs/s, 5.8166 assertions/s.
1 runs, 2 assertions, 0 failures, 0 errors, 0 skips
```

Our test passes!

Rails also generated an example test for `ProductMailer` at `test/mailers/product_mailer_test.rb`. Let's update it to make it also pass.

```ruby
# test/mailers/product_mailer_test.rb
require "test_helper"

class ProductMailerTest < ActionMailer::TestCase
  test "in_stock" do
    mail = ProductMailer.with(product: products(:tshirt), subscriber: subscribers(:david)).in_stock
    assert_equal "In stock", mail.subject
    assert_equal [ "david@example.org" ], mail.to
    assert_equal [ "from@example.com" ], mail.from
    assert_match "Good news!", mail.body.encoded
  end
end
```

Let's run the entire test suite now and ensure all the tests pass.

```console
$ bin/rails test
Running 2 tests in a single process (parallelization threshold is 50)
Run options: --seed 16302

# Running:

..

Finished in 0.665856s, 3.0037 runs/s, 10.5128 assertions/s.
2 runs, 7 assertions, 0 failures, 0 errors, 0 skips
```

You can use this as a starting place to continue building out a test suite with full coverage of the application features.

Learn more about Testing Rails Applications


## 19. Consistently Formatted Code with RuboCop

When writing code we may sometimes use inconsistent formatting. Rails comes with a linter called RuboCop that helps keep our code formatted consistently.

We can check our code for consistency by running:

```console
$ bin/rubocop
```

This will print out any offenses and tell you what they are.

```console
Inspecting 53 files
.....................................................

53 files inspected, no offenses detected
```

RuboCop can automatically fix offenses using the `--autocorrect` flag (or its short version `-a`).

```plaintext
$ bin/rubocop -a
```


## 20. Security

Rails includes the Brakeman gem for checking security issues with your application - vulnerabilities that can lead to attacks such as session hijacking, session fixation, or redirection.

Run `bin/brakeman` and it will analyze your application and output a report.

```console
$ bin/brakeman
Loading scanner...
...

== Overview ==

Controllers: 6
Models: 6
Templates: 15
Errors: 0
Security Warnings: 0

== Warning Types ==

No warnings found
```

Learn more about Securing Rails Applications


## 21. Continuous Integration with GitHub Actions

Rails apps generate a `.github` folder that includes a prewritten GitHub Actions configuration that runs rubocop, brakeman, and our test suite.

When we push our code to a GitHub repository with GitHub Actions enabled, it will automatically run these steps and report back success or failure for each. This allows us to monitor our code changes for defects and issues and ensure consistent quality for our work.


## 22. Deploying to Production

And now the fun part: let’s deploy your app.

Rails comes with a deployment tool called Kamal that we can use to deploy our application directly to a server. Kamal uses Docker containers to run your application and deploy with zero downtime.

By default, Rails comes with a production-ready Dockerfile that Kamal will use to build the Docker image, creating a containerized version of your application with all its dependencies and configurations. This Dockerfile uses Thruster to compress and serve assets efficiently in production.

To deploy with Kamal, we need:

- A server running Ubuntu LTS with 1GB RAM or more. The server should run the Ubuntu operating system with a Long-Term Support (LTS) version so it receives regular security and bug fixes. Hetzner, DigitalOcean, and other hosting services provide servers to get started.
- A Docker Hub account and access token. Docker Hub stores the image of the application so it can be downloaded and run on the server.

On Docker Hub, create a Repository for your application image. Use "store" as the name for the repository.

Open `config/deploy.yml` and replace `192.168.0.1` with your server's IP address and `your-user` with your Docker Hub username.

```yaml
# config/deploy.yml
# Name of your application. Used to uniquely configure containers.
service: store

# Name of the container image.
image: your-user/store

# Deploy to these servers.
servers:
  web:
    - 192.168.0.1

# Credentials for your image host.
registry:
  # Specify the registry server, if you're not using Docker Hub
  # server: registry.digitalocean.com / ghcr.io / ...
  username: your-user
```

Under the `proxy:` section, you can add a domain to enable SSL for your application too. Make sure your DNS record points to the server and Kamal will use LetsEncrypt to issue an SSL certificate for the domain.

```yaml
# config/deploy.yml
proxy:
  ssl: true
  host: app.example.com
```

Create an access token with Read & Write permissions on Docker's website so Kamal can push the Docker image for your application.

Then export the access token in the terminal so Kamal can find it.

```console
export KAMAL_REGISTRY_PASSWORD=your-access-token
```

Run the following command to set up your server and deploy your application for the first time.

```console
$ bin/kamal setup
```

Congratulations! Your new Rails application is live and in production!

To view your new Rails app in action, open your browser and enter your server's IP address. You should see your store up and running.

After this, when you make changes to your app and want to push them to production, you can run the following:

```console
$ bin/kamal deploy
```

### 22.1. Adding a User to Production

To create and edit products in production, we need a User record in the production database.

You can use Kamal to open a production Rails console.

```console
$ bin/kamal console
```

```ruby
store(prod)> User.create!(email_address: "you@example.org", password: "s3cr3t", password_confirmation: "s3cr3t")
```

Now you can log in to production with this email and password and manage products.

### 22.2. Background Jobs using Solid Queue

Background jobs allow you to run tasks asynchronously behind-the-scenes in a separate process, preventing them from interrupting the user experience. Imagine sending in stock emails to 10,000 recipients. It could take a while, so we can offload that task to a background job to keep the Rails app responsive.

In development, Rails uses the `:async` queue adapter to process background jobs with ActiveJob. Async stores pending jobs in memory but it will lose pending jobs on restart. This is great for development, but not production.

To make background jobs more robust, Rails uses `solid_queue` for production environments. Solid Queue stores jobs in the database and executes them in a separate process.

Solid Queue is enabled for our production Kamal deployment using the `SOLID_QUEUE_IN_PUMA: true` environment variable to `config/deploy.yml`. This tells our web server, Puma, to start and stop the Solid Queue process automatically.

When emails are sent with Action Mailer's `deliver_later`, these emails will be sent to Active Job for sending in the background so they don't delay the HTTP request. With Solid Queue in production, emails will be sent in the background, automatically retried if they fail to send, and jobs are kept safe in the database during restarts.


## 23. What's Next?

Congratulations on building and deploying your first Rails application!

Next, follow the Sign Up and Settings tutorial to continue learning.

We also recommend learning more by reading other Ruby on Rails Guides:

- Active Record Basics
- Layouts and Rendering in Rails
- Testing Rails Applications
- Debugging Rails Applications
- Securing Rails Applications

Happy building!
