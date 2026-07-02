---
title: "Introduction"
source: https://handlebarsjs.com/guide/
domain: handlebars-templating
license: CC-BY-SA-4.0
tags: handlebars templating, handlebars template engine, logic-less templates, web template rendering
fetched: 2026-07-02
---

# Introduction 

## What is Handlebars? 

Handlebars is a simple **templating language**.

It uses a template and an input object to generate HTML or other text formats. Handlebars templates look like regular text with embedded Handlebars expressions.

template

Click to try out

A handlebars expression is a `{{`, some contents, followed by a `}}`. When the template is executed, these expressions are replaced with values from an input object.

Learn More: Expressions

## Installation 

The fastest way to test Handlebars is to load it from a *CDN* and embed it in an HTML file.

html

```html
<!-- Include Handlebars from a CDN -->
<script src="https://cdn.jsdelivr.net/npm/handlebars@latest/dist/handlebars.js"></script>
<script>
  // compile the template
  var template = Handlebars.compile("Handlebars <b>{{doesWhat}}</b>");
  // execute the compiled template and print the output to the console
  console.log(template({ doesWhat: "rocks!" }));
</script>
```

WARNING

This method can be used for small pages and for testing. There are several other ways to use Handlebars, when you target real production systems.

Learn more: Installation

## Language features 

### Simple expressions 

As shown before, the following template defines two Handlebars expressions

template

Click to try out

If applied to the input object

input

Click to try out

the expressions will be replaced by the corresponding properties. The result is then

output

Click to try out

### Nested input objects 

Sometimes, the input objects contains other objects or arrays. For example:

input

Click to try out

In such a case, you can use a dot-notation to gain access to the nested properties

template

Click to try out

Learn more: Expressions

Some built-in helpers allow you to change the current context to a nested object. You can then access this object as if it were the root object

### Evaluation context 

The built-in block-helpers `each` and `with` allow you to change the current evaluation context.

The `with`-helper dives into an object-property, giving you access to its properties

template

Click to try out

input

Click to try out

The `each`-helper iterates an array, allowing you to access the properties of each object via simple handlebars expressions.

template

Click to try out

input

Click to try out

Learn more: Built-in helpers

You can use comments in your handlebars code just as you would in your code. Since there is generally some level of logic, this is a good practice.

The comments will not be in the resulting output. If you'd like the comments to show up just use HTML comments, and they will be output.

Any comments that must contain `}}` or other handlebars tokens should use the `{{!-- --}}` syntax.

template

Click to try out

### Custom Helpers 

Handlebars helpers can be accessed from any context in a template. You can register a helper with the Handlebars.registerHelper method.

template

Click to try out

preparationScript

Click to try out

Helpers receive the current context as the `this`-context of the function.

template

Click to try out

preparationScript

Click to try out

### Block Helpers 

Block expressions allow you to define helpers that will invoke a section of your template with a different context than the current. These block helpers are identified by a `#` preceeding the helper name and require a matching closing mustache, `/`, of the same name. Let's consider a helper that will generate an HTML list:

preparationScript

Click to try out

The example creates a helper named `list` to generate our HTML list. The helper receives the `people` as its first parameter, and an `options` hash as its second parameter. The options hash contains a property named `fn`, which you can invoke with a context just as you would invoke a normal Handlebars template.

When executed, the template will render:

output

Click to try out

Block helpers have more features, such as the ability to create an `else` section (used, for instance, by the built-in `if` helper).

Since the contents of a block helper are escaped when you call `options.fn(context)`, Handlebars does not escape the results of a block helper. If it did, inner content would be double-escaped!

Learn More: Block Helpers

### HTML Escaping 

Because it was originally designed to generate HTML, Handlebars escapes values returned by a `{{expression}}`. If you don't want Handlebars to escape a value, use the "triple-stash", `{{{`.

template

Click to try out

The special characters in the second line will be escaped:

output

Click to try out

Handlebars will not escape a `Handlebars.SafeString`. If you write a helper that generates its own HTML, you will usually want to return a `new Handlebars.SafeString(result)`. In such a circumstance, you will want to manually escape parameters.

preparationScript

Click to try out

This will escape the passed in parameters, but mark the response as safe, so Handlebars will not try to escape it even if the "triple-stash" is not used.

WARNING

Handlebars does not escape JavaScript strings. Using Handlebars to generate JavaScript, such as inline event handlers, could potentially lead to cross-site scripting vulnerabilities.

### Partials 

Handlebars partials allow for code reuse by creating shared templates. You can register a partial using the `registerPartial`-method:

preparationScript

Click to try out

The following template and input:

template

Click to try out

input

Click to try out

will then provide the following result:

output

Click to try out

Learn More: Partials

### Built-In Helpers 

Handlebars offers a variety of built-in helpers such as the if conditional and each iterator.

Learn More: Built-In Helpers

### API Reference 

Handlebars offers a variety of APIs and utility methods for applications and helpers.

Learn More: API Reference
