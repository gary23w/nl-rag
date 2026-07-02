---
title: "CSS: registerProperty() static method - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static
domain: css-houdini
license: CC-BY-SA-4.0
tags: css houdini apis, css painting worklet, css properties and values api, registered custom property
fetched: 2026-07-02
---

# CSS: registerProperty() static method

Baseline

2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

- Learn more
- See full compatibility

The **`CSS.registerProperty()`** static method registers custom properties, allowing for property type checking, default values, and properties that do or do not inherit their value.

Registering a custom property allows you to tell the browser how the custom property should behave; what types are allowed, whether the custom property inherits its value, and what the default value of the custom property is.

## Syntax

```js
CSS.registerProperty(propertyDefinition)
```

### Parameters

**`propertyDefinition`**

An object containing the following properties:

**`name`**

A string representing the `<dashed-ident>` name of the property being defined.

**`syntax` Optional**

A string representing the expected syntax of the defined property. Defaults to `"*"`. See the `syntax`.

**`inherits`**

A boolean value defining whether the defined property should be inherited (`true`), or not (`false`). Defaults to `false`.

**`initialValue` Optional**

A string representing the initial value of the defined property.

### Return value

`undefined`.

### Exceptions

**`InvalidModificationError` `DOMException`**

The given `name` has already been registered.

**`SyntaxError` `DOMException`**

The given `name` isn't a valid custom property name (starts with two dashes, e.g., `--foo`).

**`TypeError`**

The required `name` and/or `inherits` dictionary members were not provided.

## Examples

The following will register a custom property, `--my-color`, using `registerProperty()`, as a color, give it a default value, and have it not inherit its value:

```js
window.CSS.registerProperty({
  name: "--my-color",
  syntax: "<color>",
  inherits: false,
  initialValue: "#c0ffee",
});
```

In this example, the custom property `--my-color` has been registered using the syntax `<color>`. We can now use that property to transition a gradient on hover or focus. Notice that with the registered property, the transition works, but it doesn't work with the unregistered property!

```css
.registered {
  --my-color: #c0ffee;
  background-image: linear-gradient(to right, white, var(--my-color));
  transition: --my-color 1s ease-in-out;
}

.registered:hover,
.registered:focus {
  --my-color: #b4d455;
}

.unregistered {
  --unregistered: #c0ffee;
  background-image: linear-gradient(to right, white, var(--unregistered));
  transition: --unregistered 1s ease-in-out;
}

.unregistered:hover,
.unregistered:focus {
  --unregistered: #b4d455;
}
button {
  font-size: 3vw;
}
```

We can add these styles to some buttons:

```html
<button class="registered">Background Registered</button>
<button class="unregistered">Background Not Registered</button>
```

## Specifications

| Specification |
|---|
| CSS Properties and Values API Level 1 # the-registerproperty-function |

## Browser compatibility
