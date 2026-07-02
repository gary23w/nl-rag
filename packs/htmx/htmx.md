---
title: "htmx"
source: https://en.wikipedia.org/wiki/HTMX
domain: htmx
license: CC-BY-SA-4.0 / BSD (htmx.org)
tags: htmx, hypermedia driven, hx-get, ajax attributes
fetched: 2026-07-02
---

# htmx

(Redirected from

HTMX

)

**htmx** (also stylized as **HTMX**) is an open-source front-end JavaScript library that extends HTML with custom attributes that enable the use of AJAX directly in HTML and with a hypermedia-driven approach. These attributes allow for the dynamic definition of a web page directly in HTML and CSS, without the need for writing additional JavaScript. These attributes allows tasks that traditionally required writing JavaScript to be done completely with HTML. The library was created by Carson Gross as a new version of **intercooler.js**.

The library supports communication with the server using standard HTTP methods and simplifies inserting server responses (usually text or HTML fragments) into designated parts of the web page without having to redraw the entire page. This in turn allows for similar behavior to what can be achieved with reconciliation behavior in virtual DOMs.

## History

htmx has its roots in intercooler.js, a frontend library created by Carson Gross in 2013. The library aimed to address the complexity associated with AJAX (asynchronous JavaScript and XML) by introducing a simplified approach using HTML attributes. The intent was to create a framework that was aligned with Roy Fielding's original intent for REST (representational state transfer) - and specifically HATEOAS (hypermedia as the engine of application state). The problem is described in Fielding's blog post "REST APIs must be hypertext-driven" from October 2008.

htmx was created as an improved version of intercooler.js that did not rely on jQuery with version 1.0.0 being released in November 2020. The release of htmx was a significant milestone for the project, by offering a way to utilize AJAX, CSS transitions, WebSockets, and Server-Sent Events directly in HTML using attributes.

In 2023, htmx was added to the first cohort of the GitHub Accelerator program, a program that provides open source projects with funding and guidance from members of mature open source projects.

## Design and functionality

htmx combines the capabilities of modern frameworks with the server-side processing of traditional web applications. The library's design philosophy revolves around a goal to "complete HTML as a hypertext." By leveraging custom HTML attributes prefixed with `hx-` to trigger AJAX requests to fetch content to update parts of the DOM with, htmx enables developers to define dynamic behavior directly within their markup, reducing or even eliminating the need for extensive JavaScript code. This allows the library to avoid issues with large bundles, complex state management, and hydration. This approach offers a more accessible and intuitive way to build modern user interfaces while avoiding the complexities often associated with traditional JavaScript frameworks. As htmx can update specific parts of a webpage without the need to reload the entire page, as would be the case with plain HTML and CSS, using it might result in improved user experience and performance, since only a part of the data needs to be re-fetched from the server.

The library also challenges the common approach of utilizing JSON as the standard payload for HTTP requests by replacing it with HTML. This is meant to solve the issues related to the performance and cognitive overhead of JSON serialization, deserialization, and subsequent use in the user interface, such as JavaScript and JSON's inability to accurately process numbers greater than 253 or distinguish floating-point numbers from integers and the complexity involved with alternatives to JSON-oriented REST, such as GraphQL or gRPC. Additionally, a potential advantage of htmx and hypertext-oriented approach in general, is that data retrieved directly from the database does not need to either be in a JSON or JSON-compliant format, such as that used by many document databases or the PostgreSQL's JSON type, or be serialized by the backend only to be then deserialized by the frontend again. The reduced client-side computation also helps to shift the development focus towards the backend, which might result in better client-side performance, albeit at a cost of higher server load, and providing the developers with a simpler way to solve more problems which they would otherwise solve using client-side JavaScript in virtually any other programming language.

## Usage

htmx adds custom attributes to HTML to define dynamic behavior such as triggering server requests and updating content. The functionality of htmx is built off of the attributes `hx-get`, `hx-post`, `hx-put`, `hx-delete`, and`hx-patch`, which issue AJAX requests with the specified HTTP method. These requests are made when a certain DOM event is fired: `change` for input, select, and textarea elements; `submit` for form elements; and `click` for other elements. The event can also be overridden with `hx-trigger`. Other attributes include `hx-target` for specifying a target other than the current element for swapping content into and `hx-swap` for setting how the content fetched from the server should be swapped or placed relative to the target element.

## Community and adoption

Since its inception as intercooler.js and its subsequent evolution into htmx, the library has gained a significant following within the web development community. htmx has been viewed as a simpler and lighter weight alternative to full-blown JavaScript frameworks like React, Vue.js, and Angular. As a result, it has gained a measure of popularity as an alternative to the approach used by most JavaScript frameworks for building dynamic web applications.

htmx integrations have been developed for various full-stack/backend web frameworks, programming languages and templating engines, including Node.js, Django, Flask, Adobe ColdFusion, ASP.NET, Java, Clojure, and Ruby on Rails. Such libraries are usually a matter of nothing more than convenience since htmx's portable and minimalist design allows it to be integrated with virtually any HTML templating engine.
