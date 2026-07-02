---
title: "Delimited continuation"
source: https://en.wikipedia.org/wiki/Delimited_continuation
domain: algebraic-effects
license: CC-BY-SA-4.0
tags: algebraic effect, effect handler, delimited continuation, one-shot continuation
fetched: 2026-07-02
---

# Delimited continuation

In programming languages, a **delimited continuation**, **composable continuation** or **partial continuation**, is a "slice" of a continuation frame that has been reified into a function. Unlike regular continuations, delimited continuations return a value, and thus may be reused and composed. Control delimiters, the basis of delimited continuations, were introduced by Matthias Felleisen in 1988 though early allusions to composable and delimited continuations can be found in Carolyn Talcott's Stanford 1984 dissertation, Felleisen *et al.*, Felleisen's 1987 dissertation, and algorithms for functional backtracking, e.g., for pattern matching, for parsing, in the Algebraic Logic Functional programming language, and in the functional implementations of Prolog where the failure continuation is often kept implicit and the reason of being for the success continuation is that it is composable.

## History

Delimited continuations were first introduced by Felleisen in 1988 with an operator called ${\mathcal {F}}$ , first introduced in a tech report in 1987, along with a prompt construct $\#$ . The operator was designed to be a generalization of control operators that had been described in the literature such as `call/cc` from Scheme, ISWIM's J operator, John C. Reynolds' `escape` operator, and others. Subsequently, many competing delimited control operators were invented by the programming languages research community such as `prompt` and `control`, `shift` and `reset`,`cupto`, `fcontrol`, and others.

## Examples

Various operators for delimited continuations have been proposed in the research literature.

One independent proposal is based on continuation-passing style (CPS)—i.e., not on continuation frames—and offers two control operators, `shift` and `reset`, that give rise to static rather than to dynamic delimited continuations. The `reset` operator sets the limit for the continuation while the `shift` operator captures or reifies the current continuation up to the innermost enclosing `reset`. For example, consider the following snippet in Scheme:

```mw
(* 2 (reset (+ 1 (shift k (k 5)))))
```

The `reset` delimits the continuation that `shift` captures (named by `k` in this example). When this snippet is executed, the use of `shift` will bind `k` to the continuation `(+ 1 [])` where `[]` represents the part of the computation that is to be filled with a value. This continuation directly corresponds to the code that surrounds the `shift` up to the `reset`. Because the body of shift (i.e., `(k 5)`) immediately invokes the continuation, this code is equivalent to the following:

```mw
(* 2 (+ 1 5))
```

In general, these operators can encode more interesting behavior by, for example, returning the captured continuation `k` as a value or invoking `k` multiple times. The `shift` operator passes the captured continuation `k` to the code in its body, which can either invoke it, produce it as a result, or ignore it entirely. Whatever result that `shift` produces is provided to the innermost `reset`, discarding the continuation in between the `reset` and `shift`. However, if the continuation is invoked, then it effectively re-installs the continuation after returning to the `reset`. When the entire computation within `reset` is completed, the result is returned by the delimited continuation. For example, in this Scheme code:

```mw
 (reset (* 2 (shift k CODE)))
```

whenever `CODE` invokes `(k N)`, `(* 2 N)` is evaluated and returned.

This is equivalent to the following:

```mw
  (let ((k (lambda (x) (* 2 x)))) CODE)
```

Furthermore, once the entire computation within `shift` is completed, the continuation is discarded, and execution restarts outside `reset`. Therefore,

```mw
 (reset (* 2 (shift k (k (k 4)))))
```

invokes `(k 4)` first (which returns 8), and then `(k 8)` (which returns 16). At this point, the `shift` expression has terminated, and the rest of the `reset` expression is discarded. Therefore, the final result is 16.

Everything that happens outside the `reset` expression is hidden, i.e. not influenced by the control transfer. For example, this returns 17:

```mw
 (+ 1 (reset (* 2 (shift k (k (k 4))))))
```

Delimited continuations were first described independently by Felleisen *et al.* and Johnson. They have since been used in a large number of domains, particularly in defining new control operators; see Queinnec for a survey.

Let's take a look at a more complicated example. Let `null` be the empty list:

```mw
 (reset
   (begin
     (shift k (cons 1 (k (void)))) ;; (1)
     null))
```

The context captured by `shift` is `(begin [*] null)`, where `[*]` is the hole where `k`'s parameter will be injected. The first call of `k` inside `shift` evaluates to this context with `(void)` = `#<void>` replacing the hole, so the value of `(k (void))` is `(begin #<void> null)` = `null`. The body of `shift`, namely `(cons 1 null)` = `(1)`, becomes the overall value of the `reset` expression as the final result.

Making this example more complicated, add a line:

```mw
 (reset
   (begin
     (shift k (cons 1 (k (void))))
     (shift k (cons 2 (k (void))))
     null))
```

If we comment out the first `shift`, we already know the result, it is `(2)`; so we can as well rewrite the expression like this:

```mw
 (reset
   (begin
     (shift k (cons 1 (k (void))))
     (list 2)))
```

This is pretty familiar, and can be rewritten as `(cons 1 (list 2))`, that is, `(list 1 2)`.

We can define `yield` using this trick:

```
(define (yield x) (shift k (cons x (k (void)))))
```

and use it in building lists:

```mw
 (reset (begin
          (yield 1)
          (yield 2)
          (yield 3)
          null))    ;; (list 1 2 3)
```

If we replace `cons` with `stream-cons`, we can build lazy streams:

```mw
  (define (stream-yield x) (shift k (stream-cons x (k (void)))))

  (define lazy-example
    (reset (begin
            (stream-yield 1)
            (stream-yield 2)
            (stream-yield 3)
            stream-null)))
```

We can generalize this and convert lists to stream, in one fell swoop:

```mw
 (define (list->stream xs)
   (reset (begin
            (for-each stream-yield xs)
            stream-null)))
```

In a more complicated example below the continuation can be safely wrapped into a body of a lambda, and be used as such:

```mw
 (define (for-each->stream-maker for-each) 
   (lambda (collection) 
     (reset (begin 
              (for-each (lambda (element) 
                          (shift k 
                            (stream-cons element (k 'ignored)))) 
                        collection) 
              stream-null))))
```

The part between `reset` and `shift` includes control functions like `lambda` and `for-each`; this is impossible to rephrase using lambdas.

Delimited continuations are also useful in linguistics: see Continuations in linguistics for details.

## A worked-out illustration of the `(shift k k)` idiom: the generalized curry function

The generalized curry function is given an uncurried function `f` and its arity (say, 3), and it returns the value of `(lambda (v1) (lambda (v2) (lambda (v3) (f v1 v2 v3))))`. This example is due to Olivier Danvy and was worked out in the mid-1980s.

Here is a unit-test function to illustrate what the generalized curry function is expected to do:

```mw
(define test-curry
  (lambda (candidate)
    (and (= (candidate + 0)
            (+))
         (= ((candidate + 1) 1)
            (+ 1))
         (= (((candidate + 2) 1) 10)
            (+ 1 10))
         (= ((((candidate + 3) 1) 10) 100)
            (+ 1 10 100)))
         (= (((((candidate + 4) 1) 10) 100) 1000)
            (+ 1 10 100 1000))))
```

These unit tests verify whether currying the variadic function `+` into an n-ary curried function and applying the result to n arguments yields the same result as applying `+` to these n arguments, for n = 0, 1, 2, 3, and 4.

The following recursive function is accumulator-based and eventually reverses the accumulator before applying the given uncurried function. In each instance of the induction step, the function `(lambda (v) ...)` is explicitly applied to an argument in the curried application:

```mw
(define curry_a
  (lambda (f n)
    (if (< n 0)
        (error 'curry_a "negative input: ~s" n)
        (letrec ([visit (lambda (i a)
                          (if (= i 0)
                              (apply f (reverse a))
                              (lambda (v)
                                (visit (- i 1) (cons v a)))))])
          (visit n '())))))
```

For example, evaluating

```mw
(((curry_a + 2) 1) 10)
```

reduces to evaluating

```mw
(((visit 2 '()) 1) 10)
```

which reduces to evaluating

```mw
(((lambda (v) (visit 1 (cons v '()))) 1) 10)
```

which beta-reduces to evaluating

```mw
((visit 1 (cons 1 '())) 10)
```

which reduces to evaluating

```mw
((lambda (v) (visit 0 (cons v (cons 1 '())))) 10)
```

which beta-reduces to evaluating

```mw
(visit 0 (cons 10 (cons 1 '())))
```

which reduces to evaluating

```mw
(apply + (reverse (cons 10 (cons 1 '()))))
```

which reduces to evaluating

```mw
(apply + (cons 1 (cons 10 '())))
```

which is equivalent to

```mw
(+ 1 10)
```

which delta-reduces to the result, `11`.

The following recursive function is continuation-based and involves no list reversal. Likewise, in each instance of the induction step, the function `(lambda (v) ...)` is explicitly applied to an argument in the curried application:

```mw
(define curry_c
  (lambda (f n)
    (if (< n 0)
        (error 'curry_c "negative input: ~s" n)
        (letrec ([visit (lambda (i c)
                          (if (= i 0)
                              (c '())
                              (lambda (v)
                                (visit (- i 1) (lambda (vs)
                                                 (c (cons v vs)))))))])
          (visit n (lambda (vs)
                     (apply f vs)))))))
```

So evaluating

```mw
(((curry_c + 2) 1) 10)
```

reduces to evaluating

```mw
(((visit 2 (lambda (vs) (apply + vs))) 1) 10)
```

which reduces to evaluating

```mw
(((lambda (v) (visit 1 (lambda (vs) ((lambda (vs) (apply + vs)) (cons v vs))))) 1) 10)
```

which beta-reduces to evaluating

```mw
((visit 1 (lambda (vs) ((lambda (vs) (apply + vs)) (cons 1 vs)))) 10)
```

which reduces to evaluating

```mw
((lambda (v) (visit 0 (lambda (vs) ((lambda (vs) ((lambda (vs) (apply + vs)) (cons 1 vs))) (cons v vs))))) 10)
```

which beta-reduces to evaluating

```mw
(visit 0 (lambda (vs) ((lambda (vs) ((lambda (vs) (apply + vs)) (cons 1 vs))) (cons 10 vs))))
```

which reduces to evaluating

```mw
((lambda (vs) ((lambda (vs) ((lambda (vs) (apply + vs)) (cons 1 vs))) (cons 10 vs))) '())
```

which beta-reduces to evaluating

```mw
((lambda (vs) ((lambda (vs) (apply + vs)) (cons 1 vs))) (cons 10 '()))
```

which beta-reduces to evaluating

```mw
((lambda (vs) (apply + vs)) (cons 1 (cons 10 '())))
```

which beta-reduces to evaluating

```mw
(apply + (cons 1 (cons 10 '())))
```

which is equivalent to

```mw
(+ 1 10)
```

which delta-reduces to the result, `11`.

The following recursive function, `curry_d`, is the direct-style counterpart of `curry_c` and features the `(shift k k)` idiom, using Andrzej Filinski's implementation of shift and reset in terms of a global mutable cell and of `call/cc`. In each instance of the induction step, the continuation abstraction is implicitly applied to an argument in the curried application:

```mw
(define curry_d
  (lambda (f n)
    (if (< n 0)
        (error 'curry_d "negative input: ~s" n)
        (letrec ([visit (lambda (i)
                          (if (= i 0)
                              '()
                              (cons (shift k k)
                                    (visit (- i 1)))))])
          (reset (apply f (visit n)))))))
```

The heart of the matter is the observational equivalence between `(reset (... (shift k k) ...))` and `(lambda (x) (reset (... x ...)))` where `x` is fresh and the ellipses represent a pure context, i.e., one without control effects.

So evaluating

```mw
(((curry_d + 2) 1) 10)
```

reduces to evaluating

```mw
(((reset (apply + (visit 2))) 1) 10)
```

which reduces to evaluating

```mw
(((reset (apply + (cons (shift k k) (visit 1)))) 1) 10)
```

which is observationally equivalent to

```mw
(((lambda (x) (reset (apply + (cons x (visit 1))))) 1) 10)
```

which beta-reduces to evaluating

```mw
((reset (apply + (cons 1 (visit 1)))) 10)
```

which reduces to evaluating

```mw
((reset (apply + (cons 1 (cons (shift k k) (visit 0))))) 10)
```

which is observationally equivalent to

```mw
((lambda (x) (reset (apply + (cons 1 (cons x (visit 0)))))) 10)
```

which beta-reduces to evaluating

```mw
(reset (apply + (cons 1 (cons 10 (visit 0)))))
```

which reduces to evaluating

```mw
(reset (apply + (cons 1 (cons 10 '()))))
```

which is equivalent to

```mw
(reset (+ 1 10))
```

which delta-reduces to evaluating

```mw
(reset 11)
```

which yields the result, `11`.

The definition of `curry_d` also illustrates static delimited continuations. This static extent needs to be explicitly encoded if one wants to use `control` and `prompt`:

```mw
(define curry_cp
  (lambda (f n)
    (if (< n 0)
        (error 'curry_cp "negative input: ~s" n)
        (letrec ([visit (lambda (i)
                          (if (= i 0)
                              '()
                              (cons (control k (lambda (x) (prompt (k x))))
                                    (visit (- i 1)))))])
          (prompt (apply f (visit n)))))))
```
