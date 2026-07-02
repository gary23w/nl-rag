---
title: "Dining philosophers (part 5/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/6
---

## Prolog

Works with SWI-Prolog and XPCE. Use the same solution as in Erlang (a waiter gives the forks to philosophers). Bonus : the code of an animation in XPCE is given, and statistics are displayed at the end of the process.

```mw
dining_philosophers :-
	new(D, window('Dining philosophers')),
	new(S, window('Dining philosophers : statistics')),
	send(D, size, new(_, size(800,800))),

	new(E, ellipse(400,400)),
	send(E, center, point(400,400)),
	send(D, display, E),

	new(F1, fork(0)),
	new(F2, fork(1)),
	new(F3, fork(2)),
	new(F4, fork(3)),
	new(F5, fork(4)),

	send_list(D, display, [F1,F2,F3,F4,F5]),

	new(Waiter, waiter(F1, F2, F3, F4, F5)),

	create_plate(P1, 0),
	create_plate(P2, 1),
	create_plate(P3, 2),
	create_plate(P4, 3),
	create_plate(P5, 4),

	create_point(0, Pt1),
	create_point(1, Pt2),
	create_point(2, Pt3),
	create_point(3, Pt4),
	create_point(4, Pt5),

	new(Ph1, philosopher('Aristotle', Waiter, P1, D, S, 0, Pt1, left)),
	new(Ph2, philosopher('Kant', Waiter, P2, D, S, 1, Pt2, left)),
	new(Ph3, philosopher('Spinoza', Waiter, P3, D, S, 2, Pt3, right)),
	new(Ph4, philosopher('Marx', Waiter, P4, D, S, 3, Pt4, right)),
	new(Ph5, philosopher('Russell', Waiter, P5, D, S, 4, Pt5, left)),

	send(Waiter, init_phi, Ph1, Ph2, Ph3, Ph4, Ph5),

	send_list([Ph1, Ph2, Ph3, Ph4, Ph5], start),

	send(D, done_message, and(message(Waiter, free),
				 message(Ph1, free),
				 message(Ph2, free),
				 message(Ph3, free),
				 message(Ph4, free),
				 message(Ph5, free),
				 message(S, open),
				 message(D, destroy))),

	send(D, open).

create_plate(P, N) :-
	new(P, ellipse(80,80)),
	X is 400 + 140 * cos(N * pi / 2.5),
	Y is 400 + 140 * sin(N * pi / 2.5),
	send(P, center, point(X, Y)).

create_point(N, point(X, Y)) :-
	X is 400 + 220 * cos(N * pi / 2.5),
	Y is 400 + 220 * sin(N * pi / 2.5) - 20.

:- pce_begin_class(waiter , object, "gives the forks to the philosophers").
variable(f1, fork, both, "free or used").
variable(f2, fork, both, "free or used").
variable(f3, fork, both, "free or used").
variable(f4, fork, both, "free or used").
variable(f5, fork, both, "free or used").
variable(phi1, philosopher, both, "philosopher").
variable(phi2, philosopher, both, "philosopher").
variable(phi3, philosopher, both, "philosopher").
variable(phi4, philosopher, both, "philosopher").
variable(phi5, philosopher, both, "philosopher").

initialise(P, F1, F2, F3, F4, F5) :->
	send(P, slot, f1, F1),
	send(P, slot, f2, F2),
	send(P, slot, f3, F3),
	send(P, slot, f4, F4),
	send(P, slot, f5, F5).

init_phi(P, Phi1,Phi2, Phi3, Phi4, Phi5) :->
	send(P, slot, phi1, Phi1),
	send(P, slot, phi2, Phi2),
	send(P, slot, phi3, Phi3),
	send(P, slot, phi4, Phi4),
	send(P, slot, phi5, Phi5).

want_forks(P, Phi) :->
	( get(P, slot, phi1, Phi) ,!, check_forks(P, Phi, f5, f1);
	 get(P, slot, phi2, Phi),!, check_forks(P, Phi, f1, f2);
	 get(P, slot, phi3, Phi),!, check_forks(P, Phi, f2, f3);
	 get(P, slot, phi4, Phi),!, check_forks(P, Phi, f3, f4);
	 get(P, slot, phi5, Phi),!, check_forks(P, Phi, f4, f5)).

give_back_forks(P, Phi) :->
	( get(P, slot, phi1, Phi) ,!, release_forks(P, phi1);
	 get(P, slot, phi2, Phi),!, release_forks(P, phi2);
	 get(P, slot, phi3, Phi),!, release_forks(P, phi3);
	 get(P, slot, phi4, Phi),!, release_forks(P, phi4);
	 get(P, slot, phi5, Phi),!, release_forks(P, phi5)),

	get(P, slot, phi1, Phi1),
	check_forks(P, Phi1, f5, f1),
	get(P, slot, phi2, Phi2),
	check_forks(P, Phi2, f1, f2),
	get(P, slot, phi3, Phi3),
	check_forks(P, Phi3, f2, f3),
	get(P, slot, phi4, Phi4),
	check_forks(P, Phi4, f3, f4),
	get(P, slot, phi5, Phi5),
	check_forks(P, Phi5, f4, f5).

release_forks(P, phi1) :-
	get(P, slot, f5, F5),
	send(F5, free),
	get(P, slot, f1, F1),
	send(F1, free).

release_forks(P, phi2) :-
	get(P, slot, f1, F1),
	send(F1, free),
	get(P, slot, f2, F2),
	send(F2, free).

release_forks(P, phi3) :-
	get(P, slot, f2, F2),
	send(F2, free),
	get(P, slot, f3, F3),
	send(F3, free).

release_forks(P, phi4) :-
	get(P, slot, f3, F3),
	send(F3, free),
	get(P, slot, f4, F4),
	send(F4, free).

release_forks(P, phi5) :-
	get(P, slot, f4, F4),
	send(F4, free),
	get(P, slot, f5, F5),
	send(F5, free).

check_forks(P, Phi, F1, F2) :-
	get(P, slot, F1, FF1),
	get(P, slot, F2, FF2),
	(   (get(Phi, slot, status, waiting),
	     get(FF1, slot, status, free),
	     get(FF2, slot, status, free))
	->
	     send(Phi, receive_forks),
	     send(FF1, used, right),
	     send(FF2, used, left)
	;
	     true).

:- pce_end_class.

:- pce_begin_class(philosopher , object, "eat, think or wait !").
variable(name, string, both).
variable(window, object, both).
variable(status, object, both, "eating/thinking/waiting").
variable(waiter, object, both).
variable(plate,  object, both).
variable(mytimer, timer, both).
variable(pos, point, both).
variable(side, object, both).
variable(old_text, object, both).
variable(window_stat, object, both).
variable(line_stat, number, both).
variable(stat_wait, my_stat, both).
variable(stat_eat, my_stat, both).
variable(stat_think, my_stat, both).

% méthode appelée lors de la destruction de l'objet
% On arrête d'abord le timer pour poursuivre ensuite
% sans problème (appel par le timer de ressources libérées)
unlink(P) :->
	send(P?mytimer, stop),

	get(P, status, Sta),
	stop_timer(P, Sta),
	get(P, slot, window_stat, WS),
	get(P, slot, line_stat, LS),
	get(LS, value, VLS),
	get(P, slot, name, Name),
	get(Name, value, V),
	sformat(A, 'Statistics of philosopher : ~w', [V]),
	new(Text, text(A)),
	send(Text, font, font(times, bold, 16)),
	Y is VLS * 30,
	send(WS, display, Text, point(30, Y)),

	VLS1 is VLS+1,
	get(P, slot, stat_think, ST),
	send(ST, statistics, WS, VLS1),

	VLS2 is VLS+2,
	get(P, slot, stat_eat, SE),
	send(SE, statistics, WS, VLS2),

	VLS3 is VLS+3,
	get(P, slot, stat_wait, SW),
	send(SW, statistics, WS, VLS3),

	send(P, send_super, unlink).

initialise(P, Name, Waiter, Plate, Window, Window_stat, Line_stat, Point, Side) :->
	% gtrace,
	send(P, slot, name, Name),
	send(P, slot, window, Window),
	send(P, slot, window_stat, Window_stat),
	Line is Line_stat * 5,
	send(P, slot, line_stat, Line),
	send(P, slot, waiter,Waiter),
	send(P, slot, plate,Plate),
	send(P, slot, status, thinking),
	send(P, slot, pos, Point),
	send(P, slot, side, Side),
	send(Window, display, Plate),
	send(P, slot, old_text, new(_, text(' '))),
	send(P, display_status),
	send(P, slot, stat_wait, new(_, my_stat('Waiting'))),
	send(P, slot, stat_eat, new(_, my_stat('Eating'))),
	send(P, slot, stat_think, new(_, my_stat('Thinking'))).

stop_timer(P, eating) :-
	get(P, slot, stat_eat, SE),
	send(SE, stop).

stop_timer(P, waiting) :-
	get(P, slot, stat_wait, SW),
	send(SW, stop).

stop_timer(P, thinking) :-
	get(P, slot, stat_think, ST),
	send(ST, stop).

% internal message send by the timer
my_message(P) :->
	% gtrace,
	get(P, slot, status, Status),
	next_status(P, Status).

% philosopher eating ==> thinking
next_status(P, eating) :-
	get(P, slot, waiter, Waiter),
	get(P, slot, stat_eat, SE),
	send(SE, stop),
	get(P, slot, stat_think, ST),
	send(ST, start),
	send(Waiter, give_back_forks, P),
	send(P, slot, status, thinking),
	send(P, display_status),
	get(P, plate, Plate),
	send(Plate, fill_pattern, colour(white)),
	I is random(20)+ 10,
	get(P, slot, mytimer, Timer),
	send(Timer, interval, I),
	send(Timer, start, once).

next_status(P, thinking) :-
	get(P, slot, waiter, Waiter),
	send(P, slot, status, waiting),
	send(P, display_status),
	get(P, slot, stat_think, ST),
	send(ST, stop),
	get(P, slot, stat_wait, SW),
	send(SW, start),
	send(Waiter, want_forks, P).

% send by the waiter
% philosopher can eat !
receive_forks(P) :->
	get(P, slot, stat_wait, SW),
	send(SW, stop),
	get(P, slot, stat_eat, SE),
	send(SE, start),
	send(P, slot, status, eating),
	send(P, display_status),
	get(P, plate, Plate),
	send(Plate, fill_pattern, colour(black)),
	I is random(20)+ 5,
	get(P, slot, mytimer, Timer),
	send(Timer, interval, I),
	send(Timer, start, once).

display_status(P) :->
	get(P, old_text, OT),
	free(OT),
	get(P, name, Name),
	get(Name, value, V),
	get(P, status, Status),
	choose_color(Status, Colour),
	sformat(A, '~w ~w', [V, Status]),
	get(P, window, W),
	get(P, pos, point(X, Y)),
	new(Text, text(A)),
	send(Text, font, font(times, bold, 16)),
	send(Text, colour, Colour),
	get(Text, string, Str),
	get(font(times, bold, 16), width(Str), M),
	(get(P, side, right) -> X1 is X - M; X1 = X),
	send(W, display, Text, point(X1, Y)),
	send(P, old_text, Text).

start(P) :->
	I is random(10)+ 2,
	get(P, slot, stat_think, ST),
	send(ST, start),
	send(P, mytimer, new(_, timer(I,message(P, my_message)))),
	send(P?mytimer, start, once).

choose_color(eating, colour(blue)).
choose_color(thinking, colour(green)).
choose_color(waiting, colour(red)).

:- pce_end_class.

:- pce_begin_class(disk, ellipse, "disk with color ").

initialise(P, C, R, Col) :->
        send(P, send_super, initialise, R, R),
	send(P, center, C),
	send(P, pen, 0),
	send(P, fill_pattern, Col).

change_color(P, Col) :->
	send(P, fill_pattern, Col).

:- pce_end_class.

:- pce_begin_class(my_stat , object, "statistics").
variable(name, string, both).
variable(nb, number, both).
variable(duration, real, both).
variable(start, real, both).

initialise(P, Name) :->
	send(P, name, Name),
	send(P, nb, 0),
	send(P, duration, 0.0).

start(P) :->
	get_time(T),
	send(P, slot, start, T).

stop(P) :->
	get_time(Fin),

	get(P, slot, nb, N),
	send(N, plus,1),
	send(P, slot, nb, N),

	get(P, slot, duration, D),
	get(P, slot, start, Deb),

	get(D, value, VD),
	get(Deb, value, VDeb),
	X is VD + Fin - VDeb,

	send(P, slot, duration, X).

statistics(P, W, L) :->
	get(P, nb, N),
	get(N, value, VN),
	get(P, duration, D),
	get(D, value, VD),
	get(P, name, Name),
	get(Name, value, V),
	sformat(A, '~w~tnb :~13| ~t~w~17| duration : ~t~1f~35|', [V, VN, VD]),
	new(Text, text(A)),
	send(Text, font, font(screen, roman, 14)),
	Y is L * 30,
	send(W, display, Text, point(40, Y)).

:-pce_end_class.

% forks changes of place
:- pce_begin_class(fork, line, "to help philosopphers to eat").
variable(value, number, both, "0 => 4").
variable(side, object, both), "left / right".
variable(status, object, both, "free / used").

initialise(P, Val) :->
	send_super(P, initialise),
	send(P, slot, value, Val),
	send(P, slot, status, free),
	compute(Val, free, _, PS, PE),
	send(P, start, PS),
	send(P, end, PE).

free(P) :->
	send(P, status, free),
	send(P, position).

used(P, Side) :->
	send(P, status, used),
	send(P, side, Side),
	send(P, position).

position(P) :->
	get(P, value, V),
	get(V, value, N),
	get(P, status, St),
	get(P, side, Side),
	compute(N, St, Side, PS, PE),
	send(P, start, PS),
	send(P, end, PE).

compute(N, free, _Side, point(XS,YS), point(XE,YE)) :-
	A is N * pi / 2.5 + pi / 5,
	XS is 400 + 100 * cos(A),
	YS is 400 + 100 * sin(A),
	XE is 400 + 180 * cos(A),
	YE is 400 + 180 * sin(A).

compute(N, used, left, point(XS,YS), point(XE,YE)) :-
	A is N * pi / 2.5 + pi / 5 - 2 * pi / 15,
	XS is 400 + 100 * cos(A),
	YS is 400 + 100 * sin(A),
	XE is 400 + 180 * cos(A),
	YE is 400 + 180 * sin(A).

compute(N, used, right, point(XS,YS), point(XE,YE)) :-
	A is N * pi / 2.5 + pi / 5 +  2 * pi / 15,
	XS is 400 + 100 * cos(A),
	YS is 400 + 100 * sin(A),
	XE is 400 + 180 * cos(A),
	YE is 400 + 180 * sin(A).

:- pce_end_class.
```


## PureBasic

My Philosophers are very polite, if one can not get both forks they then put down the first and waits a few breaths, then boldly tries in the opposite order.

```mw
Macro Tell(Mutex, Message) ; Make a macro to easy send info back to main thread
  LockMutex(Mutex)
    LastElement(Queue())
    AddElement(Queue())
    Queue() = Message
    SignalSemaphore(Semaphore)
  UnlockMutex(Mutex)
EndMacro

;Set up a data structure to pass needed info into the threads
Structure Thread_Parameters
  Name.s
  fork1.i
  fork2.i
EndStructure

; Declare function to be used
Declare.i TryFork(n)
Declare   PutDownFork(n)
Declare   Invite(Namn.s, Fork1, Fork2)
Declare   _philosophers(*arg.Thread_Parameters)

Global Semaphore = CreateSemaphore()
Global Mutex1     = CreateMutex() ; Eg. fork 1
Global Mutex2     = CreateMutex() ; Eg. fork 2
Global Mutex3     = CreateMutex() ; Eg. fork 3
Global Mutex4     = CreateMutex() ; Eg. fork 4
Global Mutex5     = CreateMutex() ; Eg. fork 5
Global Mutex_main = CreateMutex() ; locking communication with the main thread which do all output.
Global NewList Queue.s()

If OpenConsole()
  Invite("Aristotle",1,2)  ; Get all Philosophers activated
  Invite("Kant",     2,3)
  Invite("Spinoza",  3,4)
  Invite("Marx",     4,5)
  Invite("Russell",  5,1)
  CompilerIf #PB_Compiler_OS=#PB_OS_Windows
    SetConsoleTitle_("Dining philosophers, by Jofur")   ; Using a Windows-API here, so checking before
  CompilerEndIf
  ; Wait and see if any Philosophers want to tell me anything
  Repeat
    WaitSemaphore(Semaphore)
    LockMutex(Mutex_main)
      ForEach Queue()
        PrintN( Queue() )  ; Print what the Philosopher(s) told me
        i-1
      Next Queue()
      ClearList(Queue())
    UnlockMutex(Mutex_main)
  ForEver
EndIf

Procedure TryFork(n)  ; Se is fork #n is free and if so pick it up
  Select n
    Case 1: ProcedureReturn TryLockMutex(Mutex1)
    Case 2: ProcedureReturn TryLockMutex(Mutex2)
    Case 3: ProcedureReturn TryLockMutex(Mutex3)
    Case 4: ProcedureReturn TryLockMutex(Mutex4)
    Default:ProcedureReturn TryLockMutex(Mutex5)
  EndSelect
EndProcedure

Procedure PutDownFork(n) ; put down fork #n and free it to be used by neighbors. 
  Select n
    Case 1: UnlockMutex(Mutex1)
    Case 2: UnlockMutex(Mutex2)
    Case 3: UnlockMutex(Mutex3)
    Case 4: UnlockMutex(Mutex4)
    Default:UnlockMutex(Mutex5)
  EndSelect
EndProcedure

Procedure Invite(Namn.s, Fork1, Fork2)
  Protected *arg.Thread_Parameters ;create the structure containing the parameters
  Protected Thread
  *arg = AllocateMemory(SizeOf(Thread_Parameters))
  *arg\Name = Namn
  *arg\fork1 = Fork1
  *arg\fork2 = Fork2
  Thread=CreateThread(@_philosophers(), *arg) ;send the thread a pointer to our structure
  ProcedureReturn Thread
EndProcedure

Procedure _philosophers(*arg.Thread_Parameters)
  Protected Iam.s=*arg\Name, j=*arg\fork1, k=*arg\fork2
  Protected f1, f2
  ClearStructure(*arg, Thread_Parameters)
  FreeMemory(*arg)
  ;
  Repeat
    Tell(Mutex_main,Iam+": Going to the table")
    Repeat          ;Trying to get my two forks
      f1=TryFork(j)
      If f1
        f2=TryFork(k)
        If Not f2   ; I got only one fork  
          PutDownFork(j)
          f1=0
        EndIf
      EndIf
      If Not f2
        Delay(Random(100))  ; Take a short breath, then try the forks in the other order
        Swap j,k
      EndIf
    Until f1 And f2
    Tell(Mutex_main,Iam+": I have fork #"+Str(j)+" & #"+Str(k)+" and I'm eating now")
    Delay(Random(1500)+15)
    Tell(Mutex_main,Iam+": release fork #"+Str(j)+" & #"+Str(k)+"")
    Delay(Random(45)+15)
    PutDownFork(j)
    PutDownFork(k)
    f1=0:f2=0
    Tell(Mutex_main,Iam+": Thinking about the nature of the universe...")
    Delay(Random(2500)+25)
  ForEver
EndProcedure
```


## Python

### With the threading library

This solution avoids deadlock by never waiting for a fork while having one in hand. If a philosopher acquires one fork but can't acquire the second, he releases the first fork before waiting to acquire the other (which then becomes the first fork acquired).

```mw
import threading
import random
import time

# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
#
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork.  If failed to get second fork, release first fork,
# swap which fork is first and which is second and retry until getting both.
#  
# See discussion page note about 'live lock'.

class Philosopher(threading.Thread):
    
    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            time.sleep( random.uniform(3,13))
            print '%s is hungry.' % self.name
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print '%s swaps forks' % self.name
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):			
        print '%s starts eating '% self.name
        time.sleep(random.uniform(1,10))
        print '%s finishes eating and leaves to think.' % self.name

def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Aristotle','Kant','Spinoza','Marx', 'Russel')

    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print ("Now we're finishing.")

DiningPhilosophers()
```

### With the multiprocessing library

This version uses the multiprocessing library to achieve concurrency on multiple CPUs. (Threads run on a single CPU and are run in "turns". The Python threading library simulate concurrency.)

Some other improvements and modifications: configurable number of philosophers, "more deterministic" randomization by pre-allocating the thinking and dining schedules, time scaling to allow faster runs producing results that are essentially the same, collect statistics on wait times, attempt to check for deadlock, adds more algorithms, including a naive to demonstrate deadlock and two symmetry breaking one versions.

Changed forks to chopsticks. Sorry Edsger, nobody (not even philosophers) need two forks to eat with. Furthermore, using 'fork' may cause confusion, since fork has a meaning in the context of concurrent programming.

```mw
"""Dining philosophers with multiprocessing module."""
import multiprocessing as mp
import random
import time

# Dining philosophers. See also comments at the threading
# version. Improvements, modifications:
# Support variable number of philosophers.
# "More deterministic" randomization by prealocating the schedules.
# Use scaling to allow faster runs producing results that are
# essentially the same.
# Collect statistics on wait times.

SCALE = 0.2
THINK = (3, 13)
DINE = (1, 10)

class Philosopher(mp.Process):
    """Independently running philosopher processes."""
    def __init__(self, idx, name, run_flag, chopstick_left, chopstick_right,
                 stats, schedule_think, schedule_dine):
        mp.Process.__init__(self)
        self.idx = idx
        self.name = name
        self.run_flag = run_flag
        self.chopstick_left = chopstick_left
        self.chopstick_right = chopstick_right
        self.stats = stats
        self.schedule_think = schedule_think
        self.schedule_dine = schedule_dine
        self.counter = 0
        self.num_dined = 0
        self.hungry_time_total = 0.0
        self.hungry_time_max = 0.0

    def run(self):
        while self.run_flag.value and self.counter < len(self.schedule_think):
            #  Philosopher is thinking (but really is sleeping).
            time.sleep(self.schedule_think[self.counter]*SCALE)
            duration = -time.perf_counter()
            print(f'{self.name} is hungry', flush=True)
            self.get_chopsticks2()
            duration += time.perf_counter()
            self.hungry_time_total += duration
            self.hungry_time_max = max(self.hungry_time_max, duration)
            self.dining()
        # Populate self.stats:
        self.stats.put({'name': self.name,
                        'num_dined': self.num_dined,
                        'hungry_time_total': self.hungry_time_total,
                        'hungry_time_max': self.hungry_time_max})

    def get_chopsticks(self):
        """Use swaps and do not hold on to chopsticks."""
        chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right

        while True:
            chopstick1.acquire(True)
            locked = chopstick2.acquire(False)
            if locked:
                return
            chopstick1.release()
            print(f'{self.name} swaps chopsticks', flush=True)
            chopstick1, chopstick2 = chopstick2, chopstick1

    def get_chopsticks0(self):
        """Naive greedy implementation to trigger deadlock."""
        self.chopstick_left.acquire(True)
        time.sleep(0.1)
        self.chopstick_right.acquire(True)

    def get_chopsticks1(self):
        """Break the symmetry by having one philosopher to be left handed."""
        if self.idx == 0:
            chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right
        else:
            chopstick1, chopstick2 = self.chopstick_right, self.chopstick_left
        chopstick1.acquire(True)
        locked = chopstick2.acquire(False)
        if not locked:
            chopstick1.release()
            chopstick2.acquire(True)
            chopstick1.acquire(True)

    def get_chopsticks2(self):
        """Break the symmetry by having the even numbered philosophers to be
           left handed."""
        if self.idx == 0:
            chopstick1, chopstick2 = self.chopstick_left, self.chopstick_right
        else:
            chopstick1, chopstick2 = self.chopstick_right, self.chopstick_left
        chopstick1.acquire(True)
        locked = chopstick2.acquire(False)
        if not locked:
            chopstick1.release()
            chopstick2.acquire(True)
            chopstick1.acquire(True)

    def dining(self):
        """Dining with two chopsticks."""
        print(f'{self.name} starts eating', flush=True)
        self.num_dined += 1
        time.sleep(self.schedule_dine[self.counter]*SCALE)
        self.counter += 1
        print(f'{self.name} finishes eating and leaves to think.', flush=True)
        self.chopstick_left.release()
        self.chopstick_right.release()

def performance_report(stats):
    """Print some stats about the wait times."""
    print("Performance report:")
    for queue in stats:
        data = queue.get()
        print(f"Philosopher {data['name']} dined {data['num_dined']} times. ")
        print(f"  Total wait  : {data['hungry_time_total'] / SCALE}")
        print(f"  Max wait    : {data['hungry_time_max'] / SCALE}")
        if data['num_dined'] > 0:
            print(f"  Average wait: "
                  f"{data['hungry_time_total'] / data['num_dined']/SCALE}")

def generate_philosophers(names, run_flag, chopsticks, stats, max_dine):
    """Gebnerate a list of philosophers with random schedules."""
    num = len(names)
    philosophers = [Philosopher(i, names[i], run_flag,
                                chopsticks[i % num],
                                chopsticks[(i+1) % num],
                                stats[i],
                                [random.uniform(THINK[0], THINK[1])
                                 for j in range(max_dine)],
                                [random.uniform(DINE[0], DINE[1])
                                 for j in range(max_dine)])
                    for i in range(num)]
    return philosophers

def generate_philosophers0(names, run_flag, chopsticks, stats,
                           schedule_think, schedule_dine):
    """Allows the use of a predetermined thinking and dining schedule.
       This may aid in triggering a deadlock."""
    num = len(names)
    philosophers = [Philosopher(i, names[i], run_flag,
                                chopsticks[i % num],
                                chopsticks[(i+1) % num],
                                stats[i],
                                schedule_think[i],
                                schedule_dine[i])
                    for i in range(num)]
    return philosophers

def dining_philosophers(philosopher_names=(('Aristotle', 'Kant',
                                            'Buddha', 'Marx', 'Russel')),
                        num_sec=100, max_dine=100):
    """Main routine."""
    num = len(philosopher_names)
    chopsticks = [mp.Lock() for n in range(num)]
    random.seed(507129)
    run_flag = mp.Value('b', True)
    stats = [mp.Queue() for n in range(num)]

    philosophers = generate_philosophers(philosopher_names, run_flag,
                                         chopsticks, stats, max_dine)

    # Use the following when trying to trigger a deadlock in conjunction with
    # get_chopsticks0():
    #philosophers = generate_philosophers0(philosopher_names, run_flag,
    #                                     chopsticks, stats, [3]*max_dine,
    #                                     [5]*max_dine)

    for phi in philosophers:
        phi.start()
    time.sleep(num_sec*SCALE)
    run_flag.value = False
    print("Now we're finishing.", flush=True)
    # We want to allow the philosophers to finish their meal. In fact,
    # we even allow them to still start eating if they are presently
    # hungry. This means we may need to wait at most num*DINE[1].
    wait_time = num*DINE[1]
    while wait_time >= 0 and sum(p.is_alive() for p in philosophers) > 0:
        time.sleep(1)
        wait_time -= 1.0
    if wait_time < 0:
        for phi in philosophers:
            if phi.is_alive():
                print(f"Ooops, {phi.name} has not finished!!")
                phi.terminate()
        return 1
    performance_report(stats)

if __name__ == '__main__':
    dining_philosophers()
```


## Racket

```mw
#lang racket

;; Racket has traditional semaphores in addition to several higher level
;; synchronization tools.  (Note that these semaphores are used for Racket's
;; green-threads, there are also "future semaphores" which are used for OS
;; threads, with a similar interface.)

;; ----------------------------------------------------------------------------
;; First, a bunch of code to run the experiments below

;; Only two philosophers to make it deadlock very fast
(define philosophers '(Aristotle Kant #|Spinoza Marx Russell|#))

(define (run-philosopher name fork1 fork2)
  (define (show what) (displayln (~a name " " what)))
  (define (loop)
    (show "thinks") (sleep (* 2 (random))) (show "is hungry")
    (grab-forks fork1 fork2 (λ() (show "eats") (sleep (random))))
    (loop))
  (thread loop))

(define (run:simple)
  (define forks (for/list ([i philosophers]) (make-semaphore 1)))
  (for ([i philosophers] [fork1 forks] [fork2 (cons (last forks) forks)])
    (run-philosopher i fork1 fork2))
  (sleep (* 60 60 24 365)))

;; ----------------------------------------------------------------------------
;; This is the naive implementation, which can be used to try getting a
;; deadlock.

(define (grab:naive fork1 fork2 eat!)
  (semaphore-wait fork1)
  (sleep (random)) ; to make deadlocks probable
  (semaphore-wait fork2)
  (eat!)
  (semaphore-post fork1)
  (semaphore-post fork2))

;; ----------------------------------------------------------------------------
;; One way to solve it is to release the first fork if the second is busy and
;; wait for a while.

(define (grab:release+wait fork1 fork2 eat!)
  (semaphore-wait fork1)
  (if (not (semaphore-try-wait? fork2))
    ;; couldn't grab the second fork, so release the first and wait
    (begin (semaphore-post fork1)
           (sleep (random))
           (grab-forks fork1 fork2)) ; can swap them to improve chances
    ;; we have both forks
    (begin (eat!)
           (semaphore-post fork1)
           (semaphore-post fork2))))

;; ----------------------------------------------------------------------------
;; Another solution is to label the forks and lock the lowest-id one first,
;; which makes the naive solution work.

(define (run:labeled-forks)
  (define forks (for/list ([i philosophers]) (make-semaphore 1)))
  ;; the simple run used forks as (1 2 3 4) (4 1 2 3) -- so to implement this,
  ;; we can swap the two first ones: (4 2 3 4) (1 1 2 3)
  (for ([i philosophers]
        [fork1 (cons (last forks) (cdr forks))]
        [fork2 (cons (first forks) forks)])
    (run-philosopher i fork1 fork2))
  (sleep (* 60 60 24 365)))

;; ----------------------------------------------------------------------------
;; Homework: implement the centralized waiter solution

;; ...

;; ----------------------------------------------------------------------------
;; Uncomment one of the following pairs to try it

;; (define grab-forks grab:naive)
;; (define run run:simple)

;; (define grab-forks grab:release+wait)
;; (define run run:simple)

;; (define grab-forks grab:naive)
;; (define run run:labeled-forks)

(run)
```


## Raku

(formerly Perl 6)

Works with

:

rakudo

version 2015-09-09

We use locking mutexes for the forks, and a lollipop to keep the last person who finished eating from getting hungry until the next person finishes eating, which prevents a cycle of dependency from forming. The algorithm should scale to many philosophers, and no philosopher need be singled out to be left-handed, so it's fair in that sense.

```mw
class Fork {
    has $!lock = Lock.new;
    method grab($who, $which) {
	say "$who grabbing $which fork";
	$!lock.lock;
    }
    method drop($who, $which) {
	say "$who dropping $which fork";
	$!lock.unlock;
    }
}
 
class Lollipop {
    has $!channel = Channel.new;
    method mine($who) { $!channel.send($who) }
    method yours { $!channel.receive }
}
 
sub dally($sec) { sleep 0.01 + rand * $sec }
 
sub MAIN(*@names) {
    @names ||= <Aristotle Kant Spinoza Marx Russell>;
 
    my @lfork = Fork.new xx @names;
    my @rfork = @lfork.rotate;
 
    my $lollipop = Lollipop.new;
    start { $lollipop.yours; }
 
    my @philosophers = do for flat @names Z @lfork Z @rfork -> $n, $l, $r {
	start { 
	    sleep 1 + rand*4;
	    loop {
		$l.grab($n,'left');
		dally 1;  # give opportunity for deadlock
		$r.grab($n,'right');
		say "$n eating";
		dally 10;
		$l.drop($n,'left');
		$r.drop($n,'right');
 
		$lollipop.mine($n);
		sleep 1;  # lick at least once
		say "$n lost lollipop to $lollipop.yours(), now digesting";
 
		dally 20;
	    }
	}
    }
    sink await @philosophers;
}
```

**Output:**

```
Aristotle grabbing left fork
Aristotle grabbing right fork
Aristotle eating
Marx grabbing left fork
Marx grabbing right fork
Marx eating
Spinoza grabbing left fork
Aristotle dropping left fork
Aristotle dropping right fork
Russell grabbing left fork
Kant grabbing left fork
Kant grabbing right fork
Spinoza grabbing right fork
Marx dropping left fork
Marx dropping right fork
Aristotle lost lollipop to Marx, now digesting
Spinoza eating
Spinoza dropping left fork
Spinoza dropping right fork
Kant eating
Russell grabbing right fork
Russell eating
Marx lost lollipop to Spinoza, now digesting
Kant dropping left fork
Kant dropping right fork
Spinoza lost lollipop to Kant, now digesting
Russell dropping left fork
Russell dropping right fork
Kant lost lollipop to Russell, now digesting
Spinoza grabbing left fork
Spinoza grabbing right fork
Spinoza eating
Aristotle grabbing left fork
Aristotle grabbing right fork
Aristotle eating
Aristotle dropping left fork
Aristotle dropping right fork
Russell lost lollipop to Aristotle, now digesting
Spinoza dropping left fork
Spinoza dropping right fork
Aristotle lost lollipop to Spinoza, now digesting
Russell grabbing left fork
Marx grabbing left fork
Russell grabbing right fork
Russell eating
Marx grabbing right fork
Kant grabbing left fork
Kant grabbing right fork
Kant eating
Russell dropping left fork
Russell dropping right fork
Spinoza lost lollipop to Russell, now digesting
Marx eating
Spinoza grabbing left fork
Kant dropping left fork
Kant dropping right fork
Russell lost lollipop to Kant, now digesting
Spinoza grabbing right fork
^C
```


## REXX

Programming notes:   This REXX version allows a specification of the names and numbers of dining philosophers   (but no check was made if the number of philosophers is less than two).   The philosopher's names may have imbedded blanks in them, blanks are signified by an underscore   (**_**).   A random number   *seed*   can be specified to allow for repeatability.   The duration of any of the activities the philosophers partake in are herein designated in   *minutes*,   but any consistent timer unit may be used.   Intermediate steps (such as putting the forks down after finishing eating, leaving the dining room to contemplating the nature of the universe, then getting hungry and entering the dining room) are not shown.   If the   *seed*   (first argument) has a leading plus sign   (**+**),   then no status trace is shown.   A random selection of diners (for determining who gets to grab for the forks first) could've been implemented to make a more realistic simulation.

Deadlocks are eliminated by the method of acquiring the resources (forks):   both forks are (attempted to be) grabbed at the same time (by both hands).

```mw
/*REXX program demonstrates a solution in solving the  dining philosophers problem.     */
signal on halt                                   /*branches to  HALT:   (on Ctrl─break).*/
parse arg seed diners                            /*obtain optional arguments from the CL*/
if datatype(seed, 'W')  then call random ,, seed /*this allows for random repeatability.*/
if diners= ''           then diners = 'Aristotle, Kant, Spinoza, Marx, Russell'
  tell= left(seed, 1) \== '+'                    /*Leading + in SEED? Then no statistics*/
diners= space( translate(diners, , ',') )        /*change to an uncommatized diners list*/
     #= words(diners);      @.=   0              /*#: the number of dining philosophers.*/
  eatL= 15;               eatH=  60              /*minimum & maximum minutes for eating.*/
thinkL= 30;             thinkH= 180              /*   "    "    "       "     " thinking*/
forks.=  1                                       /*indicate that all forks are on table.*/
            do tic=1         /*'til halted.*/    /*use  "minutes"  for time advancement.*/
            call grabForks                       /*determine if anybody can grab 2 forks*/
            call passTime                        /*handle philosophers eating|thinking. */
            end   /*tic*/                        /*     ··· and time marches on ···     */
                                                 /* [↓]    this REXX program was halted,*/
halt: say '  ··· REXX program halted!'           /*probably by Ctrl─Break or equivalent.*/
exit                                             /*stick a fork in it,  we're all done. */
/*──────────────────────────────────────────────────────────────────────────────────────*/
fork: parse arg x 1 ox;  x= abs(x) ;  L= x - 1 ;  if L==0  then L= # /*use "round Robin"*/
      if ox<0  then do;  forks.L= 1;  forks.x=1;  return;  end       /*drop the forks.  */
      got2= forks.L  &  forks.x                                      /*get 2 forks │ not*/
      if got2  then do;  forks.L= 0;  forks.x=0;           end       /*obtained 2 forks */
      return got2                                /*return with success  ··· or failure. */
/*──────────────────────────────────────────────────────────────────────────────────────*/
grabForks:   do person=1  for  #                 /*see if any person can grab two forks.*/
             if @.person.state\==0  then iterate /*this diner ain't in a waiting state. */
             if \fork(person)       then iterate /*  "    "   didn't grab two forks.    */
             @.person.state= 'eating'            /*  "    "   is slurping spaghetti.    */
             @.person.dur= random(eatL, eatH)    /*how long will this diner eat pasta ? */
             end   /*person*/                    /* [↑]  process the dining philosophers*/
          return                                 /*all the diners have been examined.   */
/*──────────────────────────────────────────────────────────────────────────────────────*/
passTime: if tell  then say                      /*display a handy blank line separator.*/
            do p=1  for #                        /*handle each of the diner's activity. */
            if tell  then say  right(tic, 9, .)           right( word( diners, p), 20),
                      right(word(@.p.state 'waiting',1+(@.p.state==0)),9) right(@.p.dur,5)
            if @.p.dur==0   then iterate         /*this diner is waiting for two forks. */
            @.p.dur= @.p.dur - 1                 /*indicate single time unit has passed.*/
            if @.p.dur\==0  then iterate         /*Activity done?   No, then keep it up.*/
            if @.p.state=='eating'  then do                      /*now, leave the table.*/
                                         call fork  -p           /*drop the darn forks. */
                                         @.p.state= 'thinking'                 /*status.*/
                                         @.p.dur= random(thinkL, thinkH)       /*length.*/
                                         end     /* [↓]  a diner goes   ──►  the table. */
                                    else if  @.p.state=='thinking'  then @.p.state=0
            end   /*p*/                          /*[↑]  P (person)≡ dining philosophers.*/
          return                                 /*now, have some human beans grab forks*/
```

{{out|output|text=    (some middle and end portions have been elided):

```
........1            Aristotle    eating    42
........1                 Kant   waiting     0
........1              Spinoza    eating    26
........1                 Marx   waiting     0
........1              Russell   waiting     0

........2            Aristotle    eating    41
........2                 Kant   waiting     0
........2              Spinoza    eating    25
........2                 Marx   waiting     0
........2              Russell   waiting     0

         ~~~elided~~~

.....2074            Aristotle  thinking    20
.....2074                 Kant  thinking    56
.....2074              Spinoza  thinking   157
.....2074                 Marx    eating    29
.....2074              Russell  thinking    85

         ~~~elided~~~
```


## Ruby

Translation of

:

Python

Works with

:

Ruby

version 1.8.7

```mw
require 'mutex_m'

class Philosopher
  def initialize(name, left_fork, right_fork)
    @name = name
    @left_fork = left_fork
    @right_fork = right_fork
    @meals = 0
  end

  def go
    while @meals < 5
      think
      dine
    end
    puts "philosopher #@name is full!"
  end

  def think
    puts "philosopher #@name is thinking..."
    sleep(rand())
    puts "philosopher #@name is hungry..."
  end

  def dine
    fork1, fork2 = @left_fork, @right_fork
    while true
      pickup(fork1, :wait => true)
      puts "philosopher #@name has fork #{fork1.fork_id}..."
      if pickup(fork2, :wait => false)
        break
      end
      puts "philosopher #@name cannot pickup second fork #{fork2.fork_id}..."
      release(fork1)
      fork1, fork2 = fork2, fork1
    end
    puts "philosopher #@name has the second fork #{fork2.fork_id}..."

    puts "philosopher #@name eats..."
    sleep(rand())
    puts "philosopher #@name belches"
    @meals += 1

    release(@left_fork)
    release(@right_fork)
  end

  def pickup(fork, opt)
    puts "philosopher #@name attempts to pickup fork #{fork.fork_id}..."
    opt[:wait] ? fork.mutex.mu_lock : fork.mutex.mu_try_lock
  end

  def release(fork)
    puts "philosopher #@name releases fork #{fork.fork_id}..."
    fork.mutex.unlock
  end
end

n = 5

Fork = Struct.new(:fork_id, :mutex)
forks = Array.new(n) {|i| Fork.new(i, Object.new.extend(Mutex_m))}

philosophers = Array.new(n) do |i| 
                 Thread.new(i, forks[i], forks[(i+1)%n]) do |id, f1, f2|
                   ph = Philosopher.new(id, f1, f2).go
                 end
               end
  
philosophers.each {|thread| thread.join}
```


## Rust

A Rust implementation of a solution for the Dining Philosophers Problem. We prevent a deadlock by using Dijkstra's solution of making a single diner "left-handed." That is, all diners except one pick up the chopstick "to their left" and then the chopstick "to their right." The remaining diner performs this in reverse.

```mw
use std::thread;
use std::sync::{Mutex, Arc};

struct Philosopher {
    name: String,
    left: usize,
    right: usize,
}

impl Philosopher {
    fn new(name: &str, left: usize, right: usize) -> Philosopher {
        Philosopher {
            name: name.to_string(),
            left: left,
            right: right,
        }
    }

    fn eat(&self, table: &Table) {
        let _left = table.forks[self.left].lock().unwrap();
        let _right = table.forks[self.right].lock().unwrap();

        println!("{} is eating.", self.name);

        thread::sleep_ms(1000);

        println!("{} is done eating.", self.name);
    }
}

struct Table {
    forks: Vec<Mutex<()>>,
}

fn main() {
    let table = Arc::new(Table { forks: vec![
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
        Mutex::new(()),
    ]});

    let philosophers = vec![
        Philosopher::new("Baruch Spinoza", 0, 1),
        Philosopher::new("Gilles Deleuze", 1, 2),
        Philosopher::new("Karl Marx", 2, 3),
        Philosopher::new("Friedrich Nietzsche", 3, 4),
        Philosopher::new("Michel Foucault", 0, 4),
    ];

    let handles: Vec<_> = philosophers.into_iter().map(|p| {
        let table = table.clone();

        thread::spawn(move || {
            p.eat(&table);
        })
    }).collect();

    for h in handles {
        h.join().unwrap();
    }
}
```
