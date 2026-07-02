---
title: "Dining philosophers (part 3/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/6
---

## Go

### Channels

Goroutine synchronization done with Go channels. Deadlock prevented by making one philosopher "left handed."

```mw
package main

import (
    "hash/fnv"
    "log"
    "math/rand"
    "os"
    "time"
)

// Number of philosophers is simply the length of this list.
// It is not otherwise fixed in the program.
var ph = []string{"Aristotle", "Kant", "Spinoza", "Marx", "Russell"}

const hunger = 3                // number of times each philosopher eats
const think = time.Second / 100 // mean think time
const eat = time.Second / 100   // mean eat time

var fmt = log.New(os.Stdout, "", 0) // for thread-safe output

var done = make(chan bool)

// This solution uses channels to implement synchronization.
// Sent over channels are "forks."
type fork byte

// A fork object in the program models a physical fork in the simulation.
// A separate channel represents each fork place.  Two philosophers
// have access to each fork.  The channels are buffered with capacity = 1,
// representing a place for a single fork.

// Goroutine for philosopher actions.  An instance is run for each
// philosopher.  Instances run concurrently.
func philosopher(phName string,
    dominantHand, otherHand chan fork, done chan bool) {
    fmt.Println(phName, "seated")
    // each philosopher goroutine has a random number generator,
    // seeded with a hash of the philosopher's name.
    h := fnv.New64a()
    h.Write([]byte(phName))
    rg := rand.New(rand.NewSource(int64(h.Sum64())))
    // utility function to sleep for a randomized nominal time
    rSleep := func(t time.Duration) {
        time.Sleep(t/2 + time.Duration(rg.Int63n(int64(t))))
    }
    for h := hunger; h > 0; h-- {
        fmt.Println(phName, "hungry")
        <-dominantHand // pick up forks
        <-otherHand
        fmt.Println(phName, "eating")
        rSleep(eat)
        dominantHand <- 'f' // put down forks
        otherHand <- 'f'
        fmt.Println(phName, "thinking")
        rSleep(think)
    }
    fmt.Println(phName, "satisfied")
    done <- true
    fmt.Println(phName, "left the table")
}

func main() {
    fmt.Println("table empty")
    // Create fork channels and start philosopher goroutines,
    // supplying each goroutine with the appropriate channels
    place0 := make(chan fork, 1)
    place0 <- 'f' // byte in channel represents a fork on the table.
    placeLeft := place0
    for i := 1; i < len(ph); i++ {
        placeRight := make(chan fork, 1)
        placeRight <- 'f'
        go philosopher(ph[i], placeLeft, placeRight, done)
        placeLeft = placeRight
    }
    // Make one philosopher left handed by reversing fork place
    // supplied to philosopher's dominant hand.
    // This makes precedence acyclic, preventing deadlock.
    go philosopher(ph[0], place0, placeLeft, done)
    // they are all now busy eating
    for range ph {
        <-done // wait for philosphers to finish
    }
    fmt.Println("table empty")
}
```

Output:

```
table empty
Kant seated
Marx seated
Spinoza seated
Aristotle seated
Kant hungry
Russell seated
Marx hungry
Russell hungry
Kant eating
Marx eating
Aristotle hungry
Spinoza hungry
Kant thinking
Marx thinking
Spinoza eating
Russell eating
Kant hungry
Russell thinking
Aristotle eating
Marx hungry
Spinoza thinking
Marx eating
Russell hungry
Marx thinking
Aristotle thinking
Russell eating
Kant eating
Russell thinking
Aristotle hungry
Kant thinking
Aristotle eating
Spinoza hungry
Spinoza eating
Marx hungry
Aristotle thinking
Russell hungry
Aristotle hungry
Kant hungry
Spinoza thinking
Kant eating
Marx eating
Marx thinking
Russell eating
Kant thinking
Marx satisfied
Marx left the table
Russell thinking
Aristotle eating
Spinoza hungry
Spinoza eating
Russell satisfied
Russell left the table
Kant satisfied
Kant left the table
Spinoza thinking
Aristotle thinking
Aristotle satisfied
Aristotle left the table
Spinoza satisfied
Spinoza left the table
table empty
```

### Mutexes and WaitGroup

The first solution just uses channels for synchronization. Channels can solve lots of problems but the sync library has a few other functions to more directly model common operations. In Dining Philosophers, fork use is mutually exclusive so it's very clear to model forks with sync.Mutex objects. Also waiting for a number of concurrent tasks to finish is a common pattern directly implemented with sync.WaitGroup.

One more concurrency technique actually used in both solutions is to use the log package for output rather than the fmt package. Output from concurrent goroutines can get accidentally interleaved in some cases. While neither package makes claims about this problem, the log package historically has been coded to avoid interleaved output.

```mw
package main

import (
    "hash/fnv"
    "log"
    "math/rand"
    "os"
    "sync"
    "time"
)

var ph = []string{"Aristotle", "Kant", "Spinoza", "Marx", "Russell"}

const hunger = 3
const think = time.Second / 100
const eat = time.Second / 100

var fmt = log.New(os.Stdout, "", 0)

var dining sync.WaitGroup

func philosopher(phName string, dominantHand, otherHand *sync.Mutex) {
    fmt.Println(phName, "seated")
    h := fnv.New64a()
    h.Write([]byte(phName))
    rg := rand.New(rand.NewSource(int64(h.Sum64())))
    rSleep := func(t time.Duration) {
        time.Sleep(t/2 + time.Duration(rg.Int63n(int64(t))))
    }
    for h := hunger; h > 0; h-- {
        fmt.Println(phName, "hungry")
        dominantHand.Lock() // pick up forks
        otherHand.Lock()
        fmt.Println(phName, "eating")
        rSleep(eat)
        dominantHand.Unlock() // put down forks
        otherHand.Unlock()
        fmt.Println(phName, "thinking")
        rSleep(think)
    }
    fmt.Println(phName, "satisfied")
    dining.Done()
    fmt.Println(phName, "left the table")
}

func main() {
    fmt.Println("table empty")
    dining.Add(5)
    fork0 := &sync.Mutex{}
    forkLeft := fork0
    for i := 1; i < len(ph); i++ {
        forkRight := &sync.Mutex{}
        go philosopher(ph[i], forkLeft, forkRight)
        forkLeft = forkRight
    }
    go philosopher(ph[0], fork0, forkLeft)
    dining.Wait() // wait for philosphers to finish
    fmt.Println("table empty")
}
```


## Groovy

Deadlocks are avoided by always getting locks on forks with lower numbers first.

```mw
import groovy.transform.Canonical

import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock

@Canonical
class Fork {
    String name
    Lock lock = new ReentrantLock()

    void pickUp(String philosopher) {
        lock.lock()
        println "  $philosopher picked up $name"
    }

    void putDown(String philosopher) {
        lock.unlock()
        println "  $philosopher put down $name"
    }
}

@Canonical
class Philosopher extends Thread {
    Fork f1
    Fork f2

    @Override
    void run() {
        def random = new Random()
        (1..20).each { bite ->
            println "$name is hungry"
            f1.pickUp name
            f2.pickUp name
            println "$name is eating bite $bite"
            Thread.sleep random.nextInt(300) + 100
            f2.putDown name
            f1.putDown name
        }
    }
}

void diningPhilosophers(names) {
    def forks = (1..names.size()).collect { new Fork(name: "Fork $it") }
    def philosophers = []
    names.eachWithIndex{ n, i ->
        def (i1, i2) = [i, (i + 1) % 5]
        if (i2 < i1) (i1, i2) = [i2, i]

        def p = new Philosopher(name: n, f1: forks[i1], f2: forks[i2])
        p.start()
        philosophers << p
    }
    philosophers.each { it.join() }
}

diningPhilosophers(['Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell'])
```


## Haskell

Using the built-in Software Transactional Memory in GHC.

```mw
module Philosophers where

import Control.Monad
import Control.Concurrent
import Control.Concurrent.STM
import System.Random

-- TMVars are transactional references. They can only be used in transactional actions.
-- They are either empty or contain one value. Taking an empty reference fails and
-- putting a value in a full reference fails. A transactional action only succeeds
-- when all the component actions succeed, else it rolls back and retries until it
-- succeeds.
-- The Int is just for display purposes.
type Fork = TMVar Int

newFork :: Int -> IO Fork
newFork i = newTMVarIO i

-- The basic transactional operations on forks
takeFork :: Fork -> STM Int
takeFork fork = takeTMVar fork

releaseFork :: Int -> Fork -> STM ()
releaseFork i fork = putTMVar fork i

type Name = String

runPhilosopher :: Name -> (Fork, Fork) -> IO ()
runPhilosopher name (left, right) = forever $ do
  putStrLn (name ++ " is hungry.")
  
  -- Run the transactional action atomically.
  -- The type system ensures this is the only way to run transactional actions.
  (leftNum, rightNum) <- atomically $ do
    leftNum <- takeFork left
    rightNum <- takeFork right
    return (leftNum, rightNum)
  
  putStrLn (name ++ " got forks " ++ show leftNum ++ " and " ++ show rightNum ++ " and is now eating.")
  delay <- randomRIO (1,10)
  threadDelay (delay * 1000000) -- 1, 10 seconds. threadDelay uses nanoseconds.
  putStrLn (name ++ " is done eating. Going back to thinking.")

  atomically $ do
    releaseFork leftNum left
    releaseFork rightNum right
    
  delay <- randomRIO (1, 10)
  threadDelay (delay * 1000000)

philosophers :: [String]
philosophers = ["Aristotle", "Kant", "Spinoza", "Marx", "Russel"]

main = do
  forks <- mapM newFork [1..5]
  let namedPhilosophers  = map runPhilosopher philosophers
      forkPairs          = zip forks (tail . cycle $ forks)
      philosophersWithForks = zipWith ($) namedPhilosophers forkPairs
  
  putStrLn "Running the philosophers. Press enter to quit."
  
  mapM_ forkIO philosophersWithForks
  
  -- All threads exit when the main thread exits.
  getLine
```


## Icon and Unicon

Icon doesn't support concurrency. This Unicon solution avoids deadlock and livelock (but not starvation) by not allowing philosophers to hold onto one fork if they can't get the other, and by having each philosopher pick up their lowest numbered fork first. The code would be slightly simpler if the philosophers wouldn't waste time waiting when they can't get both forks and went back to thinking instead. (Take away their grant money.)

```mw
global forks, names

procedure main(A)
    names := ["Aristotle","Kant","Spinoza","Marks","Russell"]
    write("^C to terminate")
    nP := *names
    forks := [: |mutex([])\nP :]
    every p := !nP do thread philosopher(p)
    delay(-1)
end

procedure philosopher(n)
    f1 := forks[min(n, n%*forks+1)]
    f2 := forks[max(n, n%*forks+1)]
    repeat {
        write(names[n]," thinking")
        delay(1000*?5)
        write(names[n]," hungry")
        repeat {
            fork1 := lock(f1)
            if fork2 := trylock(f2) then {
                write(names[n]," eating")
                delay(1000*?5)
                break (unlock(fork2), unlock(fork1))  # full
                }
            unlock(fork1)  # Free first fork and go back to waiting
            }
        }
end
```

A sample run, terminated after some time.

```
->dp
^C to terminate
Kant thinking
Spinoza thinking
Aristotle thinking
Russell thinking
Marks thinking
Kant hungry
Russell hungry
Kant eating
Spinoza hungry
Russell eating
Aristotle hungry
Marks hungry
Kant thinking
Spinoza eating
Russell thinking
Aristotle eating
Kant hungry
Spinoza thinking
Marks eating
Aristotle thinking
Kant eating
Russell hungry
Spinoza hungry
Russell eating
Marks thinking
Aristotle hungry
Kant thinking
Spinoza eating
Russell thinking
Marks hungry
Aristotle eating
Kant hungry
Spinoza thinking
Marks eating
Russell hungry
Aristotle thinking
Spinoza hungry
Kant eating
Russell eating
Marks thinking
Kant thinking
Marks hungry
Spinoza eating
Aristotle hungry
Russell thinking
Aristotle eating
^C
```


## J

### Using Threading Primitives

Currently, this only works under jconsole. (Unfortunately, QT requires all GUI interactions occur on the main thread, and as of j9.4, jqt has not been updated force this behavior, so do not use jqt here.)

Here, to prevent deadlock, philosophers always pick up forks in a specific order and always lay down their forks in the reverse order. This means that one philosopher (Marx) will use the opposite left/right order from the rest of the philosophers.

```mw
reqthreads=: {{ 0&T.@''^:(0>.y-1 T.'')0 }}
dispatchwith=: (t.'')every
newmutex=: (; 10&T.@0)@>
lock=: 11&T.@{:
unlock=: 13&T.@{:
dl=: 6!:3

dine=: {{
  'forkA forkB'=. <"1 /:~ n
  announce=. m {{ echo m,' ',y }}
  announce 'will use fork ',(":;{.forkA),' first and put it down last'
  announce 'will use fork ',(":;{.forkB),' second and put it down first'
  dl 1
  while. do.
    announce 'is hungry'
    lock forkA
    announce 'picked up fork ',":;{.forkA
    lock forkB
    announce 'picked up fork ',":;{.forkB
    announce 'is eating'
    dl 2+(?3e3)%1e3
    announce 'has finished eating'
    unlock forkB
    announce 'has put down fork ',":;{.forkB
    unlock forkA
    announce 'has put down fork ',":;{.forkA
    announce 'has left the room'
    dl 4+(?1e4)%1e3
  end.
  y
}}

start=: {{
  echo 'Hit enter to exit'
  dl 1
  reqthreads 5
  forks=. newmutex i.5
  for_philosopher.;:' Aristotle Kant Spinoza Marx Russell' do.
    forks=. 1|.forks
    (;philosopher) dine (2{.forks) dispatchwith EMPTY
  end.
  exit 1!:1]1
}}
```

Sample session:

```mw
   start''
Hit enter to exit
Aristotle will use fork 1 first and put it down last
Kant will use fork 2 first and put it down last
Marx will use fork 0 first and put it down last
Spinoza will use fork 3 first and put it down last
Russell will use fork 0 first and put it down last
Aristotle will use fork 2 second and put it down first
Kant will use fork 3 second and put it down first
Marx will use fork 4 second and put it down first
Spinoza will use fork 4 second and put it down first
Russell will use fork 1 second and put it down first
Spinoza is hungry
Marx is hungry
Aristotle is hungry
Aristotle picked up fork 1
Spinoza picked up fork 3
Marx picked up fork 0
Kant is hungry
Aristotle picked up fork 2
Spinoza picked up fork 4
Aristotle is eating
Spinoza is eating
Russell is hungry
Aristotle has finished eating
Spinoza has finished eating
Aristotle has put down fork 2
Kant picked up fork 2
Spinoza has put down fork 4
Marx picked up fork 4
Aristotle has put down fork 1
Spinoza has put down fork 3
Kant picked up fork 3
Marx is eating
Aristotle has left the room
Spinoza has left the room
Kant is eating
Kant has finished eating
Marx has finished eating
Kant has put down fork 3
Marx has put down fork 4
Kant has put down fork 2
Marx has put down fork 0
Russell picked up fork 0
Kant has left the room
Marx has left the room
Russell picked up fork 1
Russell is eating
```

### Older Emulations

These philosophers are very smart and polite: they figured out immediately that at most two of them can eat simultaneously (take the floor of n divided by 2 for n philosophers); so, when they are hungry and it is necessary, they wait in line. (In general, for n > 1, because they are very smart and polite, when a philosopher seats he leaves exactly one empty seat between himself and one of the philosophers which are already eating if any.)

J does not support concurrency; so, this is a discrete-event simulation (DES). The time spent thinking and eating is assumed to be exponentially distributed, respectively, at the rates of 1 and 0.5 per time unit.

#### The simulation code

The simulation is defined in terms of fixed tacit (stateless point-free) code (a Turing complete dialect of J; see, https://rosettacode.org/wiki/Universal_Turing_machine#J),

```mw
". noun define -. CRLF     NB. Fixed tacit simulation code...

simulate=.
''"_@:((<@:(1 -~ 1&({::)) 1} ])@:(([ 0 0&$@(1!:2&2)@:(((6j3 ": 9&({::)) , ': 
'"_) , ' starts waiting and thinking about hunger.' ,~ 8&({::) {:: 0&({::)))@
:(<@:(6&({::) , 8&({::)) 6} ])@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} 
])@:(3 8 2&{)) 2} ])@:(<@:2: 3} ]))@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {::
 ])} ])@:(5 8 4&{)) 4} ])@:(<@:_: 5} ]))`(([ 0 0&$@(1!:2&2)@:(((6j3 ": 9&({::
)) , ': '"_) , ' starts eating.' ,~ 8&({::) {:: 0&({::)))@:((<@:((0 (0 {:: ])
`(<@:(1 {:: ]))`(2 {:: ])} ])@:(3 8 2&{)) 2} ])@:(<@:1: 3} ]))@:((<@:((0 (0 {
:: ])`(<@:(1 {:: ]))`(2 {:: ])} ])@:(5 8 4&{)) 4} ])@:(<@:(_2 * ^.@:?@:0:) 5}
 ])))@.(7&({::) > 1 +/@:= 2&({::))`((<@:(}.@:(6&({::))) 6} ])@:(([ 0 0&$@(1!:
2&2)@:(((6j3 ": 9&({::)) , ': '"_) , ' starts eating.' ,~ 8&({::) {:: 0&({::)
))@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} ])@:(3 8 2&{)) 2} ])@:(<@:1:
 3} ]))@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} ])@:(5 8 4&{)) 4} ])@:(
<@:(_2 * ^.@:?@:0:) 5} ])))@:(<@:({.@:(6&({::))) 8} ])^:(1 <: #@:(6&({::)))@:
([ 0 0&$@(1!:2&2)@:(((6j3 ": 9&({::)) , ': '"_) , ' starts thinking.' ,~ 8&({
::) {:: 0&({::)))@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} ])@:(3 8 2&{)
) 2} ])@:(<@:0: 3} ]))@:((<@:((0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} ])@:(5 8
 4&{)) 4} ])@:(<@:(_1 * ^.@:?@:0:) 5} ])))@.('' ($ ,) 8&({::) { 2&({::)))@:(<
@:(0 I.@:= 4&({::)) 8} ])@:(<@:((- <./)@:(4&({::))) 4} ])@:(<@:(9&({::) + <./
@:(4&({::))) 9} ])^:(0 < 1&({::))^:_)@:(([ 0 0&$@(1!:2&2)@:(((6j3 ": 9&({::))
 , ': '"_) , 'All of them start thinking.'"_))@:((0 ; <.@:(2 %~ #@:(0&({::)))
) 9 7} ])@:((0:"_1 ,&< (_1 * ^.@:?@:0:)&>)@:(0&({::)) 2 4} ])@:((;:@:(0&({::)
) ,&< ''"_) 0 6} ]))@:(,&(;:8$','))@:;        

)
```

#### Simulation of 11 chronological events for five philosophers

```mw
   'Aristotle Kant Spinoza Marx Russell' simulate 11
 0.000: All of them start thinking.
 0.097: Spinoza starts eating.
 0.474: Aristotle starts eating.
 0.950: Russell starts waiting and thinking about hunger.
 1.125: Kant starts waiting and thinking about hunger.
 2.263: Spinoza starts thinking.
 2.263: Russell starts eating.
 2.762: Marx starts waiting and thinking about hunger.
 2.771: Spinoza starts waiting and thinking about hunger.
 4.769: Russell starts thinking.
 4.769: Kant starts eating.
 4.845: Russell starts waiting and thinking about hunger.
 5.166: Aristotle starts thinking.
 5.166: Marx starts eating.
 5.915: Marx starts thinking.
 5.915: Spinoza starts eating.
```

#### Simulation of 22 chronological events for eight philosophers

```mw
   'Aristotle Kant Spinoza Marx Russell Laozi Nezahualcoyotl Averroes' simulate 22
 0.000: All of them start thinking.
 0.077: Nezahualcoyotl starts eating.
 0.312: Marx starts eating.
 0.424: Laozi starts eating.
 0.502: Kant starts eating.
 0.541: Marx starts thinking.
 0.545: Marx starts eating.
 0.660: Laozi starts thinking.
 0.715: Laozi starts eating.
 0.766: Aristotle starts waiting and thinking about hunger.
 0.871: Laozi starts thinking.
 0.871: Aristotle starts eating.
 0.893: Averroes starts waiting and thinking about hunger.
 1.035: Nezahualcoyotl starts thinking.
 1.035: Averroes starts eating.
 1.071: Laozi starts waiting and thinking about hunger.
 1.168: Kant starts thinking.
 1.168: Laozi starts eating.
 1.614: Russell starts waiting and thinking about hunger.
 1.660: Spinoza starts waiting and thinking about hunger.
 1.813: Aristotle starts thinking.
 1.813: Russell starts eating.
 2.022: Marx starts thinking.
 2.022: Spinoza starts eating.
 2.164: Russell starts thinking.
 2.182: Aristotle starts eating.
 2.339: Marx starts waiting and thinking about hunger.
 2.446: Aristotle starts thinking.
 2.446: Marx starts eating.
```

#### The structured derivation of the verb (function)

The fixed tacit code of the verb (simulate) was produced by means of an unorthodox tacit toolkit; however, the verb produced is orthodox (compliant):

```mw
NB. Quick and dirty tacit toolkit...
 
o=. @:
c=."_
 
ver=. (0:`)([:^:)
 
d=. (fix=. (;:'f.')ver) (train=.(;:'`:')ver&6) (an=. <@:((,'0') (,&<) ]))
ver=. (an f. o fix'ver')ver o an f. 
z=. ((an'')`($ ,)`) (`:6)
d=. (a0=. `'') (a1=. (@[) ((<'&')`) (`:6)) (a2=. (`(<(":0);_)) (`:6))
av=. ((an o fix'a0')`)  (`(an o fix'a1')) (`(an o fix'a2') ) (`:6)
 
Fetch=. (ver o train ;:'&{::')&.> o i. f.av
tie=. ver o train ;:'`'
 
indices=. (, $~ 1 -.~ $) o (train"0 o ((1 -: L.)S:1 # <S:1) o (tie&'') o fix :: ])
f=. ((ver o train ;:'&{')) o indices o train f.av
 
'A B'=. 2 Fetch
head=. (;:'<@:') {.~ 2 * 1 = #@[
h=. train o (indices o train o (A f) (head , (B f)@] , < o an@[  , (;:'}]')c) ]) f.av
 
DropIfNB=. < o ('('"_ , ] , ')'"_) o ((}: ^: ('NB.' -: 3&{. o > o {:)) &. ;:)
pipe=. ([ , ' o ' , ])&:>/ o |.
 
is=. ". o (, o ": o > , '=. ' , pipe o (DropIfNB;._2) o ". o ('0 ( : 0)'c)) f.av
 
NB.--------------------------------------------------------------------------------------
   
NB. Producing the verb simulate...

Note 0

NB. X and Y...
  N - Philosophers names 
  C - Number of chronological events to simulate

NB. Local...
  A - Activity (0 - Thinking, 1 -eating, 2 - Thinking while queuing,)
  B - New activity
  T - Residual time left for the activity
  S - Starting time for the new activity
  Q - Queue
  U - Upper bound for the number of philosophers who can eat simultaneously
  P - Active philosopher
  E - Elapsed Time (only for information purposes)
)

amend=. 0 (0 {:: ])`(<@:(1 {:: ]))`(2 {:: ])} ]

'N C A B T S Q U P E'=. 10 Fetch  NB. 10 Boxes

thinktime=. _1 * ^. o ? o 0:  NB. Exponentially distributed at a rate of one
eattime  =. _2 * ^. o ? o 0:  NB. Exponentially distributed at a rate of one-half
j=. ,&<

time=. (6j3 ": E) , ': 'c

start is
  (N Q)`((;: o N) j (''c))            h NB. Boxing the names, empty queue
  (A T)`((0:items j thinktime&>) o N) h NB. All start thinking
  (E U)`(0 ; <. o (2 %~ # o N))       h NB. Elapsed time 0, Upper bound
  [ echo o (time , 'All of them start thinking.'c)
)

CanEat=. U > 1 +/ o = A   NB. Can eat if there is a suitable place at the table

eat is
  T`(amend o ((S P T)f))h o (S`eattime h)  NB. Eating time
  A`(amend o ((B P A)f))h o (B`1:      h)  NB. Activity: eating
  [ echo o (time , ' starts eating.' ,~ P {:: N)
)

enqueue is
  T`(amend o ((S P T)f))h o (S`_:h) NB. Inactive until someone else ends eating
  A`(amend o ((B P A)f))h o (B`2:h) NB. Activity: thinking while queuing
  Q`(Q , P)h                        NB. Enqueuing
  [ echo o (time , ' starts waiting and thinking about hunger.' ,~ P {:: N)
)

thinking=. enqueue`eat@.CanEat  NB. Either enqueues or eats after thinking

dequeue is
  P`({. o Q)h  NB. Activating the one in front of the queue 
  eat          NB. and starts eating
  Q`(}. o Q)h  NB. dequeuing
)

eating is  NB. Thinks after eating
  T`(amend o ((S P T)f))h o (S`thinktime h) NB. Thinking time
  A`(amend o ((B P A)f))h o (B`0:        h) NB. Activity: thinking
  [ echo o ( time , ' starts thinking.' ,~ P {:: N)
  dequeue ^: (1 <: # o Q)     NB. Dequeuing a philosopher (if possible)
)

update is
  E`(E + <./ o T)h            NB. Updating the elapsed time
  T`((- <./)@:T) h            NB. Updating the residual times
  P`(0 I. o = T) h            NB. Setting the active philosopher
  thinking`eating@.((P { A)z) NB. Was thinking or eating?
  C`(1 -~ C)     h            NB. One chronological event completed
)

simulate is NB. Discrete event simulation (dyadic verb)
  ;                           NB. Linking the arguments (N C)
  ,&(;:8$',')                 NB. Appending 8 local boxes (A B T S Q U P E)
  start
  update ^: (0 < C) ^: _      NB. Updating while events are less than C
  ''c
)

simulate=. simulate f.

NB. The simulation code is produced by the sentence,
NB. 77 (-@:[ ]\ 5!:5@<@:]) 'simulate'
```


## Java

This Java implementation uses a token system. If a philosopher's number is on the token, they pick up their left and right forks. Passing the token to their immediate neighbor would be pointless, so they increment the token by 2, passing it to the philosopher after their neighbor. The +2 works well for odd numbers of philosophers. With wait down at 1 millisecond I get about 1.5M eats/sec running 5 philosophers, down to about 0.5M eats/sec running 25. The single token generates good availability for 80% of 5 forks, but a much lower availability % of 25 forks.

```mw
package diningphilosophers;

import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

enum PhilosopherState { Get, Eat, Pon }

class Fork {
    public static final int ON_TABLE = -1;
    static int instances = 0;
    public int id;
    public AtomicInteger holder = new AtomicInteger(ON_TABLE);

    Fork() { id = instances++; }
}

class Philosopher implements Runnable {
    static final int maxWaitMs = 100;                          //  must be > 0
    static AtomicInteger token = new AtomicInteger(0);
    static int instances = 0;
    static Random rand = new Random();
    AtomicBoolean end = new AtomicBoolean(false);
    int id;
    PhilosopherState state = PhilosopherState.Get;
    Fork left;
    Fork right;
    int timesEaten = 0;

    Philosopher() {
        id = instances++;
        left = Main.forks.get(id);
        right = Main.forks.get((id+1)%Main.philosopherCount);
    }

    void sleep() { try { Thread.sleep(rand.nextInt(maxWaitMs)); }
        catch (InterruptedException ex) {} }

    void waitForFork(Fork fork) {
        do {
            if (fork.holder.get() == Fork.ON_TABLE) {
                fork.holder.set(id);                //  my id shows I hold it
                return;
            } else {                                //  someone still holds it
                sleep();                            //  check again later
            }
        } while (true);
    }

    public void run() {
        do {
            if (state == PhilosopherState.Pon) {    //  all that pondering
                state = PhilosopherState.Get;       //  made me hungry
            } else { // ==PhilosopherState.Get
                if (token.get() == id) {            //  my turn now
                    waitForFork(left);
                    waitForFork(right);             //  Ah needs me some foahks!
                    token.set((id+2)% Main.philosopherCount);
                    state = PhilosopherState.Eat;
                    timesEaten++;
                    sleep();                        //  eat for a while
                    left.holder.set(Fork.ON_TABLE);
                    right.holder.set(Fork.ON_TABLE);
                    state = PhilosopherState.Pon;   //  ponder for a while
                    sleep();
                } else {                    //  token.get() != id, so not my turn
                    sleep();
                }
            }
        } while (!end.get());
    }
}

public class Main {
    static final int philosopherCount = 5; //  token +2 behavior good for odd #s
    static final int runSeconds = 15;
    static ArrayList<Fork> forks = new ArrayList<Fork>();
    static ArrayList<Philosopher> philosophers = new ArrayList<Philosopher>();

    public static void main(String[] args) {
        for (int i = 0 ; i < philosopherCount ; i++) forks.add(new Fork());
        for (int i = 0 ; i < philosopherCount ; i++)
            philosophers.add(new Philosopher());
        for (Philosopher p : philosophers) new Thread(p).start();
        long endTime = System.currentTimeMillis() + (runSeconds * 1000);

        do {                                                    //  print status
            StringBuilder sb = new StringBuilder("|");

            for (Philosopher p : philosophers) {
                sb.append(p.state.toString());
                sb.append("|");            //  This is a snapshot at a particular
            }                              //  instant.  Plenty happens between.

            sb.append("     |");

            for (Fork f : forks) {
                int holder = f.holder.get();
                sb.append(holder==-1?"   ":String.format("P%02d",holder));
                sb.append("|");
            }
            
            System.out.println(sb.toString());
            try {Thread.sleep(1000);} catch (Exception ex) {}
        } while (System.currentTimeMillis() < endTime);

        for (Philosopher p : philosophers) p.end.set(true);
        for (Philosopher p : philosophers)
            System.out.printf("P%02d: ate %,d times, %,d/sec\n",
                p.id, p.timesEaten, p.timesEaten/runSeconds);
    }
}
```

**Output:**

```
|Eat|Get|Eat|Get|Get|     |P00|P00|P02|P02|P04|
|Eat|Get|Get|Get|Get|     |P00|P00|   |   |   |
|Get|Get|Get|Get|Get|     |   |   |   |   |   |
|Get|Pon|Get|Pon|Get|     |P00|   |   |   |   |
|Eat|Get|Get|Get|Get|     |P00|P00|   |   |   |
|Get|Eat|Get|Get|Pon|     |   |P01|P01|   |   |
|Pon|Get|Eat|Get|Eat|     |P04|   |P02|P02|P04|
|Get|Get|Get|Get|Pon|     |   |   |   |P03|   |
|Pon|Get|Eat|Pon|Get|     |   |   |P02|P02|P04|
|Get|Eat|Pon|Get|Eat|     |P04|P01|P01|   |   |
|Get|Pon|Get|Get|Get|     |   |   |   |P03|   |
|Eat|Get|Get|Pon|Get|     |P00|P00|   |   |   |
|Get|Pon|Get|Get|Get|     |P00|   |   |   |   |
|Get|Get|Eat|Get|Eat|     |P04|P01|P02|P02|P04|
|Pon|Pon|Eat|Get|Get|     |   |   |P02|P02|   |
P00: ate 59 times, 3/sec
P01: ate 59 times, 3/sec
P02: ate 59 times, 3/sec
P03: ate 59 times, 3/sec
P04: ate 59 times, 3/sec
```


## JoCaml

### Minimal simple solution

This solution allows a philosopher to take only two forks at once, or none at all. This is achieved by making each fork into a channel, and guarding the eating process by two forks. There are two channels for each philosopher: a thinking philosopher and a hungry philosopher.

What this simple solution achieves:

- no deadlock (waiting for forks forever)
- no "livelock" (trying to pick up and put down forks forever)
- philosophers can eat at any time (no fixed order is imposed)

Deficiencies of this solution:

- Supports only a fixed set of philosophers, since all channels are declared statically. More philosophers needs more lines of code.
- The mean time of waiting while hungry is not bounded and grows very slowly (logarithmically) with time.

```mw
let random_wait n = Unix.sleep (Random.int n);;
let print s m = Printf.printf "philosopher %s is %s\n" s m; flush(stdout);;
let will_eat s = print s "eating"; random_wait 10;;
let will_think s = print s "thinking"; random_wait 20; print s "hungry";;

  (* a,b,c,d,e are thinking philosophers; ah,bh,ch,dh,eh are the same philosophers when hungry;
     fab is the fork located between philosophers a and b; similarly for fbc, fcd, ... *)

def  ah() & fab() & fea() = will_eat "Aristotle"; a() & fab() & fea() 
 or  bh() & fab() & fbc() = will_eat "Kant";      b() & fab() & fbc() 
 or  ch() & fbc() & fcd() = will_eat "Spinoza";   c() & fbc() & fcd() 
 or  dh() & fcd() & fde() = will_eat "Marx";      d() & fcd() & fde() 
 or  eh() & fde() & fea() = will_eat "Russell";   e() & fde() & fea()

 and a() = will_think "Aristotle"; ah()
 and b() = will_think "Kant";      bh()
 and c() = will_think "Spinoza";   ch()
 and d() = will_think "Marx";      dh()
 and e() = will_think "Russell";   eh()
;; 
spawn fab() & fbc() & fcd() & fde() & fea() & a() & b() & c() & d() & e();;
```

Sample output:

```
philosopher Aristotle is thinking
philosopher Russell is thinking
philosopher Marx is thinking
philosopher Kant is thinking
philosopher Spinoza is thinking
philosopher Kant is hungry
philosopher Kant is eating
philosopher Kant is thinking
philosopher Russell is hungry
philosopher Russell is eating
philosopher Russell is thinking
philosopher Spinoza is hungry
philosopher Spinoza is eating
philosopher Spinoza is thinking
philosopher Spinoza is hungry
philosopher Spinoza is eating
philosopher Spinoza is thinking
philosopher Aristotle is hungry
philosopher Aristotle is eating
philosopher Marx is hungry
philosopher Marx is eating
philosopher Russell is hungry
philosopher Aristotle is thinking
philosopher Russell is eating
philosopher Marx is thinking
philosopher Kant is hungry
philosopher Kant is eating
philosopher Russell is thinking
philosopher Kant is thinking
```

### Simple solution with statistics

This solution is logically the same as the "minimal simple" solution above, but now the timing information is printed. Statistical information is also printed on hungry waiting time before eating: average among all instances of eating, and maximum time ever waited by anyone.

```mw
let print s t m = Printf.printf "t=%d: philosopher %s is %s\n" t s m; flush(stdout);;
let random_wait n = Unix.sleep (Random.int n);;

(* auxiliary function to keep track of time ticks, using integer seconds *)
def  ts () & counter(n) = counter(n) & reply n to ts
or   update_counter() & counter(n) = counter(n+1) & reply to update_counter
and  counter_sentinel() = Unix.sleep 1; update_counter(); counter_sentinel()
;;
spawn counter(0) & counter_sentinel();;

def stats(n, waited, maxwaited) & report_wait_time(m) =
 let (n', waited', maxwaited') = (n+1, waited+m, max maxwaited m) in 
 Printf.printf "waiting average %f, max waited %d\n" 
   (float_of_int waited' /. float_of_int n') 
   maxwaited';
 flush(stdout);
 stats(n',waited',maxwaited') & reply () to report_wait_time
;;

spawn stats(0,0,0);;

let eat s t = print s t "eating"; random_wait 10;; 
let think s = print s (ts()) "thinking"; random_wait 20;;

(* "p" will be a philosopher channel, to be defined later
 the messages ah, bh, ... do not need to be injected now. *)

let will_eat s t = let t' = ts() in report_wait_time(t'-t); eat s t';;

def ah(t,p) & fab() & fea() = will_eat "Aristotle" t; p() & fab() & fea() 
or  bh(t,p) & fab() & fbc() = will_eat "Kant" t; p() & fab() & fbc() 
or  ch(t,p) & fbc() & fcd() = will_eat "Spinoza" t; p() & fbc() & fcd() 
or  dh(t,p) & fcd() & fde() = will_eat "Marx" t; p() & fcd() & fde() 
or  eh(t,p) & fde() & fea() = will_eat "Russell" t; p() & fde() & fea()
;;

spawn fab() & fbc() & fcd() & fde() & fea();;

(* define the thinking -> hungry transitions using local philosophers, and inject the philosophers *)
List.map 
 (fun (h,s) -> def p() = think s; let t = ts() in print s t "hungry"; h(t,p) in spawn p())
 [(ah,"Aristotle"); (bh,"Kant"); (ch,"Spinoza"); (dh,"Marx"); (eh,"Russell")]
;; 
(* this replaces repetitive code such as that shown in the previous solution *)

(* now we need to wait and do nothing; nobody will be able to inject godot() *)
def wait_forever() & godot() = reply () to wait_forever in wait_forever();;
```

Sample output (excerpt):

```
t=2: philosopher Aristotle is thinking
t=3: philosopher Aristotle is hungry
waiting average 0.000000, max waited 0
t=3: philosopher Aristotle is eating
t=3: philosopher Aristotle is thinking
t=4: philosopher Russell is hungry
waiting average 0.000000, max waited 0
t=4: philosopher Russell is eating
t=5: philosopher Marx is hungry
t=5: philosopher Kant is hungry
waiting average 0.000000, max waited 0
t=5: philosopher Kant is eating
waiting average 0.666667, max waited 4
t=9: philosopher Marx is eating
t=9: philosopher Russell is thinking
t=14: philosopher Kant is thinking
t=17: philosopher Marx is thinking
t=18: philosopher Marx is hungry
waiting average 0.571429, max waited 4
t=18: philosopher Marx is eating
t=19: philosopher Spinoza is hungry
t=20: philosopher Aristotle is hungry
waiting average 0.500000, max waited 4
t=20: philosopher Aristotle is eating
t=24: philosopher Russell is hungry
waiting average 1.000000, max waited 5
t=24: philosopher Marx is thinking
t=24: philosopher Spinoza is eating
t=26: philosopher Kant is hungry
waiting average 1.300000, max waited 5
t=28: philosopher Russell is eating
t=28: philosopher Aristotle is thinking
t=31: philosopher Russell is thinking
t=33: philosopher Marx is hungry
waiting average 1.181818, max waited 5
t=33: philosopher Marx is eating
```

### Fair solution

This solution implements "fairness" -- if two neighbors are hungry, the one who waited more will eat first. The waiting time for each philosopher is bounded by twice the maximum eating time.

```mw
#!/usr/bin/jocamlrun jocaml

(* eating and thinking between 0 and this-1 *)
let eating_max_interval = 10;;
let thinking_max_interval = 10;;
let number_of_philosophers = 5;;
let random_wait n = Unix.sleep (Random.int n);;

(* counter for unique timestamp, not related to time in seconds *)
def get_current_time () & unique_ts_counter(n) = unique_ts_counter(n+1) & reply n to get_current_time;;
spawn unique_ts_counter(0);;

(* functions that wait and print diagnostics *)
let name i = List.nth ["Aristotle"; "Kant"; "Spinoza"; "Marx"; "Russell"] i;;
let message i m = Printf.printf "philosopher %s is %s\n" (name i) m; flush(stdout);;
let eat i = message i "eating"; random_wait eating_max_interval;; 
let think i = message i "thinking"; random_wait thinking_max_interval;;

type philosopher_state_t = Eating | Hungry of int | Thinking;;

(* initial states *)
let states = Array.make number_of_philosophers Thinking;;
(* one philosopher's processes *)
let make_philosopher i got_hungry done_eating =
 def hungry() & forks() = eat i ; done_eating(i) & thinking()
 and thinking() = think i; got_hungry(i) & hungry()
 in spawn thinking(); forks
;;

(* deciding who will eat first *)
let next_phil i = (i+1) mod number_of_philosophers;;
let prev_phil i = (number_of_philosophers+i-1) mod number_of_philosophers;;
let is_hungry p = match p with
    | Hungry h -> true
    | _ -> false;;
let not_eating p = match p with
    | Eating -> false
    | _ -> true;;
let is_more_hungry p q = match q with
    | Hungry hj -> (
    	match p with
	    | Hungry hi -> hi <= hj
	    | _ -> false
    )
    | _ -> true
;;

let may_eat_first i =
  is_hungry states.(i)
  && not_eating states.(next_phil i) && not_eating states.(prev_phil i)
  && is_more_hungry states.(i) states.(next_phil i) 
  && is_more_hungry states.(i) states.(prev_phil i);;

let decide_eating i =
 if (may_eat_first i) then (states.(i) <- Eating; true)
 else false;;

def waiter(all_forks) & got_hungry(i) =
 states.(i) <- Hungry (get_current_time());
 let will_eat = decide_eating i in (
 waiter(all_forks) & (if will_eat then all_forks.(i)() else 0)
)
or  waiter(all_forks) & done_eating(i) =
  states.(i) <- Thinking;
  let next_will_eat = decide_eating (next_phil i) in
  let prev_will_eat = decide_eating (prev_phil i) in (
 waiter(all_forks)
  & (if next_will_eat then all_forks.(next_phil i)() else 0)
  & (if prev_will_eat then all_forks.(prev_phil i)() else 0)
 );;

let all_forks = Array.init number_of_philosophers (fun i -> make_philosopher i got_hungry done_eating)
in spawn waiter(all_forks);;

(* now we need to wait and do nothing; nobody will be able to inject godot() *)

def wait_forever() & godot() = reply () to wait_forever in wait_forever();;
```

Sample output:

```
philosopher Aristotle is thinking
philosopher Kant is thinking
philosopher Marx is thinking
philosopher philosopher Spinoza is thinking
Russell is thinking
philosopher Spinoza is eating
philosopher Spinoza is thinking
philosopher Marx is eating
philosopher Marx is thinking
philosopher Marx is eating
philosopher Marx is thinking
philosopher Aristotle is eating
philosopher Aristotle is thinking
philosopher Kant iphilosopher s eating
Russell is eating
philosopher Russell is thinking
philosopher Kant is thinking
philosopher Spinoza is eating
philosopher Spinoza is thinking
philosopher Marx is eating
```


## Julia

Pentagonal table with assigned seats. Aristotle, seated on the north side, takes his left fork first since he was left-handed, see historical note in http://time.com/3107557/top-10-lefties/ and the others take the right fork first. The forks are represented by 5 channels. One lefty's taking left fork before right prevents deadlocks (see C solution).

```mw
mutable struct Philosopher
    name::String
    hungry::Bool
    righthanded::Bool
    rightforkheld::Channel
    leftforkheld::Channel
    function Philosopher(name, leftfork, rightfork)
        this = new()
        this.name = name
        this.hungry = rand([false, true]) # not specified so start as either
        this.righthanded   = (name == "Aristotle") ? false : true
        this.leftforkheld  = leftfork
        this.rightforkheld = rightfork
        this
    end
end

mutable struct FiveForkTable
    fork51::Channel
    fork12::Channel
    fork23::Channel
    fork34::Channel
    fork45::Channel    
    function FiveForkTable()
        this = new()
        this.fork51 = Channel(1); put!(this.fork51, "fork") # start with one fork per channel
        this.fork12 = Channel(1); put!(this.fork12, "fork") 
        this.fork23 = Channel(1); put!(this.fork23, "fork") 
        this.fork34 = Channel(1); put!(this.fork34, "fork") 
        this.fork45 = Channel(1); put!(this.fork45, "fork") 
        this
    end
end

table = FiveForkTable();
tasks = [Philosopher("Aristotle", table.fork12, table.fork51),
         Philosopher("Kant", table.fork23, table.fork12),
         Philosopher("Spinoza", table.fork34, table.fork23),
         Philosopher("Marx", table.fork45, table.fork34),
         Philosopher("Russell", table.fork51, table.fork45)]

function dine(t,p)
    if p.righthanded
       take!(p.rightforkheld); println("$(p.name) takes right fork")
       take!(p.leftforkheld); println("$(p.name) takes left fork")
    else
       take!(p.leftforkheld); println("$(p.name) takes left fork")
       take!(p.rightforkheld); println("$(p.name) takes right fork")
    end    
end

function leavetothink(t, p)
    put!(p.rightforkheld, "fork"); println("$(p.name) puts down right fork")
    put!(p.leftforkheld, "fork");  println("$(p.name) puts down left fork")
end

contemplate(t) = sleep(t)

function dophil(p, t, fullaftersecs=2.0, hungryaftersecs=10.0)
    while true
        if p.hungry
            println("$(p.name) is hungry")
            dine(table, p)
            sleep(fullaftersecs)
            p.hungry = false
            leavetothink(t, p)
        else
            println("$(p.name) is out of the dining room for now.")
            contemplate(hungryaftersecs)
            p.hungry = true
        end
    end
end

function runall(tasklist)
    for p in tasklist
        @async dophil(p, table)
    end
    while true begin sleep(5) end end
end

runall(tasks)
```

**Output:**

Aristotle is out of the dining room for now. Kant is out of the dining room for now. Spinoza is hungry Spinoza takes right fork Spinoza takes left fork Marx is hungry Russell is hungry Russell takes right fork Russell takes left fork Spinoza puts down right fork Spinoza puts down left fork Spinoza is out of the dining room for now. Marx takes right fork Marx takes left fork Russell puts down right fork Russell puts down left fork Russell is out of the dining room for now. Marx puts down right fork Marx puts down left fork Marx is out of the dining room for now. Aristotle is hungry Aristotle takes left fork Aristotle takes right fork Kant is hungry Aristotle puts down right fork Aristotle puts down left fork Aristotle is out of the dining room for now. Kant takes right fork Kant takes left fork Spinoza is hungry Russell is hungry Russell takes right fork Russell takes left fork Kant puts down right fork Kant puts down left fork Kant is out of the dining room for now. Spinoza takes right fork Spinoza takes left fork Marx is hungry Russell puts down right fork Russell puts down left fork Russell is out of the dining room for now. Spinoza puts down right fork Spinoza puts down left fork Spinoza is out of the dining room for now. Marx takes right fork Marx takes left fork Marx puts down right fork Marx puts down left fork Marx is out of the dining room for now. Aristotle is hungry Aristotle takes left fork Aristotle takes right fork Aristotle puts down right fork Aristotle puts down left fork Aristotle is out of the dining room for now. Kant is hungry Kant takes right fork Kant takes left fork Russell is hungry Russell takes right fork Russell takes left fork Kant puts down right fork Kant puts down left fork Kant is out of the dining room for now. Spinoza is hungry Spinoza takes right fork Spinoza takes left fork Russell puts down right fork Russell puts down left fork Russell is out of the dining room for now.


## Kotlin

Translation of

:

Groovy

As noted in the Groovy entry, deadlocks are avoided by always getting locks on forks with lower numbers first.

```mw
// Version 1.2.31

import java.util.Random
import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock

val rand = Random()

class Fork(val name: String) {
    val lock = ReentrantLock()

    fun pickUp(philosopher: String) {
        lock.lock()
        println("  $philosopher picked up $name")
    }

    fun putDown(philosopher: String) {
        lock.unlock()
        println("  $philosopher put down $name")
    }
}

class Philosopher(val pname: String, val f1: Fork, val f2: Fork) : Thread() {
    override fun run() {
        (1..20).forEach {
            println("$pname is hungry")
            f1.pickUp(pname)
            f2.pickUp(pname)
            println("$pname is eating bite $it")
            Thread.sleep(rand.nextInt(300) + 100L)
            f2.putDown(pname)
            f1.putDown(pname)
        }
    }
}

fun diningPhilosophers(names: List<String>) {
    val size = names.size
    val forks = List(size) { Fork("Fork ${it + 1}") }
    val philosophers = mutableListOf<Philosopher>()
    names.forEachIndexed { i, n ->
        var i1 = i
        var i2 = (i + 1) % size
        if (i2 < i1) {
            i1 = i2
            i2 = i
        }
        val p = Philosopher(n, forks[i1], forks[i2])
        p.start()
        philosophers.add(p)
    }
    philosophers.forEach { it.join() }
}

fun main(args: Array<String>) {
    val names = listOf("Aristotle", "Kant", "Spinoza", "Marx", "Russell")
    diningPhilosophers(names)
}
```
