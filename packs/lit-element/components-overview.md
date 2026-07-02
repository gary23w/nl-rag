---
title: "Components overview"
source: https://lit.dev/docs/components/overview/
domain: lit-element
license: CC-BY-SA-4.0 / BSD (lit.dev)
tags: lit element, lit html, reactive web component, lit template
fetched: 2026-07-02
---

# Components overview

A Lit component is a reusable piece of UI. You can think of a Lit component as a container that has some state and that displays a UI based on its state. It can also react to user input, fire events—anything you'd expect a UI component to do. And a Lit component is an HTML element, so it has all of the standard element APIs.

Creating a Lit component involves a number of concepts:

- Defining a component. A Lit component is implemented as a *custom element*, registered with the browser.
- Rendering. A component has *render method* that's called to render the component's contents. In the render method, you define a *template* for the component.
- Reactive properties. Properties hold the state of the component. Changing one or more of the components' *reactive properties* triggers an update cycle, re-rendering the component.
- Styles. A component can define *encapsulated styles* to control its own appearance.
- Lifecycle. Lit defines a set of callbacks that you can override to hook into the component's lifecycle—for example, to run code when the element's added to a page, or whenever the component updates.

Here's a sample component:

This example uses TypeScript decorators.

See the Decorators documentation for more information on configuring TypeScript for decorators.

Previous

Getting Started

Next

Defining a component
