---
title: "jq (programming language)"
source: https://en.wikipedia.org/wiki/Jq_(programming_language)
domain: jq-json
license: CC-BY-SA-4.0
tags: jq json, json processor, command-line json, json filter
fetched: 2026-07-02
---

# jq (programming language)

**jq** is a widely-used command-line utility and very high-level, functional, domain-specific programming language designed for processing JSON data. jq filters its input data to produce modified output in a manner similar to AWK or sed. The input typically consists of one or more JSON values but may instead by one or more lines of text. In jq, programs consist of *filters* that can be composed in pipelines that perform a variety of operations on their inputs.

## History

jq was created by Stephen Dolan, and released in October 2012. It was described as being "like sed for JSON data". Support for regular expressions was added in jq version 1.5.

The original implementation of jq was in Haskell before being ported to the language C.

The jq language was subsequently implemented in other programming languages:

- gojq is an implementation in Go;
- jaq is an implementation with some variations in Rust;
- jqjq implements a substantial subset of jq in jq itself.

## Use

### Command-line use

jq is typically used at the command line and can be used with other command-line utilities, such as GNU Wget. Here is an example showing how the output of a `wget` command can be piped to a jq filter to determine the category names associated with this Wikipedia page:

```mw
$ wget -qO- 'https://en.wikipedia.org/w/api.php?action=parse&page=jq_(programming_language)&format=json' | jq '.parse.categories[]."*"'
```

The output produced by this pipeline consists of a stream of JSON strings, the first few of which are:

```mw
"CS1_errors:_missing_title"
"CS1_errors:_bare_URL"
"Articles_with_short_description"
"Short_description_matches_Wikidata"
"Official_website_not_in_Wikidata"
"Dynamically_typed_programming_languages"
"Functional_languages"
"Programming_languages"
"Programming_languages_created_in_2012"
"Query_languages"
"2012_software"
"Articles_with_example_code"
```

The `wget` command above uses the MediaWiki API for this page to produce a JSON response. The pipe `|` allows the output of `wget` to be accessed by jq, a standard Unix shell mechanism.

The jq filter shown is an abbreviation for the jq pipeline:

```mw
.["parse"] | .["categories"] | .[] | .["*"]
```

This corresponds to the nested JSON structure produced by the call to `wget`. Notice that the jq pipeline is constructed in the same manner using the `|` character as the Unix-style pipeline.

### Embedded use

jq provides a C API, libjq, allowing it to be used from C.

## Modes of operation

jq by default acts as a "stream editor" for JSON inputs, much like the sed utility can be thought of as a "stream editor" for lines of text. However jq has several other modes of operation:

1. it can treat its input from one or more sources as lines of text;
2. it can gather a stream of inputs from a specified source into a JSON array;
3. it can parse its JSON inputs using a so-called "streaming parser" that produces a stream of [path, value] arrays for all "leaf" paths.

The *streaming parser* is very useful when one of more of the JSON inputs is too large to fit in memory, since its memory needs are usually quite small. For example, for an arbitrarily large array of JSON objects, the peak memory need is little more than needed to handle the largest top-level object.

These modes of operation can, within certain limitations, be combined.

## Syntax and semantics

### Types

Every JSON value is also a value in jq, which accordingly has the data types shown in the table below.

| Type | Examples |
|---|---|
| "number" | `3` `3.2` `1e6` `nan` `infinite` |
| "string" | `"Hello"` `"😐"` |
| "boolean" | `true` `false` |
| "array" | `[1, "2", {"mixed": "type"}, [3,4]]` |
| "object" | `{"one": 1, "two": "2", "three": [3]}` |
| "null" | `null` |

`null` is a value, just like any other JSON scalar; it is not a pointer or a "null pointer". `nan` (corresponding to NaN) and `infinite` (see IEEE 754) are the only two jq scalars that are not also JSON values.

### Forms

Special syntactic forms exist for function creation, conditionals, stream reduction, and the module system.

### Filters

Here is an example of defining a named, parameterized filter for formatting an integer in any base from 2 to 36 inclusive. The implementation illustrates tacit (or point-free) programming:

```mw
def tobase($b):
    def digit: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[.:.+1];
    def mod: . % $b;
    def div: ((. - mod) / $b);
    def digits: recurse( select(. >= $b) | div) | mod ;

    select(2 <= $b and $b <= 36)
    | [digits | digit] | reverse | add;
```

The next example demonstrates the use of generators in the classic "SEND MORE MONEY" verbal arithmetic game:

```mw
def send_more_money:
    def choose(m;n;used): ([range(m;n+1)] - used)[];
    def num(a;b;c;d): 1000*a + 100*b + 10*c + d;
    def num(a;b;c;d;e): 10*num(a;b;c;d) + e;
    first(
      1 as $m
      | 0 as $o
      | choose(8;9;[]) as $s
      | choose(2;9;[$s]) as $e
      | choose(2;9;[$s,$e]) as $n
      | choose(2;9;[$s,$e,$n]) as $d
      | choose(2;9;[$s,$e,$n,$d]) as $r
      | choose(2;9;[$s,$e,$n,$d,$r]) as $y
      | select(num($s;$e;$n;$d) + num($m;$o;$r;$e) ==
               num($m;$o;$n;$e;$y))
      | [$s,$e,$n,$d,$m,$o,$r,$e,$m,$o,$n,$e,$y] );
```

jq has inspired several clones and similar programs.

gojq reimplements much of jq in *Go*. It also supports processing YAML files.

jaq is a Rust implementation of jq developed using denotational semantics to formalize its behavior in cases where the original jq documentation is unclear or does not match its behavior.

Mike Farah's yq is a jq-like program that supports several file formats, including JSON, YAML, and XML. Its syntax is not fully compatible with jq.

Andrey Kislyuk's yq provides a collection of wrapper scripts that use jq to process YAML, XML, or TOML files.
