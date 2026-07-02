---
title: "Virtual DOM"
source: https://en.wikipedia.org/wiki/Virtual_DOM
domain: preact
license: CC-BY-SA-4.0
tags: preact, lightweight react alternative, virtual dom library, small react runtime
fetched: 2026-07-02
---

# Virtual DOM

A **virtual DOM** is a lightweight JavaScript representation of the Document Object Model (DOM) used in declarative web frameworks such as React, Vue.js, and Elm. Since generating a virtual DOM is relatively fast, any given framework is free to rerender the virtual DOM as many times as needed relatively cheaply. The framework can then find the differences between the previous virtual DOM and the current one (diffing), and only makes the necessary changes to the actual DOM (reconciliation). While technically slower than using just vanilla JavaScript, the pattern makes it much easier to write websites with a lot of dynamic content, since markup is directly coupled with state.

Similar techniques include Ember.js' Glimmer and Angular's incremental DOM.

## History

The JavaScript DOM API has historically been inconsistent across browsers, clunky to use, and difficult to scale for large projects. While libraries like jQuery aimed to improve the overall consistency and ergonomics of interacting with HTML, it too was prone to repetitive code that didn't describe the nature of the changes being made well and decoupled logic from markup.

The release of AngularJS in 2010 provided a major paradigm shift in the interaction between JavaScript and HTML with the idea of dirty checking. Instead of imperatively declaring and destroying event listeners and modifying individual DOM nodes, changes in variables were tracked and sections of the DOM were invalidated and rerendered when a variable in their scope changed. This digest cycle provided a framework to write more declarative code that coupled logic and markup in a more logical way.

While AngularJS aimed to provide a more declarative experience, it still required data to be explicitly bound to and watched by the DOM, and performance concerns were cited over the expensive process of dirty checking hundreds of variables. To alleviate these issues, React was the first major library to adopt a virtual DOM in 2013, which removed both the performance bottlenecks (since diffing and reconciling the DOM was relatively cheap) and the difficulty of binding data (since components were effectively just objects). Other benefits of a virtual DOM included improved security since XSS was effectively impossible and better extensibility since a component's state was entirely encapsulated. Its release also came with the advent of JSX, which further coupled HTML and JavaScript with an XML-like syntax extension.

Following React's success, many other web frameworks copied the general idea of an ideal DOM representation in memory, such as Vue.js in 2014, which used a template compiler instead of JSX and had fine-grained reactivity built as part of the framework.

In recent times, the virtual DOM has been criticized for being slow due to the additional time required for diffing and reconciling DOM nodes. This has led to the development of frameworks without a virtual DOM, such as Svelte, and frameworks that edit the DOM in-place such as Angular 2.

## Implementations

### React

React pioneered the use of a virtual DOM to make components declaratively. Virtual DOM nodes are constructed using the `createElement()` function, but are often transpiled from JSX to make writing components more ergonomic. In class-based React, virtual DOM nodes are returned from the `render()` function, while in functional hook-based components, the return value of the function itself serves as the page markup.

### Vue.js

Vue.js uses a virtual DOM to handle state changes, but is usually not directly interacted with; instead, a compiler is used to transform HTML templates into virtual DOM nodes as an implementation detail. While Vue supports writing JSX and custom render functions, it's more typical to use the template compiler since a build step isn't required that way.

### Svelte

Svelte does not have a virtual DOM, with its creator Rich Harris calling the virtual DOM "pure overhead". Instead of diffing and reconciling DOM nodes at runtime, Svelte uses compile-time reactivity to analyze markup and generate JavaScript code that directly manipulates the DOM, drastically increasing performance.
