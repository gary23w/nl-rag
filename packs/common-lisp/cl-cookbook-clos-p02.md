---
title: "Fundamentals of CLOS (part 2/2)"
source: https://lispcookbook.github.io/cl-cookbook/clos.html
domain: common-lisp
license: CC-BY-SA-4.0
tags: common lisp, hyperspec, clos, sbcl
fetched: 2026-07-02
part: 2/2
---

## MOP

We gather here some examples that make use of the framework provided by the meta-object protocol, the configurable object system that rules Lisp’s object system. We touch advanced concepts so, new reader, don’t worry: you don’t need to understand this section to start using the Common Lisp Object System.

We won’t explain much about the MOP here, but hopefully sufficiently to make you see its possibilities or to help you understand how some CL libraries are built. We invite you to read the books referenced in the introduction.

### Metaclasses

Metaclasses are needed to control the behaviour of other classes.

*As announced, we won’t talk much. See also Wikipedia for metaclasses or CLOS*.

The standard metaclass is `standard-class`:

```lisp
(class-of p1) ;; #<STANDARD-CLASS PERSON>
```

But we’ll change it to one of our own, so that we’ll be able to **count the creation of instances**. This same mechanism could be used to auto increment the primary key of a database system (this is how the Postmodern or Mito libraries do), to log the creation of objects, etc.

Our metaclass inherits from `standard-class`:

```lisp
(defclass counted-class (standard-class)
  ((counter :initform 0)))
#<STANDARD-CLASS COUNTED-CLASS>

(unintern 'person)
;; this is necessary to change the metaclass of person.
;; or (setf (find-class 'person) nil)
;; https://stackoverflow.com/questions/38811931/how-to-change-classs-metaclass#38812140

(defclass person ()
  ((name
    :initarg :name
    :accessor name))
  (:metaclass counted-class)) ;; <- metaclass
;; #<COUNTED-CLASS PERSON>
;;   ^^^ not standard-class anymore.
```

The `:metaclass` class option can appear only once.

Actually you should have gotten a message asking to implement `validate-superclass`. So, still with the `closer-mop` library:

```lisp
(defmethod closer-mop:validate-superclass ((class counted-class)
                                           (superclass standard-class))
  t)
```

Now we can control the creation of new `person` instances:

```lisp
(defmethod make-instance :after ((class counted-class) &key)
  (incf (slot-value class 'counter)))
;; #<STANDARD-METHOD MAKE-INSTANCE :AFTER (COUNTED-CLASS) {1007718473}>
```

See that an `:after` qualifier is the safest choice, we let the standard method run as usual and return a new instance.

The `&key` is necessary, remember that `make-instance` is given initargs.

Now testing:

```lisp
(defvar p3 (make-instance 'person :name "adam"))
#<PERSON {1007A8F5B3}>

(slot-value p3 'counter)
;; => error. No, our new slot isn't on the person class.
(slot-value (find-class 'person) 'counter)
;; 1

(make-instance 'person :name "eve")
;; #<PERSON {1007AD5773}>
(slot-value (find-class 'person) 'counter)
;; 2
```

It’s working.

### Controlling the initialization of instances (initialize-instance)

To further control the creation of object instances, we can specialize the method `initialize-instance`. It is called by `make-instance`, just after a new instance was created but wasn’t initialized yet with the default initargs and initforms.

It is recommended (Keene) to create an after method, since creating a primary method would prevent slots’ initialization.

```lisp
(defmethod initialize-instance :after ((obj person) &key)
;; note the &key in the arglist:                    ^^^^
  (do something with obj))
```

A typical example would be to validate the initial values. Here we’ll check that the person’s name is longer than 3 characters:

```lisp
(defmethod initialize-instance :after ((obj person) &key)
  (with-slots (name) obj
    (assert (>= (length name) 3))))
```

So this call doesn’t work anymore:

```lisp
(make-instance 'person :name "me")
;; The assertion (>= #1=(LENGTH NAME) 3) failed with #1# = 2.
;;   [Condition of type SIMPLE-ERROR]
```

We are prompted into the interactive debugger and we are given a choice of restarts (continue, retry, abort).

So while we’re at it, here’s an assertion that uses the debugger features to offer to change “name”. We give `assert` a list of places that can be changed from the debugger:

```lisp
(defmethod INITIALIZE-INSTANCE :after ((obj person) &key)
  (with-slots (name) obj
    (assert (>= (length name) 3)
            (name)  ;; <-- list of places
            "The value of name is ~a. It should be longer than 3 characters." name)))
```

We get:

```
The value of name is me. It should be longer than 3 characters.
   [Condition of type SIMPLE-ERROR]

Restarts:
 0: [CONTINUE] Retry assertion with new value for NAME.
                               ^^^^^^^^^^^^ our new restart
 1: [RETRY] Retry SLIME REPL evaluation request.
 2: [*ABORT] Return to SLIME's top level.
```

Another rationale. The CLOS implementation of `make-instance` is in two stages: allocate the new object, and then pass it along with all the `make-instance` keyword arguments, to the generic function `initialize-instance`. Implementors and application writers define `:after` methods on `initialize-instance`, to initialize the slots of the instance. The system-supplied primary method does this with regard to (a) `:initform` and `:initarg` values supplied with the class was defined and (b) the keywords passed through from `make-instance`. Other methods can extend this behaviour as they see fit. For example, they might accept an additional keyword which invokes a database access to fill certain slots. The lambda list for `initialize-instance` is:

```
initialize-instance instance &rest initargs &key &allow-other-keys
```

### Controlling the update of instances (update-instance-for-redefined-class)

Suppose you created a “circle” class, with coordinates and a diameter. Later on, you decide to replace the diameter by a radius. You want all the existing objects to be cleverly updated: the radius should have the diameter value, divided by 2. Use `update-instance-for-redefined-class`.

Its parameters are:

- instance: the object instance that is being updated
- added-slots: a list of added slots
- discarded-slots: a list of discarded slots
- property-list: a plist that captured the slot names and values of all the discarded-slots with values in the original instance.
- initargs: an initialization argument list. `&key` catches them below.

and it returns an object.

We actually don’t call the method direcly, but we use a `:before` method:

```lisp
(defmethod update-instance-for-redefined-class
    :before ((obj circle) added deleted plist-values &key)
  (format t "plist values: ~a~&" plist-values)
  (let ((diameter (getf plist-values 'diameter)))
    (setf (radius obj) (/ diameter 2))))
```

Here’s how to try it. Start with a `circle` class:

```lisp
(defclass circle ()
  ((diameter :accessor diameter :initform 9)))
```

and create a circle object:

```lisp
(make-instance 'circle)
```

inspect it or check its diameter value.

Now write and compile a new class definition:

```lisp
(defclass circle ()
  ((radius :accessor radius)))
```

Nothing happens yet, you don’t see the output of our “plist values” print.

Inspect or `describe` the object: now it will be updated, and you’ll find the `radius` slot.

Existing objects are updated lazily.

See more on the HyperSpec or on the Community Spec.

### Controlling the update of instances to new classes (update-instance-for-different-class)

Now imagine you are working with the `circle` class, but you realize you only need a `surface` kind of objects. You will discard the circle class altogether, but you want your existing objects to be updated -to this new class, and compute new slots intelligently. Use `update-instance-for-different-class`.

See more on the HyperSpec or on the Community Spec.

### Finding methods matching qualifiers and types

You want to check if a method exists with a given set of *qualifiers* (such as the `:around` method) and, most importantly, *specializers* (the type(s) the method dispatches on.

For example, in this chapter we specialized the `print-object` method for a `person` object:

```lisp
(defmethod print-object ((obj person) stream)
```

Now, in our program that uses some introspection, we want to see if such a function exists, and get a reference to it.

Use `find-method`:

```lisp
(find-method #'print-object nil '(person t))
;;          ^^^ a function object, not only a symbol
;; => <STANDARD-METHOD COMMON-LISP:PRINT-OBJECT (PERSON T) {1204FA0B83}>
```

The first argument, `nil`, is a list of qualifiers. We are not interested in the `:around`, `:before` or `:after` methods, so we keep it `nil`. We could use `'(:around)`, as a list.

The second argument is a list of the method’s arguments’ types. `print-object` takes 2 arguments, a person and a stream. We can use `'(t t)` to get a reference to the generic function. We use `'(person t)` to get a reference to the method that specializes on a person, and on any stream.

If no such method exists, `find-method` signals an error:

```
There is no method on
#<STANDARD-GENERIC-FUNCTION COMMON-LISP::PRINT-OBJECT (1)> with no
qualifiers and specializers
(… …)
condition of type simple-error
```

unless you set its last optional argument `errorp` to `nil`.

### Final words

See (much) more in the books!

Page source: clos.md
