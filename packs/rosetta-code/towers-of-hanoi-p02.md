---
title: "Towers of Hanoi (part 2/5)"
source: https://rosettacode.org/wiki/Towers_of_Hanoi
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/5
---

## Bruijn

Translation of

:

Python

```mw
:import std/Combinator .
:import std/Number .
:import std/String .

hanoi y [[[[=?2 empty go]]]]
	go [(4 --3 2 0) ++ str ++ (4 --3 0 1)] ((+6) - 1 - 0)
		str "Move " ++ disk ++ " from " ++ source ++ " to " ++ destination ++ "\n"
			disk number→string 3
			source number→string 2
			destination number→string 1
```


## C

```mw
#include <stdio.h>

void move(int n, int from, int via, int to)
{
  if (n > 1) {
    move(n - 1, from, to, via);
    printf("Move disk from pole %d to pole %d\n", from, to);
    move(n - 1, via, from, to);
  } else {
    printf("Move disk from pole %d to pole %d\n", from, to);
  }
}
int main()
{
  move(4, 1,2,3);
  return 0;
}
```

Animate it for fun:

```mw
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct { int *x, n; } tower;
tower *new_tower(int cap)
{
	tower *t = calloc(1, sizeof(tower) + sizeof(int) * cap);
	t->x = (int*)(t + 1);
	return t;
}

tower *t[3];
int height;

void text(int y, int i, int d, const char *s)
{
	printf("\033[%d;%dH", height - y + 1, (height + 1) * (2 * i + 1) - d);
	while (d--) printf("%s", s);
}

void add_disk(int i, int d)
{
	t[i]->x[t[i]->n++] = d;
	text(t[i]->n, i, d, "==");

	usleep(100000);
	fflush(stdout);
}

int remove_disk(int i)
{
	int d = t[i]->x[--t[i]->n];
	text(t[i]->n + 1, i, d, "  ");
	return d;
}

void move(int n, int from, int to, int via)
{
	if (!n) return;

	move(n - 1, from, via, to);
	add_disk(to, remove_disk(from));
	move(n - 1, via, to, from);
}

int main(int c, char *v[])
{
	puts("\033[H\033[J");

	if (c <= 1 || (height = atoi(v[1])) <= 0)
		height = 8;
	for (c = 0; c < 3; c++)	 t[c] = new_tower(height);
	for (c = height; c; c--) add_disk(0, c);

	move(height, 0, 2, 1);

	text(1, 0, 1, "\n");
	return 0;
}
```


## C

```mw
public  void move(int n, int from, int to, int via) {
   if (n == 1) {
     System.Console.WriteLine("Move disk from pole " + from + " to pole " + to);
   } else {
     move(n - 1, from, via, to);
     move(1, from, to, via);
     move(n - 1, via, to, from);
   }
 }
```


## C++

Works with

:

g++

```mw
void move(int n, int from, int to, int via) {
  if (n == 1) {
    std::cout << "Move disk from pole " << from << " to pole " << to << std::endl;
  } else {
    move(n - 1, from, via, to);
    move(1, from, to, via);
    move(n - 1, via, to, from);
  }
}
```


## Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

Translation of

:

FreeBASIC

```mw
100 cls
110 print "Three disks" : print
120 hanoi(3,1,2,3)
130 print chr$(10)"Four disks" chr$(10)
140 hanoi(4,1,2,3)
150 print : print "Towers of Hanoi puzzle completed!"
160 end
170 sub hanoi(n,desde,hasta,via)
180   if n > 0 then
190     hanoi(n-1,desde,via,hasta)
200     print "Move disk " n "from pole " desde "to pole " hasta
210     hanoi(n-1,via,hasta,desde)
220   endif
230 end sub
```


## Clojure

### Side-Effecting Solution

```mw
(defn towers-of-hanoi [n from to via]
  (when (pos? n)
    (towers-of-hanoi (dec n) from via to)
    (printf "Move from %s to %s\n" from to)
    (recur (dec n) via to from)))
```

### Lazy Solution

```mw
(defn towers-of-hanoi [n from to via]
  (when (pos? n)
    (lazy-cat (towers-of-hanoi (dec n) from via to)
              (cons [from '-> to]
                    (towers-of-hanoi (dec n) via to from)))))
```


## CLU

```mw
move = proc (n, from, via, to: int)
    po: stream := stream$primary_output()
    if n > 0 then
        move(n-1, from, to, via)
        stream$putl(po, "Move disk from pole "
                     || int$unparse(from)
                     || " to pole "
                     || int$unparse(to))
        move(n-1, via, from, to)
    end
end move

start_up = proc ()
    move(4, 1, 2, 3)
end start_up
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## COBOL

Translation of

:

C

Works with

:

OpenCOBOL

version 2.0

```mw
       >>SOURCE FREE
IDENTIFICATION DIVISION.
PROGRAM-ID. towers-of-hanoi.

PROCEDURE DIVISION.
    CALL "move-disk" USING 4, 1, 2, 3
    .
END PROGRAM towers-of-hanoi.

IDENTIFICATION DIVISION.
PROGRAM-ID. move-disk RECURSIVE.

DATA DIVISION.
LINKAGE SECTION.
01  n                         PIC 9 USAGE COMP.
01  from-pole                 PIC 9 USAGE COMP.
01  to-pole                   PIC 9 USAGE COMP.
01  via-pole                  PIC 9 USAGE COMP.

PROCEDURE DIVISION USING n, from-pole, to-pole, via-pole.
    IF n > 0
       SUBTRACT 1 FROM n
       CALL "move-disk" USING CONTENT n, from-pole, via-pole, to-pole
       DISPLAY "Move disk from pole " from-pole " to pole " to-pole
       CALL "move-disk" USING CONTENT n, via-pole, to-pole, from-pole
    END-IF
    .
END PROGRAM move-disk.
```

Template:Number of disks also

```mw
 
IDENTIFICATION DIVISION.
PROGRAM-ID. towers-of-hanoi.
 
PROCEDURE DIVISION.
    CALL "move-disk" USING 4, 1, 2, 3
    .
END PROGRAM towers-of-hanoi.
 
IDENTIFICATION DIVISION.
PROGRAM-ID. move-disk RECURSIVE.
 
DATA DIVISION.
LINKAGE SECTION.
01  n                         PIC 9 USAGE COMP.
01  from-pole                 PIC 9 USAGE COMP.
01  to-pole                   PIC 9 USAGE COMP.
01  via-pole                  PIC 9 USAGE COMP.
 
PROCEDURE DIVISION USING n, from-pole, to-pole, via-pole.
    IF n > 0
       SUBTRACT 1 FROM n
       CALL "move-disk" USING CONTENT n, from-pole, via-pole, to-pole
       ADD 1 TO n
       DISPLAY "Move disk number "n " from pole " from-pole " to pole " to-pole
       SUBTRACT 1 FROM n
       CALL "move-disk" USING CONTENT n, via-pole, to-pole, from-pole
    END-IF
    .
END PROGRAM move-disk.
```

### ANSI-74 solution

Early versions of COBOL did not have recursion. There are no locally-scoped variables and the call of a procedure does not have to use a stack to save return state. Recursion would cause undefined results. It is therefore necessary to use an iterative algorithm. This solution is an adaptation of Kolar's Hanoi Tower algorithm no. 1.

Works with

:

CIS COBOL

version 4.2

Works with

:

GnuCOBOL

version 3.0-rc1.0

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID. ITERATIVE-TOWERS-OF-HANOI.
       AUTHOR. SOREN ROUG.
       DATE-WRITTEN. 2019-06-28.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. LINUX.
       OBJECT-COMPUTER. KAYPRO4.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77  NUM-DISKS                   PIC 9 VALUE 4.
       77  N1                          PIC 9 COMP.
       77  N2                          PIC 9 COMP.
       77  FROM-POLE                   PIC 9 COMP.
       77  TO-POLE                     PIC 9 COMP.
       77  VIA-POLE                    PIC 9 COMP.
       77  FP-TMP                      PIC 9 COMP.
       77  TO-TMP                      PIC 9 COMP.
       77  P-TMP                       PIC 9 COMP.
       77  TMP-P                       PIC 9 COMP.
       77  I                           PIC 9 COMP.
       77  DIV                         PIC 9 COMP.
       01  STACKNUMS.
           05  NUMSET OCCURS 3 TIMES.
               10  DNUM                PIC 9 COMP.
       01  GAMESET.
           05  POLES OCCURS 3 TIMES.
               10  STACK OCCURS 10 TIMES.
                   15  POLE            PIC 9 USAGE COMP.

       PROCEDURE DIVISION.
       HANOI.
           DISPLAY "TOWERS OF HANOI PUZZLE WITH ", NUM-DISKS, " DISKS.".
           ADD NUM-DISKS, 1 GIVING N1.
           ADD NUM-DISKS, 2 GIVING N2.
           MOVE 1 TO DNUM (1).
           MOVE N1 TO DNUM (2), DNUM (3).
           MOVE N1 TO POLE (1, N1), POLE (2, N1), POLE (3, N1).
           MOVE 1 TO POLE (1, N2).
           MOVE 2 TO POLE (2, N2).
           MOVE 3 TO POLE (3, N2).
           MOVE 1 TO I.
           PERFORM INIT-PUZZLE UNTIL I = N1.
           MOVE 1 TO FROM-POLE.
           DIVIDE 2 INTO NUM-DISKS GIVING DIV.
           MULTIPLY 2 BY DIV.
           IF DIV NOT = NUM-DISKS PERFORM INITODD ELSE PERFORM INITEVEN.
           PERFORM MOVE-DISK UNTIL DNUM (3) NOT > 1.
           DISPLAY "TOWERS OF HANOI PUZZLE COMPLETED!".
           STOP RUN.
       INIT-PUZZLE.
           MOVE I TO POLE (1, I).
           MOVE 0 TO POLE (2, I), POLE (3, I).
           ADD 1 TO I.
       INITEVEN.
           MOVE 2 TO TO-POLE.
           MOVE 3 TO VIA-POLE.
       INITODD.
           MOVE 3 TO TO-POLE.
           MOVE 2 TO VIA-POLE.
       MOVE-DISK.
           MOVE DNUM (FROM-POLE) TO FP-TMP.
           MOVE POLE (FROM-POLE, FP-TMP) TO I.
           DISPLAY "MOVE DISK FROM ", POLE (FROM-POLE, N2),
               " TO ", POLE (TO-POLE, N2).
           ADD 1 TO DNUM (FROM-POLE).
           MOVE VIA-POLE TO TMP-P.
           SUBTRACT 1 FROM DNUM (TO-POLE).
           MOVE DNUM (TO-POLE) TO TO-TMP.
           MOVE I TO POLE (TO-POLE, TO-TMP).
           DIVIDE 2 INTO I GIVING DIV.
           MULTIPLY 2 BY DIV.
           IF I NOT = DIV PERFORM MOVE-TO-VIA ELSE
               PERFORM MOVE-FROM-VIA.
       MOVE-TO-VIA.
           MOVE TO-POLE TO VIA-POLE.
           MOVE DNUM (FROM-POLE) TO FP-TMP.
           MOVE DNUM (TMP-P) TO P-TMP.
           IF POLE (FROM-POLE, FP-TMP) > POLE (TMP-P, P-TMP)
               PERFORM MOVE-FROM-TO
           ELSE MOVE TMP-P TO TO-POLE.
       MOVE-FROM-TO.
           MOVE FROM-POLE TO TO-POLE.
           MOVE TMP-P TO FROM-POLE.
           MOVE DNUM (FROM-POLE) TO FP-TMP.
           MOVE DNUM (TMP-P) TO P-TMP.
       MOVE-FROM-VIA.
           MOVE FROM-POLE TO VIA-POLE.
           MOVE TMP-P TO FROM-POLE.
```


## CoffeeScript

```mw
hanoi = (ndisks, start_peg=1, end_peg=3) ->
  if ndisks
    staging_peg = 1 + 2 + 3 - start_peg - end_peg
    hanoi(ndisks-1, start_peg, staging_peg)
    console.log "Move disk #{ndisks} from peg #{start_peg} to #{end_peg}"
    hanoi(ndisks-1, staging_peg, end_peg)
 
hanoi(4)
```


## Common Lisp

```mw
(defun move (n from to via)
  (cond ((= n 1)
         (format t "Move from ~A to ~A.~%" from to))
        (t
         (move (- n 1) from via to)
         (format t "Move from ~A to ~A.~%" from to)
         (move (- n 1) via to from))))
```


## Crystal

Translation of

:

Common Lisp

– ☝

```mw
def move (n, from, to, via)
  if n == 1
    printf "Move from %s to %s.\n", from, to
  else
    move n-1, from, via, to
    printf "Move from %s to %s.\n", from, to
    move n-1, via, to, from
  end
end

move 3, "1", "3", "2"
```

**Output:**

```
Move from 1 to 3.
Move from 1 to 2.
Move from 3 to 2.
Move from 1 to 3.
Move from 2 to 1.
Move from 2 to 3.
Move from 1 to 3.
```


## D

### Recursive Version

```mw
import std.stdio;

void hanoi(in int n, in char from, in char to, in char via) {
    if (n > 0) {
        hanoi(n - 1, from, via, to);
        writefln("Move disk %d from %s to %s", n, from, to);
        hanoi(n - 1, via, to, from);
    }
}

void main() {
    hanoi(3, 'L', 'M', 'R');
}
```

**Output:**

```
Move disk 1 from L to M
Move disk 2 from L to R
Move disk 1 from M to R
Move disk 3 from L to M
Move disk 1 from R to L
Move disk 2 from R to M
Move disk 1 from L to M
```

### Fast Iterative Version

See: The shortest and "mysterious" TH algorithm

```mw
// Code found and then improved by Glenn C. Rhoads,
// then some more by M. Kolar (2000).
void main(in string[] args) {
    import core.stdc.stdio, std.conv, std.typetuple;

    immutable size_t n = (args.length > 1) ? args[1].to!size_t : 3;
    size_t[3] p = [(1 << n) - 1, 0, 0];

    // Show the start configuration of the pegs.
    '|'.putchar;
    foreach_reverse (immutable i; 1 .. n + 1)
        printf(" %lu", i);
    "\n|\n|".puts;

    foreach (immutable size_t x; 1 .. (1 << n)) {
        {
            immutable size_t i1 = x & (x - 1);
            immutable size_t fr = (i1 + i1 / 3) & 3;
            immutable size_t i2 = (x | (x - 1)) + 1;
            immutable size_t to = (i2 + i2 / 3) & 3;

            size_t j = 1;
            for (size_t w = x; !(w & 1); w >>= 1, j <<= 1) {}

            // Now j is not the number of the disk to move,
            // it contains the single bit to be moved:
            p[fr] &= ~j;
            p[to] |= j;
        }

        // Show the current configuration of pegs.
        foreach (immutable size_t k; TypeTuple!(0, 1, 2)) {
            "\n|".printf;
            size_t j = 1 << n;
            foreach_reverse (immutable size_t w; 1 .. n + 1) {
                j >>= 1;
                if (j & p[k])
                    printf(" %zd", w);
            }
        }
        '\n'.putchar;
    }
}
```

**Output:**

```
| 3 2 1
|
|

| 3 2
|
| 1

| 3
| 2
| 1

| 3
| 2 1
|

|
| 2 1
| 3

| 1
| 2
| 3

| 1
|
| 3 2

|
|
| 3 2 1
```


## Dart

```mw
main() { 
  moveit(from,to) {
    print("move ${from} ---> ${to}");
  }

  hanoi(height,toPole,fromPole,usePole) {
    if (height>0) {
      hanoi(height-1,usePole,fromPole,toPole);  
      moveit(fromPole,toPole);
      hanoi(height-1,toPole,usePole,fromPole);
    }
  }

  hanoi(3,3,1,2);
}
```

The same as above, with optional static type annotations and styled according to http://www.dartlang.org/articles/style-guide/

```mw
main() {
  String say(String from, String to) => "$from ---> $to"; 

  hanoi(int height, int toPole, int fromPole, int usePole) {
    if (height > 0) {
      hanoi(height - 1, usePole, fromPole, toPole);  
      print(say(fromPole.toString(), toPole.toString()));
      hanoi(height - 1, toPole, usePole, fromPole);
    }
  }

  hanoi(3, 3, 1, 2);
}
```

**Output:**

```
move 1 ---> 3
move 1 ---> 2
move 3 ---> 2
move 1 ---> 3
move 2 ---> 1
move 2 ---> 3
move 1 ---> 3
```


## Dc

From Here

```
 [ # move(from, to)
    n           # print from
    [ --> ]n    # print " --> "
    p           # print to\n
    sw          # p doesn't pop, so get rid of the value
 ]sm
 
 [ # init(n)
    sw          # tuck n away temporarily
    9           # sentinel as bottom of stack
    lw          # bring n back
    1           # "from" tower's label
    3           # "to" tower's label
    0           # processed marker
 ]si
 
 [ # Move()
    lt          # push to
    lf          # push from
    lmx         # call move(from, to)
 ]sM
 
 [ # code block <d>
    ln          # push n
    lf          # push from
    lt          # push to
    1           # push processed marker 1
    ln          # push n
    1           # push 1
    -           # n - 1
    lf          # push from
    ll          # push left
    0           # push processed marker 0
 ]sd
 
 [ # code block <e>
    ln          # push n
    1           # push 1
    -           # n - 1
    ll          # push left
    lt          # push to
    0           # push processed marker 0
 ]se
 
 [ # code block <x>
    ln 1 =M
    ln 1 !=d
 ]sx
 
 [ # code block <y>
    lMx
    lex
 ]sy
 
 [ # quit()
    q           # exit the program
 ]sq
 
 [ # run()
    d 9 =q      # if stack empty, quit()
    sp          # processed
    st          # to
    sf          # from
    sn          # n
    6           #
    lf          #
    -           #
    lt          #
    -           # 6 - from - to
    sl          #
    lp 0 =x     #
    lp 0 !=y    #
    lrx         # loop
 ]sr
 
 5lix # init(n)
 lrx # run()
```


## Delphi

See Pascal.


## Draco

```mw
proc move(byte n, src, via, dest) void:
    if n>0 then
        move(n-1, src, dest, via);
        writeln("Move disk from pole ",src," to pole ",dest);
        move(n-1, via, src, dest)
    fi
corp

proc nonrec main() void: 
    move(4, 1, 2, 3) 
corp
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 2 to pole 1
Move disk from pole 3 to pole 1
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
```


## Dyalect

Translation of

:

Swift

```mw
func hanoi(n, a, b, c) {
    if n > 0 {
        hanoi(n - 1, a, c, b)
        print("Move disk from \(a) to \(c)")
        hanoi(n - 1, b, a, c)
    }
}
 
hanoi(4, "A", "B", "C")
```

**Output:**

```
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from A to B
Move disk from C to A
Move disk from C to B
Move disk from A to B
Move disk from A to C
Move disk from B to C
Move disk from B to A
Move disk from C to A
Move disk from B to C
Move disk from A to B
Move disk from A to C
Move disk from B to C
```


## E

```mw
def move(out, n, fromPeg, toPeg, viaPeg) {
    if (n.aboveZero()) {
        move(out, n.previous(), fromPeg, viaPeg, toPeg)
        out.println(`Move disk $n from $fromPeg to $toPeg.`)
        move(out, n.previous(), viaPeg, toPeg, fromPeg)
    }
}

move(stdout, 4, def left {}, def right {}, def middle {})
```


## EasyLang

```mw
proc hanoi n src dst aux .
   if n >= 1
      hanoi n - 1 src aux dst
      print "Move " & src & " to " & dst
      hanoi n - 1 aux dst src
   .
.
hanoi 4 1 2 3
```

**Output:**

```
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 3 to 1
Move 2 to 1
Move 3 to 2
Move 1 to 3
Move 1 to 2
Move 3 to 2
```


## EDSAC order code

The Wikipedia article on EDSAC says "recursive calls were forbidden", and this is true if the standard "Wheeler jump" is used. In the Wheeler jump, the caller (in effect) passes the return address to the subroutine, which uses that address to manufacture a "link order", i.e. a jump back to the caller. This link order is normally stored at a fixed location in the subroutine, so if the subroutine were to call itself then the original link order would be overwritten and lost. However, it is easy enough to make a subroutine save its link orders in a stack, so that it can be called recursively, as the Rosetta Code task requires.

The program has a maximum of 9 discs, so as to simplify the printout of the disc numbers. Discs are numbered 1, 2, 3, ... in increasing order of size. The program could be speeded up by shortening the messages, which at present take up most of the runtime.

```mw
[Towers of Hanoi task for Rosetta Code.]
[EDSAC program, Initial Orders 2.]

            T100K   [load program at location 100 (arbitrary)]
            GK
[Number of discs, in the address field]
      [0]   P3F     [<--- edit here, value 1..9]
[Letters to represent the rods]
      [1]   LF      [left]
      [2]   CF      [centre]
      [3]   RF      [right]

[Main routine. Enter with acc = 0]
      [4]   T1F     [1F := 0]
      [5]   A5@     [initialize recursive subroutine]
            G104@
            A@      [number of discs]
            T1F     [pass to subroutines]
            A1@     [source rod]
            T4F     [pass to subroutines]
            A3@     [target rod]
            T5F     [pass to subroutines]
     [13]   A13@    [call subroutine to write header ]
            G18@
     [15]   A15@    [call recursive subroutine to write moves ]
            G104@
            ZF      [stop]

[Subroutine to write a header]
[Input:  1F = number of discs (in the address field)]
        [4F = letter for starting rod]
        [5F = letter for ending rod]
[Output: None. 1F, 4F, 5F must be preserved.]
     [18]   A3F     [plant return link as usual]
            T35@
            A1F     [number of discs]
            L512F   [shift 11 left to make output char]
            T39@    [plant in message]
            A4F     [starting rod]
            T53@    [plant in message]
            A5F     [ending rod]
            T58@    [plant in message]
            A36@    [O order for first char of message]
            E30@    [skip next order (code for 'O' is positive)]
     [29]   A37@    [restore acc after test below]
     [30]   U31@    [plant order to write next character]
     [31]   OF      [(planted) write next character]
            A2F     [inc address in previous order]
            S37@    [finished yet?]
            G29@    [if not, loop back]
     [35]   ZF      [(planted) exit with acc = 0]
     [36]   O38@    [O order for start of message]
     [37]   O61@    [O order for exclusive end of message]
     [38]   #F
     [39]   PFK2048F!FDFIFSFCFSF!FFFRFOFMF!F
     [53]   PF!FTFOF!F
     [58]   PF@F&F
     [61]

[Subroutine to write a move of one disc.]
[Input:  1F = disc number 1..9 (in the address field)]
        [4F = letter for source rod]
        [5F = letter for target rod]
[Output: None. 1F, 4F, 5F must be preserved.]
[Condensed to save space; very similar to previous subroutine.]
     [61]   A3FT78@A1FL512FT88@ A4FT96@A5FT101@A79@E73@
     [72]   A80@
     [73]   U74@
     [74]   OFA2FS80@G72@
     [78]   ZF      [(planted) exit with acc = 0]
     [79]   O81@
     [80]   O104@
     [81]   K2048FMFOFVFEF!F#F
     [88]   PFK2048F!FFFRFOFMF!F
     [96]   PF!FTFOF!F
    [101]   PF@F&F
    [104]

[Recursive subroutine to move discs 1..n, where 1 <= n <= 9.]
[Call with n = 0 to initialize.]
[Input:  1F = n (in the address field)]
        [4F = letter for source rod]
        [5F = letter for target rod]
[Output: None. 1F, 4F, 5F must be preserved.]
    [104]   A3F     [plant link as usual ]
            T167@
[The link will be saved in a stack if recursive calls are required.]
            S1F     [load -n]
            G115@   [jump if n > 0]
[Here if n = 0. Initialize; no recursive calls.]
            A169@   [initialize push order to start of stack]
            T122@
            A1@     [find total of the codes for the rod letters]
            A2@
            A3@
            T168@   [store for future use]
            E167@   [jump to link]
[Here with acc = -n in address field]
    [115]   A2F     [add 1]
            G120@   [jump if n > 1]
[Here if n = 1. Just write the move; no recursive calls.]
    [117]   A117@   [call write subroutine]
            G61@
            E167@   [jump to link]
[Here if n > 1. Recursive calls are required.]
    [120]   TF      [clear acc]
            A167@   [load link order]
    [122]   TF      [(planted) push link order onto stack]
            A122@   [inc address in previous order]
            A2F
            T122@
[First recursive call. Modify parameters 1F and 5F; 4F stays the same]
            A1F     [load n]
            S2F     [make n - 1]
            T1F     [pass as parameter]
            A168@   [get 3rd rod, neither source nor target]
            S4F
            S5F
            T5F
    [133]   A133@   [recursive call]
            G104@
[Returned, restore parameters]
            A1F
            A2F
            T1F
            A168@
            S4F
            S5F
            T5F
[Write move of largest disc]
    [142]   A142@
            G61@
[Second recursive call. Modify parameters 1F and 4F; 5F stays the same]
[Condensed to save space; very similar to first recursice call.]
            A1FS2FT1FA168@S4FS5FT4F
    [151]   A151@G104@A1FA2FT1FA168@S4FS5FT4F
[Pop return link off stack]
            A122@   [dec address in push order]
            S2F
            U122@
            A170@   [make A order with same address]
            T165@   [plant in code]
    [165]   AF      [(planted) pop return link from stack]
            T167@   [plant in code]
    [167]   ZF      [(planted) return to caller]
[Constants]
    [168]   PF      [(planted) sum of letters for rods]
    [169]   T171@   [T order for start of stack]
    [170]   MF      [add to T order to make A order, same address]
[Stack: placed at end of program, grows into free space.]
    [171]
            E4Z     [define entry point]
            PF      [acc = 0 on entry]
[end]
```

**Output:**

```
3 DISCS FROM L TO R
MOVE 1 FROM L TO R
MOVE 2 FROM L TO C
MOVE 1 FROM R TO C
MOVE 3 FROM L TO R
MOVE 1 FROM C TO L
MOVE 2 FROM C TO R
MOVE 1 FROM L TO R
```


## Eiffel

```mw
class
	APPLICATION

create
	make

feature {NONE} -- Initialization

	make
		do
			move (4, "A", "B", "C")
		end

feature -- Towers of Hanoi

	move (n: INTEGER; frm, to, via: STRING)
		require
			n > 0
	    do
			if n = 1 then
    			print ("Move disk from pole " + frm + " to pole " + to + "%N")
    		else
    			move (n - 1, frm, via, to)
    			move (1, frm, to, via)
    			move (n - 1, via, to, frm)
	        end
	    end
end
```


## Ela

Translation of

:

Haskell

```mw
open monad io
:::IO

//Functional approach
hanoi 0 _ _ _ = []
hanoi n a b c = hanoi (n - 1) a c b ++ [(a,b)] ++ hanoi (n - 1) c b a

hanoiIO n = mapM_ f $ hanoi n 1 2 3 where
  f (x,y) = putStrLn $ "Move " ++ show x ++ " to " ++ show y

//Imperative approach using IO monad
hanoiM n = hanoiM' n 1 2 3 where
  hanoiM' 0 _ _ _ = return ()
  hanoiM' n a b c = do
    hanoiM' (n - 1) a c b
    putStrLn $ "Move " ++ show a ++ " to " ++ show b
    hanoiM' (n - 1) c b a
```


## Elena

ELENA 6.x :

```mw
move = (n,from,to,via)
{
    if (n == 1)
    {
        Console.printLine("Move disk from pole ",from," to pole ",to)
    }
    else
    {
        move(n-1,from,via,to);
        move(1,from,to,via);
        move(n-1,via,to,from)
    }
};
```


## Elixir

```mw
defmodule RC do
  def hanoi(n) when 0<n and n<10, do: hanoi(n, 1, 2, 3)
  
  defp hanoi(1, f, _, t), do: move(f, t)
  defp hanoi(n, f, u, t) do
    hanoi(n-1, f, t, u)
    move(f, t)
    hanoi(n-1, u, f, t)
  end
  
  defp move(f, t), do: IO.puts "Move disk from #{f} to #{t}"
end

RC.hanoi(3)
```

**Output:**

```
Move disk from 1 to 3
Move disk from 1 to 2
Move disk from 3 to 2
Move disk from 1 to 3
Move disk from 2 to 1
Move disk from 2 to 3
Move disk from 1 to 3
```


## Emacs Lisp

Translation of

:

Common Lisp

```mw
(defun move (n from to via)
  (if (= n 1)
      (message "Move from %S to %S" from to)
    (move (- n 1) from via to)
    (message "Move from %S to %S" from to)
    (move (- n 1) via to from)))
```


## EMal

Translation of

:

C#

```mw
fun move ← void by int n, int from, int to, int via
  if n æ 1
    writeLine("Move disk from pole " + from + " to pole " + to)
    return
  end
  move(n - 1, from, via, to)
  move(1, from, to, via)
  move(n - 1, via, to, from)
end
move(3, 1, 2, 3)
```

**Output:**

```
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2
```


## Erlang

```mw
move(1, F, T, _V) -> 
  io:format("Move from ~p to ~p~n", [F, T]);
move(N, F, T, V) -> 
  move(N-1, F, V, T), 
  move(1  , F, T, V),
  move(N-1, V, T, F).
```


## ERRE

```mw
!-----------------------------------------------------------
! HANOI.R : solve tower of Hanoi puzzle using a recursive 
! modified algorithm.
!-----------------------------------------------------------

PROGRAM HANOI

!$INTEGER

!VAR I,J,MOSSE,NUMBER

PROCEDURE PRINTMOVE
  LOCAL SOURCE$,DEST$
  MOSSE=MOSSE+1
  CASE I OF
     1-> SOURCE$="Left" END ->
     2-> SOURCE$="Center" END ->
     3-> SOURCE$="Right" END ->
  END CASE
  CASE J OF
     1-> DEST$="Left" END ->
     2-> DEST$="Center" END ->
     3-> DEST$="Right" END ->
  END CASE
  PRINT("I move a disk from ";SOURCE$;" to ";DEST$)
END PROCEDURE

PROCEDURE MOVE
  IF NUMBER<>0 THEN
     NUMBER=NUMBER-1
     J=6-I-J
     MOVE
     J=6-I-J
     PRINTMOVE
     I=6-I-J
     MOVE
     I=6-I-J
     NUMBER=NUMBER+1
  END IF
END PROCEDURE

BEGIN
  MAXNUM=12
  MOSSE=0
  PRINT(CHR$(12);TAB(25);"--- TOWERS OF HANOI ---")
  REPEAT
     PRINT("Number of disks ";)
     INPUT(NUMBER)
  UNTIL NUMBER>1 AND NUMBER<=MAXNUM
  PRINT
  PRINT("For ";NUMBER;"disks the total number of moves is";2^NUMBER-1)
  I=1  ! number of source pole
  J=3  ! number of destination pole
  MOVE
END PROGRAM
```

**Output:**

```
                        --- TOWER OF HANOI ---
Number of disks ? 3

For  3 disks the total number of moves is 7
I move a disk from Left to Right
I move a disk from Left to Center
I move a disk from Right to Center
I move a disk from Left to Right
I move a disk from Center to Left
I move a disk from Center to Right
I move a disk from Left to Right
```


## Excel

### LAMBDA (Name Manager)

With the names HANOI and SHOWHANOI bound to the following lambdas in the Excel worksheet Name Manager:

(See LAMBDA: The ultimate Excel worksheet function)

Works with

:

Office 365 Betas 2021

```mw
SHOWHANOI
=LAMBDA(n,
    FILTERP(
        LAMBDA(x, "" <> x)
    )(
        HANOI(n)("left")("right")("mid")
    )
)

HANOI
=LAMBDA(n,
    LAMBDA(l,
        LAMBDA(r,
            LAMBDA(m,
                IF(0 = n,
                    "",
                    LET(
                        next, n - 1,
                        APPEND(
                            APPEND(
                                HANOI(next)(l)(m)(r)
                            )(
                                CONCAT(l, " -> ", r)
                            )
                        )(
                            HANOI(next)(m)(r)(l)
                        )
                    )
                )
            )
        )
    )
)
```

And assuming that these generic lambdas are also bound to the following names in Name Manager:

```mw
APPEND
=LAMBDA(xs,
    LAMBDA(ys,
        LET(
            nx, ROWS(xs),
            rowIndexes, SEQUENCE(nx + ROWS(ys)),
            colIndexes, SEQUENCE(
                1,
                MAX(COLUMNS(xs), COLUMNS(ys))
            ),
            IF(
                rowIndexes <= nx,
                INDEX(xs, rowIndexes, colIndexes),
                INDEX(ys, rowIndexes - nx, colIndexes)
            )
        )
    )
)

FILTERP
=LAMBDA(p,
    LAMBDA(xs,
        FILTER(xs, p(xs))
    )
)
```

In the output below, the expression in B2 defines an array of strings which additionally populate the following cells.

**Output:**

|   | fx | =SHOWHANOI(A2) |
|---|---|---|
|   | A | B |
| 1 | Disks | Steps |
| 2 | 3 | left -> right |
| 3 |   | left -> mid |
| 4 |   | right -> mid |
| 5 |   | left -> right |
| 6 |   | mid -> left |
| 7 |   | mid -> right |
| 8 |   | left -> right |

### LAMBDA (Self-contained)

This solution provides an implementation in a single formula without requiring any named lambdas in Excel's Name Manager. It uses LET to define a recursive LAMBDA function and expects the number of disks in A2.

```mw
=LET(
   TOH, LAMBDA(TOH, n, from, to, aux,
          IF(n=0, "", VSTACK(
              TOH(TOH, n-1, from, aux, to),
              "Move disk " & n & " from " & from & " to " & to,
              TOH(TOH, n-1, aux, to, from)
          ))
        ),
   ans, TOH(TOH, A2, "A", "C", "B"),
   FILTER(ans, LEN(ans))
 )
```

**Output:**

|   | A | B |
|---|---|---|
| 1 | Disks | Steps |
| 2 | 3 | Move disk 1 from A to C |
| 3 |   | Move disk 2 from A to B |
| 4 |   | Move disk 1 from C to B |
| 5 |   | Move disk 3 from A to C |
| 6 |   | Move disk 1 from B to A |
| 7 |   | Move disk 2 from B to C |
| 8 |   | Move disk 1 from A to C |


## Ezhil

```mw
# (C) 2013 Ezhil Language Project
# Tower of Hanoi – recursive solution

நிரல்பாகம் ஹோனாய்(வட்டுகள், முதல்அச்சு, இறுதிஅச்சு,வட்டு)

  @(வட்டுகள் == 1 ) ஆனால்
     பதிப்பி  “வட்டு ” + str(வட்டு) + “ஐ \t  (” + str(முதல்அச்சு) + “  —> ” +  str(இறுதிஅச்சு)+ “) அச்சிற்கு நகர்த்துக.”
  இல்லை

  @( ["இ", "அ",  "ஆ"]  இல் அச்சு ) ஒவ்வொன்றாக
          @( (முதல்அச்சு != அச்சு)  && (இறுதிஅச்சு  != அச்சு) ) ஆனால்
              நடு = அச்சு
          முடி
  முடி

    # solve problem for n-1 again between src and temp pegs                      
    ஹோனாய்(வட்டுகள்-1,   முதல்அச்சு,நடு,வட்டுகள்-1)

    # move largest disk from src to destination
    ஹோனாய்(1, முதல்அச்சு, இறுதிஅச்சு,வட்டுகள்)

    # solve problem for n-1 again between different pegs
    ஹோனாய்(வட்டுகள்-1, நடு, இறுதிஅச்சு,வட்டுகள்-1)
  முடி
முடி

ஹோனாய்(4,”அ”,”ஆ”,0)
```


## F

```mw
#light
let rec hanoi num start finish =
  match num with
  | 0 -> [ ]
  | _ -> let temp = (6 - start - finish)
         (hanoi (num-1) start temp) @ [ start, finish ] @ (hanoi (num-1) temp finish)

[<EntryPoint>]
let main args =
  (hanoi 4 1 2) |> List.iter (fun pair -> match pair with
                                          | a, b -> printf "Move disc from %A to %A\n" a b)
  0
```


## Factor

```mw
USING: formatting kernel locals math ;
IN: rosettacode.hanoi

: move ( from to -- )
    "%d->%d\n" printf ;
:: hanoi ( n from to other -- )
    n 0 > [
        n 1 - from other to hanoi
        from to move
        n 1 - other to from hanoi
    ] when ;
```

In the REPL:

```
( scratchpad ) 3 1 3 2 hanoi
1->3
1->2
3->2
1->3
2->1
2->3
1->3
```


## FALSE

```mw
["Move disk from "$!\" to "$!\"
"]p:  { to from }
[n;0>[n;1-n: @\ h;! @\ p;! \@ h;! \@ n;1+n:]?]h:  { via to from }
4n:["right"]["middle"]["left"]h;!%%%
```


## Fermat

```mw
Func Hanoi( n, f, t, v ) = 
if n = 0 then 
    !'';
else 
    Hanoi(n - 1, f, v, t); 
    !f;!' -> ';!t;!',   ';
    Hanoi(n - 1, v, t, f)  
fi.
```

**Output:**

```
1 -> 3,   1 -> 2,   3 -> 2,   1 -> 3,   2 -> 1,   2 -> 3,   1 -> 3,   1 -> 2,   3 -> 2,   3 -> 1,   2 -> 1,   3 -> 2,   1 -> 3,   1 -> 2,   3 -> 2,
```


## FOCAL

```mw
01.10 S N=4;S S=1;S V=2;S T=3
01.20 D 2
01.30 Q

02.02 S N(D)=N(D)-1;I (N(D)),2.2,2.04
02.04 S D=D+1
02.06 S N(D)=N(D-1);S S(D)=S(D-1)
02.08 S T(D)=V(D-1);S V(D)=T(D-1)
02.10 D 2
02.12 S D=D-1
02.14 D 3
02.16 S A=S(D);S S(D)=V(D);S V(D)=A
02.18 G 2.02
02.20 D 3

03.10 T %1,"MOVE DISK FROM POLE",S(D)
03.20 T " TO POLE",T(D),!
```

**Output:**

```
MOVE DISK FROM POLE= 1 TO POLE= 2
MOVE DISK FROM POLE= 1 TO POLE= 3
MOVE DISK FROM POLE= 2 TO POLE= 3
MOVE DISK FROM POLE= 1 TO POLE= 2
MOVE DISK FROM POLE= 3 TO POLE= 1
MOVE DISK FROM POLE= 3 TO POLE= 2
MOVE DISK FROM POLE= 1 TO POLE= 2
MOVE DISK FROM POLE= 1 TO POLE= 3
MOVE DISK FROM POLE= 2 TO POLE= 3
MOVE DISK FROM POLE= 2 TO POLE= 1
MOVE DISK FROM POLE= 3 TO POLE= 1
MOVE DISK FROM POLE= 2 TO POLE= 3
MOVE DISK FROM POLE= 1 TO POLE= 2
MOVE DISK FROM POLE= 1 TO POLE= 3
MOVE DISK FROM POLE= 2 TO POLE= 3
```


## Forth

With locals:

```mw
CREATE peg1 ," left "   
CREATE peg2 ," middle " 
CREATE peg3 ," right " 

: .$   COUNT TYPE ;
: MOVE-DISK 
  LOCALS| via to from n | 
  n 1 =
  IF   CR ." Move disk from " from .$ ." to " to .$ 
  ELSE n 1- from via to RECURSE 
       1    from to via RECURSE 
       n 1- via to from RECURSE 
  THEN ;
```

Without locals, executable pegs:

```mw
: left   ." left" ;
: right  ." right" ;
: middle ." middle" ;

: move-disk ( v t f n -- v t f )
  dup 0= if drop exit then
  1-       >R
  rot swap R@ ( t v f n-1 ) recurse
  rot swap
  2dup cr ." Move disk from " execute ."  to " execute
  swap rot R> ( f t v n-1 ) recurse
  swap rot ;
: hanoi ( n -- )
  1 max >R ['] right ['] middle ['] left R> move-disk drop drop drop ;
```


## Fortran

Works with

:

Fortran

version 90 and later

```mw
PROGRAM TOWER
                             
  CALL Move(4, 1, 2, 3)
                
CONTAINS

  RECURSIVE SUBROUTINE Move(ndisks, from, to, via)
    INTEGER, INTENT (IN) :: ndisks, from, to, via
   
    IF (ndisks == 1) THEN
       WRITE(*, "(A,I1,A,I1)") "Move disk from pole ", from, " to pole ", to
    ELSE
       CALL Move(ndisks-1, from, via, to)
       CALL Move(1, from, to, via)
       CALL Move(ndisks-1, via, to, from)
    END IF
  END SUBROUTINE Move

END PROGRAM TOWER
```

```
More informative version 
```

```mw
!	This is a nice alternative to the usual recursive Hanoi solutions. It runs about 10x
!       faster than a well crafted recursive solution for 30 disks.
      SUBROUTINE olives(Numdisk)
!>  This is an implementation of "Olive's Algorithm"
!!  The “simpler” algorithm where the smallest disk moves circularly every second
!!  move is attributed to Raoul Olive, the nephew of Edouard Lucas, the inventor of the
!!  Towers of Hanoi puzzle. We alternately move disk one in it's established direction
!!  Then we move the one of the 'non-one' disks, depending on the legality of the move.
!!  In this implementation, I use a small array of the stack entities. This allows us
!!  to easily find the stack where the disk to be moved resides.
      USE data_defs
      IMPLICIT NONE
!
! PARAMETER definitions
!
      INTEGER(int32) , PARAMETER  ::  bigm = maxpos*3
!
! Dummy arguments
!
      INTEGER(int32)  ::  Numdisk
      INTENT (IN) Numdisk
!
! Local variables
!
      TYPE(stack) , POINTER  ::  a , b , c , on_now   !< on_now is where disk 1 is
      TYPE(stack) , TARGET , DIMENSION(3) ::  abc !< The three stack are put in an array for identification i.e. abc(1)%stack_id = 1
      INTEGER  ::  direction !< Direction of disk1, negative is counter clockwise, positive = clockwise
      INTEGER(int32)  ::  i , j

      DATA(abc(i)%height , i = 1 , 3)/3*0/
      DATA(abc(i)%stack_id , i = 1 , 3)/1 , 2 , 3/
      DATA((abc(i)%disks(j),i = 1,3) , j = 1 , maxpos)/bigm*0/
! Code starts here
!
! Move numdisks from A to C using B as intermediate
!
      a => abc(1)
      b => abc(2)
      c => abc(3)
      on_now => a   !< Point to the starting pole
      a%height = Numdisk    !< A = the starting pole
!
      last_move = -1
!
      a%disks = [(Numdisk + 1 - j, j = 1, Numdisk)]

      IF( btest(Numdisk,0) )THEN        !< First move rule always involves disk 1, test odd/even for first move
         CALL move(a , c)
         direction = -1         ! Counter clockwise
         on_now => c
      ELSE
         CALL move(a , b)
         direction = 1          ! Clockwise
         on_now => b
      END IF
!
      DO WHILE ( c%height/=Numdisk )
!
         SELECT CASE(on_now%stack_id)   !< Depending where disk one is, make a legal move
         CASE(1)    !< One is on stack 1 i.e. a so we can only make a legal move in between b and c
            IF( legal(b,c) )THEN
               CALL move(b , c)
            ELSE
               CALL move(c , b)
            END IF
         CASE(2)                        ! Disk one on stack 2 i.e. "b"
            IF( legal(a,c) )THEN
               CALL move(a , c)
            ELSE
               CALL move(c , a)
            END IF
         CASE(3)                        ! Disk one on stack 3 i.e. "c"
            IF( legal(a,b) )THEN
               CALL move(a , b)
            ELSE
               CALL move(b , a)
            END IF
         END SELECT

!< Now move disk 1 in the direction it was heading
         i = on_now%stack_id + direction       !< Increment the stack a->b->c->a or vice versa Decrement the stack c->b->a->c
!< Note that here we use the stack_id to figure out which disk destination to use. As we increment or decrement the stack counter
!! we reset it to the correct disk when it is outside the 1..3 range. It is set so as to maintain the correct disk direction.
         SELECT CASE(i)
         CASE(0)
            i = 3
         CASE(1:3)
         CASE(4)
            i = 1
         END SELECT

         CALL move(on_now , abc(i))
         on_now => abc(i)
      END DO
      PRINT '(*(i0,2x))' , (c%disks(i) , i = 1 , Numdisk) ! Print final disk configuration
      on_now => null()
!
      RETURN
      END SUBROUTINE olives
      SUBROUTINE Move(Donor , Receiver)
      USE Data_defs
      IMPLICIT NONE

! Dummy arguments
!
      TYPE(stack)  ::  Donor , Receiver
      INTENT (INOUT) Donor , Receiver
! Code starts here
!$GCC$ attributes INLINE :: MOVE
!
! Code starts here
      last_move = Receiver%Stack_id
      Receiver%Height = Receiver%Height + 1           ! make slot in receiver
      Receiver%Disks(Receiver%Height) = Donor%Disks(Donor%Height)     !Move the disk
      Donor%Disks(Donor%Height) = 0                   ! Black it out
      Donor%Height = Donor%Height - 1                 ! Decrement the donor height
      RETURN
      END SUBROUTINE Move
    Module data_defs
      IMPLICIT NONE
!
! PARAMETER definitions
!
      INTEGER , PARAMETER  ::  int32 = selected_int_kind(8) , &
                             & int64 = selected_int_kind(16)
                            
      INTEGER(int32) , PARAMETER  ::  maxpos = 40        ! Maximum possible disks without a huge blowout
!
! Derived Type definitions
!
      TYPE :: stack
         INTEGER(int32)  ::  stack_id
         INTEGER(int32)  ::  height
         INTEGER(int32) , DIMENSION(maxpos)  ::  disks
      END TYPE stack
!
! Local variables
!
      INTEGER  ::  last_move              ! Holds the destination of the last move
      end module data_defs
```


## FreeBASIC

```mw
' FB 1.05.0 Win64

Sub move(n As Integer, from As Integer, to_ As Integer, via As Integer)
  If n > 0 Then
    move(n - 1, from, via, to_)
    Print "Move disk"; n; " from pole"; from; " to pole"; to_
    move(n - 1, via, to_, from)
  End If
End Sub

Print "Three disks" : Print
move 3, 1, 2, 3 
Print 
Print "Four disks" : Print
move 4, 1, 2, 3
Print "Press any key to quit"
Sleep
```

**Output:**

```
Three disks

Move disk 1 from pole 1 to pole 2
Move disk 2 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 3
Move disk 3 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 1
Move disk 2 from pole 3 to pole 2
Move disk 1 from pole 1 to pole 2

Four disks

Move disk 1 from pole 1 to pole 3
Move disk 2 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
Move disk 3 from pole 1 to pole 3
Move disk 1 from pole 2 to pole 1
Move disk 2 from pole 2 to pole 3
Move disk 1 from pole 1 to pole 3
Move disk 4 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
Move disk 2 from pole 3 to pole 1
Move disk 1 from pole 2 to pole 1
Move disk 3 from pole 3 to pole 2
Move disk 1 from pole 1 to pole 3
Move disk 2 from pole 1 to pole 2
Move disk 1 from pole 3 to pole 2
```


## Frink

```mw
/** Set up the recursive call for n disks */
hanoi[n] := hanoi[n, 1, 3, 2]

/** The recursive call. */
hanoi[n, source, target, aux] :=
{
   if n > 0
   {                       
      hanoi[n-1, source, aux, target]                          
      println["Move from $source to $target"]                                                                     
      hanoi[n-1, aux, target, source]
   }
}

hanoi[7]
```


## FutureBasic

```mw
window 1, @"Towers of Hanoi", ( 0, 0, 300, 300 )

void local fn Move( n as long, fromPeg as long, toPeg as long, viaPeg as long )
  if n > 0
    fn Move( n-1, fromPeg, viaPeg, toPeg )
    print "Move disk from "; fromPeg; " to "; toPeg
    fn Move( n-1, viaPeg, toPeg, fromPeg )
  end if
end fn

fn Move( 4, 1, 2, 3 )
print
print "Towers of Hanoi puzzle solved."

HandleEvents
```

Output:

```
Move disk from  1 to  3
Move disk from  1 to  2
Move disk from  3 to  2
Move disk from  1 to  3
Move disk from  2 to  1
Move disk from  2 to  3
Move disk from  1 to  3
Move disk from  1 to  2
Move disk from  3 to  2
Move disk from  3 to  1
Move disk from  2 to  1
Move disk from  3 to  2
Move disk from  1 to  3
Move disk from  1 to  2
Move disk from  3 to  2

Towers of Hanoi puzzle solved.
```


## Fōrmulæ

Fōrmulæ programs are not textual, visualization/edition of programs is done showing/manipulating structures but not text. Moreover, there can be multiple visual representations of the same program. Even though it is possible to have textual representation —i.e. XML, JSON— they are intended for storage and transfer purposes more than visualization and edition.

Programs in Fōrmulæ are created/edited online in its website.

In **this page** you can see and run the program(s) related to this task and their results. You can also change either the programs or the parameters they are called with, for experimentation, but remember that these programs were created with the main purpose of showing a clear solution of the task, and they generally lack any kind of validation.

**Solution**

**Test case**


## Gambas

Translation of

:

FreeBASIC

```mw
Public Sub Main() 
  
  Print "Three disks\n"
  move_(3, 1, 2, 3)
  Print  
  Print "Four disks\n"
  move_(4, 1, 2, 3)
  
End 

Public Sub move_(n As Integer, from As Integer, to As Integer, via As Integer) 

  If n > 0 Then 
    move_(n - 1, from, via, to) 
    Print "Move disk "; n; " from pole "; from; " to pole "; to 
    move_(n - 1, via, to, from) 
  End If 

End Sub
```

**Output:**

```
Same as FreeBASIC entry.
```


## GAP

```mw
Hanoi := function(n)
	local move;
	move := function(n, a, b, c) # from, through, to
		if n = 1 then
			Print(a, " -> ", c, "\n");
		else
			move(n - 1, a, c, b);
			move(1, a, b, c);
			move(n - 1, b, a, c);
		fi;
	end;
	move(n, "A", "B", "C");
end;

Hanoi(1);
# A -> C

Hanoi(2);
# A -> B
# A -> C
# B -> C

Hanoi(3);
# A -> C
# A -> B
# C -> B
# A -> C
# B -> A
# B -> C
# A -> C
```


## Go

```mw
package main

import "fmt"

// a towers of hanoi solver just has one method, play
type solver interface {
    play(int)
}

func main() {
    var t solver    // declare variable of solver type
    t = new(towers) // type towers must satisfy solver interface
    t.play(4)
}

// towers is example of type satisfying solver interface
type towers struct {
    // an empty struct.  some other solver might fill this with some
    // data representation, maybe for algorithm validation, or maybe for
    // visualization.
}

// play is sole method required to implement solver type
func (t *towers) play(n int) {
    // drive recursive solution, per task description
    t.moveN(n, 1, 2, 3)
}

// recursive algorithm
func (t *towers) moveN(n, from, to, via int) {
    if n > 0 {
        t.moveN(n-1, from, via, to)
        t.move1(from, to)
        t.moveN(n-1, via, to, from)
    }
}

// example function prints actions to screen.
// enhance with validation or visualization as needed.
func (t *towers) move1(from, to int) {
    fmt.Println("move disk from rod", from, "to rod", to)
}
```

In other words:

```mw
package main

import "fmt"

func main() {
	move(3, "A", "B", "C")
}

func move(n uint64, a, b, c string) {
	if n > 0 {
		move(n-1, a, c, b)
		fmt.Println("Move disk from " + a + " to " + c)
		move(n-1, b, a, c)
	}
}
```


## Golfscript

```
{:q;.@.@<@@\)>q\++}:at;
{\.@\}:over;
{1 [" -> "] at puts}:disp;

{ . 0>
  { over over
      \ ~[\]+ \(
      move
    \ .disp \
    over over
      \ )\~\[@] \(
      move
  } *;;
}:move;

[1 2 3] 3 move
```

**Output:**

```
1 -> 3
1 -> 2
3 -> 2
1 -> 3
2 -> 1
2 -> 3
1 -> 3
```
