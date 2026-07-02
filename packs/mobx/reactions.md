---
title: "Running side effects with reactions · MobX 🇺🇦"
source: https://mobx.js.org/reactions.html
domain: mobx
license: CC-BY-SA-4.0 / MIT (mobx.js.org)
tags: mobx, observable state, transparent reactivity, mobx reaction
fetched: 2026-07-02
---

# Running side effects with reactions {🚀}

Reactions are an important concept to understand, as it is where everything in MobX comes together. The goal of reactions is to model side effects that happen automatically. Their significance is in creating consumers for your observable state and *automatically* running side effects whenever something *relevant* changes.

However, with that in mind, it is important to realize that the APIs discussed here should rarely be used. They are often abstracted away in other libraries (like mobx-react) or abstractions specific to your application.

But, to grok MobX, let's take a look at how reactions can be created. The simplest way is to use the `autorun` utility. Beyond that, there are also `reaction` and `when`.

## Autorun

Usage:

- `autorun(effect: (reaction) => void, options?)`

The `autorun` function accepts one function that should run every time anything it observes changes. It also runs once when you create the `autorun` itself. It only responds to changes in observable state, things you have annotated `observable` or `computed`.

### How tracking works

Autorun works by running the `effect` in a *reactive context*. During the execution of the provided function, MobX keeps track of all observable and computed values that are directly or indirectly *read* by the effect. Once the function finishes, MobX will collect and subscribe to all observables that were read and wait until any of them changes again. Once they do, the `autorun` will trigger again, repeating the entire process.

(autorun)

This is how the example below works like.

### Example

```javascript
import { makeAutoObservable, autorun } from "mobx"

class Animal {
    name
    energyLevel

    constructor(name) {
        this.name = name
        this.energyLevel = 100
        makeAutoObservable(this)
    }

    reduceEnergy() {
        this.energyLevel -= 10
    }

    get isHungry() {
        return this.energyLevel < 50
    }
}

const giraffe = new Animal("Gary")

autorun(() => {
    console.log("Energy level:", giraffe.energyLevel)
})

autorun(() => {
    if (giraffe.isHungry) {
        console.log("Now I'm hungry!")
    } else {
        console.log("I'm not hungry!")
    }
})

console.log("Now let's change state!")
for (let i = 0; i < 10; i++) {
    giraffe.reduceEnergy()
}
```

Running this code, you will get the following output:

```
Energy level: 100
I'm not hungry!
Now let's change state!
Energy level: 90
Energy level: 80
Energy level: 70
Energy level: 60
Energy level: 50
Energy level: 40
Now I'm hungry!
Energy level: 30
Energy level: 20
Energy level: 10
Energy level: 0
```

As you can see in the first two lines of the output above, both `autorun` functions run once when they are initialized. This is all you would see without the `for` loop.

Once we run the `for` loop to change the `energyLevel` with the `reduceEnergy` action, we see a new log entry every time an `autorun` function observes a change in its observable state:

1. For the *"Energy level"* function, this is every time the `energyLevel` observable changes, 10 times in total.
2. For the *"Now I'm hungry"* function, this is every time the `isHungry` computed changes, only one time.

## Reaction

Usage:

- `reaction(() => value, (value, previousValue, reaction) => { sideEffect }, options?)`.

`reaction` is like `autorun`, but gives more fine grained control on which observables will be tracked. It takes two functions: the first, *data* function, is tracked and returns the data that is used as input for the second, *effect* function. It is important to note that the side effect *only* reacts to data that was *accessed* in the data function, which might be less than the data that is actually used in the effect function.

The typical pattern is that you produce the things you need in your side effect in the *data* function, and in that way control more precisely when the effect triggers. By default, the result of the *data* function has to change in order for the *effect* function to be triggered. Unlike `autorun`, the side effect won't run once when initialized, but only after the data expression returns a new value for the first time.

**Example:** the data and effect functions

In the example below, the reaction is only triggered once, when `isHungry` changes. Changes to `giraffe.energyLevel`, which is used by the *effect* function, do not cause the *effect* function to be executed. If you wanted `reaction` to respond to this as well, you would have to also access it in the *data* function and return it.

```javascript
import { makeAutoObservable, reaction } from "mobx"

class Animal {
    name
    energyLevel

    constructor(name) {
        this.name = name
        this.energyLevel = 100
        makeAutoObservable(this)
    }

    reduceEnergy() {
        this.energyLevel -= 10
    }

    get isHungry() {
        return this.energyLevel < 50
    }
}

const giraffe = new Animal("Gary")

reaction(
    () => giraffe.isHungry,
    isHungry => {
        if (isHungry) {
            console.log("Now I'm hungry!")
        } else {
            console.log("I'm not hungry!")
        }
        console.log("Energy level:", giraffe.energyLevel)
    }
)

console.log("Now let's change state!")
for (let i = 0; i < 10; i++) {
    giraffe.reduceEnergy()
}
```

Output:

```
Now let's change state!
Now I'm hungry!
Energy level: 40
```

## When

Usage:

- `when(predicate: () => boolean, effect?: () => void, options?)`
- `when(predicate: () => boolean, options?): Promise`

`when` observes and runs the given *predicate* function until it returns `true`. Once that happens, the given *effect* function is executed and the autorunner is disposed.

The `when` function returns a disposer, allowing you to cancel it manually, unless you don't pass in a second `effect` function, in which case it returns a `Promise`.

**Example:** dispose of things in a reactive way

`when` is really useful for disposing or canceling of things in a reactive way. For example:

```javascript
import { when, makeAutoObservable } from "mobx"

class MyResource {
    constructor() {
        makeAutoObservable(this, { dispose: false })
        when(
            
            () => !this.isVisible,
            
            () => this.dispose()
        )
    }

    get isVisible() {
        
    }

    dispose() {
        
    }
}
```

As soon as `isVisible` becomes `false`, the `dispose` method is called that then does some cleanup for `MyResource`.

### `await when(...)`

If no `effect` function is provided, `when` returns a `Promise`. This combines nicely with `async / await` to let you wait for changes in observable state.

```javascript
async function() {
    await when(() => that.isVisible)
    
}
```

To cancel `when` prematurely, it is possible to call `.cancel()` on the promise returned by itself.

## Rules

There are a few rules that apply to any reactive context:

1. Affected reactions run by default immediately (synchronously) if an observable is changed. However, they won't run before the end of the current outermost (trans)action.
2. Autorun tracks only the observables that are read during the synchronous execution of the provided function, but it won't track anything that happens asynchronously.
3. Autorun won't track observables that are read by an action invoked by the autorun, as actions are always *untracked*.

For more examples on what precisely MobX will and will not react to, check out the Understanding reactivity section. For a more detailed technical breakdown on how tracking works, read the blog post Becoming fully reactive: an in-depth explanation of MobX.

## Always dispose of reactions

The functions passed to `autorun`, `reaction` and `when` are only garbage collected if all objects they observe are garbage collected themselves. In principle, they keep waiting forever for new changes to happen in the observables they use. To be able to stop them from waiting until forever has passed, they all return a disposer function that can be used to stop them and unsubscribe from any observables they used.

```javascript
const counter = observable({ count: 0 })

const disposer = autorun(() => {
    console.log(counter.count)
})

counter.count++

disposer()

counter.count++
```

We strongly recommend to always use the disposer function that is returned from these methods as soon as their side effect is no longer needed. Failing to do so can lead to memory leaks.

The `reaction` argument that is passed as second argument to the effect functions of `reaction` and `autorun`, can be used to prematurely clean up the reaction as well by calling `reaction.dispose()`.

**Example:** memory leak

```javascript
class Vat {
    value = 1.2

    constructor() {
        makeAutoObservable(this)
    }
}

const vat = new Vat()

class OrderLine {
    price = 10
    amount = 1
    constructor() {
        makeAutoObservable(this)

        
        
        
        this.disposer1 = autorun(() => {
            doSomethingWith(this.price * this.amount)
        })

        
        
        
        this.disposer2 = autorun(() => {
            doSomethingWith(this.price * this.amount * vat.value)
        })
    }

    dispose() {
        
        
        this.disposer1()
        this.disposer2()
    }
}
```

In environments that support Explicit Resource Management, the disposer function includes a `[Symbol.dispose]` method that can be used to dispose of the reaction. This can be useful when disposing of several reactions simultaneously or when disposing of reactions alongside other Disposables.

**Example:** using DisposableStack

```javascript
function createSomeDisposableResource() {}

class Vat {
    value = 1.2

    constructor() {
        makeAutoObservable(this)
    }
}

const vat = new Vat()

class OrderLine {
    price = 10
    amount = 1
    disposableStack = new DisposableStack()
    someDisposableResource

    constructor() {
        makeAutoObservable(this)

        this.disposableStack.use(autorun(() => {
            doSomethingWith(this.price * this.amount)
        }))

        this.disposableStack.use(autorun(() => {
            doSomethingWith(this.price * this.amount * vat.value)
        }))

        this.someDisposableResource = this.disposableStack.use(createSomeDisposableResource())
    }

    [Symbol.dispose]() {
        this.disposableStack[Symbol.dispose]();
    }
}
```

## Use reactions sparingly!

As it was already said, you won't create reactions very often. It might very well be that your application doesn't use any of these APIs directly, and the only way reactions are constructed is indirectly, through for example `observer` from the mobx-react bindings.

Before you set up a reaction, it is good to first check if it conforms to the following principles:

1. **Only use Reactions if there is no direct relation between cause and effect**: If a side effect should happen in response to a very limited set of events / actions, it will often be clearer to directly trigger the effect from those specific actions. For example, if pressing a form submit button should lead to a network request to be posted, it is clearer to trigger this effect directly in response of the `onClick` event, rather than indirectly through a reaction. In contrast, if any change you make to the form state should automatically end up in local storage, then a reaction can be very useful, so that you don't have to trigger this effect from every individual `onChange` event.
2. **Reactions shouldn't update other observables**: Is the reaction going to modify other observables? If the answer is yes, typically the observable you want to update should be annotated as a `computed` value instead. For example, if a collection of todos is altered, don't use a reaction to compute the amount of `remainingTodos`, but annotate `remainingTodos` as a computed value. That will lead to much clearer and easier to debug code. Reactions should not compute new data, but only cause effects.
3. **Reactions should be independent**: Does your code rely on some other reaction having to run first? If that is the case, you probably either violated the first rule, or the new reaction you are about to create should be merged into the one it is depending upon. MobX does not guarantee the order in which reactions will be run.

There are real-life scenarios that do not fit in the above principles. That is why they are *principles*, not *laws*. But, the exceptions are rare so only violate them as a last resort.

## Options {🚀}

The behavior of `autorun`, `reaction` and `when` can be further fine-tuned by passing in an `options` argument as shown in the usages above.

### `name`

This string is used as a debug name for this reaction in the Spy event listeners and MobX developer tools.

### `fireImmediately` *(reaction)*

Boolean indicating that the *effect* function should immediately be triggered after the first run of the *data* function. `false` by default.

### `delay` *(autorun, reaction)*

Number of milliseconds that can be used to throttle the effect function. If zero (default), no throttling happens.

### `timeout` *(when)*

Set a limited amount of time that `when` will wait for. If the deadline passes, `when` will reject / throw.

### `signal`

An AbortSignal object instance; can be used as an alternative method for disposal. When used with promise version of `when`, the promise rejects with the "WHEN_ABORTED" error.

### `onError`

By default, any exception thrown inside an reaction will be logged, but not further thrown. This is to make sure that an exception in one reaction does not prevent the scheduled execution of other, possibly unrelated reactions. This also allows reactions to recover from exceptions. Throwing an exception does not break the tracking done by MobX, so subsequent runs of the reaction might complete normally again if the cause for the exception is removed. This option allows overriding that behavior. It is possible to set a global error handler or to disable catching errors completely using configure.

### `scheduler` *(autorun, reaction)*

Set a custom scheduler to determine how re-running the autorun function should be scheduled. It takes a function that should be invoked at some point in the future, for example: `{ scheduler: run => { setTimeout(run, 1000) }}`

### `equals`: (reaction)

Set to `comparer.default` by default. If specified, this comparer function is used to compare the previous and next values produced by the *data* function. The *effect* function is only invoked if this function returns false.

Check out the Built-in comparers section.
