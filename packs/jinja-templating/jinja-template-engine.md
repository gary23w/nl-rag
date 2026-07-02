---
title: "Jinja (template engine)"
source: https://en.wikipedia.org/wiki/Jinja_(template_engine)
domain: jinja-templating
license: CC-BY-SA-4.0
tags: jinja template, jinja2 engine, python templating, template inheritance
fetched: 2026-07-02
---

# Jinja (template engine)

**Jinja** is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine, but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox. It is a text-based template language and thus can be used to generate any markup as well as source code.

The Jinja template engine allows customization of tags, filters (for formatting or transforming values), tests (for evaluating conditions), and globals. Also, unlike the Django template engine, Jinja allows the template designer to call functions with arguments on objects. Jinja is the default template engine for Flask, as well as Home Assistant's Automations. It is also used by Ansible, Trac, and Salt. It is also used to make SQL macros, for example for use with dbt.

## Features

Some of the features of Jinja are:

- sandboxed execution
- automatic HTML escaping to prevent cross-site scripting (XSS) attacks
- template inheritance
- compiles down to the optimal Python code just-in-time
- optional ahead-of-time template compilation
- easy to debug (for example, line numbers of exceptions directly point to the correct line in the template)
- configurable syntax

Jinja, like Smarty, also ships with an easy-to-use filter system similar to the Unix pipeline.

## Syntax

The syntax for printing output in Jinja is using the double curly braces, for example `{{ Hello, World! }}`.

Statements which set variables in jinja or those which do not have an output can be wrapped within `{%` and `%}`, using the `set` keyword. For example `{% set foo = 42 %}` sets a variable called `foo` with a value of 42.

Similar to above, comments in jinja can be written using a number sign (`#`) instead of a percentage (`%`), for example, `{# helpful comment #}`.

The syntax for creating a filter in Jinja is a vertical bar (`|`), for example `{{ variable|filter }}`. A variable can have multiple filters, for example `{{ variable|filter|filter }}`).

The syntax for creating a test in Jinja is the keyword `is` as well as the conditions for evaluating the validity of a test, such as for example `{% if variable is divisibleby 10 %}do something{% endif %}`).

For loops can be used to iterate over sequences, while retaining their object properties. The following example demonstrates iterating over a list of users with `username` and `password` fields.

```mw
{% for user in users %}
    {{ user.username }}
    {{ user.password }}
{% endfor %}
```

Although `break` and `continue` are not allowed inside loops, sequences can be filtered.

## Example

Here is a small example of a template file `example.html.jinja`:

```mw
<!DOCTYPE html>
<html>
  <head>
    <title>{{ variable|escape }}</title>
  </head>
  <body>
  {%- for item in item_list %}
    {{ item }}{% if not loop.last %},{% endif %}
  {%- endfor %}
  </body>
</html>
```

and templating code:

```mw
from jinja2 import Template
with open("example.html.jinja") as f:
    tmpl = Template(f.read())
print(tmpl.render(
    variable = "Value with <unsafe> data",
    item_list = [1, 2, 3, 4, 5, 6]
))
```

This produces the HTML string:

```mw
<!DOCTYPE html>
<html>
  <head>
    <title>Value with &lt;unsafe&gt; data</title>
  </head>
  <body>
    1,
    2,
    3,
    4,
    5,
    6
  </body>
</html>
```

Note the minus sign (`-`) after the tag `{%`: If you add a minus sign (`-`) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed.
