---
title: "Ruby on Rails"
source: https://en.wikipedia.org/wiki/Ruby_on_Rails
domain: activerecord-orm
license: CC-BY-SA-4.0
tags: active record pattern, rails activerecord, ruby orm, database migrations
fetched: 2026-07-02
---

# Ruby on Rails

**Ruby on Rails** (simplified as **Rails**) is a server-side web application framework written in Ruby under the MIT License. Rails is a model–view–controller (MVC) framework, providing default structures for a database, a web service, and web pages. It encourages and facilitates the use of web standards such as JSON or XML for data transfer and HTML, CSS and JavaScript for user interfacing. In addition to MVC, Rails emphasizes the use of other well-known software engineering patterns and paradigms, including convention over configuration (CoC), don't repeat yourself (DRY), and the active record pattern.

Ruby on Rails' emergence in 2005 greatly influenced web app development, through innovative features such as seamless database table creations, migrations, and scaffolding of views to enable rapid application development. Ruby on Rails' influence on other web frameworks remains apparent today, with many frameworks in other languages borrowing its ideas, including Django in Python; Catalyst in Perl; Laravel, CakePHP and Yii in PHP; Grails in Groovy; Phoenix in Elixir; Play in Scala; and Sails.js in Node.js.

Well-known sites that use Ruby on Rails include Airbnb, Archive of Our Own, Crunchbase, Dribbble, GitHub, Twitch and Shopify.

## History

David Heinemeier Hansson extracted Ruby on Rails from his work on the project management tool Basecamp at the web application company 37signals. Hansson first released Rails as open source in July 2004, but did not share commit rights to the project until February 2005. In August 2006, the framework reached a milestone when Apple announced that it would ship Ruby on Rails with Mac OS X v10.5 "Leopard", which was released in October 2007.

Rails version 2.3 was released on 15 March 2009, with major new developments in templates, engines, Rack and nested model forms. Templates enable the developer to generate a skeleton application with custom gems and configurations. Engines give developers the ability to reuse application pieces complete with routes, view paths and models. The Rack web server interface and Metal allow one to write optimized pieces of code that route around Action Controller.

On 23 December 2008, Merb, another web application framework, was launched, and Ruby on Rails announced it would work with the Merb project to bring "the best ideas of Merb" into Rails 3, ending the "unnecessary duplication" across both communities. Merb was merged with Rails as part of the Rails 3.0 release.

Rails 3.1 was released on 31 August 2011, featuring Reversible Database Migrations, Asset Pipeline, Streaming, jQuery as default JavaScript library and newly introduced CoffeeScript and Sass into the stack.

Rails 3.2 was released on 20 January 2012 with a faster development mode and routing engine (also known as Journey engine), Automatic Query Explain and Tagged Logging. Rails 3.2.x is the last version that supports Ruby 1.8.7. Rails 3.2.12 supports Ruby 2.0.

Rails 4.0 was released on 25 June 2013, introducing Russian Doll Caching, Turbolinks, and Live Streaming as well as making Active Resource, Active Record Observer and other components optional by splitting them as gems.

Rails 4.1 was released on 8 April 2014, introducing Spring, Variants, Enums, Mailer previews, and secrets.yml.

Rails 4.2 was released on 19 December 2014, introducing Active Job, asynchronous emails, Adequate Record, Web Console, and foreign keys.

Rails 5.0 was released on 30 June 2016, introducing Action Cable, API mode, and Turbolinks 5.

Rails 5.0.0.1 was released on 10 August 2016, with Exclusive use of rails CLI over Rake and support for Ruby version 2.2.2 and above.

Rails 5.1 was released on 27 April 2017, introducing JavaScript integration changes (management of JavaScript dependencies from NPM via Yarn, optional compilation of JavaScript using Webpack, and a rewrite of Rails UJS to use vanilla JavaScript instead of depending on jQuery), system tests using Capybara, encrypted secrets, parameterized mailers, direct & resolved routes, and a unified form_with helper replacing the form_tag/form_for helpers.

Rails 5.2 was released on 9 April 2018, introducing new features that include ActiveStorage, built-in Redis Cache Store, updated Rails Credentials and a new DSL that allows for configuring a Content Security Policy for an application.

Rails 5.2.2 was released on 4 December 2018, introducing numerous bug fixes and several logic improvements.

Rails 6.0 was released on 16 August 2019, making Webpack default, adding mailbox routing, a default online rich-text editor, parallel testing, multiple database support, mailer routing and a new autoloader.

Rails 6.1 was released on 9 December 2020, adding per-database connection switching, horizontal database sharding, eager loading of all associations, Delegated Types as an alternative to single-table inheritance, asynchronous deletion of associations, error objects, and other improvements and bug fixes.

Rails 7.0 was released on 15 December 2021, replacing Node.js and Webpack with import maps for JavaScript management by default, replacing Turbolinks with a combination of Turbo and Stimulus, adding at-work encryption into Active Record, using Zeitwerk exclusively for code loading, and more.

Rails 7.1 was released on 5 October 2023, Dockerfiles support using Kamal in order to deploy your application, authentication improvements, and now including support for Bun.

Ruby on Rails 8.0.0 was released on 8 November 2024. This major release introduces fundamental shifts in Rails development, enabling individual developers to host and manage their applications independently without the need for a Platform-as-a-service. The update focuses on empowering single developers to handle all aspects of application deployment and management seamlessly.

Ruby on Rails 8.1.0 was released on October 24, 2025. Major features include Active Job Continuations, Structured Event Reporting, Local CI, and Markdown rendering.

| Version | Release date | Compatible Ruby version(s) |
|---|---|---|
| Unsupported: 1.0 | 13 December 2005 | 1.8.6 |
| Unsupported: 1.2 | 19 January 2007 | 1.8.6 |
| Unsupported: 2.0 | 7 December 2007 | 1.8.6 |
| Unsupported: 2.1 | 31 May 2008 | 1.8.6 |
| Unsupported: 2.2 | 21 November 2008 | 1.8.7 recommended; 1.8.6 possible |
| Unsupported: 2.3 | 16 March 2009 | 1.8.7 recommended; 1.8.6 and 1.9.1 possible |
| Unsupported: 3.0 | 29 August 2010 | 1.9.3 recommended; 1.8.7 and 1.9.2 possible |
| Unsupported: 3.1 | 31 August 2011 | 1.9.3 recommended; 1.8.7 and 1.9.2 possible |
| Unsupported: 3.2 | 20 January 2012 | 1.9.3 recommended; 1.8.7 and 1.9.2 possible |
| Unsupported: 4.0 | 25 June 2013 | 2.0 preferred; 1.9.3 or newer required |
| Unsupported: 4.1 | 8 April 2014 | 2.0 preferred; 1.9.3 or newer required |
| Unsupported: 4.2 | 19 December 2014 | 2.0 preferred; 1.9.3 or newer required |
| Unsupported: 5.0 | 30 June 2016 | 2.2.2 or newer |
| Unsupported: 5.1 | 10 May 2017 | 2.2.2 or newer |
| Unsupported: 5.2 | 9 April 2018 | 2.2.2 or newer |
| Unsupported: 6.0 | 16 August 2019 | 2.5.0 or newer |
| Unsupported: 6.1 | 9 December 2020 | 2.5.0 or newer |
| Unsupported: 7.0 | 15 December 2021 | 2.7.0 or newer |
| Unsupported: 7.1 | 5 October 2023 | 2.7.0 or newer |
| Supported: 7.2 | 10 August 2024 | 3.1.0 or newer |
| Supported: 8.0 | 7 November 2024 | 3.2.0 or newer |
| Latest version: 8.1 | 24 October 2025 | 3.2.0 or newer |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |

A revised maintenance policy was instituted in October 2024.

## Technical overview

Ruby on Rails evolves radically from release to release exploring the use of new technologies and adopting new standards on the Internet. Some features are very stable in Ruby on Rails while some are replaced in favour of new techniques.

### Model-view-controller pattern

The model–view–controller (MVC) pattern is the fundamental structure to organize application programming.

In a default configuration, a *model* in the Ruby on Rails framework maps to a table in a database and to a Ruby file. For example, a model class *User* will usually be defined in the file 'user.rb' in the app/models directory, and linked to the table 'users' in the database. While developers are free to ignore this convention and choose differing names for their models, files, and database table, this is not common practice and is usually discouraged in accordance with the "convention-over-configuration" philosophy.

A *controller* is a server-side component of Rails that responds to external requests from the web server to the application, by determining which view file to render. The controller may also have to query one or more models for information and pass these on to the view. For example, in an airline reservation system, a controller implementing a flight-search function would need to query a model representing individual flights to find flights matching the search, and might also need to query models representing airports and airlines to find related secondary data. The controller might then pass some subset of the flight data to the corresponding view, which would contain a mixture of static HTML and logic that use the flight data to create an HTML document containing a table with one row per flight. A controller may provide one or more actions. In Ruby on Rails, an action is typically a basic unit that describes how to respond to a specific external web-browser request. Also, note that the controller/action will be accessible for external web requests only if a corresponding route is mapped to it. Rails encourages developers to use RESTful routes, which include actions such as create, new, edit, update, destroy, show, and index. These mappings of incoming requests/routes to controller actions can be easily set up in the routes.rb configuration file.

A *view* in the default configuration of Rails is an erb file, which is evaluated and converted to HTML at run-time. Alternatively, many other templating systems can be used for views.

Ruby on Rails includes tools that make common development tasks easier "out-of-the-box", such as scaffolding that can automatically construct some of the models and views needed for a basic website. Also included are WEBrick, a simple Ruby web server that is distributed with Ruby, and Rake, a build system, distributed as a gem. Together with Ruby on Rails, these tools provide a basic development environment.

### HTTP servers

Ruby on Rails is most commonly not connected to the Internet directly, but through some front-end web server. Mongrel was generally preferred over WEBrick in the early days, but it can also run on Lighttpd, Apache, Cherokee, Hiawatha, Nginx (either as a module – Phusion Passenger for example – or via CGI, FastCGI or mod ruby), and many others. From 2008 onward, Passenger replaced Mongrel as the most-used web server for Ruby on Rails. Ruby is also supported natively on IBM i.

### JavaScript

Ruby on Rails is also noteworthy for its extensive use of the JavaScript libraries Prototype and Script.aculo.us for scripting Ajax actions. Ruby on Rails 3.0 separates the markup of the page (which defines the structure of the page) from scripting (which determines functionality or logic of the page). As of version 7.0, new Ruby on Rails applications come with the Hotwire family of JavaScript libraries installed by default.

### Web services

Since version 2.0, Ruby on Rails offers both HTML and XML as standard output formats. The latter is the facility for RESTful web services.

### CSS

Rails 3.1 introduced Sass as standard CSS templating.

### Template

By default, the server uses Embedded Ruby in the HTML views, with files having an html.erb extension. Rails supports swapping-in alternative templating languages, such as HAML and Mustache.

### Ruby versions

Ruby on Rails 3.0 has been designed to work with Ruby 1.8.7, Ruby 1.9.2, and JRuby 1.5.2+; earlier versions are not supported.

Ruby on Rails 3.2 is the last series of releases that support Ruby 1.8.7.

### Framework structure

Ruby on Rails is separated into various packages, namely ActiveRecord (an object-relational mapping system for database access), Action Pack, Active Support and Action Mailer. Prior to version 2.0, Ruby on Rails also included the Action Web Service package that is now replaced by Active Resource. Apart from standard packages, developers can make plugins to extend existing packages. Earlier Rails supported plugins within their own custom framework; version 3.2 deprecates these in favor of standard Ruby "gems".

### Deployment

Ruby on Rails is often installed using RubyGems, a package manager which is included with current versions of Ruby. Many free Unix-like systems also support installation of Ruby on Rails and its dependencies through their native package management system.

Ruby on Rails is typically deployed with a database server such as MySQL or PostgreSQL, and a web server such as Apache running the Phusion Passenger module.

## Philosophy and design

Ruby on Rails is intended to emphasize *Convention over Configuration* (CoC), and the *Don't Repeat Yourself* (DRY) principle.

The Rails Doctrine is an enduring enabler that guides the philosophy, design, and implementation of the Ruby on Rails framework.

"Convention over Configuration" means a developer only needs to specify unconventional aspects of the application. For example, if there is a class *Sale* in the model, the corresponding table in the database is called *sales* by default. It is only if one deviates from this convention, such as calling the table "products sold", that the developer needs to write code regarding these names. Generally, Ruby on Rails conventions lead to less code and less repetition.

"Don't repeat yourself" means that information is located in a single, unambiguous place. For example, using the ActiveRecord module of Rails, the developer does not need to specify database column names in class definitions. Instead, Ruby on Rails can retrieve this information from the database based on the class name.

"Fat models, skinny controllers" means that most of the application logic should be placed within the model while leaving the controller as light as possible.

HTML Over The Wire (Hotwire), Conceptual compression, and robust security mark Rails 7.0's approach to the One person framework.

## Trademarks

In March 2007, David Heinemeier Hansson applied to register three Ruby on Rails-related trademarks with the USPTO. These applications concern the phrase "RUBY ON RAILS", the word "RAILS", and the official Rails logo. In the summer of 2007, Hansson denied the publisher Apress permission to use the Ruby on Rails logo on the cover of a new Ruby on Rails book written by some authoritative community members. The episode gave rise to a polite protest in the Ruby on Rails community. In response to this criticism, Hansson replied:

> I only grant promotional use [of the Rails logo] for products I'm directly involved with. Such as books that I've been part of the development process for or conferences where I have a say in the execution. I would most definitely seek to enforce all the trademarks of Rails.

The trademark of the logo was cancelled on 25 October 2019.

## Reception

### Scalability

In earlier days, Rails running on Matz's Ruby Interpreter (the *de facto* reference interpreter for Ruby) had been criticized for issues with scalability. These critiques often mentioned various Twitter outages in 2007 and 2008, which spurred Twitter's partial transition to Scala (which runs on the Java Virtual Machine) for their queueing system and other middleware. The user interface aspects of the site continued to run Ruby on Rails until 2011 when it was replaced due to concerns over performance. On the other hand, many Rails business application developers relied on system architecture design, including choices of database engine, cache configuration, and servers, to tackle scalability issues. The original author of Rails, David Heinemeier Hansson, criticized Twitter, saying that their problems scaling were the consequences of their own poor architectural decisions and not the fault of Rails. According to Hansson, blaming Rails for their troubles while making no contributions to the framework is ungrateful and unjust.

In 2011, Gartner Research noted that despite criticisms and comparisons to Java, many high-profile consumer web firms are using Ruby on Rails to build scalable web applications. Some of the largest sites running Ruby on Rails include Airbnb, Cookpad, GitHub, GitLab, Scribd, Shopify, and Basecamp. As of January 2016, it is estimated that more than 1.2 million web sites are running Ruby on Rails.

### Security

In March 2012, security researcher Egor Homakov discovered a mass assignment vulnerability that allowed certain Rails applications to be remotely exploited, and demonstrated it by non-maliciously hacking GitHub after his earlier attempts at responsible disclosure were dismissed.

On 24 September 2013, a session cookie persistence security flaw was reported in Ruby on Rails. In a default configuration, the entire session hash is stored within a session cookie known as *CookieStore*, allowing any authenticated session possessing the session cookie to log in as the target user at any time in the future. As a workaround, administrators are advised to configure cookies to be stored on the server using mechanisms such as *ActiveRecordStore*.

Researchers Daniel Jackson and Joseph Near developed a data debugger they called "Space" that can analyze the data access of a Rails program and determine if the program properly adheres to rules regarding access restrictions. On 15 April 2016, Near reported that an analysis of 50 popular Web applications using Space uncovered 23 previously unknown security flaws.
