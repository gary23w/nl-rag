---
title: "Double dispatch"
source: https://en.wikipedia.org/wiki/Double_dispatch
domain: ad-hoc-polymorphism
license: CC-BY-SA-4.0
tags: ad hoc polymorphism, function overloading, type class, operator overloading
fetched: 2026-07-02
---

# Double dispatch

In software engineering, **double dispatch** is a special form of multiple dispatch, and a mechanism that dispatches a function call to different concrete functions depending on the runtime types of two objects involved in the call. In most object-oriented systems, the concrete function that is called from a function call in the code depends on the dynamic type of a single object and therefore they are known as single dispatch calls, or simply virtual function calls.

Dan Ingalls first described how to use double dispatching in Smalltalk, calling it multiple polymorphism.

## Overview

The general problem addressed is how to dispatch a message to different methods depending not only on the receiver but also on the arguments.

To that end, systems like CLOS implement multiple dispatch. Double dispatch is another solution that gradually reduces the polymorphism on systems that do not support multiple dispatch.

## Use cases

Double dispatch is useful in situations where the choice of computation depends on the runtime types of its arguments. For example, a programmer could use double dispatch in the following situations:

- *Sorting a mixed set of objects:* algorithms require that a list of objects be sorted into some canonical order. Deciding if one element comes before another element requires knowledge of both types and possibly some subset of the fields.
- *Adaptive collision algorithms* usually require that collisions between different objects be handled in different ways. A typical example is in a game environment where the collision between a spaceship and an asteroid is computed differently from the collision between a spaceship and a spacestation.
- *Painting algorithms* that require the intersection points of overlapping sprites to be rendered in a different manner.
- *Personnel management* systems may *dispatch* different types of jobs to different personnel. A `schedule` algorithm that is given a person object typed as an accountant and a job object typed as engineering rejects the scheduling of that person for that job.
- *Event handling* systems that use both the event type and the type of the receptor object in order to call the correct event handling routine.
- *Lock and key* systems where there are many types of locks and many types of keys and every type of key opens multiple types of locks. Not only do you need to know the types of the objects involved, but the subset of "information about a particular key that are relevant to seeing if a particular key opens a particular lock" is different between different lock types.

### A common idiom

The common idiom, as in the examples presented above, is that the selection of the appropriate algorithm is based on the call's argument types at runtime. The call is therefore subject to all the usual additional performance costs that are associated with dynamic resolution of calls, usually more than in a language supporting only single method dispatch. In C++, for example, a dynamic function call is usually resolved by a *single* offset calculation - which is possible because the compiler knows the location of the function in the object's method table and so can statically calculate the offset. In a language supporting *double* dispatch, this is slightly more costly, because the compiler must generate code to calculate the method's offset in the method table at runtime, thereby increasing the overall instruction path length (by an amount that is likely to be no more than the total number of calls to the function, which may not be very significant).

## Examples

### Ruby

A common use case is displaying an object on a display port which can be a screen or a printer, or something else entirely that doesn't exist yet. This is a naive implementation of how to deal with those different media.

```mw
class Rectangle
  def display_on(port)
    # selects the right code based on the object class
    case port
      when DisplayPort
        # code for displaying on DisplayPort
      when PrinterPort
        # code for displaying on PrinterPort
      when RemotePort
        # code for displaying on RemotePort
    end
  end
end
```

The same would need to be written for Oval, Triangle and any other object that wants to display itself on a medium, and all would need to be rewritten if a new type of port were to be created. The problem is that more than one degree of polymorphism exist: one for dispatching the display_on method to an object and another for selecting the right code (or method) for displaying.

A much cleaner and more maintainable solution is then to do a second dispatch, this time for selecting the right method for displaying the object on the medium:

```mw
class Rectangle
  def display_on(port)
    # second dispatch
    port.display_rectangle(self)
  end
end

class Oval
  def display_on(port)
    # second dispatch
    port.display_oval(self)
  end
end

class DisplayPort
  def display_rectangle(object)
    # code for displaying a rectangle on a DisplayPort
  end
  def display_oval(object)
    # code for displaying an oval on a DisplayPort
  end
  # ...
end

class PrinterPort
  def display_rectangle(object)
    # code for displaying a rectangle on a PrinterPort
  end
  def display_oval(object)
    # code for displaying an oval on a PrinterPort
  end
  # ...
end
```

### C++

At first glance, double dispatch appears to be a natural result of function overloading. Function overloading allows the function called to depend on the type of the argument. Function overloading, however, is done at compile time using "name mangling" where the internal name of the function encodes the argument's type. For example, a function `foo(int)` may internally be called *__foo_i* and the function `foo(double)` may be called *__foo_d*. Thus, there is no name collision, and no virtual table lookup. By contrast, dynamic dispatch is based on the type of the calling object, meaning it uses virtual functions (overriding) instead of function overloading, and does result in a vtable lookup. Consider the following example, written in C++, of collisions in a game:

```mw
class Spaceship {};
class ApolloSpacecraft : public Spaceship {};

class Asteroid {
public:
    virtual void collideWith(Spaceship&) {
        std::println("Asteroid hit a Spaceship");
    }

    virtual void collideWith(ApolloSpacecraft&) {
        std::println("Asteroid hit an ApolloSpacecraft");
    }
};

class ExplodingAsteroid : public Asteroid {
public:
    void collideWith(Spaceship&) override {
        std::println("ExplodingAsteroid hit a Spaceship");
    }

    void collideWith(ApolloSpacecraft&) override {
        std::println("ExplodingAsteroid hit an ApolloSpacecraft");
    }
};
```

If you have:

```mw
Asteroid asteroid;
Spaceship spaceship;
ApolloSpacecraft apolloSpacecraft;
```

then, because of function overloading,

```mw
asteroid.collideWith(spaceship); 
asteroid.collideWith(apolloSpacecraft);
```

will print, respectively, `Asteroid hit a Spaceship` and `Asteroid hit an ApolloSpacecraft`, without using any dynamic dispatch. Furthermore:

```mw
ExplodingAsteroid explodingAsteroid;
explodingAsteroid.collideWith(spaceship); 
explodingAsteroid.collideWith(apolloSpacecraft);
```

will print `ExplodingAsteroid hit a Spaceship` and `ExplodingAsteroid hit an ApolloSpacecraft` respectively, again without dynamic dispatch.

With a reference to an `Asteroid`, dynamic dispatch is used, and this code:

```mw
Asteroid& asteroidRef = explodingAsteroid;
asteroidRef.collideWith(spaceship); 
asteroidRef.collideWith(apolloSpacecraft);
```

prints `ExplodingAsteroid hit a Spaceship` and `ExplodingAsteroid hit an ApolloSpacecraft`, again as expected. However, the following code does not work as desired:

```mw
Spaceship& spaceshipRef = apolloSpacecraft;
asteroid.collideWith(spaceshipRef);
asteroidRef.collideWith(spaceshipRef);
```

The desired behaviour is to bind these calls to the function that takes `apolloSpacecraft` as its argument, as that is the instantiated type of the variable, meaning the expected output would be `Asteroid hit an ApolloSpacecraft` and `ExplodingAsteroid hit an ApolloSpacecraft`. However, the output is actually `Asteroid hit a Spaceship` and `ExplodingAsteroid hit a Spaceship`. The problem is that, while virtual functions are dispatched dynamically in C++, function overloading is done statically.

The problem described above can be resolved by simulating double dispatch, for example by using a visitor pattern. Suppose the existing code is extended so that both `Spaceship` and `ApolloSpacecraft` are given the function

```mw
virtual void collideWith(Asteroid& asteroid) {
    asteroid.collideWith(*this);
}
```

Then, while the previous example still does not work correctly, reframing the calls so that the spaceship is the agent gives us the desired behaviour:

```mw
Spaceship& spaceshipRef = apolloSpacecraft;
Asteroid& asteroidRef = explodingAsteroid;
spaceshipRef.collideWith(asteroid);
spaceshipRef.collideWith(asteroidRef);
```

It prints out `Asteroid hit an ApolloSpacecraft` and `ExplodingAsteroid hit an ApolloSpacecraft`, as expected. The key is that `spaceshipRef.collideWith(asteroidRef);` does the following at run time:

1. `spaceshipRef` is a reference, so C++ looks up the correct method in the vtable. In this case, it will call `ApolloSpacecraft::collideWith(Asteroid&)`.
2. Within `ApolloSpacecraft::collideWith(Asteroid&)`, `asteroid` is a reference, so `asteroid.collideWith(*this)` will result in *another vtable lookup*. In this case, `asteroid` is a reference to an `ExplodingAsteroid` so `ExplodingAsteroid::collideWith(ApolloSpacecraft&)` will be called.

### C

In C#, when calling an instance method accepting an argument, multiple dispatch can be achieved without employing the visitor pattern. This is done by using traditional polymorphism while also casting the argument to *dynamic*. The run-time binder will choose the appropriate method overload at run-time. This decision will take into consideration the run-time type of the object instance (polymorphism) as well as the run-time type of the argument.

### Eiffel

The Eiffel programming language can bring the concept of agents to bear on the double-dispatch problem. The example below applies the agent language construct to the double-dispatch problem.

Consider a problem domain with various forms of SHAPE and of drawing SURFACE upon which to draw a SHAPE. Both SHAPE and SURFACE know about a function called `draw' in themselves, but not in each other. We want objects of the two types to co-variantly interact with each other in a double-dispatch using a visitor pattern.

The challenge is to get a polymorphic SURFACE to draw a polymorphic SHAPE on itself.

#### Output

The output example below shows the results of two SURFACE visitor objects being polymorphically passed over a list of polymorphic SHAPE objects. The visitor code pattern is only aware of SHAPE and SURFACE generically and not of the specific type of either. Instead, the code relies on run-time polymorphism and the mechanics of agents to achieve a highly flexible co-variant relationship between these two deferred classes and their descendants.

```
draw a red POLYGON on ETCHASKETCH
draw a red POLYGON on GRAFFITI_WALL
draw a grey RECTANGLE on ETCHASKETCH
draw a grey RECTANGLE on GRAFFITI_WALL
draw a green QUADRILATERAL on ETCHASKETCH
draw a green QUADRILATERAL on GRAFFITI_WALL
draw a blue PARALLELOGRAM on ETCHASKETCH
draw a blue PARALLELOGRAM on GRAFFITI_WALL
draw a yellow POLYGON on ETCHASKETCH
draw a yellow POLYGON on GRAFFITI_WALL
draw a purple RECTANGLE on ETCHASKETCH
draw a purple RECTANGLE on GRAFFITI_WALL
```

#### Setup

Before looking at SHAPE or SURFACE, we need to examine the high level decoupled use of our double-dispatch.

##### Visitor pattern

The visitor pattern works by way of a visitor object visiting the elements of a data structure (e.g. list, tree and so on) polymorphically, applying some action (call or agent) against the polymorphic element objects in the visited target structure.

In our example below, we make a list of polymorphic SHAPE objects, visiting each of them with a polymorphic SURFACE, asking the SHAPE to be drawn on the SURFACE.

```mw
	make
			-- Print shapes on surfaces.
		local
			l_shapes: ARRAYED_LIST [SHAPE]
			l_surfaces: ARRAYED_LIST [SURFACE]
		do
			create l_shapes.make (6)
			l_shapes.extend (create {POLYGON}.make_with_color ("red"))
			l_shapes.extend (create {RECTANGLE}.make_with_color ("grey"))
			l_shapes.extend (create {QUADRILATERAL}.make_with_color ("green"))
			l_shapes.extend (create {PARALLELOGRAM}.make_with_color ("blue"))
			l_shapes.extend (create {POLYGON}.make_with_color ("yellow"))
			l_shapes.extend (create {RECTANGLE}.make_with_color ("purple"))

			create l_surfaces.make (2)
			l_surfaces.extend (create {ETCHASKETCH}.make)
			l_surfaces.extend (create {GRAFFITI_WALL}.make)

			across l_shapes as ic_shapes loop
				across l_surfaces as ic_surfaces loop
					ic_surfaces.item.drawing_agent (ic_shapes.item.drawing_data_agent)
				end
			end
		end
```

We start by creating a collection of SHAPE and SURFACE objects. We then iterate over one of the lists (SHAPE), allowing elements of the other (SURFACE) to visit each of them in turn. In the example code above, SURFACE objects are visiting SHAPE objects.

The code makes a polymorphic call on {SURFACE}.draw indirectly by way of the `drawing_agent', which is the first call (dispatch) of the double-dispatch pattern. It passes an indirect and polymorphic agent (`drawing_data_agent'), allowing our visitor code to only know about two things:

- What is the drawing agent of the surface (e.g. al_surface.drawing_agent on line #21)?
- What is the drawing data agent of the shape (e.g. al_shape.drawing_data_agent on line #21)?

Because both SURFACE and SHAPE define their own agents, our visitor code is freed from having to know what is the appropriate call to make, polymorphically or otherwise. This level of indirection and decoupling is simply not achievable in other common languages like C, C++ and Java except through either some form of reflection or feature overloading with signature matching.

##### SURFACE

Within the polymorphic call to {SURFACE}.draw is the call to an agent, which becomes the second polymorphic call or dispatch in the double-dispatch pattern.

```mw
	deferred class
		SURFACE
	
	feature {NONE} -- Initialization
	
		make
				-- Initialize Current.
			do
				drawing_agent := agent draw
			end
	
	feature -- Access

		drawing_agent: PROCEDURE [ANY, TUPLE [STRING, STRING]]
				-- Drawing agent of Current.
	
	feature {NONE} -- Implementation
	
		draw (a_data_agent: FUNCTION [ANY, TUPLE, TUPLE [name, color: STRING]])
				-- Draw `a_shape' on Current.
			local
				l_result: TUPLE [name, color: STRING]
			do
				l_result := a_data_agent (Void)
				print ("draw a " + l_result.color + " " + l_result.name + " on " + type + "%N")
			end
	
		type: STRING
				-- Type name of Current.
			deferred end
	
	end
```

The agent argument in line #19 and call in line #24 are both polymorphic and decoupled. The agent is decoupled because the {SURFACE}.draw feature has no idea what class `a_data_agent' is based on. There is no way to tell what class the operation agent was derived from, so it does not have to come from SHAPE or one of its descendants. This is a distinct advantage of Eiffel agents over the single inheritance, dynamic and polymorphic binding of other languages.

The agent is dynamically polymorphic at run-time because the object is created in the moment it is needed, dynamically, where the version of the objectified routine is determined at that time. The only strongly bound knowledge is of the Result type of the agent signature—that is—a named TUPLE with two elements. However, this specific requirement is based on a demand of the enclosing feature (e.g. line #25 uses the named elements of the TUPLE to fulfill `draw' feature of SURFACE), which is necessary and has not been avoided (and perhaps cannot be).

Finally, note how only the `drawing_agent' feature is exported to ANY client! This means that the visitor pattern code (who is the ONLY client of this class) only needs to know about the agent to get its job done (e.g. using the agent as the feature applied to the visited objects).

##### SHAPE

The SHAPE class has the basis (e.g. drawing data) for what is drawn, perhaps on a SURFACE, but it does not have to be. Again, the agents provide the indirection and class agnostics required to make the co-variant relationship with SHAPE as decoupled as possible.

Additionally, please take note of the fact that SHAPE only provides `drawing_data_agent' as a fully exported feature to any client. Therefore, the only way to interact with SHAPE, other than creation, is through the facilities of the `drawing_data_agent', which is used by ANY client to indirectly and polymorphically gather drawing data for the SHAPE!

```mw
	deferred class
		SHAPE
	
	feature {NONE} -- Initialization
	
		make_with_color (a_color: like color)
				-- Make with `a_color' as `color'.
			do
				color := a_color
				drawing_data_agent := agent drawing_data
			ensure
				color_set: color.same_string (a_color)
			end

	feature -- Access
	
		drawing_data_agent: FUNCTION [ANY, TUPLE, like drawing_data]
				-- Data agent for drawing.
	
	feature {NONE} -- Implementation
	
		drawing_data: TUPLE [name: like name; color: like color]
				-- Data needed for drawing of Current.
			do
				Result := [name, color]
			end
	
		name: STRING
				-- Object name of Current.
			deferred end
	
		color: STRING
				-- Color of Current.

	end
```

#### Classic Spaceship example

A variation of the classic Spaceship example has one or more spaceship objects roaming about a universe filled with other items like rogue asteroids and space stations. What we want is a double-dispatch method for handling encounters (e.g. possible collisions) between two co-variant objects in our make-believe universe. In our example below, the output excursion of our USS Enterprise and USS Excelsior will be:

```mw
Starship Enterprise changes position from A-001 to A-002.
Starship Enterprise takes evasive action, avoiding Asteroid `Rogue 1'!
Starship Enterprise changes position from A-002 to A-003.
Starship Enterprise takes evasive action, avoiding Asteroid `Rogue 2'!
Starship Enterprise beams a science team to Starship Excelsior as they pass!
Starship Enterprise changes position from A-003 to A-004.
Starship Excelsior changes position from A-003 to A-005.
Starship Enterprise takes evasive action, avoiding Asteroid `Rogue 3'!
Starship Excelsior is near Space Station Deep Space 9 and is dockable.
Starship Enterprise changes position from A-004 to A-005.
Starship Enterprise beams a science team to Starship Excelsior as they pass!
Starship Enterprise is near Space Station Deep Space 9 and is dockable.
```

##### Visitor

The visitor for the classic Spaceship example also has a double-dispatch mechanism.

```mw
make
		-- Allow SPACESHIP objects to visit and move about in a universe.
	local
		l_universe: ARRAYED_LIST [SPACE_OBJECT]
		l_enterprise,
		l_excelsior: SPACESHIP
	do
		create l_enterprise.make_with_name ("Enterprise", "A-001")
		create l_excelsior.make_with_name ("Excelsior", "A-003")
		create l_universe.make (0)
		l_universe.force (l_enterprise)
		l_universe.force (create {ASTEROID}.make_with_name ("Rogue 1", "A-002"))
		l_universe.force (create {ASTEROID}.make_with_name ("Rogue 2", "A-003"))
		l_universe.force (l_excelsior)
		l_universe.force (create {ASTEROID}.make_with_name ("Rogue 3", "A-004"))
		l_universe.force (create {SPACESTATION}.make_with_name ("Deep Space 9", "A-005"))
		visit (l_enterprise, l_universe)
		l_enterprise.set_position ("A-002")
		visit (l_enterprise, l_universe)
		l_enterprise.set_position ("A-003")
		visit (l_enterprise, l_universe)
		l_enterprise.set_position ("A-004")
		l_excelsior.set_position ("A-005")
		visit (l_enterprise, l_universe)
		visit (l_excelsior, l_universe)
		l_enterprise.set_position ("A-005")
		visit (l_enterprise, l_universe)
	end
feature {NONE} -- Implementation
visit (a_object: SPACE_OBJECT; a_universe: ARRAYED_LIST [SPACE_OBJECT])
		-- `a_object' visits `a_universe'.
	do
		across a_universe as ic_universe loop
			check attached {SPACE_OBJECT} ic_universe.item as al_universe_object then
				a_object.encounter_agent.call ([al_universe_object.sensor_data_agent])
			end
		end
	end
```

The double-dispatch can be seen in line #35, where two indirect agents are working together to provide two co-variant calls working in perfect polymorphic concert with each other. The `a_object' of the `visit' feature has an `encounter_agent' which is called with the sensor data of the `sensor_data_agent' coming from the `al_universe_object'. The other interesting part of this particular example is the SPACE_OBJECT class and its `encounter' feature:

##### Visitor action

The only exported features of a SPACE_OBJECT are the agents for encounter and sensor data, as well as the capacity to set a new position. As one object (the spaceship) visits each object in the universe, the sensor data is collected and passed to the visiting object in its encounter agent. There, the sensor data from the sensor_data_agent (that is—the data element items of the sensor_data TUPLE as returned by the sensor_data_agent query) are evaluated against the current object and a course of action is taken based on that evaluation (see `encounter' in SPACE_OBJECT below). All other data is exported to {NONE}. This is similar to C, C++ and Java scopes of Private. As non-exported features, the data and routines are used only internally by each SPACE_OBJECT. Finally, note that encounter calls to `print' do not include specific information about possible descendant classes of SPACE_OBJECT! The only thing found at this level in the inheritance are general relational aspects based completely on what can be known from the attributes and routines of a general SPACE_OBJECT. The fact that the output of the `print' makes sense to us, as human beings, based on what we know or imagine about Star ships, space stations and asteroids is merely logical planning or coincidence. The SPACE_OBJECT is not programmed with any specific knowledge of its descendants.

```mw
deferred class
SPACE_OBJECT
feature {NONE} -- Initialization
make_with_name (a_name: like name; a_position: like position)
    -- Initialize Current with `a_name' and `a_position'.
  do
    name := a_name
    position := a_position
    sensor_data_agent := agent sensor_data
    encounter_agent := agent encounter
  ensure
    name_set: name.same_string (a_name)
    position_set: position.same_string (a_position)
  end
feature -- Access
encounter_agent: PROCEDURE [ANY, TUPLE]
    -- Agent for managing encounters with Current.
sensor_data_agent: FUNCTION [ANY, TUPLE, attached like sensor_data_anchor]
    -- Agent for returning sensor data of Current.
feature -- Settings
set_position (a_position: like position)
    -- Set `position' with `a_position'.
  do
    print (type + " " + name + " changes position from " + position + " to " + a_position + ".%N")
    position := a_position
  ensure
    position_set: position.same_string (a_position)
  end
feature {NONE} -- Implementation
encounter (a_sensor_agent: FUNCTION [ANY, TUPLE, attached like sensor_data_anchor])
    -- Detect and report on collision status of Current with `a_radar_agent'.
  do
    a_sensor_agent.call ([Void])
    check attached {like sensor_data_anchor} a_sensor_agent.last_result as al_sensor_data then
      if not name.same_string (al_sensor_data.name) then
        if (position.same_string (al_sensor_data.position)) then
          if ((al_sensor_data.is_dockable and is_dockable) and
              (is_manned and al_sensor_data.is_manned) and
              (is_maneuverable and al_sensor_data.is_not_maneuverable)) then
            print (type + " " + name + " is near " + al_sensor_data.type + " " +
                al_sensor_data.name + " and is dockable.%N")
          elseif ((is_dockable and al_sensor_data.is_dockable) and
                (is_manned and al_sensor_data.is_manned) and
                (is_maneuverable and al_sensor_data.is_maneuverable)) then
            print (type + " " + name + " beams a science team to " + al_sensor_data.type + " " +
                al_sensor_data.name + " as they pass!%N")
          elseif (is_manned and al_sensor_data.is_not_manned) then
            print (type + " " + name + " takes evasive action, avoiding " +
                al_sensor_data.type + " `" + al_sensor_data.name + "'!%N")
          end
        end
      end
    end
  end
name: STRING
    -- Name of Current.
type: STRING
    -- Type of Current.
  deferred
  end
position: STRING
    -- Position of Current.
is_dockable: BOOLEAN
    -- Is Current dockable with another manned object?
  deferred
  end
is_manned: BOOLEAN
    -- Is Current a manned object?
  deferred
  end
is_maneuverable: BOOLEAN
    -- Is Current capable of being moved?
  deferred
  end
sensor_data: attached like sensor_data_anchor
    -- Sensor data of Current.
  do
      Result := [name, type, position, is_dockable, not is_dockable, is_manned, not is_manned, is_maneuverable, not is_maneuverable]
    end

  sensor_data_anchor: detachable TUPLE [name, type, position: STRING; is_dockable, is_not_dockable, is_manned, is_not_manned, is_maneuverable, is_not_maneuverable: BOOLEAN]
      -- Sensor data type anchor of Current.

end
```

There are three descendant classes of SPACE_OBJECT:

```mw
SPACE_OBJECT
ASTEROID
SPACESHIP
SPACESTATION
```

In our example, the ASTEROID class is used for the `Rogue' items, SPACESHIP for the two star ships and SPACESTATION for Deep Space Nine. In each class, the only specialization is the setting of the `type' feature and of certain properties of the object. The `name' is supplied in the creation routine as well as the `position'. For example: Below is the SPACESHIP example.

```mw
class
SPACESHIP
inherit
SPACE_OBJECT
create
make_with_name
feature {NONE} -- Implementation
type: STRING = "Starship"
  -- <Precursor>
is_dockable: BOOLEAN = True
  -- <Precursor>
is_manned: BOOLEAN = True
  -- <Precursor>
is_maneuverable: BOOLEAN = True
  -- <Precursor>
end
```

So, any SPACESHIP in our universe is dock-able, manned and maneuverable. Other objects, like Asteroids are none of these things. A SPACESTATION, on the other hand, is both dock-able and manned, but is not maneuverable. Thus, when one object has an encounter with another, it first checks to see if the positions put them in the vicinity of each other and if they are, then the objects interact based upon their basic properties. Note that objects with the same type and name are considered to the same object, so an interaction is logically disallowed.

#### Conclusion

With regards to double-dispatch, Eiffel allows the designer and programmer to further remove a level of direct object-to-object knowledge by decoupling class routines from their classes by way of making them agents and then passing those agents instead of making direct object feature calls. The agents also have specific signatures and possible results (in the case of queries), making them ideal static type checking vehicles without giving up specific object details. The agents are fully polymorphic so that the resulting code has only the specific knowledge required to get its local job done. Otherwise, there is no maintenance burden added by having specific internal class feature knowledge spread around many co-variant objects. The use and mechanics of agents ensure this. One possible downside of the use of agents is that an agent is computationally more expensive than its direct call counterpart. With this in mind, one ought never to presume the use of agents in the double-dispatch and their application in visitor patterns. If one can clearly see a design limit as to the domain of class types that will be involved in the co-variant interactions, then a direct call is the more efficient solution in terms of computational expense. However, if the class domain of participating types is expected to grow or differ substantially, then agents present an excellent solution to lessening the maintenance burden in the double-dispatch pattern.
