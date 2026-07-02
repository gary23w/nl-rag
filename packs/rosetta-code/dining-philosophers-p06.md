---
title: "Dining philosophers (part 6/6)"
source: https://rosettacode.org/wiki/Dining_philosophers
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/6
---

## Simula

```mw
COMMENT
!    DEADLOCK IS PREVENTED BY REVERSING THE ORDER OF TAKING THE CHOPSTICKS FOR THE LAST PHILOSOPHER.
!    THAT MEANS ALL PHILOSOPHERS FIRST TAKE THE LEFT CHOPSTICK, THEN THE RIGHT CHOPSTICK.
!    BUT THE LAST PHILOSOPHER FIRST TAKES THE RIGHT CHOPSTICK, THEN THE LEFT.
!
!    THE DETACH STATEMENT IN CLASS PHILOSOPHER GIVES CONTROL BACK TO THE MAIN BLOCK.
!    THE MAIN BLOCK CALLS/RESUMES ALL THE PHILOSOPHERS USING THE RESUME(PHILOSOPHER) STATEMENT.
!    THIS CONTINUES THE CODE IN THE PHILOSOPHER CLASS AFTER THE LAST DETACH STATEMENT.
!    (ANOTHER NAME FOR THIS FEATURE IS THE CONCEPT OF A COROUTINE)
;
BEGIN
    INTEGER N;
    INTEGER PNR, CNR;
    INTEGER SEED;
    SEED := ININT;
    N := 5;
    BEGIN

        CLASS CHOPSTICK;
        BEGIN
            REF(PHILOSOPHER) OWNER;
            INTEGER ID;
            ID := CNR := CNR + 1;
        END CHOPSTICK;

        CLASS PHILOSOPHER(L,R);
            REF(CHOPSTICK) L,R;
        BEGIN
            INTEGER ID;
            ID := PNR := PNR + 1;
            WHILE TRUE DO
            BEGIN
                DETACH;

                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") THINKING...");
                OUTIMAGE;
                DETACH;

                WHILE RANDINT(0,1,SEED) = 0 DO BEGIN
                    OUTTEXT("PHILOSOPHER(");
                    OUTINT(ID, 0);
                    OUTTEXT(") THINKING DEEPER...");
                    OUTIMAGE;
                    DETACH;
                END;

                WHILE L.OWNER =/= NONE DO BEGIN
                    OUTTEXT("PHILOSOPHER(");
                    OUTINT(ID, 0);
                    OUTTEXT(") WAITING FOR LEFT CHOPSTICK(");
                    OUTINT(L.ID, 0);
                    OUTTEXT(") ...");
                    OUTIMAGE;
                    DETACH;
                END;
                L.OWNER :- THIS PHILOSOPHER;
                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") GRABBED LEFT CHOPSTICK(");
                OUTINT(L.ID, 0);
                OUTTEXT(")");
                OUTIMAGE;

                WHILE R.OWNER =/= NONE DO BEGIN
                    OUTTEXT("PHILOSOPHER(");
                    OUTINT(ID, 0);
                    OUTTEXT(") WAITING FOR RIGHT CHOPSTICK(");
                    OUTINT(R.ID, 0);
                    OUTTEXT(") ...");
                    OUTIMAGE;
                    DETACH;
                END;
                R.OWNER :- THIS PHILOSOPHER;
                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") GRABBED RIGHT CHOPSTICK(");
                OUTINT(R.ID, 0);
                OUTTEXT(")");
                OUTIMAGE;

                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") EATING...");
                OUTIMAGE;
                WHILE RANDINT(0,1,SEED) = 0 DO BEGIN
                    DETACH;
                    OUTTEXT("PHILOSOPHER(");
                    OUTINT(ID, 0);
                    OUTTEXT(") STILL EATING...");
                    OUTIMAGE;
                END;
                L.OWNER :- NONE;
                R.OWNER :- NONE;
                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") RELEASED LEFT CHOPSTICK(");
                OUTINT(L.ID, 0);
                OUTTEXT(")");
                OUTIMAGE;
                OUTTEXT("PHILOSOPHER(");
                OUTINT(ID, 0);
                OUTTEXT(") RELEASED RIGHT CHOPSTICK(");
                OUTINT(R.ID, 0);
                OUTTEXT(")");
                OUTIMAGE;
            END;
        END PHILOSOPHER;

        !---------------------------------------|
        !                                       |
        !                                       |
        !                  (3)                  |
        !             P2         P3             |
        !                                       |
        !        (2)                  (4)       |
        !                                       |
        !                                       |
        !      P1                       P4      |
        !                                       |
        !                                       |
        !         (1)              (5)          |
        !                                       |
        !                  P5                   |  only P5 takes Right first (5), then Left (1)
        !                                       |
        !---------------------------------------|
        !;

        REF(PHILOSOPHER) ARRAY PHILS (1:N);
        REF(CHOPSTICK) L, R;
        INTEGER I, LOOPS;

        R :- NEW CHOPSTICK;
        FOR I := 1 STEP 1 UNTIL N-1 DO
        BEGIN
            L :- NEW CHOPSTICK;
            PHILS(I) :- NEW PHILOSOPHER(L,R);
            R :- L;
        END;
        ! REVERSED ORDER FOR THE LAST PHILOSOPHER ;
        PHILS(N) :- NEW PHILOSOPHER(R,PHILS(1).R);

        FOR I := 1 STEP 1 UNTIL N DO BEGIN
            OUTTEXT("PHILOSOPHER(ID=");
            OUTINT(PHILS(I).ID, 0);
            OUTTEXT(", L=");
            OUTINT(PHILS(I).L.ID, 0);
            OUTTEXT(", R=");
            OUTINT(PHILS(I).R.ID, 0);
            OUTTEXT(")");
            OUTIMAGE;
        END;

        FOR LOOPS := 1 STEP 1 UNTIL 10 DO BEGIN
            FOR I := 1 STEP 1 UNTIL N DO BEGIN
                RESUME(PHILS(I));
            END;
        END;

    END;
END.
```

**Input:**

```
12121
```

**Output:**

```
PHILOSOPHER(ID=1, L=2, R=1)
PHILOSOPHER(ID=2, L=3, R=2)
PHILOSOPHER(ID=3, L=4, R=3)
PHILOSOPHER(ID=4, L=5, R=4)
PHILOSOPHER(ID=5, L=5, R=1)
PHILOSOPHER(1) THINKING...
PHILOSOPHER(2) THINKING...
PHILOSOPHER(3) THINKING...
PHILOSOPHER(4) THINKING...
PHILOSOPHER(5) THINKING...
PHILOSOPHER(1) THINKING DEEPER...
PHILOSOPHER(2) GRABBED LEFT CHOPSTICK(3)
PHILOSOPHER(2) GRABBED RIGHT CHOPSTICK(2)
PHILOSOPHER(2) EATING...
PHILOSOPHER(3) THINKING DEEPER...
PHILOSOPHER(4) GRABBED LEFT CHOPSTICK(5)
PHILOSOPHER(4) GRABBED RIGHT CHOPSTICK(4)
PHILOSOPHER(4) EATING...
PHILOSOPHER(5) WAITING FOR LEFT CHOPSTICK(5) ...
PHILOSOPHER(1) WAITING FOR LEFT CHOPSTICK(2) ...
PHILOSOPHER(2) STILL EATING...
PHILOSOPHER(3) WAITING FOR LEFT CHOPSTICK(4) ...
PHILOSOPHER(4) STILL EATING...
PHILOSOPHER(5) WAITING FOR LEFT CHOPSTICK(5) ...
PHILOSOPHER(1) WAITING FOR LEFT CHOPSTICK(2) ...
PHILOSOPHER(2) STILL EATING...
PHILOSOPHER(2) RELEASED LEFT CHOPSTICK(3)
PHILOSOPHER(2) RELEASED RIGHT CHOPSTICK(2)
PHILOSOPHER(3) WAITING FOR LEFT CHOPSTICK(4) ...
PHILOSOPHER(4) STILL EATING...
PHILOSOPHER(5) WAITING FOR LEFT CHOPSTICK(5) ...
PHILOSOPHER(1) GRABBED LEFT CHOPSTICK(2)
PHILOSOPHER(1) GRABBED RIGHT CHOPSTICK(1)
PHILOSOPHER(1) EATING...
PHILOSOPHER(1) RELEASED LEFT CHOPSTICK(2)
PHILOSOPHER(1) RELEASED RIGHT CHOPSTICK(1)
PHILOSOPHER(2) THINKING...
PHILOSOPHER(3) WAITING FOR LEFT CHOPSTICK(4) ...
PHILOSOPHER(4) STILL EATING...
PHILOSOPHER(5) WAITING FOR LEFT CHOPSTICK(5) ...
PHILOSOPHER(1) THINKING...
PHILOSOPHER(2) GRABBED LEFT CHOPSTICK(3)
PHILOSOPHER(2) GRABBED RIGHT CHOPSTICK(2)
PHILOSOPHER(2) EATING...
PHILOSOPHER(2) RELEASED LEFT CHOPSTICK(3)
PHILOSOPHER(2) RELEASED RIGHT CHOPSTICK(2)
PHILOSOPHER(3) WAITING FOR LEFT CHOPSTICK(4) ...
PHILOSOPHER(4) STILL EATING...
PHILOSOPHER(4) RELEASED LEFT CHOPSTICK(5)
PHILOSOPHER(4) RELEASED RIGHT CHOPSTICK(4)
PHILOSOPHER(5) GRABBED LEFT CHOPSTICK(5)
PHILOSOPHER(5) GRABBED RIGHT CHOPSTICK(1)
PHILOSOPHER(5) EATING...
PHILOSOPHER(5) RELEASED LEFT CHOPSTICK(5)
PHILOSOPHER(5) RELEASED RIGHT CHOPSTICK(1)
PHILOSOPHER(1) GRABBED LEFT CHOPSTICK(2)
PHILOSOPHER(1) GRABBED RIGHT CHOPSTICK(1)
PHILOSOPHER(1) EATING...
PHILOSOPHER(2) THINKING...
PHILOSOPHER(3) GRABBED LEFT CHOPSTICK(4)
PHILOSOPHER(3) GRABBED RIGHT CHOPSTICK(3)
PHILOSOPHER(3) EATING...
PHILOSOPHER(4) THINKING...
PHILOSOPHER(5) THINKING...
PHILOSOPHER(1) STILL EATING...
PHILOSOPHER(1) RELEASED LEFT CHOPSTICK(2)
PHILOSOPHER(1) RELEASED RIGHT CHOPSTICK(1)
PHILOSOPHER(2) THINKING DEEPER...
PHILOSOPHER(3) STILL EATING...
PHILOSOPHER(4) THINKING DEEPER...
PHILOSOPHER(5) THINKING DEEPER...
PHILOSOPHER(1) THINKING...
PHILOSOPHER(2) WAITING FOR LEFT CHOPSTICK(3) ...
PHILOSOPHER(3) STILL EATING...
PHILOSOPHER(3) RELEASED LEFT CHOPSTICK(4)
PHILOSOPHER(3) RELEASED RIGHT CHOPSTICK(3)
PHILOSOPHER(4) GRABBED LEFT CHOPSTICK(5)
PHILOSOPHER(4) GRABBED RIGHT CHOPSTICK(4)
PHILOSOPHER(4) EATING...
PHILOSOPHER(5) THINKING DEEPER...
PHILOSOPHER(1) THINKING DEEPER...
PHILOSOPHER(2) GRABBED LEFT CHOPSTICK(3)
PHILOSOPHER(2) GRABBED RIGHT CHOPSTICK(2)
PHILOSOPHER(2) EATING...
PHILOSOPHER(2) RELEASED LEFT CHOPSTICK(3)
PHILOSOPHER(2) RELEASED RIGHT CHOPSTICK(2)
PHILOSOPHER(3) THINKING...
PHILOSOPHER(4) STILL EATING...
PHILOSOPHER(4) RELEASED LEFT CHOPSTICK(5)
PHILOSOPHER(4) RELEASED RIGHT CHOPSTICK(4)
PHILOSOPHER(5) THINKING DEEPER...
```


## Smalltalk

This solution is similar to the Python solution, except this uses Semaphore instances for forks and an OrderedCollection to hold sequence of forks and philosophers around the table. The method #pickUpForks releases and retries after a small delay till it has both. **Special note:** Smalltalk concurrent processes are created by sending the message #fork to a block. Do not confuse this method name with the forks of the problem domain.

```mw
'From Squeak3.7 of ''4 September 2004'' [latest update: #5989] on 13 October 2011 at 2:44:42 pm'!
Object subclass: #Philosopher
	instanceVariableNames: 'table random name seat forks running'
	classVariableNames: ''
	poolDictionaries: ''
	category: 'rosettacode'!

!Philosopher methodsFor: 'private'!
createfork
	^ Semaphore forMutualExclusion! !

!Philosopher methodsFor: 'private'!
displayState: aStateName 
	Transcript show: name , ' is ' , aStateName;
		 cr! !

!Philosopher methodsFor: 'private'!
pickUpForkAt: relativePosition 
	| fork pos |
	pos := self tableIndex: seat + relativePosition.
	(fork := table at: pos)
		ifNotNil: [fork
				critical: [(table at: pos) notNil
						ifTrue: [table at: pos put: nil]
						ifFalse: [fork := nil]]].
	^ (forks at: relativePosition put: fork) notNil! !

!Philosopher methodsFor: 'private'!
putBackForkAt: aRelativePosition 
	| fork |
	fork := forks at: aRelativePosition.
	fork
		ifNotNil: [table
				at: (self tableIndex: seat + aRelativePosition)
				put: fork.
			forks at: aRelativePosition put: nil]! !

!Philosopher methodsFor: 'private'!
tableIndex: aNum 
	^ aNum - 1 \\ table size + 1! !

!Philosopher methodsFor: 'private'!
waitRandomTime
	(Delay forMilliseconds: (random next * 4000) rounded) wait! !

!Philosopher methodsFor: 'dining'!
eat
	self displayState: 'eating';
		 waitRandomTime;
		 putBackForkAt: -1;
		 putBackForkAt: 1! !

!Philosopher methodsFor: 'dining'!
pickUpForks
	self displayState: 'trying to pick up forks'.
	[(self pickUpForkAt: -1)
		ifTrue: [(self pickUpForkAt: 1)
				ifFalse: [self putBackForkAt: -1]].
	(forks at: 1) notNil]
		whileFalse: [(Delay forMilliseconds: 10) wait]! !

!Philosopher methodsFor: 'dining'!
think
	self displayState: 'thinking';
		 waitRandomTime! !

!Philosopher methodsFor: 'initialize-release'!
beginDining: aName at: aTable 
	name := aName.
	table := aTable.
	forks := Dictionary new at: -1 put: nil;
				 at: 1 put: nil;
				 yourself.
	random := Random new seed: name hash.
	seat := table size + 1.
	table add: self;
		 add: self createfork.
	running := true.
	[(Delay forSeconds: 20) wait.
	running := false] fork.
	[[running]
		whileTrue: [self think; pickUpForks; eat].
	nil] fork! !

"-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- "!

Philosopher class
	instanceVariableNames: ''!

!Philosopher class methodsFor: 'examples'!
diningPhilosophersTest
	| diningTable |
	diningTable := OrderedCollection new.
	#('Aristotle' 'Kant' 'Buddha' 'Marx' 'Russel' )
		do: [:aName | Philosopher new beginDining: aName at: diningTable]! !
```


## Tcl

Works with

:

Tcl

version 8.6

```mw
package require Thread

foreach name {Aristotle Kant Spinoza Marx Russel} {
    lappend forks [thread::mutex create]
    lappend tasks [set t [thread::create -preserved {
        # Implement each task as a coroutine internally for simplicity of presentation
        # This is because we want to remain able to receive messages so we can shut
        # down neatly at the end of the program.
	interp alias {} doTask {} coroutine t philosopher
	proc delay {expression} {
	    yield [after [expr $expression] [info coroutine]]
	}

        # Forks are mutexes...
        proc pickUpFork fork {
            thread::mutex lock $fork
        }
        proc putDownFork fork {
            thread::mutex unlock $fork
        }

        # The actual implementation of the task
	proc philosopher {f1 f2} {
	    global name
	    # Always acquire forks in order; prevents deadlock
            # Uses the "natural" order of the lexicographical order of the fork names
	    if {$f1 > $f2} {
                lassign [list $f1 $f2] f2 f1
            }

            # The classic "philosophers" loop
	    while {true} {
		puts "$name is thinking"
		delay {int(200*rand())}

		puts "$name is hungry, getting fork in left hand"
		pickUpFork $f1
		delay {int(2000*rand())} ;# Make deadlock likely if it is possible!

		puts "$name is hungry, getting fork in right hand"
		pickUpFork $f2

		puts "$name is eating"
		delay {int(2000*rand())}

		puts "$name has finished eating; putting down forks"
		putDownFork $f2
		putDownFork $f1
                delay 100
	    }
	}
	thread::wait
    }]]
    thread::send $t [list set name $name]
}

# Set the tasks going
foreach t $tasks {f1 f2} {0 1 1 2 2 3 3 4 4 0} {
    thread::send -async $t [list \
            doTask [lindex $forks $f1] [lindex $forks $f2]]
}

# Kill everything off after 30 seconds; that's enough for demonstration!
after 30000
puts "Completing..."
foreach t $tasks {
    thread::send -async $t thread::exit
}
```


## VBA

Unfortunately, VBA is single threaded. The task is implemented by introducing a separate program counter for each individual philosopher. While the routine dine loops through all philosophers the routine philosopher execute the actions for each philosopher separately, as if in separate threads. Program terminates after max count is reached. Statistics show how many program ticks are spent at each step at the dining table.

```mw
'The combination of holding to the second fork
'(HOLDON=True) and all philosophers start
'with same hand (DIJKSTRASOLUTION=False) leads
'to a deadlock. To prevent deadlock
'set HOLDON=False, and DIJKSTRASOLUTION=True.
Public Const HOLDON = False
Public Const DIJKSTRASOLUTION = True
Public Const X = 10 'chance to continue eating/thinking
Public Const GETS = 0
Public Const PUTS = 1
Public Const EATS = 2
Public Const THKS = 5
Public Const FRSTFORK = 0
Public Const SCNDFORK = 1
Public Const SPAGHETI = 0
Public Const UNIVERSE = 1
Public Const MAXCOUNT = 100000
Public Const PHILOSOPHERS = 5
Public semaphore(PHILOSOPHERS - 1) As Integer
Public positi0n(1, PHILOSOPHERS - 1) As Integer
Public programcounter(PHILOSOPHERS - 1) As Long
Public statistics(PHILOSOPHERS - 1, 5, 1) As Long
Public names As Variant
Private Sub init()
    names = [{"Aquinas","Babbage","Carroll","Derrida","Erasmus"}]
    For j = 0 To PHILOSOPHERS - 2
        positi0n(0, j) = j + 1 'first fork in right hand
        positi0n(1, j) = j     'second fork in left hand
    Next j
    If DIJKSTRASOLUTION Then
        positi0n(0, PHILOSOPHERS - 1) = j '  first fork in left hand
        positi0n(1, PHILOSOPHERS - 1) = 0 'second fork in right hand
    Else
        positi0n(0, PHILOSOPHERS - 1) = 0 'first fork in right hand
        positi0n(1, PHILOSOPHERS - 1) = j 'second fork in left hand
    End If
End Sub
Private Sub philosopher(subject As Integer, verb As Integer, objekt As Integer)
    statistics(subject, verb, objekt) = statistics(subject, verb, objekt) + 1
    If verb < 2 Then
        If semaphore(positi0n(objekt, subject)) <> verb Then
            If Not HOLDON Then
                'can't get a fork, release first fork if subject has it, and
                'this won't toggle the semaphore if subject hasn't firt fork
                semaphore(positi0n(FRSTFORK, subject)) = 1 - objekt
                'next round back to try to get first fork
                programcounter(subject) = 0
            End If
        Else
            'just toggle semaphore and move on
            semaphore(positi0n(objekt, subject)) = 1 - verb
            programcounter(subject) = (programcounter(subject) + 1) Mod 6
        End If
    Else
        'when eating or thinking, (100*(X-1)/X)% continue eating or thinking
        '(100/X)% advance program counter
        programcounter(subject) = IIf(X * Rnd > 1, verb, verb + 1) Mod 6
    End If
End Sub
Private Sub dine()
    Dim ph As Integer
    Do While TC < MAXCOUNT
        For ph = 0 To PHILOSOPHERS - 1
            Select Case programcounter(ph)
                Case 0: philosopher ph, GETS, FRSTFORK
                Case 1: philosopher ph, GETS, SCNDFORK
                Case 2: philosopher ph, EATS, SPAGHETI
                Case 3: philosopher ph, PUTS, FRSTFORK
                Case 4: philosopher ph, PUTS, SCNDFORK
                Case 5: philosopher ph, THKS, UNIVERSE
            End Select
            TC = TC + 1
        Next ph
    Loop
End Sub
Private Sub show()
    Debug.Print "Stats", "Gets", "Gets", "Eats", "Puts", "Puts", "Thinks"
    Debug.Print "", "First", "Second", "Spag-", "First", "Second", "About"
    Debug.Print "", "Fork", "Fork", "hetti", "Fork", "Fork", "Universe"
    For subject = 0 To PHILOSOPHERS - 1
        Debug.Print names(subject + 1),
        For objekt = 0 To 1
            Debug.Print statistics(subject, GETS, objekt),
        Next objekt
        Debug.Print statistics(subject, EATS, SPAGHETI),
        For objekt = 0 To 1
            Debug.Print statistics(subject, PUTS, objekt),
        Next objekt
        Debug.Print statistics(subject, THKS, UNIVERSE)
    Next subject
End Sub
Public Sub main()
    init
    dine
    show
End Sub
```

**Output:**

```
Stats         Gets          Gets          Eats          Puts          Puts          Thinks
              First         Second        Spag-         First         Second        About
              Fork          Fork          hetti         Fork          Fork          Universe
Aquinas        5595          1902          5843          550           550           5560 
Babbage        5811          2360          5585          529           529           5186 
Carroll        6445          2359          4929          523           523           5221 
Derrida        6341          1828          5479          545           545           5262 
Erasmus        5998          1556          5891          550           550           5455 
```


## Visual Basic .NET

This has three modes.

- In the first mode a dead lock will occur if each philosopher picks up their left fork before any pick up their right.
- In the second mode each philosopher will put down their left fork if they cannot pick up their right. This is susceptible to *live lock*, where each philosopher keeps retrying but never makes any progress.
- In the third mode, each fork is numbered. The philosopher will always pick up a lower number fork before a higher number fork, thus preventing a dead-lock while guaranteeing forward progress.

```mw
Imports System.Threading
Module Module1
   Public rnd As New Random

   Sub Main()
       'Aristotle, Kant, Spinoza, Marx, and Russel 
       Dim f1 As New Fork(1)
       Dim f2 As New Fork(2)
       Dim f3 As New Fork(3)
       Dim f4 As New Fork(4)
       Dim f5 As New Fork(5)

       Console.WriteLine("1: Deadlock")
       Console.WriteLine("2: Live lock")
       Console.WriteLine("3: Working")
       Select Console.ReadLine
           Case "1"
               Using _
                   Aristotle As New SelfishPhilosopher("Aristotle", f1, f2), _
                   Kant As New SelfishPhilosopher("Kant", f2, f3), _
                   Spinoza As New SelfishPhilosopher("Spinoza", f3, f4), _
                   Marx As New SelfishPhilosopher("Marx", f4, f5), _
                   Russel As New SelfishPhilosopher("Russel", f5, f1)

                   Console.ReadLine()
               End Using
           Case "2"
               Using _
                   Aristotle As New SelflessPhilosopher("Aristotle", f1, f2), _
                   Kant As New SelflessPhilosopher("Kant", f2, f3), _
                   Spinoza As New SelflessPhilosopher("Spinoza", f3, f4), _
                   Marx As New SelflessPhilosopher("Marx", f4, f5), _
                   Russel As New SelflessPhilosopher("Russel", f5, f1)

                   Console.ReadLine()
               End Using
           Case "3"
               Using _
                   Aristotle As New WisePhilosopher("Aristotle", f1, f2), _
                   Kant As New WisePhilosopher("Kant", f2, f3), _
                   Spinoza As New WisePhilosopher("Spinoza", f3, f4), _
                   Marx As New WisePhilosopher("Marx", f4, f5), _
                   Russel As New WisePhilosopher("Russel", f5, f1)

                   Console.ReadLine()
               End Using
       End Select
   End Sub

End Module
```

```mw
Class Fork
   Private ReadOnly m_Number As Integer
   Public Sub New(ByVal number As Integer)
       m_Number = number
   End Sub
   Public ReadOnly Property Number() As Integer
       Get
           Return m_Number
       End Get
   End Property
End Class
```

```mw
MustInherit Class PhilosopherBase
   Implements IDisposable

   Protected m_Disposed As Boolean
   Protected ReadOnly m_Left As Fork
   Protected ReadOnly m_Right As Fork
   Protected ReadOnly m_Name As String
   Public Sub New(ByVal name As String, ByVal right As Fork, ByVal left As Fork)
       m_Name = name
       m_Right = right
       m_Left = left
       Dim t As New Thread(AddressOf MainLoop)
       t.IsBackground = True
       t.Start()
   End Sub
   Protected Overridable Sub Dispose(ByVal disposing As Boolean)
       m_Disposed = True
   End Sub

   Public Sub Dispose() Implements IDisposable.Dispose
       Dispose(True)
       GC.SuppressFinalize(Me)
   End Sub
   Public ReadOnly Property Name() As String
       Get
           Return m_Name
       End Get
   End Property

   Public MustOverride Sub MainLoop()
End Class
```

### Deadlock

```mw
Class SelfishPhilosopher
   Inherits PhilosopherBase
   Public Sub New(ByVal name As String, ByVal right As Fork, ByVal left As Fork)
       MyBase.New(name, right, left)
   End Sub

   Public Overrides Sub MainLoop()
       Do
           Console.WriteLine(Name & " sat down")
           SyncLock m_Left
               Console.WriteLine(Name & " picked up fork " & m_Left.Number)

               SyncLock m_Right
                   Console.WriteLine(Name & " picked up fork " & m_Right.Number)

                   Console.WriteLine(Name & " ate!!!!")

                   Console.WriteLine(Name & " put down fork " & m_Right.Number)
               End SyncLock

               Console.WriteLine(Name & " put down fork " & m_Left.Number)
           End SyncLock

           Console.WriteLine(Name & " stood up")

           Thread.Sleep(rnd.Next(0, 10000))
       Loop Until m_Disposed
   End Sub

End Class
```

### Live Lock

```mw
Class SelflessPhilosopher
   Inherits PhilosopherBase

   Public Sub New(ByVal name As String, ByVal right As Fork, ByVal left As Fork)
       MyBase.New(name, right, left)
   End Sub

   Public Overrides Sub MainLoop()
       Do
           Console.WriteLine(Name & " sat down")
           Dim needDelay = False
TryAgain:
           If needDelay Then Thread.Sleep(rnd.Next(0, 10000))
           Try
               Monitor.Enter(m_Left)
               Console.WriteLine(Name & " picked up fork " & m_Left.Number)

               If Monitor.TryEnter(m_Right) Then
                   Console.WriteLine(Name & " picked up fork " & m_Right.Number)

                   Console.WriteLine(Name & " ate!!!!!!")

                   Console.WriteLine(Name & " put down fork " & m_Right.Number)
                   Monitor.Exit(m_Right)
               Else
                   Console.WriteLine(Name & " is going to wait")
                   needDelay = True
                   GoTo TryAgain
               End If
           Finally
               Console.WriteLine(Name & " put down fork " & m_Left.Number)
           End Try

           Console.WriteLine(Name & " stood up")

           Thread.Sleep(rnd.Next(0, 10000))

       Loop Until m_Disposed
   End Sub

End Class
```

### Working

```mw
Class WisePhilosopher
   Inherits PhilosopherBase
   Public Sub New(ByVal name As String, ByVal right As Fork, ByVal left As Fork)
       MyBase.New(name, right, left)
   End Sub

   Public Overrides Sub MainLoop()
       Do
           Console.WriteLine(Name & " sat down")

           Dim first As Fork, second As Fork
           If m_Left.Number > m_Right.Number Then
               first = m_Left
               second = m_Right
           Else
               first = m_Right
               second = m_Left
           End If

           SyncLock first
               Console.WriteLine(Name & " picked up fork " & m_Left.Number)

               SyncLock second
                   Console.WriteLine(Name & " picked up fork " & m_Right.Number)

                   Console.WriteLine(Name & " ate!!!!")

                   Console.WriteLine(Name & " put down fork " & m_Right.Number)
               End SyncLock

               Console.WriteLine(Name & " put down fork " & m_Left.Number)
           End SyncLock

           Console.WriteLine(Name & " stood up")

           Thread.Sleep(rnd.Next(0, 10000))
       Loop Until m_Disposed
   End Sub

End Class
```


## Wren

This is loosely based on the Kotlin entry.

However, Wren uses co-operatively scheduled fibers rather than threads for concurrency and, as long as a philosoper waits until he can pick up both forks to eat, deadlock is impossible because only one fiber can run at a time.

```mw
import "random" for Random
import "scheduler" for Scheduler
import "timer" for Timer

var Rand = Random.new()

var ForkInUse = List.filled(5, false)

class Fork {
    construct new(name, index) {
        _name = name
        _index = index
    }

    index { _index }

    pickUp(philosopher) {
        System.print("  %(philosopher) picked up %(_name)")
        ForkInUse[index] = true
    }

    putDown(philosopher) {
        System.print("  %(philosopher) put down %(_name)")
        ForkInUse[index] = false
    }
}

class Philosopher {
    construct new(pname, f1, f2) {
        _pname = pname
        _f1 = f1
        _f2 = f2
    }

    delay() { Timer.sleep(Rand.int(300) + 100) }

    eat() {
        (1..5).each { |bite|  // limit to 5 bites say
            while (true) {
                System.print("%(_pname) is hungry")
                if (!ForkInUse[_f1.index] && !ForkInUse[_f2.index]) {
                    _f1.pickUp(_pname)
                    _f2.pickUp(_pname)
                    break
                }
                System.print("%(_pname) is unable to pick up both forks")
                // try again later
                delay()
            }
            System.print("%(_pname) is eating bite %(bite)")
            // allow time to eat
            delay()
            _f2.putDown(_pname)
            _f1.putDown(_pname)
            // allow other philospohers time to pick up forks
            delay()
        }
    }
}

var diningPhilosophers = Fn.new { |names|
    var size = names.count
    var forks = List.filled(size, null)
    for (i in 0...size) forks[i] = Fork.new("Fork %(i + 1)", i)
    var philosophers = []
    var i = 0
    for (n in names) {
        var i1 = i
        var i2 = (i + 1) % size
        if (i2 < i1) {
            i1 = i2
            i2 = i
        }
        var p = Philosopher.new(n, forks[i1], forks[i2])
        philosophers.add(p)
        i = i + 1
    }
    // choose a philosopher at random to start eating
    var r = Rand.int(size)
    // schedule the others to eat later
    for (i in 0...size) if (i != r) Scheduler.add { philosophers[i].eat() }
    philosophers[r].eat()
}

var names = ["Aristotle", "Kant", "Spinoza", "Marx", "Russell"]
diningPhilosophers.call(names)
```


## zkl

The model used here is five seats, each with two forks. Sn:(Fn,Fn+1). Seat(n+1) shares a fork with seat n and so on. Fork are represented by an atomic bool, a bool that changes state atomically. Each philosopher is a thread. Each philosopher is ambidextrous, leading with a random hand. If the trailing hand can not get a fork, the already in hand fork is put down.

```mw
var [const] forks=(5).pump(List,Atomic.Bool.fp(False)),  // True==fork in use
    seats=(5).pump(List,'wrap(n){ List(forks[n],forks[(n+1)%5]) });
fcn sitAndEat(name,n){  // assigned seating
   while(1){
      fa,fb:=seats[n].shuffle(); // ambidextrous
      if(fa.setIf(True,False)){  // got the first fork
	 if(fb.setIf(True,False)){  // got the other fork, nom nom time
	    name.println(" is eating"); 
	    Atomic.sleep((1).random(5));
	    fa.set(False); fb.set(False);  // put forks down
	    return();  // leave the table
	 }
	 else{
	    fa.set(False);  // put fork down, try again in a bit
	    name.println(": Could not get two forks");
	 }
      } else name.println(": Could not get first fork");
      Atomic.sleep((1).random(2));  // sits for a bit
   }
}
fcn philo([(seat,name)]){  // a thread
   while(1){  // eat and think forever
      name.println(" is thinking."); Atomic.sleep((1).random(5));
      sitAndEat(name,seat);
   }
}
```

The setIf method atomically sets the bool to the first value if it is currently the second value.

```mw
T("Aristotle", "Kant", "Spinoza", "Marx", "Russell").enumerate()
.apply(philo.launch);

Atomic.sleep(100000);  // hang out in the REPL, aka thread keep alive
```

**Output:**

```
...
Aristotle: Could not get two forks
Russell: Could not get two forks
Aristotle: Could not get two forks
Russell: Could not get first fork
Spinoza: Could not get first fork
Kant is thinking.
Aristotle is eating
...
```

Retrieved from "

https://rosettacode.org/wiki/Dining_philosophers?oldid=386918

"
