---
title: "Event store"
source: https://en.wikipedia.org/wiki/Event_store
domain: eventstore-db
license: CC-BY-SA-4.0
tags: eventstoredb, event sourcing database, event stream database, cqrs pattern
fetched: 2026-07-02
---

# Event store

An **event store** is a type of database optimized for storage of events.

Conceptually, an event store records only the *events* affecting an entity, dossier, or policy, and the state of the entity at any point in its history can be reconstructed by *replaying* its contributing events in sequential order. Events (and their corresponding data) are the only "real" facts that should be stored in the database. All other objects can be derived from these events, meaning they are instantiated in memory by runtime code as needed (e.g. for showing in a user interface). In theory, any object that aggregates over recorded event data is *not* stored in the database. Instead these objects are built 'on the fly', by traversing the event history. When the aggregated object instance is no longer needed, it can simply be discarded (released from memory).

## Example with insurance policies

For example, the event store concept of a database can be applied to insurance policies or pension dossiers. In these policies or dossiers the instantiation of each object that make up the dossier or policy (the person, partner(s), employments, etc.) can be derived and can be instantiated in memory based on the real world events.

## Double timeline

A crucial part of an event store database is that each event has a double timeline: This enables event stores to correct errors of events that have been entered into the event store database before.

The two dates are:

- Valid date is the date at which the event has become valid.
- Transaction date is the date at which the event is entered into the database.

## Error correction

Another crucial part of an event store database is that events that are stored are not allowed to be changed. Once stored, also erroneous events are not changed anymore. The only way to change (or better: correct) these events is to instantiate a new event with the new values and using the double timeline. A correcting event would have the new values of the original event, with an event data of that corrected event, but a different transaction date. This mechanism ensures reproducibility at each moment in the time, even in the time period before the correction has taken place. It also allows to reproduce situations based on erroneous events (if required).

## Advantages and disadvantages

One advantage of the event store concept is that handling the effects of back dated events (events that take effect before previous events and that may even invalidate them) is much easier.

An event store will simplify the code in that rolling back erroneous situations and rolling up the new, correct situations is not needed anymore.

Disadvantage may be that the code needs to re-instantiate all objects in memory based on the events each time a service call is received for a specific dossier or policy.

## Compared to regular databases

In regular databases, handling backdated events to correct previous, erroneous events can be painful as it often results in rolling back all previous, erroneous transactions and objects and rolling up the new, correct transactions and objects. In an event store, only the new event (and its corresponding facts) are stored. The code will then redetermine the transactions and objects based on the new facts in memory.
