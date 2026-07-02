---
title: "Dining philosophers problem"
source: https://en.wikipedia.org/wiki/Dining_philosophers_problem
domain: self-stabilization
license: CC-BY-SA-4.0
tags: self stabilizing system, fault tolerant convergence, dijkstra token ring, closure property
fetched: 2026-07-02
---

# Dining philosophers problem

In computer science, the **dining philosophers problem** is an example problem often used in concurrent algorithm design to illustrate synchronization issues and techniques for resolving them.

It was originally formulated in 1965 by Edsger Dijkstra as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals. Soon after, Tony Hoare gave the problem its present form.

## Problem statement

Five philosophers dine together at the same table. Each philosopher has their own plate at the table. There is a fork between each pair of adjacent plates. The dish served is a kind of spaghetti which has to be eaten with two forks. Each philosopher can only alternately think and eat. Moreover, a philosopher can only eat their spaghetti when they have both a left and a right fork. Thus, two forks will only be available when their two nearest neighbors are thinking, not eating. After an individual philosopher finishes eating, they will put down both forks. The problem is how to design a regimen (a concurrent algorithm) such that any philosopher will not starve; *i.e.*, each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think (an issue of incomplete information).

### Problems

The problem was designed to illustrate the challenges of avoiding deadlock, a system state in which no progress is possible. To see that a proper solution to this problem is not obvious, consider a proposal in which each philosopher is instructed to behave as follows:

- think unless the left fork is available; when it is, pick it up;
- think unless the right fork is available; when it is, pick it up;
- when both forks are held, eat for a fixed amount of time;
- put the left fork down;
- put the right fork down;
- repeat from the beginning.

With these instructions, the situation may arise where each philosopher holds the fork to their left; in that situation, they will all be stuck forever, waiting for the other fork to be available: it is a deadlock.

Resource starvation, mutual exclusion, and livelock are other types of sequence and access problems.

## Solutions

These four conditions are necessary for a deadlock to occur:

- *mutual exclusion* (no fork can be simultaneously used by multiple philosophers)
- *resource holding* (the philosophers hold a fork while waiting for the second)
- *non-preemption* (no philosopher can take a fork from another), and
- *circular wait* (each philosopher may be waiting on the philosopher to their left)

A solution must negate at least one of those four conditions. In practice, negating mutual exclusion or non-preemption somehow can give a valid solution, but most theoretical treatments assume that those assumptions are non-negotiable, instead attacking resource holding or circular waiting (often both).

### Dijkstra's solution

Dijkstra's solution negates resource holding; the philosophers atomically pick up both forks or wait, never holding exactly one fork outside of a critical section. To accomplish this, Dijkstra's solution uses one mutex, one semaphore per philosopher, and one state variable per philosopher. This solution is more complex than the resource hierarchy solution. This is a C++20 version of Dijkstra's solution with changes by Andrew S. Tanenbaum:

```mw
#include <chrono>
#include <iostream>
#include <mutex>
#include <random>
#include <semaphore>
#include <thread>

constexpr const size_t N = 5;  // number of philosophers (and forks)
enum class State 
{
    THINKING = 0,  // philosopher is THINKING
    HUNGRY = 1,    // philosopher is trying to get forks
    EATING = 2,    // philosopher is EATING
};

size_t inline left(size_t i) 
{  
    // number of the left neighbor of philosopher i
    return (i - 1 + N) % N; // N is added for the case when  i - 1 is negative
}

size_t inline right(size_t i) 
{  
    // number of the right neighbor of the philosopher i
    return (i + 1) % N;
}

State state[N];  // array to keep track of everyone's both_forks_available state

std::mutex critical_region_mtx;  // mutual exclusion for critical regions for 
// (picking up and putting down the forks)
std::mutex output_mtx;  // for synchronized cout (printing THINKING/HUNGRY/EATING status)

// array of binary semaphores, one semaphore per philosopher.
// Acquiring each semaphore means philosopher i has returned from the take_forks function, i.e. acquired (blocked) two forks
// Beginning in state 0/false, meaning both forks are considered not available
std::binary_semaphore both_forks_available[N]
{
    std::binary_semaphore{0}, std::binary_semaphore{0},
    std::binary_semaphore{0}, std::binary_semaphore{0},
    std::binary_semaphore{0}
};

size_t my_rand(size_t min, size_t max) 
{
    static std::mt19937 rnd(std::time(nullptr));
    return std::uniform_int_distribution<>(min, max)(rnd);
}

void test(size_t i) 
// if philosopher i is hungry and both neighbors are not eating then philosopher i's semaphore is released.
// This gives philosopher i permission to proceed past the last line of take_forks
{ 
    // i: philosopher number, from 0 to N-1
    if (state[i] == State::HUNGRY &&
        state[left(i)] != State::EATING &&
        state[right(i)] != State::EATING) 
    {
        state[i] = State::EATING;
        both_forks_available[i].release(); // both forks are declared available for philosopher i
    }
}

void think(size_t i) 
{
    size_t duration = my_rand(400, 800);
    {
        std::lock_guard<std::mutex> lk(output_mtx); // critical section for uninterrupted print
        std::cout << i << " is thinking " << duration << "ms\n";
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(duration));
}

void take_forks(size_t i)
{
    {
        std::lock_guard<std::mutex> lk{critical_region_mtx};  // enter critical region
        state[i] = State::HUNGRY;  // record fact that philosopher i is State::HUNGRY
        {
            std::lock_guard<std::mutex> lk(output_mtx); // critical section for uninterrupted print
            std::cout << "\t\t" << i << " is State::HUNGRY\n";
        }
        test(i);                        // try to release philosopher i's own semaphore, i.e. acquire (a permit for) 2 forks
    }                                   // exit critical region
    both_forks_available[i].acquire();  // wait (blocked) if both forks are not currently available
}

void eat(size_t i)
{
    size_t duration = my_rand(400, 800);
    {
        std::lock_guard<std::mutex> lk(output_mtx); // critical section for uninterrupted print
        std::cout << "\t\t\t\t" << i << " is eating " << duration << "ms\n";
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(duration));
}

void put_forks(size_t i) 
{ 
    
    std::lock_guard<std::mutex> lk{critical_region_mtx};    // enter critical region
    state[i] = State::THINKING;  // philosopher has finished State::EATING
    test(left(i));               // try to release left neighbor's semaphore for them
    test(right(i));              // try to release right neighbor's semaphore for them
                                 // exit critical region by exiting the function
}

void philosopher(size_t i)
{  
    while (true) 
    {                         // repeat forever
        think(i);             // philosopher is State::THINKING
        take_forks(i);        // acquire two forks or be blocked
        eat(i);               // yum-yum, spaghetti
        put_forks(i);         // put both forks back on table and check if neighbors can eat
    }
}

int main() {
    std::cout << "dp_14\n";

    std::jthread t0([&] { philosopher(0); }); // [&] means every variable outside the ensuing lambda 
    std::jthread t1([&] { philosopher(1); }); // is captured by reference
    std::jthread t2([&] { philosopher(2); });
    std::jthread t3([&] { philosopher(3); });
    std::jthread t4([&] { philosopher(4); });
}
```

The function test() and its use in take_forks() and put_forks() make the Dijkstra solution deadlock-free.

### Resource hierarchy solution

This solution negates circular waiting by assigning a partial order to the resources (the forks, in this case), and establishes the convention that all resources will be requested in order, and that no two resources unrelated by order will ever be used by a single unit of work at the same time. Here, the resources (forks) will be numbered 1 through 5, and each unit of work (philosopher) will always pick up the lower-numbered fork first, and then the higher-numbered fork, from among the two forks he plans to use. The order in which each philosopher puts down the forks does not matter. In this case, if four of the five philosophers simultaneously pick up their lower-numbered forks, only the highest-numbered fork will remain on the table, so the fifth philosopher will not be able to pick up any fork. Moreover, only one philosopher will have access to that highest-numbered fork, so he will be able to eat using two forks. This can intuitively be thought of as having one "left-handed" philosopher at the table, who – unlike all the other philosophers – takes his fork from the left first.

While the resource hierarchy solution avoids deadlocks, it is not always practical, especially when the list of required resources is not completely known in advance. For example, if a unit of work holds resources 3 and 5 and then determines it needs resource 2, it must release 5, then 3, before acquiring 2, and then it must re-acquire 3 and 5 in that order. Computer programs that access large numbers of database records would not run efficiently if they were required to release all higher-numbered records before accessing a new record, making the method impractical for that purpose.

The resource hierarchy solution is not *fair*. If philosopher 1 is slow to take a fork, and if philosopher 2 is quick to think and pick their forks back up, then philosopher 1 will never get to pick up both forks. A fair solution must guarantee that each philosopher will eventually eat, no matter how slowly that philosopher moves relative to the others.

The following source code is a C++11 implementation of the resource hierarchy solution for five philosophers. The sleep_for() function simulates the time normally spent with business logic.

For GCC: compile with

```mw
g++ src.cpp -std=c++11 -pthread
```

```mw
#include <iostream>
#include <chrono>
#include <mutex>
#include <thread>
#include <random>
#include <ctime>

using namespace std;

int myrand(int min, int max) {
  static mt19937 rnd(time(nullptr));
  return uniform_int_distribution<>(min,max)(rnd);
}

void philosopher(int ph, mutex& ma, mutex& mb, mutex& mo) {
  for (;;) {  // prevent thread from termination
    int duration = myrand(200, 800);
    {
      // Block { } limits scope of lock
      lock_guard<mutex> gmo(mo);
      cout<<ph<<" thinks "<<duration<<"ms\n";
    }
    this_thread::sleep_for(chrono::milliseconds(duration));
    {
      lock_guard<mutex> gmo(mo);
      cout<<"\t\t"<<ph<<" is hungry\n";
    }
    lock_guard<mutex> gma(ma);
    // sleep_for() Delay before seeking second fork can be added here but should not be required.
    lock_guard<mutex> gmb(mb);
    duration = myrand(200, 800);
    {
      lock_guard<mutex> gmo(mo);
      cout<<"\t\t\t\t"<<ph<<" eats "<<duration<<"ms\n";
    }
    this_thread::sleep_for(chrono::milliseconds(duration));
  }
}

int main() {
  cout<<"dining Philosophers C++11 with Resource hierarchy\n";
  mutex m1, m2, m3, m4, m5;   // 5 forks are 5 mutexes
  mutex mo;           // for proper output
  // 5 philosophers are 5 threads
  thread t1([&] {philosopher(1, m1, m2, mo);});
  thread t2([&] {philosopher(2, m2, m3, mo);});
  thread t3([&] {philosopher(3, m3, m4, mo);});  
  thread t4([&] {philosopher(4, m4, m5, mo);});  
  thread t5([&] {philosopher(5, m1, m5, mo);});  // Force a resource hierarchy
  t1.join();  // prevent threads from termination
  t2.join();
  t3.join();
  t4.join();
  t5.join();
}
```

### Arbitrator solution

Another approach is to guarantee that a philosopher can only pick up both forks or none by introducing an arbitrator to replace circular waiting, e.g., a waiter. In order to pick up the forks, a philosopher must ask permission of the waiter. The waiter gives permission to only one philosopher at a time until the philosopher has picked up both of his forks. Putting down a fork is always allowed. The waiter can be implemented as a mutex.

In addition to introducing a new central entity (the waiter), this approach can result in reduced parallelism: if a philosopher is eating and one of his neighbors is requesting the forks, all other philosophers must wait until this request has been fulfilled, even if forks for them are still available.

### Limiting the number of diners in the table

A solution presented by William Stallings is to allow a maximum of *n-1* philosophers to sit down at any time. The last philosopher would have to wait (for example, using a semaphore) for someone to finish dining before he "sits down" and requests access to any fork. This negates circular wait, guaranteeing that at least one philosopher may always acquire both forks, allowing the system to make progress.

### Chandy/Misra solution

In 1984, K. Mani Chandy and J. Misra proposed a different solution to the dining philosophers problem to allow for arbitrary agents (numbered *P*1, ..., *P**n*) to contend for an arbitrary number of resources, unlike Dijkstra's solution. It is also completely distributed and requires no central authority after initialization. However, it violates the requirement that "the philosophers do not speak to each other" (due to the request messages).

1. For every pair of philosophers contending for a resource, create a fork and give it to the philosopher with the lower ID (*n* for agent *P**n*). Each fork can either be *dirty* or *clean.* Initially, all forks are dirty.
2. When a philosopher wants to use a set of resources (*i.e.*, eat), the said philosopher must obtain the forks from his contending neighbors. For all such forks that the philosopher does not have, he sends a request message.
3. When a philosopher with a fork receives a request message, he keeps the fork if it is clean, but gives it up when it is dirty. If the philosopher sends the fork over, he cleans the fork before doing so.
4. After a philosopher is done eating, all his forks become dirty. If another philosopher had previously requested one of the forks, the philosopher who has just finished eating cleans the fork and sends it.

This solution also allows for a large degree of concurrency and will solve an arbitrarily large problem.

It also solves the starvation problem. The clean/dirty labels act as a way of giving preference to the most "starved" processes, and a disadvantage to processes that have just "eaten". One could compare their solution to one where philosophers are not allowed to eat twice in a row without letting others use the forks in between. Chandy and Misra's solution is more flexible than that, but has an element tending in that direction.

In their analysis, they derive a system of preference levels from the distribution of the forks and their clean/dirty states. They show that this system may describe a directed acyclic graph, and if so, the operations in their protocol cannot turn that graph into a cyclic one. This guarantees that deadlock cannot occur by negating circular waiting. However, if the system is initialized to a perfectly symmetric state, like all philosophers holding their left side forks, then the graph is cyclic at the outset, and their solution cannot prevent a deadlock. Initializing the system so that philosophers with lower IDs have dirty forks ensures the graph is initially acyclic.
