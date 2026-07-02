---
title: "Quickstart"
source: https://click.palletsprojects.com/en/stable/quickstart/
domain: click-cli
license: CC-BY-SA-4.0
tags: python click, click cli, command line parsing
fetched: 2026-07-02
---

# Quickstart

## Install

Install from PyPI:

```console
pip install click
```

Installing into a virtual environment is highly recommended. We suggest Virtualenv.

## Examples

Some standalone examples of Click applications are packaged with Click. They are available in the examples folder of the repo.

- inout : A very simple example of an application that can read from files and write to files and also accept input from stdin or write to stdout.
- validation : A simple example of an application that performs custom validation of parameters in different ways.
- naval : Port of the docopt naval example.
- colors : A simple example that colorizes text. Uses colorama on Windows.
- aliases : An advanced example that implements Command Aliases.
- imagepipe : A complex example that implements some Command Pipelines . It chains together image processing instructions. Requires pillow.
- repo : An advanced example that implements a Git-/Mercurial-like command line interface.
- complex : A very advanced example that implements loading subcommands dynamically from a plugin folder.
- termui : A simple example that showcases terminal UI helpers provided by click.

## Basic Concepts - Creating a Command

Click is based on declaring commands through decorators. Internally, there is a non-decorator interface for advanced use cases, but it’s discouraged for high-level usage.

A function becomes a Click command line tool by decorating it through `command()`. At its simplest, just decorating a function with this decorator will make it into a callable script:

```python
import click

@click.command()
def hello():
    click.echo('Hello World!')
```

What’s happening is that the decorator converts the function into a `Command` which then can be invoked:

```python
if __name__ == '__main__':
    hello()
```

And what it looks like:

```shell
$ python hello.py
Hello World!
```

And the corresponding help page:

```shell
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```

## Echoing

Why does this example use `echo()` instead of the regular `print()` function? The answer to this question is that Click attempts to support different environments consistently and to be very robust even when the environment is misconfigured. Click wants to be functional at least on a basic level even if everything is completely broken.

What this means is that the `echo()` function applies some error correction in case the terminal is misconfigured instead of dying with a `UnicodeError`.

The echo function also supports color and other styles in output. It will automatically remove styles if the output stream is a file. On Windows, colorama is automatically installed and used. See ANSI Colors.

If you don’t need this, you can also use the `print()` construct / function.

## Nesting Commands

Commands can be attached to other commands of type `Group`. This allows arbitrary nesting of scripts. As an example here is a script that implements two commands for managing databases:

```python
@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
```

As you can see, the `group()` decorator works like the `command()` decorator, but creates a `Group` object instead which can be given multiple subcommands that can be attached with `Group.add_command()`.

For simple scripts, it’s also possible to automatically attach and create a command by using the `Group.command()` decorator instead. The above script can instead be written like this:

```python
@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')
```

You would then invoke the `Group` in your entry points or other invocations:

```python
if __name__ == '__main__':
    cli()
```

## Registering Commands Later

Instead of using the `@group.command()` decorator, commands can be decorated with the plain `@command()` decorator and registered with a group later with `group.add_command()`. This could be used to split commands into multiple Python modules.

```python
@click.command()
def greet():
    click.echo("Hello, World!")
```

```python
@click.group()
def group():
    pass

group.add_command(greet)
```

## Adding Parameters

To add parameters, use the `option()` and `argument()` decorators:

```python
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")
```

What it looks like:

```shell
$ python hello.py --help
Usage: hello.py [OPTIONS] NAME

Options:
  --count INTEGER  number of greetings
  --help           Show this message and exit.
```

## Switching to Entry Points

In the code you wrote so far there is a block at the end of the file which looks like this: `if __name__ == '__main__':`. This is traditionally how a standalone Python file looks like. With Click you can continue doing that, but a better way is to package your app with an entry point.

There are two main (and many more) reasons for this:

The first one is that installers automatically generate executable wrappers for Windows so your command line utilities work on Windows too.

The second reason is that entry point scripts work with virtualenv on Unix without the virtualenv having to be activated. This is a very useful concept which allows you to bundle your scripts with all requirements into a virtualenv.

Click is perfectly equipped to work with that and in fact the rest of the documentation will assume that you are writing applications as distributed packages.

Look at the Packaging Entry Points chapter before reading the rest as the examples assume that you will be using entry points.
