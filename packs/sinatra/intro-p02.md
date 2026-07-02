---
title: "Sinatra: README (part 2/2)"
source: https://sinatrarb.com/intro.html
domain: sinatra
license: CC-BY-SA-4.0
tags: sinatra framework, ruby microframework, rack interface, ruby web dsl
fetched: 2026-07-02
part: 2/2
---

## Error Handling

Error handlers run within the same context as routes and before filters, which means you get all the goodies it has to offer, like `haml`, `erb`, `halt`, etc.

### Not Found

When a `Sinatra::NotFound` exception is raised, or the response’s status code is 404, the `not_found` handler is invoked:

```ruby
not_found do
  'This is nowhere to be found.'
end
```

### Error

The `error` handler is invoked any time an exception is raised from a route block or a filter. But note in development it will only run if you set the show exceptions option to `:after_handler`:

```ruby
set :show_exceptions, :after_handler
```

A catch-all error handler can be defined with `error` and a block:

```ruby
error do
  'Sorry there was a nasty error'
end
```

The exception object can be obtained from the `sinatra.error` Rack variable:

```ruby
error do
  'Sorry there was a nasty error - ' + env['sinatra.error'].message
end
```

Pass an error class as an argument to create handlers for custom errors:

```ruby
error MyCustomError do
  'So what happened was...' + env['sinatra.error'].message
end
```

Then, if this happens:

```ruby
get '/' do
  raise MyCustomError, 'something bad'
end
```

You get this:

```
So what happened was... something bad
```

Alternatively, you can install an error handler for a status code:

```ruby
error 403 do
  'Access forbidden'
end

get '/secret' do
  403
end
```

Or a range:

```ruby
error 400..510 do
  'Boom'
end
```

Sinatra installs special `not_found` and `error` handlers when running under the development environment to display nice stack traces and additional debugging information in your browser.

### Behavior with `raise_errors` option

When `raise_errors` option is `true`, errors that are unhandled are raised outside of the application. Additionally, any errors that would have been caught by the catch-all error handler are raised.

For example, consider the following configuration:

```ruby
# First handler
error MyCustomError do
  'A custom message'
end

# Second handler
error do
  'A catch-all message'
end
```

If `raise_errors` is `false`:

- When `MyCustomError` or descendant is raised, the first handler is invoked. The HTTP response body will contain `"A custom message"`.
- When any other error is raised, the second handler is invoked. The HTTP response body will contain `"A catch-all message"`.

If `raise_errors` is `true`:

- When `MyCustomError` or descendant is raised, the behavior is identical to when `raise_errors` is `false`, described above.
- When any other error is raised, the second handler is *not* invoked, and the error is raised outside of the application.
  - If the environment is `production`, the HTTP response body will contain a generic error message, e.g. `"An unhandled lowlevel error occurred. The application logs may have details."`
  - If the environment is not `production`, the HTTP response body will contain the verbose error backtrace.
  - Regardless of environment, if `show_exceptions` is set to `:after_handler`, the HTTP response body will contain the verbose error backtrace.

In the `test` environment, `raise_errors` is set to `true` by default. This means that in order to write a test for a catch-all error handler, `raise_errors` must temporarily be set to `false` for that particular test.


## Rack Middleware

Sinatra rides on Rack, a minimal standard interface for Ruby web frameworks. One of Rack’s most interesting capabilities for application developers is support for “middleware” – components that sit between the server and your application monitoring and/or manipulating the HTTP request/response to provide various types of common functionality.

Sinatra makes building Rack middleware pipelines a cinch via a top-level `use` method:

```ruby
require 'sinatra'
require 'my_custom_middleware'

use Rack::Lint
use MyCustomMiddleware

get '/hello' do
  'Hello World'
end
```

The semantics of `use` are identical to those defined for the Rack::Builder DSL (most frequently used from rackup files). For example, the `use` method accepts multiple/variable args as well as blocks:

```ruby
use Rack::Auth::Basic do |username, password|
  username == 'admin' && password == 'secret'
end
```

Rack is distributed with a variety of standard middleware for logging, debugging, URL routing, authentication, and session handling. Sinatra uses many of these components automatically based on configuration so you typically don’t have to `use` them explicitly.

You can find useful middleware in rack, rack-contrib, or in the Rack wiki.


## Testing

Sinatra tests can be written using any Rack-based testing library or framework. Rack::Test is recommended:

```ruby
require 'my_sinatra_app'
require 'minitest/autorun'
require 'rack/test'

class MyAppTest < Minitest::Test
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def test_my_default
    get '/'
    assert_equal 'Hello World!', last_response.body
  end

  def test_with_params
    get '/meet', :name => 'Frank'
    assert_equal 'Hello Frank!', last_response.body
  end

  def test_with_user_agent
    get '/', {}, 'HTTP_USER_AGENT' => 'Songbird'
    assert_equal "You're using Songbird!", last_response.body
  end
end
```

Note: If you are using Sinatra in the modular style, replace `Sinatra::Application` above with the class name of your app.


## Sinatra::Base - Middleware, Libraries, and Modular Apps

Defining your app at the top-level works well for micro-apps but has considerable drawbacks when building reusable components such as Rack middleware, Rails metal, simple libraries with a server component, or even Sinatra extensions. The top-level assumes a micro-app style configuration (e.g., a single application file, `./public` and `./views` directories, logging, exception detail page, etc.). That’s where `Sinatra::Base` comes into play:

```ruby
require 'sinatra/base'

class MyApp < Sinatra::Base
  set :sessions, true
  set :foo, 'bar'

  get '/' do
    'Hello world!'
  end
end
```

The methods available to `Sinatra::Base` subclasses are exactly the same as those available via the top-level DSL. Most top-level apps can be converted to `Sinatra::Base` components with two modifications:

- Your file should require `sinatra/base` instead of `sinatra`; otherwise, all of Sinatra’s DSL methods are imported into the main namespace.
- Put your app’s routes, error handlers, filters, and options in a subclass of `Sinatra::Base`.

`Sinatra::Base` is a blank slate. Most options are disabled by default, including the built-in server. See Configuring Settings for details on available options and their behavior. If you want behavior more similar to when you define your app at the top level (also known as Classic style), you can subclass `Sinatra::Application`:

```ruby
require 'sinatra/base'

class MyApp < Sinatra::Application
  get '/' do
    'Hello world!'
  end
end
```

### Modular vs. Classic Style

Contrary to common belief, there is nothing wrong with the classic style. If it suits your application, you do not have to switch to a modular application.

The main disadvantage of using the classic style rather than the modular style is that you will only have one Sinatra application per Ruby process. If you plan to use more than one, switch to the modular style. There is no reason you cannot mix the modular and classic styles.

If switching from one style to the other, you should be aware of slightly different default settings:

| Setting | Classic | Modular | Modular |
|---|---|---|---|
| app_file | file loading sinatra | file subclassing Sinatra::Base | file subclassing Sinatra::Application |
| run | $0 == app_file | false | false |
| logging | true | false | true |
| method_override | true | false | true |
| inline_templates | true | false | true |
| static | true | File.exist?(public_folder) | true |

### Serving a Modular Application

There are two common options for starting a modular app, actively starting with `run!`:

```ruby
# my_app.rb
require 'sinatra/base'

class MyApp < Sinatra::Base
  # ... app code here ...

  # start the server if ruby file executed directly
  run! if app_file == $0
end
```

Start with:

```shell
ruby my_app.rb
```

Or with a `config.ru` file, which allows using any Rack handler:

```ruby
# config.ru (run with rackup)
require './my_app'
run MyApp
```

Run:

```shell
rackup -p 4567
```

### Using a Classic Style Application with a config.ru

Write your app file:

```ruby
# app.rb
require 'sinatra'

get '/' do
  'Hello world!'
end
```

And a corresponding `config.ru`:

```ruby
require './app'
run Sinatra::Application
```

### When to use a config.ru?

A `config.ru` file is recommended if:

- You want to deploy with a different Rack handler (Passenger, Unicorn, Heroku, …).
- You want to use more than one subclass of `Sinatra::Base`.
- You want to use Sinatra only for middleware, and not as an endpoint.

**There is no need to switch to a `config.ru` simply because you switched to the modular style, and you don’t have to use the modular style for running with a `config.ru`.**

### Using Sinatra as Middleware

Not only is Sinatra able to use other Rack middleware, any Sinatra application can, in turn, be added in front of any Rack endpoint as middleware itself. This endpoint could be another Sinatra application, or any other Rack-based application (Rails/Hanami/Roda/…):

```ruby
require 'sinatra/base'

class LoginScreen < Sinatra::Base
  enable :sessions

  get('/login') { haml :login }

  post('/login') do
    if params['name'] == 'admin' && params['password'] == 'admin'
      session['user_name'] = params['name']
    else
      redirect '/login'
    end
  end
end

class MyApp < Sinatra::Base
  # middleware will run before filters
  use LoginScreen

  before do
    unless session['user_name']
      halt "Access denied, please <a href='/login'>login</a>."
    end
  end

  get('/') { "Hello #{session['user_name']}." }
end
```

### Dynamic Application Creation

Sometimes you want to create new applications at runtime without having to assign them to a constant. You can do this with `Sinatra.new`:

```ruby
require 'sinatra/base'
my_app = Sinatra.new { get('/') { "hi" } }
my_app.run!
```

It takes the application to inherit from as an optional argument:

```ruby
# config.ru (run with rackup)
require 'sinatra/base'

controller = Sinatra.new do
  enable :logging
  helpers MyHelpers
end

map('/a') do
  run Sinatra.new(controller) { get('/') { 'a' } }
end

map('/b') do
  run Sinatra.new(controller) { get('/') { 'b' } }
end
```

This is especially useful for testing Sinatra extensions or using Sinatra in your own library.

This also makes using Sinatra as middleware extremely easy:

```ruby
require 'sinatra/base'

use Sinatra do
  get('/') { ... }
end

run RailsProject::Application
```


## Scopes and Binding

The scope you are currently in determines what methods and variables are available.

### Application/Class Scope

Every Sinatra application corresponds to a subclass of `Sinatra::Base`. If you are using the top-level DSL (`require 'sinatra'`), then this class is `Sinatra::Application`, otherwise it is the subclass you created explicitly. At the class level, you have methods like `get` or `before`, but you cannot access the `request` or `session` objects, as there is only a single application class for all requests.

Options created via `set` are methods at class level:

```ruby
class MyApp < Sinatra::Base
  # Hey, I'm in the application scope!
  set :foo, 42
  foo # => 42

  get '/foo' do
    # Hey, I'm no longer in the application scope!
  end
end
```

You have the application scope binding inside:

- Your application class body
- Methods defined by extensions
- The block passed to `helpers`
- Procs/blocks used as a value for `set`
- The block passed to `Sinatra.new`

You can reach the scope object (the class) like this:

- Via the object passed to configure blocks (`configure { |c| ... }`)
- `settings` from within the request scope

### Request/Instance Scope

For every incoming request, a new instance of your application class is created, and all handler blocks run in that scope. From within this scope you can access the `request` and `session` objects or call rendering methods like `erb` or `haml`. You can access the application scope from within the request scope via the `settings` helper:

```ruby
class MyApp < Sinatra::Base
  # Hey, I'm in the application scope!
  get '/define_route/:name' do
    # Request scope for '/define_route/:name'
    @value = 42

    settings.get("/#{params['name']}") do
      # Request scope for "/#{params['name']}"
      @value # => nil (not the same request)
    end

    "Route defined!"
  end
end
```

You have the request scope binding inside:

- get, head, post, put, delete, options, patch, link and unlink blocks
- before and after filters
- helper methods
- templates/views

### Delegation Scope

The delegation scope just forwards methods to the class scope. However, it does not behave exactly like the class scope, as you do not have the class binding. Only methods explicitly marked for delegation are available, and you do not share variables/state with the class scope (read: you have a different `self`). You can explicitly add method delegations by calling `Sinatra::Delegator.delegate :method_name`.

You have the delegate scope binding inside:

- The top-level binding, if you did `require "sinatra"`
- An object extended with the `Sinatra::Delegator` mixin

Have a look at the code for yourself: here’s the Sinatra::Delegator mixin being extending the main object.


## Command Line

Sinatra applications can be run directly:

```shell
ruby myapp.rb [-h] [-x] [-q] [-e ENVIRONMENT] [-p PORT] [-o HOST] [-s HANDLER]
```

Options are:

```
-h # help
-p # set the port (default is 4567)
-o # set the host (default is 0.0.0.0)
-e # set the environment (default is development)
-s # specify rack server/handler (default is puma)
-q # turn on quiet mode for server (default is off)
-x # turn on the mutex lock (default is off)
```

### Multi-threading

*Paraphrasing from this StackOverflow answer by Konstantin*

Sinatra doesn’t impose any concurrency model but leaves that to the underlying Rack handler (server) like Puma or Falcon. Sinatra itself is thread-safe, so there won’t be any problem if the Rack handler uses a threaded model of concurrency.


## Requirement

The following Ruby versions are officially supported:

**Ruby**

The stable releases

are fully supported and recommended.

**TruffleRuby**

The latest stable release of TruffleRuby is supported.

**JRuby**

The latest stable release of JRuby is supported. It is not recommended to use C extensions with JRuby.

Versions of Ruby before 2.7.8 are no longer supported as of Sinatra 4.0.0.

Sinatra should work on any operating system supported by the chosen Ruby implementation.

Running Sinatra on a not officially supported Ruby flavor means that if things only break there we assume it’s not our issue but theirs.


## The Bleeding Edge

If you would like to use Sinatra’s latest bleeding-edge code, feel free to run your application against the main branch, it should be rather stable.

We also push out prerelease gems from time to time, so you can do a

```shell
gem install sinatra --pre
```

to get some of the latest features.

### With Bundler

If you want to run your application with the latest Sinatra, using Bundler is the recommended way.

First, install bundler, if you haven’t:

```shell
gem install bundler
```

Then, in your project directory, create a `Gemfile`:

```ruby
source 'https://rubygems.org'
gem 'sinatra', :github => 'sinatra/sinatra'

# other dependencies
gem 'haml'                    # for instance, if you use haml
```

Note that you will have to list all your application’s dependencies in the `Gemfile`. Sinatra’s direct dependencies (Rack and Tilt) will, however, be automatically fetched and added by Bundler.

Now you can run your app like this:

```shell
bundle exec ruby myapp.rb
```


## Versioning

Sinatra follows Semantic Versioning, both SemVer and SemVerTag.
