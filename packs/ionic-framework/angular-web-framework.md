---
title: "Angular (web framework)"
source: https://en.wikipedia.org/wiki/Angular_(web_framework)
domain: ionic-framework
license: CC-BY-SA-4.0
tags: ionic framework, hybrid mobile toolkit, web component controls, cordova capacitor shell
fetched: 2026-07-02
---

# Angular (web framework)

**Angular** (also referred to as **Angular 2+**) is a TypeScript-based free and open-source single-page web application framework. It is developed by Google and by a community of individuals and corporations. Angular is a complete rewrite from the same team that built AngularJS. The Angular ecosystem consists of a diverse group of over 1.7 million developers, library authors, and content creators. According to the Stack Overflow Developer Survey, Angular is one of the most commonly used web frameworks.

## Differences between Angular and AngularJS

Google designed Angular as a ground-up rewrite of AngularJS. Unlike AngularJS, Angular does not have a concept of "scope" or controllers; instead, it uses a hierarchy of components as its primary architectural characteristic. Angular has a different expression syntax, focusing on `"[ ]"` for property binding, and `"( )"` for event binding. Angular recommends the use of Microsoft's TypeScript language, which introduces features such as static typing, generics, and type annotations.

## Features

### Component-based architecture

Angular uses a component-based architecture, which allows developers to build encapsulated, reusable user interface elements. Each component encapsulates its own HTML, CSS, and TypeScript, making it easier to manage and test individual pieces of an application.

### Data binding

Angular supports two-way data binding which synchronizes data between the model and the view. This ensures that any changes in the view are automatically reflected in the model and vice versa.

### Dependency injection

Angular has a built-in dependency injection system that makes it easier to manage and inject dependencies into components and services. This promotes modularity and easier testing.

### Directives

Angular extends HTML with additional attributes called directives. Directives offer functionality to change the behavior or appearance of DOM elements.

### Routing

Angular includes a router that allows developers to define and manage application states and navigation paths, making it easier to build single-page applications with complex routing.

### Angular CLI

The Angular CLI (Command Line Interface) provides a set of tools for creating, building, testing, and deploying Angular applications. It enables rapid application setup and simplifies ongoing development tasks.

### Server-side rendering

Angular has official support for server-side rendering, which improves an application's load time and performance. Server-side rendering also enhances search engine optimization by making content more accessible to web crawlers.

## History

Angular 2.0 was announced during the keynote of the 2014 NG-Conf conference 16–17 January 2014. On April 30, 2015, the Angular developers announced that Angular 2 moved from Alpha to Developer Preview. Angular 2 moved to Beta in December 2015, and the first release candidate was published in May 2016. The final version was released on 14 September 2016.

Version 8 of Angular introduced a new compilation and rendering pipeline, Ivy, and version 9 of Angular enabled Ivy by default. Angular 13 removed the deprecated former compiler, View Engine. Angular 14 introduced standalone components and Angular 17 made them the default, de-emphasizing the use of modules.

Angular 18, released in 2024, introduced several improvements such as standalone components defaulting to true, built-in control flow syntax, zoneless support previews, and modern SSR debugging tools.[44]

### Naming

The rewrite of AngularJS was called "Angular 2", but this led to confusion among developers. To clarify, the team announced that separate names should be used for each framework with "AngularJS" referring to the 1.X versions and "Angular" without the "JS" referring to versions 2 and up.

### Version history

| Version | Release date | New features |
|---|---|---|
| Latest version: Angular 22 | June 3, 2026 | Stable Signal forms and Stable accessible components with Angular ARIA. |
| Supported: Angular 21 | November 19, 2025 | Experimental Signal forms, Experimental accessible components with Angular ARIA and Zoneless by default |
| Supported: Angular 20 | May 28, 2025 | by default Angular CLI will not generate suffixes for components, directives, services, and pipes. |
| Unsupported: Angular 19 | November 19, 2024 | Angular directives, components and pipes are now standalone by default. |
| Unsupported: Angular 18 | May 22, 2024 | Experimental zoneless change detection support and server-side rendering improvements. |
| Unsupported: Angular 17 | November 8, 2023 | Standalone is now the new default for the CLI (Application builder), without the need for Angular modules (NgModule), a new syntax for control flow and documentation website. |
| Unsupported: Angular 16 | 3 May 2023 | Partial hydration for Angular Universal server-side rendering, experimental Jest support, and esbuild-based build system for development servers. |
| Unsupported: Angular 15 | November 18, 2022 | Standalone APIs, directive composition API. |
| Unsupported: Angular 14 | 2 June 2022 | Typed forms, standalone components, and new primitives in the Angular CDK (component dev kit). |
| Unsupported: Angular 13 | 4 November 2021 | Removed deprecated View Engine renderer. |
| Unsupported: Angular 12 | 12 May 2021 | Deprecated support for Internet Explorer 11. |
| Unsupported: Angular 11 | 11 November 2020 | Experimental Webpack 5 support |
| Unsupported: Angular 10 | 24 June 2020 | New Date Range Picker (Material UI library). |
| Unsupported: Angular 9 | 6 February 2020 | Improved build times, enabling AOT on by default |
| Unsupported: Angular 8 | 28 May 2019 | Differential loading for all application code, Dynamic imports for lazy routes, Web workers, TypeScript 3.4 support, and Angular Ivy as an opt-in preview. |
| Unsupported: Angular 7 | 18 October 2018 | Updates regarding Application Performance, Angular Material & CDK, Virtual Scrolling, Improved Accessibility of Selects. Support for Content Projection using web standard for custom elements, and dependency updates regarding TypeScript 3.1, RxJS 6.3 and Node.js 10. |
| Unsupported: Angular 6 | 4 May 2018 | Experimental custom element support, added ng update command |
| Unsupported: Angular 5 | 1 November 2017 | Support for progressive web apps, a build optimizer and improvements related to Material Design. |
| Unsupported: Angular 4.3 | 18 July 2017 | HttpClient for making HTTP requests, conditionally disabling animations, new router life cycle events for Guards and Resolvers. Minor release, meaning that it contains no breaking changes and that it is a drop-in replacement for Angular 4.x.x. |
| Unsupported: Angular 4 | 23 March 2017 | Added ngIf and ngFor. Backward compatible with Angular 2. |
| Unsupported: Angular 2 | 14 September 2016 | Initial release |

### Future releases

Since v9, the Angular team has moved all new applications to use the Ivy compiler and runtime. They will be working on Ivy to improve output bundle sizes and development speeds.

Each version is expected to be backward-compatible with the prior release. The Angular development team has pledged to do twice-a-year upgrades.

### Support policy and schedule

All the major releases are supported for 18 months. This consists of 6 months of active support, during which regularly scheduled updates and patches are released. It is then followed by 12 months of long-term support (LTS), during which only critical fixes and security patches are released.

| Version | Status | Released | Active Ends | LTS Ends | Duration |
|---|---|---|---|---|---|
| ^21.0.0 | Active | November 19, 2025 | May 19, 2026 | May 19, 2027 | 1.5 years |
| ^20.0.0 | LTS | May 28, 2025 | Nov 21, 2025 | Nov 21, 2026 | 1.5 years |

Angular versions v2 to v19 are no longer under support.

## Associated projects

Analog is a full stack web meta-framework based upon Angular powered by Vite and Nitro.

## Libraries

### Angular Material

Angular Material is a UI component library that implements Material Design in Angular. It provides a collection of reusable components that adhere to Google's Material Design specifications, aiming to offer a consistent user interface across different devices and platforms.

Angular Material includes a variety of UI components such as buttons, cards, dialogs, grids, and form controls. These components are designed to be customizable and easy to integrate into Angular applications. Additional features of Angular Material include support for responsive design, theming, and accessibility.

### Angular Elements

In 2018, Angular 6 introduced Angular Elements, enabling developers to package Angular components as custom web elements, which are part of the web components set of web platform APIs.
