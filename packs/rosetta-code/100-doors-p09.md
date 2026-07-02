---
title: "100 doors (part 9/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 9/10
---

## Scilab

Translation of

:

Octave

```mw
doors=zeros(1,100);
for i = 1:100
  for j = i:i:100
    doors(j) = ~doors(j);
  end
end
for i = 1:100
  if ( doors(i) )
    s = "open";
  else
    s = "closed";
  end
  printf("%d %s\n", i, s);
end
```

**Output:**

```
1 open
2 closed
3 closed
4 open
5 closed
6 closed
7 closed
8 closed
9 open
10 closed
11 closed
12 closed
13 closed
14 closed
15 closed
16 open
17 closed
18 closed
19 closed
20 closed
21 closed
22 closed
23 closed
24 closed
25 open
26 closed
27 closed
28 closed
29 closed
30 closed
31 closed
32 closed
33 closed
34 closed
35 closed
36 open
37 closed
38 closed
39 closed
40 closed
41 closed
42 closed
43 closed
44 closed
45 closed
46 closed
47 closed
48 closed
49 open
50 closed
51 closed
52 closed
53 closed
54 closed
55 closed
56 closed
57 closed
58 closed
59 closed
60 closed
61 closed
62 closed
63 closed
64 open
65 closed
66 closed
67 closed
68 closed
69 closed
70 closed
71 closed
72 closed
73 closed
74 closed
75 closed
76 closed
77 closed
78 closed
79 closed
80 closed
81 open
82 closed
83 closed
84 closed
85 closed
86 closed
87 closed
88 closed
89 closed
90 closed
91 closed
92 closed
93 closed
94 closed
95 closed
96 closed
97 closed
98 closed
99 closed
100 open
```


## Scratch

Scratch is a visual programming language. Click the link, then "see inside" to see the code.

https://scratch.mit.edu/projects/168687954/

Output: 100 indications that "Door ___ is _____," where doors with perfect square indices are open and the rest are closed.


## Seed7

**unoptimized**

```mw
$ include "seed7_05.s7i";
 
const proc: main is func
  local
    var array boolean: doorOpen is 100 times FALSE;
    var integer: pass is 0;
    var integer: index is 0;
    var array[boolean] string: closedOrOpen is [boolean] ("closed", "open");
  begin
    for pass range 1 to 100 do
      for key index range doorOpen do
        if index rem pass = 0 then
          doorOpen[index] := not doorOpen[index];
        end if;
      end for;
    end for;
    for key index range doorOpen do
      write(index lpad 3 <& " is " <& closedOrOpen[doorOpen[index]] rpad 7);
      if index rem 5 = 0 then
        writeln;
      end if;
    end for;
  end func;
```

**optimized**

```mw
$ include "seed7_05.s7i";

const proc: main is func
  local
    var integer: index is 0;
    var integer: number is 0;
    var array[boolean] string: closedOrOpen is [boolean] ("closed", "open");
  begin
    for index range 1 to 100 do
      number := sqrt(index);
      write(index lpad 3 <& " is " <& closedOrOpen[number**2 = index] rpad 7);
      if index rem 5 = 0 then
        writeln;
      end if;
    end for;
  end func;
```

Output of both programs:

```
  1 is open     2 is closed   3 is closed   4 is open     5 is closed 
  6 is closed   7 is closed   8 is closed   9 is open    10 is closed 
 11 is closed  12 is closed  13 is closed  14 is closed  15 is closed 
 16 is open    17 is closed  18 is closed  19 is closed  20 is closed 
 21 is closed  22 is closed  23 is closed  24 is closed  25 is open   
 26 is closed  27 is closed  28 is closed  29 is closed  30 is closed 
 31 is closed  32 is closed  33 is closed  34 is closed  35 is closed 
 36 is open    37 is closed  38 is closed  39 is closed  40 is closed 
 41 is closed  42 is closed  43 is closed  44 is closed  45 is closed 
 46 is closed  47 is closed  48 is closed  49 is open    50 is closed 
 51 is closed  52 is closed  53 is closed  54 is closed  55 is closed 
 56 is closed  57 is closed  58 is closed  59 is closed  60 is closed 
 61 is closed  62 is closed  63 is closed  64 is open    65 is closed 
 66 is closed  67 is closed  68 is closed  69 is closed  70 is closed 
 71 is closed  72 is closed  73 is closed  74 is closed  75 is closed 
 76 is closed  77 is closed  78 is closed  79 is closed  80 is closed 
 81 is open    82 is closed  83 is closed  84 is closed  85 is closed 
 86 is closed  87 is closed  88 is closed  89 is closed  90 is closed 
 91 is closed  92 is closed  93 is closed  94 is closed  95 is closed 
 96 is closed  97 is closed  98 is closed  99 is closed 100 is open   
```


## SenseTalk

```mw
put false repeated 100 times as a list into Doors100

repeat 1 to 100
	set step to it
	repeat step to 100 by step 
		set newValue to not item it of Doors100
		set item it of Doors100 to newValue
	end repeat
end repeat

put the counter for each item of Doors100 which is true
```

Output:

```
(1,4,9,16,25,36,49,64,81,100)
```


## SequenceL

**Unoptimized**

```mw
import <Utilities/Sequence.sl>;

main:=
	let
		doors := flipDoors(duplicate(false, 100), 1);
		open[i] := i when doors[i];
	in
		open;
	
flipDoors(doors(1), count) :=
	let
		newDoors[i] := not doors[i] when i mod count = 0 else doors[i];
	in
		doors when count >= 100 else flipDoors(newDoors, count + 1);
```

**Optimized**

```mw
main := flipDoors([1], 2);

flipDoors(openDoors(1), i) :=
	openDoors when i * i >= 100 else flipDoors(openDoors ++ [i * i], i + 1);
```


## SETL

**Unoptimized**

```mw
program hundred_doors;

const toggle := {['open', 'closed'], ['closed', 'open']};

doorStates := ['closed'] * 100;

(for interval in [1..100])
  doorStates := [if i mod interval = 0 then
                    toggle(prevState) else
                    prevState end:
                 prevState = doorStates(i)];
end;

(for finalState = doorStates(i))
  print('door', i, 'is', finalState);
end;

end program;
```

If 'open' weren't a reserved word, we could omit the single quotes around it.

**Optimized** Exploits the fact that squares are separated by successive odd numbers. Use array replication to insert the correct number of closed doors in between the open ones.

```mw
program hundred_doors;

doorStates := (+/ [['closed'] * oddNum with 'open': oddNum in [1,3..17]]);

(for finalState = doorStates(i))
  print('door', i, 'is', finalState);
end;

end program;
```


## SheerPower 4GL

```mw
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!         I n i t i a l i z a t i o n
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
doors% = 100

dim doorArray?(doors%)

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!         M a i n   L o g i c   A r e a
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

// Initialize Array
for index% = 1 to doors%
  doorArray?(index%) = false
next index%

// Execute routine
toggle_doors

// Print results
for index% = 1 to doors%
  if doorArray?(index%) = true then print index%, ' is open'
next index%

stop

!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
!         R o u t i n e s
!%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
routine toggle_doors
  for index_outer% = 1 to doors%
    for index_inner% = 1 to doors%
      if mod(index_inner%, index_outer%) = 0 then
        doorArray?(index_inner%) = not doorArray?(index_inner%) 
      end if
    next index_inner%
  next index_outer%
end routine

end
```


## Sidef

**Unoptimized**

```mw
var doors = []

{ |pass|
    { |i|
        if (pass `divides` i) {
            doors[i] := false -> not!
        }
    } << 1..100
} << 1..100

{ |i|
    say ("Door %3d is %s" % (i, doors[i] ? 'open' : 'closed'))
} << 1..100
```

**Optimized**

```mw
{ |i|
    "Door %3d is %s\n".printf(i, <closed open>[i.is_sqr])
} << 1..100
```


## Simula

```mw
BEGIN
    INTEGER LIMIT = 100, door, stride;
    BOOLEAN ARRAY DOORS(1:LIMIT);
    TEXT intro;

    FOR stride := 1 STEP 1 UNTIL LIMIT DO
        FOR door := stride STEP stride UNTIL LIMIT DO
            DOORS(door) := NOT DOORS(door);

    intro :- "All doors closed but ";
    FOR door := 1 STEP 1 UNTIL LIMIT DO
        IF DOORS(door) THEN BEGIN
            OUTTEXT(intro); OUTINT(door, 0); intro :- ", "
        END;
    OUTIMAGE
END.
```

**Output:**

```
All doors closed but 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```


## Slate

**Unoptimized**

```mw
define: #a -> (Array newSize: 100).
a infect: [| :_ | False].

a keysDo: [| :pass |
  pass to: a indexLast by: pass do: [| :door |
    a at: door infect: #not `er]].

a keysAndValuesDo: [| :door :isOpen |
  inform: 'door #' ; door ; ' is ' ; (isOpen ifTrue: ['open'] ifFalse: ['closed'])].
```

**Optimized**

```mw
define: #a -> (Array newSize: 100).
a infect: [| :_ | False].

0 below: 10 do: [| :door | a at: door squared put: True].
a keysAndValuesDo: [| :door :isOpen |
  inform: 'door #' ; door ; ' is ' ; (isOpen ifTrue: ['open'] ifFalse: ['closed'])].
```


## Smalltalk

Works with

:

GNU Smalltalk

**Unoptimized**

```mw
|a|
a := Array new: 100 .
1 to: 100 do: [ :i | a at: i put: false ].

1 to: 100 do: [ :pass |
  pass to: 100 by: pass do: [ :door |
    a at: door put: (a at: door) not .
  ]
].

"output"
1 to: 100 do: [ :door |
   ( 'door #%1 is %2' %
     { door . (a at: door) ifTrue: [ 'open' ] ifFalse: [ 'closed' ] } ) displayNl
]
```

**Optimized**

```mw
|a|
a := (1 to: 100) collect: [ :x | false ].
1 to: 10 do: [ :i | a at: (i squared) put: true ].
1 to: 100 do: [ :i |
   ( 'door #%1 is %2' % { i . 
           (a at: i) ifTrue: [ 'open' ] 
                     ifFalse: [ 'closed' ] }
   ) displayNl
]
```

Works with

:

Squeak Smalltalk

**Unoptimized, using Morphs**

```mw
| m w h smh smw delay closedDoor border subMorphList |

closedDoor := Color black.
border := Color veryLightGray.
delay := Delay forMilliseconds: 50.
w := World bounds corner x.
h := (World bounds corner y) / 2.
smw := w/100.
smh := h/2.

m := BorderedMorph new position: 0@h.
m height: smh; width: w; borderColor: border.
m color: Color veryLightGray.

1 to: 100 do: [ :pos || sm |
	sm := BorderedMorph new height: smh ; width: smw ; 
		borderColor: border; color: closedDoor; 
		position: (smw*pos)@h.
	m addMorph: sm asElementNumber: pos].

m openInWorld.
delay wait.
subMorphList := m submorphs.
"display every step"
[1 to: 100 do: [ :step |
	step to: 100 by: step do: [ :pos | | subMorph |
		subMorph := subMorphList at: pos.
		subMorph color: subMorph color negated.
		delay wait]]] fork.
```


## smart BASIC

```mw
x=1!y=3!z=0
PRINT "Open doors: ";x;" ";
DO
    z=x+y
    PRINT z;" ";
    x=z
    y=y+2
UNTIL z>=100
END
```


## SNOBOL4

**unoptimized**

```mw
		DEFINE('PASS(A,I),O')		:(PASS.END)
PASS		O = 0
PASS.LOOP	O = O + I
		EQ(A<O>,1)			:S(PASS.1)F(PASS.0)
PASS.0		A<O> = 1			:S(PASS.LOOP)F(RETURN)
PASS.1		A<O> = 0			:S(PASS.LOOP)F(RETURN)
PASS.END
 
MAIN		D = ARRAY(100,0)
		I = 0
 
MAIN.LOOP	I = LE(I,100) I + 1		:F(OUTPUT)
		PASS(D,I)			:(MAIN.LOOP)
 
OUTPUT		I = 1 ; OPEN = 'Opened doors are: '
OUTPUT.LOOP	OPEN = OPEN EQ(D<I>,1) " " I
		I = LE(I,100) I + 1		:S(OUTPUT.LOOP)F(OUTPUT.WRITE)
OUTPUT.WRITE	OUTPUT = OPEN

END
```

A run of this using CSNOBOL4 looks like this:

```
$ snobol4 100doors.sno 
The Macro Implementation of SNOBOL4 in C (CSNOBOL4) Version 1.3+
    by Philip L. Budne, January 23, 2011
SNOBOL4 (Version 3.11, May 19, 1975)
    Bell Telephone Laboratories, Incorporated

No errors detected in source program

Opened doors are:  1 4 9 16 25 36 49 64 81 100
Normal termination at level 0
100doors.sno:18: Last statement executed was 19
```

(There are command flags to remove the header and the summary, but these have been left in to keep the original SNOBOL4 experience intact.)

**optimized**

```mw
MAIN		D = ARRAY(100,0)
		I = 1

MAIN.LOOP	LE(I, 10)			:F(OUTPUT)
		D<I ** 2> = 1		
		I = I + 1			:(MAIN.LOOP)

OUTPUT		I = 1 ; O = 'Opened doors are: '
OUTPUT.LOOP	O = O EQ(D<I>,1) " " I
		I = LE(I,100) I + 1		:S(OUTPUT.LOOP)F(OUTPUT.WRITE)
OUTPUT.WRITE	OUTPUT = O
END
```

The output of this version is almost identical to the above.


## SparForte

As a structured script.

```mw
#!/usr/local/bin/spar
pragma annotate( summary, "doors" )
       @( description, "Problem: You have 100 doors in a row that are all initially closed. You" )
       @( description, "make 100 passes by the doors. The first time through, you visit every door" )
       @( description, "and toggle the door (if the door is closed, you open it; if it is open, you" )
       @( description, "close it). The second time you only visit every 2nd door (door #2, #4, #6," )
       @( description, "...). The third time, every 3rd door (door #3, #6, #9, ...), etc, until you" )
       @( description, "only visit the 100th door." )
       @( description, "Question: What state are the doors in after the last pass? Which are open," )
       @( description, "which are closed?" )
       @( see_also, "http://rosettacode.org/wiki/100_doors" )
       @( author, "Ken O. Burtch" );
pragma license( unrestricted );

pragma restriction( no_external_commands );

procedure Doors is
   type Door_State is (Closed, Open);
   type Door_List is array(1..100) of Door_State;
   The_Doors : Door_List;
begin
   for I in 1..100 loop
      The_Doors(I) := Closed;
   end loop;
   for I in 1..100 loop
      for J in arrays.first(The_Doors)..arrays.last(The_Doors) loop
         if J mod I = 0 then
            if The_Doors(J) = Closed then
                The_Doors(J) := Open;
            else
               The_Doors(J) := Closed;
            end if;
         end if;
      end loop;
   end loop;
   for I in arrays.first(The_Doors)..arrays.last(The_Doors) loop
      put (I) @ (" is ") @ (The_Doors(I));
      new_line;
   end loop;
end Doors;
```


## Sparkling

**unoptimized**

```mw
/* declare the variables */
var isOpen = {};
var pass, door;

/* initialize the doors */
for door = 0; door < 100; door++ {
	isOpen[door] = true;
}

/* do the 99 remaining passes */
for pass = 1; pass < 100; ++pass {
	for door = pass; door < 100; door += pass+1 {
  		isOpen[door] = !isOpen[door];
	}
}

/* print the results */
var states = { true: "open", false: "closed" };
for door = 0; door < 100; door++ {
	printf("Door #%d is %s.\n", door+1, states[isOpen[door]]);
}
```

**optimized**

```mw
/* declare the variables */
var door_sqrt = 1;
var door;

/* print the perfect square doors as open */
for door = 0; door < 100; door++ {
	if (door_sqrt*door_sqrt == door+1) {
		printf("Door #%d is open.\n", door+1);
		door_sqrt ++;
	} else {
		printf("Door #%d is closed.\n", door+1);
	}
}
```


## Spin

Works with

:

BST/BSTC

Works with

:

FastSpin/FlexSpin

Works with

:

HomeSpun

Works with

:

OpenSpin

```mw
con
  _clkmode = xtal1+pll16x
  _clkfreq = 80_000_000

obj
  ser : "FullDuplexSerial.spin"

pub init
  ser.start(31, 30, 0, 115200)

  doors

  waitcnt(_clkfreq + cnt)
  ser.stop
  cogstop(0)

var

  byte door[101] ' waste one byte by using only door[1..100]

pri doors | i,j

  repeat i from 1 to 100
    repeat j from i to 100 step i
      not door[j]

  ser.str(string("Open doors: "))

  repeat i from 1 to 100
    if door[i]
      ser.dec(i)
      ser.tx(32)

  ser.str(string(13,10))
```

**Output:**

```
Open doors: 1 4 9 16 25 36 49 64 81 100 
```


## SQL

**optimized**

```mw
DECLARE	@sqr int,
		@i int,
		@door int;
		
SELECT @sqr =1,
	@i = 3,
	@door = 1;	
				
WHILE(@door <=100)
BEGIN
	IF(@door = @sqr)
	BEGIN
		PRINT 'Door ' + RTRIM(CAST(@door as char)) + ' is open.';
		SET @sqr= @sqr+@i;
		SET @i=@i+2;
	END
	ELSE
	BEGIN
		PRINT 'Door ' + RTRIM(CONVERT(char,@door)) + ' is closed.';
	END
SET @door = @door + 1
END
```

**A postgres version, in one request**

principle: the number of passes per door is counted, if this is odd, the door is open.

```mw
with numbers as (
    select generate_series(1, 100) as n
),
passes as (
    select passes.n pass, doors.n door 
    from numbers doors
    cross join numbers passes 
    where doors.n % passes.n = 0  -- modulo
),
counting as (
    select door, count(pass) pass_number 
    from passes
    group by door
) 
select door from counting
where pass_number % 2 = 1
order by door
```

**A Oracle version, in one request**

```mw
with numbers as (
    select rownum as n from dual connect by level <= 100
),
passes as (
    select doors.n door, count(passes.n) pass_number
    from numbers doors
    cross join numbers passes 
    where MOD(doors.n, passes.n) = 0  -- modulo
    group by doors.n
)
select door from passes
where MOD(pass_number, 2) = 1
order by door
```

**Output:**

```
door|
----+
   1|
   4|
   9|
   ...
```


## SQL PL

Works with

:

Db2 LUW

With SQL only:

```mw
--#SET TERMINATOR @

SET SERVEROUTPUT ON @

BEGIN
 DECLARE TYPE DOORS_ARRAY AS BOOLEAN ARRAY [100];
 DECLARE DOORS DOORS_ARRAY;
 DECLARE I SMALLINT;
 DECLARE J SMALLINT;
 DECLARE STATUS CHAR(10);
 DECLARE SIZE SMALLINT DEFAULT 100;

 -- Initializes the array, with all spaces (doors) as false (closed).
 SET I = 1;
 WHILE (I <= SIZE) DO
  SET DOORS[I] = FALSE;
  SET I = I + 1;
 END WHILE;

 -- Processes the doors.
 SET I = 1;
 WHILE (I <= SIZE) DO
  SET J = 1;
  WHILE (J <= SIZE) DO
   IF (MOD(J, I) = 0) THEN
    IF (DOORS[J] = TRUE) THEN
     SET DOORS[J] = FALSE;
    ELSE
     SET DOORS[J] = TRUE;
    END IF;
   END IF;
   SET J = J + 1;
  END WHILE;
  SET I = I + 1;
 END WHILE;

 -- Prints the final status o the doors.
 SET I = 1;
 WHILE (I <= SIZE) DO
  SET STATUS = (CASE WHEN (DOORS[I] = TRUE) THEN 'OPEN' ELSE 'CLOSED' END);
  CALL DBMS_OUTPUT.PUT_LINE('Door ' || I || ' is '|| STATUS);
  SET I = I + 1;
 END WHILE;
END @
```

Output:

```
db2 -td@
db2 => BEGIN
...
db2 (cont.) => END @
DB20000I  The SQL command completed successfully.

Door 1 is OPEN      
Door 2 is CLOSED    
Door 3 is CLOSED    
Door 4 is OPEN      
Door 5 is CLOSED    
Door 6 is CLOSED    
Door 7 is CLOSED    
Door 8 is CLOSED    
Door 9 is OPEN      
Door 10 is CLOSED    
Door 11 is CLOSED    
Door 12 is CLOSED    
Door 13 is CLOSED    
Door 14 is CLOSED    
Door 15 is CLOSED    
Door 16 is OPEN      
Door 17 is CLOSED    
Door 18 is CLOSED    
Door 19 is CLOSED    
Door 20 is CLOSED    
Door 21 is CLOSED    
Door 22 is CLOSED    
Door 23 is CLOSED    
Door 24 is CLOSED    
Door 25 is OPEN      
Door 26 is CLOSED    
Door 27 is CLOSED    
Door 28 is CLOSED    
Door 29 is CLOSED    
Door 30 is CLOSED    
Door 31 is CLOSED    
Door 32 is CLOSED    
Door 33 is CLOSED    
Door 34 is CLOSED    
Door 35 is CLOSED    
Door 36 is OPEN      
Door 37 is CLOSED    
Door 38 is CLOSED    
Door 39 is CLOSED    
Door 40 is CLOSED    
Door 41 is CLOSED    
Door 42 is CLOSED    
Door 43 is CLOSED    
Door 44 is CLOSED    
Door 45 is CLOSED    
Door 46 is CLOSED    
Door 47 is CLOSED    
Door 48 is CLOSED    
Door 49 is OPEN      
Door 50 is CLOSED    
Door 51 is CLOSED    
Door 52 is CLOSED    
Door 53 is CLOSED    
Door 54 is CLOSED    
Door 55 is CLOSED    
Door 56 is CLOSED    
Door 57 is CLOSED    
Door 58 is CLOSED    
Door 59 is CLOSED    
Door 60 is CLOSED    
Door 61 is CLOSED    
Door 62 is CLOSED    
Door 63 is CLOSED    
Door 64 is OPEN      
Door 65 is CLOSED    
Door 66 is CLOSED    
Door 67 is CLOSED    
Door 68 is CLOSED    
Door 69 is CLOSED    
Door 70 is CLOSED    
Door 71 is CLOSED    
Door 72 is CLOSED    
Door 73 is CLOSED    
Door 74 is CLOSED    
Door 75 is CLOSED    
Door 76 is CLOSED    
Door 77 is CLOSED    
Door 78 is CLOSED    
Door 79 is CLOSED    
Door 80 is CLOSED    
Door 81 is OPEN      
Door 82 is CLOSED    
Door 83 is CLOSED    
Door 84 is CLOSED    
Door 85 is CLOSED    
Door 86 is CLOSED    
Door 87 is CLOSED    
Door 88 is CLOSED    
Door 89 is CLOSED    
Door 90 is CLOSED    
Door 91 is CLOSED    
Door 92 is CLOSED    
Door 93 is CLOSED    
Door 94 is CLOSED    
Door 95 is CLOSED    
Door 96 is CLOSED    
Door 97 is CLOSED    
Door 98 is CLOSED    
Door 99 is CLOSED    
Door 100 is OPEN      
```


## Standard ML

```mw
datatype Door = Closed | Opened

fun toggle Closed = Opened
  | toggle Opened = Closed

fun pass (step, doors) = List.map (fn (index, door) => if (index mod step) = 0
						       then (index, toggle door)
						       else (index, door))
				  doors

(* [1..n] *)
fun runs n = List.tabulate (n, fn k => k+1)

fun run n =
    let
	val initialdoors = List.tabulate (n, fn i => (i+1, Closed))
	val counter = runs n
    in
	foldl pass initialdoors counter
    end

fun opened_doors n = List.mapPartial (fn (index, Closed) => NONE
				       | (index, Opened) => SOME (index))
				     (run n)
```

**Output:**

```
- opened_doors 100;
val it = [1,4,9,16,25,36,49,64,81,100] : int list
```


## Stata

```mw
clear
set obs 100
gen doors=0
gen index=_n
forvalues i=1/100 {
	quietly replace doors=!doors if mod(_n,`i')==0
}
list index if doors, noobs noheader

  +-------+
  |     1 |
  |     4 |
  |     9 |
  |    16 |
  |    25 |
  |-------|
  |    36 |
  |    49 |
  |    64 |
  |    81 |
  |   100 |
  +-------+
```


## Stax

```
0]100* 1Yd
AJ{100R{y%m:0{!}&y^Yd}*
|u
```

**Output:**

```
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```


## Stringle

```mw
d "."
#d
i d
#i
p "door" #i
*p *p "."
i d f "oc"
i d #@f #*p
i d .\f "o" $ #i
i i d
#i +101 i ""
#i
d d "."
#d +101 d ""
#d
```

**Output:**

```
1
4
9
16
25
36
49
64
81
100
```


## SuperCollider

```mw
(
var n = 100, doors = false ! n;
var pass = { |j| (0, j .. n-1).do { |i| doors[i] = doors[i].not } };
(1..n-1).do(pass);
doors.selectIndices { |open| open }; // all are closed except [ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ]
)
```


## Swift

**unoptimized**

```mw
/* declare enum to identify the state of a door */
enum DoorState : String {
    case Opened = "Opened"
    case Closed = "Closed"
}

/* declare list of doors state and initialize them */
var doorsStateList = [DoorState](count: 100, repeatedValue: DoorState.Closed)

/* do the 100 passes */
for i in 1...100 {
    /* map on a strideTo instance to only visit the needed doors on each iteration */
    map(stride(from: i - 1, to: 100, by: i)) {
        doorsStateList[$0] = doorsStateList[$0] == .Opened ? .Closed : .Opened
    }
}

/* print the results */
for (index, item) in enumerate(doorsStateList) {
    println("Door \(index+1) is \(item.rawValue)")
}
```

**optimized**

```mw
/* declare enum to identify the state of a door */
enum DoorState : String {
    case Opened = "Opened"
    case Closed = "Closed"
}

/* declare list of doors state and initialize them */
var doorsStateList = [DoorState](count: 100, repeatedValue: DoorState.Closed)

/* set i^2 doors to opened */
var i = 1
do {
    doorsStateList[(i*i)-1] = DoorState.Opened
    ++i
} while (i*i) <= doorsStateList.count

/* print the results */
for (index, item) in enumerate(doorsStateList) {
    println("Door \(index+1) is \(item.rawValue)")
}
```

### One-liner

```mw
var arr: [Bool] = Array(1...100).map{ remquo(exp(log(Float($0))/2.0),1).0 == 0 }
```


## Tailspin

```mw
source hundredDoors
  @: [ 1..100 -> 0 ];
  templates toggle
    def jump: $;
    $jump..100:$jump -> \(
      when <?($@hundredDoors($) <=0>)> do @hundredDoors($): 1;
      otherwise @hundredDoors($): 0;
    \) -> !VOID
  end toggle
  1..100 -> toggle -> !VOID
  $@ -> \[i](<=1> ' $i;' !\) !
end hundredDoors

$hundredDoors -> 'Open doors:$...;' -> !OUT::write
```

In v0.5

```mw
hundredDoors source
  @ set [ 1..100 -> 0 ];
  toggle templates
    jump is $;
    $jump..100:$jump -> templates
      when <|?($@hundredDoors($) matches <|=0>)> do @hundredDoors($) set 1;
      otherwise @hundredDoors($) set 0;
    end -> !VOID
  end toggle
  1..100 -> toggle -> !VOID
  $@(.. as i; -> if <|=1> -> ' $i;') !
end hundredDoors

$hundredDoors -> 'Open doors:$...;' !
```

**Output:**

```
Open doors: 1 4 9 16 25 36 49 64 81 100
```


## Tcl

**procedures**

```mw
#!/usr/bin/env  tclsh

# 100 doors

proc seq { m n } {
    set r {}
    for {set i $m} {$i <= $n} {incr i} {
	    lappend r $i
    }    
    return $r
}

proc toggle {val a b} {
    # expr has ternary operators 
    return  [expr {
		        ${val} == ${a}? ${b} :
		        ${val} == ${b}? ${a} :      
		        [error "bad value: ${val}"]
	        }]
}

proc multiples {n max} {
    set ret {}
    set x $n

    # maximum multiple
    set mid  [expr $max / 2]
    
    if {$x>=$mid  &&  $x<$max} { return $x }

    # calculate multiples
    if {[expr $x <= $mid]} {
	    for {set i 1} {$i <= $max } {incr i} {

	        set x [expr $i * $n]

   	        if {$x > $max} { break }
	    
	        lappend ret $x
	    }
    }

    return $ret
}

# states
array set state {
    open    "open"
    closed  "closed"
    unknown "?"
}

# ==============================
# start program

# 100 doors
variable MAX  100

variable mid  [expr int($MAX / 2)]

variable Seq_100  [seq 1 $MAX]

# initialize doors closed
foreach n $Seq_100 {
    set door($n) $state(closed)
}

# do for 1 .. 100
foreach m $Seq_100 {
    
    set mults [multiples $m $MAX]
    
    foreach d $mults {
	    set door($d) [toggle $door($d) $state(open) $state(closed)]
    }
}

# output
foreach n $Seq_100 {
    if { $door($n) eq $state(open) } {
	    puts stdout "$n: $door($n)"
    }
}

# end
```

**Output:**

1: open

4: open

9: open

16: open

25: open

36: open

49: open

64: open

81: open

100: open

**unoptimized**

```mw
package require Tcl 8.5
set n 100
set doors [concat - [lrepeat $n 0]]
for {set step 1} {$step <= $n} {incr step} {
    for {set i $step} {$i <= $n} {incr i $step} {
        lset doors $i [expr { ! [lindex $doors $i]}]
    }
}
for {set i 1} {$i <= $n} {incr i} {
    puts [format "door %d is %s" $i [expr {[lindex $doors $i] ? "open" : "closed"}]]
}
```

**optimized**

```mw
package require Tcl 8.5
set doors [lrepeat [expr {$n + 1}] closed]
for {set i 1} {$i <= sqrt($n)} {incr i} {
    lset doors [expr {$i ** 2}] open
}
for {set i 1} {$i <= $n} {incr i} {
    puts [format "door %d is %s" $i [lindex $doors $i]]
}
```

**graphical**

Library:

Tk

Inspired by the E solution, here's a visual representation

```mw
package require Tcl 8.5
package require Tk

array set door_status {}

# create the gui
set doors [list x]
for {set i 0} {$i < 10} {incr i} {
    for {set j 0} {$j < 10} {incr j} {
        set k [expr {1 + $j + 10*$i}]
        lappend doors [radiobutton .d_$k -text $k -variable door_status($k) \
                         -indicatoron no -offrelief flat -width 3 -value open]
        grid [lindex $doors $k] -column $j -row $i
    }
}

# create the controls
button .start -command go -text Start
label .i_label -text " door:"
entry .i -textvariable i -width 4
label .step_label -text " step:"
entry .step -textvariable step -width 4
grid .start - .i_label - .i - .step_label - .step - -row $i
grid configure .start -sticky ew
grid configure .i_label .step_label -sticky e
grid configure .i .step -sticky w

proc go {} {
    global doors door_status i step

    # initialize the door_status (all closed)
    for {set d 1} {$d <= 100} {incr d} {
        set door_status($d) closed
    }
    
    # now, begin opening and closing
    for {set step 1} {$step <= 100} {incr step} {
        for {set i 1} {$i <= 100} {incr i} {
            if {$i % $step == 0} {
                [lindex $doors $i] [expr {$door_status($i) eq "open" ? "deselect" : "select"}]
                update
                after 50
            }
        }
    }
}
```


## TI-83 BASIC

### Naive

```
seq(0,X,1,100
For(X,1,100
0 or Ans-not(fPart(cumSum(1 or Ans)/A
End
Pause Ans
```

A-1cumsum(1 or Ans should be able to replace cumsum(1 or Ans)/A (saving a byte because of the unnecessary closing parenthesis) but it falls victim to a rounding error that causes X^(-1)*X to be stored as 0.99999999999999... (although it's still displayed as the original X). When the fPart( [fractional part] command evaluates this, it returns .999999999, which not( turns to 0 (meaning a closed door). Regular division, as shown, isn't prone to this.

### Optimized

```
Pause not(fPart(√(seq(X,X,1,100
```


## TI-89 BASIC

```mw
Define doors(fast) = Func
  Local doors,i,j
  seq(false,x,1,100) ? doors
  If fast Then
    For i,1,10,1
      true ? doors[i^2]
    EndFor
  Else
    For i,1,100,1
      For j,i,100,i
        not doors[j] ? doors[j]
      EndFor
    EndFor
  EndIf
  Return doors
EndFunc
```


## TorqueScript

```mw
for(%steps = 1; %a <= 100; %a++)
	for(%current = %steps; %current <= 100; %current += %steps)
		%door[%current] = !%door[%current];
for(%a = 1; %a <= 100; %a++)
	echo("Door #" @ %a @ " is" SPC %door[%current] ? "Open" : "Closed" @ ".");
```


## Transact-SQL

```mw
WITH    OneToTen (N)
AS  (   SELECT  N
        FROM (  VALUES (0), (1), (2), (3), (4), (5), (6), (7), (8), (9)
                ) V(N)
        )
    ,   InitDoors (Num, IsOpen)
AS  (   SELECT  1
            +   1 * Units.N
            +   10 * Tens.N As Num
            ,   Convert(Bit, 0) As IsOpen
        FROM    OneToTen As Units
        CROSS JOIN  OneToTen As Tens
        ) -- This part could be easier with a tally table or equivalent table-valued function
    ,   States (NbStep, Num, IsOpen)
AS  (   SELECT  0 As NbStep
            ,   Num
            ,   IsOpen
        FROM    InitDoors As InitState
        UNION ALL
        SELECT  1 + NbStep
            ,   Num
            ,   CASE Num % (1 + NbStep)
                    WHEN 0 THEN ~IsOpen
                    ELSE IsOpen
                END
        FROM    States
        WHERE   NbStep < 100
        )
SELECT  Num As DoorNumber
    ,   Concat( 'Door number ', Num, ' is '
            ,   CASE IsOpen
                    WHEN 1 THEN ' open'
                    ELSE ' closed'
                END ) As Result -- Concat needs SQL Server 2012
FROM    States
WHERE   NbStep = 100
ORDER By Num
; -- Fortunately, maximum recursion is 100 in SQL Server.
-- For more doors, the MAXRECURSION hint should be used.
-- More doors would also need an InitDoors with more rows.
```

### School example

Works with

:

Transact-SQL

version SQL Server 2017

```mw
SET NOCOUNT ON;

-- Doors can be open or closed.
DECLARE @open CHAR(1) = 'O';
DECLARE @closed CHAR(1) = 'C';

-- There are 100 doors in a row that are all initially closed.
DECLARE @doorsCount INT = 100;
DECLARE @doors TABLE (doorKey INT PRIMARY KEY, doorState CHAR(1));
WITH sample100 AS (
    SELECT TOP(100) object_id
    FROM sys.objects
)
INSERT @doors
  SELECT ROW_NUMBER() OVER (ORDER BY A.object_id) AS doorKey,
    @closed AS doorState
  FROM sample100 AS A
      CROSS JOIN sample100 AS B
      CROSS JOIN sample100 AS C
      CROSS JOIN sample100 AS D
  ORDER BY 1
  OFFSET 0 ROWS
  FETCH NEXT @doorsCount ROWS ONLY;

-- You make 100 passes by the doors, visiting every door and toggle the door (if
-- the door is closed, open it; if it is open, close it), according to the rules
-- of the task.
DECLARE @pass INT = 1;
WHILE @pass <= @doorsCount BEGIN
  UPDATE @doors
  SET doorState = CASE doorState WHEN @open THEN @closed ELSE @open END
  WHERE doorKey >= @pass
    AND doorKey % @pass = 0;

  SET @pass = @pass + 1;
END;

-- Answer the question: what state are the doors in after the last pass?
-- The answer as the query result is:
SELECT doorKey, doorState FROM @doors;
-- The answer as the console output is:
DECLARE @log VARCHAR(max);
DECLARE @doorKey INT = (SELECT MIN(doorKey) FROM @doors);
WHILE @doorKey <= @doorsCount BEGIN
  SET @log = (
      SELECT TOP(1) CONCAT('Doors ', doorKey, ' are ',
        CASE doorState WHEN @open THEN ' open' ELSE 'closed' END, '.')
      FROM @doors
      WHERE doorKey = @doorKey
    );
  RAISERROR (@log, 0, 1) WITH NOWAIT;

  SET @doorKey = (SELECT MIN(doorKey) FROM @doors WHERE doorKey > @doorKey);
END;

-- Which are open, which are closed?
-- The answer as the query result is:
SELECT doorKey, doorState FROM @doors WHERE doorState = @open;
SELECT doorKey, doorState FROM @doors WHERE doorState = @closed;
-- The answer as the console output is:
SET @log = (
  SELECT CONCAT('These are open doors: ',
    STRING_AGG(CAST(doorKey AS VARCHAR(max)), ', '), '.')
  FROM @doors
  WHERE doorState = @open
);
RAISERROR (@log, 0, 1) WITH NOWAIT;
SET @log = (
  SELECT CONCAT('These are closed doors: ',
    STRING_AGG(CAST(doorKey AS VARCHAR(max)), ', '), '.')
  FROM @doors
  WHERE doorState = @closed
);
RAISERROR (@log, 0, 1) WITH NOWAIT;

-- Assert:
DECLARE @expected TABLE (doorKey INT PRIMARY KEY);
SET @doorKey = 1;
WHILE @doorKey * @doorKey <= @doorsCount BEGIN
  INSERT @expected VALUES (@doorKey * @doorKey);
  SET @doorKey = @doorKey + 1;
END;
IF NOT EXISTS (
    SELECT doorKey FROM @doors WHERE doorState = @open
    EXCEPT
    SELECT doorKey FROM @expected
  )
  AND NOT EXISTS (
    SELECT doorKey FROM @expected
    EXCEPT
    SELECT doorKey FROM @doors WHERE doorState = @open
  )
  PRINT 'The task is solved.';
ELSE
  THROW 50000, 'These aren''t the doors you''re looking for.', 1;
```


## Transd

```mw
#lang transd

MainModule: {
    doors: Vector<Bool>(100),
    _start: (λ 
        (for i in Seq(100) do
            (for k in Seq(i 100 (+ i 1)) do
                (set-el doors k (not (get doors k)))
        ))

        (for i in Seq(100) do
            (if (get doors i) (textout (+ i 1) " "))
    ))
}
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```


## True BASIC

```mw
! Optimized solution with True BASIC

OPTION NOLET
x = 1 
y = 3 
z = 0
PRINT STR$(x) & " Open"
DO UNTIL z >= 100
z = x + y
PRINT STR$(z) & " Open"
x = z 
y = y + 2
LOOP

END
```


## TSE SAL

```mw
// library: math: get: task: door: open: close100 <description></description> <version control></version control> <version>1.0.0.0.11</version> <version control></version control> (filenamemacro=getmaocl.s) [<Program>] [<Research>] [kn, ri, mo, 31-12-2012 22:03:16]
PROC PROCMathGetTaskDoorOpenClose( INTEGER doorMaxI, INTEGER passMaxI )
 // e.g. PROC Main()
 // e.g.  PROCMathGetTaskDoorOpenClose( 100, 100 )
 // e.g. END
 // e.g.
 // e.g. <F12> Main()
 //
 // ===
 //
 // The output will be:
 //
 // door 1 is open
 // door 4 is open
 // door 9 is open
 // door 16 is open
 // door 25 is open
 // door 36 is open
 // door 49 is open
 // door 64 is open
 // door 81 is open
 // door 100 is open
 // all other doors are closed
 //
 // ===
 //
 INTEGER passMinI = 1
 INTEGER passI = 0
 //
 INTEGER doorminI = 1
 INTEGER doorI = 0
 //
 STRING s[255] = ""
 //
 INTEGER bufferI = 0
 //
 PushPosition()
 bufferI = CreateTempBuffer()
 PopPosition()
 //
 FOR doorI = doorMinI TO doorMaxI
  //
  SetGlobalInt( Format( "doorsI", doorI ), 0 )
  //
 ENDFOR
 //
 FOR passI = passMinI TO passMaxI
  //
  doorI = passI - passI
  //
  REPEAT
   //
   doorI = doorI + passI
   //
   SetGlobalInt( Format( "doorsI", doorI ), NOT( GetGlobalInt( Format( "doorsI", doorI ) ) ) )
   //
  UNTIL ( doorI >= doorMaxI )
  //
 ENDFOR
 //
 FOR doorI = doorMinI TO doorMaxI
  //
  IF ( GetGlobalInt( Format( "doorsI", doorI ) ) > 0 )
   //
   s = "open"
   //
   AddLine( Format( "door", " ", doorI, " ", "is", " ", s ), bufferI )
   //
  ELSE
   //
   s = "closed"
   //
  ENDIF
  //
 ENDFOR
 //
 AddLine( "all other doors are closed", bufferI )
 //
 GotoBufferId( bufferI )
 //
END

PROC Main()
 PROCMathGetTaskDoorOpenClose( 100, 100 )
END
```


## TUSCRIPT

```mw
$$ MODE TUSCRIPT
DICT doors create
COMPILE
LOOP door=1,100
 LOOP pass=1,100
 SET go=MOD (door,pass)
 DICT doors lookup door,num,cnt,status
   IF (num==0) THEN
     SET status="open"
     DICT doors add  door,num,cnt,status
   ELSE
    IF (go==0) THEN
       IF (status=="closed") THEN
         SET status="open"
       ELSE
         SET status="closed"
       ENDIF
     DICT doors update door,num,cnt,status
     ENDIF
   ENDIF
 ENDLOOP
ENDLOOP
ENDCOMPILE
DICT doors unload door,num,cnt,status
```

Output (variable status):

```
 status       = *
           1 = open
           2 = closed
           3 = closed
           4 = open
           5 = closed
           6 = closed
           7 = closed
           8 = closed
           9 = open
          10 = closed
          11 = closed
          12 = closed
          13 = closed
          14 = closed
          15 = closed
          16 = open
          17 = closed
          18 = closed
          19 = closed
          20 = closed
          21 = closed
          22 = closed
          23 = closed
          24 = closed
          25 = open
          26 = closed
          27 = closed
          28 = closed
          29 = closed
          30 = closed
          31 = closed
          32 = closed
          33 = closed
          34 = closed
          35 = closed
          36 = open
          37 = closed
          38 = closed
          39 = closed
          40 = closed
          41 = closed
          42 = closed
          43 = closed
          44 = closed
          45 = closed
          46 = closed
          47 = closed
          48 = closed
          49 = open
          50 = closed
          51 = closed
          52 = closed
          53 = closed
          54 = closed
          55 = closed
          56 = closed
          57 = closed
          58 = closed
          59 = closed
          60 = closed
          61 = closed
          62 = closed
          63 = closed
          64 = open
          65 = closed
          66 = closed
          67 = closed
          68 = closed
          69 = closed
          70 = closed
          71 = closed
          72 = closed
          73 = closed
          74 = closed
          75 = closed
          76 = closed
          77 = closed
          78 = closed
          79 = closed
          80 = closed
          81 = open
          82 = closed
          83 = closed
          84 = closed
          85 = closed
          86 = closed
          87 = closed
          88 = closed
          89 = closed
          90 = closed
          91 = closed
          92 = closed
          93 = closed
          94 = closed
          95 = closed
          96 = closed
          97 = closed
          98 = closed
          99 = closed
         100 = open
```


## TypeScript

```mw
interface Door {
  id: number;
  open: boolean;
}

function doors(): Door[] {
  var Doors: Door[] = [];

  for (let i = 1; i <= 100; i++) {
    Doors.push({id: i, open: false});
  }

  for (let secuence of Doors) {
    for (let door of Doors) {
      if (door.id % secuence.id == 0) {
        door.open = !door.open;
      }
    }
  }

  return Doors.filter(a => a.open);
}
```


## TXR

```mw
(defun hyaku-mai-tobira ()
  (let ((doors (vector 100)))
    (each ((i (range 0 99)))
      (each ((j (range i 99 (+ i 1))))
        (flip [doors j])))
    doors))

(each ((counter (range 1))
       (door (hyaku-mai-tobira)))
  (put-line `door @counter is @(if door "open" "closed")`))
```


## uBasic/4tH

Translation of

:

BBC BASIC

Deliberately unoptimized.

```mw
FOR p = 1 TO 100
  FOR d = p TO 100 STEP p
    @(d) = @(d) = 0
  NEXT d
NEXT p

FOR d= 1 TO 100
  IF @(d) PRINT "Door ";d;" is open"
NEXT d
```


## Uiua

```mw
◿2/+=0⊞◿.+1⇡100
         +1⇡100 # 1-100
      ⊞◿.       # Mod each with 1-100
    =0          # Find where mod = 0, aka the divisors
  /+            # Sum to get num of divisors
◿2              # Num divisors is odd
```

**Output:**

```
[1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1]
```

Version #2 (Display of door numbers)

```mw
⊜∘/≠±⊞◿..+1⇡100
```

**Output:**

```
╭─     
╷   1  
    4  
    9  
   16  
   25  
   36  
   49  
   64  
   81  
  100  
      ╯
```

Optimised version

```mw
×.+1⇡⌊√ 100
```

**Output:**

```
[1 4 9 16 25 36 49 64 81 100]
```


## Uniface

**unoptimized**

Works with

:

Uniface 9.6

```mw
entry LP_DO_IT

    variables
        string  V_DOORS
        boolean V_DOOR_STATE
        string  V_DOOR_STATE_S
        numeric V_IDX
        numeric V_TOTAL_DOORS
        string  V_DOOR_STATE_LIST
        numeric V_LOOP_COUNT
    endvariables

    V_TOTAL_DOORS = 100
    putitem V_DOORS, V_TOTAL_DOORS, 0

    V_DOORS = $replace (V_DOORS, 1, "·;", "·;0", -1)

    putitem/id V_DOOR_STATE_LIST, "1", "Open"
    putitem/id V_DOOR_STATE_LIST, "0", "Close"

    V_LOOP_COUNT = 1
    while (V_LOOP_COUNT <= V_TOTAL_DOORS)
        V_IDX = 0
        V_IDX = V_IDX + V_LOOP_COUNT

        getitem V_DOOR_STATE, V_DOORS, V_IDX
        while (V_IDX <= V_TOTAL_DOORS)

            V_DOOR_STATE = !V_DOOR_STATE
            getitem/id V_DOOR_STATE_S, V_DOOR_STATE_LIST, $number(V_DOOR_STATE)
            putitem V_DOORS, V_IDX, V_DOOR_STATE

            V_IDX = V_IDX + V_LOOP_COUNT
            getitem V_DOOR_STATE, V_DOORS, V_IDX
        endwhile

        V_LOOP_COUNT = V_LOOP_COUNT + 1

    endwhile

    V_IDX = 1
    getitem V_DOOR_STATE, V_DOORS, V_IDX
    while (V_IDX <= V_TOTAL_DOORS)
        getitem/id V_DOOR_STATE_S, V_DOOR_STATE_LIST, $number(V_DOOR_STATE)
        if (V_DOOR_STATE)
            putmess "Door %%V_IDX%%% is finally %%V_DOOR_STATE_S%%%"
        endif

        V_IDX = V_IDX + 1
        getitem V_DOOR_STATE, V_DOORS, V_IDX
    endwhile

end ; LP_DO_IT
```

**Output:**

```
Door 1 is finally Open
Door 4 is finally Open
Door 9 is finally Open
Door 16 is finally Open
Door 25 is finally Open
Door 36 is finally Open
Door 49 is finally Open
Door 64 is finally Open
Door 81 is finally Open
Door 100 is finally Open
```


## Unison

```mw
hundredDoors : [Boolean]
hundredDoors =
  toggleEachNth : Nat -> [Boolean] -> [Boolean]
  toggleEachNth n doors =
    go counter = cases
      [] -> []
      (d +: ds) -> if counter == n
        then (not d) +: go 1 ds
        else d +: go (counter+1) ds

    go 1 doors

  foldr toggleEachNth (replicate 100 'false) (range 1 101)

results = filterMap (cases (open, ix) -> if open then Some (ix+1) else None)
                    (indexed hundredDoors)
```


## UNIX Shell

Works with

:

Bourne Again SHell

```mw
#! /bin/bash

declare -a doors
for((i=1; i <= 100; i++)); do
    doors[$i]=0
done

for((i=1; i <= 100; i++)); do
    for((j=i; j <= 100; j += i)); do
	echo $i $j
	doors[$j]=$(( doors[j] ^ 1 ))
    done
done

for((i=1; i <= 100; i++)); do
    if [[ ${doors[$i]} -eq 0 ]]; then
	op="closed"
    else
	op="open"
    fi
    echo $i $op
done
```

Optimised version

```mw
#!/bin/bash

for i in {1..100}; do
  door[$i*$i]=1
  [ -z ${door[$i]} ] && echo "$i closed" || echo "$i open"
done
```


## Ursa

```mw
#
# 100 doors
#

decl int i j
decl boolean<> doors

# append 101 boolean values to doors stream
for (set i 0) (or (< i 100) (= i 100)) (inc i)
        append false doors
end for

# loop through, opening and closing doors
for (set i 1) (or (< i 100) (= i 100)) (inc i)
        for (set j i) (or (< j 100) (= j 100)) (inc j)
                if (= (mod j i) 0)
                        set doors<j> (not doors<j>)
                end if
        end for
end for

# loop through and output which doors are open
for (set i 1) (or (< i 100) (= i 100)) (inc i)
        out "Door " i ": " console
        if doors<i>
                out "open" endl console
        else
                out "closed" endl console
        end if
end if
```


## Ursala

The doors are represented as a list of 100 booleans initialized to false. The pass function takes a number and a door list to a door list with doors toggled at indices that are multiples of the number. The main program folds the pass function (to the right) over the list of pass numbers from 100 down to 1, numbers the result, and filters out the numbers of the open doors.

```mw
#import std
#import nat

doors = 0!* iota 100

pass("n","d") = remainder\"n"?l(~&r,not ~&r)* num "d"

#cast %nL

main = ~&rFlS num pass=>doors nrange(100,1)
```

optimized version:

```mw
#import nat

#cast %nL

main = product*tiiXS iota10
```

output:

```
<1,4,9,16,25,36,49,64,81>
```


## UTFool

```mw
···
http://rosettacode.org/wiki/100_doors
···
■ HundredDoors 
  § static
    ▶ main
    • args⦂ String[]
      open⦂   boolean: true
      closed⦂ boolean: false
      doors⦂  boolean[1+100] · all initially closed
      🔁 pass from 1 to 100
         ∀ visited ∈ pass‥100 by pass
         · toggle the visited doors
           if the doors[visited] are closed
              let the doors[visited] be open
           else
              let the doors[visited] be closed
      for each door #n in doors⦂ boolean
        if the door is open
           System.out.println "Door #⸨n⸩ is open."
```


## Vala

**Unoptimized**

```mw
int main() {
	bool doors_open[101];
	for(int i = 1; i < doors_open.length; i++) {
		for(int j = 1; i*j < doors_open.length; j++) {
			doors_open[i*j] = !doors_open[i*j];
		}
		stdout.printf("%d: %s\n", i, (doors_open[i] ? "open" : "closed"));
	}
	return 0;
}
```

Output:

```
1: open
2: closed
3: closed
4: open
5: closed
6: closed
7: closed
8: closed
9: open
10: closed
11: closed
...
```

**Optimized**

```mw
int main() {
	int i = 1;
	while(i*i <= 100) {
		stdout.printf("${i*i} open\n");
		i++;
	}
	return 0;
}
```

Output:

```
1 open
4 open
9 open
16 open
25 open
36 open
49 open
64 open
81 open
100 open
```


## VAX Assembly

```mw
                           00000064  0000     1 n = 100
                               0000  0000     2 .entry	doors, ^m<>
                         26'AF   9F  0002     3 	pushab	b^arr				; offset signed byte
                    50   64 8F   9A  0005     4 	movzbl	#n, r0
                            50   DD  0009     5 	pushl	r0				; (sp) -> .ascid arr
                                     000B     6 10$:
                       51   50   D0  000B     7 	movl	r0, r1				; step = start index
                                     000E     8 20$:
                  25'AF41   01   8C  000E     9 	xorb2	#^a"0" \^a"1", b^arr-1[r1]	; \ xor toggle "1"<->"0"
             FFF5 51   50   6E   F1  0013    10 	acbl	(sp), r0, r1, 20$		; limit, step, index
                         EF 50   F5  0019    11 	sobgtr	r0, 10$				; n..1
                                     001C    12 
                            5E   DD  001C    13 	pushl	sp				; descriptor by reference
              00000000'GF   01   FB  001E    14 	calls	#1, g^lib$put_output		; show result
                                 04  0025    15 	ret
                                     0026    16 
30'30'30'30'30'30'30'30'30'30'30'30' 0026    17 arr:	.byte	^a"0"[n]
30'30'30'30'30'30'30'30'30'30'30'30' 0032       
30'30'30'30'30'30'30'30'30'30'30'30' 003E       
30'30'30'30'30'30'30'30'30'30'30'30' 004A       
30'30'30'30'30'30'30'30'30'30'30'30' 0056       
30'30'30'30'30'30'30'30'30'30'30'30' 0062       
30'30'30'30'30'30'30'30'30'30'30'30' 006E       
30'30'30'30'30'30'30'30'30'30'30'30' 007A       
                        30'30'30'30' 0086       
                                     008A    18 .end	doors
$ run doors
1001000010000001000000001000000000010000000000001000000000000001000000000000000010000000000000000001
```
