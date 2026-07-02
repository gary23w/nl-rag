---
title: "Dining philosophers (part 2/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/6
---

## Common Lisp

Library:

Bordeaux Threads

This is a translation of the Python solution with small improvements.

Random times are calculated based upon a normal distribution; the main loop doesn't sleep to wait for all philosophers to end dining, it uses a condition variable instead.

```mw
(in-package :common-lisp-user)

;;
;; FLAG -- if using quicklisp, you can get bordeaux-threads loaded up 
;; with: (ql:quickload :bordeaux-threads)
;;

(defvar *philosophers* '(Aristotle Kant Spinoza Marx Russell))
 
(defclass philosopher ()
  ((name :initarg :name :reader name-of)
   (left-fork :initarg :left-fork :accessor left-fork-of)
   (right-fork :initarg :right-fork :accessor right-fork-of)
   (meals-left :initarg :meals-left :accessor meals-left-of)))
 
(defclass fork ()
  ((lock :initform (bt:make-lock "fork") :reader lock-of)))
 
(defun random-normal (&optional (mean 0.0) (sd 1.0))
  (do* ((x1 #1=(1- (* 2.0d0 (random 1d0))) #1#)
        (x2 #2=(1- (* 2.0d0 (random 1d0))) #2#)
        (w  #3=(+ (* x1 x1) (* x2 x2)) #3#))
      ((< w 1d0) (+ (* (* x1 (sqrt (/ (* -2d0 (log w)) w))) sd) mean))))
 
(defun sleep* (time) (sleep (max time (/ (expt 10 7)))))
 
(defun dining-philosophers (&key (philosopher-names *philosophers*)
                                 (meals 30)
                                 (dining-time'(1 2))
                                 (thinking-time '(1 2))
                                 ((stream e) *error-output*))
  (let* ((count (length philosopher-names))
         (forks (loop repeat count collect (make-instance 'fork)))
         (philosophers (loop for i from 0
                             for name in philosopher-names collect
                               (make-instance 'philosopher
                                    :left-fork (nth (mod i count) forks)
                                    :right-fork (nth (mod (1+ i) count) forks)
                                    :name name
                                    :meals-left meals)))
         (condition (bt:make-condition-variable))
         (lock (bt:make-lock "main loop")) 
         (output-lock (bt:make-lock "output lock")))
    (dolist (p philosophers) 
      (labels ((think ()
                 (/me "is now thinking")
                 (sleep* (apply #'random-normal thinking-time))
                 (/me "is now hungry")
                 (dine))
               (dine ()
                 (bt:with-lock-held ((lock-of (left-fork-of p)))
                   (or (bt:acquire-lock (lock-of (right-fork-of p)) nil)
                       (progn (/me "couldn't get a fork and ~
                                    returns to thinking")
                              (bt:release-lock (lock-of (left-fork-of p)))
                              (return-from dine (think))))
                   (/me "is eating")
                   (sleep* (apply #'random-normal dining-time))
                   (bt:release-lock (lock-of (right-fork-of p)))
                   (/me "is done eating (~A meals left)"
                        (decf (meals-left-of p))))
                 (cond ((<= (meals-left-of p) 0)
                        (/me "leaves the dining room")
                        (bt:with-lock-held (lock)
                          (setq philosophers (delete p philosophers))
                          (bt:condition-notify condition)))
                       (t (think))))
               (/me (control &rest args)
                 (bt:with-lock-held (output-lock)
                   (write-sequence (string (name-of p)) e)
                   (write-char #\Space e)
                   (apply #'format e (concatenate 'string control "~%")
                          args))))
        (bt:make-thread #'think))) 
    (loop (bt:with-lock-held (lock)
            (when (endp philosophers)
              (format e "all philosophers are done dining~%") 
              (return)))
          (bt:with-lock-held (lock)
            (bt:condition-wait condition lock)))))
```

Alternative solution using library STMX which provides Software Transactional Memory, as well as BORDEAUX-THREADS above. Depends on Quicklisp. TAKE will wait until something is available in a TCELL, then remove it. PUT will wait for a TCELL to become empty, then add it. ATOMIC ensures STM operations in its body happen atomically.

```mw
(ql:quickload '(:stmx :bordeaux-threads))

(defpackage :dining-philosophers
  (:use :cl))

(in-package :dining-philosophers)

(defstruct philosopher
  name
  left-fork
  right-fork)

(defparameter *philosophers* '("Aristotle" "Kant" "Spinoza" "Marx" "Russell"))
(defparameter *eating-max* 5.0)
(defparameter *thinking-max* 5.0)
(defvar *log-lock* (bt:make-lock))
(defvar *running* nil)

(defun print-log (name status)
  (bt:with-lock-held (*log-lock*)
    (format t "~a is ~a~%" name status)))

(defun philosopher-cycle (philosopher)
  "Continously atomically grab and return the left and right forks of the given PHILOSOPHER."
  (with-slots (name left-fork right-fork) philosopher
    (loop while *running*
       do
         (print-log name "hungry")
         (stmx:atomic
          (stmx.util:take left-fork)
          (stmx.util:take right-fork))
         (print-log name "eating")
         (sleep (random *eating-max*))
         (stmx:atomic
          (stmx.util:put left-fork t)
          (stmx.util:put right-fork t))
         (print-log name "thinking")
         (sleep (random *thinking-max*)))))

(defun scenario ()
  (let ((forks (loop repeat (length *philosophers*) collect (stmx.util:tcell t))))
    (setf *running* t)
    (loop for name in *philosophers*
       for left-fork in forks
       for right-fork in (append (cdr forks) (list (car forks)))
       do (let ((philosopher (make-philosopher :name name :left-fork left-fork :right-fork right-fork)))
            (bt:make-thread (lambda () (philosopher-cycle philosopher))
                            :initial-bindings (cons (cons '*standard-output* *standard-output*)
                                                    bt:*default-special-bindings*))))))
```

**Output:**

```mw
DINING-PHILOSOPHERS> (scenario)
Aristotle is hungry
Aristotle is eating
Kant is hungry
Spinoza is hungry
Spinoza is eating
Marx is hungry
NIL
Russell is hungry
Aristotle is thinking
Russell is eating
Spinoza is thinking
Kant is eating
Spinoza is hungry
Russell is thinking
Marx is eating
Kant is thinking
Aristotle is hungry
Aristotle is eating
Marx is thinking
Spinoza is eating
Spinoza is thinking
Marx is hungry
Marx is eating
Russell is hungry
Marx is thinking
Kant is hungry
Aristotle is thinking
Russell is eating
Kant is eating
Marx is hungry
Spinoza is hungry
Kant is thinking
Spinoza is eating
Kant is hungry
Aristotle is hungry
Russell is thinking
Aristotle is eating
Aristotle is thinking
Aristotle is hungry
Aristotle is eating
Spinoza is thinking
Marx is eating
...
```


## D

This code is using a strict order for the forks/mutexes to prevent a deadlock.

```mw
import std.stdio, std.algorithm, std.string, std.parallelism,
       core.sync.mutex;

void eat(in size_t i, in string name, Mutex[] forks) {
    writeln(name, " is hungry.");
    immutable j = (i + 1) % forks.length;

    // Take forks i and j. The lower one first to prevent deadlock.
    auto fork1 = forks[min(i, j)];
    auto fork2 = forks[max(i, j)];

    fork1.lock;
    scope(exit) fork1.unlock;

    fork2.lock;
    scope(exit) fork2.unlock;

    writeln(name, " is eating.");
    writeln(name, " is full.");
}

void think(in string name) {
    writeln(name, " is thinking.");
}

void main() {
    const philosophers = "Aristotle Kant Spinoza Marx Russell".split;
    Mutex[philosophers.length] forks;
    foreach (ref fork; forks)
        fork = new Mutex;

    defaultPoolThreads = forks.length;
    foreach (i, philo; taskPool.parallel(philosophers)) {
        foreach (immutable _; 0 .. 100) {
            eat(i, philo, forks);
            philo.think;
        }
    }
}
```

**Sample output:**

```
Spinoza is full.
Spinoza is thinking.
Russel is eating.
Russel is full.
Russel is thinking.
Russel is hungry.
Kant is eating.
Kant is full.
Kant is thinking.
Kant is hungry.
Spinoza is hungry.
Aristotle is eating.
Aristotle is full.
```


## Delphi

Library:

Classes

Library:

SysUtils

Library:

SyncObjs

Translation of

:

Pascal

Just a fix of Pascal version to run in Delphi

```mw
program dining_philosophers;
uses
  Classes,
  SysUtils,
  SyncObjs;

const
  PHIL_COUNT   = 5;
  LIFESPAN     = 7;
  DELAY_RANGE  = 950;
  DELAY_LOW    = 50;
  PHIL_NAMES: array[1..PHIL_COUNT] of string = ('Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell');
type
  TFork        = TCriticalSection;
//  TPhilosopher = class;
  TPhilosopher = class(TThread)
  private
    FName: string;
    FFirstFork, FSecondFork: TFork;
  protected
    procedure Execute; override;
  public
    constructor Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
  end;

var
  Forks: array[1..PHIL_COUNT] of TFork;
  Philosophers: array[1..PHIL_COUNT] of TPhilosopher;

procedure TPhilosopher.Execute;
var
  LfSpan: Integer;
begin
  LfSpan := LIFESPAN;
  while LfSpan > 0 do
    begin
      Dec(LfSpan);
      WriteLn(FName, ' sits down at the table');
      FFirstFork.Acquire;
      FSecondFork.Acquire;
      WriteLn(FName, ' eating');
      Sleep(Random(DELAY_RANGE) + DELAY_LOW);
      FSecondFork.Release;
      FFirstFork.Release;
      WriteLn(FName, ' is full and leaves the table');
      if LfSpan = 0 then
        continue;
      WriteLn(FName, ' thinking');
      Sleep(Random(DELAY_RANGE) + DELAY_LOW);
      WriteLn(FName, ' is hungry');
    end;
end;

constructor TPhilosopher.Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
begin
  inherited Create(True);
  FName := aName;
  if aForkIdx1 < aForkIdx2 then
    begin
      FFirstFork := Forks[aForkIdx1];
      FSecondFork := Forks[aForkIdx2];
    end
  else
    begin
      FFirstFork := Forks[aForkIdx2];
      FSecondFork := Forks[aForkIdx1];
    end;
end;

procedure DinnerBegin;
var
  I: Integer;
  Phil: TPhilosopher;
begin
  for I := 1 to PHIL_COUNT do
    Forks[I] := TFork.Create;
  for I := 1 to PHIL_COUNT do
    Philosophers[I] := TPhilosopher.Create(PHIL_NAMES[I], I, Succ(I mod PHIL_COUNT));
  for Phil in Philosophers do
    Phil.Start;
end;

procedure WaitForDinnerOver;
var
  Phil: TPhilosopher;
  Fork: TFork;
begin
  for Phil in Philosophers do
    begin
      Phil.WaitFor;
      Phil.Free;
    end;
  for Fork in Forks do
    Fork.Free;
end;

begin
  Randomize;
  DinnerBegin;
  WaitForDinnerOver;
  readln;
end.
```


## E

A classic article on solving a version of this problem in E is Satan Comes to Dinner in E.


## EchoLisp

We introduce a laquais who checks that no more than 4 philosophers are sitting at the same time. This prevents deadlocks. Reference : The little book of semaphores.

```mw
(lib 'tasks)

(define names #(Aristotle Kant Spinoza Marx Russell))
(define abouts #("Wittgenstein" "the nature of the World" "Kant"  "starving" 
    "spaghettis" "the essence of things" "Ω" "📞" "⚽️" "🍅" "🌿" 
    "philosophy" "💔"  "👠" "rosetta code" "his to-do list" ))
(define (about) (format "thinking about %a." (vector-ref abouts (random (vector-length abouts)))))

;; statistics
(define rounds (make-vector 5 0))
(define (eat i) (vector-set! rounds i (1+ (vector-ref rounds i))))
 
;; forks are resources = semaphores
(define (left i) i)
(define (right i) (modulo (1+ i) 5))
(define forks (for/vector ((i 5)) (make-semaphore 1)))
(define (fork i) (vector-ref forks i))

(define laquais (make-semaphore 4))

;; philosophers tasks
(define (philo i)
;; thinking
       (writeln (vector-ref names i) (about))
    (sleep (+ 2000 (random 1000)))
    (wait laquais)
;; get forks
       (writeln (vector-ref names i) 'sitting)
    (wait (fork (left i)))
    (wait (fork (right i)))
       (writeln (vector-ref names i) 'eating)
       (eat i)
       (sleep (+ 6000 (random 1000)))
;; put-forks
    (signal (fork (left i)))
    (signal (fork (right i)))
    (signal laquais)
  i)
(define tasks (for/vector ((i 5)) (make-task philo i)))
```

**Output:**

```mw
(define (observe dummmy)
		(writeln 'observer 'rounds= rounds)
		#t)
(define observer (make-task observe #t ))

(define (dinner) 
	(task-run observer 5000)
	(for ((t tasks)) (task-run t)))

(dinner)
```

Marx thinking about philosophy. Russell thinking about Kant. Aristotle thinking about 🌿. Spinoza thinking about Ω. Kant thinking about 🍅. Marx sitting Marx eating Russell sitting Aristotle sitting Aristotle eating Spinoza sitting observer rounds= #( 1 0 0 1 0) observer rounds= #( 1 0 0 1 0) Spinoza eating Marx thinking about 🍅. Kant sitting Russell eating Aristotle thinking about 💔. observer rounds= #( 1 0 1 1 1) Marx sitting Kant eating Aristotle sitting Spinoza thinking about Ω. observer rounds= #( 1 1 1 1 1) Marx eating Russell thinking about 🌿. Spinoza sitting observer rounds= #( 1 1 1 2 1) Russell sitting Aristotle eating Kant thinking about 💔. Spinoza eating Marx thinking about 📞. Kant sitting observer rounds= #( 2 1 2 2 1) Russell eating Marx sitting Aristotle thinking about Kant. Kant eating Spinoza thinking about spaghettis. observer rounds= #( 2 2 2 2 2) Aristotle sitting observer rounds= #( 2 2 2 2 2) Spinoza sitting Marx eating Russell thinking about 📞. Aristotle eating Kant thinking about the essence of things. Russell sitting [...] CTRL-C to stop.


## Eiffel

Works with

:

EiffelStudio

version 6.8, with provisional syntax enabled

This solution for the dining philosophers is programmed in Eiffel using Simple Concurrent Object-Oriented Programming (SCOOP). In SCOOP for Eiffel, the keyword `separate` in a declaration designates that the associated object may be handled by a SCOOP processor other than (separate from) the one handling the current object. So, in this example, philosophers and forks are all declared as separate types.

The synchronization of access to the resources (the forks) occurs when the routine `eat` is called. The two arguments are the two separate forks adjacent to the philosopher. The `eat` routine will not proceed until exclusive access to all separate arguments is assured. The resources are released when the routine terminates.

The example uses numbers (versus names) to identify the philosophers in order to allow the user to vary the number of philosophers.

```mw
class
    DINING_PHILOSOPHERS

create
    make

feature -- Initialization

    make
            -- Create philosophers and forks.
        local
            first_fork: separate FORK
            left_fork: separate FORK
            right_fork: separate FORK
            philosopher: separate PHILOSOPHER
            i: INTEGER
        do
            print ("Dining Philosophers%N" + philosopher_count.out + " philosophers, " + round_count.out + " rounds%N%N")
            create philosophers.make
            from
                i := 1
                create first_fork.make (philosopher_count, 1)
                left_fork := first_fork
            until
                i > philosopher_count
            loop
                if i < philosopher_count then
                    create right_fork.make (i, i + 1)
                else
                    right_fork := first_fork
                end
                create philosopher.make (i, left_fork, right_fork, round_count)
                philosophers.extend (philosopher)
                left_fork := right_fork
                i := i + 1
            end
            philosophers.do_all (agent launch_philosopher)
            print ("Make Done!%N")
        end

feature {NONE} -- Implementation

    philosopher_count: INTEGER = 5
            -- Number of philosophers.

    round_count: INTEGER = 30
            -- Number of times each philosopher should eat.

    philosophers: LINKED_LIST [separate PHILOSOPHER]
            -- List of philosophers.

    launch_philosopher (a_philosopher: separate PHILOSOPHER)
            -- Launch a_philosopher.
        do
            a_philosopher.live
        end

end -- class DINING_PHILOSOPHERS
```

```mw
class
    PHILOSOPHER

create
    make

feature -- Initialization

    make (philosopher: INTEGER; left, right: separate FORK; rounds: INTEGER)
            -- Initialize with ID of `philosopher', forks `left' and `right', and for `rounds' times to eat.
        require
            valid_id: philosopher >= 1
            valid_times_to_eat: rounds >= 1
        do
            id := philosopher
            left_fork := left
            right_fork := right
            round_count := rounds
            report ("announced")
        ensure
            id_set: id = philosopher
            left_fork_set: left_fork = left
            right_fork_set: right_fork = right
            rounds_set: round_count = rounds
        end

feature -- Access

    id: INTEGER
            -- Philosopher's id.

feature -- Basic operations

    live
            -- Model philosopher's life.
        do
            from
                report ("joined")
                has_eaten_count := 0
            until
                has_eaten_count >= round_count
            loop
                think
                eat (left_fork, right_fork)
            end
            report ("done")
        end

    eat (left, right: separate FORK)
            -- Eat, having acquired `left' and `right' forks.
        do
                -- Take forks.
            report ("taking forks")
            left.pick (Current)
            right.pick (Current)
                -- Eat.
            report ("eating")
            delay (200)
                -- Put forks back.
            report ("putting forks back")
            left.put (Current)
            right.put (Current)
                -- Report statistics.
            has_eaten_count := has_eaten_count + 1
            report ("has eaten " + has_eaten_count.out + " times")
        end

    think
            -- Think ... for a short time.
        do
            report ("thinking")
            delay (400)
        end

feature {NONE} -- Output

    report (task: STRING)
            -- Report about execution of the specified `task'.
        do
            print ("Philosopher " + id.out + ": " + task + ".%N")
        end

feature {NONE} -- Timing

    delay (milliseconds: INTEGER_64)
            -- Delay execution by `milliseconds'.
        do
            (create {EXECUTION_ENVIRONMENT}).sleep (milliseconds * 1_000_000)
        end

feature {NONE} -- Status

    round_count: INTEGER
            -- Number of times philosopher should eat.

    has_eaten_count: INTEGER
            -- Number of times philosopher has eaten so far.

    left_fork: separate FORK
            -- Left fork used for eating.	

    right_fork: separate FORK
            -- Right fork used for eating.

invariant
    valid_id: id >= 1
    valid_round_count: round_count >= 1
    valid_has_eaten_count: has_eaten_count <= round_count

end -- class PHILOSOPHER
```

```mw
class
    FORK

create
    make

feature -- Initialization

    make (left, right: INTEGER)
            -- Initialize between philosophers `left' and `right'.
        do
            id := left.out + "F" + right.out
        end

feature -- Access

    id: STRING
            -- Identification: `F' enclosed by adjacent philosopher id's.

feature -- Basic operations

    pick (philosopher: separate PHILOSOPHER)
            -- Report fork picked up.
        do
            print ("Fork " + id + " picked up by Philosopher " + philosopher.id.out + ".%N")
        end

    put (philosopher: separate PHILOSOPHER)
            -- Report fork put back.
        do
            print ("Fork " + id + " put back by Philosopher " + philosopher.id.out + ".%N")
        end

end -- class FORK
```


## Elixir

Implements the Chandy-Misra algorithm.

```mw
defmodule Philosopher do
 
  defstruct missing: [], clean: [], promised: []
 
  def run_demo do
    pid1 = spawn(__MODULE__, :init, ["Russell"])
    pid2 = spawn(__MODULE__, :init, ["Marx"])
    pid3 = spawn(__MODULE__, :init, ["Spinoza"])
    pid4 = spawn(__MODULE__, :init, ["Kant"])
    pid5 = spawn(__MODULE__, :init, ["Aristotle"])
 
    # a chopstick is simply represented by the pid of the neighbour that shares it.
 
    send(pid1, {:run, %Philosopher{}})
    send(pid2, {:run, %Philosopher{missing: [pid1]}})
    send(pid3, {:run, %Philosopher{missing: [pid2]}})
    send(pid4, {:run, %Philosopher{missing: [pid3]}})
    send(pid5, {:run, %Philosopher{missing: [pid1, pid4]}})
  end
 
  def init(philosopher_name) do
    receive do
      {:run, state} ->
        spawn(__MODULE__, :change_state, [self()])
        case flip_coin() do
          :heads -> thinking(philosopher_name, state)
          :tails -> hungry(philosopher_name, state)
        end
    end
  end
 
  defp thinking(philosopher_name, state) do
    receive do
      {:change_state} ->
        hungry(philosopher_name, state)
      {:chopstick_request, pid} ->
        if clean?(pid, state) do
          thinking(philosopher_name, promise_chopstick(philosopher_name, pid, state))
        else
          give_chopstick(philosopher_name, self(), pid)
          %{missing: missing} = state
          thinking(philosopher_name, %{state | missing: [pid | missing]})
        end
    end
  end
 
  defp hungry(philosopher_name, state) do
    IO.puts "#{philosopher_name} is hungry."
    %{missing: missing} = state
    for pid <- missing, do: request_chopstick(philosopher_name, self(), pid)
    wait_for_chopsticks(philosopher_name, state)
  end
 
  defp wait_for_chopsticks(philosopher_name, state) do
    if has_chopsticks?(state) do
      eating(philosopher_name, state)
    end
    receive do
      {:chopstick_request, pid} ->
        if clean?(pid, state) do
          wait_for_chopsticks(philosopher_name, promise_chopstick(philosopher_name, pid, state))
        else
          give_chopstick(philosopher_name, self(), pid)
          request_chopstick(philosopher_name, self(), pid)
          %{missing: missing} = state
          wait_for_chopsticks(philosopher_name, %{state | missing: [pid | missing]})
        end
      {:chopstick_response, pid} ->
        %{missing: missing, clean: clean} = state
        wait_for_chopsticks(philosopher_name, %{state | missing: List.delete(missing, pid), clean: [pid | clean]})
    end
  end
 
  defp eating(philosopher_name, state) do
    IO.puts "*** #{philosopher_name} is eating."
    receive do
      {:change_state} ->
        %{promised: promised} = state
        for pid <- promised, do: give_chopstick(philosopher_name, self(), pid)
        thinking(philosopher_name, %Philosopher{missing: promised})
    end
  end
 
  defp clean?(pid, state) do
    %{clean: clean} = state
    Enum.member?(clean, pid)
  end
  
  defp has_chopsticks?(state) do
    %{missing: missing} = state
    Enum.empty?(missing)
  end
 
  defp promise_chopstick(philosopher_name, pid, state) do
    IO.puts "#{philosopher_name} promises a chopstick."
    %{promised: promised} = state
    %{state | promised: [pid | promised]}
  end
 
  defp request_chopstick(philosopher_name, snd_pid, recv_pid) do
    IO.puts "#{philosopher_name} requests a chopstick."
    send(recv_pid, {:chopstick_request, snd_pid})
  end
 
  defp give_chopstick(philosopher_name, snd_pid, recv_pid) do
    IO.puts "#{philosopher_name} gives a chopstick."
    send(recv_pid, {:chopstick_response, snd_pid})
  end
  
  defp flip_coin do
    case Enum.random(0..1) do
      0 -> :heads
      1 -> :tails
    end
  end	
  
  def change_state(pid) do
    Process.sleep(Enum.random(1..10) * 1000)
    send(pid, {:change_state})
    change_state(pid)
  end
```


## Erlang

### Waiter-based

```mw
%%% 
%%% to compile and run:
%%% $ erl 
%%%   > c(rosetta).
%%% {ok,rosetta}
%%%   > rosetta:dining().
%%%
%%% contributor: bksteele
%%%
-module(rosetta).
-export([dining/0]).

sleep(T) ->
    receive
        after T ->
    true
    end.

doForks(ForkList) ->
    receive
        {grabforks, {Left, Right}} ->
            doForks(ForkList -- [Left, Right]);
        {releaseforks, {Left, Right}} -> 
            doForks([Left, Right| ForkList]);
        {available, {Left, Right}, Sender} ->
            Sender ! {areAvailable,
                lists:member(Left, ForkList)
                andalso lists:member(Right, ForkList)},
            doForks(ForkList);
        {die} -> io:format("Forks put away.~n")
    end.

areAvailable(Forks) ->
    forks ! {available, Forks, self()},
    receive
        {areAvailable, false} -> false;
        {areAvailable, true} -> true
    end.

processWaitList([]) -> false;
processWaitList([H|T]) ->
    {Client, Forks} = H,
    case areAvailable(Forks) of
        true -> Client ! {served},
                true;
        false -> processWaitList(T)
    end.

doWaiter([], 0, 0, false) ->
    forks ! {die},
    io:format("Waiter is leaving.~n"),
    diningRoom ! {allgone};
doWaiter(WaitList, ClientCount, EatingCount, Busy) ->
    receive
        {waiting, Client} ->
            WaitList1 = [Client|WaitList],    
            % add to waiting list
            case (not Busy) and (EatingCount<2) of
            true ->    
                Busy1 = processWaitList(WaitList1);
            false -> Busy1 = Busy
            end,
            doWaiter(WaitList1, ClientCount, EatingCount, Busy1);

        {eating, Client} ->
          doWaiter(WaitList -- [Client], ClientCount, EatingCount+1, false);

        {finished} ->
            doWaiter(WaitList, ClientCount, EatingCount-1,
            processWaitList(WaitList));
        {leaving} ->
            doWaiter(WaitList, ClientCount-1, EatingCount, Busy)
    end.

philosopher(Name, _Forks, 0) ->
    io:format("~s is leaving.~n", [Name]),
    waiter ! {leaving};
philosopher(Name, Forks, Cycle) ->
    io:format("~s is thinking.~n", [Name]),
    sleep(rand:uniform(1000)),
    io:format("~s is hungry.~n", [Name]),
    % sit at table
    waiter ! {waiting, {self(), Forks}},

    receive
        {served} -> forks ! {grabforks, Forks},
            % grab forks
            waiter ! {eating, {self(), Forks}},    
            % start eating
            io:format("~s is eating.~n", [Name])
    end,

    sleep(rand:uniform(1000)),
    % put forks down
    forks ! {releaseforks, Forks},                 
    waiter ! {finished},

    philosopher(Name, Forks, Cycle-1).

dining() ->    AllForks = [1, 2, 3, 4, 5],
    Clients = 5,
    register(diningRoom, self()),

    register(forks, 
        spawn(fun() -> doForks(AllForks) end)),
    register(waiter, 
        spawn(fun() -> doWaiter([], Clients, 0, false) end)),
    % run for 7 cycles
    Life_span = 7,
    spawn(fun() -> philosopher('Aristotle', {5, 1}, Life_span) end),
    spawn(fun() -> philosopher('Kant', {1, 2}, Life_span) end),
    spawn(fun() -> philosopher('Spinoza', {2, 3}, Life_span) end),
    spawn(fun() -> philosopher('Marx', {3, 4}, Life_span) end),
    spawn(fun() -> philosopher('Russell', {4, 5}, Life_span) end),

    receive
        {allgone} -> io:format("Dining room closed.~n")

    end,
    unregister(diningRoom).
```

Output:

```
Eshell V9.2  (abort with ^G)
1> c(rosetta).
{ok,rosetta}
2> rosetta:dining().
Aristotle is thinking.
Kant is thinking.
Spinoza is thinking.
Marx is thinking.
Russell is thinking.
Russell is hungry.
Russell is eating.
Kant is hungry.
Kant is eating.
Russell is thinking.
Aristotle is hungry.
Spinoza is hungry.
Marx is hungry.
Marx is eating.
Russell is hungry.
Kant is thinking.
Aristotle is eating.
Marx is thinking.
Spinoza is eating.
Kant is hungry.
Spinoza is thinking.
Aristotle is thinking.
Kant is eating.
Marx is hungry.
Marx is eating.
Marx is thinking.
Russell is eating.
Spinoza is hungry.
Aristotle is hungry.
Marx is hungry.
Kant is thinking.
Spinoza is eating.
Russell is thinking.
Aristotle is eating.
Russell is hungry.
Spinoza is thinking.
Marx is eating.
Spinoza is hungry.
Kant is hungry.
Aristotle is thinking.
Kant is eating.
Marx is thinking.
Russell is eating.
Aristotle is hungry.
Marx is hungry.
Russell is thinking.
Marx is eating.
Russell is hungry.
Kant is thinking.
Aristotle is eating.
Aristotle is thinking.
Marx is thinking.
Russell is eating.
Marx is hungry.
Spinoza is eating.
Aristotle is hungry.
Spinoza is thinking.
Spinoza is hungry.
Spinoza is eating.
Spinoza is thinking.
Spinoza is hungry.
Spinoza is eating.
Kant is hungry.
Russell is thinking.
Aristotle is eating.
Aristotle is thinking.
Spinoza is thinking.
Kant is eating.
Aristotle is hungry.
Marx is eating.
Russell is hungry.
Kant is thinking.
Aristotle is eating.
Kant is hungry.
Marx is thinking.
Spinoza is hungry.
Spinoza is eating.
Spinoza is thinking.
Aristotle is thinking.
Kant is eating.
Aristotle is hungry.
Russell is eating.
Spinoza is hungry.
Marx is hungry.
Kant is thinking.
Spinoza is eating.
Russell is thinking.
Aristotle is eating.
Spinoza is leaving.
Marx is eating.
Marx is thinking.
Marx is hungry.
Marx is eating.
Russell is hungry.
Aristotle is thinking.
Kant is hungry.
Kant is eating.
Marx is leaving.
Russell is eating.
Kant is thinking.
Russell is thinking.
Aristotle is hungry.
Aristotle is eating.
Aristotle is leaving.
Russell is hungry.
Russell is eating.
Kant is hungry.
Kant is eating.
Russell is leaving.
Kant is leaving.
Waiter is leaving.
Forks put away.
Dining room closed.
true
3> halt().
```

### Free-thinkers

```mw
%%% This version uses free-running 'phil' agents (actors) and
%%% state machines representing the forks.
%%%
%%% Usage to compile and run:
%%% $ erl
%%%   > c(dining).
%%%   {ok,dining}
%%%   > dining:start().
%%%

-module( dining).
-export(
    [ start/0
    ]).
-vsn( 1).
-date( '6/2020').
-author( bksteele).
-email( 'drbenkman@gmail.com').

%% fork messages: grab | drop | quit
%% a quit message is accepted only when State = available
%% @param Id numeric identification of object 
%% @param State: available | in_use

fork( Id, available ) ->
    receive
    { From, Who, grab} ->
        From ! { self(), Who, Id}
        , fork( Id, in_use)
    ;
    { From, quit} ->
        From ! { quit}
        , ok
    end
    ;
fork( Id, in_use ) ->
    receive
    { From, Who, drop} ->
        From ! { self(), Who, Id}
        , fork( Id, available)
    end
    .

%% sleep/1 : Integer -> ok
%% sleep pauses a process for T milliseconds.
%% @param T milliseconds for the time period

sleep(T) ->
    receive
        after T -> true
    end
    .

%% grab/2 : Pid String -> ()
%% Fork is the shared resource (a process object).
%% Who is the name of the acting process.
%% grab encapsulates message transmission.
%% @param Fork pid to which to send messages
%% @param Who name of the sender

grab( Fork, Who) ->
    Fork ! { self(), Who, grab}
    , receive
    { Fork, Who, _Id} -> ok
    end
    .

%% drop/2 : Pid String -> ()
%% Fork is the shared resource (a process object).
%% Who is the name of the acting process.
%% drop encapsulates message transmission.
%%
%% @param Fork pid to which to send messages
%% @param Who name of the sender

drop( Fork, Who) ->
    Fork ! { self(), Who, drop}
    , receive
    { Fork, Who, _Id} -> ok
    end
    .

%% phil/3 : String List{Id,Pid} Integer -> ok
%% phil/3 philosopher process uses a fork process.
%% phil uses two fork objects for n eating cycles.
%% A phil needs the pids of resource to communicate,
%% and the names of the fork resources it uses.
%% @param Name the string name of the philosopher
%% @param List{Id, Pid} 2 pairs of Id and Fork
%% @param Cycle the number of cycles to run

phil( Name, [{LId, Left}, {RId, Right}], Cycle)
    when LId > RId ->
        % swap so that process picks numerically lower first.
        % the swap introduces asymmetry to prevent deadlock.
        phil( Name, {RId, Right}, {LId, Left}, Cycle)
    ;
phil( Name, [{LId, Left}, {RId, Right}], Cycle) ->
    phil( Name, {LId, Left}, {RId, Right}, Cycle).

%% phil/4 : String {LId,LeftF} {RId,RightF} Integer -> ok
%% phil/4 philosopher process uses a fork process.
%% phil uses two fork objects for n eating cycles.
%% A phil needs pids of resource to communicate
%% and the names of the fork resources it uses.
%% @param Name the string name of the philosopher
%% @param {LeftId, Fork} pair of Id and Fork pid
%% @param {RightId, Fork} pair of Id and Fork pid
%% @param Cycle the number of cycles to run

phil( Name, _LFork, _RFork, 0) ->
    io:format( "~s is done.~n", [Name])
    ;
phil( Name, {LId, Left}, {RId, Right}, Cycle) ->

    io:format( "~s is thinking.~n", [Name])
    , sleep( rand:uniform( 1000))
    , io:format( "~s is hungry.~n", [Name])

    , grab( Left, Name)
    , grab( Right, Name)

    , io:format( "~s is eating.~n", [Name])
    , sleep( rand:uniform( 1000))

    , drop( Left, Name)
    , drop( Right, Name)

    , phil( Name, [{LId, Left}, {RId, Right}]
        , Cycle - 1)
    .

%% make_forks/1 : N -> List{Id, Fork}

make_forks( N) when N > 0 -> make_forks( N, []).

%% make_forks/2 : N List{Id, Fork}

make_forks( 0, Forks ) -> lists:reverse( Forks)
    ;
make_forks( N, Forks) ->
    % create and run the fork processes
    Pair = { N, spawn( 
        fun() -> fork( N, available) end) }
    , make_forks( N-1
            , lists:append( Forks, [Pair] ))
    .

%% make_phils/2 : Names, ForkList -> List{String}

make_phils( Names, Forks)
    when length( Names) > 0 ->
        make_phils( Names, Forks, [])
    .

%% make_phils/3 : Names Forks PL -> List{Fun}
%% make_phil/3 hard-codes the eat cycle count to 7

make_phils( [], _Forks, PhilList) -> PhilList
    ;
make_phils( [Hn|Tn], [Lf, Rf |FList], PhilList) ->
    % create a phil process function but do not run yet
    Phil = fun() -> phil( Hn, [Lf, Rf], 7) end
    , make_phils( Tn, rot( [Lf, Rf |FList], 1)
                , lists:append( PhilList, [Phil]))
    .

%% rot/2 : List Num -> List
%% rotate or roll a list by N slots, and return new list

rot( List, 0 ) -> List
    ;
rot( [H], 1 ) -> [H]
    ;
rot( [H|List], N ) ->
    rot( lists:append( List, [H]), N - 1)
    .

%% start free-running philosopher agents competing for Forks
%% start is fixed with N = 5 philosophers and 5 forks.

start() ->
    % create Fork list
    N = 5
    , Forks = make_forks( N)

    , Names = [ "Aristotle", "Kant"
              , "Spinoza", "Marx", "Russell"]

    , Phils = make_phils( Names, Forks)

    % run the philosophers now
    , [spawn( P) || P <- Phils]
    , ok
    .
```

Output:

```
Eshell V9.2  (abort with ^G)
1> c(dining).
{ok,dining}
2> dining:start().
Aristotle is thinking.
Kant is thinking.
Spinoza is thinking.
Marx is thinking.
Russell is thinking.
ok
Kant is hungry.
Kant is eating.
Marx is hungry.
Marx is eating.
Marx is thinking.
Spinoza is hungry.
Aristotle is hungry.
Russell is hungry.
Marx is hungry.
Marx is eating.
Aristotle is eating.
Kant is thinking.
Spinoza is eating.
Marx is thinking.
Aristotle is thinking.
Russell is eating.
Kant is hungry.
Russell is thinking.
Marx is hungry.
Russell is hungry.
Russell is eating.
Kant is eating.
Spinoza is thinking.
Aristotle is hungry.
Kant is thinking.
Russell is thinking.
Marx is eating.
Aristotle is eating.
Russell is hungry.
Aristotle is thinking.
Kant is hungry.
Kant is eating.
Kant is thinking.
Aristotle is hungry.
Spinoza is hungry.
Kant is hungry.
Spinoza is eating.
Marx is thinking.
Russell is eating.
Marx is hungry.
Russell is thinking.
Kant is eating.
Spinoza is thinking.
Marx is eating.
Spinoza is hungry.
Marx is thinking.
Russell is hungry.
Marx is hungry.
Marx is eating.
Aristotle is eating.
Kant is thinking.
Spinoza is eating.
Marx is thinking.
Spinoza is thinking.
Spinoza is hungry.
Spinoza is eating.
Kant is hungry.
Aristotle is thinking.
Russell is eating.
Russell is thinking.
Marx is hungry.
Kant is eating.
Spinoza is thinking.
Marx is eating.
Aristotle is hungry.
Russell is hungry.
Aristotle is eating.
Kant is thinking.
Kant is hungry.
Marx is thinking.
Marx is hungry.
Marx is eating.
Aristotle is thinking.
Kant is eating.
Spinoza is hungry.
Marx is done.
Russell is eating.
Kant is thinking.
Spinoza is eating.
Spinoza is thinking.
Aristotle is hungry.
Kant is hungry.
Kant is eating.
Russell is thinking.
Aristotle is eating.
Kant is done.
Russell is hungry.
Spinoza is hungry.
Spinoza is eating.
Aristotle is thinking.
Russell is eating.
Aristotle is hungry.
Russell is thinking.
Aristotle is eating.
Russell is hungry.
Spinoza is thinking.
Aristotle is thinking.
Russell is eating.
Spinoza is hungry.
Spinoza is eating.
Aristotle is hungry.
Spinoza is done.
Russell is done.
Aristotle is eating.
Aristotle is done.
3> halt().
```


## Euphoria

```mw
constant FREE = 0, LOCKED = 1
sequence forks
forks = repeat(FREE,5)

procedure person(sequence name, integer left_fork, integer right_fork)
    while 1 do
        while forks[left_fork] = LOCKED or forks[right_fork] = LOCKED do
            if forks[left_fork] = FREE then
                puts(1, name & " hasn't right fork.\n")
            elsif forks[right_fork] = FREE then
                puts(1, name & " hasn't left fork.\n")
            else
                puts(1, name & " hasn't both forks.\n")
            end if
            puts(1, name & " is waiting.\n")
            task_yield()
        end while
        
        puts(1, name & " grabs forks.\n")
        forks[left_fork] = LOCKED
        forks[right_fork] = LOCKED
        for i = 1 to rand(10) do
            puts(1, name & " is eating.\n")
            task_yield()
        end for
        puts(1, name & " puts forks down and leaves the dinning room.\n")
        forks[left_fork] = FREE
        forks[right_fork] = FREE
        
        for i = 1 to rand(10) do
            puts(1, name & " is thinking.\n")
            task_yield()
        end for
        puts(1, name & " becomes hungry.\n")
    end while
end procedure

integer rid
atom taskid
rid = routine_id("person")
taskid = task_create(rid,{"Aristotle",1,2})
task_schedule(taskid,{1,2})
taskid = task_create(rid,{"Kant",2,3})
task_schedule(taskid,{1,2})
taskid = task_create(rid,{"Spinoza",3,4})
task_schedule(taskid,{1,2})
taskid = task_create(rid,{"Marx",4,5})
task_schedule(taskid,{1,2})
taskid = task_create(rid,{"Russell",5,1})
task_schedule(taskid,{1,2})

while get_key() = -1 do
    task_yield()
end while
```

Sample output:

```
Russell grabs forks.
Russell is eating.
Marx hasn't right fork.
Marx is waiting.
Spinoza grabs forks.
Spinoza is eating.
Kant hasn't right fork.
Kant is waiting.
Aristotle hasn't left fork.
Aristotle is waiting.
Russell is eating.
Marx hasn't both forks.
Marx is waiting.
Spinoza is eating.
Kant hasn't right fork.
Kant is waiting.
Aristotle hasn't left fork.
Aristotle is waiting.
Russell is eating.
Marx hasn't both forks.
Marx is waiting.
Spinoza is eating.
Kant hasn't right fork.
Kant is waiting.
Aristotle hasn't left fork.
Aristotle is waiting.
Russell puts forks down and leaves the dinning room.
Russell is thinking.
Marx hasn't left fork.
Marx is waiting.
Spinoza puts forks down and leaves the dinning room.
Spinoza is thinking.
Kant grabs forks.
Kant is eating.
Aristotle hasn't right fork.
Aristotle is waiting.
Russell becomes hungry.
Russell grabs forks.
Russell is eating.
Marx hasn't right fork.
Marx is waiting.
Spinoza is thinking.
Kant is eating.
Aristotle hasn't both forks.
Aristotle is waiting.
```


## F

This solution avoids deadlock by employing a waiter.

```mw
open System

let flip f x y = f y x

let rec cycle s = seq { yield! s; yield! cycle s }

type Agent<'T> = MailboxProcessor<'T>

type Message = Waiting of (Set<int> * AsyncReplyChannel<unit>) | Done of Set<int>

let reply (c: AsyncReplyChannel<_>) = c.Reply()

let strategy forks waiting = 
    let aux, waiting = List.partition (fst >> flip Set.isSubset forks) waiting
    let forks = aux |> List.map fst |> List.fold (-) forks
    List.iter (snd >> reply) aux
    forks, waiting

let waiter strategy forkCount =
  Agent<_>.Start(fun inbox ->
    let rec loop forks waiting =
      async { let forks, waiting = strategy forks waiting
              let! msg = inbox.Receive()
              match msg with
                | Waiting r -> return! loop forks (waiting @ [r])
                | Done f -> return! loop (forks + f) waiting }
    loop (Set.ofList (List.init forkCount id)) [])

let philosopher (waiter: Agent<_>) name forks =
  let rng = new Random()
  let forks = Set.ofArray forks
  Agent<_>.Start(fun inbox ->
    let rec loop () = 
      async { printfn "%s is thinking" name
              do! Async.Sleep(rng.Next(100, 500))
              printfn "%s is hungry" name
              do! waiter.PostAndAsyncReply(fun c -> Waiting (forks, c))
              printfn "%s is eating" name
              do! Async.Sleep(rng.Next(100, 500))
              printfn "%s is done eating" name
              waiter.Post(Done (forks))
              return! loop () }
    loop ())

[<EntryPoint>]
let main args =
  let forks = Seq.init 5 id |> cycle |> Seq.windowed 2 |> Seq.take 5 |> Seq.toList
  let names = ["plato"; "aristotel"; "kant"; "nietzsche"; "russel"]
  let waiter = waiter strategy 5
  List.map2 (philosopher waiter) names forks |> ignore
  Console.ReadLine() |> ignore
  0
```


## Fortran

```mw
!Deadlock prevented by making one philosopher "left-handed"
!and making orderly use of omp locks which protect forks by ensuring that only one philosopher can use each fork at a time
    program dining_philosophers
    use omp_lib
    implicit none

    integer, parameter :: N = 5
    integer(omp_lock_kind) :: forks(N)
    character(len=20), dimension(N) :: names = [character(len=20) :: &
        "Aristotle", "Kant", "Spinoza", "Marx", "Russell"]
    integer :: i
    integer :: next_thread = 0  ! Shared sequencing variable

    ! Initialize forks (mutexes)
    do i = 1, N
        call omp_init_lock(forks(i))
    end do

    ! Parallel region with N threads
    !$omp parallel num_threads(N) private(i) shared(next_thread, forks, names)
        i = omp_get_thread_num() + 1  ! Philosopher IDs: 1 to N
        call philosopher(i, next_thread, forks, names)
    !$omp end parallel

    ! Destroy locks
    do i = 1, N
        call omp_destroy_lock(forks(i))
    end do

contains

    subroutine philosopher(id, next_thread, forks, names)
        integer, intent(in) :: id
        integer, intent(inout) :: next_thread
        integer(omp_lock_kind), intent(inout) :: forks(:)
        character(len=20), intent(in) :: names(:)
        integer :: left, right, meals

        left = id
        right = mod(id, size(forks)) + 1  ! Wrap around for right fork
        !$omp barrier
        ! Wait for turn to start
        do while (id - 1 /= next_thread)
            !$omp flush(next_thread)
        end do

        print *, trim(names(id)), " sits down at the table."

        !$omp atomic
        next_thread = next_thread + 1
        !$omp flush(next_thread)

        ! Philosopher's meal loop
        do meals = 1, 20
!            print *, trim(names(id)), " is thinking."
!            call sleep(1)

            ! Asymmetric fork acquisition to prevent deadlock
            if (id < size(forks)) then
                call omp_set_lock(forks(left))
                print *, trim(names(id)), " picked up left fork ", left
                call omp_set_lock(forks(right))
                print *, trim(names(id)), " picked up right fork ", right
            else
                call omp_set_lock(forks(right))
                print *, trim(names(id)), " picked up right fork ", right
                call omp_set_lock(forks(left))
                print *, trim(names(id)), " picked up left fork ", left
            end if

            print *, trim(names(id)), " is eating."
            call sleep(1)

            call omp_unset_lock(forks(left))
            call omp_unset_lock(forks(right))
            print *, trim(names(id)), " put down forks."
            print *, trim(names(id)), " is thinking."
            call sleep(1)
            print *, trim(names(id)), " returns to the table."

        end do

        print *, trim(names(id)), " leaves the table."
    end subroutine philosopher

end program dining_philosophers
```


## FreeBASIC

Based on Go's solution. Deadlock prevented by making one philosopher "left-handed" and making orderly use of mutexes (mutexes protect forks by ensuring that only one philosopher can use each fork at a time).

```mw
Const NUM_PHILOSOPHERS = 5
Const HUNGER = 3
Const THINK_TIME = 1000
Const EAT_TIME = 1000

Type Fork
    mutex As Any Ptr
    available As Boolean
End Type

Type Philosopher
    nombre As String
    leftFork As Fork Ptr
    rightFork As Fork Ptr
    hunger As Integer
End Type

Dim Shared As Philosopher philosophers(NUM_PHILOSOPHERS-1)
Dim Shared As Fork forks(NUM_PHILOSOPHERS-1)
Dim Shared As Any Ptr printMutex

Function threadSafePrint(text As String) As Integer
    Mutexlock(printMutex)
    Print text
    Mutexunlock(printMutex)
    Return 0
End Function

Sub delay(ms As Integer)
    Dim As Double t = Timer
    While (Timer - t) * 1000 < ms
        Sleep 1, 1
    Wend
End Sub

Function philosopherThread(param As Any Ptr) As Any Ptr
    Dim As Philosopher Ptr phil = param
    
    threadSafePrint(phil->nombre + "  seated")
    
    While phil->hunger > 0
        threadSafePrint(phil->nombre + "  hungry")
        
        Mutexlock(phil->leftFork->mutex)
        Mutexlock(phil->rightFork->mutex)
        
        threadSafePrint(phil->nombre + "  eating")
        delay(EAT_TIME)
        
        Mutexunlock(phil->leftFork->mutex)
        Mutexunlock(phil->rightFork->mutex)
        
        threadSafePrint(phil->nombre + "  thinking")
        delay(THINK_TIME)
        
        phil->hunger -= 1
    Wend
    
    threadSafePrint(phil->nombre + " satisfied")
    threadSafePrint(phil->nombre + " left the table")
    
    Return 0
End Function

' Main program
Dim As Integer i
Dim As String names(NUM_PHILOSOPHERS-1) = {"Aristotle", "Kant", "Spinoza", "Marx", "Russell"}
Print "Table empty"

printMutex = Mutexcreate()

' Initialize forks
For i = 0 To NUM_PHILOSOPHERS-1
    forks(i).mutex = Mutexcreate()
    forks(i).available = True
Next

' Initialize philosophers
For i = 0 To NUM_PHILOSOPHERS-1
    philosophers(i).nombre = names(i)
    philosophers(i).hunger = HUNGER
    philosophers(i).leftFork = @forks(i)
    philosophers(i).rightFork = @forks((i + 1) Mod NUM_PHILOSOPHERS)
Next

' Make last philosopher left-handed
Swap philosophers(NUM_PHILOSOPHERS-1).leftFork, philosophers(NUM_PHILOSOPHERS-1).rightFork

' Create threads
Dim As Any Ptr threads(NUM_PHILOSOPHERS-1)
For i = 0 To NUM_PHILOSOPHERS-1
    threads(i) = Threadcreate(Cast(Sub(As Any Ptr), @philosopherThread), @philosophers(i))
Next

' Wait for all threads
For i = 0 To NUM_PHILOSOPHERS-1
    Threadwait(threads(i))
Next

' Cleanup
For i = 0 To NUM_PHILOSOPHERS-1
    Mutexdestroy(forks(i).mutex)
Next

Mutexdestroy(printMutex)
Print "Table empty"

Sleep
```

**Output:**

```
Table empty
Aristotle seated
Kant seated
Spinoza seated
Marx seated
Aristotle hungry
Russell seated
Kant hungry
Spinoza hungry
Marx hungry
Aristotle eating
Russell hungry
Spinoza eating
Aristotle thinking
Russell eating
Spinoza thinking
Kant eating
Aristotle hungry
Kant thinking
Aristotle eating
Spinoza hungry
Marx eating
Russell thinking
Kant hungry
Marx thinking
Spinoza eating
Russell hungry
Aristotle thinking
Russell eating
Spinoza thinking
Marx hungry
Kant eating
Marx eating
Russell thinking
Aristotle hungry
Spinoza hungry
Aristotle eating
Kant thinking
Russell hungry
Marx thinking
Spinoza eating
Russell eating
Aristotle thinking
Kant hungry
Spinoza thinking
Marx hungry
Kant eating
Russell thinking
Aristotle satisfied
Marx eating
Aristotle Left the table
Kant thinking
Spinoza satisfied
Spinoza Left the table
Russell satisfied
Marx thinking
Russell Left the table
Kant satisfied
Kant Left the table
Marx satisfied
Marx Left the table
Table empty
```
