---
title: "Web Components"
source: https://en.wikipedia.org/wiki/Web_Components
domain: vaadin-flow
license: CC-BY-SA-4.0
tags: vaadin flow framework, java server side ui, jvm web components, vaadin component model
fetched: 2026-07-02
---

# Web Components

**Web Components** are a set of features that provide a standard component model for the web allowing for encapsulation and interoperability of individual HTML elements. Web Components are a popular approach when building microfrontends.

Primary technologies used to create Web Components include:

**Custom elements**

APIs to define new HTML elements

**Shadow DOM**

encapsulated DOM and styling, with composition

**HTML templates**

HTML fragments that are not rendered, but stored until

instantiated

via JavaScript

## Features

### Custom elements

There are two parts to Custom Elements: autonomous custom elements and customized built-in elements. Autonomous custom elements are HTML elements that are entirely separated from native HTML elements; they are essentially built from the bottom up using the Custom Elements API. Customized built-in elements are elements that are built upon native HTML elements to reuse their functionality.

### Shadow DOM

The Shadow DOM is a functionality that allows the web browser to render DOM elements without putting them into the main document DOM tree. This creates a barrier between what the developer and the browser can reach; the developer cannot access the Shadow DOM in the same way they would with nested elements, while the browser can render and modify that code the same way it would with nested elements. The impact of CSS scoped within the Shadow DOM of a particular element is that HTML elements can be encapsulated without the risk of CSS styles leaking and affecting elements that they were not supposed to affect. Although these elements are encapsulated with regard to HTML and CSS, they can still fire events that can be picked up by other elements in the document.

The scoped subtree in an element is called a shadow tree. The element the shadow tree is attached to is called a shadow host.

A Shadow DOM must always be connected to an existing element, either through attaching it as a literal element or through scripting. In JavaScript, Shadow DOMs are attached to an element using `Element.attachShadow()`.

### HTML template

An HTML template defines a block of HTML content that is not rendered when the page loads, but can be instantiated during runtime. A template element is structured as follows:

```mw
<template>
    <h1>Title</h1>
    <p>Description</p>
</template>
```

Scripts within a template do not run, and resources are not fetched, until the content is cloned or added to the DOM.

## Browser support

Web Components are supported by current versions of all major browsers.

Backward compatibility with older browsers is implemented using JavaScript-based polyfills.

## Libraries

There are many libraries that are built on Web Components with the aim of increasing the level of abstraction when creating custom elements. Some of these libraries are X-Tag, Slim.js, Polymer, Bosonic, Riot.js, Salesforce Lightning Web Components, DataFormsJS, Telepathy, and Wompo

## Community

There are numerous community efforts for the Web Components ecosystem. WebComponents.org provides an interface to search for any existing Web Components. Custom Elements Everywhere validates whether popular front-end frameworks are compatible and ready to use Web Components standard, with a set of pending bugs and available workarounds. Moreover, Vaadin Tutorials has a dedicated section that shows how those workarounds are used efficiently with example demo apps and similarly related topics.

## History

In 2011, Web Components were introduced for the first time by Alex Russell at Fronteers Conference.

In 2013, Polymer, a library based on Web Components was released by Google. Polymer is canonical implementation of Material Design for web application user interfaces.

In 2016, RequireJS was introduced as JavaScript library and AMD loader plugin for custom elements.

In 2017, Ionic (mobile app framework) team built StencilJS, a JavaScript compiler that generates Web Components.

In 2018, Angular 6 introduced Angular Elements that lets you package your Angular components as custom web elements, which are part of the web components set of web platform APIs.

In 2018, Firefox 63 enabled Web Components support by default and updated the developer tools to support them.

In 2018, LitElement was developed by the Google Chrome team as part of larger Polymer project. LitElement was designed to be a lightweight and easy-to-use framework for creating web components.
