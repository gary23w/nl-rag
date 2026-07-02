---
title: "Producer–consumer problem"
source: https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem
domain: task-queues
license: CC-BY-SA-4.0
tags: task queue, message queue, distributed task, worker queue
fetched: 2026-07-02
---

# Producer–consumer problem

In computing, the **producer-consumer problem** (also known as the **bounded-buffer problem**) is a family of problems described by Edsger W. Dijkstra since 1965.

Dijkstra found the solution for the producer-consumer problem as he worked as a consultant for the Electrologica X1 and X8 computers: "The first use of producer-consumer was partly software, partly hardware: The component taking care of the information transport between store and peripheral was called 'a channel' ... Synchronization was controlled by two counting semaphores in what we now know as the producer/consumer arrangement: the one semaphore indicating the length of the queue, was incremented (in a V) by the CPU and decremented (in a P) by the channel, the other one, counting the number of unacknowledged completions, was incremented by the channel and decremented by the CPU. [The second semaphore being positive would raise the corresponding interrupt flag.]"

Dijkstra wrote about the unbounded buffer case: "We consider two processes, which are called the 'producer' and the 'consumer' respectively. The producer is a cyclic process and each time it goes through its cycle it produces a certain portion of information, that has to be processed by the consumer. The consumer is also a cyclic process and each time it goes through its cycle, it can process the next portion of information, as has been produced by the producer ... We assume the two processes to be connected for this purpose via a buffer with unbounded capacity."

He wrote about the bounded buffer case: "We have studied a producer and a consumer coupled via a buffer with unbounded capacity ... The relation becomes symmetric, if the two are coupled via a buffer of finite size, say *N* portions"

And about the multiple producer-consumer case: "We consider a number of producer/consumer pairs, where pairi is coupled via an information stream containing ni portions. We assume ... the finite buffer that should contain all portions of all streams to have a capacity of 'tot' portions."

Per Brinch Hansen and Niklaus Wirth saw soon the problem of semaphores: "I have come to the same conclusion with regard to semaphores, namely that they are not suitable for higher level languages. Instead, the natural synchronization events are exchanges of message."

## Dijkstra's bounded buffer solution

The original semaphore bounded buffer solution was written in ALGOL style. The buffer can store N portions or elements. The "number of queueing portions" semaphore counts the filled locations in the buffer, the "number of empty positions" semaphore counts the empty locations in the buffer and the semaphore "buffer manipulation" works as mutex for the buffer put and get operations. If the buffer is full, that is the number of empty positions is zero, the producer thread will wait in the P(number of empty positions) operation. If the buffer is empty, that is the number of queueing portions is zero, the consumer thread will wait in the P(number of queueing portions) operation. The V() operations release the semaphores. As a side effect, a thread can move from the wait queue to the ready queue. The P() operation decreases the semaphore value down to zero. The V() operation increases the semaphore value.

```mw
begin integer number of queueing portions, number of empty positions,
      buffer manipulation;
      number of queueing portions:= 0;
      number of empty positions:= N;
      buffer manipulation:= 1;
      parbegin
      producer: begin
              again 1: produce next portion;
                       P(number of empty positions);
                       P(buffer manipulation);
                       add portion to buffer;
                       V(buffer manipulation);
                       V(number of queueing portions); goto again 1 end;
      consumer: begin
              again 2: P(number of queueing portions);
                       P(buffer manipulation);
                       take portion from buffer;
                       V(buffer manipulation) ;
                       V(number of empty positions);
                       process portion taken; goto again 2 end
      parend
end
```

As of C++ 20, semaphores are part of the language. Dijkstra's solution can easily be written in modern C++. The variable buffer_manipulation is a mutex. The semaphore feature of acquiring in one thread and releasing in another thread is not needed. The lock_guard() statement instead of a lock() and unlock() pair is C++ RAII. The lock_guard destructor ensures lock release in case of an exception. This solution can handle multiple consumer threads and/or multiple producer threads.

```mw
#include <thread>
#include <mutex>
#include <semaphore>

std::counting_semaphore<N> number_of_queueing_portions{0};
std::counting_semaphore<N> number_of_empty_positions{N};
std::mutex buffer_manipulation;

void producer() {
  for (;;) {
    Portion portion = produce_next_portion();
    number_of_empty_positions.acquire();
    {
      std::lock_guard<std::mutex> g(buffer_manipulation);
      add_portion_to_buffer(portion);
    }
    number_of_queueing_portions.release();
  }
}

void consumer() {
  for (;;) {
    number_of_queueing_portions.acquire();
    Portion portion;
    {
      std::lock_guard<std::mutex> g(buffer_manipulation);
      portion = take_portion_from_buffer();
    }
    number_of_empty_positions.release();
    process_portion_taken(portion);
  }
}

int main() {
  std::thread t1(producer);
  std::thread t2(consumer);
  t1.join();
  t2.join();
}
```

## Using monitors

Per Brinch Hansen defined the monitor: I will use the term monitor to denote a shared variable and the set of meaningful operations on it. The purpose of a monitor is to control the scheduling of resources among individual processes according to a certain policy. Tony Hoare laid a theoretical foundation for the monitor.

```mw
bounded buffer: monitor
  begin buffer:array 0..N-1 of portion;
    head, tail: 0..N-1;
    count: 0..N;
    nonempty, nonfull: condition;
  procedure append(x: portion);
    begin if count = N then nonfull.wait;
      note 0 <= count < N;
      buffer[tail] := x;
      tail := tail (+) 1;
      count := count + 1;
      nonempty.signal
    end append;
  procedure remove(result x: portion) ;
    begin if count = 0 then nonempty.wait;
      note 0 < count <= N;
      x := buffer[head];
      head := head (+) 1;
      count := count - 1;
      nonfull.signal
    end remove;
  head := 0; tail := 0; count := 0;
end bounded buffer;
```

The monitor is an object that contains variables `buffer`, `head`, `tail` and `count` to realize a circular buffer, the condition variables `nonempty` and `nonfull` for synchronization and the methods `append` and `remove` to access the bounded buffer. The monitor operation wait corresponds to the semaphore operation P or acquire, signal corresponds to V or release. The circled operation (+) are taken modulo N. The presented Pascal style pseudo code shows a Hoare monitor. A Mesa monitor uses `while count` instead of `if count`. A programming language C++ version is:

```mw
template<size_t N>
class Bounded_buffer {
  Portion buffer[N];         // 0..N-1
  size_t head = 0, tail = 0; // 0..N-1
  size_t size = 0;           // 0..N
  std::condition_variable non_empty, non_full;
  std::mutex mtx;

public:
  void append(Portion portion) {
    std::unique_lock lck(mtx);
    non_full.wait(lck, [&]{ return size != N; });
    assert(size < N);
    buffer[tail++] = std::move(portion);
    tail %= N;
    ++size;
    non_empty.notify_one();
  }

  Portion remove() {
    std::unique_lock lck(mtx);
    non_empty.wait(lck, [&]{ return size != 0; });
    assert(size <= N);
    Portion portion = std::move(buffer[head++]);
    head %= N; 
    --size;
    non_full.notify_one();
    return portion;
  }
};
```

The C++ version needs an additional mutex for technical reasons. It uses assert to enforce the preconditions for the buffer add and remove operations.

## Using channels

The very first producer-consumer solution in the Electrologica computers used 'channels'. Hoare defined channels: An alternative to explicit naming of source and destination would be to name a port through which communication is to take place. The port names would be local to the processes, and the manner in which pairs of ports are to be connected by channels could be declared in the head of a parallel command. Brinch Hansen implemented channels in the programming languages Joyce and Super Pascal. The Plan 9 operating system programming language Alef, the Inferno operating system programming language Limbo have channels. The following C source code compiles on Plan 9 from User Space:

```mw
#include "u.h"
#include "libc.h"
#include "thread.h"

enum { STACK = 8192 };

void producer(void *v) {
  Channel *ch = v;
  for (uint i = 1; ; ++i) {
    sleep(400);
    print("p %d\n", i);
    sendul(ch, i);
  }
}
void consumer(void *v) {
  Channel *ch = v;
  for (;;) {
    uint p = recvul(ch);
    print("\t\tc %d\n", p);
    sleep(200 + nrand(600));
  }
}
void threadmain(int argc, char **argv) {
  int (*mk)(void (*fn)(void*), void *arg, uint stack);
  mk = threadcreate;
  Channel *ch = chancreate(sizeof(ulong), 1);
  mk(producer, ch, STACK);
  mk(consumer, ch, STACK);
  recvp(chancreate(sizeof(void*), 0));
  threadexitsall(0);
}
```

The program entry point is at function `threadmain`. The function call `ch = chancreate(sizeof(ulong), 1)` creates the channel, the function call `sendul(ch, i)` sends a value into the channel and the function call `p = recvul(ch)` receives a value from the channel. The programming language Go has channels, too. A Go example:

```mw
package main

import (
	"fmt"
	"math/rand"
	"time"
)

var sendMsg = 0

func produceMessage() int {
	time.Sleep(400 * time.Millisecond)
	sendMsg++
	fmt.Printf("sendMsg = %v\n", sendMsg)
	return sendMsg
}
func consumeMessage(recvMsg int) {
	fmt.Printf("\t\trecvMsg = %v\n", recvMsg)
	time.Sleep(time.Duration(200+rand.Intn(600)) * time.Millisecond)
}
func main() {
	ch := make(chan int, 3)
	go func() {
		for {
			ch <- produceMessage()
		}
	}()
	for recvMsg := range ch {
		consumeMessage(recvMsg)
	}
}
```

The Go producer-consumer solution uses the main Go routine for consumer and creates a new, unnamed Go routine for the producer. The two Go routines are connected with channel ch. This channel can queue up to three int values. The statement `ch := make(chan int, 3)` creates the channel, the statement `ch <- produceMessage()` sends a value into the channel and the statement `recvMsg := range ch` receives a value from the channel. The allocation of memory resources, the allocation of processing resources, and the synchronization of resources are done by the programming language automatically.

## Without semaphores or monitors

Leslie Lamport documented a bounded buffer producer-consumer solution for one producer and one consumer: We assume that the buffer can hold at most b messages, b >= 1. In our solution, we let k be a constant greater than b, and let s and r be integer variables assuming values between 0 and k-1. We assume that initially s=r and the buffer is empty. By choosing k to be a multiple of b, the buffer can be implemented as an array B [0: b - 1]. The producer simply puts each new message into B[s mod b], and the consumer takes each message from B[r mod b]. The algorithm is shown below, generalized for infinite k.

```mw
Producer:
  L:  if (s - r) mod k = b then goto L fi;
      put message in buffer;
      s := (s + 1) mod k;
      goto L;
Consumer:
  L:  if (s - r) mod k = 0 then goto L fi;
      take message from buffer;
      r := (r + 1) mod k;
      goto L;
```

The Lamport solution uses busy waiting in the thread instead of waiting in the scheduler. This solution neglects the impact of scheduler thread switch at inconvenient times. If the first thread has read a variable value from memory, the scheduler switches to the second thread that changes the variable value, and the scheduler switches back to the first thread then the first thread uses the old value of the variable, not the current value. Atomic read-modify-write solves this problem. Modern C++ offers `atomic` variables and operations for multi-thread programming. The following busy waiting C++11 solution for one producer and one consumer uses atomic read-modify-write operations `fetch_add` and `fetch_sub` on the atomic variable `count`.

```mw
enum {N = 4 };
Message buffer[N];
std::atomic<unsigned> count {0};
void producer() {
  unsigned tail {0};
  for (;;) {
    Message message = produceMessage();
    while (N == count) 
      ; // busy waiting
    buffer[tail++] = message;
    tail %= N;
    count.fetch_add(1, std::memory_order_relaxed);
  }
}
void consumer() {
  unsigned head {0};
  for (;;) {
    while (0 == count) 
      ; // busy waiting
    Message message = buffer[head++];
    head %= N;
    count.fetch_sub(1, std::memory_order_relaxed);
    consumeMessage(message);
  }
}
int main() {
  std::thread t1(producer);
  std::thread t2(consumer);
  t1.join();
  t2.join();
}
```

The circular buffer index variables `head` and `tail` are thread-local and therefore not relevant for memory consistency. The variable `count` controls the busy waiting of the producer and consumer thread.
