---
title: "Scope (computer programming) (part 2/2)"
source: https://en.wikipedia.org/wiki/Lexical_scoping
domain: closure-conversion
license: CC-BY-SA-4.0
tags: closure conversion, lambda lifting, free variable capture, environment representation
fetched: 2026-07-02
part: 2/2
---

## By language

Scope rules for representative languages follow.

### C

In C, scope is traditionally known as **linkage** or **visibility**, particularly for variables. C is a lexically scoped language with global scope (known as *external linkage*), a form of module scope or file scope (known as *internal linkage*), and local scope (within a function); within a function scopes can further be nested via block scope. However, standard C does not support nested functions.

The lifetime and visibility of a variable are determined by its storage class. There are three types of lifetimes in C: static (program execution), automatic (block execution, allocated on the stack), and manual (allocated on the heap). Only static and automatic are supported for variables and handled by the compiler, while manually allocated memory must be tracked manually across different variables. There are three levels of visibility in C: external linkage (global), internal linkage (roughly file), and block scope (which includes functions); block scopes can be nested, and different levels of internal linkage is possible by use of includes. Internal linkage in C is visibility at the translation unit level, namely a source file after being processed by the C preprocessor, notably including all relevant includes.

C programs are compiled as separate object files, which are then linked into an executable or library via a linker. Thus name resolution is split across the compiler, which resolves names within a translation unit (more loosely, "compilation unit", but this is properly a different concept), and the linker, which resolves names across translation units; see linkage for further discussion.

In C, variables with block scope enter context when they are declared (not at the top of the block), go out of context if any (non-nested) function is called within the block, come back into context when the function returns, and go out of context at the end of the block. In the case of automatic local variables, they are also allocated on declaration and deallocated at the end of the block, while for static local variables, they are allocated at program initialization and deallocated at program termination.

The following program demonstrates a variable with block scope coming into context partway through the block, then exiting context (and in fact being deallocated) when the block ends:

```mw
#include <stdio.h>

int main(void) {
    char x = 'm';
    printf("%c\n", x);

    {
        printf("%c\n", x);
        char x = 'b';
        printf("%c\n", x);
    }

    printf("%c\n", x);
}
```

The program outputs:

```
m
m
b
m
```

There are other levels of scope in C. Variable names used in a function prototype have function prototype visibility, and exit context at the end of the function prototype. Since the name is not used, this is not useful for compilation, but may be useful for documentation. Label names for GOTO statement have function scope.

### C++

All the variables to use in a program must have been declared with its type specifier in an earlier point in the code, as done in the prior code at the start of the body of the function `main` when declaring that a, b, and result were of type int. A variable can be either of global or local scope. A global variable is a variable declared in the main body of the source code, outside all functions, while a local variable is one declared within the body of a function or a block.

Modern versions allow nested lexical scope.

### Swift

Swift has a similar rule for scopes with C++, but contains different access modifiers.

| Modifier | Immediate scope | File | Containing module/package | Rest of the world |
|---|---|---|---|---|
| open | Yes | Yes | Yes | Yes, allows subclass |
| public | Yes | Yes | Yes | Yes, disallows subclass |
| internal | Yes | Yes | Yes | No |
| fileprivate | Yes | Yes | No | No |
| private | Yes | No | No | No |

### Go

Go is lexically scoped using blocks.

### Java

Java is lexically scoped.

A Java class has several kinds of variables:

**Local variables**

are defined inside a method, or a particular block. These variables are local to where they were defined and lower levels. For example, a loop inside a method can use that method's local variables, but not the other way around. The loop's variables (local to that loop) are destroyed as soon as the loop ends.

**Member variables**

also called

fields

are variables declared within the class, outside of any method. By default, these variables are available for all methods within that class and also for all classes in the package.

**Parameters**

are variables in method declarations.

In general, a set of brackets defines a particular scope, but variables at top level within a class can differ in their behavior depending on the modifier keywords used in their definition. The following table shows the access to members permitted by each modifier.

| Modifier | Class | Package | Subclass | World |
|---|---|---|---|---|
| public | Yes | Yes | Yes | Yes |
| protected | Yes | Yes | Yes | No |
| (no modifier) | Yes | Yes | No | No |
| private | Yes | No | No | No |

### JavaScript

JavaScript has simple *scope rules*, but variable initialization and name resolution rules can cause problems, and the widespread use of closures for callbacks means the lexical context of a function when defined (which is used for name resolution) can be very different from the lexical context when it is called (which is irrelevant for name resolution). JavaScript objects have name resolution for properties, but this is a separate topic.

JavaScript has lexical scope nested at the function level, with the global context being the outermost context. This scope is used for both variables and for functions (meaning function declarations, as opposed to variables of function type). Block scope with the `let` and `const` keywords is standard since ECMAScript 6. Block scope can be produced by wrapping the entire block in a function and then executing it; this is known as the immediately-invoked function expression (IIFE) pattern.

While JavaScript scope is simple—lexical, function-level—the associated initialization and name resolution rules are a cause of confusion. Firstly, assignment to a name not in scope defaults to creating a new global variable, not a local one. Secondly, to create a new local variable one must use the `var` keyword; the variable is then created at the top of the function, with value `undefined` and the variable is assigned its value when the assignment expression is reached:

A variable with an

Initialiser

is assigned the value of its

AssignmentExpression

when the

VariableStatement

is executed, not when the variable is created.

This is known as *variable hoisting*—the declaration, but not the initialization, is hoisted to the top of the function. Thirdly, accessing variables before initialization yields `undefined`, rather than a syntax error. Fourthly, for function declarations, the declaration and the initialization are both hoisted to the top of the function, unlike for variable initialization. For example, the following code produces a dialog with output undefined, as the local variable declaration is hoisted, shadowing the global variable, but the initialization is not, so the variable is undefined when used:

```mw
a = 1;
function f() {
  alert(a);
  var a = 2;
}
f();
```

Further, as functions are first-class objects in JavaScript and are frequently assigned as callbacks or returned from functions, when a function is executed, the name resolution depends on where it was originally defined (the lexical context of the definition), not the lexical context or execution context where it is called. The nested scopes of a particular function (from most global to most local) in JavaScript, particularly of a closure, used as a callback, are sometimes referred to as the **scope chain**, by analogy with the prototype chain of an object.

Closures can be produced in JavaScript by using nested functions, as functions are first-class objects. Returning a nested function from an enclosing function includes the local variables of the enclosing function as the (non-local) lexical context of the returned function, yielding a closure. For example:

```mw
function newCounter() {
  // return a counter that is incremented on call (starting at 0)
  // and which returns its new value
  var a = 0;
  var b = function() { a++; return a; };
  return b;
}
c = newCounter();
alert(c() + ' ' + c());  // outputs "1 2"
```

Closures are frequently used in JavaScript, due to being used for callbacks. Indeed, any hooking of a function in the local context as a callback or returning it from a function creates a closure if there are any unbound variables in the function body (with the context of the closure based on the nested scopes of the current lexical context, or "scope chain"); this may be accidental. When creating a callback based on parameters, the parameters must be stored in a closure, otherwise it will accidentally create a closure that refers to the variables in the enclosing context, which may change.

Name resolution of properties of JavaScript objects is based on inheritance in the prototype tree—a path to the root in the tree is called a *prototype chain*—and is separate from name resolution of variables and functions.

### Lisp

Lisp dialects have various rules for scope.

The original Lisp used dynamic scope; it was Scheme, inspired by ALGOL, that introduced static (lexical) scope to the Lisp family.

Maclisp used dynamic scope by default in the interpreter and lexical scope by default in compiled code, though compiled code could access dynamic bindings by use of `SPECIAL` declarations for particular variables. However, Maclisp treated lexical binding more as an optimization than one would expect in modern languages, and it did not come with the closure feature one might expect of lexical scope in modern Lisps. A separate operation, `*FUNCTION`, was available to somewhat clumsily work around some of that issue.

Common Lisp adopted lexical scope from Scheme, as did Clojure.

ISLISP has lexical scope for ordinary variables. It also has dynamic variables, but they are in all cases explicitly marked; they must be defined by a `defdynamic` special form, bound by a `dynamic-let` special form, and accessed by an explicit `dynamic` special form.

Some other dialects of Lisp, like Emacs Lisp, still use dynamic scope by default. Emacs Lisp now has lexical scope available on a per-buffer basis.

### Python

For variables, Python has function scope, module scope, and global scope. Names enter context at the start of a scope (function, module, or global scope), and exit context when a non-nested function is called or the scope ends. If a name is used prior to variable initialization, this raises a runtime exception. If a variable is simply accessed (not assigned to), name resolution follows the LEGB (Local, Enclosing, Global, Built-in) rule which resolves names to the narrowest relevant context. However, if a variable is assigned to, it defaults to declaring a variable whose scope starts at the start of the level (function, module, or global), not at the assignment. Both these rules can be overridden with a `global` or `nonlocal` (in Python 3) declaration prior to use, which allows accessing global variables even if there is a masking nonlocal variable, and assigning to global or nonlocal variables.

As a simple example, a function resolves a variable to the global scope:

```mw
def f() -> None:
    print(x)

x: str = "global"
f()
# prints: global
```

Note that `x` is defined before `f` is called, so no error is raised, even though it is defined after its reference in the definition of `f`. Lexically this is a forward reference, which is allowed in Python.

Here assignment creates a new local variable, which does not change the value of the global variable:

```mw
def f() -> None:
    x: str = "f"
    print(x)

x: str = "global"
print(x)
# prints: global
f()
# prints: f
print(x)
# prints: global
```

Assignment to a variable within a function causes it to be declared local to the function, hence its scope is the entire function, and thus using it prior to this assignment raises an error. This differs from C, where the scope of the local variable start at its declaration. This code raises an error:

```mw
def f() -> None:
    print(x)
    x: str = "f"

x: str = "global"
f()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in f
# UnboundLocalError: local variable 'x' referenced before assignment
```

The default name resolution rules can be overridden with the `global` or `nonlocal` (in Python 3) keywords. In the below code, the `global x` declaration in `g` means that `x` resolves to the global variable. It thus can be accessed (as it has already been defined), and assignment assigns to the global variable, rather than declaring a new local variable. Note that no `global` declaration is needed in `f`—since it does not assign to the variable, it defaults to resolving to the global variable.

```mw
def f() -> None:
    print(x)

def g() -> None:
    global x
    print(x)
    x = "g"

x: str = "global"
f()
# prints: global
g()
# prints: global
f()
# prints: g
```

`global` can also be used for nested functions. In addition to allowing assignment to a global variable, as in an unnested function, this can also be used to access the global variable in the presence of a nonlocal variable:

```mw
def f() -> None:
    def g() -> None:
        global x
        print(x)
    x: str = "f"
    g()

x: str = "global"
f()
# prints: global
```

For nested functions, there is also the `nonlocal` declaration, for assigning to a nonlocal variable, similar to using `global` in an unnested function:

```mw
def f() -> None:
    def g() -> None:
        nonlocal x  # Python 3 only
        x = "g"
    x: str = "f"
    g()
    print(x)

x: str = "global"
f()
# prints: g
print(x)
# prints: global
```

### R

R is a lexically scoped language, unlike other implementations of S where the values of free variables are determined by a set of global variables, while in R they are determined by the context in which the function was created. The scope contexts may be accessed using a variety of features (such as `parent.frame()`) which can simulate the experience of dynamic scope should the programmer desire.

There is no block scope:

```mw
a <- 1
{
  a <- 2
}
message(a)

## 2
```

Functions have access to scope they were created in:

```mw
a <- 1
f <- function() {
  message(a)
}
f()

## 1
```

Variables created or modified within a function stay there:

```mw
a <- 1
f <- function() {
  message(a)
  a <- 2
  message(a)
}
f()

## 1

## 2
message(a)

## 1
```

Variables created or modified within a function stay there unless assignment to enclosing scope is explicitly requested:

```mw
a <- 1
f <- function() {
  message(a)
  a <<- 2
  message(a)
}
f()

## 1

## 2
message(a)

## 2
```

Although R has lexical scope by default, function scopes can be changed:

```mw
a <- 1
f <- function() {
  message(a)
}
my_env <- new.env()
my_env$a <- 2
f()

## 1
environment(f) <- my_env
f()

## 2
```
