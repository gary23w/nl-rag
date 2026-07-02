---
title: "State management"
source: https://en.wikipedia.org/wiki/State_management
domain: mobx
license: CC-BY-SA-4.0 / MIT (mobx.js.org)
tags: mobx, observable state, transparent reactivity, mobx reaction
fetched: 2026-07-02
---

# State management

**State management** refers to the management of the state of one or more user interface controls such as text fields, submit buttons, radio buttons, etc. in a graphical user interface. In this user interface programming technique, the state of one UI control depends on the state of other UI controls. For example, a state-managed UI control such as a button will be in the enabled state when input fields have valid input values, and the button will be in the disabled state when the input fields are empty or have invalid values. As applications grow, this can end up becoming one of the most complex development problems.

This is especially the case when the state of any particular message or form on the page depends on factors outside of the current page, or available throughout several pages. For example, consider a user who is logged in and sees the 'welcome' message on their first visit to any page, but not on subsequent page visits. Does each page manage the state of the user being logged in? That would create too much copy pasting and duplication of code. Instead, you can use a state management pattern for handling messages (this may also include handling error messages and informative messages, along with the described welcome message) and then call this to receive a message as it becomes available.

Examples of state management libraries include Pinia as a state management library for the Vue.js JavaScript framework. For the Angular framework there exist multiple community options: NgRx (based on Redux, with a lightweight alternative using Signals), NGXS and RxAngular. Redux is a general-purpose state management library that can be used with any of the above frameworks or other view libraries, but is very commonly used with the React library. As the documentation in Redux alludes, many of these state management libraries are lightweight and can be replaced by each other. It's also possible to roll your own based on a publish–subscribe pattern where your interface components (like form fields, buttons, and messages) listen to a centralized data store in your application for new changes.
