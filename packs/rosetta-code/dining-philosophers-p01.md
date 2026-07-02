---
title: "Dining philosophers (part 1/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/6
---

# Dining philosophers

The dining philosophers problem illustrates non-composability of low-level synchronization primitives like semaphores. It is a modification of a problem posed by Edsger Dijkstra.

Five philosophers, Aristotle, Kant, Spinoza, Marx, and Russell (the tasks) spend their time thinking and eating spaghetti. They eat at a round table with five individual seats. For eating each philosopher needs two forks (the resources). There are five forks on the table, one left and one right of each seat. When a philosopher cannot grab both forks it sits and waits. Eating takes random time, then the philosopher puts the forks down and leaves the dining room. After spending some random time thinking about the nature of the universe, he again becomes hungry, and the circle repeats itself.

It can be observed that a straightforward solution, when forks are implemented by semaphores, is exposed to deadlock. There exist two deadlock states when all five philosophers are sitting at the table holding one fork each. One deadlock state is when each philosopher has grabbed the fork left of him, and another is when each has the fork on his right.

There are many solutions of the problem, program at least one, and explain how the deadlock is prevented.


## Ada

### Array of mutexes

Library:

Simple components for Ada

The following solution uses an array of mutexes in order to model the forks. The forks used by a philosopher compose a subset in the array. When the the philosopher seizes his forks from the subset the array object prevents deadlocking since it is an atomic operation.

```mw
with Ada.Numerics.Float_Random;  use Ada.Numerics.Float_Random;
with Ada.Text_IO;                use Ada.Text_IO;

with Synchronization.Generic_Mutexes_Array;

procedure Test_Dining_Philosophers is
   type Philosopher is (Aristotle, Kant, Spinoza, Marx, Russel);
   package Fork_Arrays is new Synchronization.Generic_Mutexes_Array (Philosopher);
   use Fork_Arrays;

   Life_Span : constant := 20;    -- In his life a philosopher eats 20 times
   Forks : aliased Mutexes_Array; -- Forks for hungry philosophers
   
   function Left_Of (Fork : Philosopher) return Philosopher is
   begin
      if Fork = Philosopher'First then
         return Philosopher'Last;
      else
         return Philosopher'Pred (Fork);
      end if;
   end Left_Of;

   task type Person (ID : Philosopher);
   task body Person is
      Cutlery : aliased Mutexes_Set := ID or Left_Of (ID);
      Dice    : Generator;
   begin
      Reset (Dice);
      for Life_Cycle in 1..Life_Span loop
         Put_Line (Philosopher'Image (ID) & " is thinking");
         delay Duration (Random (Dice) * 0.100);
         Put_Line (Philosopher'Image (ID) & " is hungry");
         declare
            Lock : Set_Holder (Forks'Access, Cutlery'Access);
         begin
            Put_Line (Philosopher'Image (ID) & " is eating");
            delay Duration (Random (Dice) * 0.100);
         end;
      end loop;
      Put_Line (Philosopher'Image (ID) & " is leaving");
   end Person;

   Ph_1 : Person (Aristotle); -- Start philosophers
   Ph_2 : Person (Kant);
   Ph_3 : Person (Spinoza);
   Ph_4 : Person (Marx);
   Ph_5 : Person (Russel);
begin
   null; -- Nothing to do in the main task, just sit and behold
end Test_Dining_Philosophers;
```

### Ordered mutexes

In the following solution forks are implemented as plain mutexes. The deadlock is prevented by ordering mutexes. Philosopher tasks seize them in same order 1, 2, 3, 4, 5.

```mw
with Ada.Numerics.Float_Random;  use Ada.Numerics.Float_Random;
with Ada.Text_IO;                use Ada.Text_IO;

procedure Test_Dining_Philosophers is
   type Philosopher is (Aristotle, Kant, Spinoza, Marx, Russel);
   protected type Fork is
      entry Grab;
      procedure Put_Down;
   private
      Seized : Boolean := False;
   end Fork;
   protected body Fork is
      entry Grab when not Seized is
      begin
         Seized := True;
      end Grab;
      procedure Put_Down is
      begin
         Seized := False;
      end Put_Down;
   end Fork;
   
   Life_Span : constant := 20;    -- In his life a philosopher eats 20 times
   
   task type Person (ID : Philosopher; First, Second : not null access Fork);
   task body Person is
      Dice : Generator;
   begin
      Reset (Dice);
      for Life_Cycle in 1..Life_Span loop
         Put_Line (Philosopher'Image (ID) & " is thinking");
         delay Duration (Random (Dice) * 0.100);
         Put_Line (Philosopher'Image (ID) & " is hungry");
         First.Grab;
         Second.Grab;
         Put_Line (Philosopher'Image (ID) & " is eating");
         delay Duration (Random (Dice) * 0.100);
         Second.Put_Down;
         First.Put_Down;
      end loop;
      Put_Line (Philosopher'Image (ID) & " is leaving");
   end Person;

   Forks : array (1..5) of aliased Fork; -- Forks for hungry philosophers
                                         -- Start philosophers
   Ph_1 : Person (Aristotle, Forks (1)'Access, Forks (2)'Access);
   Ph_2 : Person (Kant,      Forks (2)'Access, Forks (3)'Access);
   Ph_3 : Person (Spinoza,   Forks (3)'Access, Forks (4)'Access);
   Ph_4 : Person (Marx,      Forks (4)'Access, Forks (5)'Access);
   Ph_5 : Person (Russel,    Forks (1)'Access, Forks (5)'Access);
begin
   null; -- Nothing to do in the main task, just sit and behold
end Test_Dining_Philosophers;
```

### Host of the dining room

Both deadlocks happen when all philosophers are in the dining room. The following solution has a host of the room who chatters the last philosopher while four of them are in the room. So there are never more than four of them in there, which prevents deadlock. Now the forks can be picked up in a "wrong" order, i.e. the left one first.

```mw
with Ada.Numerics.Float_Random;  use Ada.Numerics.Float_Random;
with Ada.Text_IO;                use Ada.Text_IO;

procedure Test_Dining_Philosophers is
   type Philosopher is (Aristotle, Kant, Spinoza, Marx, Russel);
   
   protected type Fork is
      entry Grab;
      procedure Put_Down;
   private
      Seized : Boolean := False;
   end Fork;
   
   protected Host is
      entry Greet;
      procedure Farewell;
   private
      Guests : Natural := 0;
   end Host;

   protected body Fork is
      entry Grab when not Seized is
      begin
         Seized := True;
      end Grab;
      procedure Put_Down is
      begin
         Seized := False;
      end Put_Down;
   end Fork;

   protected body Host is
      entry Greet when Guests < 5 is
      begin
         Guests := Guests + 1;
      end Greet;
      procedure Farewell is
      begin
         Guests := Guests - 1;
      end Farewell;
   end Host;

   Life_Span : constant := 20;    -- In his life a philosopher eats 20 times
   
   task type Person (ID : Philosopher; Left, Right : not null access Fork);
   task body Person is
      Dice : Generator;
   begin
      Reset (Dice);
      for Life_Cycle in 1..Life_Span loop
         Put_Line (Philosopher'Image (ID) & " is thinking");
         delay Duration (Random (Dice) * 0.100);
         Put_Line (Philosopher'Image (ID) & " is hungry");
         Host.Greet;
         Left.Grab;
         Right.Grab;
         Put_Line (Philosopher'Image (ID) & " is eating");
         delay Duration (Random (Dice) * 0.100);
         Left.Put_Down;
         Right.Put_Down;
         Host.Farewell;
      end loop;
      Put_Line (Philosopher'Image (ID) & " is leaving");
   end Person;

   Forks : array (1..5) of aliased Fork; -- Forks for hungry philosophers
                                         -- Start philosophers
   Ph_1 : Person (Aristotle, Forks (1)'Access, Forks (2)'Access);
   Ph_2 : Person (Kant,      Forks (2)'Access, Forks (3)'Access);
   Ph_3 : Person (Spinoza,   Forks (3)'Access, Forks (4)'Access);
   Ph_4 : Person (Marx,      Forks (4)'Access, Forks (5)'Access);
   Ph_5 : Person (Russel,    Forks (5)'Access, Forks (1)'Access);
begin
   null; -- Nothing to do in the main task, just sit and behold
end Test_Dining_Philosophers;
```


## AutoHotkey

AutoHotkey doesn't support concurrency, so we fake it with timers. Deadlock is prevented by releasing a single fork when the other is unobtainable. Livelock is prevented by randomly trying for the opposite fork first. Starvation will only occur if one (or more) of the philosophers never stops eating. Try changing EnoughForks to 4 and fork supply per philosopher to 2.

```mw
#Persistent
SetWorkingDir, %A_ScriptDir%
FileDelete, output.txt
EnoughForks := 2 ; required forks to begin eating
Fork1 := Fork2 := Fork3 := Fork4 := Fork5 := 1 ; fork supply per philosopher
SetTimer, AristotleWaitForLeftFork
SetTimer, KantWaitForLeftFork
SetTimer, SpinozaWaitForLeftFork
SetTimer, MarxWaitForLeftFork
SetTimer, RussellWaitForLeftFork
Return ;---------------------------------------------------------------

AristotleWaitForLeftFork:
	WaitForFork("Aristotle", "left", Fork1, Fork2, AristotleLeftForkCount, AristotleRightForkCount, AristotleWaitCount, EnoughForks)
Return
AristotleWaitForRightFork:
	WaitForFork("Aristotle", "right", Fork2, Fork1, AristotleRightForkCount, AristotleLeftForkCount, AristotleWaitCount, EnoughForks)
Return
AristotleFinishEating:
	ReturnForks("Aristotle", Fork1, Fork2, AristotleLeftForkCount, AristotleRightForkCount, EnoughForks)
Return

KantWaitForLeftFork:
	WaitForFork("Kant", "left", Fork2, Fork3, KantLeftForkCount, KantRightForkCount, KantWaitCount, EnoughForks)
Return
KantWaitForRightFork:
	WaitForFork("Kant", "right", Fork3, Fork2, KantRightForkCount, KantLeftForkCount, KantWaitCount, EnoughForks)
Return
KantFinishEating:
	ReturnForks("Kant", Fork2, Fork3, KantLeftForkCount, KantRightForkCount, EnoughForks)
Return

SpinozaWaitForLeftFork:
	WaitForFork("Spinoza", "left", Fork3, Fork4, SpinozaLeftForkCount, SpinozaRightForkCount, SpinozaWaitCount, EnoughForks)
Return
SpinozaWaitForRightFork:
	WaitForFork("Spinoza", "right", Fork4, Fork3, SpinozaRightForkCount, SpinozaLeftForkCount, SpinozaWaitCount, EnoughForks)
Return
SpinozaFinishEating:
	ReturnForks("Spinoza", Fork3, Fork4, SpinozaLeftForkCount, SpinozaRightForkCount, EnoughForks)
Return

MarxWaitForLeftFork:
	WaitForFork("Marx", "left", Fork4, Fork5, MarxLeftForkCount, MarxRightForkCount, MarxWaitCount, EnoughForks)
Return
MarxWaitForRightFork:
	WaitForFork("Marx", "right", Fork5, Fork4, MarxRightForkCount, MarxLeftForkCount, MarxWaitCount, EnoughForks)
Return
MarxFinishEating:
	ReturnForks("Marx", Fork4, Fork5, MarxLeftForkCount, MarxRightForkCount, EnoughForks)
Return

RussellWaitForLeftFork:
	WaitForFork("Russell", "left", Fork5, Fork1, RussellLeftForkCount, RussellRightForkCount, RussellWaitCount, EnoughForks)
Return
RussellWaitForRightFork:
	WaitForFork("Russell", "right", Fork1, Fork5, RussellRightForkCount, RussellLeftForkCount, RussellWaitCount, EnoughForks)
Return
RussellFinishEating:
	ReturnForks("Russell", Fork5, Fork1, RussellLeftForkCount, RussellRightForkCount, EnoughForks)
Return

ReturnForks(Philosopher, ByRef ThisFork, ByRef OtherFork, ByRef CurrentThisForkCount, ByRef CurrentOtherForkCount, EnoughForks) {
	OutputDebug, %Philosopher% finishes eating.
	FileAppend, %Philosopher% finishes eating.`n,output.txt
	ThisFork += CurrentThisForkCount ; return this fork
	OtherFork += CurrentOtherForkCount ; return other fork
	CurrentThisForkCount := 0 ; release this fork
	CurrentOtherForkCount := 0 ; release other fork
	OutputDebug, %Philosopher% returns all forks.
	FileAppend, %Philosopher% returns all forks.`n,output.txt
	
	; do something while resting
	
	Random, Rand, 0, 1
	Rand := Rand ? "Left" : "Right"
	SetTimer, %Philosopher%WaitFor%Rand%Fork
}

WaitForFork(Philosopher, This, ByRef ThisFork, ByRef OtherFork, ByRef CurrentThisForkCount, ByRef CurrentOtherForkCount, ByRef CurrentWaitCount, EnoughForks) {
	If This not in Left,Right
		Return Error
	Other := (This="right") ? "left" : "right"
	OutputDebug, %Philosopher% is hungry.
	FileAppend, %Philosopher% is hungry.`n,output.txt
	If (ThisFork) ; if this fork available
	{
		SetTimer, %Philosopher%WaitFor%This%Fork, Off
		CurrentWaitCount := 0
		ThisFork-- ; take this fork
		CurrentThisForkCount++ ; receive this fork
		OutputDebug, %Philosopher% grabs %This% fork.
		FileAppend, %Philosopher% grabs %This% fork.`n,output.txt
		If (CurrentThisForkCount + CurrentOtherForkCount = EnoughForks) ; if philosopher has enough forks
		{
			OutputDebug, %Philosopher% starts eating.
			FileAppend, %Philosopher% starts eating.`n,output.txt
			
			; do something while eating
		
			SetTimer, %Philosopher%FinishEating, -250
		}
		Else If (EnoughForks=2)
		{
			SetTimer, %Philosopher%WaitFor%Other%Fork
		}
		Else
		{
			Random, Rand, 0, 1
			Rand := Rand ? "Left" : "Right"
			SetTimer, %Philosopher%WaitFor%Rand%Fork
		}
	}
	Else If (CurrentOtherForkCount and CurrentWaitCount > 5) ; if we've been holding other fork too long
	{
		SetTimer, %Philosopher%WaitFor%This%Fork, Off
		CurrentWaitCount := 0
		OtherFork++ ; return other fork
		CurrentOtherForkCount-- ; release other fork
		OutputDebug, %Philosopher% drops %Other% fork.
		FileAppend, %Philosopher% drops %Other% fork.`n,output.txt
		Random, Rand, 0, 1
		Rand := Rand ? "Left" : "Right"
		SetTimer, %Philosopher%WaitFor%Rand%Fork
	}
	Else If (CurrentThisForkCount and CurrentWaitCount > 5) ; if we've been holding one of this fork too long
	{
		SetTimer, %Philosopher%WaitFor%This%Fork, Off
		CurrentWaitCount := 0
		ThisFork++ ; return other fork
		CurrentThisForkCount-- ; release other fork
		OutputDebug, %Philosopher% drops %This% fork.
		FileAppend, %Philosopher% drops %This% fork.`n,output.txt
		Random, Rand, 0, 1
		Rand := Rand ? "Left" : "Right"
		SetTimer, %Philosopher%WaitFor%Rand%Fork
	}
	Else
	{
		CurrentWaitCount++
	}
}
```

**Output:**

```
Aristotle is hungry.
Aristotle grabs left fork.
Kant is hungry.
Kant grabs left fork.
Spinoza is hungry.
Spinoza grabs left fork.
Marx is hungry.
Marx grabs left fork.
Russell is hungry.
Russell grabs left fork.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Russell is hungry.
Aristotle is hungry.
Aristotle drops left fork.
Kant is hungry.
Kant drops left fork.
Spinoza is hungry.
Spinoza drops left fork.
Marx is hungry.
Marx drops left fork.
Russell is hungry.
Russell grabs right fork.
Russell starts eating.
Marx is hungry.
Marx grabs left fork.
Aristotle is hungry.
Aristotle grabs right fork.
Kant is hungry.
Kant grabs right fork.
Spinoza is hungry.
Russell finishes eating.
Russell returns all forks.
Aristotle is hungry.
Aristotle grabs left fork.
Aristotle starts eating.
Kant is hungry.
Spinoza is hungry.
Marx is hungry.
Marx grabs right fork.
Marx starts eating.
Russell is hungry.
Kant is hungry.
Spinoza is hungry.
Aristotle finishes eating.
Aristotle returns all forks.
Marx finishes eating.
Marx returns all forks.
Russell is hungry.
Russell grabs left fork.
Kant is hungry.
Spinoza is hungry.
Spinoza grabs right fork.
Marx is hungry.
Russell is hungry.
Russell grabs right fork.
Russell starts eating.
Aristotle is hungry.
Aristotle grabs right fork.
Kant is hungry.
Aristotle is hungry.
Spinoza is hungry.
Marx is hungry.
Russell finishes eating.
Russell returns all forks.
Kant is hungry.
Aristotle is hungry.
Aristotle grabs left fork.
Aristotle starts eating.
Spinoza is hungry.
Marx is hungry.
Marx grabs right fork.
Russell is hungry.
⋮
```


## BASIC

### BBC BASIC

Works with

:

BBC BASIC for Windows

This avoids deadlocks using the same strategy as the C solution (one of the philosophers picks up the left fork first).

```mw
      INSTALL @lib$+"TIMERLIB"
      
      nSeats% = 5
      DIM Name$(nSeats%-1), Fork%(nSeats%-1), tID%(nSeats%-1), Leftie%(nSeats%-1)
      
      Name$() = "Aristotle", "Kant", "Spinoza", "Marx", "Russell"
      Fork%() = TRUE : REM All forks are initially on the table
      Leftie%(RND(nSeats%)-1) = TRUE : REM One philosopher is lefthanded
      
      tID%(0) = FN_ontimer(10, PROCphilosopher0, 1)
      tID%(1) = FN_ontimer(10, PROCphilosopher1, 1)
      tID%(2) = FN_ontimer(10, PROCphilosopher2, 1)
      tID%(3) = FN_ontimer(10, PROCphilosopher3, 1)
      tID%(4) = FN_ontimer(10, PROCphilosopher4, 1)
      
      ON CLOSE PROCcleanup : QUIT
      ON ERROR PRINT REPORT$ : PROCcleanup : END
      
      DEF PROCphilosopher0 : PROCtask(0) : ENDPROC
      DEF PROCphilosopher1 : PROCtask(1) : ENDPROC
      DEF PROCphilosopher2 : PROCtask(2) : ENDPROC
      DEF PROCphilosopher3 : PROCtask(3) : ENDPROC
      DEF PROCphilosopher4 : PROCtask(4) : ENDPROC
      
      REPEAT
        WAIT 0
      UNTIL FALSE
      END
      
      DEF PROCtask(n%)
      PRIVATE state%(), lh%(), rh%()
      DIM state%(nSeats%-1), lh%(nSeats%-1), rh%(nSeats%-1)
      REM States: 0 = waiting for forks, > 0 = eating, < 0 = left the room
      CASE TRUE OF
        WHEN state%(n%) < 0:
          state%(n%) += 1 : REM Waiting to get hungry again
          IF state%(n%) = 0 PRINT Name$(n%) " is hungry again"
        WHEN state%(n%) > 0:
          state%(n%) -= 1 : REM Eating
          IF state%(n%) = 0 THEN
            SWAP Fork%((n%-1+nSeats%) MOD nSeats%), lh%(n%)
            SWAP Fork%((n% + 1) MOD nSeats%), rh%(n%)
            state%(n%) = -RND(100)
            PRINT Name$(n%) " is leaving the room"
          ENDIF
        WHEN state%(n%) = 0:
          IF Leftie%(n%) THEN
            IF NOT lh%(n%) SWAP Fork%((n%-1+nSeats%) MOD nSeats%), lh%(n%)
            IF lh%(n%) IF NOT rh%(n%) SWAP Fork%((n% + 1) MOD nSeats%), rh%(n%)
          ELSE
            IF NOT rh%(n%) SWAP Fork%((n% + 1) MOD nSeats%), rh%(n%)
            IF rh%(n%) IF NOT lh%(n%) SWAP Fork%((n%-1+nSeats%) MOD nSeats%), lh%(n%)
          ENDIF
          IF lh%(n%) AND rh%(n%) THEN
            state%(n%) = RND(100)
            PRINT Name$(n%) " is eating (" ; state%(n%) " ticks)"
          ENDIF
      ENDCASE
      ENDPROC
      
      DEF PROCcleanup
      LOCAL I%
      FOR I% = 0 TO nSeats%-1
        PROC_killtimer(tID%(I%))
      NEXT
      ENDPROC
```

**Sample output:**

```
Russell is eating (92 ticks)
Marx is eating (94 ticks)
Russell is leaving the room
Spinoza is eating (96 ticks)
Marx is leaving the room
Kant is eating (40 ticks)
Marx is hungry again
Kant is leaving the room
Kant is hungry again
Russell is hungry again
Spinoza is leaving the room
Aristotle is eating (30 ticks)
Aristotle is leaving the room
Marx is eating (19 ticks)
Spinoza is hungry again
Marx is leaving the room
Kant is eating (20 ticks)
Marx is hungry again
Aristotle is hungry again
Kant is leaving the room
Russell is eating (100 ticks)
Marx is eating (7 ticks)
Marx is leaving the room
Kant is hungry again
Marx is hungry again
Russell is leaving the room
Spinoza is eating (7 ticks)
Kant is eating (82 ticks)
Spinoza is leaving the room
Aristotle is eating (74 ticks)
```


## C

Avoid deadlocks by making each philosopher have a different order of picking up forks. As long as one person waits for left fork first and another waits for right first, cycles can't form.

```mw
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdarg.h>

#define N 5
const char *names[N] = { "Aristotle", "Kant", "Spinoza", "Marx", "Russell" };
pthread_mutex_t forks[N];

#define M 5 /* think bubbles */
const char *topic[M] = { "Spaghetti!", "Life", "Universe", "Everything", "Bathroom" };

#define lock pthread_mutex_lock
#define unlock pthread_mutex_unlock
#define xy(x, y) printf("\033[%d;%dH", x, y)
#define clear_eol(x) print(x, 12, "\033[K")
void print(int y, int x, const char *fmt, ...)
{
	static pthread_mutex_t screen = PTHREAD_MUTEX_INITIALIZER;
	va_list ap;
	va_start(ap, fmt);

	lock(&screen);
	xy(y + 1, x), vprintf(fmt, ap);
	xy(N + 1, 1), fflush(stdout);
	unlock(&screen);
}

void eat(int id)
{
	int f[2], ration, i; /* forks */
	f[0] = f[1] = id;

	/* make some (but not all) philosophers leftie.
	   could have been f[!id] = (id + 1) %N; for example */
	f[id & 1] = (id + 1) % N;

	clear_eol(id);
	print(id, 12, "..oO (forks, need forks)");

	for (i = 0; i < 2; i++) {
		lock(forks + f[i]);
		if (!i) clear_eol(id);

		print(id, 12 + (f[i] != id) * 6, "fork%d", f[i]);
		/* delay 1 sec to clearly show the order of fork acquisition */
		sleep(1);
	}

	for (i = 0, ration = 3 + rand() % 8; i < ration; i++)
		print(id, 24 + i * 4, "nom"), sleep(1);

	/* done nomming, give up forks (order doesn't matter) */
	for (i = 0; i < 2; i++) unlock(forks + f[i]);
}

void think(int id)
{
	int i, t;
	char buf[64] = {0};

	do {
		clear_eol(id);
		sprintf(buf, "..oO (%s)", topic[t = rand() % M]);

		for (i = 0; buf[i]; i++) {
			print(id, i+12, "%c", buf[i]);
			if (i < 5) usleep(200000);
		}
		usleep(500000 + rand() % 1000000);
	} while (t);
}

void* philosophize(void *a)
{
	int id = *(int*)a;
	print(id, 1, "%10s", names[id]);
	while(1) think(id), eat(id);
}

int main()
{
	int i, id[N];
	pthread_t tid[N];

	for (i = 0; i < N; i++)
		pthread_mutex_init(forks + (id[i] = i), 0);

	for (i = 0; i < N; i++)
		pthread_create(tid + i, 0, philosophize, id + i);

	/* wait forever: the threads don't actually stop */
	return pthread_join(tid[0], 0);
}
```

This uses a modified version of the Python algorithm version below. Uses POSIX threads.

```mw
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct philData {
    pthread_mutex_t *fork_lft, *fork_rgt;
    const char *name;
    pthread_t thread;
    int   fail;
} Philosopher;

int running = 1;

void *PhilPhunction(void *p) {
    Philosopher *phil = (Philosopher*)p;
    int failed;
    int tries_left;
    pthread_mutex_t *fork_lft, *fork_rgt, *fork_tmp;

    while (running) {
        printf("%s is sleeping --er thinking\n", phil->name);
        sleep( 1+ rand()%8);

        fork_lft = phil->fork_lft;
        fork_rgt = phil->fork_rgt;
        printf("%s is hungry\n", phil->name);
        tries_left = 2;   /* try twice before being forceful */
        do {
            failed = pthread_mutex_lock( fork_lft);
            failed = (tries_left>0)? pthread_mutex_trylock( fork_rgt )
                                   : pthread_mutex_lock(fork_rgt);
            if (failed) {
                pthread_mutex_unlock( fork_lft);
                fork_tmp = fork_lft;
                fork_lft = fork_rgt;
                fork_rgt = fork_tmp;
                tries_left -= 1;
            }
        } while(failed && running);

        if (!failed) {
            printf("%s is eating\n", phil->name);
            sleep( 1+ rand() % 8);
            pthread_mutex_unlock( fork_rgt);
            pthread_mutex_unlock( fork_lft);
        }
    }
    return NULL;
}

void Ponder()
{
    const char *nameList[] = { "Kant", "Guatma", "Russel", "Aristotle", "Bart" };
    pthread_mutex_t forks[5];
    Philosopher philosophers[5];
    Philosopher *phil;
    int i;
    int failed;

    for (i=0;i<5; i++) {
        failed = pthread_mutex_init(&forks[i], NULL);
        if (failed) {
            printf("Failed to initialize mutexes.");
            exit(1);
        }
    }

    for (i=0;i<5; i++) {
        phil = &philosophers[i];
        phil->name = nameList[i];
        phil->fork_lft = &forks[i];
        phil->fork_rgt = &forks[(i+1)%5];
        phil->fail = pthread_create( &phil->thread, NULL, PhilPhunction, phil);
    }

    sleep(40);
    running = 0;
    printf("cleanup time\n");

    for(i=0; i<5; i++) {
        phil = &philosophers[i];
        if ( !phil->fail && pthread_join( phil->thread, NULL) ) {
            printf("error joining thread for %s", phil->name);
            exit(1);
        }
    }
}

int main()
{
    Ponder();
    return 0;
}
```

This version uses C11 threads and the approach of making one of the philosophers left-handed to avoid deadlock.

```mw
#include <stdio.h>
#include <threads.h>
#include <stdlib.h>

#define NUM_THREADS 5

struct timespec time1;
mtx_t forks[NUM_THREADS];

typedef struct {
	char *name;
	int left;
	int right;
} Philosopher;

Philosopher *create(char *nam, int lef, int righ) {
	Philosopher *x = malloc(sizeof(Philosopher));
	x->name = nam;
	x->left = lef;
	x->right = righ;
	return x; 
}

int eat(void *data) {
	time1.tv_sec = 1;
	Philosopher *foo = (Philosopher *) data;
	mtx_lock(&forks[foo->left]);   
	mtx_lock(&forks[foo->right]);
	printf("%s is eating\n",  foo->name);
	thrd_sleep(&time1, NULL);
	printf("%s is done eating\n",  foo->name);
	mtx_unlock(&forks[foo->left]);
	mtx_unlock(&forks[foo->right]);
	return 0;
}

int main(void) {
    thrd_t threadId[NUM_THREADS];
	Philosopher *all[NUM_THREADS] = {create("Teral", 0 ,1), 
					create("Billy", 1, 2), 
					create("Daniel", 2,3), 
					create("Philip", 3, 4),
					create("Bennet", 0, 4)};
	for (int i = 0; i < NUM_THREADS; i++){
		if (mtx_init(&forks[i], mtx_plain) != thrd_success){
			puts("FAILED IN MUTEX INIT!");
			return 0;
		}
	}
    for (int i=0; i < NUM_THREADS; ++i) {
        if (thrd_create(threadId+i, eat, all[i]) != thrd_success) {
            printf("%d-th thread create error\n", i);
            return 0;
        }
    }

    for (int i=0; i < NUM_THREADS; ++i)
        thrd_join(threadId[i], NULL);
    return 0;
}
```


## C

```mw
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Dining_Philosophers
{
    class Program
    {
        private const int DinerCount = 5;
        private static List<Diner> Diners = new List<Diner>();
        private static List<Fork> Forks = new List<Fork>();
        private static DateTime TimeToStop;

        static void Main(string[] args)
        {
            Initialize();
            WriteHeaderLine();

            do
            {
                WriteStatusLine();
                Thread.Sleep(1000);
            }
            while (DateTime.Now < TimeToStop);

            TearDown();
        }

        private static void Initialize()
        {
            for (int i = 0; i < DinerCount; i++)
                Forks.Add(new Fork());
            for (int i = 0; i < DinerCount; i++)
                Diners.Add(new Diner(i, Forks[i], Forks[(i + 1) % DinerCount]));

            TimeToStop = DateTime.Now.AddSeconds(60);
        }

        private static void TearDown()
        {
            foreach (var diner in Diners)
                diner.Dispose();
        }

        private static void WriteHeaderLine()
        {
            Console.Write("|");

            foreach (Diner d in Diners)
                Console.Write("D " + d.ID + "|");

            Console.Write("    |");

            for (int i = 0; i < DinerCount; i++)
                Console.Write("F" + i + "|");

            Console.WriteLine();
        }

        private static void WriteStatusLine()
        {
            Console.Write("|");

            foreach (Diner d in Diners)
                Console.Write(FormatDinerState(d) + "|");

            Console.Write("    |");

            foreach (Fork f in Forks)
                Console.Write(FormatForkState(f) + "|");

            Console.WriteLine();
        }

        private static string FormatDinerState(Diner diner)
        {
            switch (diner.State)
            {
                case Diner.DinerState.Eating:
                    return "Eat";
                case Diner.DinerState.Pondering:
                    return "Pon";
                case Diner.DinerState.TryingToGetForks:
                    return "Get";
                default:
                    throw new Exception("Unknown diner state.");
            }
        }

        private static string FormatForkState(Fork fork)
        {
            return (!ForkIsBeingUsed(fork) ? "  " : "D" + GetForkHolder(fork));
        }

        private static bool ForkIsBeingUsed(Fork fork)
        {
            return Diners.Count(d => d.CurrentlyHeldForks.Contains(fork)) > 0;
        }

        private static int GetForkHolder(Fork fork)
        {
            return Diners.Single(d => d.CurrentlyHeldForks.Contains(fork)).ID;
        }
    }

    class Diner : IDisposable
    {
        private bool IsCurrentlyHoldingLeftFork = false;
        private bool IsCurrentlyHoldingRightFork = false;
        private const int MaximumWaitTime = 100;
        private static Random Randomizer = new Random();
        private bool ShouldStopEating = false;

        public int ID { get; private set; }
        public Fork LeftFork { get; private set; }
        public Fork RightFork { get; private set; }
        public DinerState State { get; private set; }

        public IEnumerable<Fork> CurrentlyHeldForks
        {
            get
            {
                var forks = new List<Fork>();
                if (IsCurrentlyHoldingLeftFork)
                    forks.Add(LeftFork);
                if (IsCurrentlyHoldingRightFork)
                    forks.Add(RightFork);
                return forks;
            }
        }

        public Diner(int id, Fork leftFork, Fork rightFork)
        {
            InitializeDinerState(id, leftFork, rightFork);
            BeginDinerActivity();
        }

        private void KeepTryingToEat()
        {
            do
                if (State == DinerState.TryingToGetForks)
                {
                    TryToGetLeftFork();
                    if (IsCurrentlyHoldingLeftFork)
                    {
                        TryToGetRightFork();
                        if (IsCurrentlyHoldingRightFork)
                        {
                            Eat();
                            DropForks();
                            Ponder();
                        }
                        else
                        {
                            DropForks();
                            WaitForAMoment();
                        }
                    }
                    else
                        WaitForAMoment();
                }
                else
                    State = DinerState.TryingToGetForks;
            while (!ShouldStopEating);
        }

        private void InitializeDinerState(int id, Fork leftFork, Fork rightFork)
        {
            ID = id;
            LeftFork = leftFork;
            RightFork = rightFork;
            State = DinerState.TryingToGetForks;
        }

        private async void BeginDinerActivity()
        {
            await Task.Run(() => KeepTryingToEat());
        }

        private void TryToGetLeftFork()
        {
            Monitor.TryEnter(LeftFork, ref IsCurrentlyHoldingLeftFork);
        }

        private void TryToGetRightFork()
        {
            Monitor.TryEnter(RightFork, ref IsCurrentlyHoldingRightFork);
        }

        private void DropForks()
        {
            DropLeftFork();
            DropRightFork();
        }

        private void DropLeftFork()
        {
            if (IsCurrentlyHoldingLeftFork)
            {
                IsCurrentlyHoldingLeftFork = false;
                Monitor.Exit(LeftFork);
            }
        }

        private void DropRightFork()
        {
            if (IsCurrentlyHoldingRightFork)
            {
                IsCurrentlyHoldingRightFork = false;
                Monitor.Exit(RightFork);
            }
        }

        private void Eat()
        {
            State = DinerState.Eating;
            WaitForAMoment();
        }

        private void Ponder()
        {
            State = DinerState.Pondering;
            WaitForAMoment();
        }

        private static void WaitForAMoment()
        {
            Thread.Sleep(Randomizer.Next(MaximumWaitTime));
        }

        public void Dispose()
        {
            ShouldStopEating = true;
        }

        public enum DinerState
        {
            Eating,
            TryingToGetForks,
            Pondering
        }
    }

    class Fork { }
}
```


## C++

Uses C++17

```mw
#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <mutex>
#include <random>
#include <string>
#include <string_view>
#include <thread>

const int timeScale = 42;  // scale factor for the philosophers task duration

void Message(std::string_view message)
{
    // thread safe printing
    static std::mutex cout_mutex;
    std::scoped_lock cout_lock(cout_mutex);
    std::cout << message << std::endl;
}

struct Fork {
    std::mutex mutex;
};

struct Dinner {
    std::array<Fork, 5> forks;
    ~Dinner() { Message("Dinner is over"); }
};

class Philosopher
{
    // generates random numbers using the Mersenne Twister algorithm
    // for task times and messages
    std::mt19937 rng{std::random_device {}()};

    const std::string name;
    Fork& left;
    Fork& right;
    std::thread worker;

    void live();
    void dine();
    void ponder();
public:
    Philosopher(std::string name_, Fork& l, Fork& r)
    : name(std::move(name_)), left(l), right(r), worker(&Philosopher::live, this)
    {}
    ~Philosopher()
    {
        worker.join();
        Message(name + " went to sleep.");
    }
};

void Philosopher::live()
{
    for(;;) // run forever
    {
        {
            //Aquire forks.  scoped_lock acquires the mutexes for 
            //both forks using a deadlock avoidance algorithm
            std::scoped_lock dine_lock(left.mutex, right.mutex);

            dine();

            //The mutexes are released here at the end of the scope
        }
        
        ponder();
    }
}

void Philosopher::dine()
{
    Message(name + " started eating.");

    // Print some random messages while the philosopher is eating
    thread_local std::array<const char*, 3> foods {"chicken", "rice", "soda"};
    thread_local std::array<const char*, 3> reactions {
        "I like this %s!", "This %s is good.", "Mmm, %s..."
    };
    thread_local std::uniform_int_distribution<> dist(1, 6);
    std::shuffle(    foods.begin(),     foods.end(), rng);
    std::shuffle(reactions.begin(), reactions.end(), rng);
    
    constexpr size_t buf_size = 64;
    char buffer[buf_size];
    for(int i = 0; i < 3; ++i) {
        std::this_thread::sleep_for(std::chrono::milliseconds(dist(rng) * timeScale));
        snprintf(buffer, buf_size, reactions[i], foods[i]);
        Message(name + ": " + buffer);
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(dist(rng)) * timeScale);

    Message(name + " finished and left.");
}

void Philosopher::ponder()
{
    static constexpr std::array<const char*, 5> topics {{
        "politics", "art", "meaning of life", "source of morality", "how many straws makes a bale"
    }};
    thread_local std::uniform_int_distribution<> wait(1, 6);
    thread_local std::uniform_int_distribution<> dist(0, topics.size() - 1);
    while(dist(rng) > 0) {
        std::this_thread::sleep_for(std::chrono::milliseconds(wait(rng) * 3 * timeScale));
        Message(name + " is pondering about " + topics[dist(rng)] + ".");
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(wait(rng) * 3 * timeScale));
    Message(name + " is hungry again!");
}

int main()
{
    Dinner dinner;
    Message("Dinner started!");
    // The philosophers will start as soon as they are created
    std::array<Philosopher, 5> philosophers {{
            {"Aristotle",   dinner.forks[0], dinner.forks[1]},
            {"Democritus",  dinner.forks[1], dinner.forks[2]},
            {"Plato",       dinner.forks[2], dinner.forks[3]},
            {"Pythagoras",  dinner.forks[3], dinner.forks[4]},
            {"Socrates",    dinner.forks[4], dinner.forks[0]},
    }};
    Message("It is dark outside...");
}
```

Dinner started! Aristotle started eating. It is dark outside... Plato started eating. Aristotle: Mmm, soda... Aristotle: This chicken is good. Plato: I like this soda! Aristotle: I like this rice! Aristotle finished and left. Plato: Mmm, chicken... Socrates started eating. Socrates: I like this soda! Plato: This rice is good. Plato finished and left. Democritus started eating. Socrates: Mmm, rice... Democritus: Mmm, soda... Aristotle is pondering about politics. Aristotle is pondering about meaning of life. Democritus: I like this chicken! Socrates: This chicken is good. Democritus: This rice is good. Democritus finished and left. Plato is pondering about source of morality. Socrates finished and left. Pythagoras started eating. Plato is pondering about how many straws makes a bale. Socrates is pondering about politics. Pythagoras: I like this chicken! Aristotle is hungry again! Aristotle started eating. Aristotle: This chicken is good. Socrates is pondering about art. Pythagoras: This soda is good. Pythagoras: Mmm, rice... Aristotle: I like this soda! Pythagoras finished and left. Socrates is hungry again! Aristotle: Mmm, rice... Democritus is pondering about source of morality. Plato is pondering about how many straws makes a bale. Aristotle finished and left. Socrates started eating. Democritus is hungry again! Democritus started eating. Plato is pondering about art. Socrates: Mmm, chicken... Democritus: This soda is good. Socrates: I like this rice! Democritus: I like this rice! Pythagoras is pondering about source of morality. Aristotle is pondering about source of morality. Socrates: This soda is good. Democritus: Mmm, chicken... Socrates finished and left. Democritus finished and left. Plato is pondering about politics. Aristotle is pondering about art. Pythagoras is pondering about source of morality. Socrates is pondering about source of morality. Plato is hungry again! Plato started eating. Plato: Mmm, rice... Plato: I like this soda! Plato: This chicken is good. Aristotle is hungry again! Aristotle started eating. Plato finished and left. Democritus is pondering about politics. Aristotle: Mmm, chicken... Aristotle: I like this rice! Pythagoras is pondering about art. Aristotle: This soda is good. Socrates is pondering about politics. Aristotle finished and left. Pythagoras is pondering about source of morality. Socrates is pondering about politics. Democritus is pondering about politics. Pythagoras is pondering about art. Plato is pondering about art. Aristotle is pondering about art. Socrates is pondering about source of morality. Democritus is pondering about meaning of life. Pythagoras is pondering about how many straws makes a bale. . . . .

Uses C++14 Without threads, uses state machine.

```mw
#include <iostream>
#include <vector>
#include <random>
#include <memory>
#include <cassert>

using namespace std;

struct Fork {
    static const int ON_TABLE = -1;
    int holder = ON_TABLE;
    int request = ON_TABLE;
    int id;
    bool dirty = true;
    Fork(int id) {
        this->id = id;
    }
    bool isRequest() {
        return request != Fork::ON_TABLE;
    }

    void process(int &forkCount, int &dirtyCount) {
        if (holder == id) {
            forkCount++;
            if (isRequest()) {
                if (dirty) {
                    forkCount--;
                    dirty = false;
                    holder = request;
                }
                request = Fork::ON_TABLE;
            }
        }
        else
        if (holder == Fork::ON_TABLE) {
            holder = id;
            forkCount++;
            assert(dirty);
            dirtyCount++;
            assert(request == Fork::ON_TABLE);
        } else {
            request = id;
        }
    }
};

class Table;

enum State { Have0Forks, Have1Fork,Have01Fork, Have2Forks, Eat, AfterEat, Pon };

class Philosopher {
    int id;
    Table *table;
public:
    Fork* left;
    Fork* right;
    int eatStarts = 0;
    Philosopher(Table *table, int id);
    void naive();
    void ChandyMisra();
    State state;

    void selectState(int forkCount, int dirtyCount);
};

class Table {
    mt19937 mt_rand;
    std::uniform_real_distribution<> dis;
    unique_ptr<std::uniform_int_distribution<>> disint;
public:
    static const int PhilCount = 5;
    vector<unique_ptr<Philosopher>> philosophers;
    vector<unique_ptr<Fork>> forks;
    Table() {
        mt_rand.seed(1234);
        disint = make_unique<std::uniform_int_distribution<>>(0, PhilCount-1);
        for (int i=0; i<PhilCount; i++)
            forks.push_back(make_unique<Fork>(i));
        for (int i=0; i<PhilCount; i++)
            philosophers.push_back(make_unique<Philosopher>(this, i));
    }
    double rand() {
        return dis(mt_rand);
    }

    double randInt() {
        return (*disint)(mt_rand);
    }
    void naive() {
        cout << "Naive algorithm" << endl;
        for (int i=0; i<Table::PhilCount; i++)
            philosophers[i]->state = State::Have0Forks;
        for (int i=0; i<100000; i++) {
            philosophers[randInt()]->naive();
        }
        for (int i=0; i<Table::PhilCount; i++)
            cout << i << " : " << philosophers[i]->eatStarts << endl;
    }
    void ChandyMisra() {
        cout << "Chandy-Misra algorithm" << endl;
        for (int i=0; i<Table::PhilCount; i++) {
            philosophers[i]->state = State::Have01Fork;
            philosophers[i]->eatStarts = 0;
            philosophers[i]->left->holder = i;
        }
        for (int i=0; i<100000; i++) {
            philosophers[randInt()]->ChandyMisra();
        }
        for (int i=0; i<Table::PhilCount; i++)
            cout << i << " : " << philosophers[i]->eatStarts << endl;
    }
};

Philosopher::Philosopher(Table *table, int id):table(table), id(id) {
    left = table->forks[id].get();
    right = table->forks[(id+1) % Table::PhilCount].get();
}

void Philosopher::naive() {
    switch (state) {
        case State::Pon:
            if (table->rand()<0.2)
                state = State::Have0Forks;
            return;
        case State::Have0Forks:
            int forkCount;
            forkCount = 0;
            if (left->holder==Fork::ON_TABLE) {
                left->holder=id;
                forkCount++;
            }
            if (right->holder==Fork::ON_TABLE) {
                right->holder=id;
                forkCount++;
            }
            if (forkCount==1)
                state = State::Have1Fork;
            else if (forkCount==2)
                state = State::Have2Forks;
            return;
        case State::Have1Fork:
            Fork* forkToWait;
            if (left->holder==id)
                forkToWait = right;
            else 
                forkToWait = left;
            if (forkToWait->holder==Fork::ON_TABLE) {
                forkToWait->holder=id;
                state = State::Have2Forks;
            }
            return;
        case State::Have2Forks:
            state = State::Eat;
            eatStarts++;
            return;
        case State::Eat:
            if (table->rand()<0.2)
                state = State::AfterEat;
            return;
        case State::AfterEat:
            left->holder = Fork::ON_TABLE;
            right->holder = Fork::ON_TABLE;
            state = State::Pon;
            return;
    }
}

void Philosopher::ChandyMisra() {
    switch (state) {
        case State::Pon:
            if (table->rand() < 0.2)
                state = State::Have01Fork;
            return;
        case State::Have01Fork:
            int forkCount;
            int dirtyCount;
            forkCount = 0;
            dirtyCount = 0;
            left->process(forkCount, dirtyCount);
            right->process(forkCount, dirtyCount);
            selectState(forkCount, dirtyCount);
            return;
        case State::Have2Forks:
            state = State::Eat;
            eatStarts++;
            return;
        case State::Eat:
            if (table->rand()<0.2)
                state = State::AfterEat;
            return;
        case State::AfterEat:
            if (left->request!=Fork::ON_TABLE) {
                left->dirty = false;
                left->holder = left->request;
                left->request = Fork::ON_TABLE;
            } else {
                left->holder = Fork::ON_TABLE;
                left->dirty = true;
            }

            if (right->request!=Fork::ON_TABLE) {
                right->dirty = false;
                right->holder = right->request;
                right->request = Fork::ON_TABLE;
            } else {
                right->holder = Fork::ON_TABLE;
                right->dirty = true;
            }
            state = State::Pon;
            return;
    }
}

void Philosopher::selectState(int forkCount, int dirtyCount) {
    if (forkCount == 2 && dirtyCount==0)
        state = State::Have2Forks;
    else
        state = State::Have01Fork;
}

int main() {
    Table table;
    table.naive();
    table.ChandyMisra();
    return 0;
}
```


## Clojure

Clojure's STM allows us to avoid low-level synchronization primitives like semaphores. In order to simulate the Dining Philosophers scenario, the forks are references to a boolean indicating whether or not it is available for use. Each philosopher (also held in a ref) has a fixed amount of food he will try to eat, first by trying to acquire both forks, eating for some period of time, releasing both forks, then thinking for some period of time; if the forks cannot be acquired, the philosopher waits for a fixed amount of time and tries again.

```mw
(defn make-fork [] 
  (ref true))

(defn make-philosopher [name forks food-amt]
  (ref {:name name :forks forks :eating? false :food food-amt}))

(defn start-eating [phil]
  (dosync
    (if (every? true? (map ensure (:forks @phil)))  ; <-- the essential solution
      (do
        (doseq [f (:forks @phil)] (alter f not))
        (alter phil assoc :eating? true)
        (alter phil update-in [:food] dec)
        true)
      false)))

(defn stop-eating [phil]
  (dosync
    (when (:eating? @phil)
      (alter phil assoc :eating? false)
      (doseq [f (:forks @phil)] (alter f not)))))

(defn dine [phil retry-interval max-eat-duration max-think-duration]
  (while (pos? (:food @phil))
    (if (start-eating phil)
      (do
        (Thread/sleep (rand-int max-eat-duration))
        (stop-eating phil)
        (Thread/sleep (rand-int max-think-duration)))
      (Thread/sleep retry-interval))))
```

The second line of the start-eating function contains the essential solution: by invoking ensure on every fork reference, we are guaranteed that the state of the forks will not be modified by other transactions, thus we can rely on those values for the rest of the transaction. Now we just need to run it:

```mw
(def *forks* (cycle (take 5 (repeatedly #(make-fork)))))

(def *philosophers* 
  (doall (map #(make-philosopher %1 [(nth *forks* %2) (nth *forks* (inc %2))] 1000)
              ["Aristotle" "Kant" "Spinoza" "Marx" "Russell"] 
              (range 5))))

(defn start []
  (doseq [phil *philosophers*] 
    (.start (Thread. #(dine phil 5 100 100)))))

(defn status []
  (dosync
    (doseq [i (range 5)]
      (let [f @(nth *forks* i)
            p @(nth *philosophers* i)]
        (println (str "fork: available=" f))
        (println (str (:name p) 
                      ": eating=" (:eating? p) 
                      " food=" (:food p)))))))
```

The status function inspects the data structures within a transaction so as to give consistent results (e.g., every unavailable fork has exactly one "eating" philosopher adjacent).
