---
title: "Dynamic programming language"
source: https://en.wikipedia.org/wiki/Dynamic_programming_language
domain: gradual-typing
license: CC-BY-SA-4.0
tags: gradual typing, dynamic type checking, type soundness, blame calculus
fetched: 2026-07-02
---

# Dynamic programming language

A **dynamic programming language** is a type of programming language that allows various operations to be determined and executed at runtime. This is different from the compilation phase. Key decisions about variables, method calls, or data types are made when the program is running, unlike in static languages, where the structure and types are fixed during compilation. Dynamic languages provide flexibility. This allows developers to write more adaptable and concise code.

For instance, in a dynamic language, a variable can start as an integer. It can later be reassigned to hold a string without explicit type declarations. This feature of dynamic typing enables more fluid and less restrictive coding. Developers can focus on the logic and functionality rather than the constraints of the language.

## Implementation

### Eval

Some dynamic languages offer an *eval* function. This function takes a string or abstract syntax tree containing code in the language and executes it. If this code stands for an expression, the resulting value is returned. Erik Meijer and Peter Drayton distinguish the runtime code generation offered by eval from the dynamic loading offered by shared libraries and warn that in many cases eval is used merely to implement higher-order functions (by passing functions as strings) or deserialization.

### Object runtime alteration

A type or object system can typically be modified during runtime in a dynamic language. This can mean generating new objects from a runtime definition or based on mixins of existing types or objects. This can also refer to changing the inheritance or type tree, and thus altering the way that existing types behave (especially with respect to the invocation of methods).

### Type inference

As a lot of dynamic languages come with a dynamic type system, runtime inference of types based on values for internal interpretation marks a common task. As value types may change throughout interpretation, it is regularly used upon performing atomic operations.

### Variable memory allocation

Static programming languages (possibly indirectly) require developers to define the size of utilized memory before compilation (unless working around with pointer logic). Consistent with object runtime alteration, dynamic languages implicitly need to (re-)allocate memory based on program individual operations.

### Reflection

Reflective programming (reflection) is common in many dynamic languages, and typically involves analysis of the types and metadata of generic or polymorphic data. However, it can also include full evaluation and modification of a program's code as data, as in the features that Lisp provides in analyzing S-expressions.

### Macros

A limited number of dynamic programming languages provide features which combine code introspection (the ability to examine classes, functions, and keywords to know what they are, what they do and what they know) and eval in a feature called macros. Most programmers today who are aware of the term *macro* have encountered them in C or C++, where they are a static feature which is built in a small subset of the language, and are capable only of string substitutions on the text of the program. In dynamic languages, however, they provide access to the inner workings of the compiler, *and* full access to the interpreter, virtual machine, or runtime, allowing the definition of language-like constructs which can optimize code or modify the syntax or grammar of the language.

Assembly, C, C++, early Java, and Fortran do not generally fit into this category.

The earliest dynamic programming language is considered to be Lisp (McCarthy, 1965) which continued to influence the design of programming languages to the present day.

## Example code

The following examples show dynamic features using the language Common Lisp and its Common Lisp Object System (CLOS).

### Computation of code at runtime and late binding

The example shows how a function can be modified at runtime from computed source code

```mw
; the source code is stored as data in a variable
CL-USER > (defparameter *best-guess-formula* '(lambda (x) (* x x 2.5)))
*BEST-GUESS-FORMULA*

; a function is created from the code and compiled at runtime, the function is available under the name best-guess
CL-USER >  (compile 'best-guess *best-guess-formula*)
#<Function 15 40600152F4>

; the function can be called
CL-USER > (best-guess 10.3)
265.225

; the source code might be improved at runtime
CL-USER > (setf *best-guess-formula* `(lambda (x) ,(list 'sqrt (third *best-guess-formula*))))
(LAMBDA (X) (SQRT (* X X 2.5)))

; a new version of the function is being compiled
CL-USER > (compile 'best-guess *best-guess-formula*)
#<Function 16 406000085C>

; the next call will call the new function, a feature of late binding
CL-USER > (best-guess 10.3)
16.28573
```

### Object runtime alteration

This example shows how an existing instance can be changed to include a new slot when its class changes and that an existing method can be replaced with a new version.

```mw
; a person class. The person has a name.
CL-USER > (defclass person () ((name :initarg :name)))
#<STANDARD-CLASS PERSON 4020081FB3>

; a custom printing method for the objects of class person
CL-USER > (defmethod print-object ((p person) stream)
            (print-unreadable-object (p stream :type t)
              (format stream "~a" (slot-value p 'name))))
#<STANDARD-METHOD PRINT-OBJECT NIL (PERSON T) 4020066E5B>

; one example person instance
CL-USER > (setf *person-1* (make-instance 'person :name "Eva Luator"))
#<PERSON Eva Luator>

; the class person gets a second slot. It then has the slots name and age.
CL-USER > (defclass person () ((name :initarg :name) (age :initarg :age :initform :unknown)))
#<STANDARD-CLASS PERSON 4220333E23>

; updating the method to print the object
CL-USER > (defmethod print-object ((p person) stream)
            (print-unreadable-object (p stream :type t)
              (format stream "~a age: ~" (slot-value p 'name) (slot-value p 'age))))
#<STANDARD-METHOD PRINT-OBJECT NIL (PERSON T) 402022ADE3>

; the existing object has now changed, it has an additional slot and a new print method
CL-USER > *person-1*
#<PERSON Eva Luator age: UNKNOWN>

; we can set the new age slot of instance
CL-USER > (setf (slot-value *person-1* 'age) 25)
25

; the object has been updated
CL-USER > *person-1*
#<PERSON Eva Luator age: 25>
```

### Assembling of code at runtime based on the class of instances

In the next example, the class **person** gets a new superclass. The **print** method gets redefined such that it assembles several methods into the effective method. The effective method gets assembled based on the class of the argument and the at runtime available and applicable methods.

```mw
; the class person
CL-USER > (defclass person () ((name :initarg :name)))
#<STANDARD-CLASS PERSON 4220333E23>

; a person just prints its name
CL-USER > (defmethod print-object ((p person) stream)
            (print-unreadable-object (p stream :type t)
              (format stream "~a" (slot-value p 'name))))
#<STANDARD-METHOD PRINT-OBJECT NIL (PERSON T) 40200605AB>

; a person instance
CL-USER > (defparameter *person-1* (make-instance 'person :name "Eva Luator"))
*PERSON-1*

; displaying a person instance
CL-USER > *person-1*
#<PERSON Eva Luator>

; now redefining the print method to be extensible
; the around method creates the context for the print method and it calls the next method
CL-USER > (defmethod print-object :around ((p person) stream)
            (print-unreadable-object (p stream :type t)
              (call-next-method)))
#<STANDARD-METHOD PRINT-OBJECT (:AROUND) (PERSON T) 4020263743>

; the primary method prints the name
CL-USER > (defmethod print-object ((p person) stream)
            (format stream "~a" (slot-value p 'name)))
#<STANDARD-METHOD PRINT-OBJECT NIL (PERSON T) 40202646BB>

; a new class id-mixin provides an id
CL-USER > (defclass id-mixin () ((id :initarg :id)))
#<STANDARD-CLASS ID-MIXIN 422034A7AB>

; the print method just prints the value of the id slot
CL-USER > (defmethod print-object :after ((object id-mixin) stream)
          (format stream " ID: ~a" (slot-value object 'id)))
#<STANDARD-METHOD PRINT-OBJECT (:AFTER) (ID-MIXIN T) 4020278E33>

; now we redefine the class person to include the mixin id-mixin
CL-USER > (defclass person (id-mixin) ((name :initarg :name)))
#<STANDARD-CLASS PERSON 4220333E23>

; the existing instance *person-1* now has a new slot and we set it to 42
CL-USER > (setf (slot-value *person-1* 'id) 42)
42

; displaying the object again. The print-object function now has an effective method, which calls three methods: an around method, the primary method and the after method.
CL-USER > *person-1*
#<PERSON Eva Luator ID: 42>
```

## Examples

Popular dynamic programming languages include JavaScript, Python, Ruby, PHP, Lua, and Perl. The following are generally considered dynamic languages:

- ActionScript
- BeanShell
- C# (using reflection)
- Clojure
- CobolScript
- ColdFusion Markup Language
- Common Lisp and most other Lisps
- Dylan
- E
- Elixir
- Erlang
- Forth
- Gambas
- GDScript
- Groovy
- Java (using Reflection)
- JavaScript
- Julia
- Lua
- MATLAB – Octave
- Objective-C
- Object REXX (ooRexx)
- Perl
- PHP
- PowerShell
- Prolog
- Python
- R
- Raku
- Rebol
- Ruby
- Smalltalk
- SuperCollider
- Tcl
- VBScript
- Wolfram Language
