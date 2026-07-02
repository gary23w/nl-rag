---
title: "Command Reference"
source: https://www.nushell.sh/commands/
domain: nushell
license: docs: MIT (nushell.sh)
tags: nushell, nu shell, nushell pipeline
fetched: 2026-07-02
---

# Command Reference

If you're new to Nushell, the quick tour can show you the most important commands. You don't need to know them all!

To see all commands from inside Nushell, run `help commands`.

Command

Categories

Description

Feature

abbr

platform

Abbreviations related commands.

abbr list

platform

List all defined abbreviations.

alias

core

Alias a command (with optional flags) to a new name.

all

filters

Test if every element of the input fulfills a predicate expression.

ansi

platform

Output ANSI codes to change color and style of text.

ansi gradient

platform

Add a color gradient (using ANSI color codes) to the given string.

ansi link

platform

Add a link (using OSC 8 escape sequence) to the given string.

ansi strip

platform

Strip ANSI escape sequences from a string.

any

filters

Tests if any element of the input fulfills a predicate expression.

append

filters

Append any number of rows to a table.

ast

debug

Print the abstract syntax tree (ast) for a pipeline.

attr

core

Various attributes for custom commands.

attr category

core

Attribute for adding a category to custom commands.

attr complete

core

Attribute for using another command as a completion source for all arguments.

attr complete external

core

Attribute for enabling use of the external completer for internal commands.

attr deprecated

core

Attribute for marking a command or flag as deprecated.

attr example

core

Attribute for adding examples to custom commands.

attr search-terms

core

Attribute for adding search terms to custom commands.

banner

default

Print a banner for Nushell with information about the project

bits

bits

Various commands for working with bits.

bits and

bits

Performs bitwise and for ints or binary values.

bits not

bits

Performs logical negation on each bit.

bits or

bits

Performs bitwise or for ints or binary values.

bits rol

bits

Bitwise rotate left for ints or binary values.

bits ror

bits

Bitwise rotate right for ints or binary values.

bits shl

bits

Bitwise shift left for ints or binary values.

bits shr

bits

Bitwise shift right for ints or binary values.

bits xor

bits

Performs bitwise xor for ints or binary values.

break

core

Break a loop.

bytes

bytes

Various commands for working with byte data.

bytes add

bytes

Add specified bytes to the binary input.

bytes at

bytes

Get bytes from the input defined by a range.

bytes build

bytes

Create a binary value from the provided arguments.

bytes collect

bytes

Concatenate multiple binary into a single binary, with an optional separator between each.

bytes ends-with

bytes

Check if binary data ends with a pattern.

bytes index-of

bytes

Returns start index of first occurrence of pattern in bytes, or -1 if no match.

bytes length

bytes

Output the length of any bytes in the pipeline.

bytes remove

bytes

Remove specified bytes from the input.

bytes replace

bytes

Find and replace bytes in binary data.

bytes reverse

bytes

Reverse the bytes in the pipeline.

bytes split

bytes

Split input into multiple items using a separator.

bytes starts-with

bytes

Check if binary data starts with a pattern.

cal

generators

Display a calendar.

cd

filesystem

Change the current working directory.

char

strings

Output special characters (e.g., 'newline').

chunk-by

filters

Divides a sequence into sub-sequences based on a closure.

chunks

filters

Divide a list, table or binary input into chunks of `chunk_size`.

clear

platform

Clear the terminal screen.

collect

core

Collect a stream into a value.

columns

filters

Given a record or table, produce a list of its columns' names.

commandline

core

View the current command line input buffer.

commandline edit

core

Modify the current command line input buffer.

commandline get-cursor

core

Get the current cursor position.

commandline set-cursor

core

Set the current cursor position.

compact

filters

Creates a table with non-empty rows.

complete

system

Capture the outputs and exit code from an external piped in command in a nushell table.

config

env

Edit nushell configuration files.

config env

env

Edit nu environment configurations.

config flatten

debug

Show the current configuration in a flattened form.

config nu

env

Edit nu configurations.

config reset

env

Reset nushell environment configurations to default, and saves old config files in the config location as oldconfig.nu and oldenv.nu.

config use-colors

env

Get the configuration for color output.

const

core

Create a parse-time constant.

continue

core

Continue a loop from the next iteration.

cp

filesystem

Copy files using uutils/coreutils cp.

date

date

Date-related commands.

date format

removed

Removed command: use `format date` instead.

date from-human

date

Convert a human readable datetime string to a datetime.

date humanize

date

Print a 'humanized' format for the date, relative to now.

date list-timezone

date

List supported time zones.

date now

date

Get the current date.

date to-timezone

date

Convert a date to a given time zone.

debug

debug

Debug print the value(s) piped in.

debug env

debug

Show environment variables as external commands would get it.

debug experimental-options

debug

Show all experimental options.

debug info

debug

View process memory info.

debug profile

debug

Profile pipeline elements in a closure.

decode

strings

Decode bytes into a string.

decode base32

formats

Decode a Base32-encoded value.

decode base32hex

formats

Encode a base32hex value.

decode base64

formats

Decode a Base64-encoded value.

decode hex

formats

Decode a hex-encoded value.

def

core

Define a custom command.

default

filters

Sets a default value if a row's column is missing or null.

describe

core

Describe the type and structure of the value(s) piped in.

detect

strings

Various commands for detecting things.

detect columns

strings

Attempt to automatically split text into multiple columns.

detect type

strings

Infer Nushell datatype from a string.

do

core

Run a closure, providing it with the pipeline input.

drop

filters

Remove items/rows from the end of the input list/table. Counterpart of `skip`. Opposite of `last`.

drop column

filters

Remove N columns at the right-hand end of the input table. To remove columns by name, use `reject`.

drop nth

filters

Drop the selected rows.

du

filesystem

Find disk usage sizes of specified items.

each

filters

Run a closure on each row of the input list, creating a new list with the results.

each while

filters

Run a closure on each row of the input list until a null is found, then create a new list with the results.

echo

core

Returns its arguments, ignoring the piped-in value.

encode

strings

Encode a string into bytes.

encode base32

formats

Encode a string or binary value using Base32.

encode base32hex

formats

Encode a binary value or a string using base32hex.

encode base64

formats

Encode a string or binary value using Base64.

encode hex

formats

Hex encode a binary value or a string.

enumerate

filters

Enumerate the elements in a stream.

error

core

Various commands for working with errors.

error make

core

Create an error.

every

filters

Show (or skip) every n-th row, starting from the first one.

exec

system

Execute a command, replacing or exiting the current process, depending on platform.

exit

shells

Exit Nu.

explain

debug

Explain closure contents.

explore

viewers

Explore acts as a table pager, just like `less` does for text.

explore config

viewers

Launch a TUI to view and edit the nushell configuration interactively.

explore regex

viewers

Launch a TUI to create and explore regular expressions interactively.

export

core

Export definitions or environment variables from a module.

export alias

core

Alias a command (with optional flags) to a new name and export it from a module.

export const

core

Use parse-time constant from a module and export them from this module.

export def

core

Define a custom command and export it from a module.

export extern

core

Define an extern and export it from a module.

export module

core

Export a custom module from a module.

export use

core

Use definitions from a module and export them from this module.

export-env

env

Run a block and preserve its environment in a current scope.

extern

core

Define a signature for an external command.

fill

conversions

Fill and align text in columns.

filter

filters

Filter values based on a predicate closure.

find

filters

Search for terms in the input data.

first

filters

Return only the first several rows of the input. Counterpart of `last`. Opposite of `skip`.

flatten

filters

Flatten a table by extracting nested values.

for

core

Loop over a range.

format

strings

Various commands for formatting data.

format bits

conversions

Convert value to a string of binary data represented by 0 and 1.

format date

strings

Format a given date using a format string.

format duration

strings

Outputs duration with a specified unit of time.

format filesize

strings

Converts a column of filesizes to some specified format.

format number

conversions

Format a number.

format pattern

strings

Format columns into a string using a simple pattern.

from

formats

Parse a string or binary data into structured data.

from csv

formats

Parse text as .csv and create table.

from eml

formats

Parse text as .eml and create record.

from ics

formats

Parse text as .ics and create table.

from ini

formats

Parse text as .ini and create table.

from json

formats

Convert JSON text into structured data.

from md

formats

Convert markdown text into human-friendly structured rows. Use --verbose for the full AST.

from msgpack

formats

Convert MessagePack data into Nu values.

from msgpackz

formats

Convert brotli-compressed MessagePack data into Nu values.

from nuon

formats

Convert from nuon to structured data.

from ods

formats

Parse OpenDocument Spreadsheet(.ods) data and create table.

from plist

formats

Convert plist to Nushell values

from ssv

formats

Parse text as space-separated values and create a table. The default minimum number of spaces counted as a separator is 2.

from toml

formats

Parse text as .toml and create record.

from tsv

formats

Parse text as .tsv and create table.

from url

formats

Parse url-encoded string as a record.

from vcf

formats

Parse text as .vcf and create table.

from xlsx

formats

Parse binary Excel(.xlsx) data and create table.

from xml

formats

Parse text as .xml and create record.

from yaml

formats

Parse text as .yaml/.yml and create table.

from yml

formats

Parse text as .yaml/.yml and create table.

generate

generators

Generate a list of values by successively invoking a closure.

get

filters

Extract data using a cell path.

glob

filesystem

Creates a list of files and/or folders based on the glob pattern provided.

grid

viewers

Renders the output to a textual terminal grid.

group-by

filters

Splits a list or table into groups, and returns a record containing those groups.

gstat

prompt

Get the git status of a repo

hash

hash

Apply hash function.

hash md5

hash

Hash a value using the md5 hash algorithm.

hash sha256

hash

Hash a value using the sha256 hash algorithm.

headers

filters

Use the first row of the table as column names.

help

core

Display help information about different parts of Nushell.

help aliases

core

Show help on nushell aliases.

help commands

core

Show help on nushell commands.

help escapes

core

Show help on nushell string escapes.

help externs

core

Show help on nushell externs.

help modules

core

Show help on nushell modules.

help operators

core

Show help on nushell operators.

help pipe-and-redirect

core

Show help on nushell pipes and redirects.

hide

core

Hide definitions in the current scope.

hide-env

core

Hide environment variables in the current scope.

histogram

chart

Creates a new table with a histogram based on the column name passed in.

history

history

Get the command history.

history import

history

Import command line history.

history session

history

Get the command history session.

http

network

Various commands for working with http methods.

http delete

network

Delete the specified resource.

http get

network

Fetch the contents from a URL.

http head

network

Get the headers from a URL.

http options

network

Requests permitted communication options for a given URL.

http patch

network

Send a PATCH request to a URL with a request body.

http pool

network

Configure and reset builtin http connection pool.

http post

network

Send a POST request to a URL with a request body.

http put

network

Send a PUT request to a URL with a request body.

idx

filesystem

Manage in-memory file index state.

idx dirs

filesystem

List indexed directories from idx state.

idx drop

filesystem

Drop the current idx runtime from memory.

idx export

filesystem

Persist idx state to disk.

idx files

filesystem

List indexed files, or lookup a specific indexed path.

idx find

filesystem

Search idx with fuzzy matching across files and directories by default.

idx import

filesystem

Import idx state from disk.

idx init

filesystem

Initialize the in-memory idx index for a path.

idx search

filesystem

Search indexed file contents.

idx status

filesystem

Show status information for the global in-memory idx runtime.

if

core

Conditionally run a block.

ignore

core

Ignore the output of the previous command in the pipeline.

inc

default

Increment a value or version. Optionally use the column of a table.

input

platform

Get input from the user via the terminal.

input list

platform

Display an interactive list for user selection.

input listen

platform

Listen for user interface events.

insert

filters

Insert a new column, using an expression or closure to create each row's values.

inspect

debug

Inspect pipeline results while running a pipeline.

interleave

filters

Read multiple streams in parallel and combine them into one stream.

into

conversions

Commands to convert data from one type to another.

into binary

conversions

Convert value to a binary primitive.

into bool

conversions

Convert value to a boolean.

into cell-path

conversions

Convert value to a cell-path.

into datetime

conversions

Convert text or timestamp into a datetime.

into duration

conversions

Convert value to a duration.

into filesize

conversions

Convert value to a filesize.

into float

conversions

Convert data into floating point number.

into glob

conversions

Convert value to a glob pattern.

into int

conversions

Convert value to an integer.

into record

conversions

Convert value to a record.

into sqlite

conversions

Convert table into a SQLite database.

into string

conversions

Convert value to a string.

into value

conversions

Convert custom values into base values.

is-admin

core

Check if nushell is running with administrator or root privileges.

is-empty

filters

Check for empty values.

is-not-empty

filters

Check for non-empty values.

is-terminal

platform

Check if stdin, stdout, or stderr is a terminal.

items

filters

Given a record, iterate on each pair of column name and associated value.

job

experimental

Various commands for working with background jobs.

job describe

experimental

Add a description to a background job.

job flush

experimental

Clear this job's mailbox.

job id

experimental

Get id of current job.

job kill

experimental

Kill a background job.

job list

experimental

List background jobs.

job recv

experimental

Read a message from a job's mailbox.

job send

experimental

Send a message to the mailbox of a job.

job spawn

experimental

Spawn a background job and retrieve its ID.

job unfreeze

experimental

Unfreeze a frozen process job in foreground.

join

filters

Join two tables.

keybindings

platform

Keybindings related commands.

keybindings default

platform

List default keybindings.

keybindings list

platform

List available options that can be used to create keybindings.

keybindings listen

platform

Get input from the user.

kill

platform

Kill a process using its process ID.

last

filters

Return only the last several rows of the input. Counterpart of `first`. Opposite of `drop`.

length

filters

Count the number of items in an input list, rows in a table, or bytes in binary data.

let

core

Create a variable and give it a value.

let-env

removed

`let-env FOO = ...` has been removed, use `$env.FOO = ...` instead.

lines

filters

Converts input to lines.

load-env

filesystem

Loads an environment update from a record.

loop

core

Run a block in a loop.

ls

filesystem

List the filenames, sizes, and modification times of items in a directory.

match

core

Conditionally run a block on a matched value.

math

math

Use mathematical functions as aggregate functions on a list of numbers or tables.

math abs

math

Returns the absolute value of a number.

math arccos

math

Returns the arccosine of the number.

math arccosh

math

Returns the inverse of the hyperbolic cosine function.

math arcsin

math

Returns the arcsine of the number.

math arcsinh

math

Returns the inverse of the hyperbolic sine function.

math arctan

math

Returns the arctangent of the number.

math arctanh

math

Returns the inverse of the hyperbolic tangent function.

math avg

math

Returns the average of a list of numbers.

math ceil

math

Returns the ceil of a number (smallest integer greater than or equal to that number).

math cos

math

Returns the cosine of the number.

math cosh

math

Returns the hyperbolic cosine of the number.

math exp

math

Returns e raised to the power of x.

math floor

math

Returns the floor of a number (largest integer less than or equal to that number).

math ln

math

Returns the natural logarithm. Base: (math e).

math log

math

Returns the logarithm for an arbitrary base.

math max

math

Returns the maximum of a list of values, or of columns in a table.

math median

math

Computes the median of a list of numbers.

math min

math

Finds the minimum within a list of values or tables.

math mode

math

Returns the most frequent element(s) from a list of numbers or tables.

math product

math

Returns the product of a list of numbers or the products of each column of a table.

math round

math

Returns the input number rounded to the specified precision.

math sin

math

Returns the sine of the number.

math sinh

math

Returns the hyperbolic sine of the number.

math sqrt

math

Returns the square root of the input number.

math stddev

math

Returns the standard deviation of a list of numbers, or of each column in a table.

math sum

math

Returns the sum of a list of numbers or of each column in a table.

math tan

math

Returns the tangent of the number.

math tanh

math

Returns the hyperbolic tangent of the number.

math variance

math

Returns the variance of a list of numbers or of each column in a table.

merge

filters

Merge the input with a record or table, overwriting values in matching columns.

merge deep

filters

Merge the input with a record or table, recursively merging values in matching columns.

metadata

debug

Get the metadata for items in the stream.

metadata access

debug

Access the metadata for the input stream within a closure.

metadata set

debug

Set the metadata for items in the stream.

mkdir

filesystem

Create directories, with intermediary directories if required using uutils/coreutils mkdir.

mktemp

filesystem

Create temporary files or directories using uutils/coreutils mktemp.

module

core

Define a custom module.

move

filters

Moves columns relative to other columns or make them the first/last columns. Flags are mutually exclusive.

mut

core

Create a mutable variable and give it a value.

mv

filesystem

Move files or directories using uutils/coreutils mv.

nu-check

strings

Validate and parse Nushell input content.

nu-highlight

strings

Syntax highlight the input string.

open

filesystem

Load a file into a cell, converting to table if possible (avoid by appending '--raw').

overlay

core

Commands for manipulating overlays.

overlay hide

core

Hide an active overlay.

overlay list

core

List all overlays with their active status.

overlay new

core

Create an empty overlay.

overlay use

core

Use definitions from a module as an overlay.

panic

debug

Causes nushell to panic.

par-each

filters

Run a closure on each row of the input list in parallel, creating a new list with the results.

parse

strings

Parse columns from string data using a simple pattern or a supplied regular expression.

path

path

Explore and manipulate paths.

path basename

path

Get the final component of a path.

path dirname

path

Get the parent directory of a path.

path exists

path

Check whether a path exists.

path expand

path

Try to expand a path to its absolute form.

path join

path

Join a structured path or a list of path parts.

path parse

path

Convert a path into structured data.

path relative-to

path

Express a path as relative to another path.

path self

path

Get the absolute path of the script or module containing this command at parse time.

path split

path

Split a path into a list based on the system's path separator.

path type

path

Get the type of the object a path refers to (e.g., file, dir, symlink).

peek

default

Peek the first <n> elements of a stream and store them in the metadata.

plugin

plugin

Commands for managing plugins.

plugin add

plugin

Add a plugin to the plugin registry file.

plugin list

plugin

List loaded and installed plugins.

plugin rm

plugin

Remove a plugin from the plugin registry file.

plugin stop

plugin

Stop an installed plugin if it was running.

plugin use

plugin

Load a plugin from the plugin registry file into scope.

polars

dataframe

Operate with data in a dataframe format.

polars agg

lazyframe

Performs a series of aggregations from a group-by.

polars agg-groups

dataframe

Creates an agg_groups expression.

polars all-false

dataframe

Returns true if all values are false.

polars all-true

dataframe

Returns true if all values are true.

polars append

dataframe

Appends a new dataframe.

polars arg-max

dataframe

Return index for max value in series.

polars arg-min

dataframe

Return index for min value in series.

polars arg-sort

dataframe

Returns indexes for a sorted series.

polars arg-true

dataframe

Returns indexes where values are true.

polars arg-unique

dataframe

Returns indexes for unique values.

polars arg-where

expression

Creates an expression that returns the arguments where expression is true.

polars as

expression

Creates an alias expression.

polars as-date

dataframe

Converts string to date.

polars as-datetime

dataframe

Converts string to datetime.

polars cache

dataframe

Caches operations in a new LazyFrame.

polars cast

dataframe

Cast a column to a different dtype.

polars col

expression

Creates a named column expression.

polars collect

lazyframe

Collect lazy dataframe into eager dataframe.

polars columns

dataframe

Show dataframe columns.

polars concat

dataframe

Concatenate two or more dataframes.

polars concat-str

expression

Creates a concat string expression.

polars contains

dataframe

Checks if a pattern is contained in a string.

polars convert-time-zone

dataframe

Convert datetime to target timezone.

polars count

dataframe

Returns the number of non-null values in the column.

polars count-null

dataframe

Counts null values.

polars cumulative

dataframe

Cumulative calculation for a column or series.

polars cut

dataframe

Bin continuous values into discrete categories for a series.

polars datepart

expression

Creates an expression for capturing the specified datepart in a column.

polars decimal

dataframe

Converts a string column into a decimal column

polars drop

dataframe

Creates a new dataframe by dropping the selected columns.

polars drop-duplicates

dataframe

Drops duplicate values in dataframe.

polars drop-nulls

dataframe

Drops null values in dataframe.

polars dummies

dataframe

Creates a new dataframe with dummy variables.

polars entropy

dataframe

Compute the entropy as `-sum(pk * log(pk))` where `pk` are discrete probabilities.

polars explode

lazyframe

Explodes a dataframe or creates a explode expression.

polars expr-not

dataframe

Creates a not expression.

polars fill-nan

lazyframe

Replaces NaN values with the given expression.

polars fill-null

lazyframe

Replaces NULL values with the given expression.

polars filter

lazyframe

Filter dataframe based in expression.

polars filter-with

dataframe or lazyframe

Filters dataframe using a mask or expression as reference.

polars first

dataframe

Show only the first number of rows or create a first expression

polars flatten

lazyframe

An alias for polars explode.

polars get

dataframe

Creates dataframe with the selected columns.

polars get-day

dataframe

Gets day from date.

polars get-hour

dataframe

Gets hour from datetime.

polars get-minute

dataframe

Gets minute from date.

polars get-month

dataframe

Gets month from date.

polars get-nanosecond

dataframe

Gets nanosecond from date.

polars get-ordinal

dataframe

Gets ordinal from date.

polars get-second

dataframe

Gets second from date.

polars get-week

dataframe

Gets week from date.

polars get-weekday

dataframe

Gets weekday from date.

polars get-year

dataframe

Gets year from date.

polars group-by

lazyframe

Creates a group-by object that can be used for other aggregations.

polars horizontal

expression

Horizontal calculation across multiple columns.

polars implode

dataframe

Aggregates values into a list.

polars integer

dataframe

Converts a string column into a integer column

polars into-df

dataframe

Converts a list, table or record into a dataframe.

polars into-dtype

dataframe

Convert a string to a specific datatype.

polars into-lazy

lazyframe

Converts a dataframe into a lazy dataframe.

polars into-nu

dataframe

Converts a dataframe or an expression into nushell value for access and exploration.

polars into-repr

dataframe

Display a dataframe in its repr format.

polars into-schema

dataframe

Convert a value to a polars schema object

polars is-duplicated

dataframe

Creates mask indicating duplicated values.

polars is-in

expression

Creates an is-in expression or checks to see if the elements are contained in the right series

polars is-not-null

dataframe

Creates mask where value is not null.

polars is-null

dataframe

Creates mask where value is null.

polars is-unique

dataframe

Creates mask indicating unique values.

polars join

lazyframe

Joins a lazy frame with other lazy frame.

polars join-where

lazyframe

Joins a lazy frame with other lazy frame based on conditions.

polars last

dataframe

Creates new dataframe with tail rows or creates a last expression.

polars len

dataframe

Return the number of rows in the context. This is similar to COUNT(*) in SQL.

polars list-contains

dataframe

Checks if an element is contained in a list.

polars lit

expression

Creates a literal expression.

polars lowercase

dataframe

Lowercase the strings in the column.

polars math

dataframe

Collection of math functions to be applied on one or more column expressions

polars max

dataframe

Creates a max expression or aggregates columns to their max value.

polars mean

dataframe

Creates a mean expression for an aggregation or aggregates columns to their mean value.

polars median

lazyframe

Median value from columns in a dataframe or creates expression for an aggregation

polars min

dataframe

Creates a min expression or aggregates columns to their min value.

polars n-unique

dataframe

Counts unique values.

polars not

dataframe

Inverts boolean mask.

polars open

dataframe

Opens CSV, JSON, NDJSON/JSON lines, arrow, avro, or parquet file to create dataframe. A lazy dataframe will be created by default, if supported.

polars otherwise

expression

Completes a when expression.

polars over

lazyframe

Compute expressions over a window group defined by partition expressions.

polars pivot

dataframe

Pivot a DataFrame from long to wide format.

polars profile

dataframe

Profile a lazy dataframe.

polars qcut

dataframe

Bin continuous values into discrete categories based on their quantiles for a series.

polars quantile

lazyframe

Aggregates the columns to the selected quantile.

polars query

dataframe

Query dataframe using SQL. Note: The dataframe is always named 'df' in your query's from clause.

polars rename

dataframe or lazyframe

Rename a dataframe column.

polars replace

expression

Create an expression that replaces old values with new values

polars replace-time-zone

dataframe

Replace the timezone information in a datetime column.

polars reverse

dataframe

Reverses the LazyFrame

polars rolling

dataframe

Rolling calculation for a series.

polars sample

dataframe

Create sample dataframe.

polars save

lazyframe

Saves a dataframe to disk. For lazy dataframes a sink operation will be used if the file type supports it (parquet, ipc/arrow, csv, and ndjson).

polars schema

dataframe

Show schema for a dataframe.

polars select

lazyframe

Selects columns from lazyframe.

polars selector

expression

Create column selectors for use in polars commands.

polars selector all

expression

Creates a selector that selects all columns.

polars selector alpha

expression

Select all columns with alphabetic names (eg: only letters). Matching column names cannot contain *any* non-alphabetic characters. Note that the definition of "alphabetic" consists of all valid Unicode alphabetic characters by default; this can be changed by setting `--ascii-only`.

polars selector alphanumeric

expression

Select all columns with alphanumeric names (eg: only letters). Matching column names cannot contain *any* non-alphanumeric characters. Note that the definition of "alphanumeric" consists of all valid Unicode alphanumeric characters by default; this can be changed by setting `ascii_only=true`.

polars selector array

expression

Select all array columns. Optionally filter by fixed width.

polars selector binary

expression

Select all binary columns.

polars selector boolean

expression

Select all boolean columns.

polars selector by-dtype

expression

Creates a selector that selects columns by data type.

polars selector by-index

expression

Select columns by their index position. Supports negative indices (e.g., -1 for the last column).

polars selector by-name

expression

Creates a selector that selects columns by name.

polars selector categorical

expression

Select all categorical columns.

polars selector contains

expression

Select columns whose names contain the given literal substring(s).

polars selector date

expression

Select all date columns.

polars selector datetime

expression

Select all datetime columns. Optionally filter by time unit (ns, us, ms) and/or timezone.

polars selector decimal

expression

Select all decimal columns.

polars selector digit

expression

Select columns whose names consist entirely of digit characters. By default uses Unicode decimal digits; use `--ascii-only` to restrict to ASCII 0-9.

polars selector duration

expression

Select all duration columns. Optionally filter by time unit (ns, us, ms).

polars selector empty

expression

Create an empty selector that matches no columns. Useful as a base for selector composition.

polars selector ends-with

expression

Select columns that end with the given substring(s).

polars selector enum

expression

Select all enum columns.

polars selector exclude

expression

Select all columns except those with the given name(s). This is the inverse of `polars selector by-name`.

polars selector first

expression

Creates a selector that selects the first column(s) by index.

polars selector float

expression

Select all float columns.

polars selector integer

expression

Select all integer columns.

polars selector last

expression

Creates a selector that selects the last column(s) by index.

polars selector list

expression

Select all list columns.

polars selector matches

expression

Select all columns that match the given regex pattern.

polars selector nested

expression

Select all nested columns (list, array, or struct).

polars selector not

expression

Inverts selector.

polars selector numeric

expression

Select all numeric columns.

polars selector object

expression

Select all object columns.

polars selector signed-integer

expression

Select all signed integer columns.

polars selector starts-with

expression

Select columns that start with the given substring(s).

polars selector string

expression

Select all string columns. Use `--include-categorical` to also select categorical columns.

polars selector struct

expression

Select all struct columns.

polars selector temporal

expression

Select all temporal columns (date, datetime, duration, and time).

polars selector unsigned-integer

expression

Select all unsigned integer columns.

polars set

dataframe

Sets value where given mask is true.

polars set-with-idx

dataframe

Sets value in the given index.

polars shape

dataframe

Shows column and row size for a dataframe.

polars shift

dataframe or lazyframe

Shifts the values by a given period.

polars slice

dataframe

Creates new dataframe from a slice of rows.

polars sort-by

lazyframe

Sorts a lazy dataframe based on expression(s).

polars std

dataframe

Creates a std expression for an aggregation of std value from columns in a dataframe.

polars store-get

dataframe

Gets a Dataframe or other object from the plugin cache.

polars store-ls

dataframe

Lists stored polars objects.

polars store-rm

dataframe

Removes a stored Dataframe or other object from the plugin cache.

polars str-join

dataframe

Concatenates strings within a column or dataframes

polars str-lengths

dataframe

Get lengths of all strings.

polars str-replace

dataframe

Replace the leftmost (sub)string by a regex pattern.

polars str-replace-all

dataframe

Replace all (sub)strings by a regex pattern.

polars str-slice

dataframe

Slices the string from the start position until the selected length.

polars str-split

dataframe

Split the string by a substring. The resulting dtype is list<str>.

polars str-strip-chars

dataframe

Strips specified characters from strings in a column

polars strftime

dataframe

Formats date based on string rule.

polars struct-json-encode

dataframe

Convert this struct to a string column with json values.

polars sum

dataframe

Creates a sum expression for an aggregation or aggregates columns to their sum value.

polars summary

dataframe

For a dataframe, produces descriptive statistics (summary statistics) for its numeric columns.

polars take

dataframe

Creates new dataframe using the given indices.

polars truncate

expression

Divide the date/datetime range into buckets.

polars unique

dataframe or lazyframe

Returns unique values from a dataframe.

polars unnest

dataframe

Decompose struct columns into separate columns for each of their fields. The new columns will be inserted into the dataframe at the location of the struct column.

polars unpivot

dataframe

Unpivot a DataFrame from wide to long format.

polars uppercase

dataframe

Uppercase the strings in the column.

polars value-counts

dataframe

Returns a dataframe with the counts for unique values in series.

polars var

dataframe

Create a var expression for an aggregation.

polars when

expression

Creates and modifies a when expression.

polars with-column

dataframe or lazyframe

Adds a series to the dataframe.

port

network

Get a free TCP port from system.

prepend

filters

Prepend any number of rows to a table.

print

strings

Print the given values to stdout.

ps

system

View information about system processes.

pwd

default

Return the current working directory

query

filters

Show all the query commands

query db

database

Query a SQLite database with SQL statements.

query json

filters

execute json query on json file (open --raw <file> | query json 'query string')

query web

network

execute selector query on html/web

query webpage-info

network

uses the webpage crate to extract info from html: title, description, language, links, RSS feeds, Opengraph, Schema.org, and more

query xml

filters

Execute XPath 1.0 query on XML input

random

random

Generate a random value.

random binary

random

Generate random bytes.

random bool

random

Generate a random boolean value.

random chars

random

Generate random chars uniformly distributed over ASCII letters and numbers: a-z, A-Z and 0-9.

random float

random

Generate a random float within a range [min..max].

random int

random

Generate a random integer [min..max].

random uuid

random

Generate a random uuid string of the specified version.

reduce

filters

Aggregate a list (starting from the left) to a single value using an accumulator closure.

registry

system

Various commands for interacting with the system registry (Windows only).

registry query

system

Query the Windows registry.

reject

filters

Remove the given columns or rows from the table. Opposite of `select`.

rename

filters

Creates a new table with columns renamed.

return

core

Return early from a custom command.

reverse

filters

Reverses the input list or table.

rm

filesystem

Remove files and directories.

roll

filters

Rolling commands for tables.

roll down

filters

Roll table rows down.

roll left

filters

Roll record or table columns left.

roll right

filters

Roll table columns right.

roll up

filters

Roll table rows up.

rotate

filters

Rotates a table or record clockwise (default) or counter-clockwise (use --ccw flag).

run-external

system

Runs external command.

run-internal

default

Run a built-in command by name. Used internally by `%($cmd)` dynamic dispatch.

save

filesystem

Save a file.

schema

database

Show the schema of a SQLite database.

scope

core

Commands for getting info about what is in scope.

scope aliases

core

Output info on the aliases in the current scope.

scope commands

core

Output info on the commands in the current scope.

scope engine-stats

core

Output stats on the engine in the current state.

scope externs

core

Output info on the known externals in the current scope.

scope modules

core

Output info on the modules in the current scope.

scope variables

core

Output info on the variables in the current scope.

select

filters

Select only these columns or rows from the input. Opposite of `reject`.

seq

generators

Output sequences of numbers.

seq char

generators

Print a sequence of ASCII characters.

seq date

generators

Print sequences of dates.

shuffle

filters

Shuffle rows randomly.

skip

filters

Skip the first several rows of the input. Counterpart of `drop`. Opposite of `first`.

skip until

filters

Skip elements of the input until a predicate is true.

skip while

filters

Skip elements of the input while a predicate is true.

sleep

platform

Delay for a specified amount of time.

slice

filters

Return only the selected rows.

sort

filters

Sort the input in increasing order.

sort-by

filters

Sort by the given cell path or closure.

source

core

Runs a script file in the current context.

source-env

core

Source the environment from a source file into the current environment.

split

strings

Split contents across desired subcommand (like row, column) via the separator.

split cell-path

conversions

Split a cell-path into its components.

split chars

strings

Split a string into a list of characters.

split column

strings

Split a string into multiple columns using a separator.

split list

filters

Split a list into multiple lists using a separator.

split row

strings

Split a string into multiple rows using a separator.

split words

strings

Split a string's words into separate rows.

start

filesystem

Open a folder, file, or website in the default application or viewer.

stor

database

Various commands for working with the in-memory sqlite database.

stor create

database

Create a table in the in-memory sqlite database.

stor delete

database

Delete a table or specified rows in the in-memory sqlite database.

stor export

database

Export the in-memory sqlite database to a sqlite database file.

stor import

database

Import a sqlite database file into the in-memory sqlite database.

stor insert

database

Insert information into a specified table in the in-memory sqlite database.

stor open

database

Opens the in-memory sqlite database.

stor reset

database

Reset the in-memory database by dropping all tables.

stor update

database

Update information in a specified table in the in-memory sqlite database.

str

strings

Various commands for working with string data.

str camel-case

strings

Convert a string to camelCase.

str capitalize

strings

Capitalize the first letter of text.

str contains

strings

Checks if string input contains a substring.

str distance

strings

Compare two strings and return the edit distance/Levenshtein distance.

str downcase

strings

Convert text to lowercase.

str ends-with

strings

Check if an input ends with a string.

str escape-regex

strings

Escapes special characters in the input string with '\'.

str expand

strings

Generates all possible combinations defined in brace expansion syntax.

str index-of

strings

Returns start index of first occurrence of string in input, or -1 if no match.

str join

strings

Concatenate multiple strings into a single string, with an optional separator between each.

str kebab-case

strings

Convert a string to kebab-case.

str length

strings

Output the length of any strings in the pipeline.

str pascal-case

strings

Convert a string to PascalCase.

str replace

strings

Find and replace text in the input string.

str reverse

strings

Reverse every string in the pipeline.

str screaming-snake-case

strings

Convert a string to SCREAMING_SNAKE_CASE.

str snake-case

strings

Convert a string to snake_case.

str starts-with

strings

Check if an input starts with a string.

str stats

strings

Gather word count statistics on the text.

str substring

strings

Get part of a string. Note that the first character of a string is index 0.

str title-case

strings

Convert a string to Title Case.

str trim

strings

Trim whitespace or specific character.

str upcase

strings

Convert text to uppercase.

sys

system

View information about the system.

sys cpu

system

View information about the system CPUs.

sys disks

system

View information about the system disks.

sys host

system

View information about the system host.

sys mem

system

View information about the system memory.

sys net

system

View information about the system network interfaces.

sys temp

system

View the temperatures of system components.

sys users

system

View information about the users on the system.

table

viewers

Render the table.

take

filters

Take only the first n elements of a list, or the first n bytes of a binary value.

take until

filters

Take elements of the input until a predicate is true.

take while

filters

Take elements of the input while a predicate is true.

tee

filters

Copy a stream to another command in parallel.

term

platform

Commands for querying information about the terminal.

term query

platform

Query the terminal for information.

term size

platform

Returns a record containing the number of columns (width) and rows (height) of the terminal.

timeit

debug

Time how long it takes a closure to run.

to

formats

Translate structured data to various formats.

to csv

formats

Convert table into .csv text .

to html

formats

Convert table into simple HTML.

to json

formats

Converts table data into JSON text.

to md

formats

Convert table into simple Markdown.

to msgpack

formats

Convert Nu values into MessagePack.

to msgpackz

formats

Convert Nu values into brotli-compressed MessagePack.

to nuon

formats

Converts table data into Nuon (Nushell Object Notation) text.

to plist

formats

Convert Nu values into plist

to text

formats

Convert data into plain text format.

to toml

formats

Convert record into .toml text.

to tsv

formats

Convert table into .tsv text.

to xml

formats

Convert special record structure into .xml text.

to yaml

formats

Convert table into .yaml/.yml text.

to yml

formats

Convert table into .yaml/.yml text.

touch

filesystem

Creates one or more files.

transpose

filters

Transposes the table contents so rows become columns and columns become rows.

try

core

Try to run a block, if it fails optionally run a catch closure.

tutor

misc

Run the tutorial. To begin, run: tutor.

ulimit

platform

Set or get resource usage limits.

umask

platform

Get or set default file creation permissions.

uname

system

Print certain system information using uutils/coreutils uname.

uniq

filters

Return the distinct values in the input.

uniq-by

filters

Return the distinct values in the input by the given column(s).

unlet

experimental

Delete variables from nushell memory, making them unrecoverable.

update

filters

Update an existing column to have a new value.

update cells

filters

Update the table cells.

upsert

filters

Update an existing column to have a new value, or insert a new column.

url

network

Various commands for working with URLs.

url build-query

network

Converts record or table into query string applying percent-encoding.

url decode

strings

Converts a percent-encoded web safe string to a string.

url encode

strings

Converts a string to a percent encoded web safe string.

url join

network

Convert a record to a URL string.

url parse

network

Parse a URL string into structured data.

url split-query

network

Converts query string into table applying percent-decoding.

use

core

Use definitions from a module, making them available in your shell.

values

filters

Given a record or table, produce a list of its columns' values.

version

core

Display Nu version, and its build configuration.

version check

platform

Checks to see if you have the latest version of nushell.

view

debug

Various commands for viewing debug information.

view blocks

debug

View the blocks registered in nushell's EngineState memory.

view files

debug

View the files registered in nushell's EngineState memory.

view ir

debug

View the compiled IR code for a block of code.

view source

debug

View a block, module, or a definition.

view span

debug

View the contents of a span.

watch

filesystem

Watch for file changes and execute Nu code when they happen.

where

filters

Filter values of an input list based on a condition.

which

system

Finds a program file, alias or custom command. If `application` is not provided, all deduplicated commands will be returned.

while

core

Conditionally run a block in a loop.

whoami

platform

Get the current username using uutils/coreutils whoami.

window

filters

Creates a sliding window of `window_size` that slide by n rows/elements across input.

with-env

env

Runs a block with an environment variable set.

wrap

filters

Wrap the value into a column.

zip

filters

Combine a stream with the input.
