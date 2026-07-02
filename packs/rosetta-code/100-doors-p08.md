---
title: "100 doors (part 8/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 8/10
---

## Polyglot:PL/I and PL/M

Works with

:

8080 PL/M Compiler

... under CP/M (or an emulator)

Should work with many PL/I implementations. The PL/I include file "pg.inc" can be found on the Polyglot:PL/I and PL/M page. Note the use of text in column 81 onwards to hide the PL/I specifics from the PL/M compiler.

```mw
/* FIND THE FIRST FEW SQUARES VIA THE UNOPTIMISED DOOR FLIPPING METHOD */
doors_100H: procedure options                                                   (main);

/* PROGRAM-SPECIFIC %REPLACE STATEMENTS MUST APPEAR BEFORE THE %INCLUDE AS */
/* E.G. THE CP/M PL/I COMPILER DOESN'T LIKE THEM TO FOLLOW PROCEDURES      */
   /* PL/I                                                                      */
      %replace dcldoors by         100;
   /* PL/M */                                                                   /*
      DECLARE  DCLDOORS LITERALLY '101';
   /* */

/* PL/I DEFINITIONS                                                             */
%include 'pg.inc';
/* PL/M DEFINITIONS: CP/M BDOS SYSTEM CALL AND CONSOLE I/O ROUTINES, ETC. */    /*
   DECLARE BINARY LITERALLY 'ADDRESS', CHARACTER LITERALLY 'BYTE';
   DECLARE FIXED  LITERALLY ' ',       BIT       LITERALLY 'BYTE';
   DECLARE STATIC LITERALLY ' ',       RETURNS   LITERALLY ' ';
   DECLARE FALSE  LITERALLY '0',       TRUE LITERALLY '1';
   DECLARE HBOUND LITERALLY 'LAST',    SADDR  LITERALLY '.';
   BDOSF: PROCEDURE( FN, ARG )BYTE;
                               DECLARE FN BYTE, ARG ADDRESS; GOTO 5;   END; 
   BDOS: PROCEDURE( FN, ARG ); DECLARE FN BYTE, ARG ADDRESS; GOTO 5;   END;
   PRCHAR:   PROCEDURE( C );   DECLARE C BYTE;      CALL BDOS( 2, C ); END;
   PRSTRING: PROCEDURE( S );   DECLARE S ADDRESS;   CALL BDOS( 9, S ); END;
   PRNL:     PROCEDURE;        CALL PRCHAR( 0DH ); CALL PRCHAR( 0AH ); END;
   PRNUMBER: PROCEDURE( N );
      DECLARE N ADDRESS;
      DECLARE V ADDRESS, N$STR( 6 ) BYTE, W BYTE;
      N$STR( W := LAST( N$STR ) ) = '$';
      N$STR( W := W - 1 ) = '0' + ( ( V := N ) MOD 10 );
      DO WHILE( ( V := V / 10 ) > 0 );
         N$STR( W := W - 1 ) = '0' + ( V MOD 10 );
      END; 
      CALL BDOS( 9, .N$STR( W ) );
   END PRNUMBER;
   MODF:     PROCEDURE( A, B )ADDRESS;
      DECLARE ( A, B ) ADDRESS;
      RETURN A MOD B;
   END MODF;
/* END LANGUAGE DEFINITIONS */

   /* TASK */

   /* ARRAY OF DOORS - DOOR( I ) IS TRUE IF OPEN, FALSE IF CLOSED */
   DECLARE DOOR( DCLDOORS )  BIT;
   DECLARE ( I, J, MAXDOOR ) FIXED BINARY;

   MAXDOOR = HBOUND( DOOR                                                       ,1
                   );

   /* SET ALL DOORS TO CLOSED */
   DO I = 0 TO MAXDOOR; DOOR( I ) = FALSE; END;
   /* REPEATEDLY FLIP THE DOORS */
   DO I = 1 TO MAXDOOR;
      DO J = I TO MAXDOOR BY I;
         DOOR( J ) = NOT( DOOR( J ) );
      END;
   END;
   /* DISPLAY THE RESULTS */
   DO I = 1 TO MAXDOOR;
      IF DOOR( I ) THEN DO;
         CALL PRCHAR( ' ' );
         CALL PRNUMBER( I );
      END;
   END;
   CALL PRNL;

EOF: end doors_100H;
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```


## Pony

**Combined Optimized and Unoptimized**

Probably also rather pointless in its use of actors, but, after all, they're cheap.

```mw
actor Toggler
    let doors:Array[Bool]
    let env: Env
    new create(count:USize,_env:Env) =>
        var i:USize=0
        doors=Array[Bool](count)
        env=_env
        while doors.size() < count do
            doors.push(false)
        end
    be togglin(interval : USize)=>
        var i:USize=0
        try
            while i < doors.size() do
                doors.update(i,not doors(i)?)?
                i=i+interval
            end
        else
            env.out.print("Errored while togglin'!")
        end
    be printn(onlyOpen:Bool)=>
        try
            for i in doors.keys() do
                if onlyOpen and not doors(i)? then
                    continue
                end
                env.out.print("Door " + i.string() + " is " +
                    if doors(i)? then
                        "Open"
                    else
                        "closed"
                    end)
            end
        else
            env.out.print("Error!")
        end
        true

actor OptimizedToggler
    let doors:Array[Bool]
    let env:Env
    new create(count:USize,_env:Env)=>
        env=_env
        doors=Array[Bool](count)
        while doors.size()<count do
            doors.push(false)
        end
    be togglin()=>
        var i:USize=0
        if alreadydone then
            return
        end
        try
            doors.update(0,true)?
            doors.update(1,true)?
            while i < doors.size() do
                i=i+1
                let z=i*i
                let x=z*z
                if z > doors.size() then
                    break
                else
                    doors.update(z,true)?
                end
                if x < doors.size() then
                    doors.update(x,true)?
                end
            end
        end
    be printn(onlyOpen:Bool)=>
        try
            for i in doors.keys() do
                if onlyOpen and not doors(i)? then
                    continue
                end
                env.out.print("Door " + i.string() + " is " +
                    if doors(i)? then
                        "Open"
                    else
                        "closed"
                    end)
            end
        else
            env.out.print("Error!")
        end
        true
actor Main
    new create(env:Env)=>
        var count: USize =100
        try
            let index=env.args.find("-n",0,0,{(l,r)=>l==r})?
            try
            match env.args(index+1)?.read_int[USize]()?
                | (let x:USize, _)=>count=x
                end
            else
                env.out.print("You either neglected to provide an argument after -n or that argument was not an integer greater than zero.")
                return
            end
        end
        if env.args.contains("optimized",{(l,r)=>r==l}) then
            let toggler=OptimizedToggler(count,env)
            var i:USize = 1
            toggler.togglin()
            toggler.printn(env.args.contains("onlyopen", {(l,r)=>l==r}))
        else
            let toggler=Toggler(count,env)
            var i:USize = 1
            while i < count do
                toggler.togglin(i)
                i=i+1
            end
            toggler.printn(env.args.contains("onlyopen", {(l,r)=>l==r}))
        end
```


## Pop11

**unoptimized**

```mw
lvars i;
lvars doors = {% for i from 1 to 100 do false endfor %};
for i from 1 to 100 do
   for j from i by i to 100 do
      not(doors(j)) -> doors(j);
   endfor;
endfor;
;;; Print state
for i from 1 to 100 do
   printf('Door ' >< i >< ' is ' ><
            if doors(i) then 'open' else 'closed' endif, '%s\n');
endfor;
```

**optimized**

```mw
for i to 100 do
    lvars root = sqrt(i);
    i; if root = round(root) then ' open' ><; else ' closed' ><; endif; =>
endfor;
```


## PostScript

Bruteforce:

```mw
/doors [ 100 { false } repeat ] def

1 1 100 { dup 1 sub exch 99 {
        dup doors exch get not doors 3 1 roll put
} for } for
doors pstack
```

Shows:

```mw
[true false false true false false false false true false ...<90 doors later>... true]
```


## Potion

```mw
square=1, i=3
1 to 100(door):
  if (door == square):
    ("door", door, "is open") say
    square += i
    i += 2.
.
```


## PowerShell

### unoptimized

```mw
$doors = @(0..99)
for($i=0; $i -lt 100; $i++) {
  $doors[$i] = 0  # start with all doors closed
}
for($i=0; $i -lt 100; $i++) {
  $step = $i + 1
  for($j=$i; $j -lt 100; $j = $j + $step) {
    $doors[$j] = $doors[$j] -bxor 1
  }
}
foreach($doornum in 1..100) {
  if($doors[($doornum-1)] -eq $true) {"$doornum open"}
  else {"$doornum closed"}
}
```

### Alternative Method

```mw
function Get-DoorState($NumberOfDoors)
{
   begin 
   {
      $Doors = @()
      $Multiple = 1
   }

   process
   {
      for ($i = 1; $i -le $NumberOfDoors; $i++)
      {
         $Door = [pscustomobject]@{
                    Name = $i
                    Open = $false
                 }

         $Doors += $Door   
      }

      While ($Multiple -le $NumberOfDoors)
      {
	 Foreach ($Door in $Doors)
	 {
	    if ($Door.name % $Multiple -eq 0)
               {
	          If ($Door.open -eq $False){$Door.open = $True}
	          Else {$Door.open = $False}
	       }
	 }
			
         $Multiple++
      }
    }

    end {$Doors}
}
```

### unoptimized Pipeline

```mw
$doors = 1..100 | ForEach-Object {0}
1..100 | ForEach-Object { $a=$_;1..100 | Where-Object { -not ( $_ % $a )  } | ForEach-Object { $doors[$_-1] = $doors[$_-1] -bxor 1 }; if ( $doors[$a-1] ) { "door opened" } else { "door closed" } }
```

### unoptimized Pipeline 2

```mw
$doors = 1..100 | ForEach-Object {0}
$visited = 1..100
1..100 | ForEach-Object { $a=$_;$visited[0..([math]::floor(100/$a)-1)] | Where-Object { -not ( $_ % $a )  } | ForEach-Object { $doors[$_-1] = $doors[$_-1] -bxor 1;$visited[$_/$a-1]+=($_/$a) }; if ( $doors[$a-1] ) { "door opened" } else { "door closed" } }
```

### unoptimized Pipeline 3 (dynamically build pipeline)

```mw
1..100|foreach-object {$pipe += "toggle $_ |"} -begin {$pipe=""}
filter toggle($pass) {$_.door = $_.door -xor !($_.index % $pass);$_}
invoke-expression "1..100| foreach-object {@{index=`$_;door=`$false}} | $pipe  out-host"
```

### Using Powershell Workflow for Parallelism

```mw
Workflow Calc-Doors {
    Foreach –parallel ($number in 1..100) {
        "Door " + $number.ToString("0000") + ": " + @{$true="Closed";$false="Open"}[([Math]::pow($number, 0.5)%1) -ne 0]
    }
}
Calc-Doors | sort
```

### optimized

```mw
1..10|%{"Door "+ $_*$_ + " is open"}
```


## Processing

**Unoptimized:**

```mw
boolean[] doors = new boolean[100];

void setup() {
  for (int i = 0; i < 100; i++) {
    doors[i] = false;
  }
  for (int i = 1; i < 100; i++) {
    for (int j = 0; j < 100; j += i) {
      doors[j] = !doors[j];
    }
  }
  println("Open:");
  for (int i = 1; i < 100; i++) {
    if (doors[i]) {
      println(i);
    }
  }
  exit();
}
```

**Output:**

```
Open:
1
4
9
16
25
36
49
64
81
```

### Processing.R

**Unoptimized:**

```mw
setup <- function() {
  for(door in doors(100, 100)) {
    stdout$print(paste(door, ""))
  }
}

doors <- function(ndoors=100,passes=100) {
  doors <- rep(FALSE,ndoors)
  for (ii in seq(1,passes)) {
      mask <- seq(0,ndoors,ii)
      doors[mask] <- !doors[mask]  
  }
  return (which(doors == TRUE))
}
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```


## ProDOS

Uses math module.

```mw
enableextensions 
enabledelayedexpansion
editvar /newvar /value=0 /title=closed
editvar /newvar /value=1 /title=open
editvar /newvar /range=1-100 /increment=1 /from=2
editvar /newvar /value=2 /title=next
:doors
for /alloccurrences (!next!-!102!) do editvar /modify /value=-open-
editvar /modify /value=-next-=+1
if -next- /hasvalue=100 goto :cont else goto :doors
:cont
printline !1!-!102!
stoptask
```


## Prolog

### unoptimized

Declarative:

```mw
main :-
    forall(between(1,100,Door), ignore(display(Door))).

% show output if door is open after the 100th pass
display(Door) :-
    status(Door, 100, open),
    format("Door ~d is open~n", [Door]).

% true if Door has Status after Pass is done
status(Door, Pass, Status) :-
    Pass > 0,
    Remainder is Door mod Pass,
    toggle(Remainder, OldStatus, Status),
    OldPass is Pass - 1,
    status(Door, OldPass, OldStatus).
status(_Door, 0, closed).

toggle(Remainder, Status, Status) :-
    Remainder > 0.
toggle(0, open, closed).
toggle(0, closed, open).
```

Doors as a list:

```mw
doors_unoptimized(N) :-
	length(L, N),
	maplist(init, L),
	doors(N, N, L, L1),
	affiche(N, L1).

init(close).

doors(Max, 1, L, L1) :-
	!,
       inverse(1, 1, Max, L, L1).

doors(Max, N, L, L1) :-
	N1 is N - 1,
	doors(Max, N1, L, L2),
	inverse(N, 1, Max, L2, L1).

inverse(N, Max, Max, [V], [V1]) :-
	!,
	0 =:= Max mod N -> inverse(V, V1); V1 = V.

inverse(N, M, Max, [V|T], [V1|T1]) :-
	M1 is M+1,
	inverse(N, M1, Max, T, T1),
	(   0 =:= M mod N -> inverse(V, V1); V1 = V).

inverse(open, close).
inverse(close, open).

affiche(N, L) :-
	forall(between(1, N, I),
	       (   nth1(I, L, open) -> format('Door ~w is open.~n', [I]); true)).
```

Using dynamic-rules. Tried to be ISO:

```mw
doors(Num, Passes) :-
    forall(( everyNth(1,Passes,1,Pass)
           , forall((everyNth(Pass,Num,Pass,Door), toggle(Door)))
           ))
  , show(Num)
  .

toggle(Door) :-
    Opened = opened(Door)
  , ( clause(Opened,_) -> retract(Opened)
                        ; asserta(Opened)
    ).

show(Num) :-
    forall(( between(1,Num,Door)
           , (opened(Door) -> State = opened ; State = closed)
           , write(Door), write(' '), write(State), nl
           )).

% utils
forall(X) :- findall(_, X, _).

everyNth(From,To,Step,X) :-
    From =< To
  , ( X = From ; From1 is From + Step, everyNth(From1,To,Step,X) )
  .

main :- doors(100,100), halt.
```

### optimized

```mw
doors_optimized(N) :-
	Max is floor(sqrt(N)),
	forall(between(1, Max, I),
	       (   J is I*I,format('Door ~w is open.~n',[J]))).
```


## PROMAL

```mw
;;; find the first few squares via the unoptimised door flipping method
PROGRAM hundredDoors
INCLUDE LIBRARY
CON INT doorMax = 100
BYTE door [ doorMax + 1 ] ; door( i ) is true if open, false if closed
WORD i
BYTE j
BEGIN
FOR i = 0 TO doorMax            ; set all doors to closed
  door[ i ] = false
FOR i = 1 TO doorMax            ; repeatedly flip the doors
  j = i:<
  WHILE j <= doorMax
    door[ j ] = not door[ j ]
    j = j + i:<
FOR i = 1 TO doorMax            ; display the results
  IF door[ i ]
    OUTPUT " #W", i
OUTPUT "#C"
END
```


## Pure

```mw
using system;

// initialize doors as pairs: number, status where 0 means open
let doors = zip (1..100) (repeat 1);

toogle (x,y) = x,~y;

toogleEvery n d = map (tooglep n) d with
                    tooglep n d@((x,_)) = toogle d if ~(x mod n);
                                        = d otherwise; end;

// show description of given doors
status (n,x) = (str n) + (case x of
                            1 = " close";
                            0 = " open"; end);

let result = foldl (\a n -> toogleEvery n a) doors (1..100);

// pretty print the result (only open doors)
showResult = do (puts.status) final when
               final = filter open result with
                         open (_,x) = ~x;
                       end; end;
```

**Output:**

```
 
> showResult;
1 open
4 open
9 open
16 open
25 open
...
```


## Pure Data

```mw
100Doors.pd

#N canvas 241 375 414 447 10;
#X obj 63 256 expr doors[$f1] = doors[$f1] ^ 1;
#X msg 83 118 \; doors const 0;
#X msg 44 66 bang;
#X obj 44 92 t b b b;
#X obj 43 28 table doors 101;
#X obj 44 360 sel 0;
#X obj 44 336 expr if (doors[$f1] == 1 \, $f1 \, 0);
#X obj 63 204 t b f f;
#X text 81 66 run;
#X obj 71 384 print -n;
#X text 132 310 print results (open doors);
#X obj 63 179 loop 1 100 1;
#X obj 63 231 loop 1 100 1;
#X obj 44 310 loop 1 100 1;
#X text 148 28 create array;
#X text 151 180 100 passes;
#X text 179 123 set values to 0;
#X connect 2 0 3 0;
#X connect 3 0 13 0;
#X connect 3 1 11 0;
#X connect 3 2 1 0;
#X connect 5 1 9 0;
#X connect 6 0 5 0;
#X connect 7 0 12 0;
#X connect 7 1 12 1;
#X connect 7 2 12 3;
#X connect 11 0 7 0;
#X connect 12 0 0 0;
#X connect 13 0 6 0;

loop.pd

#N canvas 656 375 427 447 10;
#X obj 62 179 until;
#X obj 102 200 f;
#X obj 62 89 inlet;
#X obj 303 158 f \$3;
#X obj 270 339 outlet;
#X obj 223 89 inlet;
#X obj 138 89 inlet;
#X obj 324 89 inlet;
#X obj 117 158 f \$1;
#X text 323 68 step;
#X obj 202 158 f \$2;
#X obj 62 118 t b b b b;
#X obj 270 315 spigot;
#X obj 89 314 sel 0;
#X obj 137 206 +;
#X obj 102 237 expr $f1 \; if ($f3 > 0 \, if ($f1 > $f2 \, 0 \, 1)
\, if ($f3 < 0 \, if ($f1 < $f2 \, 0 \, 1) \, 0)), f 34;
#X text 63 68 run;
#X text 136 68 start;
#X text 227 68 end;
#X text 58 31 loop (abstraction);
#X connect 0 0 1 0;
#X connect 1 0 14 0;
#X connect 1 0 15 0;
#X connect 2 0 11 0;
#X connect 3 0 14 1;
#X connect 3 0 15 2;
#X connect 5 0 10 1;
#X connect 6 0 8 1;
#X connect 7 0 3 1;
#X connect 8 0 1 1;
#X connect 10 0 15 1;
#X connect 11 0 0 0;
#X connect 11 1 8 0;
#X connect 11 2 10 0;
#X connect 11 3 3 0;
#X connect 12 0 4 0;
#X connect 13 0 0 1;
#X connect 14 0 1 1;
#X connect 15 0 12 0;
#X connect 15 1 12 1;
#X connect 15 1 13 0;
```


## PureBasic

**unoptimized**

```mw
Dim doors.i(100)
 
For x = 1 To 100
  y = x
  While y <= 100
    doors(y) = 1 - doors(y)
    y + x
  Wend
Next
 
OpenConsole()
PrintN("Following Doors are open:")
For x = 1 To 100
  If doors(x)
    Print(Str(x) + ", ")
  EndIf
Next
Input()
```

**optimized**

```mw
OpenConsole()
PrintN("Following Doors are open:")
For i = 1 To 100
    root.f = Sqr(i)
    If root = Int(root)
    	Print (Str(i) + ", ")
    EndIf
Next     
Input()
```

Output:

```
Following Doors are open:
1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
```


## Pyret

````mw
data Door:
  | open
  | closed
end
 
fun flip-door(d :: Door) -> Door:
  cases(Door) d:
    | open => closed
    | closed => open
  end
end
 

fun flip-doors(doors :: List<Door>) -> List<Door>:
  doc:```Given a list of door positions, repeatedly switch the positions of
      every nth door for every nth pass, and return the final list of door
      positions```
  for fold(flipped-doors from doors, n from range(1, doors.length() + 1)):
    for map_n(m from 1, d from flipped-doors):
      if num-modulo(m, n) == 0:
        flip-door(d)
      else:
        d
      end
    end
  end
where:
    flip-doors([list: closed, closed, closed]) is
  [list: open, closed, closed]

  flip-doors([list: closed, closed, closed, closed]) is
  [list: open, closed, closed, open]

  flip-doors([list: closed, closed, closed, closed, closed, closed]) is
  [list: open, closed, closed, open, closed, closed]

  closed-100 = for map(_ from range(1, 101)): closed end
  answer-100 = for map(n from range(1, 101)):
    if num-is-integer(num-sqrt(n)): open
    else: closed
    end
  end

  flip-doors(closed-100) is answer-100
end

fun find-indices<A>(pred :: (A -> Boolean), xs :: List<A>) -> List<Number>:
    doc:```Given a list and a predicate function, produce a list of index
      positions where there's a match on the predicate```
  ps = map_n(lam(n,e): if pred(e): n else: -1 end end, 1, xs)
  ps.filter(lam(x): x >= 0 end)
where:
  find-indices((lam(i): i == true end), [list: true,false,true]) is [list:1,3]
end

fun run(n):
  doc:```Given a list of doors that are closed, make repeated passes 
      over the list, switching the positions of every nth door for 
      each nth pass. Return a list of positions in the list where the
      door is Open.```
  doors = repeat(n, closed)
  ys = flip-doors(doors)
  find-indices((lam(y): y == open end), ys)
where:
  run(4) is [list: 1,4]
end
 
run(100)
````


## Python

Works with

:

Python

version 2.5-2.7

**unoptimized**

```mw
doors = [False] * 100
for i in range(100):
   for j in range(i, 100, i+1):
       doors[j] = not doors[j]
   print("Door %d:" % (i+1), 'open' if doors[i] else 'close')
```

**optimized**

A version that only visits each door once:

```mw
for i in xrange(1, 101):
    root = i ** 0.5
    print "Door %d:" % i, 'open' if root == int(root) else 'close'
```

One liner using a list comprehension, item lookup, and is_integer

```mw
print '\n'.join(['Door %s is %s' % (i, ('closed', 'open')[(i**0.5).is_integer()]) for i in xrange(1, 101)])
```

One liner using a generator expression, ternary operator, and modulo

```mw
print '\n'.join('Door %s is %s' % (i, 'closed' if i**0.5 % 1 else 'open') for i in range(1, 101))
```

Works with

:

Python

version 3.12+

```mw
for i in range(1, 101):
    print(f"Door {i}:{"closed" if i**0.5 % 1 else "open"}")
```

**ultra-optimized**: ported from Julia version

```mw
for i in range(1,11): print(f"Door {i**2} is open")
```


## Q

The classic solution uses 100 booleans, one for each door. Qubits are more expensive so I rearrange the algorith to use only 1.

```mw
import Std.Math.*;
operation HundredDoors () : Int[] {
  use q = Qubit();
  mutable doors = [];
  for n in 1..100 {
    for g in 1..n{
      let (_,r)=DivRemI(n,g);
      if (r==0) {X(q)};
    }
    if (M(q)==One) {doors+=[n];}
    Reset(q);
  }
  return doors;
}
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## Q

**unoptimized**

```mw
`closed`open(100#0b){@[x;where y;not]}/100#'(til[100]#'0b),'1b
```

Binary function `{@[x;where y;not]}` is applied using Over. The initial state is `100#0b` and the right argument is a list of 100 boolean masks. The boolean vector result is used to index the pair of states.

Following expressions simply flag perfect squares.

**optimized**

```mw
`closed`open (1+til 100) in {x*x} 1+til 10
```

**alternative**

```mw
@[100#`closed; -1+{x*x}1+til 10; :; `open]
```


## QB64

```mw
Const Opened = -1, Closed = 0
Dim Doors(1 To 100) As Integer, Passes As Integer, Index As Integer
Rem Normal implementation
Print "100doors Normal method"
For Passes = 1 To 100 Step 1
    Doors(Passes) = Closed
Next Passes
For Passes = 1 To 100 Step 1
    For Index = 0 To 100 Step Passes
        If Index > 100 Then Exit For
        If Index > 0 Then If Doors(Index) = Opened Then Doors(Index) = Closed Else Doors(Index) = Opened
    Next Index
Next Passes
Print "OPEN DOORS after 100th passes"
For Passes = 1 To 100 Step 1
    If Doors(Passes) = Opened Then Print Passes; " ";
Next

Rem Alternative solution of perfect squares

Print "Alternative method"
Passes = 0
For Passes = 1 To 100 Step 1
    Doors(Passes) = Closed
Next Passes
For Passes = 1 To 100 Step 1
    If Sqr(Passes) = Int(Sqr(Passes)) Then Doors(Passes) = Opened
Next
Print "Opened doors found by SQR method"
For Passes = 1 To 100 Step 1
    If Doors(Passes) = Opened Then Print Passes; " ";
Next Passes
End
```


## Quackery

**unoptimized**

```mw
  [ bit ^ ]                       is toggle      ( f n --> f )
   
  [ 0
    100 times
      [ i^ 1+ swap
        101 times
          [ i^ toggle over step ]
      nip ] ]                     is toggledoors (     --> f )
   
   [ 100 times
       [ 1 >> dup 1 &
         if [ i^ 1+ echo sp ] ]
         drop ]                   is echodoors   (   f -->   )
  
  toggledoors
  say " These doors are open: " echodoors cr
  say " The rest are closed." cr
```

**Output:**

```
 These doors are open: 1 4 9 16 25 36 49 64 81 100 
 The rest are closed.
```

**optimized**

```mw
  10 times [ i^ 1+ 2 ** echo sp ]
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```


## R

**Using a loop**

```mw
doors_puzzle <- function(ndoors, passes = ndoors) {
    doors <- logical(ndoors)
    for (ii in seq(passes)) {
        mask <- seq(ii, ndoors, ii)
        doors[mask] <- !doors[mask]	
    }
    which(doors)
}

doors_puzzle(100)
```

**optimized**

```mw
x <- rep(1, 100)
for (i in 1:100-1) {
    x <- xor(x, rep(c(rep(0,i),1), length.out=100))
}
which(!x)
```

**Using a **ply function**

```mw
doors_puzzle <- function(ndoors=100,passes=100) {
names(which(table(unlist(sapply(1:passes, function(X) seq(0, ndoors, by=X)))) %% 2 == 1))
}

doors_puzzle()
```

### Using Reduce

```mw
H=100
f=rep(F,H)
which(Reduce(function(d,n) xor(replace(f,seq(n,H,n),T),d), 1:H, f))
```

**Output:**

```
1   4   9  16  25  36  49  64  81 100
```


## Racket

```mw
#lang racket

;; Applies fun to every step-th element of seq, leaving the others unchanged.
(define (map-step fun step seq)
  (for/list ([elt seq] [i (in-naturals)])
    ((if (zero? (modulo i step)) fun values) elt)))

(define (toggle-nth n seq)
  (map-step not n seq))

(define (solve seq)
  (for/fold ([result seq]) ([_ seq] [pass (in-naturals 1)])
    (toggle-nth pass result)))

(for ([door (solve (make-vector 101 #f))] [index (in-naturals)]
      #:when (and door (> index 0)))
  (printf "~a is open~%" index))
```

Optimized:

```mw
#lang racket
(for ([x (in-range 1 101)] #:when (exact-integer? (sqrt x)))
  (printf "~a is open\n" x))
```

Unoptimized imperative, with graphic rendering:

```mw
#lang slideshow
(define-syntax-rule (vector-neg! vec pos)
  (vector-set! vec pos (not (vector-ref vec pos))))

(define (make-doors)
  (define doors (make-vector 100 #f))
  (for* ([i 100] [j (in-range i 100 (add1 i))]) (vector-neg! doors j))
  doors)

(displayln (list->string (for/list ([d (make-doors)]) (if d #\o #\-))))

(define closed-door (inset (filled-rectangle 4 20) 2))
(define open-door (inset (rectangle 4 20) 2))

(for/fold ([doors (rectangle 0 0)]) ([open? (make-doors)])
  (hc-append doors (if open? open-door closed-door)))
```

Output:


## Raku

(formerly Perl 6)

### unoptimized

Works with

:

Rakudo

version 2015.09"

```mw
my @doors = False xx 101;
 
(.=not for @doors[0, $_ ... 100]) for 1..100;
 
say "Door $_ is ", <closed open>[ @doors[$_] ] for 1..100;
```

### optimized

```mw
say "Door $_ is open" for map {$^n ** 2}, 1..10;
```

### probably the most compact idiom

```mw
say 'Door $_ is open' for (1..10)»²;
```

### Here's a version using the cross meta-operator instead of a map:

```mw
 say "Door $_ is open" for 1..10 X** 2;
```

This one prints both opened and closed doors:

```mw
say "Door $_ is ", <closed open>[.sqrt == .sqrt.floor] for 1..100;
```

### verbose version, but uses ordinary components

Works with

:

Rakudo

version 2016.07 Tom Legrady

```mw
sub  output( @arr, $max ) {
    my $output = 1;
    for 1..^$max -> $index {
	if @arr[$index] {
	    printf "%4d", $index;
	    say '' if $output++ %%  10;
	}
    }
    say '';
}

sub MAIN ( Int :$doors = 100 ) {
    my $doorcount = $doors + 1;
    my @door[$doorcount] = 0 xx ($doorcount);
    
    INDEX:
    for 1...^$doorcount -> $index {
        # flip door $index & its multiples, up to last door.
        #
	for ($index, * + $index ... *)[^$doors] -> $multiple {
	    next INDEX if $multiple > $doors;
	    @door[$multiple] =  @door[$multiple] ?? 0 !! 1;
	}
    }
    output @door, $doors+1;
}
```

**Output:**

```
$ ./100_doors.pl6 -doors=100
   1   4   9  16  25  36  49  64  81
```


## RapidQ

```mw
dim x as integer, y as integer
dim door(1 to 100) as byte

'initialize array
for x = 1 to 100 : door(x) = 0 : next

'set door values
for y = 1 to 100
    for x = y to 100 step y
        door(x) = not door(x)
    next x
next y

'print result
for x = 1 to 100
    if door(x) then print "Door " + str$(x) + " = open"
next 

while inkey$="":wend
end
```

**Output**

```
Door 1 = open
Door 4 = open
Door 9 = open
Door 16 = open
Door 25 = open
Door 36 = open
Door 49 = open
Door 64 = open
Door 81 = open
Door 100 = open
```


## Rebol

### Unoptimized

```mw
doors: array/initial 100 'closed
repeat i 100 [
    door: at doors i
    forskip door i [change door either 'open = first door ['closed] ['open]]
]
```

Using bitset in Rebol 3

```mw
;; Create a bitset with capacity for 100 bits (representing 100 doors)
;; Each bit represents a door state: 0 = closed, 1 = open
doors: make bitset! 100

;; Outer loop: Make 100 passes (i = 1 to 100)
repeat i 100 [
    ;; Inner loop: Check each door position (j = 1 to 100)
    repeat j 100 [
        ;; If door j index is divisible by pass number i (no remainder)
        if zero? remainder j i [
            ;; Toggle the door's bit:
            ;; doors/:j accesses door j in the bitset
            ;; 'not' flips the bit value (0 -> 1, 1 -> 0)
            doors/:j: not doors/:j
        ]
    ]
]

;; Final loop: Check which doors are open, print their numbers
repeat i 100 [
    ;; If door i's bit is set (open)
    if doors/:i [
        ;; Print the door's number and that it is open
        print ["door" i "is open"]
    ]
]
```

### Optimized

Mathematical Approach

```mw
;; Loop variable i from 1 to 10 (since 10^2 = 100, covers doors 1 to 100)
repeat i 10 [
    ;; Print that door number (i squared) is open
    ;; These are exactly the doors with perfect square numbers: 1, 4, 9, ..., 100
    print ["door" (i * i) "is open"]
]
```

**Output:**

```
door 1 is open
door 4 is open
door 9 is open
door 16 is open
door 25 is open
door 36 is open
door 49 is open
door 64 is open
door 81 is open
door 100 is open
```


## Red

### Unoptimized

```mw
Red [
  Purpose: "100 Doors Problem (Perfect Squares)"
  Author: "Barry Arthur"
  Date: "07-Oct-2016"
]
doors: make vector! [char! 8 100]
repeat i 100 [change at doors i #"."]

repeat i 100 [
    j: i
    while [j <= 100] [
      door: at doors j
      change door either #"O" = first door [#"."] [#"O"]
      j: j + i
    ]
]

repeat i 10 [
  print copy/part at doors (i - 1 * 10 + 1) 10
]
```

### Using bitset! type

```mw
Red ["Doors"]

doors: make bitset! len: 100
repeat step len [
	repeat n to-integer len / step [
		m: step * n 
		doors/:m: not doors/:m
	]
]
repeat n len [if doors/:n [print n]]
```


## Refal

```mw
$ENTRY Go {
    = <Show 1 <Walk 1 <Doors>>>;
};

NDoors { = 100; };
Doors  { = <Repeat <NDoors> Closed>; };

Repeat {
    0   s.val = ;
    s.N s.val = s.val <Repeat <- s.N 1> s.val> ;
};    

Toggle {
    1   Closed e.rest = Open   e.rest;
    1   Open   e.rest = Closed e.rest;
    s.N s.door e.rest = s.door <Toggle <- s.N 1> e.rest>;
};
    
Pass {
    s.pass s.door e.doors, <Compare s.door <NDoors>>: '+'
        = e.doors;
    s.pass s.door e.doors
        = <Pass s.pass <+ s.pass s.door> <Toggle s.door e.doors>>;
};

Walk {
    s.pass e.doors, <Compare s.pass <NDoors>>: '+' 
        = e.doors;
    s.pass e.doors
        = <Walk <+ s.pass 1> <Pass s.pass s.pass e.doors>>;
};

Show {
    s.N Open   e.rest = <Prout Door s.N is open> 
                        <Show <+ s.N 1> e.rest>;
    s.N Closed e.rest = <Show <+ s.N 1> e.rest>;
    s.N = ;
};
```

**Output:**

```
Door 1 is open
Door 4 is open
Door 9 is open
Door 16 is open
Door 25 is open
Door 36 is open
Door 49 is open
Door 64 is open
Door 81 is open
Door 100 is open
```


## Relation

```mw
relation door, state
set i = 1
while i <= 100
insert i, 1
set i = i+1
end while
set i = 2
while i <= 100
update state = 1-state where not (door mod i)
set i = i+1
end while
update state = "open" where state
update state = "closed" where state !== "open"
print
```

| door | state |
|---|---|
| 1 | open |
| 2 | closed |
| 3 | closed |
| 4 | open |
| 5 | closed |
| 6 | closed |
| 7 | closed |
| 8 | closed |
| 9 | open... |


## Retro

```mw
:doors (n-) [ #1 repeat dup-pair n:square gt? 0; drop dup n:square n:put sp n:inc again ] do drop-pair ;
#100 doors
```


## REXX

### the idiomatic way

```mw
/*REXX pgm solves the  100 doors puzzle, doing it the hard way by opening/closing doors.*/
parse arg doors .                                /*obtain the optional argument from CL.*/
if doors=='' | doors==","  then doors=100        /*not specified?  Then assume 100 doors*/
                                                 /*        0 =  the door is  closed.    */
                                                 /*        1 =   "    "   "  open.      */
door.=0                                          /*assume all doors are closed at start.*/
                do #=1  for doors                /*process a pass─through for all doors.*/
                    do j=#  by #  to doors       /*  ··· every Jth door from this point.*/
                    door.j= \door.j              /*toggle the  "openness"  of the door. */
                    end   /*j*/
                end       /*#*/

say 'After '                doors          " passes, the following doors are open:"
say
                do k=1  for doors
                if door.k  then say right(k, 20) /*add some indentation for the output. */
                end    /*k*/                     /*stick a fork in it,  we're all done. */
```

**output   when using the default input:**

```
After  100  passes, the following doors are open:

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

### the shortcut way

```mw
/*REXX pgm solves the  100 doors  puzzle,  doing it the easy way by calculating squares.*/
parse arg doors .                                /*obtain the optional argument from CL.*/
if doors=='' | doors==","  then doors=100        /*not specified?  Then assume 100 doors*/
say 'After '          doors          " passes, the following doors are open:"
say
          do #=1  while  #**2 <= doors           /*process easy pass─through  (squares).*/
          say right(#**2, 20)                    /*add some indentation for the output. */
          end   /*#*/                            /*stick a fork in it,  we're all done. */
```

**output   is identical to the 1st REXX version.**


## Ring

**Unoptimized**

```mw
doors = list(100)
for i = 1 to 100
doors[i] = false
next

For pass = 1 To 100
         For door = pass To 100
             if doors[door] doors[door] = false else doors[door] = true ok
         door += pass-1
         Next
Next

For door = 1 To 100
     see "Door (" + door + ") is "
     If doors[door] see "Open" else see "Closed" ok
     see nl
Next
```

**Optimized**

```mw
doors = list(100)
for i = 1 to 100
doors[i] = false
next

For p = 1 To 10
        doors[pow(p,2)] = True
Next

For door = 1 To 100
     see "Door (" + door + ") is "
     If doors[door] see "Open" else see "Closed" ok
     see nl
Next
```


## Rocq

Basic solution:

```mw
Require Import List.

Fixpoint rep {A} (a : A) n :=
  match n with
    | O => nil
    | S n' => a::(rep a n')
  end.

Fixpoint flip (l : list bool) (n k : nat) : list bool :=
  match l with
    | nil => nil
    | cons h t => match k with
                | O => (negb h) :: (flip t n n)
                | S k' => h :: (flip t n k')
              end
  end.

Definition flipeach l n := flip l n n.

Fixpoint flipwhile l n :=
  match n with
    | O => flipeach l 0
    | S n' => flipwhile (flipeach l (S n')) n'
  end.

Definition prison cells := flipwhile (rep false cells) cells.
```

Optimized version ((n+1)^2 = n^2 + 2n + 1):

```mw
Require Import List.

Fixpoint prisoo' nd n k accu :=
  match nd with
    | O => rev accu
    | S nd' => let ra := match k with
                 | O => (true, S n, (n + n))
                 | S k' => (false, n, k')
               end in
               prisoo' nd' (snd (fst ra)) (snd ra) ((fst (fst ra))::accu)
  end.

Definition prisoo cells := prisoo' cells 1 0 nil.
```

Unit test:

```mw
Goal prison 100 = prisoo 100. compute. reflexivity. Qed.
```

Full proof at github:

```mw
Goal forall n, prison n = prisoo n. Abort.
```


## RPL

Translation of

:

Python

Works with

:

Halcyon Calc

version 4.2.7

| RPL code | Comment |
|---|---|
| ≪ { } { 100 } 0 CON 1 100 **FOR** ii ii 100 **FOR** j DUP j GET NOT j SWAP PUT ii **STEP** **IF** DUP ii GET **THEN** SWAP ii + SWAP **END** **NEXT** DROP ≫ '**DOORS'** STO | **DOORS** *( -- { open_doors } )* doors = [False] * 100 for i in range(100): for j in range(i, 100, i+1): doors[j] = not doors[j] if doors[i} then print(i) // clean stack |

**Output:**

```
1: { 1 4 9 16 25 36 49 64 81 100 }
```

### Optimized

```
≪ { } 1 100 FOR ii IF ii √ FP NOT THEN ii + END NEXT ≫
```

Run time on standard HP-28S:

- unoptimized: 45 seconds
- optimized: 3 seconds


## Ruby

```mw
doors = Array.new(101,0)
print "Open doors "
(1..100).step(){ |i|
(i..100).step(i) { |d|
    doors[d] = doors[d]^= 1
    if i == d and doors[d] == 1 then
      print "#{i} "
    end
  }
}
```

Output:

```
Open doors 1 4 9 16 25 36 49 64 81 100
```

**unoptimized; Ruby-way**

```mw
class Door
  attr_reader :state

  def initialize
    @state = :closed
  end
  
  def close
    @state = :closed
  end

  def open
    @state = :open
  end
  
  def closed?
    @state == :closed
  end
  
  def open?
    @state == :open
  end
  
  def toggle
    if closed? then open else close end
  end
  
  def to_s
    @state.to_s
  end
end

doors = Array.new(100) { Door.new }
1.upto(100) do |multiplier|
  doors.each_with_index do |door, i|
    door.toggle if (i + 1) % multiplier == 0
  end
end

doors.each_with_index { |door, i| puts "Door #{i+1} is #{door}." }
```

**unoptimized**

```mw
n = 100
Open = "open"
Closed = "closed"
def Open.toggle
  Closed
end
def Closed.toggle
  Open
end
doors = [Closed] * (n + 1)
for mul in 1..n
  for x in (mul..n).step(mul)
    doors[x] = doors[x].toggle
  end
end
doors.each_with_index do |b, i|
  puts "Door #{i} is #{b}" if i > 0
end
```

**optimized**

```mw
n = 100
(1..n).each do |i| 
  puts "Door #{i} is #{i**0.5 == (i**0.5).round ? "open" : "closed"}"
end
```

**generic true/false, with another way of handling the inner loop demonstrating Range#step**

```mw
doors = [false] * 100
100.times do |i|
  (i ... doors.length).step(i + 1) do |j|
    doors[j] = !doors[j]
  end
end
puts doors.map.with_index(1){|d,i| "Door #{i} is #{d ? 'open' : 'closed'}."}
```

**Output:**

```
Door 1 is open
Door 2 is closed
Door 3 is closed
Door 4 is open
Door 5 is closed
Door 6 is closed
Door 7 is closed
Door 8 is closed
Door 9 is open
Door 10 is closed
Door 11 is closed
Door 12 is closed
Door 13 is closed
Door 14 is closed
Door 15 is closed
Door 16 is open
Door 17 is closed
Door 18 is closed
Door 19 is closed
Door 20 is closed
Door 21 is closed
Door 22 is closed
Door 23 is closed
Door 24 is closed
Door 25 is open
Door 26 is closed
Door 27 is closed
Door 28 is closed
Door 29 is closed
Door 30 is closed
Door 31 is closed
Door 32 is closed
Door 33 is closed
Door 34 is closed
Door 35 is closed
Door 36 is open
Door 37 is closed
Door 38 is closed
Door 39 is closed
Door 40 is closed
Door 41 is closed
Door 42 is closed
Door 43 is closed
Door 44 is closed
Door 45 is closed
Door 46 is closed
Door 47 is closed
Door 48 is closed
Door 49 is open
Door 50 is closed
Door 51 is closed
Door 52 is closed
Door 53 is closed
Door 54 is closed
Door 55 is closed
Door 56 is closed
Door 57 is closed
Door 58 is closed
Door 59 is closed
Door 60 is closed
Door 61 is closed
Door 62 is closed
Door 63 is closed
Door 64 is open
Door 65 is closed
Door 66 is closed
Door 67 is closed
Door 68 is closed
Door 69 is closed
Door 70 is closed
Door 71 is closed
Door 72 is closed
Door 73 is closed
Door 74 is closed
Door 75 is closed
Door 76 is closed
Door 77 is closed
Door 78 is closed
Door 79 is closed
Door 80 is closed
Door 81 is open
Door 82 is closed
Door 83 is closed
Door 84 is closed
Door 85 is closed
Door 86 is closed
Door 87 is closed
Door 88 is closed
Door 89 is closed
Door 90 is closed
Door 91 is closed
Door 92 is closed
Door 93 is closed
Door 94 is closed
Door 95 is closed
Door 96 is closed
Door 97 is closed
Door 98 is closed
Door 99 is closed
Door 100 is open
```


## Run BASIC

Works with

:

Just BASIC

Works with

:

Liberty BASIC

```mw
dim doors(100)
print "Open doors ";
for i = 1 to 100 
    for door = i to 100 step i
        doors(door) = (doors(door) <> 1)
        if i = door and doors(door) = 1 then   print i;" ";
    next door
next i
```

Output:

```
Open doors 1 4 9 16 25 36 49 64 81 100
```


## Rust

```mw
fn main() {
    let mut door_open = [false; 100];
    for pass in 1..101 {
        let mut door = pass;
        while door <= 100 {
            door_open[door - 1] = !door_open[door - 1];
            door += pass;
        }
    }
    for (i, &is_open) in door_open.iter().enumerate() {
        println!(
            "Door {} is {}.",
            i + 1,
            if is_open { "open" } else { "closed" }
        );
    }
}
```

Declarative version of above:

```mw
fn main() {
    let doors = vec![false; 100]
        .iter_mut()
        .enumerate()
        .map(|(door, door_state)| {
            (1..101)
                .into_iter()
                .filter(|pass| (door + 1) % pass == 0)
                .map(|_| {
                    *door_state = !*door_state;
                    *door_state
                })
                .last()
                .unwrap()
        })
        .collect::<Vec<_>>();

    println!("{:?}", doors);
}
```

Optimized version: (In this case the printing is the bottleneck so this version is not faster than the above one.)

```mw
fn main() {
    let squares: Vec<_> = (1..11).map(|n| n * n).collect();
    let is_square = |num| squares.binary_search(&num).is_ok();

    for i in 1..101 {
        let state = if is_square(i) { "open" } else { "closed" };
        println!("Door {} is {}", i, state);
    }
}
```

ultra-optimized: ported from Julia version

```mw
fn main() {
    for i in 1u32..11u32 {
        println!("Door {} is open", i.pow(2));
    }
}
```


## Rye

Works with

:

Rye

version 0.1.00

```mw
replicate 100 { false }
|walk\pos 'p {
	.map\pos 'r { ::d ,
		either r .is-multiple-of p { not d } { d } }
	|at p }
|map\pos 'p { .either { p } { false } }
|filter { .is-integer }
|for { .embed "Door {} is open." |print }
```

**Output:**

```
Door 1 is open.
Door 4 is open.
Door 9 is open.
Door 16 is open.
Door 25 is open.
Door 36 is open.
Door 49 is open.
Door 64 is open.
Door 81 is open.
Door 100 is open.
```


## S-BASIC

```mw
$constant DOOR_OPEN = 1
$constant DOOR_CLOSED = 0
$constant MAX_DOORS = 100

var i, j = integer
dim integer doors(MAX_DOORS)

rem - all doors are initially closed
for i = 1 to MAX_DOORS
  doors(i) = DOOR_CLOSED
next i

rem - cycle through at increasing intervals and flip doors
for i = 1 to MAX_DOORS
  for j = i to MAX_DOORS step i
    doors(j) = 1 - doors(j)
  next j
next i

rem - report results
print "The open doors are:"
for i = 1 to MAX_DOORS
  if doors(i) = DOOR_OPEN then
     print i;
next i

end
```

**Output:**

```
The open doors are:
 1 4 9 16 25 36 49 64 81 100
```


## S-lang

```mw
variable door,
    isOpen = Char_Type [101],
    pass;
 
for (door = 1; door <= 100; door++) {
    isOpen[door] = 0;
}
 
for (pass = 1; pass <= 100; pass++) {
    for (door = pass; door <= 100; door += pass) {
        isOpen[door] = not isOpen[door];
    }
}
 
for (door = 1; door <= 100; door++) {
    if (isOpen[door]) {
        print("Door " + string(door) + ":open");
    } else {
        print("Door " + string(door) + ":close");
    }
}
```


## Salmon

Here's an unoptimized version:

```mw
variable open := <<(* --> false)>>;
for (pass; 1; pass <= 100)
    for (door_num; pass; door_num <= 100; pass)
        open[door_num] := !(open[door_num]);;;
iterate (door_num; [1...100])
    print("Door ", door_num, " is ",
          (open[door_num] ? "open.\n" : "closed.\n"));;
```

And here's an optimized one-line version:

```mw
iterate (x; [1...10]) { iterate (y; [(x-1)*(x-1)+1...x*x-1]) { print("Door ", y, " is closed.\n"); }; print("Door ", x*x, " is open.\n"); };
```

And a shorter optimized one-line version:

```mw
variable y:=1;for(x;1;x<101)"Door "~sprint(x)~" is "~(x==y*y?{++y;return"open";}:"closed")!;
```


## SAS

```mw
data _null_;
   open=1;
   close=0;
   array Door{100};
   do Pass = 1 to 100;
      do Current = Pass to 100 by Pass;
         if Door{Current} ne open 
            then Door{Current} = open;
            else Door{Current} = close;
      end;
   end;
   NumberOfOpenDoors = sum(of Door{*});
   put "Number of Open Doors:  " NumberOfOpenDoors; 
run;
```


## Sather

```mw
class MAIN is
  main is
    doors :ARRAY{BOOL} := #(100);
    loop
      pass::= doors.ind!;
      loop
        i::= pass.stepto!(doors.size - 1, pass + 1);
        doors[i] := ~doors[i];
      end;
    end;
    loop
      #OUT + (doors.ind! + 1) + " " + doors.elt! + "\n";
    end;
  end;
end;
```


## Scala

```mw
for { i <- 1 to 100
      r = 1 to 100 map (i % _ == 0) reduceLeft (_^_)                 
    } println (i +" "+ (if (r) "open" else "closed"))
```

The map operation maps each door (i) to a boolean sequence of toggles, one for each pass: true toggles, false leaves the same.

The reduceLeft method combines all the toggles sequentially, using the XOR operator.

And then we just need to output the result.

I made a version that optional accepts an argument for the number of doors. It is also a little more a ‘classical’ solution:

```mw
def openDoors(length : Int = 100) = {
    var isDoorOpen = new Array[Boolean](length)

    for (i <- 0 until length) {
        for (j <- i until length by i + 1) {
            isDoorOpen(j) ^= true
        }
    }
    isDoorOpen
}

val doorState  = scala.collection.immutable.Map(false -> "closed", true -> "open")
val isDoorOpen = openDoors()

for (doorNo <- 0 until isDoorOpen.length) {
    println("Door %d is %s".format(doorNo + 1, doorState(isDoorOpen(doorNo))))
}
```

I created the function openDoors which gives back an array signifying if a door is open and optional accepts an argument for the number of doors. (I like to make things general.) I call the function and use the result to display the status of the doors.

"Optimized" version:

```mw
val o = 1 to 10 map (i => i * i)
println("open: " + o)
println("closed: " + (1 to 100 filterNot o.contains))
```


## Scheme

**unoptimized**

```mw
(define *max-doors* 100)

(define (show-doors doors)
  (let door ((i 0)
             (l (vector-length doors)))
    (cond ((= i l) 
           (newline))
          (else 
           (printf "~nDoor ~a is ~a" 
                   (+ i 1) 
                   (if (vector-ref doors i) "open" "closed"))
           (door (+ i 1) l)))))

(define (flip-doors doors)
  (define (flip-all i)
    (cond ((> i *max-doors*) doors)
          (else 
           (let flip ((idx (- i 1)))
             (cond ((>= idx *max-doors*) 
                    (flip-all (+ i 1))) 
                   (else 
                    (vector-set! doors idx (not (vector-ref doors idx)))
                    (flip (+ idx i))))))))
  (flip-all 1))

(show-doors (flip-doors (make-vector *max-doors* #f)))
```

**optimized**

```mw
(define (optimised-flip-doors doors)
  (define (flip-all i)
    (cond ((> i (floor (sqrt *max-doors*))) doors)
          (else 
           (vector-set! doors (- (* i i) 1) #t)
           (flip-all (+ i 1)))))
  (flip-all 1))

(show-doors (optimised-flip-doors (make-vector *max-doors* #f)))
```

**unoptimized v2**

```mw
(define (N_doors N)
  (define (init)
    (define (str n)
      (if (> n N) '() (cons 0 (str (+ 1 n)))))
    (str 1))
  (define (toggle x str)
    (define (s n lis)
      (define (revert x)
        (if (eq? x 0) 1 0))
      (cond ((null? lis) '())
          ((zero? (remainder n x)) (cons (revert (car lis)) (s (+ n 1) (cdr lis))))
          (else (cons (car lis) (s (+ n 1) (cdr lis))))))
    (s 1 str))
  (define (iterate x lis)
    (if (> x N) lis (iterate (+ x 1) (toggle x lis))))
  (iterate 1 (init)))
(N_doors 100)
```

Output of the 3rd version: 1 represents open, 0 represents closed.

```
(1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1)
```

**unoptimized v3**

```mw
(define (doors-toggle door-state)
  (define (doors-toggle-helper door-state num-doors step counter)
    (cond ((> step num-doors) door-state)
          ((> counter (1- num-doors))
           (doors-toggle-helper door-state num-doors (1+ step) step))
          (else (vector-set! door-state
                             counter
                             (not (array-ref door-state counter)))
                (doors-toggle-helper door-state
                                     num-doors
                                     step
                                     (+ step counter)))))
  (let ((step 1)
        (num-doors (vector-length door-state)))
    (doors-toggle-helper door-state num-doors step (1- step))))

(doors-toggle (make-vector 100 #f)) ;; #t is an open door, #f a closed one
```

```
(#t #f #f #t #f #f #f #f #t #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #t #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #f #t)
```
