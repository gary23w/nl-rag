---
title: "Ember.js"
source: https://en.wikipedia.org/wiki/Ember.js
domain: emberjs
license: CC-BY-SA-4.0
tags: ember.js, emberjs, handlebars templates, convention over configuration ui
fetched: 2026-07-02
---

# Ember.js

**Ember.js** is an open-source JavaScript web framework that utilizes a component-service pattern. It is designed with the aim to allow developers to create scalable single-page web applications by incorporating common idioms, best practices, and patterns from other single-page-app ecosystem patterns into the framework.

Ember is used on websites including HashiCorp, DigitalOcean, Apple Music, Square, Inc., Intercom, Discourse, Groupon, LinkedIn, Live Nation, Ghost, Nordstrom, and Twitch. Although primarily considered a framework for the web, it is also possible to build desktop and mobile applications with Ember when utilizing a hybrid app pattern. The most notable example of an Ember desktop application is Apple Music, a feature of the iTunes desktop application.

The Ember trademark is owned by Tilde Inc.

## History

In December 2011, the SproutCore 2.0 framework was renamed to Ember.js, to reduce confusion between the application framework and the widget library of SproutCore 1.0. The framework was created by Yehuda Katz who was a member of the jQuery, Ruby on Rails and SproutCore core teams.

## Design

According to the company, Ember was designed around four key ideas:

**Web applications**

Ember sets out to provide a solution to the client-side application problem.

**More productivity**

Ember is one component of a set of tools to provide a development stack. Ember CLI provides an application structure and build pipeline with an add-on.

**Stability**

Ember aims to prioritize backward compatibility and allow it to be maintained while still evolving the framework.

**Future web standards**

Ember was an adopter of standards around JavaScript and the web, including promises,

web components

and ES6 syntax.

Yehuda Katz, one of Ember's co-founders, is a member on TC39, which is the committee responsible for future versions of the JavaScript language.

Like Ruby on Rails, Ember follows *convention over configuration* (CoC), and the *don't repeat yourself* (DRY) principle. It has been described as a highly opinionated framework built to be very flexible.

## Concepts

According to the company, Ember consists of five key concepts:

**Routes**

In Ember, the state of an application is represented by a URL. Each URL has a corresponding "route object" that controls what is visible to the user.

**Models**

Every route has an associated model, containing the data associated with the current state of the application.

While one can use window.fetch to load

JSON

objects from a server and use those objects as models, most applications use a model library such as Ember Data to handle this.

**Templates**

Templates are used to build the application's HTML and are written with the

HTMLBars

templating language. (HTMLBars is a variation of

Handlebars

that builds DOM elements rather than a String.)

**Components**

A component is a custom HTML tag. Its behavior is implemented using JavaScript, and its appearance is defined using HTMLBars templates. Components "own" their data. They can also be nested and can communicate with their parent components through actions (events). Other component libraries, such as Polymer can also be used with Ember.

**Services**

Services are just singleton objects to hold long-lived data such as user sessions.

Ember also provides

dependency injection

,

declarative

one-way data-flow, tracked properties, and automatically updating

templates

.

## Ember software / Addons

Ember.js is one component of a complete front-end stack built and supported by the Ember core team.

### Ember CLI

Ember-CLI aims to bring convention over configuration to build tools. A command line utility based on broccoli, running the command `ember new <app-name>` generates a new Ember app with the default stack. This provides:

- Standard file and directory structure
- Development server with live reload
- Testing framework
- Dependencies managed via npm.
- ES6/ES7+ syntax support (using Babel)
- Asset management (including combining, minifying, and versioning)

Other features include:

- Blueprints, which are code generators for creating models, controllers, components, and so on that are needed in an application. Custom blueprints can also be created.
- Addons, which provide the ability to extend the features of Ember CLI,. Addons are installed by typing `ember install <addon-name>`. Around two thousand add-ons are currently available (as of 2018) including add-ons for CoffeeScript, LESS, Sass, Compass and Mocha.

### Ember Data

Most Ember applications use Ember Data, a data-persistence library providing many of the facilities of object-relational mapping (ORM). However it is also possible to use Ember without Ember Data.

Ember Data maps client-side models to server-side data. It can then load and save records and their relationships without any configuration via a RESTful JSON API that implements the JSON API specification, provided certain conventions are followed. However it is also configurable and can work with servers through the use of adapters and addons. JSON API has server library implementations for PHP, Node.js, Ruby, Python, Go, .NET and Java. Connecting to a Java-Spring-based server is also documented.

The first stable version of Ember Data (labeled 1.13 to align with Ember itself) was released on June 18 June 2015.

### Ember Inspector

The Ember Inspector is an extension currently available for the Mozilla Firefox and Google Chrome web browsers for debugging Ember applications. Features include the ability to see which templates, components, and views are currently rendered, see the properties of any Ember object with a UI that computes bindings and computed properties, and access one's application's objects from the console. If Ember Data is used, one can also see the records loaded for each model.

- The Object Inspector allows viewing and editing of the runtime contents of Ember Objects and Classes.
- The View Tree visually displays the structure of the rendered Ember application.
- The Routes tab allows one to determine and follow the router state and the URLs used to represent routes.
- The Data tab shows the models in the application and the records loaded for each model.
- The Info tab displays dependency versions.
- The Deprecations tab allows for stack traces of deprecation warnings that do not trigger exceptions.
- The Promises tab allows for the tracing of code through asynchronous operations.
- The Container tab is used to check which objects have been loaded.
- The Render Performance tab is for determining what is slowing down an Ember application.

### Fastboot

Fastboot is an Ember CLI add-on created by the Ember core team that gives Ember developers the ability to run their apps in Node.js. This feature allows end users to see HTML and CSS right away, with JavaScript downloading in the background and taking over once it has fully loaded.

### Liquid Fire

Liquid Fire provides animation support for Ember applications. Features include animated transitions between routes and between models within a single route. It provides a DSL for solidifying spatial route relationships, cleanly separated from view-layer implementation details. An example would be to animate a screen transition so that the new screen appears to slide in from one edge of the browser.

## Release process

See the releases blog for the full list of releases and detailed changelog.

### Release cycle

Ember follows a six-week release cycle, inspired by the rapid release cycle of Google Chrome.

Starting with Ember 2.0, related projects supported by the core team have their releases coordinated, and share a version number with Ember itself.

### Upgrading and backward compatibility

Ember follows the semantic versioning convention. In particular, breaking changes are only introduced at significant version numbers, such as 1.0, 2.0, etc. While new features can be added at point releases (1.1, 1.2...), and features deprecated, no breaking changes to the public APIs are introduced. Tooling was also under development in 2015 to help streamline the upgrade process.

In addition to this process, several steps were taken to mitigate issues around upgrading to the 2.0 release:

- All major 2.0 features were introduced early and spread out over several releases to reduce many of the issues caused by upgrades.
- Most features that were removed are still available through add-ons.

The process follows the core Ember principle of Stability without Stagnation and is in marked contrast to the upgrade plans of similar projects such as AngularJS.

## Future development

Project status can be tracked via the core team meeting minutes. However, major changes to Ember go through the Request For Comment process. This gives the Ember community a chance to give feedback on new proposals. Notable RFCs include:

- Engines. Engines allow multiple logical applications to be composed together into a single application from the user's perspective. Currently released as an experimental add-on.
- Release cycle improvements. Among other things, it proposes changes to Ember CLI to support "svelte builds", which will strip out deprecated and unused features.
- Outlet Focusing. Making Ember accessible by default. This RFC aims to improve the user experience for people using screen readers.

## Sponsorship

Unlike other projects such as AngularJS (Google) and React (Facebook) which have the backing of one main company, Ember.js has a variety of sponsors and backers. These include users of the framework such as Yahoo!, LinkedIn and Bustle.
