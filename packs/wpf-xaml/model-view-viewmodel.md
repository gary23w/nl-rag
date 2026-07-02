---
title: "Model–view–viewmodel"
source: https://en.wikipedia.org/wiki/Model-view-viewmodel
domain: wpf-xaml
license: CC-BY-SA-4.0
tags: wpf xaml, windows presentation foundation, xaml markup, data binding pipeline
fetched: 2026-07-02
---

# Model–view–viewmodel

(Redirected from

Model-view-viewmodel

)

**Model–view–viewmodel** (**MVVM**) is a layer architecture design in computer software that facilitates the separation of the development of a graphical user interface (GUI; the *view*)—be it via a markup language or GUI code—from the development of the business logic or back-end logic (the *model*) such that the view is not dependent upon any specific model platform.

The *viewmodel* of MVVM is a value converter, meaning it is responsible for exposing (converting) the data objects from the model in such a way they can be easily managed and presented. In this respect, the viewmodel is more *model* than *view*, and handles most (if not all) of the view's display logic. The viewmodel may implement a mediator pattern, organizing access to the back-end logic around the set of use cases supported by the view.

MVVM is a variation of Martin Fowler's Presentation Model design pattern. MVVM is very similar to the Model-view-presenter pattern. It was invented by Microsoft architects Ken Cooper and Ted Peters specifically to simplify event-driven programming of user interfaces. The pattern was incorporated into the Windows Presentation Foundation (WPF) (Microsoft's .NET graphics system) and Silverlight, WPF's Internet application derivative. John Gossman, a Microsoft WPF and Silverlight architect, announced MVVM on his blog in 2005.

Model–view–viewmodel is also referred to as **model–view–binder**, especially in implementations not involving the .NET platform. ZK, a web application framework written in Java, and the JavaScript library KnockoutJS use model–view–binder.

## Components of MVVM pattern

**Model**

Model

refers either to a

domain model

, which represents real state content (an object-oriented approach), or to the

data access layer

, which represents content (a data-centric approach).

**View**

As in the

model–view–controller

(MVC) and

model–view–presenter

(MVP) patterns, the

view

is the structure, layout, and appearance of what a user sees on the screen.

It displays a representation of the model and receives the user's interaction with the view (mouse clicks, keyboard input, screen tap gestures, etc.), and it forwards the handling of these to the view model via the

data binding

(properties, event callbacks, etc.) that is defined to link the view and view model.

**View model**

The

view model

is an abstraction of the view exposing public properties and commands. Instead of the controller of the MVC pattern, or the presenter of the MVP pattern, MVVM has a

binder

, which automates communication between the view and its bound properties in the view model. The view model has been described as a state of the data in the model.

The main difference between the view model and the Presenter in the MVP pattern is that the presenter has a reference to a view, whereas the view model does not. Instead, a view directly binds to properties on the view model to send and receive updates. To function efficiently, this requires a binding technology or generating

boilerplate code

to do the binding.

Under

object-oriented programming

, the view model can sometimes be referred to as a

data transfer object

.

**Binder**

Declarative data and command-binding are implicit in the MVVM pattern. In the Microsoft

solution stack

, the binder is a

markup language

called

XAML

.

The binder frees the developer from being obliged to write boiler-plate logic to synchronize the view model and view. When implemented outside of the Microsoft stack, the presence of a declarative data binding technology is what makes this pattern possible,

and without a binder, one would typically use MVP or MVC instead and have to write more boilerplate (or generate it with some other tool).

## Rationale

MVVM was designed to remove virtually all GUI code ("code-behind") from the view layer, by using data binding functions in WPF (Windows Presentation Foundation) to better facilitate the separation of view layer development from the rest of the pattern. Instead of requiring user experience (UX) developers to write GUI code, they can use the framework markup language (e.g. XAML) and create data bindings to the view model, which is written and maintained by application developers. The separation of roles allows interactive designers to focus on UX needs rather than programming of business logic. The layers of an application can thus be developed in multiple work streams for higher productivity. Even when a single developer works on the entire codebase, a proper separation of the view from the model is more productive, as the user interface typically changes frequently and late in the development cycle based on end-user feedback.

The MVVM pattern attempts to gain both advantages of separation of functional development provided by MVC, while leveraging the advantages of data bindings and the framework by binding data as close to the pure application model as possible. It uses the binder, view model, and any business layers' data-checking features to validate incoming data. The result is that the model and framework drive as much of the operations as possible, eliminating or minimizing application logic which directly manipulates the view (e.g., code-behind).

## Criticism

John Gossman has criticized the MVVM pattern and its application in specific uses, stating that MVVM can be "overkill" when creating simple user interfaces. For larger applications, he believes that generalizing the viewmodel upfront can be difficult, and that large-scale data binding can lead to lower performance.

## Implementations

### .NET frameworks

- .NET Community Toolkit
- Avalonia
- Caliburn, Caliburn.Micro
- Chinook.DynamicMvvm Open source
- DevExpress MVVM
- DotVVM open source project
- FreshMvvm
- Jellyfish
- Mugen MVVM Toolkit
- MVVMLight Toolkit
- MvvmCross
- MvvmZero
- Prism Library
- Rascl
- ReactiveUI
- Uno Platform - Open source

#### Web Component libraries

- Microsoft FAST
- Omi.js

### Java frameworks

- ZK Studio

### JavaScript frameworks

- Angular
- Aurelia
- Durandal
- Ember.js
- Ext JS
- Knockout.js
- Oracle JET
- React
- Svelte
- Vue.js

### Frameworks for C++ and XAML (Windows)

- Xamlcc

## Examples

The following are simple examples of an implementation of the MVVM pattern.

### C++

This is an example using C++.

Model.cppm:

```mw
export module wikipedia.examples.mvvm.Model;

export namespace wikipedia::examples::mvvm {

class Model {
private:
    int counter = 0;

public:
    [[nodiscard]]
    int getCounter() const noexcept {
        return counter;
    }

    void increment() noexcept {
        counter++;
    }

    void decrement() noexcept {
        counter--;
    }
};

}
```

ViewModel.cppm:

```mw
export module wikipedia.examples.mvvm.ViewModel;

import wikipedia.examples.mvvm.Model;

export namespace wikipedia::examples::mvvm {

class ViewModel {
private:
    Model& model;

public:
    explicit ViewModel(Model& m): 
        model{m} {}

    void incrementCounter() noexcept {
        model.increment();
    }

    void decrementCounter() noexcept {
        model.decrement();
    }

    [[nodiscard]]
    int getCounterValue() const noexcept {
        return model.getCounter();
    }
};

}
```

View.cppm:

```mw
export module wikipedia.examples.mvvm.View;

import std;
import wikipedia.examples.mvvm.ViewModel;

using std::cin;
using std::string;

export namespace wikipedia::examples::mvvm {

class View {
private:
    ViewModel& viewModel;

public:
    explicit View(ViewModel& vm): 
        viewModel{vm} {}

    void run() {
        string input;
        while (true) {
            std::println("Counter: {}", viewModel.getCounterValue());
            std::print("Enter command (i=increment, d=decrement, q=quit): ");
            std::getline(cin, input);

            if (input == "i") {
                viewModel.incrementCounter();
            } else if (input == "d") {
                viewModel.decrementCounter();
            } else if (input == "q") {
                break;
            } else {
                std::println("Unknown command.");
            }
        }
    }
};

}
```

Then, the application Main.cpp could be run like so:

```mw
import wikipedia.examples.mvvm.Model;
import wikipedia.examples.mvvm.View;
import wikipedia.examples.mvvm.ViewModel;

using namespace wikipedia::examples::mvvm;

int main(int argc, char* argv[]) {
    Model m;
    ViewModel vm(m);
    View v(vm);
    v.run();
    return 0;
}
```

### C

This is an example using C#.

Model.cs:

```mw
namespace Wikipedia.Examples.Mvvm;

public class Model
{
    public int Counter { get; private set; } = 0;

    public void Increment() => Counter++;
    public void Decrement() => Counter--;
}
```

ViewModel.cs:

```mw
namespace Wikipedia.Examples.Mvvm;

public class ViewModel
{
    private readonly Model _model;

    public ViewModel(Model model)
    {
        _model = model;
    }

    public void IncrementCounter() => _model.Increment();
    public void DecrementCounter() => _model.Decrement();
    public int CounterValue => _model.Counter;
}
```

View.cs:

```mw
namespace Wikipedia.Examples.Mvvm;

using System;

public class View
{
    private readonly ViewModel _viewModel;

    public View(ViewModel viewModel)
    {
        _viewModel = viewModel;
    }

    public void Run()
    {
        string input = String.Empty;
        while (true)
        {
            Console.WriteLine($"Counter: {_viewModel.CounterValue}");
            Console.Write("Enter command (i=increment, d=decrement, q=quit): ");
            input = Console.ReadLine();
            switch (input)
            {
                case "i":
                    _viewModel.IncrementCounter();
                    break;
                case "d":
                    _viewModel.DecrementCounter();
                    break;
                case "q":
                    return;
                default:
                    Console.WriteLine("Unknown command.");
                    break;
            }
        }
    }
}
```

Then, the application Main.cs could be run like so:

```mw
namespace Wikipedia.Examples;

using Wikipedia.Examples.Mvvm;

public class Main
{
    public static void Main()
    {
        Model model = new();
        ViewModel viewModel = new(model);
        View view = new(viewModel);
        view.Run();
    }
}
```

### Java

This is an example using Java.

Model.java:

```mw
package org.wikipedia.examples.mvvm;

public class Model {
    private int counter = 0;

    public int getCounter() {
        return counter;
    }

    public void increment() {
        counter++;
    }

    public void decrement() {
        counter--;
    }
}
```

ViewModel.java:

```mw
package org.wikipedia.examples.mvvm;

public class ViewModel {
    private final Model model;

    public ViewModel(Model model) {
        this.model = model;
    }

    public void incrementCounter() {
        model.increment();
    }

    public void decrementCounter() {
        model.decrement();
    }

    public int getCounterValue() {
        return model.getCounter();
    }
}
```

View.java:

```mw
package org.wikipedia.examples.mvvm;

import java.util.Scanner;

public class View {
    private final ViewModel viewModel;

    public View(ViewModel viewModel) {
        this.viewModel = viewModel;
    }

    public void run() {
        Scanner stdin = new Scanner(System.in);
        String input;
        while (true) {
            System.out.printf("Counter: %d%n", viewModel.getCounterValue());
            System.out.print("Enter command (i=increment, d=decrement, q=quit): ");
            input = stdin.nextLine();
            switch (input) {
                case "i":
                    viewModel.incrementCounter();
                    break;
                case "d":
                    viewModel.decrementCounter();
                    break;
                case "q":
                    return;
                default:
                    System.out.println("Unknown command.");
            }
        }
    }
}
```

Then, the application Main.java could be run like so:

```mw
package org.wikipedia.examples;

import org.wikipedia.examples.mvvm.*;

public class Main {
    public static void main(String[] args) {
        Model m = new Model();
        ViewModel vm = new ViewModel(m);
        View v = new View(vm);
        v.run();
    }
}
```

### Rust

This is an example using Rust.

model.rs:

```mw
pub struct Model {
    counter: i32,
}

impl Model {
    pub fn new() -> Self {
        Model { counter: 0 }
    }

    pub fn get_counter(&self) -> i32 {
        self.counter
    }

    pub fn increment(&mut self) {
        self.counter += 1;
    }

    pub fn decrement(&mut self) {
        self.counter -= 1;
    }
}
```

view_model.rs:

```mw
use super::model::Model;

pub struct ViewModel<'a> {
    model: &'a mut Model,
}

impl<'a> ViewModel<'a> {
    pub fn new(model: &'a mut Model) -> Self {
        Self { model }
    }

    pub fn increment_counter(&mut self) {
        self.model.increment();
    }

    pub fn decrement_counter(&mut self) {
        self.model.decrement();
    }

    pub fn get_counter_value(&self) -> i32 {
        self.model.get_counter()
    }
}
```

view.rs:

```mw
use std::io::{self, Write};

use super::view_model::ViewModel;

pub struct View<'a> {
    view_model: &'a mut ViewModel<'a>,
}

impl<'a> View<'a> {
    pub fn new(view_model: &'a mut ViewModel<'a>) -> Self {
        Self { view_model }
    }

    pub fn run(&mut self) {
        loop {
            println!("Counter: {}", self.view_model.get_counter_value());

            print!("Enter command (i=increment, d=decrement, q=quit): ");
            io::stdout().flush().unwrap();

            let mut input: String = String::new();
            io::stdin().read_line(&mut input).unwrap();
            let input: String = input.trim();

            match input {
                "i" => self.view_model.increment_counter(),
                "d" => self.view_model.decrement_counter(),
                "q" => break,
                _ => println!("Unknown command."),
            }
        }
    }
}
```

Then, the application main.rs could be run like so:

```mw
mod mvvm;

use mvvm::{
    model::Model, 
    view::View,
    view_model::ViewModel
};

fn main() {
    let mut m: Model = Model::new();
    let mut vm: ViewModel = ViewModel::new(&mut m);
    let mut v: View = View::new(&mut vm);
    v.run();
}
```
