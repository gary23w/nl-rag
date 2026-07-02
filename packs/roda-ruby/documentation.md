---
title: "Documentation"
source: https://roda.jeremyevans.net/documentation.html
domain: roda-ruby
license: CC-BY-SA-4.0
tags: roda ruby framework, rack routing tree, ruby routing framework, roda plugin system
fetched: 2026-07-02
---

# Documentation for Roda (v3.105.0)

## README (Introduction to Roda, start here if new)

## Online Book

Federico Iachetti has generously put his *Mastering Roda* book under the Commons Attribution 4.0 International License, and posted a publicly accessible online version. The book has been updated and now is kept up to date with changes to Roda. If you would like to improve the book, please submit a merge request.

## Guides

- Conventions

## RDoc (frames)

Here are direct links to the most important pages:

- Roda ClassMethods (used for configuring Roda)
- Roda InstanceMethods (minimal so as not to pollute the scope)
- Roda RequestMethods (all the methods for routing requests, such as r.on)
- Roda ResponseMethods (methods for manipulating the response directly)

## Plugins

Plugins are a very important part of Roda, since by design Roda has a very small core.

### Plugins that Ship with Roda

- Routing:
  - autoload_hash_branches: Allows autoloading file for a hash branch when there is a request for that branch.
  - autoload_named_routes: Allows autoloading file for a named route when there is a request for that route.
  - all_verbs: Adds request routing methods for all http verbs.
  - backtracking_array: Allows array matchers to backtrack if later matchers do not match.
  - break: Supports break inside routing blocks for skipping the current matching route block as if it didn't match.
  - class_level_routing: Adds class level routing methods, for a DSL similar to sinatra.
  - error_handler: Adds ability to automatically handle errors raised by the application.
  - hash_branches: Supports O(1) dispatching to multiple branches at all levels in the routing tree.
  - hash_paths: Supports O(1) dispatching to multiple paths at all levels in the routing tree.
  - hash_routes: Provides a DSL to configure the hash_branches and hash_paths plugins.
  - head: Treat HEAD requests like GET requests with an empty response body.
  - hmac_paths: Prevent path enumeration and support access control using HMACs in paths.
  - hooks: Adds before/after hook methods.
  - host_routing: Adds support for routing based on the host header.
  - match_hook: Adds a hook method which is called when a path segment is matched.
  - match_hook_args: Similar to match_hook plugin, but supports passing matchers and block args to hooks.
  - multi_route: Allows dispatching to multiple named route blocks in a single call.
  - multi_run: Adds the ability to dispatch to multiple rack applications based on the request path prefix.
  - named_routes: Allows for multiple named route blocks that can be dispatched to inside the main route block.
  - not_allowed: Adds support for automatically returning 405 Method Not Allowed responses.
  - not_found: Adds not_found method for handling responses not otherwise handled by a route.
  - pass: Adds pass method for skipping the current matching route block as if it didn't match.
  - path_rewriter: Adds support for rewriting paths before routing.
  - route_block_args: Controls which arguments are passed to the route block.
  - run_append_slash: Makes r.run use "/" instead of "" for app's PATH_INFO
  - run_handler: Allows for modifying rack response arrays when using r.run, and continuing routing for 404 responses.
  - run_require_slash: Skip dispatching to another application if PATH_INFO for dispatch would violate Rack SPEC
  - static_routing: Adds class level static routing methods, for maximum performance when handling static routes (routes without placeholders).
  - status_handler: Adds status_handler method for handling responses without bodies for a given status code.
  - type_routing: Route based on path extensions and Accept headers.
  - unescape_path: Decodes URL-encoded PATH_INFO before routing.
- Rendering/View:
  - additional_render_engines: Allows for considering multiple render engines, using path for first template that exists.
  - additional_view_directories: Allows for checking for templates in multiple view directories, using path for first template that exists.
  - assets: Adds support for rendering CSS/JS javascript assets on the fly in development, or compiling them into a single compressed file in production.
  - assets_preloading: Adds support for generating browser-hinting preload link tags and headers.
  - branch_locals: Adds ability to specify defaults for template locals on a per-branch basis.
  - capture_erb: Allows capturing the output of ERB template blocks, instead of injecting them into the template output.
  - chunked: Adds support for streaming template responses using Transfer-Encoding: chunked.
  - content_for: Allows storage of content in one template and retrieval of that content in a different template.
  - custom_block_results: Adds support for arbitrary objects as block results.
  - each_part: Adds each_part method for simplifying render_each with :locals.
  - erb_h: Adds faster (if slightly less safe method) h method for html escaping, based on erb/escape.
  - exception_page: Shows page with debugging information for exceptions, designed for use in error handler in development mode.
  - h: Adds h method for html escaping.
  - hash_branch_view_subdir: Automatically appends a view subdirectory for each successful hash branch taken.
  - hash_public: Adds support for serving files in the public directory, with paths that change based on file content.
  - hash_public_cache: Adds support for caching digests for files served by the hash_public plugin.
  - inject_erb: Allows injecting arbitrary content directly into ERB template output.
  - json: Allows match blocks to return arrays and hashes, using a json representation as the response body.
  - link_to: Simplifies creation of HTML links.
  - multi_public: Adds support for serving all files in multiple public directories.
  - multi_view: Allows for easily setting up routing for rendering multiple views.
  - named_templates: Adds the ability to create inline templates by name, instead of storing them in the file system.
  - padrino_render: Makes render method that work similarly to Padrino's rendering, using a layout by default.
  - part: Adds part method for simpler rendering of templates with locals.
  - partials: Adds partial method for rendering partials (templates prefixed with an underscore).
  - precompile_templates: Adds support for precompiling templates, saving memory when using a forking webserver.
  - public: Adds support for serving all files in the public directory.
  - recheck_precompiled_assets: Allows checking for the precompiled assets metadata file for updates.
  - render: Adds render method for rendering templates, using tilt.
  - render_each: Render a template for each value in an enumerable.
  - render_coverage: Sets compiled_path for Tilt templates, allowing coverage of compiled templates before Ruby 3.2 (requires tilt 2.1+).
  - render_locals: Adds ability to specify defaults for template locals.
  - static: Adds support for serving static files using Rack::Static.
  - streaming: Adds ability to stream responses.
  - symbol_views: Allows match blocks to return template name symbols, uses the template view as the response body.
  - timestamp_public: Adds support for serving files in the public directory, with paths that change based on file modification time.
  - view_options: Allows for setting view options on a per-request basis.
  - view_subdir_leading_slash: Use view subdirectory for all template names that do not start with a /.
- Request/Response:
  - assume_ssl: Makes request ssl? method always return true, for use with SSL-terminating reverse proxies that do not set appropriate headers.
  - bearer_token: Adds r.bearer_token method for retrieving bearer token from HTTP Authorization header.
  - caching: Adds request and response methods related to http caching.
  - content_security_policy: Allows setting an appropriate Content-Security-Policy header for the application/branch/action.
  - cookie_flags: Adds checks for certain cookie flags, to update, warn, or error if they are not set correctly.
  - cookies: Adds response methods for handling cookies.
  - default_headers: Allows modifying the default headers for responses.
  - default_status: Allows overriding the default status for responses.
  - delegate: Adds class methods for creating instance methods that delegate to the request, response, or class.
  - delete_empty_headers: Automatically delete response headers with empty values.
  - disallow_file_uploads: Disallow multipart file uploads.
  - drop_body: Automatically drops response body and Content-Type/Content-Length headers for response statuses indicating no body.
  - halt: Augments request halt method for support for setting response status and/or response body.
  - hsts: Sets Strict-Transport-Security response header.
  - invalid_request_body: Allows for custom handling of invalid request bodies.
  - module_include: Adds request_module and response_module class methods for adding modules/methods to request/response classes.
  - permissions_policy: Allows setting an appropriate Permissions-Policy header for the application/branch/action.
  - plain_hash_response_headers: Uses plain hashes for response headers on Rack 3, for much better performance.
  - r: Adds r method for accessing the request, useful when r local variable is not in scope.
  - redirect_http_to_https: Adds request method to redirect HTTP requests to the same location using HTTPS.
  - redirect_path: Allows r.redirect to automatically work with objects registered with the path plugin.
  - request_aref: Adds configurable handling for [] and []= request methods.
  - request_headers: Adds a headers method to the request object, for easier access to request headers.
  - response_attachment: More easily set content-disposition and content-type headers for attachments.
  - response_content_type: More easily set content-type header for responses.
  - response_request: Gives response object access to request object.
  - send_file: Adds send_file method for returning file content as a response.
  - sinatra_helpers: Port of Sinatra::Helpers methods not covered by other plugins.
  - status_303: Uses 303 as the default redirect status for non-GET requests by HTTP 1.1 clients.
  - symbol_status: Allows the use of symbols as status codes, converting them to the appropriate integer.
  - typecast_params: Allows for easily converting parameter values to explicit types.
  - typecast_params_sized_integers: Allows for easily converting parameter values to integers for specific integer sizes (8-bit, 16-bit, 32-bit, and 64-bit).
- Matchers:
  - class_matchers: Adds support for handling matchers for arbitrary classes, with support for type conversion.
  - custom_matchers: Adds support for arbitrary objects as matchers.
  - empty_root: Makes root matcher match empty string in addition to single slash.
  - hash_matcher: Adds hash_matcher class method for easily defining hash matchers.
  - header_matchers: Adds matchers using information from the request headers.
  - Integer_matcher_max: Sets a maximum integer value that will be matched by the default Integer matcher.
  - map_matcher: Adds support for :map hash matcher for matching next route segment by hash key, yielding hash value.
  - match_affix: Adds support for overriding default prefix/suffix used in match patterns.
  - multibyte_string_matcher: Makes string matcher handle multibyte characters.
  - param_matchers: Adds matchers using information from the request params.
  - params_capturing: Stores matcher captures in the request params.
  - path_matchers: Adds matchers using information from the request path.
  - placeholder_string_matchers: Supports placeholders in strings for backwards compatibility.
  - optimized_segment_matchers: Adds performance optimized matchers for single String class argument.
  - optimized_string_matchers: Adds performance optimized matchers for single string arguments.
  - slash_path_empty: Considers a path of "/" as an empty path when doing a terminal match.
  - symbol_matchers: Adds support for symbol-specific matching regexps.
- Mail:
  - error_email: Adds ability to easily email a notification when an error is raised by the application, using net/smtp.
  - error_mail: Adds ability to easily email a notification when an error is raised by the application, using mail.
  - mail_processor: Adds support for processing emails using the routing tree.
  - mailer: Adds support for sending emails using the routing tree.
- Middleware:
  - direct_call: Makes Roda.call skip the middleware stack, allowing more optimization when dispatching routes.
  - middleware: Allows the Roda app to be used as middleware by another app.
  - middleware_stack: Allows removing middleware and inserting middleware before the end of the stack.
- CSRF Protection:
  - csrf: Older CSRF plugin for backwards compatibility using rack_csrf.
  - route_csrf: Recommended CSRF plugin with request-specific tokens and control over where CSRF tokens are checked during routing.
  - sec_fetch_site_csrf: Simpler CSRF plugin using the Sec-Fetch-Site header used in modern browsers.
- Other:
  - common_logger: Adds support for logging in common log format.
  - conditional_sessions: Allows for using the session plugin for a subset of requests.
  - environments: Adds support for handling different execution environments (development/test/production).
  - early_hints: Adds support for using 103 Early Hints responses when using a compatible server.
  - filter_common_logger: Adds support for skipping the logging of certain requests when using the common_logger plugin.
  - flash: Adds flash handling.
  - heartbeat: Adds support for heartbeats.
  - host_authorization: Allows configuring an authorized host or an array of authorized hosts.
  - indifferent_params: Adds params method for indifferent parameters.
  - ip_from_header: Gets request IP address from specified header if present.
  - json_parser: Parses request bodies in JSON format.
  - path: Adds support for named paths.
  - relative_path: Adds support for turning absolute paths into paths relative to current request.
  - sessions: Implements support for encrypted sessions.
  - shared_vars: Stores and retrives variables shared between multiple Roda apps.
  - strip_path_prefix: Strips prefixes off internal absolute paths, making them relative paths.

## External Resources

### Guides

- Adding Authentication
- Up and Going in Roda: Static Ruby Websites
- Up and Going in Roda: A Simple Ruby Blog
- Digging ruby from Roda

### Plugins

These projects ship external plugins for Roda:

- autoforme: Adds autoforme method for automatic creation of administrative front-end for Sequel models.
- forme: Adds form method for simple creation of html forms inside erb templates.
- rodauth: Authentication and account management framework.
- roda-action: Resolves actions stored in roda-container.
- roda-auth: Adds authentication support for Roda.
- roda-basic-auth: Adds support for HTTP basic authentication.
- roda-component: Adds realtime components using faye and opal.
- roda-container: Turns application into an inversion of control (IoC) container.
- roda-enhanced_logger: A powerful logger.
- roda-flow: Changes routing methods to delegate to containers.
- roda-i18n: Adds easy internationalization and localization support.
- roda-mailer_ext: Teach the Roda mailer plugin a few neat tricks.
- roda-mailer_preview: Preview your emails generated by the Roda mailer plugin.
- roda-message_bus: MessageBus Integration for Roda.
- roda-parse-request: Automatically parse JSON and URL-encoded requests.
- roda-rails: Integration for using Roda as Rack middleware in a Rails app.
- roda-route_list: Parses route metadata from comments in an app file, allowing introspection of routes.
- roda-rest_api: Adds support for easily creating RESTful APIs.
- roda-sprockets: Use Sprockets to build and serve JS and CSS.
- roda-symbolized_params: Adds params method for symbolized params.
- roda-unpoly: Easily integrate Unpoly into your Roda application.
- roda-will_paginate: will_paginate integration for Roda.
- rom-roda: Adds integration with Ruby Object Mapper.

### Libraries

These external projects are related to Roda:

- newrelic-roda: Adds newrelic instrument for Roda.
- roda-bin: Add bin/roda binary for a simple development server that reloads on changes.
- roda-sequel-stack: Application Skeleton For Roda/Sequel stack.
- roda_app: Generator for Roda apps.
- roda-template-simple: Template for a simple Roda application

## Change Log

## Release Notes

- 3.105 | 3.104 | 3.103 | 3.102 | 3.101 | 3.100
- 3.99 | 3.98 | 3.97 | 3.96 | 3.95 | 3.94 | 3.93 | 3.92 | 3.91 | 3.90
- 3.89 | 3.88 | 3.87 | 3.86 | 3.85 | 3.84 | 3.83 | 3.82 | 3.81 | 3.80
- 3.79 | 3.78 | 3.77 | 3.76 | 3.75 | 3.74 | 3.73 | 3.72 | 3.71 | 3.70
- 3.69 | 3.68 | 3.67 | 3.66 | 3.65 | 3.64 | 3.63 | 3.62 | 3.61 | 3.60
- 3.59 | 3.58 | 3.57 | 3.56 | 3.55 | 3.54 | 3.53 | 3.52 | 3.51 | 3.50
- 3.49 | 3.48 | 3.47 | 3.46 | 3.45 | 3.44 | 3.43 | 3.42 | 3.41 | 3.40
- 3.39 | 3.38 | 3.37 | 3.36 | 3.35 | 3.34 | 3.33 | 3.32 | 3.31 | 3.30
- 3.29 | 3.28 | 3.27 | 3.26 | 3.25 | 3.24 | 3.23 | 3.22 | 3.21 | 3.20
- 3.19 | 3.18 | 3.17 | 3.16 | 3.15 | 3.14.1 | 3.14 | 3.13 | 3.12 | 3.11 | 3.10
- 3.9 | 3.8 | 3.7 | 3.6 | 3.5 | 3.4 | 3.3 | 3.2 | 3.1 | 3.0
- 2.29 | 2.28 | 2.27 | 2.26 | 2.25 | 2.24 | 2.23 | 2.22 | 2.21 | 2.20
- 2.19 | 2.18 | 2.17 | 2.16 | 2.15 | 2.14 | 2.13 | 2.12 | 2.11 | 2.10
- 2.9 | 2.8 | 2.7 | 2.6 | 2.5.1 | 2.5 | 2.4 | 2.3 | 2.2 | 2.1 | 2.0
- 1.3 | 1.2 | 1.1 | 1.0

## License

## Resources

## Interviews

- content_for :devs 010: Advanced Ruby with Jeremy Evans
- Rubber Duck Dev Show 83: All About Roda with Jeremy Evans
- Ruby Rogues 507: Building with Just What You Need Using Roda with Jeremy Evans
- Ruby Rogues 210: Roda and Routing Trees with Jeremy Evans

## Books

- Ruby on Roda - REST APIs with Roda & Sequel

## Presentations

- "The first 10 years of Roda" Presentation at November 2024 SF Bay Area Ruby Meetup (Video)
- "10 Years of Roda" Presentation at RubyConf 2024 (Video)
- "Roda: Simplicity, Reliability, Extensibility, Performance" Presentation at RubyConf Thailand 2022 (Video)
- "Roda: Simplicity, Reliability, Extensibility, Performance" Presentation at RubyConf Pakistan March 2022 (Video)
- "Dynamic routing in Ruby"
- "Roda" Lightning Talk at RailsConf 2015 (4x3 version) (Video)
- "Better Routing Through Trees" Presentation at MountainWest RubyConf 2015 (4x3 version) (Video)
- "Roda: The Routing Tree Web Framework" Presentation at RubyConf 2014 (4x3 Version) (Video)

## Applications Using Roda

Here are some open source applications that use Roda:

- Ubicloud (Open, Free, and Portable Cloud)
- Bridgetown (Progressive Site Generator and Fullstack Framework)
- Karafka Web (User Inferface for Karafka Framework)
- Kontena (Docker Container Management)
- Alienist Viewer (JRuby Memory Dump Viewer)
- golf-score-roda (Backend for golf-score-frontend)
- tus-ruby-server (Backend for Resumable Uploads)
- LightBlog (Blog Using Markdown Files)
- SPAM (Simple Personal Accounting Manager)
- Giftsmas (Gift Tracking)
- KaeruEra (Exception Tracking)
- Quinto (Version of 1960s 3M Board Game)
- CSPVR (Content-Security-Policy Violation Recorder and Viewer)
- Lila Shell (Basic Chat Application)
- Falcom CD Catalog (Database of Nihon Falcom Albums)
- Forme Demo (Demo Site for Forme)
- AutoForme Demo (Demo Site for AutoForme)
- Rodauth Demo (Demo Site for Rodauth)
