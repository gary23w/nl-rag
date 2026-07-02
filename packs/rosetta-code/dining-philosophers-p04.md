---
title: "Dining philosophers (part 4/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 4/6
---

## Logtalk

Works when using SWI-Prolog, XSB, or YAP as the backend compiler:

```mw
:- category(chopstick).

    % chopstick actions (picking up and putting down) are synchronized using a notification
    % such that a chopstick can only be handled by a single philosopher at a time:

    :- public(pick_up/0).
    pick_up :-
        threaded_wait(available).

    :- public(put_down/0).
    put_down :-
        threaded_notify(available).

:- end_category.

:- object(cs1,
    imports(chopstick)).

    :- threaded.
    :- initialization(threaded_notify(available)).

:- end_object.

:- object(cs2,
    imports(chopstick)).

    :- threaded.
    :- initialization(threaded_notify(available)).

:- end_object.

:- object(cs3,
    imports(chopstick)).

    :- threaded.
    :- initialization(threaded_notify(available)).

:- end_object.

:- object(cs4,
    imports(chopstick)).

    :- threaded.
    :- initialization(threaded_notify(available)).

:- end_object.

:- object(cs5,
    imports(chopstick)).

    :- threaded.
    :- initialization(threaded_notify(available)).

:- end_object.

:- category(philosopher).

    :- public(left_chopstick/1).
    :- public(right_chopstick/1).
    :- public(run/2).

    :- private(message/1).
    :- synchronized(message/1).

    :- uses(random, [random/3]).

    run(0, _) :-
        this(Philosopher),
        message([Philosopher, ' terminated.']).

    run(Count, MaxTime) :-
        Count > 0,
        think(MaxTime),
        eat(MaxTime),
        Count2 is Count - 1,
        run(Count2, MaxTime).

    think(MaxTime):-
        this(Philosopher),
        random(1, MaxTime, ThinkTime),
        message(['Philosopher ', Philosopher, ' thinking for ', ThinkTime, ' seconds.']),
        thread_sleep(ThinkTime).

    eat(MaxTime):-
        this(Philosopher),
        random(1, MaxTime, EatTime),
        ::left_chopstick(LeftStick),
        ::right_chopstick(RightStick),
        LeftStick::pick_up,
        RightStick::pick_up,
        message(['Philosopher ', Philosopher, ' eating for ', EatTime, ' seconds with chopsticks ', LeftStick, ' and ', RightStick, '.']),
        thread_sleep(EatTime),
        ::LeftStick::put_down,
        ::RightStick::put_down.

    % writing a message needs to be synchronized as it's accomplished  
    % using a combination of individual write/1 and nl/0 calls:
    message([]) :-
        nl,
        flush_output.
    message([Atom| Atoms]) :-
        write(Atom),
        message(Atoms).

:- end_category.

:- object(aristotle,
    imports(philosopher)).

    left_chopstick(cs1).
    right_chopstick(cs2).

:- end_object.

:- object(kant,
    imports(philosopher)).

    left_chopstick(cs2).
    right_chopstick(cs3).

:- end_object.

:- object(spinoza,
    imports(philosopher)).

    left_chopstick(cs3).
    right_chopstick(cs4).

:- end_object.

:- object(marx,
    imports(philosopher)).

    left_chopstick(cs4).
    right_chopstick(cs5).

:- end_object.

:- object(russell,
    imports(philosopher)).

    left_chopstick(cs1).    % change order so that the chopsticks are picked
    right_chopstick(cs5).   % in different order from the other philosophers

:- end_object.
```


## M2000 Interpreter

Version 2.1 Improved program. Choose random Sequential or Concurrent plan. In Concurrent statements in blocks { } are executed sequential (without other part of other thread executed).

At the beginning one of philosopher get a longer trigger period for entry. Also ranδomly the program choose if philosophers can change the order of picking. Each philosopher has an energy, starting from 50. If thinking then energy drop, and can die if energy<1. When philosopher thinking and energy is above 70 then he leave back any fork and drop to 60 Each time he get two forks get a counter on a random value of 4 to 8. So for 4 to 8 "cycles" hold two forks and gain 4 to 8 energy units. With this we have various eating time.

To avoid deadlock we have to put back a fork in thinking phase as the rule bellow: If a philosopher thinking and has energy>70 or the common critical>5 then he place any fork back if energy>70 then energy drop to 60 (so we make a dead zone of 10 units for this automation)

The critical variable get new value from another thread the Main.Task. Some times critical may get a value of 7 and then the thinking philosopher found it and place his fork back (if has any).

```mw
Module Dining_philosophers (whichplan) {
	Form 80, 32
	Const MayChangePick=Random(True, False)
	dim energy(1 to 5)=50
	Document Doc$
	const nl$={
	}
	Print $(,12),  ' set column width to 12
	Pen 14
	Pen 15	{
		Doc$="Dining Philosophers"+nl$
		\\ we can change thread plan only if no threads defined
		if whichplan=1 then
			Doc$="Sequential threads - to execute exclusive one threads code"+nl$
			thread.plan sequential
			\\ need time_to_think>time_to_eat, but time_to_appear maybe the same for all
			time_to_think=150  ' one or more intervals
			time_to_eat=100 ' one interval to eat only	
			time_to_appear=(150,150,150,150,150)
			Return time_to_appear, random(0,3):=300
		else
			Doc$="Concurrent threads  - to execute a statement or a block of code"+nl$
			thread.plan concurrent 
			time_to_think=100  ' one or more intervals
			time_to_eat=50 ' one interval to eat only
			time_to_appear=(100,100,100,100,100)
			Return time_to_appear, random(1,4):=200	 
		end if
		Print #-2,Doc$
		Print @(0,2),"Press left mouse button to exit"
		Print Part $(1), time_to_appear
		Print under
	}
	Pen 13 {Print "Aristotle", "Kant", "Spinoza", "Marx", "Russell"}
	enum philosopher {
		Aristotle, Kant, Spinoza, Marx, Russell
	}
	global enum forks {NoFork, Fork}
	RoundTable =(Fork, Fork, Fork, Fork, Fork)
	Getleft=lambda RoundTable (ph as philosopher) -> {
		where=(ph+4) mod 5
		= RoundTable#val(where)
		Return RoundTable, where:=NoFork
	}
	GetRight=lambda RoundTable (ph as philosopher) -> {
		where=ph mod 5
		=RoundTable#val(where)
		Return RoundTable, where:=NoFork
	}
	PlaceForks=lambda RoundTable (ph as philosopher) -> {
		Return RoundTable,  (ph+4) mod 5:=Fork,ph mod 5:=Fork 
	}
	PlaceAnyFork=lambda RoundTable (ph as philosopher, &ForkL, &ForkR) -> {
		If ForkL=Fork then Return RoundTable,  (ph+4) mod 5:=Fork : ForkL=NoFork
		If ForkR=Fork Then  Return RoundTable, ph mod 5:=Fork : ForkR=NoFork
	}
	ShowTable=lambda RoundTable -> {
		m=each(RoundTable)
		while m
			print if$(array(m)=NoFork->"No Fork", "Fork"),
		end while
		Print
	}
	noforks=lambda RoundTable -> {
		k=0
		m=each(RoundTable)
		while m
			if array(m)=NoFork then k++
		end while
		=k=5
	}
 
	def critical as long, basetick
	Document page$
	m=each(philosopher)
	while m {
		\\ we make 5 threads
		\\ a thread has module scope (except for own static variables, and stack of values)
		thread {
			if  energy(f)<1 then {
					call PlaceAnyFork(f, ForkL, ForkR)
					energy(f)=0
					Page$=format$("{0::-12} - ",tick-basetick)+eval$(f)+" - Die"+nl$
					thread this erase
			} else	{
					Page$=format$("{0::-12} - ",tick-basetick)+eval$(f)
					Page$=if$(ForkL=Nofork or ForkR=Nofork->" thinking",  " eating"+str$(eatcount))
					Page$=if$(R->"- R", " - L")+nl$
			}
			if not think then 
				{ \\ a block always run blocking all other threads
					energy(f)++
					eatcount--
					if eatcount>0 then exit
					Call PlaceForks(f) : ForkL=Nofork:ForkR=NoFork
					eatcount=random(4,8)
					if MayChangePick then R=random(-1,0)
					think=true :thread this interval  time_to_think*random(1,5)
				}
			else.if energy(f)>70 or critical>5 then
				{
					call PlaceAnyFork(f, &ForkL, &ForkR)
					if energy(f)>70  then energy(f)=60
				}
			else.if R then
					if ForkR=Nofork then ForkR=GetRight(f)
					if ForkR=fork and ForkL=Nofork then ForkL=GetLeft(f)
					if ForkL=fork then think=false:thread this interval  time_to_eat else energy(f)--
			else
					if ForkL=Nofork then ForkL=GetLeft(f)
					if ForkL=fork and ForkR=Nofork then ForkR=GetRight(f)
					if ForkR=fork then think=false:thread this interval  time_to_eat else energy(f)--
			end if
			
		} as a interval time_to_appear#val(m^)		
		\\ a is a variable which hold the number of thread (as returned from task manager)
		\\ so we can get 5 times a new number.
		\\ for each thread we make some static variables (only for each thread)
		\\ this statement execute a line of code in thread a
		thread a execute {
			\\ this executed on thread execution object
			static f=eval(m), think=true, ForkL=NoFork
			static ForkR=NoFork, eatcount=random(2,5)
			static R=-1
			if MayChangePick then  R=Random(-1,0)
		}
	}
	cls ,5  ' set split screen from fifth row
	\\ Main.Task is a thread also. Normaly exit if no other threads running in background
	\\ also serve a the wait loop for task manager (we can use Every 200 {} but isn't a thread, is a kind of a wait statement)
	\\ tick return the counter from  task manager which used to triger threads
	basetick=tick
	\\ 4hz display results
	MaxCritical=0
	Main.Task 1000/4 {
		{ \\ a block always run blocking all other threads		
			cls
			Print Part $(1),$("####;\D\I\E;\D\I\E"),energy()
			Print Under
			Print "Table:"
			Call ShowTable()
			if noforks() then critical++  else critical=0
			MaxCritical=if(MaxCritical<critical->critical,MaxCritical)
			Print "noforks on table counter:";critical, "Max:";MaxCritical
			Print #-2,Page$
			Doc$=Page$
			Clear Page$
		}
		if critical>40 or keypress(1) then exit
	}
	threads erase
	Clipboard Doc$
}
Dining_philosophers Random(1,2)
```

**Output:**

```
Dining Philosophers
Concurrent threads  - to execute a statement or a block of code
           3 - Kant thinking - L
           4 - Spinoza thinking- R
           5 - Marx thinking- R
           8 - Aristotle thinking - L
          60 - Russell thinking- R
          77 - Marx thinking- R
         514 - Spinoza eating 4- R
         729 - Kant thinking - L
         734 - Aristotle thinking - L
         736 - Spinoza eating 3- R
         737 - Marx thinking- R
         738 - Russell thinking- R
        1058 - Aristotle thinking - L
        1059 - Kant thinking - L
        1060 - Spinoza eating 2- R
..................................
        6182 - Aristotle thinking- R
        6195 - Kant thinking - L
        6196 - Spinoza eating 8 - L
        6227 - Marx thinking- R
        6228 - Russell eating 3- R
        6238 - Spinoza eating 7 - L
        6260 - Aristotle thinking- R
        6303 - Kant thinking - L
        6306 - Russell eating 2- R
        6340 - Spinoza eating 6 - L
        6342 - Russell eating 1- R
```


## Mathematica / Wolfram Language

```mw
names = <|1 -> "Aristotle", 2 -> "Kant", 3 -> "Spinoza", 4 -> "Marx", 5 -> "Russell"|>;
n = Length[names];
rp := Pause[RandomReal[4]];
PrintTemporary[Dynamic[Array[forks, n]]];
Clear[forks]; forks[_] := Null;
With[{nf = n},
  ParallelDo[
   With[{i1 = i, i2 = Mod[i + 1, nf, 1]},
    Do[Print[names[i], " thinking"]; rp; Print[names[i], " hungry"];
     CriticalSection[{forks[i1], forks[i2]}, 
      Print[names[i], " eating"]; rp],
     {2}]],
   {i, nf}]];
```

**Output:**

```
Aristotle thinking
Kant thinking
Spinoza thinking
Marx thinking
Russell thinking
Russell hungry
Russell eating
```


## Modula-3

From this implementation's point of view, a "resource" is not a *fork*, but rather a *place at the table*. Rather than use one `MUTEX` for *each* fork, it uses one `MUTEX` for the entire table.

- Each philosopher starts on his feet, waits until the `MUTEX` allows him to look for an available seat, and looks to see if two forks are available *at one place*.
- After determining whether a place is available, the philosopher does one of two things **before** releasing the `MUTEX`.
  - If a place is available, he sits down, take both forks at the place (which must be free), and releases the `MUTEX`.
  - If a place is not available, the philosopher does the following.
    - He notifies a "condition variable", comparable to what some restaurants call a "host", that he will wait on a place. *He simultaneously releases the `MUTEX`.*
    - He receives the `MUTEX` again once the condition variable informs him that someone has risen from the table. (This brings us back to the first step.)
- When a philosopher has finished eating, he puts down both forks and rises to think a while.

**Note.** These philosophers actually follow the directions and spend a *random* amount of time eating and thinking.

It is easy to modify this so that each philosopher does not rise from the table, but eats and thinks only at his assigned place. In fact, the original implementation did precisely that, but when I saw that some implementations allowed the philosophers to sit at any place with two available forks, I opted for that.

While this implementation is not a translation of the Eiffel solution, it still owes it a heads-up for the basic principle. Bertrand Meyer's ACM Webinar on SCOOP directed my attention to this problem, and probably influenced the solution.

```mw
MODULE DiningPhilosophers EXPORTS Main;

IMPORT IO, Random, Thread;

CONST

  PartySize = 5; (* modify for more/fewer philosophers *)

TYPE

  Closure = Thread.Closure OBJECT
  (* thread information *)
    which: [1..PartySize]; (* identifies the thread *)
  OVERRIDES
    apply := Live; (* procedure to execute *)
  END;

VAR

  (* how long to eat/think *)
  random: Random.T;

  (* controls access to resources *)
  test := NEW(MUTEX);
  forks := NEW(Thread.Condition); (* condition variable, used for signaling *)
  forkAvailable := ARRAY[1..PartySize] OF BOOLEAN {
    TRUE, TRUE, TRUE, TRUE, TRUE
  };
  (* the philosophers/tasks *)
  thread: ARRAY[1..PartySize] OF Thread.T;
  name := ARRAY[1..PartySize] OF TEXT {
    "Aristotle", "Kant", "Spinoza", "Marx", "Russell"
  };

PROCEDURE PlaceAvailable(): CARDINAL =
(*
  Determines whether a place is available at the table.
  If so, returns the place number. Otherwise, returns 0.
  We consider a place available if and only if *both* forks are free.
*)
BEGIN
  FOR i := 1 TO PartySize DO
    IF forkAvailable[i] AND forkAvailable[((i+1) MOD PartySize) + 1] THEN
      RETURN i;
    END;
  END;
  RETURN 0;
END PlaceAvailable;

PROCEDURE Live(philosopher: Closure): REFANY =
(* philosophers eat, sleep, ... and that's about it *)
VAR
  place: CARDINAL;
BEGIN
  WITH which = philosopher.which DO
    WHILE TRUE DO
      (* first make sure a place is available: both forks must be free! *)
      LOCK test DO
        place := PlaceAvailable();
        (* if not, release mutex and use condition variable to wait for one *)
        WHILE place = 0 DO
          IO.Put(name[which]); IO.Put(" starving!\n");
          Thread.Wait(test, forks);
          (* in Modula-3 we arrive here only if we have the lock again *)
          place := PlaceAvailable();
        END;
        (* a place has come available! seize the forks while mutex is locked *)
        forkAvailable[place] := FALSE;
        forkAvailable[(place MOD PartySize) + 1] := FALSE;
        IO.Put(name[which]); IO.Put(" eating at place "); IO.PutInt(place);
        IO.PutChar('\n');
      END;
      Thread.Pause(FLOAT(random.integer(1,3), LONGREAL));
      (* put down the forks *)
      forkAvailable[place]  := TRUE;
      forkAvailable[(place MOD PartySize) + 1] := TRUE;
      Thread.Signal(forks); (* signal the condition variable *)
      LOCK test DO
        IO.Put(name[which]); IO.Put(" thinking\n");
      END;
      Thread.Pause(FLOAT(random.integer(1,3), LONGREAL));
    END; (* WHILE *)
  END; (* WITH *)
  RETURN NIL;
END Live;

BEGIN
  random := NEW(Random.Default).init();
  (* bring philosophers to life *)
  FOR i := 1 TO PartySize DO
    thread[i] := Thread.Fork(NEW(Closure, apply := Live, which := i));
  END;
  (*
    We need to wait, otherwise the program will terminate,
    and the philosophers with it. Technically we could wait
    for just one philosopher, but in the interest of symmetry...
  *)
  FOR i := 1 TO PartySize DO
    EVAL Thread.Join(thread[i]);
  END;
END DiningPhilosophers.
```

**Output:**

```
Aristotle eating at place 1
Kant eating at place 3
Spinoza starving!
Marx starving!
Russell starving!
Aristotle thinking
Spinoza eating at place 5
Aristotle eating at place 2
Kant thinking
Marx starving!
Kant eating at place 4
Spinoza thinking
Russell starving!
...
```


## Nim

Prevents deadlocks by ordering the forks. Compile with `nim --threads:on c diningphilosophers.nim`

```mw
import threadpool, locks, math, os, random
# to call randomize() as a seed, need to import random module
randomize()

type Philosopher = ref object
  name: string
  food: string
  forkLeft, forkRight: int

const
  n = 5
  names = ["Aristotle", "Kant", "Spinoza", "Marx", "Russell"]
  foods = [" rat poison", " cockroaches", " dog food", " lemon-curd toast", " baked worms"]

var
  forks: array[n, Lock]
  phils: array[n, Philosopher]
  threads: array[n, Thread[Philosopher]]

proc run(p: Philosopher) {.thread.} =
  # random deprecated, use rand(x .. y)
  sleep rand(1..10) * 500
  echo p.name, " is hungry."
 
  acquire forks[min(p.forkLeft, p.forkRight)]
  sleep rand(1..5) * 500
  acquire forks[max(p.forkLeft, p.forkRight)]
 
  echo p.name, " starts eating", p.food, "."
  sleep rand(1..10) * 500
 
  echo p.name, " finishes eating", p.food, " and leaves to think."
 
  release forks[p.forkLeft]
  release forks[p.forkRight]

for i in 0..<n:
  initLock forks[i]
  phils[i] = Philosopher(
    name: names[i],
    food: foods[rand(0 .. n) mod n],
    forkLeft: i,
    forkRight: (i + 1) mod n
  )
  createThread(threads[i], run, phils[i])

joinThreads(threads)
```


## OxygenBasic

```mw
'=========================
class RoundTableWith5Seats
'=========================

  % hungry    0
  % beingUsed 1
  % putDown   0
  % empty     0

  sys fork[5], plate[5],chair[5],philosopher[5]
  sys first

  method AddPasta() as sys
    function rand() as sys
      static seed=0x12345678
      mov eax,seed
      rol eax,7
      mul seed
      xor eax,0x5335ABD9
      mov seed,eax
      return seed
    end function
    return 4+(rand() and 15)
  end method

  method dine()
  first++ 'PRIORITY DINER
  if first>5 then first-=5
  for i=1 to 5
    kl=first+i-1
    kr=first+i
    if kl>5 then kl-=5
    if kr>5 then kr-=5
    if philosopher(kl) = hungry then
      if not fork(kl) or fork(kr) = beingUsed then
        plate(kl) = AddPasta()
        fork(kl)=beingUsed
        fork(kr)=beingUsed
      end if
    end if
    '
  next
  '
  for kl=1 to 5
    kr=kl+1 : if kr>5 then kr-=5
    if plate(kl)
      philosopher(kl)+=1 'PHILOSOPHER DINING
      --plate(kl)
      if plate(kl)=empty
        fork(kl)=PutDown
        fork(kr)=PutDown
      end if
    else
      if philosopher(kl)>0
        --philosopher(kl) 'PHILOSOPHER THINKING
      end if
    end if
  next
  '
  end method

  method show() as string
  cr=chr(13)+chr(10) : tab=chr(9)
  pr="philos" tab "activity" tab "plate" tab "fork L" tab "fork R" cr cr
  for i=1 to 5
  j=i+1 : if j>5 then j-=5
  if plate(i)=0 then
    if philosopher(i)=0 then
      act="waiting"
    else
      act="thinks"
    end if
  else
    act="dining"
  end if
  '
  pr+=i tab act tab plate(i) tab fork(i) tab fork(j) cr
  next
  return pr
  end method

end class

'TEST
'====

RoundTableWith5Seats Sopho
for i=1 to 100
  Sopho.dine
next

print Sopho.show
'putfile "s.txt",Sopho.show

'philos	action	plate	fork L	fork R
'
'1	waiting	0	0	1
'2	dining	8	1	1
'3	thinks	0	1	1
'4	dining	8	1	1
'5	thinks	0	1	0
```


## Oz

Using first-class computation spaces as transactions on dataflow variables. Computations spaces are normally used to implement constraint search engines. But here we use them to bind two variables atomically.

```mw
declare
  Philosophers = [aristotle kant spinoza marx russell]
   
  proc {Start}
     Forks = {MakeList {Length Philosophers}}
  in
     {ForAll Forks NewFork}
     for
        Name in Philosophers
        LeftFork in Forks
        RightFork in {RightShift Forks}
     do
        thread
           {Philosopher Name LeftFork RightFork}
        end
     end
  end

  proc {Philosopher Name LeftFork RightFork}
     for do
        {ShowInfo Name#" is hungry."}
      
        {TakeForks [LeftFork RightFork]}
        {ShowInfo Name#" got forks."}
        {WaitRandom}
        {ReleaseFork LeftFork}
        {ReleaseFork RightFork}

        {ShowInfo Name#" is thinking."}
        {WaitRandom}
     end
  end

  proc {WaitRandom}
     {Delay 1000 + {OS.rand} mod 4000} %% 1-5 seconds
  end

  proc {TakeForks Forks}
     {ForAll Forks WaitForFork}
     case {TryAtomically proc {$}
                            {ForAll Forks TakeFork}
                         end}
     of true then
        {ForAll Forks InitForkNotifier}
     [] false then
        {TakeForks Forks}
     end
  end

  %%
  %% Fork type
  %%

  %% A fork is a mutable reference to a pair
  fun {NewFork}
     {NewCell
      unit(taken:_     %% a fork is taken by setting this value to a unique value
           notify:unit %% to wait for a taken fork
	  )}
  end

  proc {TakeFork F}
     (@F).taken = {NewName}
  end

  proc {InitForkNotifier F}
     %% we cannot do this in TakeFork
     %% because side effect are not allowed in subordinate spaces
     New Old
  in
     {Exchange F Old New}
     New = unit(taken:Old.taken notify:_)
  end

  proc {ReleaseFork F}
     New Old
  in
     {Exchange F Old New}
     New = unit(taken:_ notify:unit)
     Old.notify = unit %% notify waiters
  end

  proc {WaitForFork F}
     {Wait (@F).notify}  %% returns immediatly if fork is free, otherwise blocks
  end

  %%
  %% Helpers
  %%

  %% Implements transactions on data flow variables
  %% with computation spaces. Returns success.
  fun {TryAtomically P}
     try
	S = {Space.new
	     proc {$ Sync}
		{P}
		Sync = unit
	     end}
     in
	{Space.askVerbose S} \= failed = true
	{Wait {Space.merge S}}
	true
     catch _ then
	false
     end
  end

  fun {RightShift Xs} %% circular
     case Xs of nil then nil
     else {Append Xs.2 [Xs.1]}
     end
  end

  ShowInfo = System.showInfo
in
  {Start}
```


## Pascal

This FreePascal implementation uses the idea of ordered resourses, each fork is numbered by index in the array.

In order to avoid deadlocks each member first takes fork with lower number.

```mw
program dining_philosophers;
{$mode objfpc}{$H+}
uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes, SysUtils, SyncObjs;
const
  PHIL_COUNT   = 5;
  LIFESPAN     = 7;
  DELAY_RANGE  = 950;
  DELAY_LOW    = 50;
  PHIL_NAMES: array[1..PHIL_COUNT] of string = ('Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell');
type
  TFork        = TCriticalSection;
  TPhilosopher = class;
var
  Forks: array[1..PHIL_COUNT] of TFork;
  Philosophers: array[1..PHIL_COUNT] of TPhilosopher;
type
  TPhilosopher = class(TThread)
  private
    FName: string;
    FFirstFork, FSecondFork: TFork;
  protected
    procedure Execute; override;
  public
    constructor Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
  end;

procedure TPhilosopher.Execute;
var
  LfSpan: Integer = LIFESPAN;
begin
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
end.
```

The next variant exploits the idea of a single left-handed philosopher.

```mw
program dining_philosophers2;
{$mode objfpc}{$H+}
uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes, SysUtils, SyncObjs;
const
  PHIL_COUNT   = 5;
  LIFESPAN     = 7;
  DELAY_RANGE  = 950;
  DELAY_LOW    = 50;
  PHIL_NAMES: array[1..PHIL_COUNT] of string = ('Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell');
type
  TFork        = TCriticalSection;
  TPhilosopher = class;
var
  Forks: array[1..PHIL_COUNT] of TFork;
  Philosophers: array[1..PHIL_COUNT] of TPhilosopher;
type
  TPhilosopher = class(TThread)
  private
    FName: string;
    FLeftFork, FRightFork: TFork;
    FLefty: Boolean;
    procedure SetLefty(aValue: Boolean);
    procedure SwapForks;
  protected
    procedure Execute; override;
  public
    constructor Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
    property Lefty: Boolean read FLefty write SetLefty;
  end;

procedure TPhilosopher.SetLefty(aValue: Boolean);
begin
  if Lefty = aValue then
    exit;
  FLefty := aValue;
  SwapForks;
end;

procedure TPhilosopher.SwapForks;
var
  Fork: TFork;
begin
  Fork := FLeftFork;
  FLeftFork := FRightFork;
  FRightFork := Fork;
end;

procedure TPhilosopher.Execute;
var
  LfSpan: Integer = LIFESPAN;
begin
  while LfSpan > 0 do
    begin
      Dec(LfSpan);
      WriteLn(FName, ' sits down at the table');
      FLeftFork.Acquire;
      FRightFork.Acquire;
      WriteLn(FName, ' eating');
      Sleep(Random(DELAY_RANGE) + DELAY_LOW);
      FRightFork.Release;
      FLeftFork.Release;
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
  FLeftFork := Forks[aForkIdx1];
  FRightFork := Forks[aForkIdx2];
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
  Philosophers[Succ(Random(5))].Lefty := True;
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
end.
```

Another way to avoid deadlock: if a philosopher takes left fork but cannot take the right fork, he returns the left fork.

```mw
program dining_philosophers3;
{$mode objfpc}{$H+}
uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes, SysUtils, SyncObjs;
const
  PHIL_COUNT   = 5;
  LIFESPAN     = 7;
  DELAY_RANGE  = 950;
  DELAY_LOW    = 50;
  PHIL_NAMES: array[1..PHIL_COUNT] of string = ('Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell');
type
  TFork        = TCriticalSection;
  TPhilosopher = class;
var
  Forks: array[1..PHIL_COUNT] of TFork;
  Philosophers: array[1..PHIL_COUNT] of TPhilosopher;
type
  TPhilosopher = class(TThread)
  private
    FName: string;
    FLeftFork, FRightFork: TFork;
  protected
    procedure Execute; override;
  public
    constructor Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
  end;

procedure TPhilosopher.Execute;
var
  LfSpan: Integer = LIFESPAN;
begin
  while LfSpan > 0 do
    begin
      Dec(LfSpan);
      WriteLn(FName, ' sits down at the table');
      repeat
        FLeftFork.Acquire;
        if not FRightFork.TryEnter then
          begin
            FLeftFork.Release;
            Sleep(Random(DELAY_RANGE));
            continue;
          end;
        break;
      until False;
      WriteLn(FName, ' eating');
      Sleep(Random(DELAY_RANGE) + DELAY_LOW);
      FRightFork.Release;
      FLeftFork.Release;
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
  FLeftFork := Forks[aForkIdx1];
  FRightFork := Forks[aForkIdx2];
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
end.
```

And the last: deadlock can only happen if all the members are seated at the table.

This variant tries to avoid this situation.

```mw
program dining_philosophers4;
{$mode objfpc}{$H+}
uses
  {$IFDEF UNIX}
  cthreads,
  {$ENDIF}
  Classes, SysUtils, SyncObjs;
const
  PHIL_COUNT   = 5;
  LIFESPAN     = 7;
  DELAY_RANGE  = 950;
  DELAY_LOW    = 50;
  PHIL_NAMES: array[1..PHIL_COUNT] of string = ('Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell');
type
  TFork        = TCriticalSection;
  TPhilosopher = class;
var
  Forks: array[1..PHIL_COUNT] of TFork;
  Philosophers: array[1..PHIL_COUNT] of TPhilosopher;
  StilDining: Integer = 0;
procedure WaitForPlaceFree;
begin
  repeat
    if InterlockedIncrement(StilDining) > Pred(PHIL_COUNT) then
      begin
        InterlockedDecrement(StilDining);
        Sleep(Random(DELAY_LOW));
        continue;
      end;
    exit;
  until False;
end;

procedure FreePlace;
begin
  InterLockedDecrement(StilDining);
end;

type
  TPhilosopher = class(TThread)
  private
    FName: string;
    FLeftFork, FRightFork: TFork;
  protected
    procedure Execute; override;
  public
    constructor Create(const aName: string; aForkIdx1, aForkIdx2: Integer);
  end;

procedure TPhilosopher.Execute;
var
  LfSpan: Integer = LIFESPAN;
begin
  while LfSpan > 0 do
    begin
      Dec(LfSpan);
      WaitForPlaceFree;
      WriteLn(FName, ' sits down at the table');
      FLeftFork.Acquire;
      FRightFork.Acquire;
      WriteLn(FName, ' eating');
      Sleep(Random(DELAY_RANGE) + DELAY_LOW);
      FRightFork.Release;
      FLeftFork.Release;
      FreePlace;
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
  FLeftFork := Forks[aForkIdx1];
  FRightFork := Forks[aForkIdx2];
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
end.
```


## Perl

This solution requires that perl have been compiled with threads enabled.

Deadlock is prevented by having even numbered and odd numbered philosophers grab their forks in opposite orders.

```mw
use threads;
use threads::shared;
my @names = qw(Aristotle Kant Spinoza Marx Russell);

my @forks = ('On Table') x @names;
share $forks[$_] for 0 .. $#forks;

sub pick_up_forks {
   my $philosopher = shift;
   my ($first, $second) = ($philosopher, $philosopher-1);
   ($first, $second) = ($second, $first) if $philosopher % 2;
   for my $fork ( @forks[ $first, $second ] ) {
      lock $fork;
      cond_wait($fork) while $fork ne 'On Table';
      $fork = 'In Hand';
   }
}

sub drop_forks {
   my $philosopher = shift;
   for my $fork ( @forks[$philosopher, $philosopher-1] ) {
      lock $fork;
      die unless $fork eq 'In Hand';
      $fork = 'On Table';
      cond_signal($fork);
   }
}

sub philosopher {
   my $philosopher = shift;
   my $name = $names[$philosopher];
   for my $meal ( 1..5 ) {
      print $name, " is pondering\n";
      sleep 1 + rand 8;
      print $name, " is hungry\n";
      pick_up_forks( $philosopher );
      print $name, " is eating\n";
      sleep 1 + rand 8;
      drop_forks( $philosopher );
   }
   print $name, " is done\n";
}

my @t = map { threads->new(\&philosopher, $_) } 0 .. $#names;
for my $thread ( @t ) {
   $thread->join;
}

print "Done\n";
__END__
```

#### One solution based on Coro and AnyEvent

To prevent deadlock the philosophers must not start eating at the same time and the time between getting the first fork and getting second one must be shorter as possible.

```mw
#!/usr/bin/perl
use common::sense;
use Coro;
use AnyEvent;
use Coro::AnyEvent;
use EV;

my @philosophers = qw(Aristotle Kant Spinoza Marx Russell);
my @forks = (1..@philosophers);
my @fork_sem;

$fork_sem[$_] = Coro::Semaphore->new for (0..$#philosophers);

for(my $i = $#philosophers; $i >= 0; $i--){
	say $philosophers[$i] . " has fork #" . $forks[$i] . " and fork #" . $forks[$i-1];
	async {
		my ($name, ,$no, $forks_got) = (@_);

		$Coro::current->{desc} = $name;
		Coro::AnyEvent::sleep(rand 4);

		while(1){
			say $name . " is hungry.";
			$$forks_got[$no]->down();
			Coro::AnyEvent::sleep(rand 1); #Let's make deadlock!
			$$forks_got[$no-1]->down();
			say $name . " is eating.";
			Coro::AnyEvent::sleep(1 + rand 8);

			$$forks_got[$no]->up();
			$$forks_got[$no-1]->up();
			
			say $name . " is thinking.";
			Coro::AnyEvent::sleep(1 + rand 8);
		}
	}($philosophers[$i], $i, \@fork_sem);
}

EV::loop;
```


## Phix

Deadlocks are avoided by always getting the lowest numbered fork first.

You can substitute the indicated line for Russell to prove that it does indeed deadlock when the program fails to follow that rule.

If you uncomment the sleep(1)s you will probably want do the same to the terminate checks, otherwise after keying 'Q' or Escape it could take 20 seconds per diner to finish.

```
without js -- threads
integer fork1 = init_cs(),
        fork2 = init_cs(),
        fork3 = init_cs(),
        fork4 = init_cs(),
        fork5 = init_cs()
integer terminate = 0                   -- control flag
 
procedure person(sequence name, atom left_fork, atom right_fork)
-- (except Russell, who gets left and right the other way round)
    while terminate=0 do
        enter_cs(left_fork)
        enter_cs(right_fork)
        puts(1, name & " grabs forks.\n")
        for i=1 to rand(10) do
--          if terminate then exit end if
            puts(1, name & " is eating.\n")
--          sleep(1)
        end for
        puts(1, name & " puts forks down and leaves the dinning room.\n")
        leave_cs(left_fork)
        leave_cs(right_fork)
        for i=1 to rand(10) do
--          if terminate then exit end if
            puts(1, name & " is thinking.\n")
--          sleep(1)
        end for
        puts(1, name & " becomes hungry.\n")
    end while
end procedure
constant r_person = routine_id("person")
 
constant threads = {create_thread(r_person,{"Aristotle",fork1,fork2}),
                    create_thread(r_person,{"Kant",fork2,fork3}),
                    create_thread(r_person,{"Spinoza",fork3,fork4}),
                    create_thread(r_person,{"Marx",fork4,fork5}),
--                  create_thread(r_person,{"Russell",fork5,fork1})}    -- this will deadlock!
                    create_thread(r_person,{"Russell",fork1,fork5})}
 
constant ESC = #1B
while not find(get_key(),{ESC,'q','Q'}) do
    sleep(1)
end while
terminate = 1
wait_thread(threads)    -- (not strictly necessary)
delete_cs(fork1)        -- ""
delete_cs(fork2)
delete_cs(fork3)
delete_cs(fork4)
delete_cs(fork5)
```


## PicoLisp

This following solution uses the built-in fininte state machine function 'state'. Deadlocks are avoided, as each philosopher releases the first fork if he doesn't succeed to obtain the second fork, and waits for a random time.

Another solution, using the Chandy/Misra method, can be found here.

```mw
(de dining (Name State)
   (loop
      (prinl Name ": " State)
      (state 'State                       # Dispatch according to state
         (thinking 'hungry)               # If thinking, get hungry
         (hungry                          # If hungry, grab random fork
            (if (rand T)
               (and (acquire leftFork) 'leftFork)
               (and (acquire rightFork) 'rightFork) ) )
         (hungry 'hungry                  # Failed, stay hungry for a while
            (wait (rand 1000 3000)) )
         (leftFork                        # If holding left fork, try right one
            (and (acquire rightFork) 'eating)
            (wait 2000) )                 # then eat for 2 seconds
         (rightFork                       # If holding right fork, try left one
            (and (acquire leftFork) 'eating)
            (wait 2000) )                 # then eat for 2 seconds
         ((leftFork rightFork) 'hungry    # Otherwise, go back to hungry,
            (release (val State))         # release left or right fork
            (wait (rand 1000 3000)) )     # and stay hungry
         (eating 'thinking             # After eating, resume thinking
            (release leftFork)
            (release rightFork)
            (wait 6000) ) ) ) )           # for 6 seconds

(setq *Philosophers
   (maplist
      '((Phils Forks)
         (let (leftFork (tmp (car Forks))  rightFork (tmp (cadr Forks)))
            (or
               (fork)  # Parent: Collect child process IDs
               (dining (car Phils) 'hungry) ) ) )  # Initially hungry
      '("Aristotle" "Kant" "Spinoza" "Marx" "Russell")
      '("ForkA" "ForkB" "ForkC" "ForkD" "ForkE" .) ) )

(push '*Bye '(mapc kill *Philosophers))  # Terminate all upon exit
```

Output:

```
Aristotle: hungry
Aristotle: rightFork
Kant: hungry
Kant: rightFork
Spinoza: hungry
Spinoza: rightFork
Marx: hungry
Marx: rightFork
Russell: hungry
Marx: hungry
Spinoza: hungry
Kant: hungry
Russell: hungry
Aristotle: eating
...
```


## Pike

using Pike Backend call_out(), this solution avoids deadlocks by adding a 20% chance that a philosopher drops the fork if he can't pick up both.

```mw
class Philosopher
{ 
    string name;
    object left;
    object right;

    void create(string _name, object _left, object _right)
    {
        name = _name;
        left = _left;
        right = _right;
    }

    void take_forks()
    { 
        if (left->take(this) && right->take(this))
        {
            write("%s is EATING\n", name);
            call_out(drop_forks, random(30)); 
        }
        else
        {
            write("%s is WAITING\n", name);
            if (random(10) >= 8)
                drop_forks();
            call_out(take_forks, random(10)); 
        }
    } 

    void drop_forks()
    { 
        left->drop(this);
        right->drop(this);
        write("%s is THINKING\n", name);
        call_out(take_forks, random(30)); 
    } 
}

class Fork
{
    int number;
    Philosopher user;

    void create(int _number)
    {
        number = _number;
    }

    int take(object new_user)
    {
        if (!user)
        {
            write("%s takes fork %d\n", new_user->name, number);
            user = new_user;
            return 1;
        }
        else if (new_user == user)
        {
            write("%s has fork %d\n", new_user->name, number);
            return 1;
        }
        else
            write("%s tries to take fork %d from %s\n", new_user->name, number, user->name);
    }

    void drop(object old_user)
    {
        if (old_user == user)
        {
            write("%s drops fork %d\n", old_user->name, number);
            user = 0;
        }
    }
}

int main(int argc, array argv)
{
            
  array forks = ({ Fork(1), Fork(2), Fork(3), Fork(4), Fork(5) });
  array philosophers = ({ 
                           Philosopher("einstein", forks[0], forks[1]), 
                           Philosopher("plato", forks[1], forks[2]), 
                           Philosopher("sokrates", forks[2], forks[3]), 
                           Philosopher("chomsky", forks[3], forks[4]), 
                           Philosopher("archimedes", forks[4], forks[0]), 
                        });
                           
  call_out(philosophers[0]->take_forks, random(5));
  call_out(philosophers[1]->take_forks, random(5));
  call_out(philosophers[2]->take_forks, random(5));
  call_out(philosophers[3]->take_forks, random(5));
  call_out(philosophers[4]->take_forks, random(5));
  return -1;
}
```
