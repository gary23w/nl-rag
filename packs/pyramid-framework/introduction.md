---
title: "Pyramid Introduction"
source: https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/introduction.html
domain: pyramid-framework
license: CC-BY-SA-4.0
tags: pyramid python framework, pylons pyramid web, python wsgi framework, pyramid traversal routing
fetched: 2026-07-02
---

# Pyramid Introduction

Pyramid is a Python web application *framework*. It is designed to make creating web applications easier. It is open source.

Pyramid follows these design and engineering principles:

**Simplicity**

Pyramid is designed to be easy to use. You can get started even if you don't understand it all. And when you're ready to do more, Pyramid will be there for you.

**Minimalism**

Out of the box, Pyramid provides only the core tools needed for nearly all web applications: mapping URLs to code, security, and serving static assets (files like JavaScript and CSS). Additional tools provide templating, database integration and more. But with Pyramid you can *"pay only for what you eat"*.

**Documentation**

Pyramid is committed to comprehensive and up-to-date documentation.

**Speed**

Pyramid is designed to be noticeably fast.

**Reliability**

Pyramid is developed conservatively and tested exhaustively. Our motto is: "If it ain't tested, it's broke".

**Openness**

As with Python, the Pyramid software is distributed under a permissive open source license.

## Why Pyramid?

In a world filled with web frameworks, why should you choose Pyramid?

### Modern

Pyramid is fully compatible with Python 3. If you develop a Pyramid application today, you can rest assured that you'll be able to use the most modern features of your favorite language. And in the years to come, you'll continue to be working on a framework that is up-to-date and forward-looking.

### Tested

Untested code is broken by design. The Pyramid community has a strong testing culture and our framework reflects that. Every release of Pyramid has 100% statement coverage (as measured by coverage) and 95% decision/condition coverage. (as measured by instrumental) It is automatically tested using Travis and Jenkins on supported versions of Python after each commit to its GitHub repository. Official Pyramid add-ons are held to a similar testing standard.

We still find bugs in Pyramid, but we've noticed we find a lot fewer of them while working on projects with a solid testing regime.

### Documented

The Pyramid documentation is comprehensive. We strive to keep our narrative documentation both complete and friendly to newcomers. We also maintain the Pyramid Community Cookbook of recipes demonstrating common scenarios you might face. Contributions in the form of improvements to our documentation are always appreciated. And we always welcome improvements to our official tutorials as well as new contributions to our community maintained tutorials.

### Supported

You can get help quickly with Pyramid. It's our goal that no Pyramid question go unanswered. Whether you ask a question on IRC, on the Pylons-discuss mailing list, or on StackOverflow, you're likely to get a reasonably prompt response.

Pyramid is also a welcoming, friendly space for newcomers. We don't tolerate "support trolls" or those who enjoy berating fellow users in our support channels. We try to keep it well-lit and new-user-friendly.

See also

See also our #pyramid IRC channel, our pylons-discuss mailing list, and Support and Development.

## What makes Pyramid unique

There are many tools available for web development. What would make someone want to use Pyramid instead? What makes Pyramid unique?

With Pyramid you can write very small applications without needing to know a lot. And by learning a bit more, you can write very large applications too. Pyramid will allow you to become productive quickly, and will grow with you. It won't hold you back when your application is small, and it won't get in your way when your application becomes large. Other application frameworks seem to fall into two non-overlapping categories: those that support "small apps" and those designed for "big apps".

We don't believe you should have to make this choice. You can't really know how large your application will become. You certainly shouldn't have to rewrite a small application in another framework when it gets "too big". A well-designed framework should be able to be good at both. Pyramid is that kind of framework.

Pyramid provides a set of features that are unique among Python web frameworks. Others may provide some, but only Pyramid provides them all, in one place, fully documented, and *à la carte* without needing to pay for the whole banquet.

### Build single-file applications

You can write a Pyramid application that lives entirely in one Python file. Such an application is easy to understand since everything is in one place. It is easy to deploy because you don't need to know much about Python packaging. Pyramid allows you to do almost everything that so-called *microframeworks* can in very similar ways.

```
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
```

See also

See also Creating Your First Pyramid Application.

### Configure applications with decorators

Pyramid allows you to keep your configuration right next to your code. That way you don't have to switch files to see your configuration. For example:

```python
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='fred')
def fred_view(request):
    return Response('fred')
```

However, using Pyramid configuration decorators does not change your code. It remains easy to extend, test, or reuse. You can test your code as if the decorators were not there. You can instruct the framework to ignore some decorators. You can even use an imperative style to write your configuration, skipping decorators entirely.

See also

See also Adding View Configuration Using the @view_config Decorator.

### Generate application URLs

Dynamic web applications produce URLs that can change depending on what you are viewing. Pyramid provides flexible, consistent, easy to use tools for generating URLs. When you use these tools to write your application, you can change your configuration without fear of breaking links in your web pages.

See also

See also Generating Route URLs.

### Serve static assets

Web applications often require JavaScript, CSS, images and other so-called *static assets*. Pyramid provides flexible tools for serving these kinds of files. You can serve them directly from Pyramid, or host them on an external server or CDN (content delivery network). Either way, Pyramid can help you to generate URLs so you can change where your files come from without changing any code.

See also

See also Serving Static Assets.

### Develop interactively

Pyramid can automatically detect changes you make to template files and code, so your changes are immediately available in your browser. You can debug using plain old `print()` calls, which will display to your console.

Pyramid has a debug toolbar that allows you to see information about how your application is working right in your browser. See configuration, installed packages, SQL queries, logging statements and more.

When your application has an error, an interactive debugger allows you to poke around from your browser to find out what happened.

To use the Pyramid debug toolbar, build your project with our cookiecutter.

See also

See also The Debug Toolbar.

### Debug with power

When things go wrong, Pyramid gives you powerful ways to fix the problem.

You can configure Pyramid to print helpful information to the console. The `debug_notfound` setting shows information about URLs that aren't matched. The `debug_authorization` setting provides helpful messages about why you aren't allowed to do what you just tried.

Pyramid also has command line tools to help you verify your configuration. You can use `proutes` and `pviews` to inspect how URLs are connected to your application code.

See also

See also Debugging View Authorization Failures, Command-Line Pyramid, and p* Scripts Documentation

### Extend your application

Pyramid add-ons extend the core of the framework with useful abilities. There are add-ons available for your favorite template language, SQL and NoSQL databases, authentication services and more.

Supported Pyramid add-ons are held to the same demanding standards as the framework itself. You will find them to be fully tested and well documented.

See also

See also https://trypyramid.com/extending-pyramid.html

### Write your views, *your* way

A fundamental task for any framework is to map URLs to code. In Pyramid, that code is called a view callable. View callables can be functions, class methods or even callable class instances. You are free to choose the approach that best fits your use case. Regardless of your choice, Pyramid treats them the same. You can change your mind at any time without any penalty. There are no artificial distinctions between the various approaches.

Here's a view callable defined as a function:

```python
1from pyramid.response import Response
2from pyramid.view import view_config
3
4@view_config(route_name='aview')
5def aview(request):
6    return Response('one')
```

Here's a few views defined as methods of a class instead:

```python
 1from pyramid.response import Response
 2from pyramid.view import view_config
 3
 4class AView(object):
 5    def __init__(self, request):
 6        self.request = request
 7
 8    @view_config(route_name='view_one')
 9    def view_one(self):
10        return Response('one')
11
12    @view_config(route_name='view_two')
13    def view_two(self):
14        return Response('two')
```

See also

See also @view_config Placement.

### Find *your* static assets

In many web frameworks, the static assets required by an application are kept in a globally shared location, "the *static* directory". Others use a lookup scheme, like an ordered set of template directories. Both of these approaches have problems when it comes to customization.

Pyramid takes a different approach. Static assets are located using *asset specifications*, strings that contain reference both to a Python package name and a file or directory name, e.g. `MyPackage:static/index.html`. These specifications are used for templates, JavaScript and CSS, translation files, and any other package-bound static resource. By using asset specifications, Pyramid makes it easy to extend your application with other packages without worrying about conflicts.

What happens if another Pyramid package you are using provides an asset you need to customize? Maybe that page template needs better HTML, or you want to update some CSS. With asset specifications you can override the assets from other packages using simple wrappers.

Examples: Understanding Asset Specifications and Overriding Assets.

### Use *your* templates

In Pyramid, the job of creating a `Response` belongs to a renderer. Any templating system—Mako, Chameleon, Jinja2—can be a renderer. In fact, packages exist for all of these systems. But if you'd rather use another, a structured API exists allowing you to create a renderer using your favorite templating system. You can use the templating system *you* understand, not one required by the framework.

What's more, Pyramid does not make you use a single templating system exclusively. You can use multiple templating systems, even in the same project.

Example: Using Templates Directly.

### Write testable views

When you use a renderer with your view callable, you are freed from needing to return a "webby" `Response` object. Instead your views can return a simple Python dictionary. Pyramid will take care of rendering the information in that dictionary to a `Response` on your behalf. As a result, your views are more easily tested, since you don't need to parse HTML to evaluate the results. Pyramid makes it a snap to write unit tests for your views, instead of requiring you to use functional tests.

For example, a typical web framework might return a `Response` object from a `render_to_response` call:

```python
1from pyramid.renderers import render_to_response
2
3def myview(request):
4    return render_to_response('myapp:templates/mytemplate.pt', {'a':1},
5                              request=request)
```

While you *can* do this in Pyramid, you can also return a Python dictionary:

```python
1from pyramid.view import view_config
2
3@view_config(renderer='myapp:templates/mytemplate.pt')
4def myview(request):
5    return {'a':1}
```

By configuring your view to use a renderer, you tell Pyramid to use the `{'a':1}` dictionary and the specified template to render a response on your behalf.

The string passed as `renderer=` above is an asset specification. Asset specifications are widely used in Pyramid. They allow for more reliable customization. See Find your static assets for more information.

Example: Renderers.

### Use events to coordinate actions

When writing web applications, it is often important to have your code run at a specific point in the lifecycle of a request. In Pyramid, you can accomplish this using *subscribers* and *events*.

For example, you might have a job that needs to be done each time your application handles a new request. Pyramid emits a `NewRequest` event at this point in the request handling lifecycle. You can register your code as a subscriber to this event using a clear, declarative style:

```python
from pyramid.events import NewRequest
from pyramid.events import subscriber

@subscriber(NewRequest)
def my_job(event):
    do_something(event.request)
```

Pyramid's event system can be extended as well. If you need, you can create events of your own and send them using Pyramid's event system. Then anyone working with your application can subscribe to your events and coordinate their code with yours.

Example: Using Events and Event Types.

### Build international applications

Pyramid ships with internationalization-related features in its core: localization, pluralization, and creating message catalogs from source files and templates. Pyramid allows for a plurality of message catalogs via the use of translation domains. You can create a system that has its own translations without conflict with other translations in other domains.

Example: Internationalization and Localization.

### Build efficient applications

Pyramid provides an easy way to *cache* the results of slow or expensive views. You can indicate in view configuration that you want a view to be cached:

```python
@view_config(http_cache=3600) # 60 minutes
def myview(request):
    # ...
```

Pyramid will automatically add the appropriate `Cache-Control` and `Expires` headers to the response it creates.

See the `add_view()` method's `http_cache` documentation for more information.

### Build fast applications

The Pyramid core is fast. It has been engineered from the ground up for speed. It only does as much work as absolutely necessary when you ask it to get a job done. If you need speed from your application, Pyramid is the right choice for you.

Example: https://blog.curiasolutions.com/pages/the-great-web-framework-shootout.html

### Store session data

Pyramid has built-in support for HTTP sessions, so you can associate data with specific users between requests. Lots of other frameworks also support sessions. But Pyramid allows you to plug in your own custom sessioning system. So long as your system conforms to a documented interface, you can drop it in in place of the provided system.

Currently there is a binding package for the third-party Redis sessioning system that does exactly this. But if you have a specialized need (perhaps you want to store your session data in MongoDB), you can. You can even switch between implementations without changing your application code.

Example: Sessions.

### Handle problems with grace

Mistakes happen. Problems crop up. No one writes bug-free code. Pyramid`provides a way to handle the exceptions your code encounters. An :term:`exception view is a special kind of view which is automatically called when a particular exception type arises without being handled by your application.

For example, you might register an exception view for the `Exception` exception type, which will catch *all* exceptions, and present a pretty "well, this is embarrassing" page. Or you might choose to register an exception view for only certain application-specific exceptions. You can make one for when a file is not found, or when the user doesn't have permission to do something. In the former case, you can show a pretty "Not Found" page; in the latter case you might show a login form.

Example: Custom Exception Views.

### And much, much more...

Pyramid has been built with a number of other sophisticated design features that make it adaptable. Read more about them below.

- Advanced Pyramid Design Features
  - You Don't Need Singletons
  - Simplify your View Code with Predicates
  - Stop Worrying About Transactions
  - Stop Worrying About Configuration
  - Compose Powerful Apps From Simple Parts
  - Authenticate Users Your Way
  - Build Trees of Resources
  - Take Action on Each Request with Tweens
  - Return What You Want From Your Views
  - Use Global Response Objects
  - Extend Configuration
  - Introspect Your Application

## What Is The Pylons Project?

Pyramid is a member of the collection of software published under the Pylons Project. Pylons software is written by a loose-knit community of contributors. The Pylons Project website includes details about how Pyramid relates to the Pylons Project.

## Pyramid and Other Web Frameworks

The first release of Pyramid's predecessor (named `repoze.bfg`) was made in July of 2008. At the end of 2010, we changed the name of `repoze.bfg` to Pyramid. It was merged into the Pylons project as Pyramid in November of that year.

Pyramid was inspired by Zope, Pylons (version 1.0), and Django. As a result, Pyramid borrows several concepts and features from each, combining them into a unique web framework.

Similar to Zope, Pyramid applications may easily be extended. If you work within the constraints of the framework, you can produce applications that can be reused, modified, or extended without needing to modify the original application code. Pyramid also inherits the concepts of traversal and declarative security from Zope.

Similar to Pylons version 1.0, Pyramid is largely free of policy. It makes no assertions about which database or template system you should use. You are free to use whatever third-party components fit the needs of your specific application. Pyramid also inherits its approach to URL dispatch from Pylons.

Similar to Django, Pyramid values extensive documentation. In addition, the concept of a view is used by Pyramid much as it would be by Django.

Other Python web frameworks advertise themselves as members of a class of web frameworks named model-view-controller frameworks. The authors of Pyramid do not believe that the MVC pattern fits the web particularly well. However, if this abstraction works for you, Pyramid also generally fits into this class.
