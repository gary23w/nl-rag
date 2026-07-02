---
title: "Mustache (template system)"
source: https://en.wikipedia.org/wiki/Mustache_(template_system)
domain: mustache-templating
license: CC-BY-SA-4.0
tags: mustache templating, mustache template system, logic-less templates, web template rendering
fetched: 2026-07-02
---

# Mustache (template system)

**Mustache** is a web template system. It is described as a *logic-less* system because it lacks any explicit control flow statements, like `if` and `else` conditionals or for loops; however, both looping and conditional evaluation can be achieved using section tags processing lists and anonymous functions (lambdas). It is named "Mustache" because of heavy use of braces, `{ }`, that resemble a sideways moustache. Mustache is used mainly for mobile and web applications.

Implementations are available in ActionScript, C++, Clojure, CoffeeScript, ColdFusion, Common Lisp, Crystal, D, Dart, Delphi, Elixir, Erlang, Fantom, Go, Haskell, Io, Java, JavaScript, Julia, Lua, .NET, Objective-C, OCaml, Perl, PHP, Pharo, Python, R, Racket, Raku, Ruby, Rust, Scala, Smalltalk, Swift, Tcl, CFEngine, and XQuery.

## History and principles

*Mustache-1* was inspired by ctemplate and et, and began as a GitHub distribution at the end of 2009. A first version of the template engine was implemented with Ruby, running YAML template texts. The (preserved) main principles were:

- *Logic-less*: no explicit control flow statements, all control driven by data.
- Strong *separation of concerns: logic from presentation*: it is impossible to embed application logic in the templates.

The input data can be a class so that input data can be characterized as a model–view–controller (MVC) view. The Mustache *template* does nothing but reference methods in the (input data) *view*. All the logic, decisions, and code is contained in this *view*, and all the markup (ex. output XML) is contained in the *template*. In a model–view–presenter (MVP) context: input data is from MVP-*presenter*, and the Mustache template is the MVP-*view*.

## Examples

### Data

JSON data is fed to Mustache templates, resulting in an output. Here is some example data:

```mw
{
    "name": "World",
    "greater than": ">"
}
```

### Variables

A simple Mustache template such as the one below, combined with the above data, would output `Hello World`.

```mw
Hello {{name}}
```

Mustache HTML escapes data by default. For example, the below would render as `2 &gt; 1`.

```mw
2 {{greater than}} 1
```

To turn off escaping, use a `&`. The below would render as `2 > 1`.

```mw
2 {{&greater than}} 1
```

### If statements and foreach loops

Below is a template with section tag. When `x` is a Boolean value, the section tag acts like an *if* conditional. When `x` is an array, it acts like a foreach loop.

```mw
{{#x}}
Some text
{{/x}}
```

The special variable `{{.}}` refers to the current item when looping through an array, or the item checked in a conditional.

### Including other templates

You can tell a Mustache template to load another Mustache template within it using the `>` symbol.

```mw
<form>
    {{>textBox}}
    {{>submitButton}}
</form>
```

Comments are indicated using an exclamation mark.

```mw
{{!comment goes here}}
```

## Technical details

Syntax highlighting is available in Atom, Coda, Emacs, TextMate, Vim and Visual Studio Code.

Mustache template support is built into many web application frameworks (ex. CakePHP). Support in JavaScript includes both client-side programming with many JavaScript libraries and Ajax frameworks such as jQuery, Dojo and YUI, as well as server-side JavaScript using Node.js and CommonJS.

### Specification and implementations

There are many *Mustache Engine* implementations available, and all of them meet a common formal specification (see external links), that for final users results in the common syntax.

As of May 2026, the last SPEC_VERSION was 1.4.3.

## Variations and derivatives

Mustache inspired numerous JavaScript template libraries which forked from the original simplicity to add certain functionality or use.

### Handlebars

Handlebars.js is self-described as:

> Handlebars.js is an extension to the Mustache templating language created by Chris Wanstrath. Handlebars.js and Mustache are both logicless templating languages that keep the view and the code separated like we all know they should be.

Handlebars differs from its predecessor in that, within *Block Expressions* (similar to sections in Mustache), *Helpers* allow custom function through explicit user-written code for that block.
