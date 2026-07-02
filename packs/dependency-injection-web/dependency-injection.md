---
title: "Dependency injection"
source: https://en.wikipedia.org/wiki/Dependency_injection
domain: dependency-injection-web
license: CC-BY-SA-4.0
tags: dependency injection, inversion of control, ioc container, service injection
fetched: 2026-07-02
---

# Dependency injection

In software engineering, **dependency injection** is a programming technique in which an object or function receives other objects or functions that it requires, as opposed to creating them internally. Dependency injection aims to separate the concerns of constructing objects and using them, leading to loosely coupled programs. The pattern ensures that an object or function that wants to use a given service should not have to know how to construct those services. Instead, the receiving "client" (object or function) is provided with its dependencies by external code (an "injector"), which it is not aware of. Dependency injection makes implicit dependencies explicit and helps solve the following problems:

- How can a class be independent from the creation of the objects it depends on?
- How can an application and the objects it uses support different configurations?

Dependency injection is often used to keep code in-line with the dependency inversion principle.

In statically typed languages using dependency injection means that a client only needs to declare the interfaces of the services it uses, rather than their concrete implementations, making it easier to change which services are used at runtime without recompiling.

Application frameworks often combine dependency injection with inversion of control. Under inversion of control, the framework first constructs an object (such as a controller), and then passes control flow to it. With dependency injection, the framework also instantiates the dependencies declared by the application object (often in the constructor method's parameters), and passes the dependencies into the object.

Dependency injection implements the idea of "inverting control over the implementations of dependencies", which is why certain Java frameworks generically name the concept "inversion of control" (not to be confused with inversion of control flow).

## Roles

> **Dependency injection for five-year-olds**
> 
> When you go and get things out of the refrigerator for yourself, you can cause problems. You might leave the door open, you might get something Mommy or Daddy don't want you to have. You might even be looking for something we don't even have or which has expired.
> 
> What you should be doing is stating a need, "I need something to drink with lunch," and then we will make sure you have something when you sit down to eat something.

—

John Munsch, 28 October 2009.

Dependency injection involves four roles: services, clients, interfaces, and injectors.

### Services and clients

A service is any class which contains useful functionality. In turn, a client is any class which uses services. The services that a client requires are the client's *dependencies*.

Any object can be a service or a client; the names relate only to the role the objects play in an injection. The same object may even be both a client (it uses injected services) and a service (it is injected into other objects). Upon injection, the service is made part of the client's state, available for use.

### Interfaces

Clients should not know how their dependencies are implemented, only their names and API. A service which retrieves emails, for instance, may use the IMAP or POP3 protocols behind the scenes, but this detail is likely irrelevant to calling code that merely wants an email retrieved. By ignoring implementation details, clients do not need to change when their dependencies do.

### Injectors

The **injector**, sometimes also called an assembler, container, provider or factory, introduces services to the client.

The role of injectors is to construct and connect complex object graphs, where objects may be both clients and services. The injector itself may be many objects working together, but must not be the client, as this would create a circular dependency.

Because dependency injection separates how objects are constructed from how they are used, it often diminishes the importance of the **`new`** keyword found in most object-oriented languages. Because the framework handles creating services, the programmer tends to only directly construct value objects which represents entities in the program's domain (such as an `Employee` object in a business app or an `Order` object in a shopping app).

### Analogy

As an analogy, cars can be thought of as services which perform the useful work of transporting people from one place to another. Car engines can require gas, diesel or electricity, but this detail is unimportant to the client—a passenger—who only cares if it can get them to their destination.

Cars present a uniform interface through their pedals, steering wheels and other controls. As such, which engine they were 'injected' with on the factory line ceases to matter and drivers can switch between any kind of car as needed.

## Advantages and disadvantages

### Advantages

A basic benefit of dependency injection is decreased coupling between classes and their dependencies.

By removing a client's knowledge of how its dependencies are implemented, programs become more reusable, testable and maintainable.

This also results in increased flexibility: a client may act on anything that supports the intrinsic interface the client expects.

More generally, dependency injection reduces boilerplate code, since all dependency creation is handled by a singular component.

Finally, dependency injection allows concurrent development. Two developers can independently develop classes that use each other, while only needing to know the interface the classes will communicate through. Plugins are often developed by third-parties that never even talk to developers of the original product.

#### Testing

Many of dependency injection's benefits are particularly relevant to unit-testing.

For example, dependency injection can be used to externalize a system's configuration details into configuration files, allowing the system to be reconfigured without recompilation. Separate configurations can be written for different situations that require different implementations of components.

Similarly, because dependency injection does not require any change in code behavior, it can be applied to legacy code as a refactoring. This makes clients more independent and are easier to unit test in isolation, using stubs or mock objects, that simulate other objects not under test.

This ease of testing is often the first benefit noticed when using dependency injection.

### Disadvantages

Critics of dependency injection argue that it:

- Creates clients that demand configuration details, which can be onerous when obvious defaults are available.
- Makes code difficult to trace because it separates behavior from construction.
- Is typically implemented with reflection or dynamic programming, hindering IDE automation.
- Typically requires more upfront development effort.
- Encourages dependence on a framework.

## Types of dependency injection

There are several ways in which a client can receive injected services:

- Constructor injection, where dependencies are provided through a client's class constructor.
- Method Injection, where dependencies are provided to a method only when required for specific functionality.
- Setter injection, where the client exposes a setter method which accepts the dependency.
- Interface injection, where the dependency's interface provides an injector method that will inject the dependency into any client passed to it.

In some frameworks, clients do not need to actively accept dependency injection at all. In Java, for example, reflection can make private attributes public when testing and inject services directly.

### Without dependency injection

In the following Java example, the `Client` class contains a `Service` member variable initialized in the constructor. The client directly constructs and controls which service it uses, creating a hard-coded dependency.

```mw
public class Client {
    private Service service;

    Client() {
        // The dependency is hard-coded.
        this.service = new ExampleService();
    }
}
```

### Constructor injection

The most common form of dependency injection is for a class to request its dependencies through its constructor. This ensures the client is always in a valid state, since it cannot be instantiated without its necessary dependencies.

```mw
public class Client {
    private Service service;

    // The dependency is injected through a constructor.
    Client(final Service service) {
        if (service == null) {
            throw new IllegalArgumentException("service must not be null");
        }
        this.service = service;
    }
}
```

### Method Injection

Dependencies are passed as arguments to a specific method, allowing them to be used only during that method's execution without maintaining a long-term reference. This approach is particularly useful for temporary dependencies or when different implementations are needed for various method calls.

```mw
public class Client {
    public void performAction(Service service) {
        if (service == null) {
            throw new IllegalArgumentException("service must not be null");
        }
        service.execute();
    }
}
```

### Setter injection

By accepting dependencies through a setter method, rather than a constructor, clients can allow injectors to manipulate their dependencies at any time. This offers flexibility, but makes it difficult to ensure that all dependencies are injected and valid before the client is used.

```mw
public class Client {
    private Service service;

    // The dependency is injected through a setter method.
    public void setService(final Service service) {
        if (service == null) {
            throw new IllegalArgumentException("service must not be null");
        }
        this.service = service;
    }
}
```

### Interface injection

With interface injection, dependencies are completely ignorant of their clients, yet still send and receive references to new clients.

In this way, the dependencies become injectors. The key is that the injecting method is provided through an interface.

An assembler is still needed to introduce the client and its dependencies. The assembler takes a reference to the client, casts it to the setter interface that sets that dependency, and passes it to that dependency object which in turn passes a reference to itself back to the client.

For interface injection to have value, the dependency must do something in addition to simply passing back a reference to itself. This could be acting as a factory or sub-assembler to resolve other dependencies, thus abstracting some details from the main assembler. It could be reference-counting so that the dependency knows how many clients are using it. If the dependency maintains a collection of clients, it could later inject them all with a different instance of itself.

```mw
package org.wikipedia.examples;

import java.util.HashSet;
import java.util.Set;

interface ServiceSetter {
    void setService(Service service);
}

class Client implements ServiceSetter {
    private Service service;

    @Override
    public void setService(final Service service) {
        if (service == null) {
            throw new IllegalArgumentException("service must not be null");
        }
        this.service = service;
    }
}

class ServiceInjector {
	private final Set<ServiceSetter> clients = new HashSet<>();

	public void inject(final ServiceSetter client) {
		this.clients.add(client);
		client.setService(new ExampleService());
	}

	public void switch() {
		for (final Client client : this.clients) {
			client.setService(new AnotherExampleService());
		}
	}
}

class ExampleService implements Service {}

class AnotherExampleService implements Service {}
```

## Assembly

The simplest way of implementing dependency injection is to manually arrange services and clients, typically done at the program's root, where execution begins.

```mw
public class Program {
    public static void main(String[] args) {
        // Build the service.
        Service service = new ExampleService();

        // Inject the service into the client.
        Client client = new Client(service);

        // Use the objects.
        System.out.println(client.greet());
    }	
}
```

Manual construction may be more complex and involve builders, factories, or other construction patterns.

### Frameworks

Manual dependency injection is often tedious and error-prone for larger projects, promoting the use of frameworks which automate the process. Manual dependency injection becomes a dependency injection framework once the constructing code is no longer custom to the application and is instead universal. While useful, these tools are not required in order to perform dependency injection.

Some frameworks, like Spring, can use external configuration files to plan program composition:

```mw
package org.wikipedia.examples;

import org.springframework.beans.factory.BeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Injector {
	public static void main(String[] args) {
		// Details about which concrete service to use are stored in configuration separate from the program itself.
		final BeanFactory beanfactory = new ClassPathXmlApplicationContext("Beans.xml");
		final Client client = (Client) beanfactory.getBean("client");
		System.out.println(client.greet());
	}
}
```

Even with a potentially long and complex object graph, the only class mentioned in code is the entry point, in this case `Client`. `Client` has not undergone any changes to work with Spring and remains a POJO. By keeping Spring-specific annotations and calls from spreading out among many classes, the system stays only loosely dependent on Spring.

## Examples

### Angular

The following example shows an Angular component receiving a greeting service through dependency injection:

```mw
/* greeter.service.ts */
import { Injectable, inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';

export interface IGreeterService {
    greet(text: string): void;
}

@Injectable({
    providedIn: 'root'
})
export class GreeterService implements IGreeterService {
  // Use inject(DOCUMENT) and access defaultView to get the Window object
  private window: Window = inject(DOCUMENT).defaultView as Window;

  greet(text: string): void {
    this.window.alert(text);
  }
}
```

```mw
<!-- my-controller.component.html -->
<div>
  <button (click)="sayHello()">Hello</button>
</div>
```

```mw
/* my-controller.component.ts */
import { GreeterService } from './greeter.service.ts';
import { Component, inject } from '@angular/core';
@Component({
    selector: 'app-my-controller',
    template: 'my-controller.component.html'
})
export class MyControllerComponent {

    private greeter = inject(GreeterService);

    sayHello(): void {
        this.greeter.greet('Hello World');
    }
}
```

The `inject` function triggers the injector to create an instance of the `GreeterService` and its dependencies (in this case, a `Document` instance to access the `window` object).

### C++

This sample provides an example of constructor injection in C++.

```mw
import std;

class DatabaseConnection {
public:
    void connect() {
        std::println("Connecting to database...");
    }
};

class DatabaseService {
private:
    DatabaseConnection& dbConn;
public:
    explicit DatabaseService(DatabaseConnection& db):
        dbConn{db} {}

    void execute() {
        dbConn.connect();
        std::println("Executing database service...");
    }
};

int main(int argc, char* argv[]) {
    DatabaseConnection db;
    DatabaseService sv(db);
    
    sv.execute();
}
```

This sample provides an example of interface injection in C++.

```mw
import std;

using std::expected;
using std::shared_ptr;
using std::unexpected;

enum class DatabaseConnectionError {
    NO_CONNECTION,
    // more errors here
};

class IConnection {
public:
    virtual void connect() = 0;
    virtual ~IConnection() = default;
};

class DatabaseConnection: public IConnection {
public:
    DatabaseConnection() = default;

    void connect() override {
        std::println("Connecting to database...");
    }
};

class DatabaseService {
private:
    shared_ptr<IConnection> conn;
public:
    DatabaseService() = default;

    void setConnection(shared_ptr<IConnection> nextConn) noexcept {
        conn = nextConn;
    }

    expected<void, DatabaseConnectionError> execute() {
        if (conn) {
            conn->connect();
            std::println("Executing database service...");
        } else {
            return unexpected(DatabaseConnectionError::NO_CONNECTION);
        }
    }
};

int main(int argc, char* argv[]) {
    shared_ptr<DatabaseConnection> db = std::make_shared<DatabaseConnection>();
    DatabaseService sv;
    sv.setConnection(db);
    sv.execute();
}
```

### C

This sample provides an example of constructor injection in C#.

```mw
namespace Wikipedia.Examples;

using System;

// Our client will only know about this interface, not which specific gamepad it is using.
interface IGamePadFunctionality 
{
    string GetGamePadName();
    void SetVibrationPower(float power);
}

// The following services provide concrete implementations of the above interface.

class XboxGamePad : IGamePadFunctionality 
{
    float vibrationPower = 1.0f;
    
    public string GetGamePadName() => "Xbox controller";
    
    public void SetVibrationPower(float power) => this.vibrationPower = Math.Clamp(power, 0.0f, 1.0f);
}

class PlayStationJoystick : IGamePadFunctionality 
{
    float vibratingPower = 100.0f;
    
    public string GetGamePadName() => "PlayStation controller";
    
    public void SetVibrationPower(float power) => this.vibratingPower = Math.Clamp(power * 100.0f, 0.0f, 100.0f);
}

class SteamController : IGamePadFunctionality 
{
    double vibrating = 1.0;
    
    public string GetGamePadName() => "Steam controller";
    
    public void SetVibrationPower(float power) => this.vibrating = Convert.ToDouble(Math.Clamp(power, 0.0f, 1.0f));
}

// This class is the client which receives a service.
class GamePad
{
    IGamePadFunctionality gamePadFunctionality;

    // The service is injected through the constructor and stored in the above field.
    public GamePad(IGamePadFunctionality gamePadFunctionality) => this.gamePadFunctionality = gamePadFunctionality;

    public void Showcase() 
    {
        // The injected service is used.
        string gamePadName = this.gamePadFunctionality.GetGamePadName();
        string message = $"We're using the {gamePadName} right now, do you want to change the vibrating power?";
        Console.WriteLine(message);
    }
}

class Program
{
    static void Main(string[] args) 
    {
        SteamController steamController = new();
        
        // We could have also passed in an XboxController, PlayStationJoystick, etc.
        // The gamepad doesn't know what it's using and doesn't need to.
        GamePad gamepad = new(steamController);
        
        gamepad.Showcase();
    }
}
```

### Go

Go does not support classes and usually dependency injection is either abstracted by a dedicated library that utilizes reflection or generics (the latter being supported since Go 1.18). A simpler example without using dependency injection libraries is illustrated by the following example of an MVC web application.

First, pass the necessary dependencies to a router and then from the router to the controllers:

```mw
package router

import (
	"database/sql"
	"net/http"

	"example/controllers/users"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	"github.com/redis/go-redis/v9"
	"github.com/rs/zerolog"
)

type RoutingHandler struct {
	// passing the values by pointer further down the call stack
	// means we won't create a new copy, saving memory
	log    *zerolog.Logger
	db     *sql.DB
	cache  *redis.Client
	router chi.Router
}

// connection, logger and cache initialized usually in the main function
func NewRouter(
	log *zerolog.Logger,
	db *sql.DB,
	cache *redis.Client,
) (r *RoutingHandler) {
	rtr := chi.NewRouter()

	return &RoutingHandler{
		log:    log,
		db:     db,
		cache:  cache,
		router: rtr,
	}
}

func (r *RoutingHandler) SetupUsersRoutes() {
	uc := users.NewController(r.log, r.db, r.cache)

	r.router.Get("/users/:name", func(w http.ResponseWriter, r *http.Request) {
		uc.Get(w, r)
	})
}
```

Then, you can access the private fields of the struct in any method that is its pointer receiver, without violating encapsulation.

```mw
package users

import (
	"database/sql"
	"net/http"

	"example/models"

	"github.com/go-chi/chi/v5"
	"github.com/redis/go-redis/v9"
	"github.com/rs/zerolog"
)

type Controller struct {
	log     *zerolog.Logger
	storage models.UserStorage
	cache   *redis.Client
}

func NewController(log *zerolog.Logger, db *sql.DB, cache *redis.Client) *Controller {
	return &Controller{
		log:     log,
		storage: models.NewUserStorage(db),
		cache:   cache,
	}
}

func (uc *Controller) Get(w http.ResponseWriter, r *http.Request) {
	// note that we can also wrap logging in a middleware, this is for demonstration purposes
	uc.log.Info().Msg("Getting user")

	userParam := chi.URLParam(r, "name")

	var user *models.User
	// get the user from the cache
	err := uc.cache.Get(r.Context(), userParam).Scan(&user)
	if err != nil {
		uc.log.Error().Err(err).Msg("Error getting user from cache. Retrieving from SQL storage")
	}

	user, err = uc.storage.Get(r.Context(), "johndoe")
	if err != nil {
		uc.log.Error().Err(err).Msg("Error getting user from SQL storage")
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}
}
```

Finally you can use the database connection initialized in your main function at the data access layer:

```mw
package models

import (
"database/sql"
"time"
)

type (
	UserStorage struct {
		conn *sql.DB
	}

	User struct {
		Name     string 'json:"name" db:"name,primarykey"'
		JoinedAt time.Time 'json:"joined_at" db:"joined_at"'
		Email    string 'json:"email" db:"email"'
	}
)

func NewUserStorage(conn *sql.DB) *UserStorage {
	return &UserStorage{
		conn: conn,
	}
}

func (us *UserStorage) Get(name string) (user *User, err error) {
	// assuming 'name' is a unique key
	query := "SELECT * FROM users WHERE name = $1"

	if err := us.conn.QueryRow(query, name).Scan(&user); err != nil {
		return nil, err
	}

	return user, nil
}
```
