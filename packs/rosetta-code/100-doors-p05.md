---
title: "100 doors (part 5/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 5/10
---

## Emacs Lisp

### Unoptimized

```mw
(defun create-doors ()
  "Returns a list of closed doors

Each door only has two status: open or closed.
If a door is closed it has the value 0, if it's open it has the value 1."
  (let ((return_value '(0))
         ;; There is already a door in the return_value, so k starts at 1
         ;; otherwise we would need to compare k against 99 and not 100 in
         ;; the while loop
         (k 1))
    (while (< k 100)
      (setq return_value (cons 0 return_value))
      (setq k (+ 1 k)))
    return_value))

(defun toggle-single-door (doors)
  "Toggle the stat of the door at the `car' position of the DOORS list

DOORS is a list of integers with either the value 0 or 1 and it represents
a row of doors.

Returns a list where the `car' of the list has it's value toggled (if open
it becomes closed, if closed it becomes open)."
  (if (= (car doors) 1)
    (cons 0 (cdr doors))
    (cons 1 (cdr doors))))

(defun toggle-doors (doors step original-step)
  "Step through all elements of the doors' list and toggle a door when step is 1

DOORS is a list of integers with either the value 0 or 1 and it represents
a row of doors.
STEP is the number of doors we still need to transverse before we arrive
at a door that has to be toggled.
ORIGINAL-STEP is the value of the argument step when this function is
called for the first time.

Returns a list of doors"
  (cond ((null doors)
          '())
    ((= step 1)
      (cons (car (toggle-single-door doors))
        (toggle-doors (cdr doors) original-step original-step)))
    (t
      (cons (car doors)
        (toggle-doors (cdr doors) (- step 1) original-step)))))

(defun main-program ()
  "The main loop for the program"
  (let ((doors_list (create-doors))
         (k 1)
         ;; We need to define max-specpdl-size and max-specpdl-size to big
         ;; numbers otherwise the loop reaches the max recursion depth and
         ;; throws an error.
         ;; If you want more information about these variables, press Ctrl
         ;; and h at the same time and then press v and then type the name
         ;; of the variable that you want to read the documentation.
         (max-specpdl-size 5000)
         (max-lisp-eval-depth 2000))
    (while (< k 101)
      (setq doors_list (toggle-doors doors_list k k))
      (setq k (+ 1 k)))
    doors_list))

(defun print-doors (doors)
  "This function prints the values of the doors into the current buffer.

DOORS is a list of integers with either the value 0 or 1 and it represents
a row of doors.
"
  ;; As in the main-program function, we need to set the variable
  ;; max-lisp-eval-depth to a big number so it doesn't reach max recursion
  ;; depth.
  (let ((max-lisp-eval-depth 5000))
    (unless (null doors)
      (insert (int-to-string (car doors)))
      (print-doors (cdr doors)))))

;; Returns a list with the final solution
(main-program)

;; Print the final solution on the buffer
(print-doors (main-program))
```

### Using bit manipulation

```mw
(defun one-hundred-doors(initial-state)
  "Turn doors in INITIAL-STATE according to 100 Doors problem."
  (interactive "nEnter initial doors' state (as a number): ")
  (cl-loop for x from 1 to 100
           do (cl-loop for y from (1- x) to 99 by x
                       do (setq initial-state (logxor initial-state (ash 1 y)))))
  (let ((counter 1)
        (open-doors nil))
    (while (> initial-state 0)
      (when (eq (mod initial-state 2) 1)
        (push counter open-doors))
      (cl-incf counter)
      (setq initial-state (/ initial-state 2)))
    (message "Open doors are %s" (reverse open-doors))))

(one-hundred-doors 0)
```

**Output:**

```
"Open doors are (1 4 9 16 25 36 49 64 81 100)"
```


## EMal

```mw
type Door:State
enum do int CLOSED, OPEN end
type Door
model
  int id
  Door:State state
  new by int ←id, Door:State ←state do end
  fun toggle ← <|me.state ← when(me.state æ Door:State.CLOSED, Door:State.OPEN, Door:State.CLOSED)
  fun asText ← <|"Door #" + me.id + " is " + when(me.state æ Door:State.CLOSED, "closed", "open")
end
type Main
^|There are 100 doors in a row that are all initially closed.|^
List doors ← Door[].with(100, <int i|Door(i + 1, Door:State.CLOSED))
^|You make 100 passes by the doors.|^
for int pass ← 0; pass < 100; ++pass
  for int i ← pass; i < 100; i +← pass + 1
    doors[i].toggle()
  end
end
^|Which are open, which are closed?|^
for each Door door in doors
  if door.state æ Door:State.CLOSED do continue end
  writeLine(door)
end
```

**Output:**

```
Door #1 is open
Door #4 is open
Door #9 is open
Door #16 is open
Door #25 is open
Door #36 is open
Door #49 is open
Door #64 is open
Door #81 is open
Door #100 is open
```


## Erlang

**non-optimized**

```mw
-module(hundoors).

-export([go/0]).

toggle(closed) -> open;
toggle(open) -> closed.

go() -> go([closed || _ <- lists:seq(1, 100)],[], 1, 1).
go([], L, N, _I) when N =:= 101 -> lists:reverse(L);
go([], L, N, _I) -> go(lists:reverse(L), [], N + 1, 1);
go([H|T], L, N, I) ->
  H2 = case I rem N of
    0 -> toggle(H);
    _ -> H
  end,
  go(T, [H2|L], N, I + 1).
```

using an array is faster (around 2 time faster for 100 doors but already 25 faster for 10 000 doors)

```mw
array_go() -> go(array:new([101, fixed, {default, closed}]), 1, 1).

go(Array, Big, Inc) when Big > 100, Inc =< 100 ->
    go(Array, Inc + 1, Inc + 1);
go(Array, Index, Inc) when Inc < 101 ->
    go(array:set(Index, toggle(Array, Index), Array), Index + Inc, Inc);
go(Array, _, _) -> array:sparse_to_orddict(Array).

toggle(Array, Index) -> toggle(array:get(Index, Array)).
```

and, as an added benefit, the output is nicer :)

**Output:**

```
 task_100_doors:array_go().
[{1,open},
 {4,open},
 {9,open},
 {16,open},
 {25,open},
 {36,open},
 {49,open},
 {64,open},
 {81,open},
 {100,open}]
```

**optimized**

```mw
doors() ->
     F = fun(X) -> Root = math:pow(X,0.5), Root == trunc(Root) end,
     Out = fun(X, true) -> io:format("Door ~p: open~n",[X]);
              (X, false)-> io:format("Door ~p: close~n",[X]) end,
     [Out(X,F(X)) || X <- lists:seq(1,100)].
```


## ERRE

```mw
! "100 Doors" program for ERRE LANGUAGE
! Author: Claudio Larini
! Date: 21-Nov-2014
!
! PC Unoptimized version translated from a QB version

PROGRAM 100DOORS

!$INTEGER

CONST N=100

DIM DOOR[N]

BEGIN

FOR STRIDE=1 TO N DO
    FOR INDEX=STRIDE TO N STEP STRIDE DO
        DOOR[INDEX]=NOT(DOOR[INDEX])
    END FOR
END FOR

PRINT("Open doors:";)
FOR INDEX=1 TO N DO
    IF DOOR[INDEX] THEN PRINT(INDEX;) END IF
END FOR
PRINT

END PROGRAM
```


## Euler

In Euler, all variables have the value `undefined` until assigned another value. `isu x` returns `true` if x is currently undefined and the and/or operators short-circuit.

```
begin     new doors; new i; label doorLoop; label outDoors;
          doors <- list 100;
          i     <- 0;
doorLoop: if [ i <- i + 1 ] <= length doors then begin
             new j; label flipLoop;
             j  <- 0;
flipLoop:    if [ j <- J + i ] <= length doors then begin
                doors[ j ] <- isu doors[ j ] or not doors[ j ];
                goto flipLoop
             end else 0;
             goto doorLoop
          end else 0;
          i <- 0;
outDoors: if [ i <- i + 1 ] <= length doors then begin
             if doors[ i ] then out i else 0;
             goto outDoors
          end else 0
end $
```


## Euler Math Toolbox

```mw
>function Doors () ...
$  doors:=zeros(1,100);
$  for i=1 to 100
$    for j=i to 100 step i
$      doors[j]=!doors[j];
$    end;
$  end;
$  return doors
$endfunction
>nonzeros(Doors())
 [ 1  4  9  16  25  36  49  64  81  100 ]
```


## Euphoria

unoptimised

```mw
-- doors.ex
include std/console.e
sequence doors
doors = repeat( 0, 100 ) -- 1 to 100, initialised to false 

for pass = 1 to 100 do
	for door = pass to 100 by pass do
		--printf( 1, "%d", doors[door] )
		--printf( 1, "%d", not doors[door] )
		doors[door] = not doors[door]
	end for
end for

sequence oc

for i = 1 to 100 do
	if doors[i] then
		oc = "open"
	else
		oc = "closed"
	end if
 	printf( 1, "door %d is %s\n", { i, oc } )
end for
```


## Excel

### Multi-cell approaach

Note: The use of Auto Fill saves a lot of time when entering this code. One can refer to Excel help pages to learn about Auto Fill features. Create a labelling column (A) and row (1) labelling the number of the door (column A, labelling starts in row 2 with a "1" and continues counting up to "100" in row 101) and the number of the pass (row 1, labelling starts in column B with a "0" and continues counting up to "100" in column CX). Additonally, you can label cell A1 as "Door/Pass" or so. Closed doors are represented by zeroes ("0"), open doors are represented by ones ("1"). To represent the initial condition fill rows 2 to 101 in column B (pass "0") with zeroes. Starting in column C, row 2, you enter code as shown in the examples below. The examples show the code to be entered in cells C2, C3, and D2. Continue to write code for the rest of the 4245 data cells, accordingly. Excel Auto Fill feature is best used for this.

Cell C2:

```mw
=IF($A2/C$1=INT($A2/C$1),IF(B2=0,1,IF(B2=1,0)),B2)
```

Cell C3:

```mw
=IF($A3/C$1=INT($A3/C$1),IF(B3=0,1,IF(B3=1,0)),B3)
```

Cell D2:

```mw
=IF($A2/D$1=INT($A2/D$1),IF(C2=0,1,IF(C2=1,0)),C2)
```

The last column (column CX, labelled "100") shows a "1" for each door (labelled by the rows in column A) that is open after the 100th pass. It shows a "1" for the following doors: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100.

### Single cell approach (Optimized)

```mw
=LET(i, SEQUENCE(100), root, SQRT(i), "Door " & i &  ": " & IF(root = INT(root), "open", "close"))
```


## F

### Classical

```mw
type doorState=Open|Closed
let flip=function Open->Closed |_->Open
let Doors=Array.create 100 Closed
for n in 1..100 do {n-1..n..99}|>Seq.iter(fun n->Doors[n]<-flip Doors[n])
Doors|>Array.iteri(fun n g->if g=Open then printf "%d " (n+1)); printfn ""
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```

Simple single line solution using nothing but List

```mw
[1..100] |> List.fold (fun doors pass->List.mapi (fun i x->if ((i + 1) % pass)=0 then not x else x) doors) (List.init 100 (fun _->false))
```

### Translation of Q

Must save them bits!

```mw
let X q=not q
let mutable q = false
let mutable doors = []
for n in 1..100 do
  for g in 1..n do if n%g=0 then q<-X(q)
  if q then doors<-n::doors
  q<-false
printfn "%A" (doors|>List.rev)
```

**Output:**

```
[1; 4; 9; 16; 25; 36; 49; 64; 81; 100]
```


## Factor

**Unoptimized**

```mw
USING: bit-arrays formatting fry kernel math math.ranges
sequences ;
IN: rosetta.doors

CONSTANT: number-of-doors 100

: multiples ( n -- range )
    0 number-of-doors rot <range> ;

: toggle-multiples ( n doors -- )
    [ multiples ] dip '[ _ [ not ] change-nth ] each ;

: toggle-all-multiples ( doors -- )
    [ number-of-doors [1,b] ] dip '[ _ toggle-multiples ] each ;

: print-doors ( doors -- )
    [
        swap "open" "closed" ? "Door %d is %s\n" printf
    ] each-index ;

: main ( -- )
    number-of-doors 1 + <bit-array>
    [ toggle-all-multiples ] [ print-doors ] bi ;

main
```

**Optimized**

```mw
USING:
    formatting
    math math.primes.factors math.ranges
    sequences ;
IN: rosetta-doors2

: main ( -- )
    100 [1,b] [ divisors length odd? ] filter "Open %[%d, %]\n" printf ;
```


## Falcon

**Unoptimized code**

```mw
doors = arrayBuffer( 101, false )

for pass in [ 0 : doors.len() ]
  for door in [ 0 : doors.len() : pass+1 ]
    doors[ door ] = not doors[ door ]
  end
end

for door in [ 1 : doors.len() ]  // Show Output
  >  "Door ", $door, " is: ", ( doors[ door ] ) ? "open" : "closed"
end
```

**Optimized code**

```mw
for door in [ 1 : 101 ]: > "Door ", $door, " is: ", fract( door ** 0.5 ) ? "closed" : "open"
```


## FALSE

```mw
100[$][0 1ø:1-]#              {initialize doors}
%
[s;[$101\>][$$;~\:s;+]#%]d:   {function d, switch door state function}
1s:[s;101\>][d;!s;1+s:]#      {increment step width from 1 to 100, execute function d each time}
1[$101\>][$$." ";$["open
"]?~["closed
"]?1+]#                       {loop through doors, print door number and state}
```

Result:

```mw
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
...
98 closed
99 closed
100 open
```

Compare this solution to the DUP solution of this problem.


## Fantom

**Unoptimized**

```mw
    states := (1..100).toList
    100.times |i| {
      states = states.map |state| { state % (i+1) == 0 ? -state : +state }
    }
    echo("Open doors are " + states.findAll { it < 0 }.map { -it })
```

**Optimized**

```mw
    echo("Open doors are " + (1..100).toList.findAll { it.toFloat.pow(0.5f).toInt.pow(2) == it})
```


## FBSL

**Unoptimised**

```mw
#AppType Console

Dim doors[], n As Integer = 100

For Dim i = 1 To n
	For Dim j = i To n Step i
		doors[j] = Not doors[j]
	Next
Next

For i = 1 To n
	If doors[i] Then Print "Door ", i, " is open"
Next

Pause
```

**Optimised** (by ML)

```mw
#APPTYPE CONSOLE

DIM i = 0, j = 0, door = 1

WHILE INCR(i) < 101
 IF i = door THEN
   PRINT "Door ", door, " open"
   INCR(door, INCR((INCR(j) << 1)))
 END IF
WEND

PAUSE
```


## Fe

```mw
; macro for finite loop
(= repeat (mac (i n . body)
  (list 'do
    (list 'let i 0)
    (list 'while (list '< i n)
      (list '= i (list '+ i 1))
      (cons 'do body)))))

; function to get n-th element of list
(= nth (fn (i lst)
  (while (< 0 i)
    (= i (- i 1))
    (= lst (cdr lst)))
  lst))

; make list of 100 nils
(repeat i 100 (= doors (cons nil doors)))

; do algorithm iterations
(repeat i 100
  (let pos (nth (- i 1) doors))
  (while pos
    (setcar pos (not (car pos)))
    (= pos (nth i pos))))

(print doors)
```

Algorithm iterations can be simplified to:

```mw
; do algorithm iterations sqrt(100) = 10 times
(repeat i 10 (setcar (nth (- (* i i) 1) doors) 't))
```


## Fennel

```mw
(do ;;; find the first few squares via the unoptimised door flipping method

    (local door-max 100)

    ; repeatedly flip the doors and show the ones that are left open
    (var door {})
    (for [i 1 door-max]
         (for [j i door-max i]
              (tset door j (not (. door j)))
         )
         (when (. door i)
               (io.write (.. " " i))
         )
    )
)
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```


## Fhidwfe

unoptomized

```mw
doors = malloc$ 100u
for uint [0u, sizeof$ doors) with l1 {
  put_byte$ + doors l1 as false byte
}
function void pass(step:uint) {
  location = step
  while <= location sizeof$ doors {
    ac = - + doors location 1u
    put_byte$ ac ~ deref_byte$ ac// true is represented as 255 (0xff)
    location = + location step
  }
}
for uint (0u, sizeof$ doors] with l2 {//range exclusive of 0, inclusive of 100
  pass$ l2
}
count = 1u
for ubyte as doors listubyte with isopen {// list for-each
  if as isopen bool {// cast byte to bool
    puts$ "door "
    putui$ count
    puts$ " is open\n"
  } ;
  count = + count 1u
}
free$ doors
```


## Fish

**Unoptimized**

```mw
1001-p01.
>0101-p02.
>101-g001-g+:::aa*)?v101-p03.
>02-g?v1}02-p02.    >05.
      >0}02-p02.
>~~~0101-p001-g:1+001-paa*)?v02.
                            >07.
>0101-p08.
>101-g::02-g?v     >1+:101-paa*=?;
             >n" "o^
```


## FOCAL

```mw
1.1 F N=1,100;S D(N)=0
1.2 F M=1,100;F N=M,M,100;S D(N)=1-D(N)
1.3 F N=1,100;D 2.0
1.4 Q
2.1 I (D(N)),,2.2;R
2.2 T "OPEN DOOR ",%3.0,N,!
```

**Output:**

```
OPEN DOOR =   1
OPEN DOOR =   4
OPEN DOOR =   9
OPEN DOOR =  16
OPEN DOOR =  25
OPEN DOOR =  36
OPEN DOOR =  49
OPEN DOOR =  64
OPEN DOOR =  81
OPEN DOOR = 100
```


## Forth

**Unoptimized**

```mw
: toggle ( c-addr -- )  \ toggle the byte at c-addr
    dup c@ 1 xor swap c! ;

100  1+ ( 1-based indexing ) constant ndoors
create doors  ndoors allot

: init ( -- )  doors ndoors erase ;  \ close all doors

: pass ( n -- )  \ toggle every nth door
    ndoors over do
        doors i + toggle
    dup ( n ) +loop drop ;

: run ( -- )  ndoors 1 do  i pass  loop ;
: display ( -- )  \ display open doors
    ndoors 1 do  doors i + c@ if  i .  then loop cr ;

init run display
```

**Optimized**

```mw
: squared ( n -- n' )  dup * ;
: doors ( n -- )
    1 begin 2dup squared >= while
        dup squared .
    1+ repeat 2drop ;
100 doors
```


## Fortran

Works with

:

Fortran 90

**unoptimized**

```mw
program doors
    implicit none
    integer, allocatable :: door(:)
    character(6), parameter :: s(0:1) = [character(6) :: "closed", "open"]
    integer :: i, n
  
    print "(A)", "Number of doors?"
    read *, n
    allocate (door(n))
    door = 1
    do i = 1, n
        door(i:n:i) = 1 - door(i:n:i)
        print "(A,G0,2A)", "door ", i, " is ", s(door(i))
    end do
end program
```

**optimized**

```mw
PROGRAM DOORS

  INTEGER, PARAMETER :: n = 100    ! Number of doors
  INTEGER :: i
  LOGICAL :: door(n) = .TRUE.      ! Initially closed
 
  DO i = 1, SQRT(REAL(n))
    door(i*i) = .FALSE.
  END DO  
 
  DO i = 1, n
    WRITE(*,"(A,I3,A)", ADVANCE="NO") "Door ", i, " is "
    IF (door(i)) THEN
      WRITE(*,"(A)") "closed"
    ELSE
      WRITE(*,"(A)") "open"
    END IF
  END DO
 
END PROGRAM DOORS
```

**alternate approach** Alternate version in Fortan 90+

```mw
! =============================================================================
! DOORS PROBLEM
! =============================================================================
!
! PROBLEM STATEMENT:
!   100 doors are all initially closed.  We make 100 passes.
!   Pass 1 toggles every door  (1, 2, 3, ..., 100).
!   Pass 2 toggles every 2nd   (2, 4, 6, ..., 100).
!   Pass k toggles every k-th  (k, 2k, 3k, ...).
!   Pass 100 toggles only door 100.
!   What state is each door in after all 100 passes?
!
! ALGORITHM -- DIVISOR COUNTING:
!   Door number D is toggled on pass k if and only if k divides D evenly,
!   i.e. mod(D, k) == 0.  So the total number of toggles that door D receives
!   equals the number of divisors of D (including 1 and D itself).
!
!   Example: door 6
!     Divisors of 6 are 1, 2, 3, 6  =>  4 toggles  =>  even  =>  CLOSED
!
!   Example: door 9
!     Divisors of 9 are 1, 3, 9     =>  3 toggles  =>  odd   =>  OPEN
!
!   A door ends up OPEN  when its divisor count is ODD.
!   A door ends up CLOSED when its divisor count is EVEN.
!
! KEY MATHEMATICAL INSIGHT (why the pattern is perfect squares):
!   Divisors normally come in pairs: if j divides D then (D/j) also divides D,
!   giving an even count.  The only exception is when j == D/j, i.e. j*j == D.
!   That "pairing trick" breaks at the square root, leaving one unpaired divisor
!   and making the total ODD.  This happens exactly when D is a perfect square.
!   So doors 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 are open; all others closed.
!
!   This program proves the result by brute-force divisor counting, rather than
!   assuming the mathematical conclusion up front.
! =============================================================================

program doors
    implicit none

    integer, parameter :: n = 100   ! total number of doors (and passes)
    integer :: door                 ! current door being evaluated (1..n)
    integer :: pass                 ! current pass number being tested (1..n)
    integer :: toggles              ! number of times this door was toggled
    character(6) :: state           ! final state label: 'open' or 'closed'

    ! --- outer loop: consider each door in turn ---
    do door = 1, n

        toggles = 0   ! reset the toggle counter for this door

        ! --- inner loop: check every pass to see if it touches this door ---
        ! Pass number 'pass' visits door 'door' only when 'pass' is a divisor
        ! of 'door'.  mod(door, pass) == 0 means pass divides door exactly.
        do pass = 1, n
            if (mod(door, pass) == 0) toggles = toggles + 1
        end do

        ! --- determine final state from parity of toggle count ---
        ! Starting closed, an odd number of toggles leaves the door open;
        ! an even number returns it to closed.
        if (mod(toggles, 2) == 1) then
            state = 'open'
        else
            state = 'closed'
        end if

        ! --- report result for this door ---
        write(*, '(A, I3, A, A)') 'Door', door, ' is ', trim(state)

    end do

end program doors
```

```
Door  1 is open
Door  2 is closed
Door  3 is closed
Door  4 is open
Door  5 is closed
Door  6 is closed
Door  7 is closed
Door  8 is closed
Door  9 is open
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
Door100 is open
```


## Free Pascal

```mw
program OneHundredIsOpen;

const
  DoorCount = 100;

var
  IsOpen: array[1..DoorCount] of boolean;
  Door, Jump: integer;

begin
  // Close all doors
  for Door := 1 to DoorCount do
    IsOpen[Door] := False;
  // Iterations
  for Jump := 1 to DoorCount do
  begin
    Door := Jump;
    repeat
      IsOpen[Door] := not IsOpen[Door];
      Door := Door + Jump;
    until Door > DoorCount;
  end;
  // Show final status
  for Door := 1 to DoorCount do
  begin
    Write(Door, ' ');
    if IsOpen[Door] then
      WriteLn('open')
    else
      WriteLn('closed');
  end;
  // Wait for <enter>
  Readln;
end.
```


## FreeBASIC

### Toggle

```mw
' version 27-10-2016
' compile with: fbc -s console

#Define max_doors 100

Dim As ULong c, n, n1, door(1 To max_doors)

' toggle, at start all doors are closed (0)
' 0 = door closed, 1 = door open
For n = 1 To max_doors
    For n1 = n To max_doors Step n
        door(n1) = 1 - door(n1)
    Next
Next

' count the doors that are open (1)
Print "doors that are open nr: ";
For n = 1 To max_doors
    If door(n) = 1 Then
        Print n; " ";
        c = c + 1
    End If
Next

Print : Print
Print "There are " + Str(c) + " doors open"

' empty keyboard buffer
While InKey <> "" : Wend
Print : Print "hit any key to end program"
Sleep
End
```

**Output:**

```
doors that are open nr: 1 4 9 16 25 36 49 64 81 100 

There are 10 doors open
```

### Count

```mw
' version 27-10-2016
' compile with: fbc -s console

#Define max_doors 100

Dim As ULong c, n, n1, door(1 To max_doors)

' at start all doors are closed
' simple add 1 each time we open or close a door
' doors with odd numbers are open
' doors with even numbers are closed
For n = 1 To max_doors
    For n1 = n To max_doors Step n
        door(n1) += 1
    Next
Next

Print "doors that are open nr: ";
For n = 1 To max_doors
    If door(n) And 1 Then
        Print n; " ";
        c = c + 1
    End If
Next

Print : Print
Print "There are " + Str(c) + " doors open"

' empty keyboard buffer
While InKey <> "" : Wend
Print : Print "hit any key to end program"
Sleep
End
```

Output is the same as the first version.

### Optimized

```mw
' version 27-10-2016
' compile with: fbc -s console

#Define max_doors 100

Dim As ULong c, n

Print "doors that are open nr: ";
For n = 1 To 10
    Print n * n; " ";
    c = c + 1
Next

Print : Print
Print "There are " + Str(c) + " doors open"

' empty keyboard buffer
While InKey <> "" : Wend
Print : Print "hit any key to end program"
Sleep
End
```

Output is the same as the first version.

### Ultra optimizado

```mw
' version 16-06-2021
' portado desde Julia

For i As Integer = 1 To 10
    If (i Mod i^2) < 11  Then Print "La puerta"; i^2; " esta abierta"   
Next i
Sleep
```


## friendly interactive shell

**Unoptimized**

```mw
# Set doors to empty list
set doors

# Initialize doors arrays
for i in (seq 100)
    set doors[$i] 0
end

for i in (seq 100)
    set j $i
    while test $j -le 100
        # Logical not on doors
        set doors[$j] (math !$doors[$j])
        set j (math $j + $i)
    end
end

# Print every door
for i in (seq (count $doors))
    echo -n "$i "
    if test $doors[$i] -eq 0
        echo closed
    else
        echo open
    end
end
```

**Optimized**

```mw
# Set doors to empty list
set doors

for i in (seq 100)
    set doors[(math "$i * $i")] 1
    echo -n "$i "
    if test $doors[$i] -eq 1
        echo open
    else
        echo closed
    end
end
```


## Frink

```mw
doors = new array[[101], false]
for pass=1 to 100
   for door=pass to 100 step pass
      doors@door = ! doors@door

print["Open doors:  "]
for door=1 to 100
   if doors@door
      print["$door "]
```


## FTCBASIC

```mw
define i = 0, d = 0

do

	let i = i + 1
	let d = i * i
	print d

loop d < 100

pause
end
```


## FunL

### Unoptimized

```mw
for i <- 1..100
  r = foldl1( \a, b -> a xor b, [(a|i) | a <- 1..100] )
  println( i + ' ' + (if r then 'open' else 'closed') )
```

### Optimized

```mw
import math.sqrt

for i <- 1..100
  println( i + ' ' + (if sqrt(i) is Integer then 'open' else 'closed') )
```


## Futhark

```mw
let main(n: i32): [n]bool =
  loop is_open = replicate n false for i < n do
    let js = map (*i+1) (iota n)
    let flips = map (\j ->
                       if j < n
                       then unsafe !is_open[j]
                       else true -- Doesn't matter.
                    ) js
    in scatter is_open js flips
```


## FutureBasic

```mw
include "NSLog.incl"

NSInteger door, square = 1, increment = 3

for door = 1 to 100
  if ( door == square )
    NSLog( @"Door %ld is open.", door )
    square += increment : increment += 2
  else
    NSLog( @"Door %ld is closed.", door )
  end if
next

HandleEvents
```

**Output:**

```
Door 1 is open.
Door 2 is closed.
Door 3 is closed.
Door 4 is open.
Door 5 is closed.
Door 6 is closed.
Door 7 is closed.
Door 8 is closed.
Door 9 is open.
Door 10 is closed.
Door 11 is closed.
Door 12 is closed.
Door 13 is closed.
Door 14 is closed.
Door 15 is closed.
Door 16 is open.
Door 17 is closed.
Door 18 is closed.
Door 19 is closed.
Door 20 is closed.
Door 21 is closed.
Door 22 is closed.
Door 23 is closed.
Door 24 is closed.
Door 25 is open.
Door 26 is closed.
Door 27 is closed.
Door 28 is closed.
Door 29 is closed.
Door 30 is closed.
Door 31 is closed.
Door 32 is closed.
Door 33 is closed.
Door 34 is closed.
Door 35 is closed.
Door 36 is open.
Door 37 is closed.
Door 38 is closed.
Door 39 is closed.
Door 40 is closed.
Door 41 is closed.
Door 42 is closed.
Door 43 is closed.
Door 44 is closed.
Door 45 is closed.
Door 46 is closed.
Door 47 is closed.
Door 48 is closed.
Door 49 is open.
Door 50 is closed.
Door 51 is closed.
Door 52 is closed.
Door 53 is closed.
Door 54 is closed.
Door 55 is closed.
Door 56 is closed.
Door 57 is closed.
Door 58 is closed.
Door 59 is closed.
Door 60 is closed.
Door 61 is closed.
Door 62 is closed.
Door 63 is closed.
Door 64 is open.
Door 65 is closed.
Door 66 is closed.
Door 67 is closed.
Door 68 is closed.
Door 69 is closed.
Door 70 is closed.
Door 71 is closed.
Door 72 is closed.
Door 73 is closed.
Door 74 is closed.
Door 75 is closed.
Door 76 is closed.
Door 77 is closed.
Door 78 is closed.
Door 79 is closed.
Door 80 is closed.
Door 81 is open.
Door 82 is closed.
Door 83 is closed.
Door 84 is closed.
Door 85 is closed.
Door 86 is closed.
Door 87 is closed.
Door 88 is closed.
Door 89 is closed.
Door 90 is closed.
Door 91 is closed.
Door 92 is closed.
Door 93 is closed.
Door 94 is closed.
Door 95 is closed.
Door 96 is closed.
Door 97 is closed.
Door 98 is closed.
Door 99 is closed.
Door 100 is open.
```


## FUZE BASIC

```mw
READ x,y,z
PRINT "Open doors: ";x;" ";
CYCLE
    z=x+y
    PRINT z;" ";
    x=z
    y=y+2
REPEAT UNTIL z>=100
DATA 1,3,0
END
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

**Solution**

The solution consists in having a 100 element array, initialized with FALSE values. In each of the 100 rounds (controlled by a simple FOR-FROM-TO cycle), the values are flipped using a FOR-FROM-TO-STEP cycle. Finally the array is shown, using green colors for open doors, and red for closed ones. The resulting matrix is transposed in order to be shown horizontally.

The result of calling the function is:

**Improvements. Graphic output, in order to show evolution in time, and an arbitrary number of doors**

100 doors, each door is 3x3 pixel:


## Gambas

**Click this link to run this code**

```mw
Public Sub Main()
Dim bDoor As New Boolean[101]
Dim siCount1, siCount2, siStart As Short

For siCount1 = 1 To 100
  Inc siStart
  For siCount2 = siStart To 100 Step siCount1
    bDoor[siCount2] = Not bDoor[siCount2]
  Next
Next

For siCount1 = 1 To 100
  If bDoor[siCount1] Then Print siCount1;;
Next

End
```

Output:

```
1 4 9 16 25 36 49 64 81 100
```


## GAP

```mw
doors := function(n)
  local a,j,s;
  a := [ ];
  for j in [1 .. n] do
    a[j] := 0;
  od;
  for s in [1 .. n] do
    j := s;
    while j <= n do
      a[j] := 1 - a[j];
      j := j + s;
    od;
  od;
  return Filtered([1 .. n], j -> a[j] = 1);
end;

doors(100);
# [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
```


## GDScript

```mw
func Doors(door_count:int) -> void :
  var doors : Array
  doors.resize(door_count)

  # Note : Initialization is not necessarily mandatory (by default values are false)
  # Intentionally left here
  for i in door_count :
    doors[i] = false

  # do visits
  for i in door_count :
    for j in range(i,door_count,i+1) :
      doors[j] = not doors[j]
  	
  # print results
  var results : String = ""
  for i in door_count :
    results += str(i+1) + " " if doors[i] else ""
  print("Doors open : %s" % [results] )

# calling the function from the _ready function
func _ready() -> void :
  Doors(100)
```

Output:

```
Doors open : 1 4 9 16 25 36 49 64 81 100
```


## Genie

```mw
// 100 doors problem
// Author: Sinuhe masan (2019)
init

	// 100 elements array of boolean type
	doors:bool[100]
    
	for var i = 1 to 100
		doors[i] = false  // set all doors closed
    
    
	for var i = 1 to 100
		j:int = i
		while j <= 100 do
			doors[j] = not doors[j]
			j = j + i
    
	print("Doors open: ")
	for var i = 1 to 100
		if doors[i]
			stdout.printf ("%d ", i)
```


## Glee

```mw
100` *=0=>d                      $$ create vector 1..100, create bit pattern d, marking all equal to 0
:for (1..100[.s]){               $$ loop s from 1 to 100
  d^(100` %s *=0 )=>d;}          $$ d = d xor (bit pattern of vector 1..100 % s)
d                                $$ output d
```

The resulting output is the bit pattern showing the state of the 100 doors:

```mw
Result:
10010000 10000001 00000000 10000000 00010000 00000000 10000000 00000001 00000000 00000000 10000000 00000000 0001
```


## GML

```mw
var doors,a,i;
//Sets up the array for all of the doors.
for (i = 1; i<=100; i += 1)
    {
    doors[i]=0;
    }

//This first for loop goes through and passes the interval down to the next for loop.
for (i = 1; i <= 100; i += 1;)
    {
    //This for loop opens or closes the doors and uses the interval(if interval is 2 it only uses every other etc..)
    for (a = 0; a <= 100; a += i;)
        {
        //Opens or closes a door.
        doors[a] = !doors[a];
        }
    }
open_doors = '';

//This for loop goes through the array and checks for open doors.
//If the door is open it adds it to the string then displays the string.
for (i = 1; i <= 100; i += 1;)
    {
    if (doors[i] == 1)
        {
        open_doors += "Door Number "+string(i)+" is open#";
        }
    }
show_message(open_doors);
game_end();
```


## Go

**unoptimized**

```mw
package main

import "fmt"

func main() {
    doors := [100]bool{}

    // the 100 passes called for in the task description
    for pass := 1; pass <= 100; pass++ {
        for door := pass-1; door < 100; door += pass {
            doors[door] = !doors[door]
        }
    }

    // one more pass to answer the question
    for i, v := range doors {
        if v {
            fmt.Print("1")
        } else {
            fmt.Print("0")
        }

        if i%10 == 9 {
            fmt.Print("\n")
        } else {
            fmt.Print(" ")
        }

    }
}
```

Output:

```
1 0 0 1 0 0 0 0 1 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
```

**optimized**

```mw
package main

import "fmt"

func main() {
    var door int = 1
    var incrementer = 0

    for current := 1; current <= 100; current++ {
        fmt.Printf("Door %d ", current)

        if current == door {
            fmt.Printf("Open\n")
            incrementer++
            door += 2*incrementer + 1
        } else {
            fmt.Printf("Closed\n")
        }
    }
}
```

**optimized 2**

```mw
// 100 (optimized) doors in Go

package main

import (
    "fmt"
    "math"
)

func main() {
    for i := 1; i <= 100; i++ {
        f := math.Sqrt(float64(i))
        if math.Mod(f, 1) == 0 {
            fmt.Print("O")
        } else {
            fmt.Print("-")
        }
    }
    fmt.Println()
}
```

Output:

```
O--O----O------O--------O----------O------------O--------------O----------------O------------------O
```


## Goboscript

```mw
costumes "assets/blank.svg";

list doors;

proc do_100_doors {
    delete doors;
    repeat 100 {add false to doors;}

    local pass_i = 1;
    repeat 100 {
        local i = 0;
        repeat length doors / pass_i {
            i += pass_i;
            doors[i] = not doors[i];
        }
        
        pass_i++;
    }
}

onflag{main;}
proc main {
    do_100_doors;

    show doors;
    local i = 1;
    repeat length doors {
        if doors[i] {
            local state = "open";
        } else {
            local state = "closed";
        }

        log "Door " & i & " is " & state;
        i++;
    }
}
```

**Output:**

```
Args: []
Log: 'Door 1 is open'
Log: 'Door 2 is closed'
Log: 'Door 3 is closed'
Log: 'Door 4 is open'
Log: 'Door 5 is closed'
Log: 'Door 6 is closed'
Log: 'Door 7 is closed'
Log: 'Door 8 is closed'
Log: 'Door 9 is open'
Log: 'Door 10 is closed'
Log: 'Door 11 is closed'
Log: 'Door 12 is closed'
Log: 'Door 13 is closed'
Log: 'Door 14 is closed'
Log: 'Door 15 is closed'
Log: 'Door 16 is open'
Log: 'Door 17 is closed'
Log: 'Door 18 is closed'
Log: 'Door 19 is closed'
Log: 'Door 20 is closed'
Log: 'Door 21 is closed'
Log: 'Door 22 is closed'
Log: 'Door 23 is closed'
Log: 'Door 24 is closed'
Log: 'Door 25 is open'
Log: 'Door 26 is closed'
Log: 'Door 27 is closed'
Log: 'Door 28 is closed'
Log: 'Door 29 is closed'
Log: 'Door 30 is closed'
Log: 'Door 31 is closed'
Log: 'Door 32 is closed'
Log: 'Door 33 is closed'
Log: 'Door 34 is closed'
Log: 'Door 35 is closed'
Log: 'Door 36 is open'
Log: 'Door 37 is closed'
Log: 'Door 38 is closed'
Log: 'Door 39 is closed'
Log: 'Door 40 is closed'
Log: 'Door 41 is closed'
Log: 'Door 42 is closed'
Log: 'Door 43 is closed'
Log: 'Door 44 is closed'
Log: 'Door 45 is closed'
Log: 'Door 46 is closed'
Log: 'Door 47 is closed'
Log: 'Door 48 is closed'
Log: 'Door 49 is open'
Log: 'Door 50 is closed'
Log: 'Door 51 is closed'
Log: 'Door 52 is closed'
Log: 'Door 53 is closed'
Log: 'Door 54 is closed'
Log: 'Door 55 is closed'
Log: 'Door 56 is closed'
Log: 'Door 57 is closed'
Log: 'Door 58 is closed'
Log: 'Door 59 is closed'
Log: 'Door 60 is closed'
Log: 'Door 61 is closed'
Log: 'Door 62 is closed'
Log: 'Door 63 is closed'
Log: 'Door 64 is open'
Log: 'Door 65 is closed'
Log: 'Door 66 is closed'
Log: 'Door 67 is closed'
Log: 'Door 68 is closed'
Log: 'Door 69 is closed'
Log: 'Door 70 is closed'
Log: 'Door 71 is closed'
Log: 'Door 72 is closed'
Log: 'Door 73 is closed'
Log: 'Door 74 is closed'
Log: 'Door 75 is closed'
Log: 'Door 76 is closed'
Log: 'Door 77 is closed'
Log: 'Door 78 is closed'
Log: 'Door 79 is closed'
Log: 'Door 80 is closed'
Log: 'Door 81 is open'
Log: 'Door 82 is closed'
Log: 'Door 83 is closed'
Log: 'Door 84 is closed'
Log: 'Door 85 is closed'
Log: 'Door 86 is closed'
Log: 'Door 87 is closed'
Log: 'Door 88 is closed'
Log: 'Door 89 is closed'
Log: 'Door 90 is closed'
Log: 'Door 91 is closed'
Log: 'Door 92 is closed'
Log: 'Door 93 is closed'
Log: 'Door 94 is closed'
Log: 'Door 95 is closed'
Log: 'Door 96 is closed'
Log: 'Door 97 is closed'
Log: 'Door 98 is closed'
Log: 'Door 99 is closed'
Log: 'Door 100 is open'
Exited with code 0
```


## Golfscript

```mw
100:c;[{0}c*]:d;
c,{.c,>\)%{.d<\.d=1^\)d>++:d;}/}/
[c,{)"door "\+" is"+}%d{{"open"}{"closed"}if}%]zip
{" "*puts}/
```

**optimized with sqrt** (Original version of GolfScript has no sqrt operator, but it can be added easily; the code was tested using a work-in-progress C interpreter for a language compatible enough with Golfscript)

```mw
100,{)}%
{:d.sqrt 2?=
{"open"}{"close"}if"door "d+" is "+\+puts}/
```

**optimized without sqrt**

```mw
[{"close"}100*]:d;
10,{)2?(.d<\["open"]\)d>++:d;}/
[100,{)"door "\+" is"+}%d]zip
{" "*puts}/
```


## Gosu

**unoptimized**

```mw
uses java.util.Arrays

var doors = new boolean[100]
Arrays.fill( doors, false )

for( pass in 1..100 ) {
    var counter = pass-1
    while( counter < 100 ) {
        doors[counter] = !doors[counter]
        counter += pass
  }
}

for( door in doors index i ) {
    print( "door ${i+1} is ${door ? 'open' : 'closed'}" )
}
```

**optimized**

```mw
var door = 1
var delta = 0

for( i in 1..100 ) {
    if( i == door ) {
        print( "door ${i} is open" )
        delta++
        door += 2*delta + 1
    } else {
        print( "door ${i} is closed" )
    }
}
```


## Groovy

**unoptimized**

```mw
doors = [false] * 100
(0..99).each {
   it.step(100, it + 1) {
      doors[it] ^= true
   }
}
(0..99).each {
   println("Door #${it + 1} is ${doors[it] ? 'open' : 'closed'}.")
}
```

**optimized a** Using square roots

```mw
(1..100).each {
   println("Door #${it} is ${Math.sqrt(it).with{it==(int)it} ? 'open' : 'closed'}.")
}
```

**optimized b** Without using square roots

```mw
doors = ['closed'] * 100
(1..10).each { doors[it**2 - 1] = 'open' }
(0..99).each {
   println("Door #${it + 1} is ${doors[it]}.")
}
```


## GW-BASIC

```mw
10 DIM A(100)
20 FOR OFFSET = 1 TO 100
30      FOR I = 0 TO 100 STEP OFFSET
40              A(I) = A(I) + 1
50      NEXT I
60 NEXT OFFSET
70 ' Print "opened" doors
80 FOR I = 1 TO 100
90      IF A(I) MOD 2 = 1 THEN PRINT I
100 NEXT I
```

**Output**:

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


## Harbour

**Unoptimized code:**

```mw
#define ARRAY_ELEMENTS 100
PROCEDURE Main()
   LOCAL aDoors := Array( ARRAY_ELEMENTS )
   LOCAL i, j

   AFill( aDoors, .F. )
   FOR i := 1 TO ARRAY_ELEMENTS
      FOR j := i TO ARRAY_ELEMENTS STEP i
         aDoors[ j ] = ! aDoors[ j ]
      NEXT
   NEXT
   AEval( aDoors, {|e, n| QQout( Padl(n,3) + " is " + Iif(aDoors[n], "*open*", "closed" ) + "|" ), Iif( n%5 == 0, Qout(), e:=NIL) } )
   RETURN
```

**Optimized code**

```mw
#define ARRAY_ELEMENTS 100
PROCEDURE Main()
   LOCAL aDoors := Array( ARRAY_ELEMENTS )

   AFill( aDoors, .F. )
   AEval( aDoors, {|e, n| aDoors[n] := e := Iif( Int(Sqrt(n))==Sqrt(n), .T., .F. ) } )
   AEval( aDoors, {|e, n| QQout( Padl(n,3) + " is " + Iif(aDoors[n], "*open*", "closed" ) + "|" ), Iif( n%5 == 0, Qout(), e:=NIL )} )
   RETURN
```

**Output:**

```
 1 is *open*|  2 is closed|  3 is closed|  4 is *open*|  5 is closed| 
 6 is closed|  7 is closed|  8 is closed|  9 is *open*| 10 is closed| 
11 is closed| 12 is closed| 13 is closed| 14 is closed| 15 is closed| 
16 is *open*| 17 is closed| 18 is closed| 19 is closed| 20 is closed| 
21 is closed| 22 is closed| 23 is closed| 24 is closed| 25 is *open*| 
26 is closed| 27 is closed| 28 is closed| 29 is closed| 30 is closed| 
31 is closed| 32 is closed| 33 is closed| 34 is closed| 35 is closed| 
36 is *open*| 37 is closed| 38 is closed| 39 is closed| 40 is closed| 
41 is closed| 42 is closed| 43 is closed| 44 is closed| 45 is closed| 
46 is closed| 47 is closed| 48 is closed| 49 is *open*| 50 is closed| 
51 is closed| 52 is closed| 53 is closed| 54 is closed| 55 is closed| 
56 is closed| 57 is closed| 58 is closed| 59 is closed| 60 is closed| 
61 is closed| 62 is closed| 63 is closed| 64 is *open*| 65 is closed| 
66 is closed| 67 is closed| 68 is closed| 69 is closed| 70 is closed| 
71 is closed| 72 is closed| 73 is closed| 74 is closed| 75 is closed| 
76 is closed| 77 is closed| 78 is closed| 79 is closed| 80 is closed| 
81 is *open*| 82 is closed| 83 is closed| 84 is closed| 85 is closed| 
86 is closed| 87 is closed| 88 is closed| 89 is closed| 90 is closed| 
91 is closed| 92 is closed| 93 is closed| 94 is closed| 95 is closed| 
96 is closed| 97 is closed| 98 is closed| 99 is closed|100 is *open*|
```


## Haskell

### Unoptimized

```mw
data Door
  = Open
  | Closed
  deriving (Eq, Show)

toggle :: Door -> Door
toggle Open = Closed
toggle Closed = Open

toggleEvery :: Int -> [Door] -> [Door]
toggleEvery k = zipWith toggleK [1 ..]
  where
    toggleK n door
      | n `mod` k == 0 = toggle door
      | otherwise = door

run :: Int -> [Door]
run n = foldr toggleEvery (replicate n Closed) [1 .. n]

main :: IO ()
main = print $ filter ((== Open) . snd) $ zip [1 ..] (run 100)
```

**Output:**

```
[(1,Open),(4,Open),(9,Open),(16,Open),(25,Open),(36,Open),(49,Open),(64,Open),(81,Open),(100,Open)]
```

#### One liner (unoptimized)

```mw
run n = findIndices odd $ foldr toggleEvery (replicate n 0) [0..n] where toggleEvery k =  zipWith (+) $ cycle $ 1 : replicate k 0
```

#### Without toggling doors

```mw
isDoorOpen :: Integral a => a -> Bool
-- In Haskell, we are too lazy to open and close doors. Instead we
-- count how many times we would have toggled them, and then check if
-- that number is odd.
isDoorOpen doorNumber = odd numToggles
  where numToggles = length [ 1 | x <- [1..doorNumber], doorNumber `rem` x == 0]

main = do
  print $ "Open doors are " ++ show [x | x <- [0..100], isDoorOpen x]
```

### Optimized

(without using square roots)

```mw
gate :: Eq a => [a] -> [a] -> [Door]
gate (x:xs) (y:ys) | x == y  =  Open   : gate xs ys
gate (x:xs) ys               =  Closed : gate xs ys
gate []     _                =  []

run n = gate [1..n] [k*k | k <- [1..]]
```

#### One liner (optimized)

Alternatively, returning a list of all open gates, it's a one-liner:

```mw
run n = takeWhile (< n) [k*k | k <- [1..]]
```


## Haxe

### Unoptimised

```mw
class Main
{
    static public function main()
    {
        findOpenDoors( 100 );
    }

    static function findOpenDoors( n : Int )
    {
        var door = [];
        for( i in 0...n + 1 ){ door[ i ] = false; }
        for( i in 1...n + 1 ){
            var j = i;
            while( j <= n ){ 
                door[ j ] = ! door[ j ];
                j += i;
            }
        }
        for( i in 1...n + 1 ){
            if( door[ i ] ){ Sys.print( ' $i' ); }
        }
    }
}
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```

### Optimised

```mw
class RosettaDemo
{
    static public function main()
    {
        findOpenLockers(100);
    }

    static function findOpenLockers(n : Int)
    {
        var i = 1;

        while((i*i) <= n)
        {
            Sys.println(i*i);
            i++;
        }
    }
}
```


## HicEst

Unoptimized

```mw
REAL :: n=100, open=1, door(n)

door = 1 - open ! = closed
DO i = 1, n
  DO j = i, n, i
    door(j) = open - door(j)
  ENDDO
ENDDO
DLG(Text=door, TItle=SUM(door)//" doors open")
```

Optimized

```mw
door = 1 - open ! = closed
DO i = 1, n^0.5
  door(i*i) = open
ENDDO
DLG(Text=door, TItle=SUM(door)//" doors open")
```


## Hobbes

The 100 doors problem reduces to finding perfect squares from 1 to 100, since only doors at perfect square positions remain open.

```mw
isqrt n = floor(sqrt(n + 0.0))

isPerfectSquare n = isqrt(n) * isqrt(n) == n

[n | n <- [1..100], isPerfectSquare(n)]
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## HolyC

Translation of

:

C

```mw
U8 is_open[100];
U8 pass = 0, door = 0;

/* do the 100 passes */
for (pass = 0; pass < 100; ++pass)
  for (door = pass; door < 100; door += pass + 1)
    is_open[door] = !is_open[door];

/* output the result */
for (door = 0; door < 100; ++door)
  if (is_open[door])
    Print("Door #%d is open.\n", door + 1);
  else
    Print("Door #%d is closed.\n", door + 1);
```


## Hoon

```mw
|^
=/  doors=(list ?)  (reap 100 %.n)
=/  passes=(list (list ?))  (turn (gulf 1 100) pass-n)
|-
?~  passes  doors
$(doors (toggle doors i.passes), passes t.passes)
++  pass-n
  |=  n=@ud
  (turn (gulf 1 100) |=(k=@ud =((mod k n) 0)))
++  toggle
  |=  [a=(list ?) b=(list ?)]
  =|  c=(list ?)
  |-
  ?:  |(?=(~ a) ?=(~ b))  (flop c)
  $(a t.a, b t.b, c [=((mix i.a i.b) 1) c])
--
```


## Huginn

```mw
#! /bin/sh
exec huginn --no-argv -E "${0}"
#! huginn

import Algorithms as algo;

main() {
        doorCount = 100;
        doors = [].resize( doorCount, false );

        for ( pass : algo.range( doorCount ) ) {
                i = 0;
                step = pass + 1;
                while ( i < doorCount ) {
                        doors[i] = ! doors[i];
                        i += step;
                }
        }

        for ( i : algo.range( doorCount ) ) {
                if ( doors[i] ) {
                        print( "door {} is open\n".format( i ) );
                }
        }
        return ( 0 );
}
```


## Hy

Translation of

:

Coco

```mw
(setv doors (* [False] 100))

(for [pass (range (len doors))]
  (for [i (range pass (len doors) (inc pass))]
    (assoc doors i (not (get doors i)))))

(for [i (range (len doors))]
  (print (.format "Door {} is {}."
    (inc i)
    (if (get doors i) "open" "closed"))))
```


## I

```mw
software {
	var doors = len(100)
	
	for pass over [1, 100]
		var door = pass - 1
		loop door < len(doors) {
			doors[door] = doors[door]/0
			door += pass
		}
	end
	
	for door,isopen in doors
		if isopen
			print("Door ",door+1,": open")
		end
	end
	print("All other doors are closed")
}
```
