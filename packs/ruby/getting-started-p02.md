---
title: "Getting Started with Rails (part 2/3)"
source: https://guides.rubyonrails.org/getting_started.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/3
---

## 10. Controllers & Actions

Now that we've defined routes for Products, let's implement the controller and actions to handle requests to these URLs.

This command will generate a `ProductsController` with an index action. Since we've already set up routes, we can skip that part of the generator using a flag.

```console
$ bin/rails generate controller Products index --skip-routes
      create  app/controllers/products_controller.rb
      invoke  erb
      create    app/views/products
      create    app/views/products/index.html.erb
      invoke  test_unit
      create    test/controllers/products_controller_test.rb
      invoke  helper
      create    app/helpers/products_helper.rb
      invoke    test_unit
```

This command generates a handful of files for our controller:

- The controller itself
- A views folder for the controller we generated
- A view file for the action we specified when generating the controller
- A test file for this controller
- A helper file for extracting logic in our views

Let's take a look at the ProductsController defined in `app/controllers/products_controller.rb`. It looks like this:

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
  end
end
```

You may notice the file name `products_controller.rb` is an underscored version of the Class this file defines, `ProductsController`. This pattern helps Rails to automatically load code without having to use `require` like you may have seen in other languages.

The `index` method here is an Action. Even though it's an empty method, Rails will default to rendering a template with the matching name.

The `index` action will render `app/views/products/index.html.erb`. If we open up that file in our code editor, we'll see the HTML it renders.

```erb
<%# app/views/products/index.html.erb %>
<h1>Products#index</h1>
<p>Find me in app/views/products/index.html.erb</p>
```

### 10.1. Making Requests

Let's see this in our browser. First, run `bin/rails server` in your terminal to start the Rails server. Then open http://localhost:3000 and you will see the Rails welcome page.

If we open http://localhost:3000/products in the browser, Rails will render the products index HTML.

Our browser requested `/products` and Rails matched this route to `products#index`. Rails sent the request to the `ProductsController` and called the `index` action. Since this action was empty, Rails rendered the matching template at `app/views/products/index.html.erb` and returned that to our browser. Pretty cool!

If we open `config/routes.rb`, we can tell Rails the root route should render the Products index action by adding this line:

```ruby
# config/routes.rb
Rails.application.routes.draw do
  # ...
  root "products#index"
  resources :products
end
```

Now when you visit http://localhost:3000, Rails will render Products#index.

### 10.2. Instance Variables

Let's take this a step further and render some records from our database.

In the `index` action, let's add a database query and assign it to an instance variable. Rails uses instance variables (variables that start with an @) to share data with the views.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
    @products = Product.all
  end
end
```

In `app/views/products/index.html.erb`, we can replace the HTML with this ERB:

```erb
<%# app/views/products/index.html.erb %>
<%= debug @products %>
```

ERB is short for Embedded Ruby and allows us to execute Ruby code to dynamically generate HTML with Rails. The `<%= %>` tag tells ERB to execute the Ruby code inside and output the return value. In our case, this takes `@products`, converts it to YAML, and outputs the YAML.

Now refresh http://localhost:3000/ in your browser and you'll see that the output has changed. What you're seeing is the records in your database being displayed in YAML format.

The `debug` helper prints out variables in YAML format to help with debugging. For example, if you weren't paying attention and typed singular `@product` instead of plural `@products`, the debug helper could help you identify that the variable was not set correctly in the controller.

Check out the Action View Helpers guide to see more helpers that are available.

Let's update `app/views/products/index.html.erb` to render all of our product names.

```erb
<%# app/views/products/index.html.erb %>
<h1>Products</h1>

<div id="products">
  <% @products.each do |product| %>
    <div>
      <%= product.name %>
    </div>
  <% end %>
</div>
```

Using ERB, this code loops through each product in the `@products` `ActiveRecord::Relation` object and renders a `<div>` tag containing the product name.

We've used a new ERB tag this time as well. `<% %>` evaluates the Ruby code but does not output the return value. That ignores the output of `@products.each` which would output an array that we don't want in our HTML.

### 10.3. CRUD Actions

We need to be able to access individual products. This is the R in CRUD to read a resource.

We've already defined the route for individual products with our `resources :products` route. This generates `/products/:id` as a route that points to `products#show`.

Now we need to add that action to the `ProductsController` and define what happens when it is called.

### 10.4. Showing Individual Products

Open the Products controller and add the `show` action like this:

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
    @products = Product.all
  end

  def show
    @product = Product.find(params[:id])
  end
end
```

The `show` action here defines the *singular* `@product` because it's loading a single record from the database, in other words: Show this one product. We use plural `@products` in `index` because we're loading multiple products.

To query the database, we use `params` to access the request parameters. In this case, we're using the `:id` from our route `/products/:id`. When we visit `/products/1`, the params hash contains `{id: 1}` which results in our `show` action calling `Product.find(1)` to load Product with ID of `1` from the database.

We need a view for the show action next. Following the Rails naming conventions, the `ProductsController` expects views in `app/views` in a subfolder named `products`.

The `show` action expects a file in `app/views/products/show.html.erb`. Let's create that file in our editor and add the following contents:

```erb
<%# app/views/products/show.html.erb %>
<h1><%= @product.name %></h1>

<%= link_to "Back", products_path %>
```

It would be helpful for the index page to link to the show page for each product so we can click on them to navigate. We can update the `app/views/products/index.html.erb` view to link to this new page to use an anchor tag to the path for the `show` action.

```erb
<%# app/views/products/index.html.erb %>
<h1>Products</h1>

<div id="products">
  <% @products.each do |product| %>
    <div>
      <a href="/products/<%= product.id %>">
        <%= product.name %>
      </a>
    </div>
  <% end %>
</div>
```

Refresh this page in your browser and you'll see that this works, but we can do better.

Rails provides helper methods for generating paths and URLs. When you run `bin/rails routes`, you'll see the Prefix column. This prefix matches the helpers you can use for generating URLs with Ruby code.

```plaintext
  Prefix Verb   URI Pattern             Controller#Action
products GET    /products(.:format)     products#index
 product GET    /products/:id(.:format) products#show
```

These route prefixes give us helpers like the following:

- `products_path` generates `"/products"`
- `products_url` generates `"http://localhost:3000/products"`
- `product_path(1)` generates `"/products/1"`
- `product_url(1)` generates `"http://localhost:3000/products/1"`

`_path` returns a relative path which the browser understands is for the current domain.

`_url` returns a full URL including the protocol, host, and port.

URL helpers are useful for rendering emails that will be viewed outside of the browser.

Combined with the `link_to` helper, we can generate anchor tags and use the URL helper to do this cleanly in Ruby. `link_to` accepts the display content for the link (`product.name`) and the path or URL to link to for the `href` attribute (`product`).

Let's refactor this to use these helpers:

```erb
<%# app/views/products/index.html.erb %>
<h1>Products</h1>

<div id="products">
  <% @products.each do |product| %>
    <div>
      <%= link_to product.name, product_path(product.id) %>
    </div>
  <% end %>
</div>
```

### 10.5. Creating Products

So far we've had to create products in the Rails console, but let's make this work in the browser.

We need to create two actions for create:

1. The new product form to collect product information
2. The create action in the controller to save the product and check for errors

Let's start with our controller actions.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
    @products = Product.all
  end

  def show
    @product = Product.find(params[:id])
  end

  def new
    @product = Product.new
  end
end
```

The `new` action instantiates a new `Product` which we will use for displaying the form fields.

We can update `app/views/products/index.html.erb` to link to the new action.

```erb
<%# app/views/products/index.html.erb %>
<h1>Products</h1>

<%= link_to "New product", new_product_path %>

<div id="products">
  <% @products.each do |product| %>
    <div>
      <%= link_to product.name, product_path(product.id) %>
    </div>
  <% end %>
</div>
```

Let's create `app/views/products/new.html.erb` to render the form for this new `Product`.

```erb
<%# app/views/products/new.html.erb %>
<h1>New product</h1>

<%= form_with model: @product do |form| %>
  <div>
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>

<%= link_to "Cancel", products_path %>
```

In this view, we are using the Rails `form_with` helper to generate an HTML form to create products. This helper uses a *form builder* to handle things like CSRF tokens, generating the URL based upon the `model:` provided, and even tailoring the submit button text to the model.

If you open this page in your browser and View Source, the HTML for the form will look like this:

```html
<form action="/products" accept-charset="UTF-8" method="post">
  <input type="hidden" name="authenticity_token" value="UHQSKXCaFqy_aoK760zpSMUPy6TMnsLNgbPMABwN1zpW-Jx6k-2mISiF0ulZOINmfxPdg5xMyZqdxSW1UK-H-Q" autocomplete="off">

  <div>
    <label for="product_name">Name</label>
    <input type="text" name="product[name]" id="product_name">
  </div>

  <div>
    <input type="submit" name="commit" value="Create Product" data-disable-with="Create Product">
  </div>
</form>
```

The form builder has included a CSRF token for security, configured the form for UTF-8 support, set the input field names and even added a disabled state for the submit button.

Because we passed a new `Product` instance to the form builder, it automatically generated a form configured to send a `POST` request to `/products`, which is the default route for creating a new record.

To handle this, we first need to implement the `create` action in our controller.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
    @products = Product.all
  end

  def show
    @product = Product.find(params[:id])
  end

  def new
    @product = Product.new
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to @product
    else
      render :new, status: :unprocessable_entity
    end
  end

  private
    def product_params
      params.expect(product: [ :name ])
    end
end
```

#### 10.5.1. Strong Parameters

The `create` action handles the data submitted by the form, but it needs to be filtered for security. That's where the `product_params` method comes into play.

In `product_params`, we tell Rails to inspect the params and ensure there is a key named `:product` with an array of parameters as the value. The only permitted parameters for products is `:name` and Rails will ignore any other parameters. This protects our application from malicious users who might try to hack our application.

#### 10.5.2. Handling Errors

After assigning these params to the new `Product`, we can try to save it to the database. `@product.save` tells Active Record to run validations and save the record to the database.

If `save` is successful, we want to redirect to the new product. When `redirect_to` is given an Active Record object, Rails generates a path for that record's show action.

```ruby
redirect_to @product
```

Since `@product` is a `Product` instance, Rails pluralizes the model name and includes the object's ID in the path to produce `"/products/2"` for the redirect.

When `save` is unsuccessful and the record wasn't valid, we want to re-render the form so the user can fix the invalid data. In the `else` clause, we tell Rails to `render :new`. Rails knows we're in the `Products` controller, so it should render `app/views/products/new.html.erb`. Since we've set the `@product` variable in `create`, we can render that template and the form will be populated with our `Product` data even though it wasn't able to be saved in the database.

We also set the HTTP status to 422 Unprocessable Entity to tell the browser this POST request failed and to handle it accordingly.

### 10.6. Editing Products

The process of editing records is very similar to creating records. Instead of `new` and `create` actions, we will have `edit` and `update`.

Let's implement them in the controller with the following:

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  def index
    @products = Product.all
  end

  def show
    @product = Product.find(params[:id])
  end

  def new
    @product = Product.new
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to @product
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
    @product = Product.find(params[:id])
  end

  def update
    @product = Product.find(params[:id])
    if @product.update(product_params)
      redirect_to @product
    else
      render :edit, status: :unprocessable_entity
    end
  end

  private
    def product_params
      params.expect(product: [ :name ])
    end
end
```

#### 10.6.1. Extracting Partials

We've already written a form for creating new products. Wouldn't it be nice if we could reuse that for edit and update? We can, using a feature called "partials" that allows you to reuse a view in multiple places.

We can move the form into a file called `app/views/products/_form.html.erb`. The filename starts with an underscore to denote this is a partial.

We also want to replace any instance variables with a local variable, which we can define when we render the partial. We'll do this by replacing `@product` with `product`.

Let's also display any errors from the form submission inside the form.

```erb
<%# app/views/products/_form.html.erb %>
<%= form_with model: product do |form| %>
  <% if form.object.errors.any? %>
    <p class="error"><%= form.object.errors.full_messages.first %></p>
  <% end %>

  <div>
    <%= form.label :name %>
    <%= form.text_field :name %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

Using local variables allows partials to be reused multiple times on the same page with a different value each time. This comes in handy rendering lists of items like an index page.

To use this partial in our `app/views/products/new.html.erb` view, we can replace the form with a render call:

```erb
<%# app/views/products/new.html.erb %>
<h1>New product</h1>

<%= render "form", product: @product %>
<%= link_to "Cancel", products_path %>
```

The edit view becomes almost the exact same thing thanks to the form partial. Let's create `app/views/products/edit.html.erb` with the following:

```erb
<%# app/views/products/edit.html.erb %>
<h1>Edit product</h1>

<%= render "form", product: @product %>
<%= link_to "Cancel", @product %>
```

To learn more about view partials, check out the Action View Guide.

Now we can add an Edit link to `app/views/products/show.html.erb`:

```erb
<%# app/views/products/show.html.erb %>
<h1><%= @product.name %></h1>

<%= link_to "Back", products_path %>
<%= link_to "Edit", edit_product_path(@product) %>
```

#### 10.6.2. Before Actions

Since `edit` and `update` require an existing database record like `show` we can deduplicate this into a `before_action`.

A `before_action` allows you to extract shared code between actions and run it *before* the action. In the above controller code, `@product = Product.find(params[:id])` is defined in three different methods. Extracting this query to a before action called `set_product` cleans up our code for each action.

This is a good example of the DRY (Don't Repeat Yourself) philosophy in action.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  before_action :set_product, only: %i[ show edit update ]

  def index
    @products = Product.all
  end

  def show
  end

  def new
    @product = Product.new
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to @product
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
  end

  def update
    if @product.update(product_params)
      redirect_to @product
    else
      render :edit, status: :unprocessable_entity
    end
  end

  private
    def set_product
      @product = Product.find(params[:id])
    end

    def product_params
      params.expect(product: [ :name ])
    end
end
```

### 10.7. Deleting Products

The last feature we need to implement is deleting products. We will add a `destroy` action to our `ProductsController` to handle `DELETE /products/:id` requests.

Adding `destroy` to `before_action :set_product` lets us set the `@product` instance variable in the same way we do for the other actions.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  before_action :set_product, only: %i[ show edit update destroy ]

  def index
    @products = Product.all
  end

  def show
  end

  def new
    @product = Product.new
  end

  def create
    @product = Product.new(product_params)
    if @product.save
      redirect_to @product
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
  end

  def update
    if @product.update(product_params)
      redirect_to @product
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @product.destroy
    redirect_to products_path
  end

  private
    def set_product
      @product = Product.find(params[:id])
    end

    def product_params
      params.expect(product: [ :name ])
    end
end
```

To make this work, we need to add a Delete button to `app/views/products/show.html.erb`:

```erb
<%# app/views/products/show.html.erb %>
<h1><%= @product.name %></h1>

<%= link_to "Back", products_path %>
<%= link_to "Edit", edit_product_path(@product) %>
<%= button_to "Delete", @product, method: :delete, data: { turbo_confirm: "Are you sure?" } %>
```

`button_to` generates a form with a single button in it with the "Delete" text. When this button is clicked, it submits the form which makes a `DELETE` request to `/products/:id` which triggers the `destroy` action in our controller.

The `turbo_confirm` data attribute tells the Turbo JavaScript library to ask the user to confirm before submitting the form. We'll dig more into that shortly.


## 11. Adding Authentication

Anyone can edit or delete products which isn't safe. Let's add some security by requiring a user to be authenticated to manage products.

Rails comes with an authentication generator that we can use. It creates User and Session models and the controllers and views necessary to login to our application.

Head back to your terminal and run the following command:

```console
$ bin/rails generate authentication
```

Then migrate the database to add the User and Session tables.

```console
$ bin/rails db:migrate
```

Open the Rails console to create a User.

```console
$ bin/rails console
```

Use `User.create!` method to create a User in the Rails console. Feel free to use your own email and password instead of the example.

```irb
store(dev)> User.create! email_address: "you@example.org", password: "s3cr3t", password_confirmation: "s3cr3t"
```

Restart your Rails server so it picks up the `bcrypt` gem added by the generator. BCrypt is used for securely hashing passwords for authentication.

```console
$ bin/rails server
```

When you visit any page, Rails will prompt for a username and password. Enter the email and password you used when creating the User record.

Try it out by visiting http://localhost:3000/products/new

If you enter the correct username and password, it will allow you through. Your browser will also store these credentials for future requests so you don't have to type it in every page view.

### 11.1. Adding Log Out

To log out of the application, we can add a button to the top of `app/views/layouts/application.html.erb`. This layout is where you put HTML that you want to include in every page like a header or footer.

Add a small `<nav>` section inside the `<body>` with a link to Home and a Log out button and wrap `yield` with a `<main>` tag.

```erb
<%# app/views/layouts/application.html.erb %>
<!DOCTYPE html>
<html>
  <%# ... %>
  <body>
    <nav>
      <%= link_to "Home", root_path %>
      <%= button_to "Log out", session_path, method: :delete if authenticated? %>
    </nav>

    <main>
      <%= yield %>
    </main>
  </body>
</html>
```

This will display a Log out button only if the user is authenticated. When clicked, it will send a DELETE request to the session path which will log the user out.

### 11.2. Allowing Unauthenticated Access

However, our store's product index and show pages should be accessible to everyone. By default, the Rails authentication generator will restrict all pages to authenticated users only.

To allow guests to view products, we can allow unauthenticated access in our controller.

```ruby
# app/controllers/products_controller.rb
class ProductsController < ApplicationController
  allow_unauthenticated_access only: %i[ index show ]
  # ...
end
```

Log out and visit the products index and show pages to see they're accessible without being authenticated.

### 11.3. Showing Links for Authenticated Users Only

Since only logged in users can create products, we can modify the `app/views/products/index.html.erb` view to only display the new product link if the user is authenticated.

```erb
<%# app/views/products/index.html.erb %>
<%= link_to "New product", new_product_path if authenticated? %>
```

Click the Log out button and you'll see the New link is hidden. Log in at http://localhost:3000/session/new and you'll see the New link on the index page.

Optionally, you can include a link to this route in the navbar to add a Login link if not authenticated.

```erb
<%# app/views/products/index.html.erb %>
<%= link_to "Login", new_session_path unless authenticated? %>
```

You can also update the Edit and Delete links on the `app/views/products/show.html.erb` view to only display if authenticated.

```erb
<%# app/views/products/show.html.erb %>
<h1><%= @product.name %></h1>

<%= link_to "Back", products_path %>
<% if authenticated? %>
  <%= link_to "Edit", edit_product_path(@product) %>
  <%= button_to "Delete", @product, method: :delete, data: { turbo_confirm: "Are you sure?" } %>
<% end %>
```


## 12. Caching Products

Sometimes caching specific parts of a page can improve performance. Rails simplifies this process with Solid Cache, a database-backed cache store that comes included by default.

Using the `cache` method, we can store HTML in the cache. Let's cache the header in `app/views/products/show.html.erb`.

```erb
<%# app/views/products/show.html.erb %>
<% cache @product do %>
  <h1><%= @product.name %></h1>
<% end %>
```

By passing `@product` into `cache`, Rails generates a unique cache key for the product. Active Record objects have a `cache_key` method that returns a String like `"products/1"`. The `cache` helper in the views combines this with the template digest to create a unique key for this HTML.

To enable caching in development, run the following command in your terminal.

```console
$ bin/rails dev:cache
```

When you visit a product's show action (like `/products/2`), you'll see the new caching lines in your Rails server logs:

```console
Read fragment views/products/show:a5a585f985894cd27c8b3d49bb81de3a/products/1-20240918154439539125 (1.6ms)
Write fragment views/products/show:a5a585f985894cd27c8b3d49bb81de3a/products/1-20240918154439539125 (4.0ms)
```

The first time we open this page, Rails will generate a cache key and ask the cache store if it exists. This is the `Read fragment` line.

Since this is the first page view, the cache does not exist so the HTML is generated and written to the cache. We can see this as the `Write fragment` line in the logs.

Refresh the page and you'll see the logs no longer contain the `Write fragment`.

```console
Read fragment views/products/show:a5a585f985894cd27c8b3d49bb81de3a/products/1-20240918154439539125 (1.3ms)
```

The cache entry was written by the last request, so Rails finds the cache entry on the second request. Rails also changes the cache key when records are updated to ensure that it never renders stale cache data.

Learn more in the Caching with Rails guide.


## 13. Rich Text Fields with Action Text

Many applications need rich text with embeds (i.e. multimedia elements) and Rails provides this functionality out of the box with Action Text.

To use Action Text, you'll first run the installer:

```console
$ bin/rails action_text:install
$ bundle install
$ bin/rails db:migrate
```

Restart your Rails server to make sure all the new features are loaded.

Now, let's add a rich text description field to our product.

First, add the following to the `Product` model:

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  has_rich_text :description
  validates :name, presence: true
end
```

The form can now be updated to include a rich text field for editing the description in `app/views/products/_form.html.erb` before the submit button.

```erb
<%# app/views/products/_form.html.erb %>
<%= form_with model: product do |form| %>
  <%# ... %>

  <div>
    <%= form.label :description, style: "display: block" %>
    <%= form.rich_textarea :description %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

Our controller also needs to permit this new parameter when the form is submitted, so we'll update the permitted params to include description in `app/controllers/products_controller.rb`

```ruby
# app/controllers/products_controller.rb
    # Only allow a list of trusted parameters through.
    def product_params
      params.expect(product: [ :name, :description ])
    end
```

We also need to update the show view to display the description in `app/views/products/show.html.erb`:

```erb
<%# app/views/products/show.html.erb%>
<% cache @product do %>
  <h1><%= @product.name %></h1>
  <%= @product.description %>
<% end %>
```

The cache key generated by Rails also changes when the view is modified. This makes sure the cache stays in sync with the latest version of the view template.

Create a new product and add a description with bold and italic text. You'll see that the show page displays the formatted text and editing the product retains this rich text in the text area.

Check out the Action Text Overview to learn more.


## 14. File Uploads with Active Storage

Action Text is built upon another feature of Rails called Active Storage that makes it easy to upload files.

Try editing a product and dragging an image into the rich text editor, then update the record. You'll see that Rails uploads this image and renders it inside the rich text editor. Cool, right?!

We can also use Active Storage directly. Let's add a featured image to the `Product` model.

```ruby
# app/models/product.rb
class Product < ApplicationRecord
  has_one_attached :featured_image
  has_rich_text :description
  validates :name, presence: true
end
```

Then we can add a file upload field to our product form before the submit button:

```erb
<%# app/views/products/_form.html.erb %>
<%= form_with model: product do |form| %>
  <%# ... %>

  <div>
    <%= form.label :featured_image, style: "display: block" %>
    <%= form.file_field :featured_image, accept: "image/*" %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

Add `:featured_image` as a permitted parameter in `app/controllers/products_controller.rb`

```ruby
# app/controllers/products_controller.rb
    # Only allow a list of trusted parameters through.
    def product_params
      params.expect(product: [ :name, :description, :featured_image ])
    end
```

Lastly, we want to display the featured image for our product in `app/views/products/show.html.erb`. Add the following to the top.

```erb
<%# app/views/products/show.html.erb %>
<%= image_tag @product.featured_image if @product.featured_image.attached? %>
```

Try uploading an image for a product and you'll see the image displayed on the show page after saving.

Check out the Active Storage Overview for more details.


## 15. Internationalization (I18n)

Rails makes it easy to translate your app into other languages.

The `translate` or `t` helper in our views looks up a translation by name and returns the text for the current locale.

In `app/views/products/index.html.erb`, let's update the header tag to use a translation.

```erb
<%# app/views/products/index.html.erb %>
<h1><%= t "hello" %></h1>
```

Refreshing the page, we see `Hello world` is the header text now. Where did that come from?

Since the default language is in English, Rails looks in `config/locales/en.yml` (which was created during `rails new`) for a matching key under the locale.

```yaml
# config/locales/en.yml
en:
  hello: "Hello world"
```

Let's create a new locale file in our editor for Spanish and add a translation in `config/locales/es.yml`.

```yaml
# config/locales/es.yml
es:
  hello: "Hola mundo"
```

We need to tell Rails which locale to use. The simplest option is to look for a locale param in the URL. We can do this in `app/controllers/application_controller.rb` with the following:

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  # ...

  around_action :switch_locale

  def switch_locale(&action)
    locale = params[:locale] || I18n.default_locale
    I18n.with_locale(locale, &action)
  end
end
```

This will run every request and look for `locale` in the params or fallback to the default locale. It sets the locale for the request and resets it after it's finished.

- Visit http://localhost:3000/products?locale=en, you will see the English translation.
- Visit http://localhost:3000/products?locale=es, you will see the Spanish translation.
- Visit http://localhost:3000/products without a locale param, it will fallback to English.

Let's update the index header to use a real translation instead of `"Hello world"`.

```erb
<%# app/views/products/index.html.erb %>
<h1><%= t ".title" %></h1>
```

Notice the `.` before `title`? This tells Rails to use a relative locale lookup. Relative lookups include the controller and action automatically in the key so you don't have to type them every time. For `.title` with the English locale, it will look up `en.products.index.title`.

In `config/locales/en.yml` we want to add the `title` key under `products` and `index` to match our controller, view, and translation name.

```yaml
# config/locales/en.yml
en:
  hello: "Hello world"
  products:
    index:
      title: "Products"
```

In the Spanish locales file, we can do the same thing:

```yaml
# config/locales/es.yml
es:
  hello: "Hola mundo"
  products:
    index:
      title: "Productos"
```

You'll now see "Products" when viewing the English locale and "Productos" when viewing the Spanish locale.

Learn more about the Rails Internationalization (I18n) API.
