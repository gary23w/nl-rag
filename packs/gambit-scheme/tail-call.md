---
title: "Tail call"
source: https://en.wikipedia.org/wiki/Tail_call
domain: gambit-scheme
license: CC-BY-SA-4.0
tags: gambit scheme, scheme language, continuation control, tail call, self hosting compilers
fetched: 2026-07-02
---

# Tail call

In computer science, a **tail call** is a subroutine call performed as the final action of a procedure. If the target of a tail is the same subroutine, the subroutine is said to be **tail recursive**, which is a special case of direct recursion. **Tail recursion** (or **tail-end recursion**) is particularly useful, and is often easy to optimize in implementations.

Tail calls can be implemented without adding a new stack frame to the call stack. Most of the frame of the current procedure is no longer needed, and can be replaced by the frame of the tail call, modified as appropriate (similar to overlay for processes, but for function calls). The program can then jump to the called subroutine. Producing such code instead of a standard call sequence is called **tail-call elimination** or **tail-call optimization**. Tail-call elimination allows procedure calls in tail position to be implemented as efficiently as goto statements, thus allowing efficient structured programming. In the words of Guy L. Steele, "in general, procedure calls may be usefully thought of as GOTO statements which also pass parameters, and can be uniformly coded as [machine code] JUMP instructions."

Not all programming languages require tail-call elimination. However, in functional programming languages, tail-call elimination is often guaranteed by the language standard, allowing tail recursion to use a similar amount of memory as an equivalent loop. The special case of tail-recursive calls, when a function calls itself, may be more amenable to call elimination than general tail calls. When the language semantics do not explicitly support general tail calls, a compiler can often still optimize **sibling calls**, or tail calls to functions which take and return the same types as the caller.

## Description

When a function is called, the computer must "remember" the place it was called from, the *return address*, so that it can return to that location with the result once the call is complete. Typically, this information is saved on the call stack, a list of return locations in the order that the call locations were reached. In addition, compilers allocate memory for local variables of the called function and push register content (if any and/or relevant) onto the stack. Typically, it is done by allocating a stack frame including saved registers, space allocated for non-register local variables, return address and call parameters (unless they are passed in registers). For tail calls, there is no need to remember the caller or preserve content of registers – instead, tail-call elimination avoids allocation of new stack frames and makes only the minimum necessary changes to the existing stack frame before passing it on, and the tail-called function will return directly to the *original* caller. This, however, leads to complete loss of the caller's stack frame, which is sometimes considered as a hindrance in debugging. The tail call doesn't have to appear lexically after all other statements in the source code; it is only important that the calling function return immediately after the tail call, returning the tail call's result if any, since the calling function is bypassed when the optimization is performed.

For non-recursive function calls, this is usually an optimization that saves only a little time and space, since there are not that many different functions available to call. When dealing with recursive or mutually recursive functions where recursion happens through tail calls, however, the stack space and the number of returns saved can grow to be very significant, since a function can call itself, directly or indirectly, creating a new call stack frame each time. Tail-call elimination often reduces asymptotic stack space requirements from linear, or O(n), to constant, or O(1). Tail-call elimination is thus required by the standard definitions of some programming languages, such as Scheme, and languages in the ML family among others. The Scheme language definition formalizes the intuitive notion of tail position exactly, by specifying which syntactic forms allow having results in tail context. Implementations allowing an unlimited number of tail calls to be active at the same moment, thanks to tail-call elimination, can also be called 'properly tail recursive'.

Besides space and execution efficiency, tail-call elimination is important in the functional programming idiom known as continuation-passing style (CPS), which would otherwise quickly run out of stack space.

## Syntactic form

A tail call can be located just before the syntactical end of a function.

```mw
int a(int n);
int b(int n);

int foo(int data) {
    a(data);
    return b(data);
}
```

Here, both `a(data)` and `b(data)` are calls, but `b` is the last thing the procedure executes before returning and is thus in tail position. However, not all tail calls are necessarily located at the syntactical end of a subroutine:

```mw
int c(int n);

int bar(int data) {
    if (a(data) > 0) {
        return b(data);
    }
    return c(data);
}
```

Here, both calls to `b` and `c` are in tail position. This is because each of them lies in the end of if-branch respectively, even though the first one is not syntactically at the end of `bar`'s body.

Consider this example:

```mw
int foo1(int data) {
    return a(data) + 1;
}

int foo2(int data) {
    int ret = a(data);
    return ret;
}

int foo3(int data) {
    int ret = a(data);
    return (ret == 0) ? 1 : ret;
}
```

The call to `a(data)` is in tail position in `foo2`, but it is **not** in tail position either in `foo1` or in `foo3`, because control must return to the caller to allow it to inspect or modify the return value before returning it.

## Example programs

The following program is an example in Scheme:

```mw
;; factorial : number -> number
;; to calculate the product of all positive
;; integers less than or equal to n.
(define (factorial n)
 (if (= n 0)
    1
    (* n (factorial (- n 1)))))
```

This is not written in a tail-recursive style, because the multiplication function ("*") is in the tail position. This can be compared to:

```mw
;; factorial : number -> number
;; to calculate the product of all positive
;; integers less than or equal to n.
(define (factorial n)
  (fact-iter 1 n))
(define (fact-iter product n)
  (if (= n 0)
      product
      (fact-iter (* product n)
                 (- n 1))))
```

This program assumes applicative-order evaluation. The inner procedure `fact-iter` calls itself *last* in the control flow. This allows an interpreter or compiler to reorganize the execution which would ordinarily look like this:

```
  call factorial (4)
   call fact-iter (1 4)
    call fact-iter (4 3)
     call fact-iter (12 2)
      call fact-iter (24 1)
      return 24
     return 24
    return 24
   return 24
  return 24
```

into the more efficient variant, in terms of both space and time:

```
  call factorial (4)
   call fact-iter (1 4)
   replace arguments with (4 3)
   replace arguments with (12 2)
   replace arguments with (24 1)
   return 24
  return 24
```

This reorganization saves space because no state except for the calling function's address needs to be saved, either on the stack or on the heap, and the call stack frame for `fact-iter` is reused for the intermediate results storage. This also means that the programmer need not worry about running out of stack or heap space for extremely deep recursions. In typical implementations, the tail-recursive variant will be substantially faster than the other variant, but only by a constant factor.

Some programmers working in functional languages will rewrite recursive code to be tail recursive so they can take advantage of this feature. This often requires addition of an "accumulator" argument (`product` in the above example) to the function.

## Tail recursion modulo cons

**Tail recursion modulo cons** is a generalization of tail-recursion optimization introduced by David H. D. Warren in the context of compilation of Prolog, seen as an *explicitly* *set once* language. It was described (though not named) by Daniel P. Friedman and David S. Wise in 1974 as a LISP compilation technique. As the name suggests, it applies when the only operation left to perform after a recursive call is to prepend a known value in front of the list returned from it (or to perform a constant number of simple data-constructing operations, in general). This call would thus be a *tail call* save for ("modulo") the said *cons* operation. But prefixing a value at the start of a list *on exit* from a recursive call is the same as appending this value at the end of the growing list *on entry* into the recursive call, thus building the list as a side effect, as if in an implicit accumulator parameter. The following Prolog fragment illustrates the concept:

### Example code

| % Prolog, tail recursive modulo cons: partition([], _, [], []). partition([X\|Xs], Pivot, [X\|Rest], Bigs) :- X @< Pivot, !, partition(Xs, Pivot, Rest, Bigs). partition([X\|Xs], Pivot, Smalls, [X\|Rest]) :- partition(Xs, Pivot, Smalls, Rest). | -- In Haskell, guarded recursion: partition [] _ = ([],[]) partition (x:xs) p \| x < p = (x:a,b) \| otherwise = (a,x:b) where (a,b) = partition xs p |
|---|---|
| % Prolog, with explicit unifications: % non-tail recursive translation: partition([], _, [], []). partition(L, Pivot, Smalls, Bigs) :- L=[X\|Xs], ( X @< Pivot -> partition(Xs,Pivot,Rest,Bigs), Smalls=[X\|Rest] ; partition(Xs,Pivot,Smalls,Rest), Bigs=[X\|Rest] ). | % Prolog, with explicit unifications: % tail-recursive translation: partition([], _, [], []). partition(L, Pivot, Smalls, Bigs) :- L=[X\|Xs], ( X @< Pivot -> Smalls=[X\|Rest], partition(Xs,Pivot,Rest,Bigs) ; Bigs=[X\|Rest], partition(Xs,Pivot,Smalls,Rest) ). |

Thus in tail-recursive translation such a call is transformed into first creating a new list node and setting its `first` field, and *then* making the tail call with the pointer to the node's `rest` field as argument, to be filled recursively. The same effect is achieved when the recursion is *guarded* under a lazily evaluated data constructor, which is automatically achieved in lazy programming languages like Haskell.

### C example

The following fragment defines a recursive function in C that duplicates a linked list (with some equivalent Scheme and Prolog code as comments, for comparison):

| typedef struct LinkedList { void* value; struct LinkedList* next; } LinkedList; LinkedList* duplicate(const LinkedList* ls) { LinkedList* head = NULL; if (ls) { LinkedList* p = duplicate(ls->next); head = (LinkedList*)malloc(sizeof(*head)); head->value = ls->value; head->next = p; } return head; } | ;; in Scheme, (define (duplicate ls) (if (not (null? ls)) (cons (car ls) (duplicate (cdr ls))) '())) |
|---|---|
| %% in Prolog, duplicate([X\|Xs],R):- duplicate(Xs,Ys), R=[X\|Ys]. duplicate([],[]). |   |

In this form the function is not tail recursive, because control returns to the caller after the recursive call duplicates the rest of the input list. Even if it were to allocate the *head* node before duplicating the rest, it would still need to plug in the result of the recursive call into the `next` field *after* the call. So the function is *almost* tail recursive. Warren's method pushes the responsibility of filling the `next` field into the recursive call itself, which thus becomes tail call. Using sentinel head node to simplify the code,

| void duplicate_aux(const LinkedList* ls, LinkedList* end) { if (ls) { end->next = (LinkedList*)malloc(sizeof(*end)); end->next->value = ls->value; duplicate_aux(ls->next, end->next); } else { end->next = NULL; } } LinkedList* duplicate(const LinkedList* ls) { LinkedList head; duplicate_aux(ls, &head); return head.next; } | ;; in Scheme, (define (duplicate ls) (let ((head (list 1))) (let dup ((ls ls) (end head)) (cond ((not (null? ls)) (set-cdr! end (list (car ls))) (dup (cdr ls) (cdr end))))) (cdr head))) |
|---|---|
| %% in Prolog, duplicate([X\|Xs],R):- R=[X\|Ys], duplicate(Xs,Ys). duplicate([],[]). |   |

The callee now appends to the end of the growing list, rather than have the caller prepend to the beginning of the returned list. The work is now done on the way *forward* from the list's start, *before* the recursive call which then proceeds further, instead of *backward* from the list's end, *after* the recursive call has returned its result. It is thus similar to the accumulating parameter technique, turning a recursive computation into an iterative one.

Characteristically for this technique, a parent frame is created on the execution call stack, which the tail-recursive callee can reuse as its own call frame if the tail-call optimization is present.

The tail-recursive implementation can now be converted into an explicitly iterative implementation, as an accumulating loop:

| LinkedList* duplicate(const LinkedList* ls) { LinkedList head; LinkedList* end; end = &head; while (ls) { end->next = (LinkedList*)malloc(sizeof(*end)); end->next->value = ls->value; ls = ls->next; end = end->next; } end->next = NULL; return head.next; } | ;; in Scheme, (define (duplicate ls) (let ((head (list 1))) (do ((end head (cdr end)) (ls ls (cdr ls ))) ((null? ls) (cdr head)) (set-cdr! end (list (car ls)))))) |
|---|---|
| %% in Prolog, %% N/A |   |

## History

In a paper delivered to the ACM conference in Seattle in 1977, Guy L. Steele summarized the debate over the GOTO and structured programming, and observed that procedure calls in the tail position of a procedure can be best treated as a direct transfer of control to the called procedure, typically eliminating unnecessary stack manipulation operations. Since such "tail calls" are very common in Lisp, a language where procedure calls are ubiquitous, this form of optimization considerably reduces the cost of a procedure call compared to other implementations. Steele argued that poorly-implemented procedure calls had led to an artificial perception that the GOTO was cheap compared to the procedure call. Steele further argued that "in general procedure calls may be usefully thought of as GOTO statements which also pass parameters, and can be uniformly coded as [machine code] JUMP instructions", with the machine code stack manipulation instructions "considered an optimization (rather than vice versa!)". Steele cited evidence that well-optimized numerical algorithms in Lisp could execute faster than code produced by then-available commercial Fortran compilers because the cost of a procedure call in Lisp was much lower. In Scheme, a Lisp dialect developed by Steele with Gerald Jay Sussman, tail-call elimination is guaranteed to be implemented in any interpreter.

## Implementation methods

Tail recursion is important to some high-level languages, especially functional and logic languages and members of the Lisp family. In these languages, tail recursion is the most commonly used way (and sometimes the only way available) of implementing iteration. The language specification of Scheme requires that tail calls are to be optimized so as not to grow the stack. Tail calls can be made explicitly in Perl, with a variant of the "goto" statement that takes a function name: `goto &NAME;`

However, for language implementations which store function arguments and local variables on a call stack (which is the default implementation for many languages, at least on systems with a hardware stack, such as the x86), implementing generalized tail-call optimization (including mutual tail recursion) presents an issue: if the size of the callee's activation record is different from that of the caller, then additional cleanup or resizing of the stack frame may be required. For these cases, optimizing tail recursion remains trivial, but general tail-call optimization may be harder to implement efficiently.

For example, in the Java virtual machine (JVM), tail-recursive calls can be eliminated (as this reuses the existing call stack), but general tail calls cannot be (as this changes the call stack). As a result, functional languages such as Scala that target the JVM can efficiently implement direct tail recursion, but not mutual tail recursion.

The GCC, LLVM/Clang, and Intel compiler suites perform tail-call optimization for C and other languages at higher optimization levels or when the `-foptimize-sibling-calls` option is passed. Though the given language syntax may not explicitly support it, the compiler can make this optimization whenever it can determine that the return types for the caller and callee are equivalent, and that the argument types passed to both function are either the same, or require the same amount of total storage space on the call stack.

Various implementation methods are available.

### In assembly

Tail calls are often optimized by interpreters and compilers of functional programming and logic programming languages to more efficient forms of iteration. For example, Scheme programmers commonly express while loops as calls to procedures in tail position and rely on the Scheme compiler or interpreter to substitute the tail calls with more efficient jump instructions.

For compilers generating assembly directly, tail-call elimination is easy: it suffices to replace a call opcode with a jump one, after fixing parameters on the stack. From a compiler's perspective, the first example above is initially translated into pseudo-assembly language (in fact, this is valid x86 assembly):

```mw
 foo:
  call B
  call A
  ret
```

Tail-call elimination replaces the last two lines with a single jump instruction:

```mw
 foo:
  call B
  jmp  A
```

After subroutine `A` completes, it will then return directly to the return address of `foo`, omitting the unnecessary `ret` statement.

Typically, the subroutines being called need to be supplied with parameters. The generated code thus needs to make sure that the call frame for A is properly set up before jumping to the tail-called subroutine. For instance, on platforms where the call stack does not just contain the return address, but also the parameters for the subroutine, the compiler may need to emit instructions to adjust the call stack. On such a platform, for the code:

```
function foo(data1, data2)
   B(data1)
   return A(data2)
```

(where `data1` and `data2` are parameters) a compiler might translate that as:

```mw
 foo:
   mov  reg,[sp+data1] ; fetch data1 from stack (sp) parameter into a scratch register.
   push reg            ; put data1 on stack where B expects it
   call B              ; B uses data1
   pop                 ; remove data1 from stack
   mov  reg,[sp+data2] ; fetch data2 from stack (sp) parameter into a scratch register.
   push reg            ; put data2 on stack where A expects it
   call A              ; A uses data2
   pop                 ; remove data2 from stack.
   ret
```

A tail-call optimizer could then change the code to:

```mw
 foo:
   mov  reg,[sp+data1] ; fetch data1 from stack (sp) parameter into a scratch register.
   push reg            ; put data1 on stack where B expects it
   call B              ; B uses data1
   pop                 ; remove data1 from stack
   mov  reg,[sp+data2] ; fetch data2 from stack (sp) parameter into a scratch register.
   mov  [sp+data1],reg ; put data2 where A expects it
   jmp  A              ; A uses data2 and returns immediately to caller.
```

This code is more efficient both in terms of execution speed and use of stack space.

From a compiler's perspective, a pure tail call is most visible in recursive functions. Consider a pseudo-assembly example where a function calls itself as its final action to process data, taking a single parameter:

```mw
function foo(data)
   if (data == 0) return data
   return foo(data - 1)
```

An unoptimized compiler translates this into a standard call sequence, pushing a new frame to the stack for every recursion:

```mw
 foo:
   mov  reg,[sp+data] ; fetch data from stack parameter
   cmp  reg, 0        ; base case check
   je   end
   dec  reg           ; modify data
   push reg           ; push new data onto stack for next call
   call foo           ; recursive call (GROWS THE STACK)
   pop                ; clean up stack after return
 end:
   ret
```

A tail-call optimizer recognizes that the current stack frame is no longer needed after the call. It changes the code to destructively update the argument in place and jump, bounding the stack strictly to *O*(1) space:

```mw
 foo:
   mov  reg,[sp+data] ; fetch data from stack parameter
   cmp  reg, 0        ; base case check
   je   end
   dec  reg           ; modify data
   mov  [sp+data],reg ; destructively update the existing stack parameter
   jmp  foo           ; jump directly back to start (STACK REMAINS BOUNDED)
 end:
   ret
```

This optimized code is physically identical to an imperative `while` loop, executing with strictly bounded memory and maximal speed.

### Hardware and space complexity

In bare-metal environments and formal automata theory, a pure tail call is defined primarily by its space complexity: **a pure tail call occurs when the stack space is strictly bounded during recursion**. By guaranteeing that the stack pointer does not grow proportionally to the recursion depth, tail calls allow infinitely deep recursive evaluation to operate within strict physical memory constraints (such as a microkernel or a boot sector). This physically transforms the call stack into a bounded state machine.

### Relationship to coroutines

A tail call without recursion is physically equivalent to an assembly `JMP` instruction. This property makes the tail call a fundamental primitive for implementing high-performance coroutines. By replacing the traditional `CALL` and `RET` cycle with a direct jump to the next state, an execution engine can "hand off" control between different functional units in constant stack space. This mechanism is central to Continuation-passing style, where the program never returns, but instead performs a sequence of tail calls to transition between cooperative states.

### Through trampolining

Since many Scheme compilers use C as an intermediate target code, the tail recursion must be encoded in C without growing the stack, even if the C compiler does not optimize tail calls. Many implementations achieve this by using a device known as a trampoline, a piece of code that repeatedly calls functions. All functions are entered via the trampoline. When a function has to tail-call another, instead of calling it directly and then returning the result, it returns the address of the function to be called and the call parameters back to the trampoline (from which it was called itself), and the trampoline takes care of calling this function next with the specified parameters. This ensures that the C stack does not grow and iteration can continue indefinitely.

It is possible to implement trampolines using higher-order functions in languages that support them, such as Groovy, Visual Basic .NET and C#.

Using a trampoline for all function calls is rather more expensive than the normal C function call, so at least one Scheme compiler, Chicken, uses a technique first described by Henry Baker from an unpublished suggestion by Andrew Appel, in which normal C calls are used but the stack size is checked before every call. When the stack reaches its maximum permitted size, objects on the stack are garbage-collected using the Cheney algorithm by moving all live data into a separate heap. Following this, the stack is unwound ("popped") and the program resumes from the state saved just before the garbage collection. Baker says "Appel's method avoids making a large number of small trampoline bounces by occasionally jumping off the Empire State Building." The garbage collection ensures that mutual tail recursion can continue indefinitely. However, this approach requires that no C function call ever returns, since there is no guarantee that its caller's stack frame still exists; therefore, it involves a much more dramatic internal rewriting of the program code: continuation-passing style.

## Relation to the `while` statement

Tail recursion can be related to the while statement, an explicit iteration, for instance by transforming

```
procedure foo(x)
    if p(x)
        return bar(x)
    else
        return foo(baz(x))
```

into

```
procedure foo(x)
    while true
        if p(x)
            return bar(x)
        else
            x ← baz(x)
```

where *x* may be a tuple involving more than one variable: if so, care must be taken in implementing the assignment statement *x* ← baz(*x*) so that dependencies are respected. One may need to introduce auxiliary variables or use a *swap* construct.

More generally,

```
procedure foo(x)
    if p(x)
        return bar(x)
    else if q(x)
        return baz(x)
    ...
    else if r(x)
        return foo(qux(x))
    ...
    else
        return foo(quux(x))
```

can be transformed into

```
procedure foo(x)
    while true
        if p(x)
            return bar(x)
        else if q(x)
            return baz(x)
        ...
        else if r(x)
            x ← qux(x)
        ...
        else
            x ← quux(x)
```

For instance, this Julia program gives a non-tail recursive definition `factorial` of the factorial:

```mw
function factorial(n::Integer)::Integer
    if n == 0
        return 1
    else
        return n * factorial(n - 1)
    end
end
```

Indeed, `n * factorial(n - 1)` wraps the call to `factorial`. But it can be transformed into a tail-recursive definition by adding an argument `a` called an *accumulator*.

This Julia program gives a tail-recursive definition `factorial` of the factorial:

```mw
function factorial(n::Integer, a::Integer)::Integer
    if n == 0:
        return a
    else
        return factorial(n - 1, n * a)
    end
end

function factorial(n::Integer)::Integer
    return factorial(n, 1)
end
```

This Julia program gives an iterative definition `fact_iter` of the factorial:

```mw
function fact_iter(n::Integer, a::Integer)::Integer
    while n > 0
        a = n * a
        n = n - 1
    end
    return a
end

function factorial(n::Integer)::Integer
    return fact_iter(n, one(n))
end
```

## Language support

- Clojure – Clojure has `recur` special form.
- Common Lisp – Some implementations perform tail-call optimization during compilation if optimizing for speed
- Elixir – Elixir implements tail-call optimization, as do all languages currently targeting the BEAM VM.
- Elm – Yes
- Erlang – Yes
- F# – F# implements TCO by default where possible
- Go – No support
- Haskell – Yes
- JavaScript – ECMAScript 6.0 compliant engines should have tail calls which is now implemented on Safari/WebKit but rejected by V8 and SpiderMonkey
- Kotlin – Has `tailrec` modifier for functions
- Lua – Tail recursion is required by the language definition
- Objective-C – Compiler optimizes tail calls when -O1 (or higher) option specified, but it is easily disturbed by calls added by Automatic Reference Counting.
- OCaml – Yes. Since version 4.03.0, the built-in `tailcall` attribute can be used to verify that a call will be optimized, emitting a warning otherwise.
- Perl – Explicit with a variant of the "goto" statement that takes a function name: `goto &NAME;`
- Prolog – SWI-Prolog implements tail-recursion optimization.
- PureScript – Yes
- Python – Stock Python implementations do not perform tail-call optimization, though a third-party module is available to do this. Language inventor Guido van Rossum contended that stack traces are altered by tail-call elimination making debugging harder, and preferred that programmers use explicit iteration instead. In Python 3.14, a new interpreter was introduced that uses tail-call based dispatch of Python opcodes. This resulted in overall improved performance when compared to Python 3.13.
- R – Yes, `tailcall()` function introduced in R.4.4.0
- Racket – Yes
- Ruby – Yes, but disabled by default
- Rust – tail-call optimization may be done in limited circumstances, but is not guaranteed
- Scala – Tail-recursive functions are automatically optimized by the compiler. Such functions can also optionally be marked with a `@tailrec` annotation, which makes it a compilation error if the function is not tail recursive
- Scheme – Required by the language definition
- Swift – In some cases.
- Tcl – Since Tcl 8.6, Tcl has a `tailcall` command
- Zig – Yes
