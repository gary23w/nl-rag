---
title: "Twig (template engine)"
source: https://en.wikipedia.org/wiki/Twig_(template_engine)
domain: symfony
license: CC-BY-SA-4.0
tags: symfony framework, twig template, doctrine orm, php components
fetched: 2026-07-02
---

# Twig (template engine)

**Twig** is a free and open-source template engine for PHP. Its syntax originates from Jinja and Django templates. It is licensed under the BSD License and maintained by Fabien Potencier. The initial version was created by Armin Ronacher. Symfony comes with bundled support for Twig as its default template engine since version 2.

The same template language is used by the Nunjucks template engine, thus Nunjucks is also supported by the following tools.

## Features

- Complex control flow
- Automatic escaping
- Template inheritance
- Variable filters
- i18n support (gettext)
- Macros
- Fully extendable

Twig is supported by the following integrated development environments:

- Eclipse via the Twig plugin
- Komodo and Komodo Edit via the Twig highlight/syntax check mode
- NetBeans via the Twig syntax plugin (until 7.1, native as of 7.2)
- PhpStorm (native as of 2.1)
- IntelliJ IDEs, including WebStorm, via a plugin

Twig is supported by the following text editors:

- Atom via the PHP-twig for atom
- Emacs via web-mode.el
- Notepad++ via the Notepad++ Twig Highlighter
- Sublime Text via the Twig bundle
- TextMate via the Twig bundle
- Vim via the Jinja syntax plugin or the vim-twig plugin
- Brackets via Brackets Twig
- Visual Studio Code via the Twig extension
- GTKSourceView via the Twig language definition
- Coda via the Twig syntax mode
- Coda 2 via the other Twig syntax mode
- SubEthaEdit via the Twig syntax mode

## Syntax

Twig defines three kinds of delimiters:

- `{{ ... }}` is used to print the content of variables or the result of evaluating an expression.
- `{# ... #}` is used to add comments in the templates. These comments are not included in the rendered page.
- `{% ... %}` is used to execute statements, such as for-loops. For example:
  - `{% set foo = 'bar' %}`, to assign.
  - `{% if i is defined and i == 1%} ... {% endif %}`: condition.
  - `{% for i in 0..10 %} ... {% endfor %}`: counter in a loop.

Unlike in base PHP, Twig variables do not start with a dollar sign. The apostrophe (') is the escape character.

To create an iterative array:

```mw
{% set myArray = [1, 2] %}
```

An associative array:

```mw
{% set myArray = {'key': 'value'} %}
```

## Operators precedence

The operators precedence is, from the less to more priority:

| Operator | Role |
|---|---|
| or | Or |
| xor | Xor |
| and | And |
| b-or | Bitwise OR |
| b-xor | Bitwise XOR |
| b-and | Bitwise AND |
| == | Is equal? |
| != | Is different? |
| < | Inferior |
| > | Superior |
| >= | Superior or equal |
| <= | Inferior or equal |
| in | Into |
| matches | Corresponds |
| starts with | Begins by |
| ends with | Finishes by |
| .. | Sequence (ex: `1..5`) |
| + | Plus |
| - | Less |
| ~ | Concatenation |
| * | Multiplication |
| / | Division |
| // | Division rounded to lower |
| % | Modulo |
| is | Test (ex: `is defined` or `is not empty`) |
| ** | Power |
| \| | Filter |
| [] | Array entry |
| . | Attribute or method from an object (ex: `country.name`) |

### Filters

The filters provide some treatments on an expression, when placed after it, separated by pipes. For example:

- `capitalize`: changes a string's first letter to capital.
- `upper`: changes a whole string to capital.
- `first`: displays the first line of an array.
- `length`: returns a variable size.

### Special variables

- `loop` contains the current loop information. For example `loop.index` corresponds to the number of iterations which have already occurred.
- The global variables begin with underscores. For example: So, to the a page route: `{{ path(app.request.attributes.get('_route'), app.request.attributes.get('_route_params')) }}`
  - _route (URL part located after the domain)
  - _self (current file name)
- The CGI environment variables, such as `{{ app.request.server.get('SERVER_NAME') }}`.

## Example

The example below demonstrates some basic features of Twig.

```mw
{% extends "base.html" %}
{% block navigation %}
    <ul id="navigation">
    {% for item in navigation %}
        <li>
            <a href="{{ item.href }}">
                {% if item.level == 2 %}&nbsp;&nbsp;{% endif %}
                {{ item.caption|upper }}
            </a>
        </li>
    {% endfor %}
    </ul>
{% endblock navigation %}
```

## Real world usage

Twig has become a widely adopted templating engine in the PHP ecosystem. It is the default templating language for the Symfony framework and is also integrated into several content management systems (CMS) and applications, including:

- Drupal adopted Twig as its default template engine starting from version 8, replacing PHPTemplate.
- CraftCMS uses Twig as its sole templating language, allowing developers to create highly customised front-end experiences.
- eZ Platform (Ibexa) integrates Twig for rendering templates within its content management system.
- Bolt CMS uses Twig for theming and front-end rendering.
- ShopWired uses Twig for theming and front-end rendering.
- OpenCart uses Twig for theming and HTML rendering.

Twig is also employed in many custom PHP applications where secure and readable templating are important. The similarity of Twig to Jinja and Django templates has also made it familiar to developers coming from Python and other similar ecosystems.
