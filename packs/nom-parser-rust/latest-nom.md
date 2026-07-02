---
title: "nom - Rust"
source: https://docs.rs/nom/latest/nom/
domain: nom-parser-rust
license: CC-BY-SA-4.0
tags: nom parser, rust parser combinator, byte parsing rust, nom combinator library
fetched: 2026-07-02
---

# Crate nom

Source

Expand description

## §nom, eating data byte by byte

nom is a parser combinator library with a focus on safe parsing, streaming patterns, and as much as possible zero copy.

### §Example

```
use nom::{
  IResult,
  Parser,
  bytes::complete::{tag, take_while_m_n},
  combinator::map_res
};

#[derive(Debug,PartialEq)]
pub struct Color {
  pub red:     u8,
  pub green:   u8,
  pub blue:    u8,
}

fn from_hex(input: &str) -> Result<u8, std::num::ParseIntError> {
  u8::from_str_radix(input, 16)
}

fn is_hex_digit(c: char) -> bool {
  c.is_digit(16)
}

fn hex_primary(input: &str) -> IResult<&str, u8> {
  map_res(
    take_while_m_n(2, 2, is_hex_digit),
    from_hex
  ).parse(input)
}

fn hex_color(input: &str) -> IResult<&str, Color> {
  let (input, _) = tag("#")(input)?;
  let (input, (red, green, blue)) = (hex_primary, hex_primary, hex_primary).parse(input)?;

  Ok((input, Color { red, green, blue }))
}

fn main() {
  assert_eq!(hex_color("#2F14DF"), Ok(("", Color {
    red: 47,
    green: 20,
    blue: 223,
  })));
}
```

The code is available on GitHub

There are a few guides with more details about how to write parsers, or the error management system. You can also check out the recipes module that contains examples of common patterns.

**Looking for a specific combinator? Read the “choose a combinator” guide**

If you are upgrading to nom 5.0, please read the migration document.

### §Parser combinators

Parser combinators are an approach to parsers that is very different from software like lex and yacc. Instead of writing the grammar in a separate syntax and generating the corresponding code, you use very small functions with very specific purposes, like “take 5 bytes”, or “recognize the word ‘HTTP’”, and assemble them in meaningful patterns like “recognize ‘HTTP’, then a space, then a version”. The resulting code is small, and looks like the grammar you would have written with other parser approaches.

This gives us a few advantages:

- The parsers are small and easy to write
- The parsers components are easy to reuse (if they’re general enough, please add them to nom!)
- The parsers components are easy to test separately (unit tests and property-based tests)
- The parser combination code looks close to the grammar you would have written
- You can build partial parsers, specific to the data you need at the moment, and ignore the rest

Here is an example of one such parser, to recognize text between parentheses:

```
use nom::{
  IResult,
  Parser,
  sequence::delimited,
  character::complete::char,
  bytes::complete::is_not
};

fn parens(input: &str) -> IResult<&str, &str> {
  delimited(char('('), is_not(")"), char(')')).parse(input)
}
```

It defines a function named `parens` which will recognize a sequence of the character `(`, the longest byte array not containing `)`, then the character `)`, and will return the byte array in the middle.

Here is another parser, written without using nom’s combinators this time:

```
use nom::{IResult, Err, Needed};

fn take4(i: &[u8]) -> IResult<&[u8], &[u8]>{
  if i.len() < 4 {
    Err(Err::Incomplete(Needed::new(4)))
  } else {
    Ok((&i[4..], &i[0..4]))
  }
}
```

This function takes a byte array as input, and tries to consume 4 bytes. Writing all the parsers manually, like this, is dangerous, despite Rust’s safety features. There are still a lot of mistakes one can make. That’s why nom provides a list of functions to help in developing parsers.

With functions, you would write it like this:

```
use nom::{IResult, bytes::streaming::take};
fn take4(input: &str) -> IResult<&str, &str> {
  take(4u8)(input)
}
```

A parser in nom is a function which, for an input type `I`, an output type `O` and an optional error type `E`, will have the following signature:

ⓘ

```
fn parser(input: I) -> IResult<I, O, E>;
```

Or like this, if you don’t want to specify a custom error type (it will be `(I, ErrorKind)` by default):

ⓘ

```
fn parser(input: I) -> IResult<I, O>;
```

`IResult` is an alias for the `Result` type:

```
use nom::{Needed, error::Error};

type IResult<I, O, E = Error<I>> = Result<(I, O), Err<E>>;

enum Err<E> {
  Incomplete(Needed),
  Error(E),
  Failure(E),
}
```

It can have the following values:

- A correct result `Ok((I,O))` with the first element being the remaining of the input (not parsed yet), and the second the output value;
- An error `Err(Err::Error(c))` with `c` an error that can be built from the input position and a parser specific error
- An error `Err(Err::Incomplete(Needed))` indicating that more input is necessary. `Needed` can indicate how much data is needed
- An error `Err(Err::Failure(c))`. It works like the `Error` case, except it indicates an unrecoverable error: We cannot backtrack and test another parser

Please refer to the “choose a combinator” guide for an exhaustive list of parsers. See also the rest of the documentation here.

### §Making new parsers with function combinators

nom is based on functions that generate parsers, with a signature like this: `(arguments) -> impl Fn(Input) -> IResult<Input, Output, Error>`. The arguments of a combinator can be direct values (like `take` which uses a number of bytes or character as argument) or even other parsers (like `delimited` which takes as argument 3 parsers, and returns the result of the second one if all are successful).

Here are some examples:

```
use nom::IResult;
use nom::bytes::complete::{tag, take};
fn abcd_parser(i: &str) -> IResult<&str, &str> {
  tag("abcd")(i) }

fn take_10(i: &[u8]) -> IResult<&[u8], &[u8]> {
  take(10u8)(i) }
```

### §Combining parsers

There are higher level patterns, like the **`alt`** combinator, which provides a choice between multiple parsers. If one branch fails, it tries the next, and returns the result of the first parser that succeeds:

```
use nom::{IResult, Parser};
use nom::branch::alt;
use nom::bytes::complete::tag;

let mut alt_tags = alt((tag("abcd"), tag("efgh")));

assert_eq!(alt_tags.parse(&b"abcdxxx"[..]), Ok((&b"xxx"[..], &b"abcd"[..])));
assert_eq!(alt_tags.parse(&b"efghxxx"[..]), Ok((&b"xxx"[..], &b"efgh"[..])));
assert_eq!(alt_tags.parse(&b"ijklxxx"[..]), Err(nom::Err::Error((&b"ijklxxx"[..], nom::error::ErrorKind::Tag))));
```

The **`opt`** combinator makes a parser optional. If the child parser returns an error, **`opt`** will still succeed and return None:

```
use nom::{IResult, Parser, combinator::opt, bytes::complete::tag};
fn abcd_opt(i: &[u8]) -> IResult<&[u8], Option<&[u8]>> {
  opt(tag("abcd")).parse(i)
}

assert_eq!(abcd_opt(&b"abcdxxx"[..]), Ok((&b"xxx"[..], Some(&b"abcd"[..]))));
assert_eq!(abcd_opt(&b"efghxxx"[..]), Ok((&b"efghxxx"[..], None)));
```

**`many0`** applies a parser 0 or more times, and returns a vector of the aggregated results:

```
use nom::{IResult, Parser, multi::many0, bytes::complete::tag};
use std::str;

fn multi(i: &str) -> IResult<&str, Vec<&str>> {
  many0(tag("abcd")).parse(i)
}

let a = "abcdef";
let b = "abcdabcdef";
let c = "azerty";
assert_eq!(multi(a), Ok(("ef",     vec!["abcd"])));
assert_eq!(multi(b), Ok(("ef",     vec!["abcd", "abcd"])));
assert_eq!(multi(c), Ok(("azerty", Vec::new())));
```

Here are some basic combinators available:

- **`opt`**: Will make the parser optional (if it returns the `O` type, the new parser returns `Option<O>`)
- **`many0`**: Will apply the parser 0 or more times (if it returns the `O` type, the new parser returns `Vec<O>`)
- **`many1`**: Will apply the parser 1 or more times

There are more complex (and more useful) parsers like tuples, which are used to apply a series of parsers then assemble their results.

Example with a tuple of parsers:

```
use nom::{
  error::ErrorKind,
  Needed,
  Parser,
  number::streaming::be_u16,
  bytes::streaming::{tag, take}};

let mut tpl = (be_u16, take(3u8), tag("fg"));

assert_eq!(
  tpl.parse(&b"abcdefgh"[..]),
  Ok((
    &b"h"[..],
    (0x6162u16, &b"cde"[..], &b"fg"[..])
  ))
);
assert_eq!(tpl.parse(&b"abcde"[..]), Err(nom::Err::Incomplete(Needed::new(2))));
let input = &b"abcdejk"[..];
assert_eq!(tpl.parse(input), Err(nom::Err::Error((&input[5..], ErrorKind::Tag))));
```

But you can also use a sequence of combinators written in imperative style, thanks to the `?` operator:

```
use nom::{IResult, bytes::complete::tag};

#[derive(Debug, PartialEq)]
struct A {
  a: u8,
  b: u8
}

fn ret_int1(i:&[u8]) -> IResult<&[u8], u8> { Ok((i,1)) }
fn ret_int2(i:&[u8]) -> IResult<&[u8], u8> { Ok((i,2)) }

fn f(i: &[u8]) -> IResult<&[u8], A> {
  let (i, _) = tag("abcd")(i)?;
  let (i, a) = ret_int1(i)?;
  let (i, _) = tag("efgh")(i)?;
  let (i, b) = ret_int2(i)?;

  Ok((i, A { a, b }))
}

let r = f(b"abcdefghX");
assert_eq!(r, Ok((&b"X"[..], A{a: 1, b: 2})));
```

### §Streaming / Complete

Some of nom’s modules have `streaming` or `complete` submodules. They hold different variants of the same combinators.

A streaming parser assumes that we might not have all of the input data. This can happen with some network protocol or large file parsers, where the input buffer can be full and need to be resized or refilled.

A complete parser assumes that we already have all of the input data. This will be the common case with small files that can be read entirely to memory.

Here is how it works in practice:

```
use nom::{IResult, Err, Needed, error::{Error, ErrorKind}, bytes, character};

fn take_streaming(i: &[u8]) -> IResult<&[u8], &[u8]> {
  bytes::streaming::take(4u8)(i)
}

fn take_complete(i: &[u8]) -> IResult<&[u8], &[u8]> {
  bytes::complete::take(4u8)(i)
}

assert_eq!(take_streaming(&b"abcde"[..]), Ok((&b"e"[..], &b"abcd"[..])));
assert_eq!(take_complete(&b"abcde"[..]), Ok((&b"e"[..], &b"abcd"[..])));

assert_eq!(take_streaming(&b"abc"[..]), Err(Err::Incomplete(Needed::new(1))));

assert_eq!(take_complete(&b"abc"[..]), Err(Err::Error(Error::new(&b"abc"[..], ErrorKind::Eof))));

fn alpha0_streaming(i: &str) -> IResult<&str, &str> {
  character::streaming::alpha0(i)
}

fn alpha0_complete(i: &str) -> IResult<&str, &str> {
  character::complete::alpha0(i)
}

assert_eq!(alpha0_streaming("abcd;"), Ok((";", "abcd")));
assert_eq!(alpha0_complete("abcd;"), Ok((";", "abcd")));

assert_eq!(alpha0_streaming("abcd"), Err(Err::Incomplete(Needed::new(1))));

assert_eq!(alpha0_complete("abcd"), Ok(("", "abcd")));
```

**Going further:** Read the guides, check out the recipes!

## Modules

**bits**

Bit level parsers

**branch**

Choice combinators

**bytes**

Parsers recognizing bytes streams

**character**

Character specific parsers and combinators

**combinator**

General purpose combinators

**error**

Error management

**lib**

Lib module to re-export everything needed from

std

or

core

/

alloc

. This is how

serde

does it, albeit there it is not public.

**multi**

Combinators applying their child parser multiple times

**number**

Parsers recognizing numbers

**recipes`std` and (`docsrs`)**

Common recipes to build nom parsers

**sequence**

Combinators applying parsers in sequence

## Macros

**error_node_position**

Creates a parse error from a

nom::ErrorKind

, the position in the input and the next error in the parsing tree

**error_position**

Creates a parse error from a

nom::ErrorKind

and the position in the input

## Structs

**And**

Implementation of

Parser::and

**AndThen**

Implementation of

Parser::and_then

**Check**

Applies the parser, but do not a produce a value

**Complete**

Indicates that the input data is complete: no more data may be added later

**Emit**

Produces a value. This is the default behaviour for parsers

**FlatMap**

Implementation of

Parser::flat_map

**Into**

Implementation of

Parser::into

**Map**

Implementation of

Parser::map

**MapOpt**

Implementation of

Parser::map_opt

**MapRes**

Implementation of

Parser::map_res

**Or**

Implementation of

Parser::or

**OutputM**

Holds the parser execution modifiers: output

Mode

, error

Mode

and streaming behaviour for input data

**SaturatingIterator**

A saturating iterator for usize.

**Streaming**

Indicates that the input data is streaming: more data may be available later

## Enums

**CompareResult**

Indicates whether a comparison was successful, an error, or if more data was needed

**Err**

The

Err

enum indicates the parser was not successful

**Needed**

Contains information on needed data if a parser returned

Incomplete

## Traits

**AsBytes**

Helper trait for types that can be viewed as a byte slice

**AsChar**

Transforms common types to a char for basic token parsing

**Compare**

Abstracts comparison operations

**ErrorConvert**

Equivalent From implementation to avoid orphan rules in bits parsers

**ExtendInto**

Abstracts something which can extend an

Extend

. Used to build modified input slices in

escaped_transform

**FindSubstring**

Look for a substring in self

**FindToken**

Look for a token in self

**Finish**

Helper trait to convert a parser’s result to a more manageable type

**HexDisplay`std`**

Helper trait to show a byte slice as a hex dump

**Input**

Parser input types must implement this trait

**IsStreaming**

Specifies the behaviour when a parser encounters an error that could be due to partial ata

**Mode**

Parser mode: influences how combinators build values

**NomRange**

Abstractions for range-like types.

**Offset**

Useful functions to calculate the offset between slices and show a hexdump of a slice

**OutputMode**

Trait Defining the parser’s execution

**ParseTo**

Used to integrate

str

’s

parse()

method

**Parser**

All nom parsers implement this trait

**ToUsize**

Helper trait to convert numbers to usize.

## Type Aliases

**IResult**

Holds the result of parsing functions

**PResult**

Parser result type
