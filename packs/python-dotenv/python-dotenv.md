---
title: "python-dotenv"
source: https://saurabh-kumar.com/python-dotenv/
domain: python-dotenv
license: CC-BY-SA-4.0
tags: python dotenv, dotenv env file, environment variable python
fetched: 2026-07-02
---

# python-dotenv

(Build Status) (PyPI version)

python-dotenv reads key-value pairs from a `.env` file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.

- Getting Started
- Other Use Cases
  - Load configuration without altering the environment
  - Parse configuration as a stream
  - Load .env files in IPython
- Command-line Interface
- File format
  - Multiline values
  - Variable expansion
- Related Projects
- Acknowledgements

## Getting Started

```shell
pip install python-dotenv
```

If your application takes its configuration from environment variables, like a 12-factor application, launching it in development is not very practical because you have to set those environment variables yourself.

To help you with that, you can add python-dotenv to your application to make it load the configuration from a `.env` file when it is present (e.g. in development) while remaining configurable via the environment:

```python
from dotenv import load_dotenv

load_dotenv()  # reads variables from a .env file and sets them in os.environ

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
```

By default, `load_dotenv()` will:

- Look for a `.env` file in the same directory as the Python script (or higher up the directory tree).
- Read each key-value pair and add it to `os.environ`.
- **Not override** existing environment variables (`override=False`). Pass `override=True` to override existing variables.

To configure the development environment, add a `.env` in the root directory of your project:

```
.
├── .env
└── foo.py
```

The syntax of `.env` files supported by python-dotenv is similar to that of Bash:

```bash
# Development settings
DOMAIN=example.org
ADMIN_EMAIL=admin@${DOMAIN}
ROOT_URL=${DOMAIN}/app
```

If you use variables in values, ensure they are surrounded with `{` and `}`, like `${DOMAIN}`, as bare variables such as `$DOMAIN` are not expanded.

You will probably want to add `.env` to your `.gitignore`, especially if it contains secrets like a password.

See the section "File format" below for more information about what you can write in a `.env` file.

## Other Use Cases

### Load configuration without altering the environment

The function `dotenv_values` works more or less the same way as `load_dotenv`, except it doesn't touch the environment, it just returns a `dict` with the values parsed from the `.env` file.

```python
from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "[email protected]"}
```

This notably enables advanced configuration management:

```python
import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
```

### Parse configuration as a stream

`load_dotenv` and `dotenv_values` accept streams via their `stream` argument. It is thus possible to load the variables from sources other than the filesystem (e.g. the network).

```python
from io import StringIO

from dotenv import load_dotenv

config = StringIO("USER=foo\[email protected]")
load_dotenv(stream=config)
```

### Load .env files in IPython

You can use dotenv in IPython. By default, it will use `find_dotenv` to search for a `.env` file:

```python
%load_ext dotenv
%dotenv
```

You can also specify a path:

```python
%dotenv relative/or/absolute/path/to/.env
```

Optional flags:

- `-o` to override existing variables.
- `-v` for increased verbosity.

### Disable load_dotenv

Set `PYTHON_DOTENV_DISABLED=1` to disable `load_dotenv()` from loading .env files or streams. Useful when you can't modify third-party package calls or in production.

## Command-line Interface

A CLI interface `dotenv` is also included, which helps you manipulate the `.env` file without manually opening it.

```shell
$ pip install "python-dotenv[cli]"
$ dotenv set USER foo
$ dotenv set EMAIL [email protected]
$ dotenv list
USER=foo
[email protected]
$ dotenv list --format=json
{
  "USER": "foo",
  "EMAIL": "[email protected]"
}
$ dotenv run -- python foo.py
```

Run `dotenv --help` for more information about the options and subcommands.

## File format

The format is not formally specified and still improves over time. That being said, `.env` files should mostly look like Bash files. Reading from FIFOs (named pipes) on Unix systems is also supported.

Keys can be unquoted or single-quoted. Values can be unquoted, single- or double-quoted. Spaces before and after keys, equal signs, and values are ignored. Values can be followed by a comment. Lines can start with the `export` directive, which does not affect their interpretation.

Allowed escape sequences:

- in single-quoted values: `\\`, `\'`
- in double-quoted values: `\\`, `\'`, `\"`, `\a`, `\b`, `\f`, `\n`, `\r`, `\t`, `\v`

### Multiline values

It is possible for single- or double-quoted values to span multiple lines. The following examples are equivalent:

```bash
FOO="first line
second line"
```

```bash
FOO="first line\nsecond line"
```

### Variable without a value

A variable can have no value:

```bash
FOO
```

It results in `dotenv_values` associating that variable name with the value `None` (e.g. `{"FOO": None}`. `load_dotenv`, on the other hand, simply ignores such variables.

This shouldn't be confused with `FOO=`, in which case the variable is associated with the empty string.

### Variable expansion

python-dotenv can interpolate variables using POSIX variable expansion.

With `load_dotenv(override=True)` or `dotenv_values()`, the value of a variable is the first of the values defined in the following list:

- Value of that variable in the `.env` file.
- Value of that variable in the environment.
- Default value, if provided.
- Empty string.

With `load_dotenv(override=False)`, the value of a variable is the first of the values defined in the following list:

- Value of that variable in the environment.
- Value of that variable in the `.env` file.
- Default value, if provided.
- Empty string.

- environs
- Honcho
- dump-env
- dynaconf
- parse_it
- django-dotenv
- django-environ
- python-decouple
- django-configuration

## Acknowledgements

This project is currently maintained by Saurabh Kumar and Bertrand Bonnefoy-Claudet and would not have been possible without the support of these awesome people.
