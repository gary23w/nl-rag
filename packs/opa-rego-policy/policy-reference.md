---
title: "Policy Reference"
source: https://www.openpolicyagent.org/docs/latest/policy-reference/
domain: opa-rego-policy
license: CC-BY-SA-4.0
tags: open policy agent, rego policy language, declarative authorization query, policy decision point
fetched: 2026-07-02
---

# Policy Reference

This page is a reference for details of the Rego language and its syntax. See the guided Policy Language page for a walked introduction. There are also detailed sections for built-in functions as well as examples for specific keywords such as `contains`, `if` and `default`.

## Assignment and Equality

```rego
x := input.foo.bar.baz

x == y

x == {"foo", "bar"}

{"foo", "bar"} == x
```

## Lookup

### Arrays

```rego
val := arr[0]

 
"foo" == arr[0]

"foo" == arr[i]

val := arr[count(arr)-1]

some 0, val in arr   
0, "foo" in arr      
some i, "foo" in arr 
```

### Objects

```rego
val := obj["foo"]

"bar" == obj["foo"]

"bar" == obj.foo

obj.foo

k := "foo"
obj[k]

obj.foo.bar.baz

not obj.foo.bar.baz

o := {"foo": false}

false in o

"foo", false in o
```

### Sets

```rego
a_set["foo"]

not a_set["foo"]

a_set[["a", "b", "c"]]

a_set[[x, "b", z]]

"foo" in a_set
not "foo" in a_set
some ["a", "b", "c"] in a_set
some [x, "b", z] in a_set
```

## Iteration

### Arrays

```rego
arr[i]

val := arr[_]

val := arr[i]

some val in arr    
some i, _ in arr   
some i, val in arr 
```

### Objects

```rego
obj[key]

val := obj[_]

val := obj[key]

some val in obj      
some key, _ in obj   
some key, val in obj 
```

### Sets

```rego
set[val]

some val in set
```

### Advanced

```rego
foo[k].bar.baz[i] == 7

foo[k1] == bar[k2]

foo[k1] == foo[k2]; k1 != k2

foo[k].bar.baz[i] == 7; foo[k].qux > 3
```

## For All

```rego
count({x | set[x]; f(x)}) == 0

count({x | set[x]; f(x)}) == count(set)

not any_match

not any_not_match
```

```rego
any_match if {
    some x in set
    f(x)
}

any_not_match if {
    some x in set
    not f(x)
}
```

## Rules

In the examples below `...` represents one or more conditions.

### Constants

```rego
a := {1, 2, 3}
b := {4, 5, 6}
c := a | b
```

### Conditionals (Boolean)

```rego
p := true { ... }

p if { ... }

p { ... }
```

### Conditionals

```rego
default a := 1
a := 5   if { ... }
a := 100 if { ... }
```

### Incremental

```rego
a_set[x] { ... }
a_set[y] { ... }

a_set contains x if { ... }
a_set contains y if { ... }

a_map[x] := y if { ... }
a_map[w] := z if { ... }
```

### Ordered (Else)

```rego
default a := 1
a := 5 if { ... }
else := 10 if { ... }
```

### Functions (Boolean)

```rego
f(x, y) if {
    ...
}

f(x, y) := true if {
    ...
}
```

### Functions (Conditionals)

```rego
f(x) := "A" if { x >= 90 }
f(x) := "B" if { x >= 80; x < 90 }
f(x) := "C" if { x >= 70; x < 80 }
```

### Reference Heads

```rego
fruit.apple.seeds = 12 if input == "apple"             

fruit.pineapple.colors contains x if x := "yellow"     

fruit.banana.phone[x] = "bananular" if x := "cellular" 
fruit.banana.phone.cellular = "bananular" if true      

fruit.orange.color(x) = true if x == "orange"          
```

For reasons of backwards-compatibility, partial sets need to use `contains` in their rule heads, i.e.

```rego
fruit.box contains "apples" if true
```

whereas

```rego
fruit.box[x] if { x := "apples" }
```

defines a *complete document rule* `fruit.box.apples` with value `true`. The same is the case of rules with brackets that don't contain dots, like

```rego
box[x] if { x := "apples" } 
box2[x] { x := "apples" } 
```

For backwards-compatibility, rules *without* if and without *dots* will be interpreted as defining partial sets, like `box2`.

## Tests

```rego
package foo.bar_test 

test_NAME { ... }

data.foo.bar.deny with input.foo as {"bar": [1,2,3]}}
```

tip

Please see Policy Testing for an in depth look into writing and running Rego tests with OPA.

## Built-in Functions

Rego's built-in functions offer policy authors tools for common policy operations like JWT validation, signature verification, among many others. The reference documentation for these functions can be found under Built-in Functions.

## Reserved Names & Keywords

The following words are reserved and cannot be used as variable names or rule names:

- `as`
- `contains` (Examples)
- `data`
- `default` (Examples)
- `else`
- `every` (Examples)
- `false`
- `if` (Examples)
- `in`
- `import` (Examples)
- `input`
- `package`
- `not` (Examples)
- `null`
- `some` (Examples)
- `true`
- `with`

## Grammar

Rego’s syntax is defined by the following grammar:

```ebnf
module          = package { import } policy
package         = "package" ref
import          = "import" ref [ "as" var ]
policy          = { rule }
rule            = [ "default" ] rule-head { rule-body }
rule-head       = ( ref | var ) ( rule-head-set | rule-head-obj | rule-head-func | rule-head-comp )
rule-head-comp  = [ assign-operator term ] [ "if" ]
rule-head-obj   = "[" term "]" [ assign-operator term ] [ "if" ]
rule-head-func  = "(" rule-args ")" [ assign-operator term ] [ "if" ]
rule-head-set   = "contains" term [ "if" ] | "[" term "]"
rule-args       = term { "," term }
rule-body       = [ "else" [ assign-operator term ] [ "if" ] ] ( "{" query "}" ) | literal
query           = literal { ( ";" | ( [CR] LF ) ) literal }
literal         = ( some-decl | expr | "not" ( expr | "{" query "}" ) ) { with-modifier }
with-modifier   = "with" term "as" term
some-decl       = "some" term { "," term } { "in" expr }
expr            = term | expr-call | expr-infix | expr-every | expr-parens | unary-expr
expr-call       = var [ "." var ] "(" [ expr { "," expr } ] ")"
expr-infix      = expr infix-operator expr
expr-every      = "every" var { "," var } "in" ( term | expr-call | expr-infix ) "{" query "}"
expr-parens     = "(" expr ")"
unary-expr      = "-" expr
membership      = term [ "," term ] "in" term
term            = ref | var | scalar | array | object | set | membership | array-compr | object-compr | set-compr
array-compr     = "[" term "|" query "]"
set-compr       = "{" term "|" query "}"
object-compr    = "{" object-item "|" query "}"
infix-operator  = assign-operator | bool-operator | arith-operator | bin-operator
bool-operator   = "==" | "!=" | "<" | ">" | ">=" | "<="
arith-operator  = "+" | "-" | "*" | "/" | "%"
bin-operator    = "&" | "|"
assign-operator = ":=" | "="
ref             = ( var | array | object | set | array-compr | object-compr | set-compr | expr-call ) { ref-arg }
ref-arg         = ref-arg-dot | ref-arg-brack
ref-arg-brack   = "[" ( scalar | var | array | object | set | "_" ) "]"
ref-arg-dot     = "." var
var             = ( ALPHA | "_" ) { ALPHA | DIGIT | "_" }
scalar          = string | NUMBER | TRUE | FALSE | NULL
string          = STRING | raw-string | template-string
template-string = "$" ( '"' { CHAR-'"' | template-expr } '"' | "`" { CHAR-"`" | template-expr } "`" )
template-expr   = "{" ( ref | var | scalar | array | object | set | array-compr | object-compr | set-compr | expr-call | expr-infix | expr-parens | unary-expr ) "}"
raw-string      = "`" { CHAR-"`" } "`"
array           = "[" term { "," term } "]"
object          = "{" object-item { "," object-item } "}"
object-item     = ( scalar | ref | var ) ":" term
set             = empty-set | non-empty-set
non-empty-set   = "{" term { "," term } "}"
empty-set       = "set(" ")"
```

The grammar defined above makes use of the following syntax. See the Wikipedia page on EBNF for more details:

```
[]     optional (zero or one instances)
{}     repetition (zero or more instances)
|      alternation (one of the instances)
()     grouping (order of expansion)
STRING JSON string
NUMBER JSON number
TRUE   JSON true
FALSE  JSON false
NULL   JSON null
CHAR   Unicode character
ALPHA  ASCII characters A-Z and a-z
DIGIT  ASCII characters 0-9
CR     Carriage Return
LF     Line Feed
```
