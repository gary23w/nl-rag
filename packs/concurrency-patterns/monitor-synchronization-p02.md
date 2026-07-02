---
title: "Monitor (synchronization) (part 2/2)"
source: https://en.wikipedia.org/wiki/Monitor_(synchronization)
domain: concurrency-patterns
license: CC-BY-SA-4.0
tags: thread pool, lock-free, compare-and-swap, coroutine, synchronization primitive, atomic operation
fetched: 2026-07-02
part: 2/2
---

## Condition variables

### Problem statement

For many applications, mutual exclusion is not enough. Threads attempting an operation may need to wait until some condition *P* holds true. A busy waiting loop

```
while not ( P ) do skip
```

will not work, as mutual exclusion will prevent any other thread from entering the monitor to make the condition true. Other "solutions" exist such as having a loop that unlocks the monitor, waits a certain amount of time, locks the monitor and checks for the condition *P*. Theoretically, it works and will not deadlock, but issues arise. It is hard to decide an appropriate amount of waiting time: too small and the thread will hog the CPU, too big and it will be apparently unresponsive. What is needed is a way to signal the thread when the condition *P* is true (or *could* be true).

### Case study: classic bounded producer/consumer problem

A classic concurrency problem is that of the **bounded producer/consumer**, in which there is a queue or ring buffer of tasks with a maximum size, with one or more threads being "producer" threads that add tasks to the queue, and one or more other threads being "consumer" threads that take tasks out of the queue. The queue is assumed to be non–thread-safe itself, and it can be empty, full, or between empty and full. Whenever the queue is full of tasks, then we need the producer threads to block until there is room from consumer threads dequeueing tasks. On the other hand, whenever the queue is empty, then we need the consumer threads to block until more tasks are available due to producer threads adding them.

As the queue is a concurrent object shared between threads, accesses to it must be made atomic, because the queue can be put into an **inconsistent state** during the course of the queue access that should never be exposed between threads. Thus, any code that accesses the queue constitutes a **critical section** that must be synchronized by mutual exclusion. If code and processor instructions in critical sections of code that access the queue could be **interleaved** by arbitrary **context switches** between threads on the same processor or by simultaneously-running threads on multiple processors, then there is a risk of exposing inconsistent state and causing race conditions.

#### Incorrect without synchronization

A naive approach is to design the code with **busy-waiting** and no synchronization, making the code subject to race conditions:

```mw
global RingBuffer queue; // A thread-unsafe ring-buffer of tasks.

// Method representing each producer thread's behavior:
public method producer() {
    while (true) {
        task myTask = ...; // Producer makes some new task to be added.
        while (queue.isFull()) {} // Busy-wait until the queue is non-full.
        queue.enqueue(myTask); // Add the task to the queue.
    }
}

// Method representing each consumer thread's behavior:
public method consumer() {
    while (true) {
        while (queue.isEmpty()) {} // Busy-wait until the queue is non-empty.
        myTask = queue.dequeue(); // Take a task off of the queue.
        doStuff(myTask); // Go off and do something with the task.
    }
}
```

This code has a serious problem in that accesses to the queue can be interrupted and interleaved with other threads' accesses to the queue. The *queue.enqueue* and *queue.dequeue* methods likely have instructions to update the queue's member variables such as its size, beginning and ending positions, assignment and allocation of queue elements, etc. In addition, the *queue.isEmpty()* and *queue.isFull()* methods read this shared state as well. If producer/consumer threads are allowed to be interleaved during the calls to enqueue/dequeue, then inconsistent state of the queue can be exposed leading to race conditions. In addition, if one consumer makes the queue empty in-between another consumer's exiting the busy-wait and calling "dequeue", then the second consumer will attempt to dequeue from an empty queue leading to an error. Likewise, if a producer makes the queue full in-between another producer's exiting the busy-wait and calling "enqueue", then the second producer will attempt to add to a full queue leading to an error.

#### Spin-waiting

One naive approach to achieve synchronization, as alluded to above, is to use "**spin-waiting**", in which a mutex is used to protect the critical sections of code and busy-waiting is still used, with the lock being acquired and released in between each busy-wait check.

```mw
global RingBuffer queue; // A thread-unsafe ring-buffer of tasks.
global Lock queueLock; // A mutex for the ring-buffer of tasks.

// Method representing each producer thread's behavior:
public method producer() {
    while (true) {
        task myTask = ...; // Producer makes some new task to be added.

        queueLock.acquire(); // Acquire lock for initial busy-wait check.
        while (queue.isFull()) { // Busy-wait until the queue is non-full.
            queueLock.release();
            // Drop the lock temporarily to allow a chance for other threads
            // needing queueLock to run so that a consumer might take a task.
            queueLock.acquire(); // Re-acquire the lock for the next call to "queue.isFull()".
        }

        queue.enqueue(myTask); // Add the task to the queue.
        queueLock.release(); // Drop the queue lock until we need it again to add the next task.
    }
}

// Method representing each consumer thread's behavior:
public method consumer() {
    while (true) {
        queueLock.acquire(); // Acquire lock for initial busy-wait check.
        while (queue.isEmpty()) { // Busy-wait until the queue is non-empty.
            queueLock.release();
            // Drop the lock temporarily to allow a chance for other threads
            // needing queueLock to run so that a producer might add a task.
            queueLock.acquire(); // Re-acquire the lock for the next call to "queue.isEmpty()".
        }
        myTask = queue.dequeue(); // Take a task off of the queue.
        queueLock.release(); // Drop the queue lock until we need it again to take off the next task.
        doStuff(myTask); // Go off and do something with the task.
    }
}
```

This method assures that an inconsistent state does not occur, but wastes CPU resources due to the unnecessary busy-waiting. Even if the queue is empty and producer threads have nothing to add for a long time, consumer threads are always busy-waiting unnecessarily. Likewise, even if consumers are blocked for a long time on processing their current tasks and the queue is full, producers are always busy-waiting. This is a wasteful mechanism. What is needed is a way to make producer threads block until the queue is non-full, and a way to make consumer threads block until the queue is non-empty.

(N.B.: Mutexes themselves can also be **spin-locks** which involve busy-waiting in order to get the lock, but in order to solve this problem of wasted CPU resources, we assume that *queueLock* is not a spin-lock and properly uses a blocking lock queue itself.)

### Condition variables

The solution is to use **condition variables**. Conceptually, a condition variable is a queue of threads, associated with a mutex, on which a thread may wait for some condition to become true. Thus each condition variable c is associated with an assertion Pc. While a thread is waiting on a condition variable, that thread is not considered to occupy the monitor, and so other threads may enter the monitor to change the monitor's state. In most types of monitors, these other threads may signal the condition variable c to indicate that assertion Pc is true in the current state.

Thus there are three main operations on condition variables:

- `**wait** c, m`, where `*c*` is a condition variable and `m` is a mutex (lock) associated with the monitor. This operation is called by a thread that needs to wait until the assertion Pc is true before proceeding. While the thread is waiting, it does not occupy the monitor. The function, and fundamental contract, of the "wait" operation, is to do the following steps: Steps 1a and 1b can occur in either order, with 1c usually occurring after them. While the thread is sleeping and in `*c*`'s wait-queue, the next program counter to be executed is at step 2, in the middle of the "wait" function/subroutine. Thus, the thread sleeps and later wakes up in the middle of the "wait" operation. The atomicity of the operations within step 1 is important to avoid race conditions that would be caused by a preemptive thread switch in-between them. One failure mode that could occur if these were not atomic is a *missed wakeup*, in which the thread could be on `*c*`'s sleep-queue and have released the mutex, but a preemptive thread switch occurred before the thread went to sleep, and another thread called a signal operation (see below) on `*c*` moving the first thread back out of `*c*`'s queue. As soon as the first thread in question is switched back to, its program counter will be at step 1c, and it will sleep and be unable to be woken up again, violating the invariant that it should have been on `*c*`'s sleep-queue when it slept. Other race conditions depend on the ordering of steps 1a and 1b, and depend on where a context switch occurs.
  1. Atomically: release the mutex `*m*`,move this thread from the "running" to `*c*`'s "wait-queue" (a.k.a. "sleep-queue") of threads, andsleep this thread. (Context is synchronously yielded to another thread.)
  2. Once this thread is subsequently notified/signaled (see below) and resumed, then automatically re-acquire the mutex `*m*`.
- `**signal** c`, also known as `**notify** c`, is called by a thread to indicate that the assertion Pc is true. Depending on the type and implementation of the monitor, this moves one or more threads from `c`'s sleep-queue to the "ready queue", or another queue for it to be executed. It is usually considered a best practice to perform the "signal" operation before releasing mutex `*m*` that is associated with `*c*`, but as long as the code is properly designed for concurrency and depending on the threading implementation, it is often also acceptable to release the lock before signalling. Depending on the threading implementation, the ordering of this can have scheduling-priority ramifications. (Some authors instead advocate a preference for releasing the lock before signalling.) A threading implementation should document any special constraints on this ordering.
- `**broadcast** c`, also known as `**notifyAll** c`, is a similar operation that wakes up all threads in c's wait-queue. This empties the wait-queue. Generally, when more than one predicate condition is associated with the same condition variable, the application will require **broadcast** instead of **signal** because a thread waiting for the wrong condition might be woken up and then immediately go back to sleep without waking up a thread waiting for the correct condition that just became true. Otherwise, if the predicate condition is one-to-one with the condition variable associated with it, then **signal** may be more efficient than **broadcast**.

As a design rule, multiple condition variables can be associated with the same mutex, but not vice versa. (This is a one-to-many correspondence.) This is because the predicate Pc is the same for all threads using the monitor and must be protected with mutual exclusion from all other threads that might cause the condition to be changed or that might read it while the thread in question causes it to be changed, but there may be different threads that want to wait for a different condition on the same variable requiring the same mutex to be used. In the producer-consumer example described above, the queue must be protected by a unique mutex object, `*m*`. The "producer" threads will want to wait on a monitor using lock `*m*` and a condition variable $c_{full}$ which blocks until the queue is non-full. The "consumer" threads will want to wait on a different monitor using the same mutex `*m*` but a different condition variable $c_{empty}$ which blocks until the queue is non-empty. It would (usually) not make sense to have different mutexes for the same condition variable, but this classic example shows why it often certainly makes sense to have multiple condition variables using the same mutex. A mutex used by one or more condition variables (one or more monitors) may also be shared with code that does *not* use condition variables (and which simply acquires/releases it without any wait/signal operations), if those critical sections do not happen to require waiting for a certain condition on the concurrent data.

### Monitor usage

The proper basic usage of a monitor is:

```mw
acquire(m); // Acquire this monitor's lock.
while (!p) { // While the condition/predicate/assertion that we are waiting for is not true...
	wait(m, cv); // Wait on this monitor's lock and condition variable.
}
// ... Critical section of code goes here ...
signal(cv2); // Or: broadcast(cv2);
             // cv2 might be the same as cv or different.
release(m); // Release this monitor's lock.
```

The following is the same pseudocode but with more verbose comments to better explain what is going on:

```mw
// ... (previous code)
// About to enter the monitor.
// Acquire the advisory mutex (lock) associated with the concurrent
// data that is shared between threads, 
// to ensure that no two threads can be preemptively interleaved or
// run simultaneously on different cores while executing in critical
// sections that read or write this same concurrent data. If another
// thread is holding this mutex, then this thread will be put to sleep
// (blocked) and placed on m's sleep queue.  (Mutex "m" shall not be
// a spin-lock.)
acquire(m);
// Now, we are holding the lock and can check the condition for the
// first time.

// The first time we execute the while loop condition after the above
// "acquire", we are asking, "Is the condition/predicate/assertion
// we are waiting for already true?"

while (!p()) 	// "p" is any expression (e.g. variable or 
		// function-call) that checks the condition and
		// evaluates to boolean.  This itself is a critical
		// section, so you *MUST* be holding the lock when
		// executing this "while" loop condition!
				
// If this is not the first time the "while" condition is being checked,
// then we are asking the question, "Now that another thread using this
// monitor has notified me and woken me up and I have been context-switched
// back to, did the condition/predicate/assertion we are waiting on stay
// true between the time that I was woken up and the time that I re-acquired
// the lock inside the "wait" call in the last iteration of this loop, or
// did some other thread cause the condition to become false again in the
// meantime thus making this a spurious wakeup?

{
	// If this is the first iteration of the loop, then the answer is
	// "no" -- the condition is not ready yet. Otherwise, the answer is:
	// the latter.  This was a spurious wakeup, some other thread occurred
	// first and caused the condition to become false again, and we must
	// wait again.

	wait(m, cv);
		// Temporarily prevent any other thread on any core from doing
		// operations on m or cv.
		// release(m) 		// Atomically release lock "m" so other
		//			// code using this concurrent data
		// 			// can operate, move this thread to cv's
		//			// wait-queue so that it will be notified
		//			// sometime when the condition becomes
		// 			// true, and sleep this thread. Re-enable
		//			// other threads and cores to do 
		//			// operations on m and cv.
		//
		// Context switch occurs on this core.
		//
		// At some future time, the condition we are waiting for becomes
		// true, and another thread using this monitor (m, cv) does either
		// a signal that happens to wake this thread up, or a
		// broadcast that wakes us up, meaning that we have been taken out
		// of cv's wait-queue.
		//
		// During this time, other threads may cause the condition to
		// become false again, or the condition may toggle one or more
		// times, or it may happen to stay true.
		//
		// This thread is switched back to on some core.
		//
		// acquire(m)		// Lock "m" is re-acquired.
		
	// End this loop iteration and re-check the "while" loop condition to make
	// sure the predicate is still true.
	
}

// The condition we are waiting for is true!
// We are still holding the lock, either from before entering the monitor or from
// the last execution of "wait".

// Critical section of code goes here, which has a precondition that our predicate
// must be true.
// This code might make cv's condition false, and/or make other condition variables'
// predicates true.

// Call signal or broadcast, depending on which condition variables'
// predicates (who share mutex m) have been made true or may have been made true,
// and the monitor semantic type being used.

for (cv_x in cvs_to_signal) {
	signal(cv_x); // Or: broadcast(cv_x);
}
// One or more threads have been woken up but will block as soon as they try
// to acquire m.

// Release the mutex so that notified thread(s) and others can enter their critical
// sections.
release(m);
```

#### Solving the bounded producer/consumer problem

Having introduced the usage of condition variables, let us use it to revisit and solve the classic bounded producer/consumer problem. The classic solution is to use two monitors, comprising two condition variables sharing one lock on the queue:

```mw
global volatile RingBuffer queue; // A thread-unsafe ring-buffer of tasks.
global Lock queueLock; // A mutex for the ring-buffer of tasks. (Not a spin-lock.)
global CV queueEmptyCV; // A condition variable for consumer threads waiting for the queue to 
				        // become non-empty. Its associated lock is "queueLock".
global CV queueFullCV; // A condition variable for producer threads waiting for the queue to
				       // become non-full. Its associated lock is also "queueLock".

// Method representing each producer thread's behavior:
public method producer() {
    while (true) {
        // Producer makes some new task to be added.
        task myTask = ...;

        // Acquire "queueLock" for the initial predicate check.
        queueLock.acquire();

        // Critical section that checks if the queue is non-full.
        while (queue.isFull()) {
            // Release "queueLock", enqueue this thread onto "queueFullCV" and sleep this thread.
            wait(queueLock, queueFullCV);
            // When this thread is awoken, re-acquire "queueLock" for the next predicate check.
        }

        // Critical section that adds the task to the queue (note that we are holding "queueLock").
        queue.enqueue(myTask);

        // Wake up one or all consumer threads that are waiting for the queue to be non-empty
        // now that it is guaranteed, so that a consumer thread will take the task.
        signal(queueEmptyCV); // Or: broadcast(queueEmptyCV);
        // End of critical sections.

        // Release "queueLock" until we need it again to add the next task.
        queueLock.release();
    }
}

// Method representing each consumer thread's behavior:
public method consumer() {
    while (true) {
        // Acquire "queueLock" for the initial predicate check.
        queueLock.acquire();

        // Critical section that checks if the queue is non-empty.
        while (queue.isEmpty()) {
            // Release "queueLock", enqueue this thread onto "queueEmptyCV" and sleep this thread.
            wait(queueLock, queueEmptyCV);
            // When this thread is awoken, re-acquire "queueLock" for the next predicate check.
        }

        // Critical section that takes a task off of the queue (note that we are holding "queueLock").
        myTask = queue.dequeue();

        // Wake up one or all producer threads that are waiting for the queue to be non-full
        // now that it is guaranteed, so that a producer thread will add a task.
        signal(queueFullCV); // Or: broadcast(queueFullCV);
        // End of critical sections.

        // Release "queueLock" until we need it again to take the next task.
        queueLock.release();

        // Go off and do something with the task.
        doStuff(myTask);
    }
}
```

This ensures concurrency between the producer and consumer threads sharing the task queue, and blocks the threads that have nothing to do rather than busy-waiting as shown in the aforementioned approach using spin-locks.

A variant of this solution could use a single condition variable for both producers and consumers, perhaps named "queueFullOrEmptyCV" or "queueSizeChangedCV". In this case, more than one condition is associated with the condition variable, such that the condition variable represents a weaker condition than the conditions being checked by individual threads. The condition variable represents threads that are waiting for the queue to be non-full *and* ones waiting for it to be non-empty. However, doing this would require using *broadcast* in all the threads using the condition variable and cannot use a regular *signal*. This is because the regular *signal* might wake up a thread of the wrong type whose condition has not yet been met, and that thread would go back to sleep without a thread of the correct type getting signaled. For example, a producer might make the queue full and wake up another producer instead of a consumer, and the woken producer would go back to sleep. In the complementary case, a consumer might make the queue empty and wake up another consumer instead of a producer, and the consumer would go back to sleep. Using *broadcast* ensures that some thread of the right type will proceed as expected by the problem statement.

Here is the variant using only one condition variable and broadcast:

```mw
global volatile RingBuffer queue; // A thread-unsafe ring-buffer of tasks.
global Lock queueLock; // A mutex for the ring-buffer of tasks.  (Not a spin-lock.)
global CV queueFullOrEmptyCV; // A single condition variable for when the queue is not ready for any thread
                              // i.e. for producer threads waiting for the queue to become non-full 
                              // and consumer threads waiting for the queue to become non-empty.
                              // Its associated lock is "queueLock".
                              // Not safe to use regular "signal" because it is associated with
                              // multiple predicate conditions (assertions).

// Method representing each producer thread's behavior:
public method producer() {
    while (true) {
        // Producer makes some new task to be added.
        task myTask = ...;

        // Acquire "queueLock" for the initial predicate check.
        queueLock.acquire();

        // Critical section that checks if the queue is non-full.
        while (queue.isFull()) {
            // Release "queueLock", enqueue this thread onto "queueFullOrEmptyCV" and sleep this thread.
            wait(queueLock, queueFullOrEmptyCV);
            // When this thread is awoken, re-acquire "queueLock" for the next predicate check.
        }

        // Critical section that adds the task to the queue (note that we are holding "queueLock").
        queue.enqueue(myTask);

        // Wake up all producer and consumer threads that are waiting for the queue to be respectively
        // non-full and non-empty now that the latter is guaranteed, so that a consumer thread will take the task.
        broadcast(queueFullOrEmptyCV); // Do not use "signal" (as it might wake up another producer thread only).
        // End of critical sections.

        // Release "queueLock" until we need it again to add the next task.
        queueLock.release();
    }
}

// Method representing each consumer thread's behavior:
public method consumer() {
    while (true) {
        // Acquire "queueLock" for the initial predicate check.
        queueLock.acquire();

        // Critical section that checks if the queue is non-empty.
        while (queue.isEmpty()) {
            // Release "queueLock", enqueue this thread onto "queueFullOrEmptyCV" and sleep this thread.
            wait(queueLock, queueFullOrEmptyCV);
            // When this thread is awoken, re-acquire "queueLock" for the next predicate check.
        }

        // Critical section that takes a task off of the queue (note that we are holding "queueLock").
        myTask = queue.dequeue();

        // Wake up all producer and consumer threads that are waiting for the queue to be respectively
        // non-full and non-empty now that the former is guaranteed, so that a producer thread will add a task.
        broadcast(queueFullOrEmptyCV); // Do not use "signal" (as it might wake up another consumer thread only).
        // End of critical sections.

        // Release "queueLock" until we need it again to take the next task.
        queueLock.release();

        // Go off and do something with the task.
        doStuff(myTask);
    }
}
```

### Synchronization primitives

Monitors are implemented using an atomic read-modify-write primitive and a waiting primitive. The read-modify-write primitive (usually test-and-set or compare-and-swap) is usually in the form of a memory-locking instruction provided by the ISA, but can also be composed of non-locking instructions on single-processor devices when interrupts are disabled. The waiting primitive can be a busy-wait loop or an OS-provided primitive that prevents the thread from being scheduled until it is ready to proceed.

Here is an example pseudocode implementation of parts of a threading system and mutexes and Mesa-style condition variables, using **test-and-set** and a first-come, first-served policy:

#### Sample Mesa-monitor implementation with Test-and-Set

```mw
// Basic parts of threading system:
// Assume "ThreadQueue" supports random access.
public volatile ThreadQueue readyQueue; // Thread-unsafe queue of ready threads.  Elements are (Thread*).
public volatile global Thread* currentThread; // Assume this variable is per-core.  (Others are shared.)

// Implements a spin-lock on just the synchronized state of the threading system itself.
// This is used with test-and-set as the synchronization primitive.
public volatile global bool threadingSystemBusy = false;

// Context-switch interrupt service routine (ISR):
// On the current CPU core, preemptively switch to another thread.
public method contextSwitchISR() {
    if (testAndSet(threadingSystemBusy)) {
        return; // Can't switch context right now.
    }

    // Ensure this interrupt can't happen again which would foul up the context switch:
    systemCall_disableInterrupts();

    // Get all of the registers of the currently-running process.
    // For Program Counter (PC), we will need the instruction location of
    // the "resume" label below.  Getting the register values is platform-dependent and may involve
    // reading the current stack frame, JMP/CALL instructions, etc.  (The details are beyond this scope.)
    currentThread->registers = getAllRegisters(); // Store the registers in the "currentThread" object in memory.
    currentThread->registers.PC = resume; // Set the next PC to the "resume" label below in this method.

    readyQueue.enqueue(currentThread); // Put this thread back onto the ready queue for later execution.
    
    Thread* otherThread = readyQueue.dequeue(); // Remove and get the next thread to run from the ready queue.
    
    currentThread = otherThread; // Replace the global current-thread pointer value so it is ready for the next thread.

    // Restore the registers from currentThread/otherThread, including a jump to the stored PC of the other thread
    // (at "resume" below).  Again, the details of how this is done are beyond this scope.
    restoreRegisters(otherThread.registers);

    // *** Now running "otherThread" (which is now "currentThread")!  The original thread is now "sleeping". ***

    resume: // This is where another contextSwitch() call needs to set PC to when switching context back here.

    // Return to where otherThread left off.

    threadingSystemBusy = false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
}

// Thread sleep method:
// On current CPU core, a synchronous context switch to another thread without putting
// the current thread on the ready queue.
// Must be holding "threadingSystemBusy" and disabled interrupts so that this method
// doesn't get interrupted by the thread-switching timer which would call contextSwitchISR().
// After returning from this method, must clear "threadingSystemBusy".
public method threadSleep() {
    // Get all of the registers of the currently-running process.
    // For Program Counter (PC), we will need the instruction location of
    // the "resume" label below.  Getting the register values is platform-dependent and may involve
    // reading the current stack frame, JMP/CALL instructions, etc.  (The details are beyond this scope.)
    currentThread->registers = getAllRegisters(); // Store the registers in the "currentThread" object in memory.
    currentThread->registers.PC = resume; // Set the next PC to the "resume" label below in this method.

    // Unlike contextSwitchISR(), we will not place currentThread back into readyQueue.
    // Instead, it has already been placed onto a mutex's or condition variable's queue.
    
    Thread* otherThread = readyQueue.dequeue(); // Remove and get the next thread to run from the ready queue.
    
    currentThread = otherThread; // Replace the global current-thread pointer value so it is ready for the next thread.

    // Restore the registers from currentThread/otherThread, including a jump to the stored PC of the other thread
    // (at "resume" below).  Again, the details of how this is done are beyond this scope.
    restoreRegisters(otherThread.registers);

    // *** Now running "otherThread" (which is now "currentThread")!  The original thread is now "sleeping". ***

    resume: // This is where another contextSwitch() call needs to set PC to when switching context back here.

    // Return to where otherThread left off.
}

public method wait(Mutex m, ConditionVariable c) {
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)) {}
    // N.B.: "threadingSystemBusy" is now true.
    
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
 
    assert m.held; // (Specifically, this thread must be the one holding it.)
    
    m.release();
    c.waitingThreads.enqueue(currentThread);
    
    threadSleep();
    
    // Thread sleeps ... Thread gets woken up from a signal/broadcast.
    
    threadingSystemBusy = false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    
    // Mesa style:
    // Context switches may now occur here, making the client caller's predicate false.
    
    m.acquire();
}

public method signal(ConditionVariable c) {
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)) {}
    // N.B.: "threadingSystemBusy" is now true.
    
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
    
    if (!c.waitingThreads.isEmpty()) {
        wokenThread = c.waitingThreads.dequeue();
        readyQueue.enqueue(wokenThread);
    }
    
    threadingSystemBusy = false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    
    // Mesa style:
    // The woken thread is not given any priority.
}

public method broadcast(ConditionVariable c) {
    // Internal spin-lock while other threads on any core are accessing this object's
    // "held" and "threadQueue", or "readyQueue".
    while (testAndSet(threadingSystemBusy)) {}
    // N.B.: "threadingSystemBusy" is now true.
    
    // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
    // the thread-switching timer on this core which would call contextSwitchISR().
    // Done outside threadSleep() for more efficiency so that this thread will be sleeped
    // right after going on the condition-variable queue.
    systemCall_disableInterrupts();
    
    while (!c.waitingThreads.isEmpty()) {
        wokenThread = c.waitingThreads.dequeue();
        readyQueue.enqueue(wokenThread);
    }
    
    threadingSystemBusy = false; // Must be an atomic assignment.
    systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    
    // Mesa style:
    // The woken threads are not given any priority.
}

class Mutex {
    protected volatile bool held = false;
    private volatile ThreadQueue blockingThreads; // Thread-unsafe queue of blocked threads.  Elements are (Thread*).
    
    public method acquire() {
        // Internal spin-lock while other threads on any core are accessing this object's
        // "held" and "threadQueue", or "readyQueue".
        while (testAndSet(threadingSystemBusy)) {}
        // N.B.: "threadingSystemBusy" is now true.
        
        // System call to disable interrupts on this core so that threadSleep() doesn't get interrupted by
        // the thread-switching timer on this core which would call contextSwitchISR().
        // Done outside threadSleep() for more efficiency so that this thread will be sleeped
        // right after going on the lock queue.
        systemCall_disableInterrupts();

        assert !blockingThreads.contains(currentThread);

        if (held) {
            // Put "currentThread" on this lock's queue so that it will be
            // considered "sleeping" on this lock.
            // Note that "currentThread" still needs to be handled by threadSleep().
            readyQueue.remove(currentThread);
            blockingThreads.enqueue(currentThread);
            threadSleep();
            
            // Now we are woken up, which must be because "held" became false.
            assert !held;
            assert !blockingThreads.contains(currentThread);
        }
        
        held = true;
        
        threadingSystemBusy = false; // Must be an atomic assignment.
        systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    }        
        
    public method release() {
        // Internal spin-lock while other threads on any core are accessing this object's
        // "held" and "threadQueue", or "readyQueue".
        while (testAndSet(threadingSystemBusy)) {}
        // N.B.: "threadingSystemBusy" is now true.
        
        // System call to disable interrupts on this core for efficiency.
        systemCall_disableInterrupts();
        
        assert held; // (Release should only be performed while the lock is held.)

        held = false;
        
        if (!blockingThreads.isEmpty()) {
            Thread* unblockedThread = blockingThreads.dequeue();
            readyQueue.enqueue(unblockedThread);
        }
        
        threadingSystemBusy = false; // Must be an atomic assignment.
        systemCall_enableInterrupts(); // Turn pre-emptive switching back on on this core.
    }
}

struct ConditionVariable {
    volatile ThreadQueue waitingThreads;
}
```

### Blocking condition variables

The original proposals by C. A. R. Hoare and Per Brinch Hansen were for *blocking condition variables*. With a blocking condition variable, the signaling thread must wait outside the monitor (at least) until the signaled thread relinquishes occupancy of the monitor by either returning or by again waiting on a condition variable. Monitors using blocking condition variables are often called *Hoare-style* monitors or *signal-and-urgent-wait* monitors.

We assume there are two queues of threads associated with each monitor object

- `e` is the entrance queue
- `s` is a queue of threads that have signaled.

In addition we assume that for each condition variable c, there is a queue

- `c.q`, which is a queue for threads waiting on condition variable c

All queues are typically guaranteed to be fair and, in some implementations, may be guaranteed to be first in first out.

The implementation of each operation is as follows. (We assume that each operation runs in mutual exclusion to the others; thus restarted threads do not begin executing until the operation is complete.)

```
enter the monitor:
    enter the method
    if the monitor is locked
        add this thread to e
        block this thread
    else
        lock the monitor

leave the monitor:
    schedule
    return from the method

wait c:
    add this thread to c.q
    schedule
    block this thread

signal c:
    if there is a thread waiting on c.q
        select and remove one such thread t from c.q
        (t is called "the signaled thread")
        add this thread to s
        restart t
        (so t will occupy the monitor next)
        block this thread

schedule:
    if there is a thread on s
        select and remove one thread from s and restart it
        (this thread will occupy the monitor next)
    else if there is a thread on e
        select and remove one thread from e and restart it
        (this thread will occupy the monitor next)
    else
        unlock the monitor
        (the monitor will become unoccupied)
```

The `schedule` routine selects the next thread to occupy the monitor or, in the absence of any candidate threads, unlocks the monitor.

The resulting signaling discipline is known as *"signal and urgent wait,"* as the signaler must wait, but is given priority over threads on the entrance queue. An alternative is *"signal and wait,"* in which there is no `s` queue and signaler waits on the `e` queue instead.

Some implementations provide a **signal and return** operation that combines signaling with returning from a procedure.

```
signal c and return:
    if there is a thread waiting on c.q
        select and remove one such thread t from c.q
        (t is called "the signaled thread")
        restart t
        (so t will occupy the monitor next)
    else
        schedule
    return from the method
```

In either case ("signal and urgent wait" or "signal and wait"), when a condition variable is signaled and there is at least one thread waiting on the condition variable, the signaling thread hands occupancy over to the signaled thread seamlessly, so that no other thread can gain occupancy in between. If Pc is true at the start of each **signal** c operation, it will be true at the end of each **wait** c operation. This is summarized by the following contracts. In these contracts, I is the monitor's invariant.

```
enter the monitor:
    postcondition I

leave the monitor:
    precondition I

wait c:
    precondition I
    modifies the state of the monitor
    postcondition Pc and I

signal c:
    precondition Pc and I
    modifies the state of the monitor
    postcondition I

signal c and return:
    precondition Pc and I
```

In these contracts, it is assumed that I and Pc do not depend on the contents or lengths of any queues.

(When the condition variable can be queried as to the number of threads waiting on its queue, more sophisticated contracts can be given. For example, a useful pair of contracts, allowing occupancy to be passed without establishing the invariant, is:

```
wait c:
    precondition I
    modifies the state of the monitor
    postcondition Pc

signal c
    precondition (not empty(c) and Pc) or (empty(c) and I)
    modifies the state of the monitor
    postcondition I
```

(See Howard and Buhr *et al.* for more.)

The assertion Pc is entirely up to the programmer; he or she simply needs to be consistent about what it is.

We conclude this section with an example of a thread-safe class using a blocking monitor that implements a bounded, thread-safe stack.

```
monitor class SharedStack {
    private const capacity := 10
    private int[capacity] A
    private int size := 0
    invariant 0 <= size and size <= capacity
    private BlockingCondition theStackIsNotEmpty /* associated with 0 < size and size <= capacity */
    private BlockingCondition theStackIsNotFull /* associated with 0 <= size and size < capacity */

    public method push(int value)
    {
        if size = capacity then wait theStackIsNotFull
        assert 0 <= size and size < capacity
        A[size] := value ; size := size + 1
        assert 0 < size and size <= capacity
        signal theStackIsNotEmpty and return
    }

    public method int pop()
    {
        if size = 0 then wait theStackIsNotEmpty
        assert 0 < size and size <= capacity
        size := size - 1 ;
        assert 0 <= size and size < capacity
        signal theStackIsNotFull and return A[size]
    }
}
```

Note that, in this example, the thread-safe stack is internally providing a mutex, which, as in the earlier producer/consumer example, is shared by both condition variables, which are checking different conditions on the same concurrent data. The only difference is that the producer/consumer example assumed a regular non-thread-safe queue and was using a standalone mutex and condition variables, without these details of the monitor abstracted away, as is the case here. In this example, when the "wait" operation is called, it must somehow be supplied with the thread-safe stack's mutex, such as if the "wait" operation is an integrated part of the "monitor class". Aside from this kind of abstracted functionality, when a "raw" monitor is used, it will *always* have to include a mutex and a condition variable, with a unique mutex for each condition variable.

### Nonblocking condition variables

With *nonblocking condition variables* (also called *"Mesa style"* condition variables or *"signal and continue"* condition variables), signaling does not cause the signaling thread to lose occupancy of the monitor. Instead, the signaled threads are moved to the `e` queue. There is no need for the `s` queue.

With nonblocking condition variables, the **signal** operation is often called **notify** — a terminology we will follow here. It is also common to provide a **notify all** operation that moves all threads waiting on a condition variable to the `e` queue.

The meaning of various operations are given here. (We assume that each operation runs in mutual exclusion to the others; thus restarted threads do not begin executing until the operation is complete.)

```
enter the monitor:
    enter the method
    if the monitor is locked
        add this thread to e
        block this thread
    else
        lock the monitor

leave the monitor:
    schedule
    return from the method

wait c:
    add this thread to c.q
    schedule
    block this thread

notify c:
    if there is a thread waiting on c.q
        select and remove one thread t from c.q
        (t is called "the notified thread")
        move t to e

notify all c:
    move all threads waiting on c.q to e

schedule :
    if there is a thread on e
        select and remove one thread from e and restart it
    else
        unlock the monitor
```

As a variation on this scheme, the notified thread may be moved to a queue called `w`, which has priority over `e`. See Howard and Buhr *et al.* for further discussion.

It is possible to associate an assertion Pc with each condition variable c such that Pc is sure to be true upon return from `**wait** c`. However, one must ensure that Pc is preserved from the time the **notify**ing thread gives up occupancy until the notified thread is selected to re-enter the monitor. Between these times, there could be activity by other occupants. Thus, it is common for Pc to simply be *true*.

For this reason, it is usually necessary to enclose each **wait** operation in a loop like this

```
while not ( P ) do
    wait c
```

where P is some condition stronger than Pc. The operations `**notify** c` and `**notify all** c` are treated as "hints" that P may be true for some waiting thread. Every iteration of such a loop past the first represents a lost notification; thus with nonblocking monitors, one must be careful to ensure that too many notifications cannot be lost.

As an example of "hinting," consider a bank account in which a withdrawing thread will wait until the account has sufficient funds before proceeding

```
monitor class Account {
    private int balance := 0
    invariant balance >= 0
    private NonblockingCondition balanceMayBeBigEnough

    public method withdraw(int amount)
        precondition amount >= 0
    {
        while balance < amount do wait balanceMayBeBigEnough
        assert balance >= amount
        balance := balance - amount
    }

    public method deposit(int amount)
        precondition amount >= 0
    {
        balance := balance + amount
        notify all balanceMayBeBigEnough
    }
}
```

In this example, the condition being waited for is a function of the amount to be withdrawn, so it is impossible for a depositing thread to *know* that it made such a condition true. It makes sense in this case to allow each waiting thread into the monitor (one at a time) to check if its assertion is true.

### Implicit condition variable monitors

In the Java language, each object may be used as a monitor. Methods requiring mutual exclusion must be explicitly marked with the **synchronized** keyword. Blocks of code may also be marked by **synchronized**.

Rather than having explicit condition variables, each monitor (i.e., object) is equipped with a single wait queue in addition to its entrance queue. All waiting is done on this single wait queue and all **notify** and **notifyAll** operations apply to this queue. This approach has been adopted in other languages, for example C#.

### Implicit signaling

Another approach to signaling is to omit the **signal** operation. Whenever a thread leaves the monitor (by returning or waiting), the assertions of all waiting threads are evaluated until one is found to be true. In such a system, condition variables are not needed, but the assertions must be explicitly coded. The contract for wait is

```
wait P:
    precondition I
    modifies the state of the monitor
    postcondition P and I
```

## History

Brinch Hansen and Hoare developed the monitor concept in the early 1970s, based on earlier ideas of their own and of Edsger Dijkstra. Brinch Hansen published the first monitor notation, adopting the class concept of Simula 67, and invented a queueing mechanism. Hoare refined the rules of process resumption. Brinch Hansen created the first implementation of monitors, in Concurrent Pascal. Hoare demonstrated their equivalence to semaphores.

Monitors (and Concurrent Pascal) were soon used to structure process synchronization in the Solo operating system.

Programming languages that have supported monitors include:

- Ada since Ada 95 (as protected objects)
- C# (and other languages that use the .NET Framework)
- Concurrent Euclid
- Concurrent Pascal
- D
- Delphi (Delphi 2009 and above, via TObject.Monitor)
- Java (via the wait and notify methods)
- Go
- Mesa
- Modula-3
- Python (via threading.Condition object)
- Ruby
- Squeak Smalltalk
- Turing, Turing+, and Object-Oriented Turing
- μC++
- Visual Prolog

A number of libraries have been written that allow monitors to be constructed in languages that do not support them natively. When library calls are used, it is up to the programmer to explicitly mark the start and end of code executed with mutual exclusion. Pthreads is one such library.
