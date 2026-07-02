---
title: "Data structures (part 2/2)"
source: https://lispcookbook.github.io/cl-cookbook/data-structures.html
domain: common-lisp
license: CC-BY-SA-4.0
tags: common lisp, hyperspec, clos, sbcl
fetched: 2026-07-02
part: 2/2
---

## Plist

### What’s a plist

A property list is simply a list that alternates a key, a value, and so on, where its keys are keywords or symbols.

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))
```

A plist is a key-value store, like hash-tables. However, unlike hash-tables:

- a plist can store twice the same key. As such, it can be used as a queue (a “Last In First Out”), read below.
- a plist is inherently a (linked) list, and has the same performance characteristics. For non-small data sets, use hash-tables.
  - plists are OK for configuration variables, user settings, manipulating function arguments, small internal data structures…
- you can’t really use strings as keys.

The keys could be any other object, but if they are not comparable by `eq` (the lowest-level equality function), like strings (that are comparable with `equal` or `string-equal`), you won’t be able to get them back with `getf`.

To be more precise, a plist first has a cons cell whose `car` is the key, whose `cdr` points to the following cons cell whose `car` is the value. For example our above plist looks like this:

```
[o|o]---[o|o]---[o|o]---[o|/]
 |       |       |       |
:FOO     "foo"   :BAR     "bar"
```

In the example above, we used keywords for the keys: `:foo`, `:bar`. This is just the most common way to define the keys. You can use quoted symbols instead: `'foo`, `'bar`, but it’s just less conventional.

Remember that if you use symbols for keys, then when you’ll want to access those keys from another package, you’ll need to use the fully-qualified symbol name. However, all keywords live in the same package so they always evaluate to themselves. It’s a bit simpler to use keywords.

### Accessing data in a plist, using plists as queues

We access an element with `getf`:

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))
;; => (:FOO "foo" :BAR "bar")
(getf my-plist :foo)
;; => "foo"
```

Remember that we can’t set a `:test` keyword to `getf`. Keys must be *identical* by `eq` for `getf` to get you the key. If you use strings for the keys, it won’t work:

```lisp
(defparameter not-ok-plist (list "foo" "this-is-foo" "bar" "this-is-bar"))

;; you get NIL, even if you can see "foo" is a key:
(getf not-ok-plist "foo")
;; => NIL

;; We didn't create a plist, but a list.
```

A plist can be used as a queue. If it has twice the same key, `getf` takes the value of the first one (from left to right):

```lisp
(defparameter my-plist (list :foo "lifo" :foo "foo" :bar "bar"))
;;                           ^^           ^^ twice the key :foo

(getf my-plist :foo)
;; => "lifo"
```

### Removing elements from a plist

To remove an element from a plist, you’d use `remf`, which destructively changes the plist in place:

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))
;; => (:FOO "foo" :BAR "bar")
(remf my-plist :foo)
;; => T
my-plist
;; => (:bar "bar")
```

### Adding elements to a plist

To add elements to a plist, you can use `list*` and `append`, which are *not* destructive. They don’t modify the original plist in place.

Using `list*`, we add elements in front:

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))

(list* :baz "baz" my-plist)
;; => (:BAZ "baz" :FOO "foo" :BAR "bar")

my-plist
;; => (:FOO "foo" :BAR "bar")
;;    the original plist was not modified.
```

Using `append`, we add elements to the end:

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))
(append my-plist '(:baz "baz"))
;; => (:FOO "foo" :BAR "bar" :BAZ "baz")

my-plist
;; => (:FOO "foo" :BAR "bar")
;;    the original plist was not modified.
```

Use `(setf my-plist (append …))` if you want to change the plist.

### Setting elements of a plist

You can of course `setf` a place you got with `getf`. In that case, unlike `list*` or `append`, `setf` will update the plist in place:

```lisp
(defparameter my-plist (list :foo "foo" :bar "bar"))
;; => (:FOO "foo" :BAR "bar")

(getf my-plist :foo)
;; => "foo"

(setf (getf my-plist :foo) "foo!!!")
;; => "foo!!!"

my-plist
;; => (:FOO "foo!!!" :BAR "bar")
```


## Structures

Structures offer a way to store data in named slots. They support single inheritance.

Classes provided by the Common Lisp Object System (CLOS) are more flexible however structures may offer better performance (see for example the SBCL manual).

### Creation

Use `defstruct`:

```lisp
(defstruct person
   id name age)
```

At creation slots are optional and default to `nil`.

To set a default value:

```lisp
(defstruct person
   id
   (name "john doe")
   age)
```

Also specify the type after the default value:

```lisp
(defstruct person
  id
  (name "john doe" :type string)
  age)
```

We create an instance with the generated constructor `make-` + `<structure-name>`, so `make-person`:

```lisp
(defparameter *me* (make-person))
*me*
#S(PERSON :ID NIL :NAME "john doe" :AGE NIL)
```

note that printed representations can be read back by the reader.

With a bad name type:

```lisp
(defparameter *bad-name* (make-person :name 123))
```

```
Invalid initialization argument:
  :NAME
in call for class #<STRUCTURE-CLASS PERSON>.
   [Condition of type SB-PCL::INITARG-ERROR]
```

We can set the structure’s constructor so as to create the structure without using keyword arguments, which can be more convenient sometimes. We give it a name and the order of the arguments:

```lisp
(defstruct (person (:constructor create-person (id name age)))
     id
     name
     age)
```

Our new constructor is `create-person`:

```lisp
(create-person 1 "me" 7)
#S(PERSON :ID 1 :NAME "me" :AGE 7)
```

However, the default `make-person` does *not* work any more:

```lisp
(make-person :name "me")
;; debugger:
obsolete structure error for a structure of type PERSON
[Condition of type SB-PCL::OBSOLETE-STRUCTURE]
```

### Slot access

We access the slots with accessors created by `<name-of-the-struct>-` + `slot-name`:

```lisp
(person-name *me*)
;; "john doe"
```

we then also have `person-age` and `person-id`.

### Setting

Slots are `setf`-able:

```lisp
(setf (person-name *me*) "Cookbook author")
(person-name *me*)
;; "Cookbook author"
```

### Predicate

A predicate function is generated:

```lisp
(person-p *me*)
T
```

### Single inheritance

Use single inheritance with the `:include <struct>` argument:

```lisp
(defstruct (female (:include person))
     (gender "female" :type string))
(make-female :name "Lilie")
;; #S(FEMALE :ID NIL :NAME "Lilie" :AGE NIL :GENDER "female")
```

Note that the CLOS object system is more powerful.

### Shorter slot access with symbol-macrolet

If you are accessing several slots within a single function the special form `symbol-macrolet` can improve readibility, by creating symbol macros which expand into forms with structure accessors:

```lisp
(defstruct ship x-position y-position x-velocity y-velocity)

(defun move-ship (ship)
  (symbol-macrolet
      ((x (ship-x-position ship))
       (y (ship-y-position ship))
       (xv (ship-x-velocity ship))
       (yv (ship-y-velocity ship)))
    (psetf x (+ x xv)
           y (+ y yv))
    ship))
```

Here the math involved in the `move-ship` function is easier to read than if accessor functions were used.

Without `symbol-macrolet` it looks like this:

```lisp
(defun move-ship (ship)
  (psetf (ship-x-position ship)
           (+ (ship-x-position ship) (ship-x-velocity ship))
         (ship-y-position ship)
           (+ (ship-y-position ship) (ship-y-velocity ship)))
   ship)
```

In this function all the accessors are not too hard to read, but with more complex operations it would quickly get cluttered.

Now, let’s try our function:

```lisp
(move-ship (make-ship :x-position 1 :y-position 1 :x-velocity 2 :y-velocity 2))
;; #S(SHIP :X-POSITION 3 :Y-POSITION 3 :X-VELOCITY 2 :Y-VELOCITY 2)
```

### Structures and `with-slots`

Though it is not mentioned in the standard, many modern implementations of Common Lisp permit the use of the CLOS macro `with-slots` with structures. In the standard `with-slots` itself is defined using `symbol-macrolet`. At least SBCL and ECL will accept this:

```lisp
(defstruct point x y)

(defvar p (make-point :x 2.3 :y -3.2))

(with-slots (x y) p
  (list x y))

;; => (2.3 -3.2)
```

But do note that in the standard the behavior of the above use of `with-slots` with a structure is called “unspecified.”

### Limitations

After a change, instances are not updated.

If we try to add a slot (`email` below), we have the choice to lose all instances, or to continue using the new definition of `person`. But the effects of redefining a structure are undefined by the standard, so it is best to re-compile and re-run the changed code.

```lisp
(defstruct person
       id
       (name "john doe" :type string)
       age
       email)
```

gives an error and we drop in the debugger:

```
attempt to redefine the STRUCTURE-OBJECT class PERSON
incompatibly with the current definition
   [Condition of type SIMPLE-ERROR]

Restarts:
 0: [CONTINUE] Use the new definition of PERSON, invalidating already-loaded code and instances.
 1: [RECKLESSLY-CONTINUE] Use the new definition of PERSON as if it were compatible, allowing old accessors to use new instances and allowing new accessors to use old instances.
 2: [CLOBBER-IT] (deprecated synonym for RECKLESSLY-CONTINUE)
 3: [RETRY] Retry SLIME REPL evaluation request.
 4: [*ABORT] Return to SLIME's top level.
 5: [ABORT] abort thread (#<THREAD "repl-thread" RUNNING {1002A0FFA3}>)
```

If we choose restart `0`, to use the new definition, we lose access to `*me*`:

```lisp
*me*
obsolete structure error for a structure of type PERSON
   [Condition of type SB-PCL::OBSOLETE-STRUCTURE]
```

There is also very little introspection. Portable Common Lisp does not define ways of finding out defined super/sub-structures nor what slots a structure has.

The Common Lisp Object System (which came after into the language) doesn’t have such limitations. See the CLOS section.

- structures on the hyperspec
- David B. Lamkins, “Successful Lisp, How to Understand and Use Common Lisp”.


## Trees

### Built-ins

A tree can be built with lists of lists.

For example, the nested list `'(A (B) (C (D) (E)))` represents the tree:

```
   A
   ├─ B
   ╰─ C
      ├─ D
      ╰─ E
```

where `(B)`, `(D)` and `(E)` are leaf nodes.

The functions `tree-equal` and `copy-tree` descend recursively into the car and the cdr of the cons cells they visit.

See the functions `subst` and `sublis` above to replace elements in a tree.


## FSet - immutable functional data structures

You may want to have a look at the **FSet** library (in Quicklisp) and its excellent documentation to use immutable data structures.

```
 (ql:quickload "fset")
```

FSet provides the following collections:

- `maps`, aka hash-tables
- `seqs`, aka sequences
- `sets`, aka “unordered collection of values without duplicates”,
- `bags` or multisets, aka sets that count how many occurences of a member is in the bag,
- and more: “replay sets and maps”, “binary relations”, “tuples”, “interval sets” (ranges), “bounded sets”, and similar collections with strict (weak) ordering.

You can start reading its excellent documentation that includes a high level conceptual background, a tutorial, an API reference and a comparison with functional data structures from other ecosystems.

- FSet’s home and issue tracker: https://gitlab.common-lisp.net/fset/fset/


## Sycamore - purely functional weight-balanced binary trees

Another fast, purely functional data structure library for Common Lisp is Sycamore.

It features:

- fast, purely functional **Hash Array Mapped Tries** (HAMT).
- fast, purely functional weight-balanced **binary trees**.
- interfaces for tree **sets** and **maps** (hash-tables).
- ropes
- purely functional pairing **heaps**
- purely functional amortized **queues**.


## Controlling how much of data to print (`*print-length*`, `*print-level*`)

Use `*print-length*` and `*print-level*`.

They are both `nil` by default.

If you have a very big list, printing it on the REPL or in a stacktrace can take a long time and bring your editor or even your server down. Use `*print-length*` to choose the maximum of elements of the list to print, and to show there is a rest with a `...` placeholder:

```lisp
(setf *print-length* 2)
(list :A :B :C :D :E)
;; (:A :B ...)
```

And if you have a very nested data structure, set `*print-level*` to choose the depth to print:

```lisp
(let ((*print-level* 2))
  (print '(:a (:b (:c (:d :e))))))
;; (:A (:B #))             <= *print-level* in action
;; (:A (:B (:C (:D :E))))
;; => the list is returned,
;; the let binding is not in effect anymore.
```

`*print-length*` will be applied at each level.

Reference: the HyperSpec.


## Appendix A - which functions are destructive and which are not?

A destructive function alters the argument(s) it was given. For example, the function `nreverse` is destructive:

```lisp
(defparameter *hello* "hello")

(defun greet (s)
   (print (nreverse s)))

(greet *hello*)
;; => "olleh"

;; What is *hello* now?
(print *hello*)
;; => "olleh"
;;
;; Ooops, the top-level variable was altered by a side-effect and that is not a good practice (at all).
```

How do you know which functions are destructive?

- all `n`something functions are destructive: `nreverse`, `nsubstitute`… “n” means “non-consing”, the function will not allocate any new cons cell (it won’t create new objects in memory), so it might reuse the original sequence, and alter it in place.
  - `nstring-upcase`, `nstring-downcase`, `nstring-capitalize`
  - `nunion`, `nintersection`, `nset-difference`, `nset-exclusive-or`
  - `nbutlast`
  - `nsubst[-if, -if-not]`, `nsublis`, `nsubstitue[-if, -if-not]`
  - each `n`-something function has its non-destructive counterpart, that you should prefer using.
- `sort` and `stable-sort` are destructive functions, so is `merge`, so it’s best practice to use `copy-list` or `copy-seq` before calling one of them.
- the `delete[-*]` functions are destructive (`remove` isn’t destructive)
- `(setf (nth ... ...) ...)` is obviously destructive.
- `replace`, `fill` are destructive
- `vector-push` *can* be destructive
- `remprop`, `remf`
- `map-into`

Also:

- `pop`, `push`: they are not destructive in the sense that they don’t alter conses, but they change the car of the place they pop or push from/to.


## Appendix B - generic and nested access of alists, plists, hash-tables and CLOS slots

The solutions presented below might help you getting started, but keep in mind that they’ll have a performance impact and that error messages will be less explicit.

- the access library (battle tested, used by the Djula templating system) has a generic `(access my-var :elt)` (blog post). It also has `accesses` (plural) to access and set nested values.
- rutils as a generic `generic-elt` or `?`,


## Appendix C - accessing nested data structures

Sometimes we work with nested data structures, and we might want an easier way to access a nested element than intricated “getf” and “assoc” and all. Also, we might want to just be returned a `nil` when an intermediary key doesn’t exist.

The `access` library given above provides this, with `(accesses var key1 key2…)`.


## Appendix D - Collections Type Hierarchy

*Solid nodes are concrete types, while dashed ones are type aliases. For example, `'string` is an alias for an array of characters of any size, `(array character (*))`.*
