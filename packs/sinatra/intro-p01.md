---
title: "Sinatra: README (part 1/2)"
source: https://sinatrarb.com/intro.html
domain: sinatra
license: CC-BY-SA-4.0
tags: sinatra framework, ruby microframework, rack interface, ruby web dsl
fetched: 2026-07-02
part: 1/2
---

# Getting Started

(Gem Version) (Testing)

Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort:

```ruby
# myapp.rb
require 'sinatra'

get '/' do
  'Hello world!'
end
```

Install the gems needed:

```shell
gem install sinatra rackup puma
```

And run with:

```shell
ruby myapp.rb
```

View at: http://localhost:4567

The code you changed will not take effect until you restart the server. Please restart the server every time you change or use a code reloader like rerun or rack-unreloader.

It is recommended to also run `gem install puma`, which Sinatra will pick up if available.


## Routes

In Sinatra, a route is an HTTP method paired with a URL-matching pattern. Each route is associated with a block:

```ruby
get '/' do
  .. show something ..
end

post '/' do
  .. create something ..
end

put '/' do
  .. replace something ..
end

patch '/' do
  .. modify something ..
end

delete '/' do
  .. annihilate something ..
end

options '/' do
  .. appease something ..
end

link '/' do
  .. affiliate something ..
end

unlink '/' do
  .. separate something ..
end
```

Routes are matched in the order they are defined. The first route that matches the request is invoked.

Routes with trailing slashes are different from the ones without:

```ruby
get '/foo' do
  # Does not match "GET /foo/"
end
```

Route patterns may include named parameters, accessible via the `params` hash:

```ruby
get '/hello/:name' do
  # matches "GET /hello/foo" and "GET /hello/bar"
  # params['name'] is 'foo' or 'bar'
  "Hello #{params['name']}!"
end
```

You can also access named parameters via block parameters:

```ruby
get '/hello/:name' do |n|
  # matches "GET /hello/foo" and "GET /hello/bar"
  # params['name'] is 'foo' or 'bar'
  # n stores params['name']
  "Hello #{n}!"
end
```

Route patterns may also include splat (or wildcard) parameters, accessible via the `params['splat']` array:

```ruby
get '/say/*/to/*' do
  # matches /say/hello/to/world
  params['splat'] # => ["hello", "world"]
end

get '/download/*.*' do
  # matches /download/path/to/file.xml
  params['splat'] # => ["path/to/file", "xml"]
end
```

Or with block parameters:

```ruby
get '/download/*.*' do |path, ext|
  [path, ext] # => ["path/to/file", "xml"]
end
```

Route matching with Regular Expressions:

```ruby
get /\/hello\/([\w]+)/ do
  "Hello, #{params['captures'].first}!"
end
```

Or with a block parameter:

```ruby
get %r{/hello/([\w]+)} do |c|
  # Matches "GET /meta/hello/world", "GET /hello/world/1234" etc.
  "Hello, #{c}!"
end
```

Route patterns may have optional parameters:

```ruby
get '/posts/:format?' do
  # matches "GET /posts/" and any extension "GET /posts/json", "GET /posts/xml" etc
end
```

Routes may also utilize query parameters:

```ruby
get '/posts' do
  # matches "GET /posts?title=foo&author=bar"
  title = params['title']
  author = params['author']
  # uses title and author variables; query is optional to the /posts route
end
```

By the way, unless you disable the path traversal attack protection (see below), the request path might be modified before matching against your routes.

You may customize the Mustermann options used for a given route by passing in a `:mustermann_opts` hash:

```ruby
get '\A/posts\z', :mustermann_opts => { :type => :regexp, :check_anchors => false } do
  # matches /posts exactly, with explicit anchoring
  "If you match an anchored pattern clap your hands!"
end
```

It looks like a condition, but it isn’t one! These options will be merged into the global `:mustermann_opts` hash described below.


## Conditions

Routes may include a variety of matching conditions, such as the user agent:

```ruby
get '/foo', :agent => /Songbird (\d\.\d)[\d\/]*?/ do
  "You're using Songbird version #{params['agent'][0]}"
end

get '/foo' do
  # Matches non-songbird browsers
end
```

Other available conditions are `host_name` and `provides`:

```ruby
get '/', :host_name => /^admin\./ do
  "Admin Area, Access denied!"
end

get '/', :provides => 'html' do
  haml :index
end

get '/', :provides => ['rss', 'atom', 'xml'] do
  builder :feed
end
```

`provides` searches the request’s Accept header.

You can easily define your own conditions:

```ruby
set(:probability) { |value| condition { rand <= value } }

get '/win_a_car', :probability => 0.1 do
  "You won!"
end

get '/win_a_car' do
  "Sorry, you lost."
end
```

For a condition that takes multiple values use a splat:

```ruby
set(:auth) do |*roles|   # <- notice the splat here
  condition do
    unless logged_in? && roles.any? {|role| current_user.in_role? role }
      redirect "/login/", 303
    end
  end
end

get "/my/account/", :auth => [:user, :admin] do
  "Your Account Details"
end

get "/only/admin/", :auth => :admin do
  "Only admins are allowed here!"
end
```


## Return Values

The return value of a route block determines at least the response body passed on to the HTTP client or at least the next middleware in the Rack stack. Most commonly, this is a string, as in the above examples. But other values are also accepted.

You can return an object that would either be a valid Rack response, Rack body object or HTTP status code:

- An Array with three elements: `[status (Integer), headers (Hash), response body (responds to #each)]`
- An Array with two elements: `[status (Integer), response body (responds to #each)]`
- An object that responds to `#each` and passes nothing but strings to the given block
- A Integer representing the status code

That way we can, for instance, easily implement a streaming example:

```ruby
class Stream
  def each
    100.times { |i| yield "#{i}\n" }
  end
end

get('/') { Stream.new }
```

You can also use the `stream` helper method (described below) to reduce boilerplate and embed the streaming logic in the route.


## Custom Route Matchers

As shown above, Sinatra ships with built-in support for using String patterns and regular expressions as route matches. However, it does not stop there. You can easily define your own matchers:

```ruby
class AllButPattern
  def initialize(except)
    @except = except
  end

  def to_pattern(options)
    return self
  end

  def params(route)
    return {} unless @except === route
  end
end

def all_but(pattern)
  AllButPattern.new(pattern)
end

get all_but("/index") do
  # ...
end
```

Note that the above example might be over-engineered, as it can also be expressed as:

```ruby
get /.*/ do
  pass if request.path_info == "/index"
  # ...
end
```


## Static Files

Static files are served from the `./public` directory. You can specify a different location by setting the `:public_folder` option:

```ruby
set :public_folder, __dir__ + '/static'
```

Note that the public directory name is not included in the URL. A file `./public/css/style.css` is made available as `http://example.com/css/style.css`.

Use the `:static_cache_control` setting (see below) to add `Cache-Control` header info.


## Views / Templates

Each template language is exposed via its own rendering method. These methods simply return a string:

```ruby
get '/' do
  erb :index
end
```

This renders `views/index.erb`.

Instead of a template name, you can also just pass in the template content directly:

```ruby
get '/' do
  code = "<%= Time.now %>"
  erb code
end
```

Templates take a second argument, the options hash:

```ruby
get '/' do
  erb :index, :layout => :post
end
```

This will render `views/index.erb` embedded in the `views/post.erb` (default is `views/layout.erb`, if it exists).

Any options not understood by Sinatra will be passed on to the template engine:

```ruby
get '/' do
  haml :index, :format => :html5
end
```

You can also set options per template language in general:

```ruby
set :haml, :format => :html5

get '/' do
  haml :index
end
```

Options passed to the render method override options set via `set`.

Available Options:

**locals**

List of locals passed to the document. Handy with partials. Example:

erb "<%= foo %>", :locals => {:foo => "bar"}

**default_encoding**

String encoding to use if uncertain. Defaults to

settings.default_encoding

.

**views**

Views folder to load templates from. Defaults to

settings.views

.

**layout**

Whether to use a layout (

true

or

false

). If it's a Symbol, specifies what template to use. Example:

erb :index, :layout => !request.xhr?

**content_type**

Content-Type the template produces. Default depends on template language.

**scope**

Scope to render template under. Defaults to the application instance. If you change this, instance variables and helper methods will not be available.

**layout_engine**

Template engine to use for rendering the layout. Useful for languages that do not support layouts otherwise. Defaults to the engine used for the template. Example:

set :rdoc, :layout_engine => :erb

**layout_options**

Special options only used for rendering the layout. Example:

set :rdoc, :layout_options => { :views => 'views/layouts' }

Templates are assumed to be located directly under the `./views` directory. To use a different views directory:

```ruby
set :views, settings.root + '/templates'
```

One important thing to remember is that you always have to reference templates with symbols, even if they’re in a subdirectory (in this case, use: `:'subdir/template'` or `'subdir/template'.to_sym`). You must use a symbol because otherwise rendering methods will render any strings passed to them directly.

### Literal Templates

```ruby
get '/' do
  haml '%div.title Hello World'
end
```

Renders the template string. You can optionally specify `:path` and `:line` for a clearer backtrace if there is a filesystem path or line associated with that string:

```ruby
get '/' do
  haml '%div.title Hello World', :path => 'examples/file.haml', :line => 3
end
```

### Available Template Languages

Some languages have multiple implementations. To specify what implementation to use (and to be thread-safe), you should simply require it first:

```ruby
require 'rdiscount'
get('/') { markdown :index }
```

#### Haml Templates

| Dependency | haml |
|---|---|
| File Extension | .haml |
| Example | haml :index, :format => :html5 |

#### Erb Templates

| Dependency | erubi or erb (included in Ruby) |
|---|---|
| File Extensions | .erb, .rhtml or .erubi (Erubi only) |
| Example | erb :index |

#### Builder Templates

| Dependency | builder |
|---|---|
| File Extension | .builder |
| Example | builder { \|xml\| xml.em "hi" } |

It also takes a block for inline templates (see example).

#### Nokogiri Templates

| Dependency | nokogiri |
|---|---|
| File Extension | .nokogiri |
| Example | nokogiri { \|xml\| xml.em "hi" } |

It also takes a block for inline templates (see example).

#### Sass Templates

| Dependency | sass-embedded |
|---|---|
| File Extension | .sass |
| Example | sass :stylesheet, :style => :expanded |

#### Scss Templates

| Dependency | sass-embedded |
|---|---|
| File Extension | .scss |
| Example | scss :stylesheet, :style => :expanded |

#### Liquid Templates

| Dependency | liquid |
|---|---|
| File Extension | .liquid |
| Example | liquid :index, :locals => { :key => 'value' } |

Since you cannot call Ruby methods (except for `yield`) from a Liquid template, you almost always want to pass locals to it.

#### Markdown Templates

| Dependency | Anyone of: RDiscount, RedCarpet, kramdown, commonmarker pandoc |
|---|---|
| File Extensions | .markdown, .mkd and .md |
| Example | markdown :index, :layout_engine => :erb |

It is not possible to call methods from Markdown, nor to pass locals to it. You therefore will usually use it in combination with another rendering engine:

```ruby
erb :overview, :locals => { :text => markdown(:introduction) }
```

Note that you may also call the `markdown` method from within other templates:

```ruby
%h1 Hello From Haml!
%p= markdown(:greetings)
```

Since you cannot call Ruby from Markdown, you cannot use layouts written in Markdown. However, it is possible to use another rendering engine for the template than for the layout by passing the `:layout_engine` option.

#### RDoc Templates

| Dependency | RDoc |
|---|---|
| File Extension | .rdoc |
| Example | rdoc :README, :layout_engine => :erb |

It is not possible to call methods from RDoc, nor to pass locals to it. You therefore will usually use it in combination with another rendering engine:

```ruby
erb :overview, :locals => { :text => rdoc(:introduction) }
```

Note that you may also call the `rdoc` method from within other templates:

```ruby
%h1 Hello From Haml!
%p= rdoc(:greetings)
```

Since you cannot call Ruby from RDoc, you cannot use layouts written in RDoc. However, it is possible to use another rendering engine for the template than for the layout by passing the `:layout_engine` option.

#### AsciiDoc Templates

| Dependency | Asciidoctor |
|---|---|
| File Extension | .asciidoc, .adoc and .ad |
| Example | asciidoc :README, :layout_engine => :erb |

Since you cannot call Ruby methods directly from an AsciiDoc template, you almost always want to pass locals to it.

#### Markaby Templates

| Dependency | Markaby |
|---|---|
| File Extension | .mab |
| Example | markaby { h1 "Welcome!" } |

It also takes a block for inline templates (see example).

#### RABL Templates

| Dependency | Rabl |
|---|---|
| File Extension | .rabl |
| Example | rabl :index |

#### Slim Templates

| Dependency | Slim Lang |
|---|---|
| File Extension | .slim |
| Example | slim :index |

#### Yajl Templates

| Dependency | yajl-ruby |
|---|---|
| File Extension | .yajl |
| Example | yajl :index, :locals => { :key => 'qux' }, :callback => 'present', :variable => 'resource' |

The template source is evaluated as a Ruby string, and the resulting json variable is converted using `#to_json`:

```ruby
json = { :foo => 'bar' }
json[:baz] = key
```

The `:callback` and `:variable` options can be used to decorate the rendered object:

```javascript
var resource = {"foo":"bar","baz":"qux"};
present(resource);
```

### Accessing Variables in Templates

Templates are evaluated within the same context as route handlers. Instance variables set in route handlers are directly accessible by templates:

```ruby
get '/:id' do
  @foo = Foo.find(params['id'])
  haml '%h1= @foo.name'
end
```

Or, specify an explicit Hash of local variables:

```ruby
get '/:id' do
  foo = Foo.find(params['id'])
  haml '%h1= bar.name', :locals => { :bar => foo }
end
```

This is typically used when rendering templates as partials from within other templates.

### Templates with `yield` and nested layouts

A layout is usually just a template that calls `yield`. Such a template can be used either through the `:template` option as described above, or it can be rendered with a block as follows:

```ruby
erb :post, :layout => false do
  erb :index
end
```

This code is mostly equivalent to `erb :index, :layout => :post`.

Passing blocks to rendering methods is most useful for creating nested layouts:

```ruby
erb :main_layout, :layout => false do
  erb :admin_layout do
    erb :user
  end
end
```

This can also be done in fewer lines of code with:

```ruby
erb :admin_layout, :layout => :main_layout do
  erb :user
end
```

Currently, the following rendering methods accept a block: `erb`, `haml`, `liquid`, `slim`. Also, the general `render` method accepts a block.

### Inline Templates

Templates may be defined at the end of the source file:

```ruby
require 'sinatra'

get '/' do
  haml :index
end

__END__

@@ layout
%html
  != yield

@@ index
%div.title Hello world.
```

NOTE: Inline templates defined in the source file that requires Sinatra are automatically loaded. Call `enable :inline_templates` explicitly if you have inline templates in other source files.

### Named Templates

Templates may also be defined using the top-level `template` method:

```ruby
template :layout do
  "%html\n  =yield\n"
end

template :index do
  '%div.title Hello World!'
end

get '/' do
  haml :index
end
```

If a template named “layout” exists, it will be used each time a template is rendered. You can individually disable layouts by passing `:layout => false` or disable them by default via `set :haml, :layout => false`:

```ruby
get '/' do
  haml :index, :layout => !request.xhr?
end
```

### Associating File Extensions

To associate a file extension with a template engine, use `Tilt.register`. For instance, if you like to use the file extension `tt` for Haml templates, you can do the following:

```ruby
Tilt.register Tilt[:haml], :tt
```

### Adding Your Own Template Engine

First, register your engine with Tilt, then create a rendering method:

```ruby
Tilt.register MyAwesomeTemplateEngine, :myat

helpers do
  def myat(*args) render(:myat, *args) end
end

get '/' do
  myat :index
end
```

Renders `./views/index.myat`. Learn more about Tilt.

### Using Custom Logic for Template Lookup

To implement your own template lookup mechanism you can write your own `#find_template` method:

```ruby
configure do
  set :views, [ './views/a', './views/b' ]
end

def find_template(views, name, engine, &block)
  Array(views).each do |v|
    super(v, name, engine, &block)
  end
end
```


## Filters

Before filters are evaluated before each request within the same context as the routes will be and can modify the request and response. Instance variables set in filters are accessible by routes and templates:

```ruby
before do
  @note = 'Hi!'
  request.path_info = '/foo/bar/baz'
end

get '/foo/*' do
  @note #=> 'Hi!'
  params['splat'] #=> 'bar/baz'
end
```

After filters are evaluated after each request within the same context as the routes will be and can also modify the request and response. Instance variables set in before filters and routes are accessible by after filters:

```ruby
after do
  puts response.status
end
```

Note: Unless you use the `body` method rather than just returning a String from the routes, the body will not yet be available in the after filter, since it is generated later on.

Filters optionally take a pattern, causing them to be evaluated only if the request path matches that pattern:

```ruby
before '/protected/*' do
  authenticate!
end

after '/create/:slug' do |slug|
  session[:last_slug] = slug
end
```

Like routes, filters also take conditions:

```ruby
before :agent => /Songbird/ do
  # ...
end

after '/blog/*', :host_name => 'example.com' do
  # ...
end
```


## Helpers

Use the top-level `helpers` method to define helper methods for use in route handlers and templates:

```ruby
helpers do
  def bar(name)
    "#{name}bar"
  end
end

get '/:name' do
  bar(params['name'])
end
```

Alternatively, helper methods can be separately defined in a module:

```ruby
module FooUtils
  def foo(name) "#{name}foo" end
end

module BarUtils
  def bar(name) "#{name}bar" end
end

helpers FooUtils, BarUtils
```

The effect is the same as including the modules in the application class.

### Using Sessions

A session is used to keep state during requests. If activated, you have one session hash per user session:

```ruby
enable :sessions

get '/' do
  "value = " << session[:value].inspect
end

get '/:value' do
  session['value'] = params['value']
end
```

#### Session Secret Security

To improve security, the session data in the cookie is signed with a session secret using `HMAC-SHA1`. This session secret should optimally be a cryptographically secure random value of an appropriate length which for `HMAC-SHA1` is greater than or equal to 64 bytes (512 bits, 128 hex characters). You would be advised not to use a secret that is less than 32 bytes of randomness (256 bits, 64 hex characters). It is therefore **very important** that you don’t just make the secret up, but instead use a secure random number generator to create it. Humans are extremely bad at generating random values.

By default, a 32 byte secure random session secret is generated for you by Sinatra, but it will change with every restart of your application. If you have multiple instances of your application, and you let Sinatra generate the key, each instance would then have a different session key which is probably not what you want.

For better security and usability it’s recommended that you generate a secure random secret and store it in an environment variable on each host running your application so that all of your application instances will share the same secret. You should periodically rotate this session secret to a new value. Here are some examples of how you might create a 64-byte secret and set it:

**Session Secret Generation**

```text
$ ruby -e "require 'securerandom'; puts SecureRandom.hex(64)"
99ae8af...snip...ec0f262ac
```

**Session Secret Environment Variable**

Set a `SESSION_SECRET` environment variable for Sinatra to the value you generated. Make this value persistent across reboots of your host. Since the method for doing this will vary across systems this is for illustrative purposes only:

```bash
# echo "export SESSION_SECRET=99ae8af...snip...ec0f262ac" >> ~/.bashrc
```

**Session Secret App Config**

Set up your app config to fail-safe to a secure random secret if the `SESSION_SECRET` environment variable is not available:

```ruby
require 'securerandom'
set :session_secret, ENV.fetch('SESSION_SECRET') { SecureRandom.hex(64) }
```

#### Session Config

If you want to configure it further, you may also store a hash with options in the `sessions` setting:

```ruby
set :sessions, :domain => 'foo.com'
```

To share your session across other apps on subdomains of foo.com, prefix the domain with a *.* like this instead:

```ruby
set :sessions, :domain => '.foo.com'
```

#### Choosing Your Own Session Middleware

Note that `enable :sessions` actually stores all data in a cookie. This might not always be what you want (storing lots of data will increase your traffic, for instance). You can use any Rack session middleware in order to do so, one of the following methods can be used:

```ruby
enable :sessions
set :session_store, Rack::Session::Pool
```

Or to set up sessions with a hash of options:

```ruby
set :sessions, :expire_after => 2592000
set :session_store, Rack::Session::Pool
```

Another option is to **not** call `enable :sessions`, but instead pull in your middleware of choice as you would any other middleware.

It is important to note that when using this method, session based protection **will not be enabled by default**.

The Rack middleware to do that will also need to be added:

```ruby
use Rack::Session::Pool, :expire_after => 2592000
use Rack::Protection::RemoteToken
use Rack::Protection::SessionHijacking
```

See ‘Configuring attack protection’ for more information.

### Halting

To immediately stop a request within a filter or route use:

```ruby
halt
```

You can also specify the status when halting:

```ruby
halt 410
```

Or the body:

```ruby
halt 'this will be the body'
```

Or both:

```ruby
halt 401, 'go away!'
```

With headers:

```ruby
halt 402, {'Content-Type' => 'text/plain'}, 'revenge'
```

It is of course possible to combine a template with `halt`:

```ruby
halt erb(:error)
```

### Passing

A route can punt processing to the next matching route using `pass`:

```ruby
get '/guess/:who' do
  pass unless params['who'] == 'Frank'
  'You got me!'
end

get '/guess/*' do
  'You missed!'
end
```

The route block is immediately exited and control continues with the next matching route. If no matching route is found, a 404 is returned.

### Triggering Another Route

Sometimes `pass` is not what you want, instead, you would like to get the result of calling another route. Simply use `call` to achieve this:

```ruby
get '/foo' do
  status, headers, body = call env.merge("PATH_INFO" => '/bar')
  [status, headers, body.map(&:upcase)]
end

get '/bar' do
  "bar"
end
```

Note that in the example above, you would ease testing and increase performance by simply moving `"bar"` into a helper used by both `/foo` and `/bar`.

If you want the request to be sent to the same application instance rather than a duplicate, use `call!` instead of `call`.

Check out the Rack specification if you want to learn more about `call`.

### Setting Body, Status Code, and Headers

It is possible and recommended to set the status code and response body with the return value of the route block. However, in some scenarios, you might want to set the body at an arbitrary point in the execution flow. You can do so with the `body` helper method. If you do so, you can use that method from thereon to access the body:

```ruby
get '/foo' do
  body "bar"
end

after do
  puts body
end
```

It is also possible to pass a block to `body`, which will be executed by the Rack handler (this can be used to implement streaming, see “Return Values”).

Similar to the body, you can also set the status code and headers:

```ruby
get '/foo' do
  status 418
  headers \
    "Allow"   => "BREW, POST, GET, PROPFIND, WHEN",
    "Refresh" => "Refresh: 20; https://ietf.org/rfc/rfc2324.txt"
  body "I'm a teapot!"
end
```

Like `body`, `headers` and `status` with no arguments can be used to access their current values.

### Streaming Responses

Sometimes you want to start sending out data while still generating parts of the response body. In extreme examples, you want to keep sending data until the client closes the connection. You can use the `stream` helper to avoid creating your own wrapper:

```ruby
get '/' do
  stream do |out|
    out << "It's gonna be legen -\n"
    sleep 0.5
    out << " (wait for it) \n"
    sleep 1
    out << "- dary!\n"
  end
end
```

This allows you to implement streaming APIs, Server Sent Events, and can be used as the basis for WebSockets. It can also be used to increase throughput if some but not all content depends on a slow resource.

Note that the streaming behavior, especially the number of concurrent requests, highly depends on the webserver used to serve the application. Some servers might not even support streaming at all. If the server does not support streaming, the body will be sent all at once after the block passed to `stream` finishes executing. Streaming does not work at all with Shotgun.

If the optional parameter is set to `keep_open`, it will not call `close` on the stream object, allowing you to close it at any later point in the execution flow.

You can have a look at the chat example

It’s also possible for the client to close the connection when trying to write to the socket. Because of this, it’s recommended to check `out.closed?` before trying to write.

### Logging

In the request scope, the `logger` helper exposes a `Logger` instance:

```ruby
get '/' do
  logger.info "loading data"
  # ...
end
```

This logger will automatically take your Rack handler’s logging settings into account. If logging is disabled, this method will return a dummy object, so you do not have to worry about it in your routes and filters.

Note that logging is only enabled for `Sinatra::Application` by default, so if you inherit from `Sinatra::Base`, you probably want to enable it yourself:

```ruby
class MyApp < Sinatra::Base
  configure :production, :development do
    enable :logging
  end
end
```

To avoid any logging middleware to be set up, set the `logging` option to `nil`. However, keep in mind that `logger` will in that case return `nil`. A common use case is when you want to set your own logger. Sinatra will use whatever it will find in `env['rack.logger']`.

### Mime Types

When using `send_file` or static files you may have mime types Sinatra doesn’t understand. Use `mime_type` to register them by file extension:

```ruby
configure do
  mime_type :foo, 'text/foo'
end
```

You can also use it with the `content_type` helper:

```ruby
get '/' do
  content_type :foo
  "foo foo foo"
end
```

### Generating URLs

For generating URLs you should use the `url` helper method, for instance, in Haml:

```ruby
%a{:href => url('/foo')} foo
```

It takes reverse proxies and Rack routers into account - if present.

This method is also aliased to `to` (see below for an example).

### Browser Redirect

You can trigger a browser redirect with the `redirect` helper method:

```ruby
get '/foo' do
  redirect to('/bar')
end
```

Any additional parameters are handled like arguments passed to `halt`:

```ruby
redirect to('/bar'), 303
redirect 'http://www.google.com/', 'wrong place, buddy'
```

You can also easily redirect back to the page the user came from with `redirect back`:

```ruby
get '/foo' do
  "<a href='/bar'>do something</a>"
end

get '/bar' do
  do_something
  redirect back
end
```

To pass arguments with a redirect, either add them to the query:

```ruby
redirect to('/bar?sum=42')
```

Or use a session:

```ruby
enable :sessions

get '/foo' do
  session[:secret] = 'foo'
  redirect to('/bar')
end

get '/bar' do
  session[:secret]
end
```

### Cache Control

Setting your headers correctly is the foundation for proper HTTP caching.

You can easily set the Cache-Control header like this:

```ruby
get '/' do
  cache_control :public
  "cache it!"
end
```

Pro tip: Set up caching in a before filter:

```ruby
before do
  cache_control :public, :must_revalidate, :max_age => 60
end
```

If you are using the `expires` helper to set the corresponding header, `Cache-Control` will be set automatically for you:

```ruby
before do
  expires 500, :public, :must_revalidate
end
```

To properly use caches, you should consider using `etag` or `last_modified`. It is recommended to call those helpers *before* doing any heavy lifting, as they will immediately flush a response if the client already has the current version in its cache:

```ruby
get "/article/:id" do
  @article = Article.find params['id']
  last_modified @article.updated_at
  etag @article.sha1
  erb :article
end
```

It is also possible to use a weak ETag:

```ruby
etag @article.sha1, :weak
```

These helpers will not do any caching for you, but rather feed the necessary information to your cache. If you are looking for a quick reverse-proxy caching solution, try rack-cache:

```ruby
require "rack/cache"
require "sinatra"

use Rack::Cache

get '/' do
  cache_control :public, :max_age => 36000
  sleep 5
  "hello"
end
```

Use the `:static_cache_control` setting (see below) to add `Cache-Control` header info to static files.

According to RFC 2616, your application should behave differently if the If-Match or If-None-Match header is set to `*`, depending on whether the resource requested is already in existence. Sinatra assumes resources for safe (like get) and idempotent (like put) requests are already in existence, whereas other resources (for instance post requests) are treated as new resources. You can change this behavior by passing in a `:new_resource` option:

```ruby
get '/create' do
  etag '', :new_resource => true
  Article.create
  erb :new_article
end
```

If you still want to use a weak ETag, pass in a `:kind` option:

```ruby
etag '', :new_resource => true, :kind => :weak
```

### Sending Files

To return the contents of a file as the response, you can use the `send_file` helper method:

```ruby
get '/' do
  send_file 'foo.png'
end
```

It also takes options:

```ruby
send_file 'foo.png', :type => :jpg
```

The options are:

**filename**

File name to be used in the response, defaults to the real file name.

**last_modified**

Value for Last-Modified header, defaults to the file's mtime.

**type**

Value for Content-Type header, guessed from the file extension if missing.

**disposition**

Value for Content-Disposition header, possible values:

nil

(default),

:attachment

and

:inline

**length**

Value for Content-Length header, defaults to file size.

**status**

Status code to be sent. Useful when sending a static file as an error page. If supported by the Rack handler, other means than streaming from the Ruby process will be used. If you use this helper method, Sinatra will automatically handle range requests.

### Accessing the Request Object

The incoming request object can be accessed from request level (filter, routes, error handlers) through the `request` method:

```ruby
# app running on http://example.com/example
get '/foo' do
  t = %w[text/css text/html application/javascript]
  request.accept              # ['text/html', '*/*']
  request.accept? 'text/xml'  # true
  request.preferred_type(t)   # 'text/html'
  request.body                # request body sent by the client (see below)
  request.scheme              # "http"
  request.script_name         # "/example"
  request.path_info           # "/foo"
  request.port                # 80
  request.request_method      # "GET"
  request.query_string        # ""
  request.content_length      # length of request.body
  request.media_type          # media type of request.body
  request.host                # "example.com"
  request.get?                # true (similar methods for other verbs)
  request.form_data?          # false
  request["some_param"]       # value of some_param parameter. [] is a shortcut to the params hash.
  request.referrer            # the referrer of the client or '/'
  request.user_agent          # user agent (used by :agent condition)
  request.cookies             # hash of browser cookies
  request.xhr?                # is this an ajax request?
  request.url                 # "http://example.com/example/foo"
  request.path                # "/example/foo"
  request.ip                  # client IP address
  request.secure?             # false (would be true over ssl)
  request.forwarded?          # true (if running behind a reverse proxy)
  request.env                 # raw env hash handed in by Rack
end
```

Some options, like `script_name` or `path_info`, can also be written:

```ruby
before { request.path_info = "/" }

get "/" do
  "all requests end up here"
end
```

The `request.body` is an IO or StringIO object:

```ruby
post "/api" do
  request.body.rewind  # in case someone already read it
  data = JSON.parse request.body.read
  "Hello #{data['name']}!"
end
```

### Attachments

You can use the `attachment` helper to tell the browser the response should be stored on disk rather than displayed in the browser:

```ruby
get '/' do
  attachment
  "store it!"
end
```

You can also pass it a file name:

```ruby
get '/' do
  attachment "info.txt"
  "store it!"
end
```

### Dealing with Date and Time

Sinatra offers a `time_for` helper method that generates a Time object from the given value. It is also able to convert `DateTime`, `Date` and similar classes:

```ruby
get '/' do
  pass if Time.now > time_for('Dec 23, 2016')
  "still time"
end
```

This method is used internally by `expires`, `last_modified` and akin. You can therefore easily extend the behavior of those methods by overriding `time_for` in your application:

```ruby
helpers do
  def time_for(value)
    case value
    when :yesterday then Time.now - 24*60*60
    when :tomorrow  then Time.now + 24*60*60
    else super
    end
  end
end

get '/' do
  last_modified :yesterday
  expires :tomorrow
  "hello"
end
```

### Looking Up Template Files

The `find_template` helper is used to find template files for rendering:

```ruby
find_template settings.views, 'foo', Tilt[:haml] do |file|
  puts "could be #{file}"
end
```

This is not really useful. But it is useful that you can actually override this method to hook in your own lookup mechanism. For instance, if you want to be able to use more than one view directory:

```ruby
set :views, ['views', 'templates']

helpers do
  def find_template(views, name, engine, &block)
    Array(views).each { |v| super(v, name, engine, &block) }
  end
end
```

Another example would be using different directories for different engines:

```ruby
set :views, :haml => 'templates', :default => 'views'

helpers do
  def find_template(views, name, engine, &block)
    _, folder = views.detect { |k,v| engine == Tilt[k] }
    folder ||= views[:default]
    super(folder, name, engine, &block)
  end
end
```

You can also easily wrap this up in an extension and share it with others!

Note that `find_template` does not check if the file really exists but rather calls the given block for all possible paths. This is not a performance issue, since `render` will use `break` as soon as a file is found. Also, template locations (and content) will be cached if you are not running in development mode. You should keep that in mind if you write a really crazy method.


## Configuration

Run once, at startup, in any environment:

```ruby
configure do
  # setting one option
  set :option, 'value'

  # setting multiple options
  set :a => 1, :b => 2

  # same as `set :option, true`
  enable :option

  # same as `set :option, false`
  disable :option

  # you can also have dynamic settings with blocks
  set(:css_dir) { File.join(views, 'css') }
end
```

Run only when the environment (`APP_ENV` environment variable) is set to `:production`:

```ruby
configure :production do
  ...
end
```

Run when the environment is set to either `:production` or `:test`:

```ruby
configure :production, :test do
  ...
end
```

You can access those options via `settings`:

```ruby
configure do
  set :foo, 'bar'
end

get '/' do
  settings.foo? # => true
  settings.foo  # => 'bar'
  ...
end
```

### Configuring attack protection

Sinatra is using Rack::Protection to defend your application against common, opportunistic attacks. You can easily disable this behavior (which will open up your application to tons of common vulnerabilities):

```ruby
disable :protection
```

To skip a single defense layer, set `protection` to an options hash:

```ruby
set :protection, :except => :path_traversal
```

You can also hand in an array in order to disable a list of protections:

```ruby
set :protection, :except => [:path_traversal, :remote_token]
```

By default, Sinatra will only set up session based protection if `:sessions` have been enabled. See ‘Using Sessions’. Sometimes you may want to set up sessions “outside” of the Sinatra app, such as in the config.ru or with a separate `Rack::Builder` instance. In that case, you can still set up session based protection by passing the `:session` option:

```ruby
set :protection, :session => true
```

### Available Settings

**absolute_redirects**

If disabled, Sinatra will allow relative redirects, however, Sinatra will no longer conform with RFC 2616 (HTTP 1.1), which only allows absolute redirects.

Enable if your app is running behind a reverse proxy that has not been set up properly. Note that the

url

helper will still produce absolute URLs, unless you pass in

false

as the second parameter.

Disabled by default.

**add_charset**

Mime types the

content_type

helper will automatically add the charset info to. You should add to it rather than overriding this option:

settings.add_charset << "application/foobar"

**app_file**

Path to the main application file, used to detect project root, views and public folder and inline templates.

**bind**

IP address to bind to (default:

0.0.0.0

or

localhost

if your `environment` is set to development). Only used for built-in server.

**default_content_type**

Content-Type to assume if unknown (defaults to

"text/html"

). Set to

nil

to not set a default Content-Type on every response; when configured so, you must set the Content-Type manually when emitting content or the user-agent will have to sniff it (or, if

nosniff

is enabled in Rack::Protection::XSSHeader, assume

application/octet-stream

).

**default_encoding**

Encoding to assume if unknown (defaults to

"utf-8"

).

**dump_errors**

Display errors in the log. Enabled by default unless environment is "test".

**environment**

Current environment. Defaults to

ENV['APP_ENV']

, or

"development"

if not available.

**host_authorization**

You can pass a hash of options to host_authorization, to be used by the Rack::Protection::HostAuthorization middleware.

The middleware can block requests with unrecognized hostnames, to prevent DNS rebinding and other host header attacks. It checks the Host, X-Forwarded-Host and Forwarded headers.

Useful options are:

- permitted_hosts – an array of hostnames (and IPAddr objects) your app recognizes
  - in the development environment, it is set to .localhost, .test and any IPv4/IPv6 address
  - if empty, any hostname is permitted (the default for any other environment)
- status – the HTTP status code used in the response when a request is blocked (defaults to 403)
- message – the body used in the response when a request is blocked (defaults to Host not permitted)
- allow_if – supply a Proc to use custom allow/deny logic, the proc is passed the request environment

**logging**

Use the logger.

**lock**

Places a lock around every request, only running processing on request per Ruby process concurrently.

Enabled if your app is not thread-safe. Disabled by default.

**method_override**

Use

_method

magic to allow put/delete forms in browsers that don't support it.

**mustermann_opts**

A default hash of options to pass to Mustermann.new when compiling routing paths.

**port**

Port to listen on. Only used for built-in server.

**prefixed_redirects**

Whether or not to insert

request.script_name

into redirects if no absolute path is given. That way

redirect '/foo'

would behave like

redirect to('/foo')

. Disabled by default.

**protection**

Whether or not to enable web attack protections. See protection section above.

**public_dir**

Alias for

public_folder

. See below.

**public_folder**

Path to the folder public files are served from. Only used if static file serving is enabled (see

static

setting below). Inferred from

app_file

setting if not set.

**quiet**

Disables logs generated by Sinatra's start and stop commands.

false

by default.

**reload_templates**

Whether or not to reload templates between requests. Enabled in development mode.

**root**

Path to project root folder. Inferred from

app_file

setting if not set.

**raise_errors**

Raise unhandled errors (will stop application). Enabled by default when

environment

is set to

"test"

, disabled otherwise.

Any explicitly defined error handlers always override this setting. See the "Error" section below.

**run**

If enabled, Sinatra will handle starting the web server. Do not enable if using rackup or other means.

**running**

Is the built-in server running now? Do not change this setting!

**server**

Server or list of servers to use for built-in server. Order indicates priority, default depends on Ruby implementation.

**server_settings**

You can pass a hash of options to

server_settings

, such as

Host

or

Port

.

**sessions**

Enable cookie-based sessions support using

Rack::Session::Cookie

. See 'Using Sessions' section for more information.

**session_store**

The Rack session middleware used. Defaults to

Rack::Session::Cookie

. See 'Using Sessions' section for more information.

**show_exceptions**

Show a stack trace in the browser when an exception happens. Enabled by default when

environment

is set to

"development"

, disabled otherwise.

Can also be set to

:after_handler

to trigger app-specified error handling before showing a stack trace in the browser.

**static**

Whether Sinatra should handle serving static files.

Disable when using a server able to do this on its own.

Disabling will boost performance.

Enabled by default in classic style, disabled for modular apps.

**static_cache_control**

When Sinatra is serving static files, set this to add

Cache-Control

headers to the responses. Uses the

cache_control

helper. Disabled by default.

Use an explicit array when setting multiple values:

set :static_cache_control, [:public, :max_age => 300]

**threaded**

If set to

true

, will tell server to use

EventMachine.defer

for processing the request.

**traps**

Whether Sinatra should handle system signals.

**views**

Path to the views folder. Inferred from

app_file

setting if not set.

**x_cascade**

Whether or not to set the X-Cascade header if no route matches. Defaults to

true

.


## Lifecycle Events

There are 2 lifecycle events currently exposed by Sinatra. One when the server starts and one when it stops.

They can be used like this:

```ruby
on_start do
  puts "===== Booting up ====="
end

on_stop do
  puts "===== Shutting down ====="
end
```

Note that these callbacks only work when using Sinatra to start the web server.


## Environments

There are three predefined `environments`: `"development"`, `"production"` and `"test"`. Environments can be set through the `APP_ENV` environment variable. The default value is `"development"`. In the `"development"` environment all templates are reloaded between requests, and special `not_found` and `error` handlers display stack traces in your browser. In the `"production"` and `"test"` environments, templates are cached by default.

To run different environments, set the `APP_ENV` environment variable:

```shell
APP_ENV=production ruby my_app.rb
```

You can use predefined methods: `development?`, `test?` and `production?` to check the current environment setting:

```ruby
get '/' do
  if settings.development?
    "development!"
  else
    "not development!"
  end
end
```
