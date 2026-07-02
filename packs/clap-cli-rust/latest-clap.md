---
title: "clap"
source: https://docs.rs/clap/latest/clap/
domain: clap-cli-rust
license: CC-BY-SA-4.0
tags: clap cli, rust argument parser, command line parsing rust, clap derive api
fetched: 2026-07-02
---

# Crate clap

Source

Expand description

> **Command Line Argument Parser for Rust**

Quick Links:

- Derive tutorial and reference
- Builder tutorial and reference
- Cookbook
- CLI Concepts
- FAQ
- Discussions
- CHANGELOG (includes major version migration guides)

### §Aspirations

- Out of the box, users get a polished CLI experience
  - Including common argument behavior, help generation, suggested fixes for users, colored output, shell completions, etc
- Flexible enough to port your existing CLI interface
  - However, we won’t necessarily streamline support for each use case
- Reasonable parse performance
- Resilient maintainership, including
  - Willing to break compatibility rather than batching up breaking changes in large releases
  - Leverage feature flags to keep to one active branch
  - Being under WG-CLI to increase the bus factor
- We follow semver and will wait about 6-9 months between major breaking changes
- We will support the last two minor Rust releases (MSRV, currently 1.74)

While these aspirations can be at odds with fast build times and low binary size, we will still strive to keep these reasonable for the flexibility you get. Check out the argparse-benchmarks for CLI parsers optimized for other use cases.

### §Example

Run

```console
$ cargo add clap --features derive
```

*(See also feature flag reference)*

Then define your CLI in `main.rs`:

```
use clap::Parser;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Name of the person to greet
    #[arg(short, long)]
    name: String,

    /// Number of times to greet
    #[arg(short, long, default_value_t = 1)]
    count: u8,
}

fn main() {
    let args = Args::parse();

    for _ in 0..args.count {
        println!("Hello {}!", args.name);
    }
}
```

And try it out:

```console
$ demo --help
A simple to use, efficient, and full-featured Command Line Argument Parser

Usage: demo[EXE] [OPTIONS] --name <NAME>

Options:
  -n, --name <NAME>    Name of the person to greet
  -c, --count <COUNT>  Number of times to greet [default: 1]
  -h, --help           Print help
  -V, --version        Print version

$ demo --name Me
Hello Me!
```

*(version number and `.exe` extension on windows replaced by placeholders)*

See also the derive tutorial and reference

Augment clap:

- wild for supporting wildcards (`*`) on Windows like you do Linux
- argfile for loading additional arguments from a file (aka response files)
- shadow-rs for generating `Command::long_version`
- clap_mangen for generating man page source (roff)
- clap_complete for shell completion support
- clap-i18n-richformatter for i18n support with `clap::error::RichFormatter`

CLI Helpers

- clio for reading/writing to files specified as arguments
- clap-verbosity-flag
- clap-cargo
- colorchoice-clap

Testing

- `trycmd`: Bulk snapshot testing
- `snapbox`: Specialized snapshot testing
- `assert_cmd` and `assert_fs`: Customized testing

Documentation:

- Command-line Apps for Rust book

## Modules

**_concepts`unstable-doc`**

CLI Concepts

**_cookbook`unstable-doc`**

Documentation: Cookbook

**_derive`unstable-doc`**

Documentation: Derive Reference

**_faq`unstable-doc`**

Documentation: FAQ

**_features`unstable-doc`**

Documentation: Feature Flags

**_tutorial`unstable-doc`**

Tutorial for the Builder API

**builder**

Define

Command

line

arguments

**error**

Error reporting

**parser**

Command

line argument parser

## Macros

**arg**

Create an

Arg

from a usage string.

**command`cargo`**

Allows you to build the

Command

instance from your Cargo.toml at compile time.

**crate_authors`cargo`**

Allows you to pull the authors for the command from your Cargo.toml at compile time in the form:

"author1 lastname <author1@example.com>:author2 lastname <author2@example.com>"

**crate_description`cargo`**

Allows you to pull the description from your Cargo.toml at compile time.

**crate_name`cargo`**

Allows you to pull the name from your Cargo.toml at compile time.

**crate_version`cargo`**

Allows you to pull the version from your Cargo.toml at compile time as

MAJOR.MINOR.PATCH_PKGVERSION_PRE

**value_parser**

Select a

ValueParser

implementation from the intended type

## Structs

**Arg**

The abstract representation of a command line argument. Used to set all the options and relationships that define a valid argument for the program.

**ArgGroup**

Specifies a logical group of

arguments

**ArgMatches**

Container for parse results.

**Command**

Build a command-line interface.

**Id**

Arg

or

ArgGroup

identifier

## Enums

**ArgAction**

Behavior of arguments when they are encountered while parsing

**ColorChoice**

Represents the color preferences for program output

**ValueHint**

Provide shell with hint on how to complete an argument.

## Traits

**Args**

Parse a set of arguments into a user-defined container.

**CommandFactory**

Create a

Command

relevant for a user-defined container.

**FromArgMatches**

Converts an instance of

ArgMatches

to a user-defined container.

**Parser**

Parse command-line arguments into

Self

.

**Subcommand**

Parse a sub-command into a user-defined enum.

**ValueEnum**

Parse arguments into enums.

## Type Aliases

**Error**

Command Line Argument Parser Error
