---
title: "Sass (style sheet language)"
source: https://en.wikipedia.org/wiki/Sass_(style_sheet_language)
domain: sass-scss
license: CC-BY-SA-4.0
tags: sass, scss, css preprocessor, sass mixin, sass nesting
fetched: 2026-07-02
---

# Sass (style sheet language)

**Sass** (short for ***syntactically awesome style sheets***) is a preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS). SassScript is the scripting language itself.

Sass consists of two syntaxes. The original syntax, called "the indented syntax," uses a syntax similar to Haml. It uses indentation to separate code blocks and newline characters to separate rules. The newer syntax, **SCSS** (Sassy CSS), uses block formatting like that of CSS. It uses braces to denote code blocks and semicolons to separate rules within a block. The indented syntax and SCSS files are traditionally given the extensions .sass and .scss, respectively.

CSS3 consists of a series of selectors and pseudo-selectors that group rules that apply to them. Sass (in the larger context of both syntaxes) extends CSS by providing several mechanisms available in more traditional programming languages, particularly object-oriented languages, but that are not available to CSS3 itself. When SassScript is interpreted, it creates blocks of CSS rules for various selectors as defined by the Sass file. The Sass interpreter translates SassScript into CSS. Alternatively, Sass can monitor the .sass or .scss file and translate it to an output .css file whenever the .sass or .scss file is saved.

The indented syntax is a metalanguage. SCSS is a nested metalanguage and a superset of CSS, as valid CSS is valid SCSS with the same semantics.

SassScript provides the following mechanisms: variables, nesting, mixins, and selector inheritance.

## History

Sass was initially designed by Hampton Catlin and developed by Natalie Weizenbaum.

## Major implementations

SassScript was implemented in multiple languages, the noteworthy implementations are:

- The official open-source Dart implementation.
- The official "sass" node module on npm, which is Dart Sass compiled to pure JavaScript.
- The official "sass-embedded" node module which is a JavaScript wrapper around the native Dart executable.
- The original open-source Ruby implementation created in 2006, since deprecated due to the lack of maintainers and reached End-of-Life in March 2019.
- libSass, the official open-source C++ implementation, (deprecated in October 2020 then reached) end-of-life in October 2025.
- The (deprecated then) end-of-life in July 2024 "node-sass" node module on npm, based on the end-of-life (by now) libSass.
- JSass, an unofficial Java implementation, based on the end-of-life (by now) libSass.
- phamlp, an unofficial Sass/SCSS implementation in PHP.
- Vaadin has a Java implementation of Sass.
- Firebug, a Firefox XUL ("legacy") extension for web development. It has been since (deprecated and then) discontinued in favor of developer tools integrated into Firefox itself. It stopped working since Firefox 57 dropped support for XUL extensions.

## Features

### Variables

Sass allows variables to be defined. Variables begin with a dollar sign (`$`). Variable assignment is done with a colon (`:`).

SassScript supports four data types:

- Numbers (including units)
- Strings (with quotes or without)
- Colors (name, or names)
- Booleans

Variables can be arguments to or results from one of several available functions. During translation, the values of the variables are inserted into the output CSS document.

| SCSS | Sass | Compiled CSS |
|---|---|---|
| $primary-color: #3bbfce; $margin: 16px; .content-navigation { border-color: $primary-color; color: darken($primary-color, 10%); } .border { padding: $margin / 2; margin: $margin / 2; border-color: $primary-color; } | $primary-color: #3bbfce $margin: 16px .content-navigation border-color: $primary-color color: darken($primary-color, 10%) .border padding: $margin/2 margin: $margin/2 border-color: $primary-color | .content-navigation { border-color: #3bbfce; color: #2b9eab; } .border { padding: 8px; margin: 8px; border-color: #3bbfce; } |

### Nesting

CSS does support logical nesting, but the code blocks themselves are not nested. Sass allows the nested code to be inserted within each other.

| SCSS | Sass | Compiled CSS |
|---|---|---|
| table.hl { margin: 2em 0; td.ln { text-align: right; } } li { font: { family: serif; weight: bold; size: 1.3em; } } | table.hl margin: 2em 0 td.ln text-align: right li font: family: serif weight: bold size: 1.3em | table.hl { margin: 2em 0; } table.hl td.ln { text-align: right; } li { font-family: serif; font-weight: bold; font-size: 1.3em; } |

More complicated types of nesting including namespace nesting and parent references are discussed in the Sass documentation.

| SCSS | Sass | Compiled CSS |
|---|---|---|
| @mixin table-base { th { text-align: center; font-weight: bold; } td, th { padding: 2px; } } #data { @include table-base; } | =table-base th text-align: center font-weight: bold td, th padding: 2px #data +table-base | #data th { text-align: center; font-weight: bold; } #data td, #data th { padding: 2px; } |

#### Loops

Sass allows for iterating over variables using `@for`, `@each` and `@while`, which can be used to apply different styles to elements with similar classes or ids.

| Sass | Compiled CSS |
|---|---|
| $squareCount: 4 @for $i from 1 to $squareCount #square-#{$i} background-color: red width: 50px * $i height: 120px / $i | #square-1 { background-color: red; width: 50px; height: 120px; } #square-2 { background-color: red; width: 100px; height: 60px; } #square-3 { background-color: red; width: 150px; height: 40px; } |

#### Arguments

Mixins also support arguments.

| Sass | Compiled CSS |
|---|---|
| =left($dist) float: left margin-left: $dist #data +left(10px) | #data { float: left; margin-left: 10px; } |

#### In combination

| Sass | Compiled CSS |
|---|---|
| =table-base th text-align: center font-weight: bold td, th padding: 2px =left($dist) float: left margin-left: $dist #data +left(10px) +table-base | #data { float: left; margin-left: 10px; } #data th { text-align: center; font-weight: bold; } #data td, #data th { padding: 2px; } |

### Selector inheritance

While CSS3 supports the Document Object Model (DOM) hierarchy, it does not allow selector inheritance. In Sass, inheritance is achieved by inserting a line inside of a code block that uses the @extend keyword and references another selector. The extended selector's attributes are applied to the calling selector.

| Sass | Compiled CSS |
|---|---|
| .error border: 1px #f00 background: #fdd .error.intrusion font-size: 1.3em font-weight: bold .badError @extend .error border-width: 3px | .error, .badError { border: 1px #f00; background: #fdd; } .error.intrusion, .badError.intrusion { font-size: 1.3em; font-weight: bold; } .badError { border-width: 3px; } |

Sass supports multiple inheritance.

## libSass

At the 2012 HTML5 Developer Conference, Hampton Catlin, the creator of Sass, announced version 1.0 of libSass, an open source C++ implementation of Sass developed by Catlin, Aaron Leung, and the engineering team at Moovweb.

According to Catlin, libSass can be "drop[ped] into anything and it will have Sass in it...You could drop it right into Firefox today and build Firefox and it will compile in there. We wrote our own parser from scratch to make sure that would be possible."

The design goals of libSass are:

- Performance – Developers have reported 10x speed up increases over the Ruby implementation of Sass.
- Easier integration – libSass makes it easier to integrate Sass into more software. Before libSass, tightly integrating Sass into a language or software product required bundling the entire Ruby interpreter. By contrast, libSass is a statically linkable library with zero external dependencies and C-like interface, making it easy to wrap Sass directly into other programming languages and tools. For example, open source libSass bindings now exist for Node, Go, and Ruby.
- Compatibility – libSass's goal is full compatibility with the official Ruby implementation of Sass. This goal has been achieved on libsass 3.3.

## IDE integration

| IDE | Software |
|---|---|
| Adobe Dreamweaver CC 2017 |   |
| Eclipse |   |
| Emacs | sass-mode |
| JetBrains IntelliJ IDEA (Ultimate Edition) |   |
| JetBrains PhpStorm |   |
| JetBrains RubyMine |   |
| JetBrains WebStorm |   |
| Microsoft Visual Studio | Mindscape |
| Microsoft Visual Studio | SassyStudio |
| Microsoft WebMatrix |   |
| NetBeans |   |
| Vim | haml.zip |
| Atom |   |
| Visual Studio Code |   |
| Sublime |   |
| Edit+ |   |
