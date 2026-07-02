---
title: "container-name CSS property - CSS"
source: https://developer.mozilla.org/en-US/docs/Web/CSS/container-name
domain: css-container-queries
license: CC-BY-SA-4.0
tags: css container queries, container type property, container-name selector, at-container query rule
fetched: 2026-07-02
---

# `container-name` CSS property

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

- Learn more
- See full compatibility

The **container-name** CSS property specifies a list of query container names used by the @container at-rule in a container query.

## Syntax

```css
container-name: none;

/* A single name */
container-name: my-layout;

/* Multiple names */
container-name: my-page-layout my-component-library;

/* Global Values */
container-name: inherit;
container-name: initial;
container-name: revert;
container-name: revert-layer;
container-name: unset;
```

### Values

**`none`**

The default value. The query container has no name.

**`<custom-ident>`**

A case-sensitive string that is used to identify the container. The following conditions apply:

- The name must not equal `or`, `and`, `not`, or `default`.
- The name value must not be in quotes.
- The dashed ident intended to denote author-defined identifiers (e.g., `--container-name`) is permitted.
- A list of multiple names separated by a space is allowed.

## Formal definition

| Initial value | `none` |
|---|---|
| Applies to | all elements |
| Inherited | no |
| Computed value | `none` or an ordered list of identifiers |
| Animation type | Not animatable |

## Formal syntax

```
container-name = 
  none             |
  <custom-ident>+  
```

## Description

With no name specified, a container query will apply styles to elements based on attributes such as the size or scroll-state of the nearest ancestor with a containment context.

**Note:** Size containers' descendants can be sized using container query length units.

When a containment context is given a name, it can be specifically targeted by setting that name on a `@container` at-rule.

It is possible to create a query container by assigning a `container-name` to an element, and then query only the existence of that name in the associated `@container` at-rule, with no query expression specified. These so-called **name-only container queries** enable selectively applying styles to elements based only on whether they have an ancestor with a specific `container-name` set.

## Examples

### Using a container name

Given the following HTML example which is a card component with a title and some text:

```html
<div class="card">
  <div class="post-meta">
    <h2>Card title</h2>
    <p>My post details.</p>
  </div>
  <div class="post-excerpt">
    <p>
      A preview of my <a href="https://example.com">blog post</a> about cats.
    </p>
  </div>
</div>
```

To create a containment context, add the `container-type` property to an element in CSS. The following example creates two containment contexts, one for the card meta information and one for the post excerpt:

**Note:** A shorthand syntax for these declarations are described in the `container` page.

```css
.post-meta {
  container-type: inline-size;
}

.post-excerpt {
  container-type: inline-size;
  container-name: excerpt;
}
```

Writing a container query via the `@container` at-rule will apply styles to the elements of the container when the query evaluates to true. The following example has two container queries, one that will apply only to the contents of the `.post-excerpt` element and one that will apply to both the `.post-meta` and `.post-excerpt` contents:

```css
@container excerpt (width >= 400px) {
  p {
    visibility: hidden;
  }
}

@container (width >= 400px) {
  p {
    font-size: 2rem;
  }
}
```

For more information on writing container queries, see the CSS Container Queries page.

### Using multiple container names

You can also provide multiple names to a container context separated by a space:

```css
.post-meta {
  container-type: inline-size;
  container-name: meta card;
}
```

This will allow you to target the container using either name in the `@container` at-rule. This is useful if you want to target the same container with multiple container queries where either condition could be true:

```css
@container meta (width <= 500px) {
  p {
    visibility: hidden;
  }
}

@container card (width <= 200px) {
  h2 {
    font-size: 1.5em;
  }
}
```

### Using a name-only container query

This example demonstrates how to use a name-only container query.

#### HTML

We include a `<div>` with an `id` of `container`, and three `<p>` elements, two inside the container, and one outside the container:

```html
<div id="container">
  <p>I'm in the container.</p>
  <p>I'm also in the container.</p>
</div>
<p>I'm not in the container.</p>
```

#### CSS

We assign a name to the container:

```css
#container {
  container-name: my-container;
}
```

We can then selectively apply styles only to elements inside containers with that name set, as shown in the next snippet.

```css
@container my-container {
  p {
    background-color: lime;
    font-size: 1.3rem;
    width: 50vw;
    padding: 0.5rem;
    font-family: sans-serif;
  }
}
```

#### Result

The specified styles should be applied only to the first and second `<p>` elements, but not to the third.

## Specifications

| Specification |
|---|
| CSS Conditional Rules Module Level 5 # container-name |

## Browser compatibility
