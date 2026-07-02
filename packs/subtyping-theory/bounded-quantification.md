---
title: "Bounded quantification"
source: https://en.wikipedia.org/wiki/Bounded_quantification
domain: subtyping-theory
license: CC-BY-SA-4.0
tags: subtyping relation, covariance and contravariance, structural subtyping, nominal typing
fetched: 2026-07-02
---

# Bounded quantification

In type theory, **bounded quantification** (also **bounded polymorphism** or **constrained genericity**) refers to universal or existential quantifiers which are restricted ("bounded") to range only over the subtypes of a particular type. Bounded quantification is an interaction of parametric polymorphism with subtyping. Bounded quantification has traditionally been studied in the functional setting of System F<:, but is available in modern object-oriented languages supporting parametric polymorphism (generics) such as Java, C# and Scala.

## Overview

The purpose of bounded quantification is to allow for polymorphic functions to depend on some specific behaviour of objects instead of type inheritance. It assumes a record-based model for object classes, where every class member is a record element and all class members are named functions. Object attributes are represented as functions that take no argument and return an object. The specific behaviour is then some function name along with the types of the arguments and the return type. Bounded quantification considers all objects with such a function. An example would be a polymorphic `min` function that considers all objects that are comparable to each other.

### F-bounded quantification

***F*-bounded quantification** or **recursively bounded quantification**, introduced in 1989, allows for more precise typing of functions that are applied on recursive types. A recursive type is one that features as a constructor a function that uses it as a type for some argument, or the return value of a functional argument, or some argument of the functional return value of a functional argument, or so on: that is, in positive position.

## Example

This kind of type constraint can be expressed in Java with a generic interface. The following example demonstrates how to describe types that can be compared to each other and use this as typing information in polymorphic functions. The `Test::min` function uses simple bounded quantification and does not ensure the objects are mutually comparable, in contrast with the `Test::fMin` function which uses F-bounded quantification.

In mathematical notation, the types of the two functions are

- ${\texttt {min}}:\forall T,\forall S\subseteq \{{\texttt {compareTo}}:T\to {\texttt {int}}\},S\to S\to S$
- ${\texttt {fmin}}:\forall T\subseteq {\texttt {Comparable<}}T{\texttt {>}},T\to T\to T$

where ${\texttt {Comparable<}}T{\texttt {>}}=\{{\texttt {compareTo}}:T\to {\texttt {int}}\}$

Consider the following possible declarations in `java.lang`:

```mw
package java.lang;

public interface Comparable<T> {
    int compareTo(T other);
}

public class Integer implements Comparable<Integer> {
    @Override
    public int compareTo(Integer other) {
        // ...
    }
}

public class String implements Comparable<String> {
    @Override
    public int compareTo(String other) {
        // ...
    }
}
```

Then, in use:

```mw
package org.wikipedia.examples;

public class Test {
    public static <S extends Comparable> S min(S a, S b) {
        if (a.compareTo(b) <= 0) {
            return a;
        } else {
            return b;
        }
    }

    public static <T extends Comparable<T>> T fMin(T a, T b) {
        if (a.compareTo(b) <= 0) {
            return a;
        } else {
            return b;
        }
    }

    public static void main(String[] args) {
        String a = min("cat", "dog");
        Integer b = min(10, 3);
        Comparable c = min("cat", 3); // Throws ClassCastException at runtime
        String str = fMin("cat", "dog");
        Integer i = fMin(10, 3);
        // Object o = fMin("cat", 3); // Does not compile
    }
}
```
