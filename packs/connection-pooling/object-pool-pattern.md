---
title: "Object pool pattern"
source: https://en.wikipedia.org/wiki/Object_pool_pattern
domain: connection-pooling
license: CC-BY-SA-4.0
tags: connection pooling, database connection, object pool pattern, connection reuse
fetched: 2026-07-02
---

# Object pool pattern

The **object pool pattern** is a software creational design pattern that uses a set of initialized objects kept ready to use – a "pool" – rather than allocating and destroying them on demand. A client of the pool will request an object from the pool and perform operations on the returned object. When the client has finished, it returns the object to the pool rather than destroying it; this can be done manually or automatically.

Object pools are primarily used for performance: in some circumstances, object pools significantly improve performance. Object pools complicate object lifetime, as objects obtained from and returned to a pool are not actually created or destroyed at this time, and thus require care in implementation.

## Description

When it is necessary to work with numerous objects that are particularly expensive to instantiate and each object is only needed for a short period of time, the performance of an entire application may be adversely affected. An object pool design pattern may be deemed desirable in cases such as these.

The object pool design pattern creates a set of objects that may be reused. When a new object is needed, it is requested from the pool. If a previously prepared object is available, it is returned immediately, avoiding the instantiation cost. If no objects are present in the pool, a new item is created and returned. When the object has been used and is no longer needed, it is returned to the pool, allowing it to be used again in the future without repeating the computationally expensive instantiation process. Once an object has been used and returned, existing references become invalid.

In some object pools the resources are limited, so a maximum number of objects is specified. If this number is reached and a new item is requested, an exception may be thrown, or the thread will be blocked until an object is released back into the pool.

The object pool design pattern is used in several places in the standard classes of the .NET Framework. One example is the .NET Framework Data Provider for SQL Server. As SQL Server database connections can be slow to create, a pool of connections is maintained. Closing a connection does not actually relinquish the link to SQL Server. Instead, the connection is held in a pool, from which it can be retrieved when requesting a new connection. This substantially increases the speed of making connections.

## Benefits

Object pooling can offer a significant performance boost in situations where the cost of initializing a class instance is high and the rate of instantiation and destruction of a class is high – in this case objects can frequently be reused, and each reuse saves a significant amount of time. Object pooling requires resources – memory and possibly other resources, such as network sockets, and thus it is preferable that the number of instances in use at any one time is low, but this is not required.

The pooled object is obtained in predictable time when creation of the new objects (especially over network) may take variable time. These benefits are mostly true for objects that are expensive with respect to time, such as database connections, socket connections, threads and large graphic objects like fonts or bitmaps.

In other situations, simple object pooling (that hold no external resources, but only occupy memory) may not be efficient and could decrease performance. In case of simple memory pooling, the slab allocation memory management technique is more suited, as the only goal is to minimize the cost of memory allocation and deallocation by reducing fragmentation.

## Implementation

Object pools can be implemented in an automated fashion in languages like C++ via smart pointers. In the constructor of the smart pointer, an object can be requested from the pool, and in the destructor of the smart pointer, the object can be released back to the pool. In garbage-collected languages, where there are no destructors (which are guaranteed to be called as part of a stack unwind), object pools *must* be implemented manually, by explicitly requesting an object from the factory and returning the object by calling a dispose method (as in the dispose pattern). Using a finalizer to do this is not a good idea, as there are usually no guarantees on when (or if) the finalizer will be run. Instead, "try ... finally" should be used to ensure that getting and releasing the object is exception-neutral.

Manual object pools are simple to implement, but harder to use, as they require manual memory management of pool objects.

## Handling of empty pools

Object pools employ one of three strategies to handle a request when there are no spare objects in the pool.

1. Fail to provide an object (and return an error to the client).
2. Allocate a new object, thus increasing the size of the pool. Pools that do this usually allow you to set the high water mark (the maximum number of objects ever used).
3. In a multithreaded environment, a pool may block the client until another thread returns an object to the pool.

## Pitfalls

Care must be taken to ensure the state of the objects returned to the pool is reset back to a sensible state for the next use of the object, otherwise the object may be in a state unexpected by the client, which may cause it to fail. The pool is responsible for resetting the objects, not the clients. Object pools full of objects with dangerously stale state are sometimes called object cesspools and regarded as an anti-pattern.

Stale state may not always be an issue; it becomes dangerous when it causes the object to behave unexpectedly. For example, an object representing authentication details may fail if the "successfully authenticated" flag is not reset before it is reused, since it indicates that a user is authenticated (possibly as someone else) when they are not. However, failing to reset a value used only for debugging, such as the identity of the last authentication server used, may pose no issues.

Inadequate resetting of objects can cause information leaks. Objects containing confidential data (e.g. a user's credit card numbers) must be cleared before being passed to new clients, otherwise, the data may be disclosed to an unauthorized party.

If the pool is used by multiple threads, it may need the means to prevent parallel threads from trying to reuse the same object in parallel. This is not necessary if the pooled objects are immutable or otherwise thread-safe.

## Criticism

Some publications do not recommend using object pooling with certain languages, such as Java, especially for objects that only use memory and hold no external resources (such as connections to database). Opponents usually say that object allocation is relatively fast in modern languages with garbage collectors; while the operator `new` needs only ten instructions, the classic `new` - `delete` pair found in pooling designs requires hundreds of them as it does more complex work. Also, most garbage collectors scan "live" object references, and not the memory that these objects use for their content. This means that any number of "dead" objects without references can be discarded with little cost. In contrast, keeping a large number of "live" but unused objects increases the duration of garbage collection.

## Examples

### C++

In C++26, the C++ Standard Library introduces a new header `<hive>` with the data structure `std::hive`, which essentially implements an object pool. It is a collection that reuses erased elements' memory. Along with it is a class `std::hive_limits` for layout information on block capacity limits. It is itself based on the class `plf::colony` from the `plf` library.

```mw
import std;

using std::hive;
using std::plus;
using std::ranges::iota_view;

int main(int argc, char* argv[]) {
    hive<int> intHive;

    // Insert 100 ints:
    for (int i: iota_view(0, 100)) {
        intHive.insert(i);
    }

    // Erase half of them:
    for (int i: intHive) {
        intHive.erase(i);
    }

    int total = std::ranges::fold_left(intHive, 0, plus<int>());
    std::println("Total of all elements: {}", total);

    return 0;
}
```

### C

In the .NET Base Class Library there are a few objects that implement this pattern. `System.Threading.ThreadPool` is configured to have a predefined number of threads to allocate. When the threads are returned, they are available for another computation. Thus, one can use threads without paying the cost of creation and disposal of threads.

The following shows the basic code of the object pool design pattern implemented using C#. Pool is shown as a static class, as it's unusual for multiple pools to be required. However, it's equally acceptable to use instance classes for object pools.

```mw
namespace Wikipedia.Examples;

using System;
using System.Collections.Generic;

// The PooledObject class is the type that is expensive or slow to instantiate,
// or that has limited availability, so is to be held in the object pool.
public class PooledObject
{
    private DateTime _createdAt = DateTime.Now;

    public DateTime CreatedAt => _createdAt;

    public string TempData { get; set; }
}

// The Pool class controls access to the pooled objects. It maintains a list of available objects and a 
// collection of objects that have been obtained from the pool and are in use. The pool ensures that released objects 
// are returned to a suitable state, ready for reuse. 
public static class Pool
{
    private static List<PooledObject> _available = new();
    private static List<PooledObject> _inUse = new();

    public static PooledObject GetObject()
    {
        lock (_available)
        {
            if (_available.Count != 0)
            {
                PooledObject po = _available[0];
                _inUse.Add(po);
                _available.RemoveAt(0);
                return po;
            }
            else
            {
                PooledObject po = new();
                _inUse.Add(po);
                return po;
            }
        }
    }

    public static void ReleaseObject(PooledObject po)
    {
        CleanUp(po);

        lock (_available)
        {
            _available.Add(po);
            _inUse.Remove(po);
        }
    }

    private static void CleanUp(PooledObject po)
    {
        po.TempData = null;
    }
}
```

In the code above, the PooledObject has properties for the time it was created, and another, that can be modified by the client, that is reset when the PooledObject is released back to the pool. Shown is the clean-up process, on release of an object, ensuring it is in a valid state before it can be requested from the pool again.

### Go

The following Go code initializes a resource pool of a specified size (concurrent initialization) to avoid resource race issues through channels, and in the case of an empty pool, sets timeout processing to prevent clients from waiting too long.

```mw
// package pool
package pool

import (
	"errors"
	"log"
	"math/rand"
	"sync"
	"time"
)

const getResMaxTime = 3 * time.Second

var (
	ErrPoolNotExist  = errors.New("pool not exist")
	ErrGetResTimeout = errors.New("get resource time out")
)

//Resource
type Resource struct {
	resId int
}

// NewResource Simulate slow resource initialization creation
// (e.g., TCP connection, SSL symmetric key acquisition, auth authentication are time-consuming)
func NewResource(id int) *Resource {
	time.Sleep(500 * time.Millisecond)
	return &Resource{resId: id}
}

// Do Simulation resources are time consuming and random consumption is 0~400ms
func (r *Resource) Do(workId int) {
	time.Sleep(time.Duration(rand.Intn(5)) * 100 * time.Millisecond)
	log.Printf("using resource #%d finished work %d finish\n", r.resId, workId)
}

// Pool based on Go channel implementation, to avoid resource race state problem
type Pool chan *Resource

// New a resource pool of the specified size
// Resources are created concurrently to save resource initialization time
func New(size int) Pool {
	p := make(Pool, size)
	wg := new(sync.WaitGroup)
	wg.Add(size)
	for i := 0; i < size; i++ {
		go func(resId int) {
			p <- NewResource(resId)
			wg.Done()
		}(i)
	}
	wg.Wait()
	return p
}

// GetResource based on channel, resource race state is avoided and resource acquisition timeout is set for empty pool
func (p Pool) GetResource() (r *Resource, err error) {
	select {
	case r := <-p:
		return r, nil
	case <-time.After(getResMaxTime):
		return nil, ErrGetResTimeout
	}
}

// GiveBackResource returns resources to the resource pool
func (p Pool) GiveBackResource(r *Resource) error {
	if p == nil {
		return ErrPoolNotExist
	}
	p <- r
	return nil
}

// package main
package main

import (
	"github.com/tkstorm/go-design/creational/object-pool/pool"
	"log"
	"sync"
)

func main() {
	// Initialize a pool of five resources,
	// which can be adjusted to 1 or 10 to see the difference
	size := 5
	p := pool.New(size)

	// Invokes a resource to do the id job
	doWork := func(workId int, wg *sync.WaitGroup) {
		defer wg.Done()
		// Get the resource from the resource pool
		res, err := p.GetResource()
		if err != nil {
			log.Println(err)
			return
		}
		// Resources to return
		defer p.GiveBackResource(res)
		// Use resources to handle work
		res.Do(workId)
	}

	// Simulate 100 concurrent processes to get resources from the asset pool
	num := 100
	wg := new(sync.WaitGroup)
	wg.Add(num)
	for i := 0; i < num; i++ {
		go doWork(i, wg)
	}
	wg.Wait()
}
```

### Java

Java supports thread pooling via `java.util.concurrent.ExecutorService` and other related classes. The executor service has a certain number of "basic" threads that are never discarded. If all threads are busy, the service allocates the allowed number of extra threads that are later discarded if not used for the certain expiration time. If no more threads are allowed, the tasks can be placed in the queue. Finally, if this queue may get too long, it can be configured to suspend the requesting thread.

In PooledObject.java:

```mw
package org.wikipedia.examples;

public class PooledObject {
	private String temp1;
	private String temp2;
	private String temp3;
	
	public String getTemp1() {
		return temp1;
	}

	public void setTemp1(String temp1) {
		this.temp1 = temp1;
	}

	public String getTemp2() {
		return temp2;
	}

	public void setTemp2(String temp2) {
		this.temp2 = temp2;
	}

	public String getTemp3() {
		return temp3;
	}

	public void setTemp3(String temp3) {
		this.temp3 = temp3;
	}
}
```

In PooledObjectPool.java:

```mw
package org.wikipedia.examples;

import java.util.HashMap;
import java.util.Map;

public class PooledObjectPool {
	public static final long EXPIRY_TIME = 6000; // 6 seconds

	private static Map<PooledObject, Long> available = new HashMap<>();
	private static Map<PooledObject, Long> inUse = new HashMap<>();
	
	public synchronized static PooledObject getObject() {
		long now = System.currentTimeMillis();
		if (!available.isEmpty()) {
			for (Map.Entry<PooledObject, Long> entry : available.entrySet()) {
				if (now - entry.getValue() > EXPIRY_TIME) {
                    // object has expired
					popElement(available);
				} else {
					PooledObject po = popElement(available, entry.getKey());
					push(inUse, po, now); 
					return po;
				}
			}
		}

		// either no PooledObject is available or each has expired, so return a new one
		return createPooledObject(now);
	}	
	
	private synchronized static PooledObject createPooledObject(long now) {
		PooledObject po = new PooledObject();
		push(inUse, po, now);
		return po;
    }

	private synchronized static void push(HashMap<PooledObject, Long> map, PooledObject po, long now) {
		map.put(po, now);
	}

	public static void releaseObject(PooledObject po) {
		cleanUp(po);
		available.put(po, System.currentTimeMillis());
		inUse.remove(po);
	}
	
	private static PooledObject popElement(HashMap<PooledObject, Long> map) {
		 Map.Entry<PooledObject, Long> entry = map.entrySet().iterator().next();
		 PooledObject key = entry.getKey();
		 // Long value = entry.getValue();
		 map.remove(entry.getKey());
		 return key;
	}
	
	private static PooledObject popElement(HashMap<PooledObject, Long> map, PooledObject key) {
		map.remove(key);
		return key;
	}
	
	public static void cleanUp(PooledObject po) {
		po.setTemp1(null);
		po.setTemp2(null);
		po.setTemp3(null);
	}
}
```

### Rust

There is a Rust crate called *colony* which is based on `std::hive` (or `plf::colony`) from C++. It has no longer been maintained since January 2024.

```mw
use colony::Colony;

fn main() {
    let mut colony: Colony = Colony::new();

    // Insert
    let foo_handle = colony.insert("foo");
    let bar_handle = colony.insert("bar");

    // Remove
    assert_eq!(colony.remove(foo_handle), Some("foo"));

    // Lookup
    assert_eq!(colony.get(foo_handle), None);
    assert_eq!(colony.get(bar_handle), Some(&"bar"));

    // Iteration
    for (key, &value) in colony.iter() {
        assert_eq!((key, value), (bar_handle, "bar"));
    }
}
```
