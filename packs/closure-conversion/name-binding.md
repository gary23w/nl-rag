---
title: "Name binding"
source: https://en.wikipedia.org/wiki/Name_binding
domain: closure-conversion
license: CC-BY-SA-4.0
tags: closure conversion, lambda lifting, free variable capture, environment representation
fetched: 2026-07-02
---

# Name binding

In computer programming, **name binding** is the association of a data or code entity with an identifier. An identifier bound to an entity is said to reference that entity. A machine language has no built-in notion of identifiers, but name-entity binding as a service and notation for the programmer is implemented by higher-level programming languages. Binding is intimately connected with scoping, as scope determines which names bind to which entities – at which locations in the program code (lexically) and in which one of the possible execution paths (temporally).

Use of an identifier id in a context that establishes a binding for id is called a binding (or defining) occurrence. In all other occurrences (e.g., in expressions, assignments, and subprogram calls), an identifier stands for what it is bound to; such occurrences are called applied occurrences.

## Rebinding and mutation

Rebinding should not be confused with mutation or assignment. *Rebinding* is a change to the *referencing* identifier. *Assignment* is a change to (the referenced) variable. *Mutation* is a change to an entity in memory, possibly referenced by a variable or bound to an identifier.

Consider the following Java code:

```mw
import java.util.LinkedList;

LinkedList<String> list; // implicitly initialised to 'null'
list = new LinkedList<>();
list.add("foo");
list = null;
{ 
    LinkedList<Integer> list = new LinkedList<>(); 
    list.add(2);
}
```

The identifier `list` is bound to a variable in the first line; in the second, a linked list of strings is assigned to the variable. The linked list referenced by the variable is then mutated, adding a string to the list. Next, the variable is assigned the constant `null`. In the last line, the identifier is rebound for the scope of the block. Operations within the block access a new variable and not the variable previously bound to `list`.
