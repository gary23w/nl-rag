---
title: "NekoVM"
source: https://en.wikipedia.org/wiki/NekoVM
domain: haxe-language
license: CC-BY-SA-4.0
tags: haxe language, cross platform software, actionscript language, source to source compiler, neko virtual machine
fetched: 2026-07-02
---

# NekoVM

**NekoVM** is a virtual machine developed by Nicolas Cannasse as part of research and development (R&D) efforts at two independent video game developers in Bordeaux, France: first at Motion Twin and then at Shiro Games. NekoVM's native language is the bytecode for a high-level dynamically typed programming language called Neko. This pairing allows Neko to be used directly as an embedded scripting language, or to target NekoVM by compiling another language (such as Haxe) to NekoVM bytecode.

## Concept

Neko has a compiler and a virtual machine (VM) with garbage collection. The compiler converts a source .neko file into a bytecode .n file that can be executed with the VM. Since Neko is dynamically typed with no fixed classes, a developer only needs to find the proper runtime mapping (in contrast to data type mapping) so that code executes correctly. As the Neko FAQ puts it: "...it is easier to write a new or existing language on the NekoVM than it is for the CLR / JVM, since you don’t have to deal with a highlevel type system. Also, this means that languages can interoperate more easily since they only need to share the same data structures and not always the same types."

Neko requires compiling before executing, like other scripting languages such as Apache Groovy. Since Neko need not be interpreted at runtime, it executes faster. The Haxe language can compile to Neko code, among other targets.

## Virtual machine

The Neko virtual machine is used to execute a Neko bytecode file, the VM also has the option to convert a bytecode file into an executable file (output changes depending on the target operating system).

## Language

### Hello World

```mw
$print("Hello World!");
```

### Type conversions

```mw
$int("67.87"); // Converts string "67.87" to integer 67
$float(12345); // Converts integer 12345 to float 12345.0000
$string($array(1,2,3)); // Converts array [1,2,3] to string "[1,2,3]"
```

### Objects

```mw
o = $new(null); // new empty object
o2 = $new(o); // makes a copy of o
o2 = $new(33); // if parameter is not an object, throw an exception
o.field = value; //sets field to value
o.field; // returns "field" value of object o
```

### Methods

```mw
foo = function() {
	$print(this.x);
}
o = $new(null);
o.x = 3;
o.bar = function() {
	foo();
};
o.bar(); // prints 3
```

### Function scope

```mw
var x = 3;
f = function() {
	$print(x);
}
x = 4;
f(); // print 3
```

### Prototypes

```mw
var proto = $new(null);
proto.foo = function() {
  $print(this.msg)
}

var o = $new(null);
o.msg = "hello";
$objsetproto(o,proto);
o.foo(); // print "hello"

$objsetproto(o,null); // remove proto
o.foo(); // exception
```

### Web functionality

Neko includes Apache server modules mod_neko for Neko language and mod_tora for hosting the NekoVM application server tora. As such, it can process user input using GET and POST requests:

```mw
get_params = $loader.loadprim("mod_neko@get_params",0);
$print("PARAMS = "+get_params());
```
