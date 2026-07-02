---
title: "ReactiveX"
source: https://en.wikipedia.org/wiki/Reactive_extensions
domain: rxjs-observable
license: CC-BY-SA-4.0
tags: rxjs observable, reactive extensions, observable stream, async event pipeline
fetched: 2026-07-02
---

# ReactiveX

(Redirected from

Reactive extensions

)

**ReactiveX** (**Rx**, also known as **Reactive Extensions**) is a software library originally created by Microsoft that allows imperative programming languages to operate on sequences of data regardless of whether the data is synchronous or asynchronous. It provides a set of sequence operators that operate on each item in the sequence. It is an implementation of reactive programming and provides a blueprint for the tools to be implemented in multiple programming languages.

## Overview

ReactiveX is an API for asynchronous programming with observable streams.

Asynchronous programming allows programmers to call functions and then have the functions "callback" when they are done, usually by giving the function the address of another function to execute when it is done. Programs designed in this way often avoid the overhead of having many threads constantly starting and stopping.

Observable streams (i.e. streams that can be observed) in the context of Reactive Extensions are like event emitters that emit three events: next, error, and complete. An observable emits next events until it either emits an error event or a complete event. However, at that point it will not emit any more events, unless it is subscribed to again.

The examples below use the RxJS implementation of Reactive Extensions for the JavaScript programming language.

### Motivation

For sequences of data, it combines the advantages of iterators with the flexibility of event-based asynchronous programming. It also works as a simple promise, eliminating the pyramid of doom that results from multiple layers of callbacks.

### Observables and observers

ReactiveX is a combination of ideas from the observer and the iterator patterns and from functional programming.

An observer subscribes to an observable sequence. The sequence then sends the items to the observer one at a time, usually by calling the provided callback function. The observer handles each one before processing the next one. If many events come in asynchronously, they must be stored in a queue or dropped. In ReactiveX, an observer will never be called with an item out of order or (in a multi-threaded context) called before the callback has returned for the previous item. Asynchronous calls remain asynchronous and may be handled by returning an observable.

It is similar to the iterators pattern in that if a fatal error occurs, it notifies the observer separately (by calling a second function). When all the items have been sent, it completes (and notifies the observer by calling a third function). The Reactive Extensions API also borrows many of its operators from iterator operators in other programming languages.

Reactive Extensions is different from functional reactive programming as the Introduction to Reactive Extensions explains:

> It is sometimes called "functional reactive programming" but this is a misnomer. ReactiveX may be functional, and it may be reactive, but "functional reactive programming" is a different animal. One main point of difference is that functional reactive programming operates on values that change continuously over time, while ReactiveX operates on discrete values that are emitted over time. (See Conal Elliott's work for more-precise information on functional reactive programming.)

### Reactive operators

An operator is a function that takes one observable (the source) as its first argument and returns another observable (the destination, or outer observable). Then for every item that the source observable emits, it will apply a function to that item, and then emit it on the destination Observable. It can even emit another Observable on the destination observable. This is called an inner observable.

An operator that emits inner observables can be followed by another operator that in some way combines the items emitted by all the inner observables and emits the item on its outer observable. Examples include:

- `switchAll` – subscribes to each new inner observable as soon as it is emitted and unsubscribes from the previous one.
- `mergeAll` – subscribes to all inner observables as they are emitted and outputs their values in whatever order it receives them.
- `concatAll` – subscribes to each inner observable in order and waits for it to complete before subscribing to the next observable.

Operators can be chained together to create complex data flows that filter events based on certain criteria. Multiple operators can be applied to the same observable.

Some of the operators that can be used in Reactive Extensions may be familiar to programmers who use functional programming language, such as map, reduce, group, and zip. There are many other operators available in Reactive Extensions, though the operators available in a particular implementation for a programming language may vary.

#### Reactive operator examples

Here is an example of using the map and reduce operators. We create an observable from a list of numbers. The map operator will then multiply each number by two and return an observable. The reduce operator will then sum up all the numbers provided to it (the value of 0 is the starting point). Calling subscribe will register an *observer* that will observe the values from the observable produced by the chain of operators. With the subscribe method, we are able to pass in an error-handling function, called whenever an error is emitted in the observable, and a completion function when the observable has finished emitting items.

```mw
import { of, Observable, map, reduce } from 'rxjs';

const source: Observable<number> = of(1, 2, 3, 4, 5);
source
  .pipe(
    map((value) => value * 2),
    reduce((sum, value) => sum + value, 0)
  )
  .subscribe({
    next: (value) => {
      console.log(value);
    },
    error: (error) => {
      console.error(error);
    },
    complete: () => {
      console.log('done');
    },
  });
```

#### Usage in stream-oriented programming

Certain RxJS primitives such as `BehaviorSubject` make it possible to create pure stateful streams to track application state of arbitrary complexity in simple terms.

The button below will feed an event to the stream, which in turn will re-emit the next natural number every time, back into the `<span>` tag that follows and displays the count of clicks detected.

Libraries such as *Rimmel.js*, designed around RxJS Observables, enable integration between reactive streams and the HTML DOM:

```mw
import { BehaviorSubject, scan } from 'rxjs';
import { rml } from 'rimmel';

const count = new BehaviorSubject(0).pipe(
  scan(x => x+1)
);

document.body.innerHTML = rml`
  <button onclick="${counter}">click</button>
  <p>Count is: <span>${count}</span></p>
`;
```

## History

Reactive Extensions was created by the Cloud Programmability Team at Microsoft around 2011, as a byproduct of a larger effort called Volta. It was originally intended to provide an abstraction for events across different tiers in an application to support tier splitting in Volta. The project's logo represents an electric eel, which is a reference to Volta. The extensions suffix in the name is a reference to the Parallel Extensions technology which was invented around the same time; the two are considered complementary.

The initial implementation of Rx was for .NET Framework and was released on June 21, 2011. Later, the team started the implementation of Rx for other platforms, including JavaScript and C++. The technology was released as open source in late 2012, initially on CodePlex. Later, the code moved to GitHub and has been ported to several other languages, including Go, Java, Kotlin, PHP and Rust.
