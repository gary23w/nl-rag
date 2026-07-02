---
title: "100 doors (part 7/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 7/10
---

## mIRC Scripting Language

```mw
var %d = $str(0 $+ $chr(32),100), %m = 1
while (%m <= 100) {
  var %n = 1
  while ($calc(%n * %m) <= 100) {
    var %d = $puttok(%d,$iif($gettok(%d,$calc(%n * %m),32),0,1),$calc(%n * %m),32)
    inc %n
  }
  inc %m
}
echo -ag All Doors (Boolean): %d
var %n = 1
while (%n <= $findtok(%d,1,0,32)) {
  var %t = %t $findtok(%d,1,%n,32)
  inc %n
}
echo -ag Open Door Numbers: %t
```


## ML/I

```mw
MCSKIP "WITH" NL
"" 100 doors
MCINS %.
MCSKIP MT,<>
"" Doors represented by P1-P100, 0 is closed
MCPVAR 100
"" Set P variables to 0
MCDEF ZEROPS WITHS NL AS <MCSET T1=1
%L1.MCSET PT1=0
MCSET T1=T1+1
MCGO L1 UNLESS T1 EN 101
>
ZEROPS
"" Generate door state
MCDEF STATE WITHS () AS <MCSET T1=%A1.
MCGO L1 UNLESS T1 EN 0
closed<>MCGO L0
%L1.open>
"" Main macro - no arguments
"" T1 is pass number
"" T2 is door number
MCDEF DOORS WITHS NL
AS <MCSET T1=1
"" pass loop
%L1.MCGO L4 IF T1 GR 100
"" door loop
MCSET T2=T1
%L2.MCGO L3 IF T2 GR 100
MCSET PT2=1-PT2
MCSET T2=T2+T1
MCGO L2
%L3.MCSET T1=T1+1
MCGO L1
%L4."" now output the result
MCSET T1=1
%L5.door %T1. is STATE(%PT1.)
MCSET T1=T1+1
MCGO L5 UNLESS T1 GR 100
>
"" Do it
DOORS
```


## MMIX

See 100 doors/MMIX


## Modula-2

**unoptimized**

```mw
MODULE Doors;
IMPORT InOut;

TYPE State = (Closed, Open);
TYPE List = ARRAY [1 .. 100] OF State;

VAR
  Doors: List;
  I, J:  CARDINAL;

BEGIN
  FOR I := 1 TO 100 DO
    FOR J := 1 TO 100 DO
      IF J MOD I = 0 THEN
        IF Doors[J] = Closed THEN
          Doors[J] := Open
        ELSE
          Doors[J] := Closed
        END
      END
    END
  END;

  FOR I := 1 TO 100 DO
    InOut.WriteCard(I, 3);
    InOut.WriteString(' is ');

    IF Doors[I] = Closed THEN
      InOut.WriteString('Closed.')
    ELSE
      InOut.WriteString('Open.')
    END;

    InOut.WriteLn
  END
END Doors.
```

**optimized**

```mw
MODULE DoorsOpt;
IMPORT InOut;

TYPE State = (Closed, Open);
TYPE List = ARRAY [1 .. 100] OF State;

VAR
  Doors: List;
  I:  CARDINAL;

BEGIN
  FOR I := 1 TO 10 DO
    Doors[I*I] := Open
  END;

  FOR I := 1 TO 100 DO
    InOut.WriteCard(I, 3);
    InOut.WriteString(' is ');
    IF Doors[I] = Closed THEN
      InOut.WriteString('Closed.')
    ELSE
      InOut.WriteString('Open.')
    END;
    InOut.WriteLn
  END
END DoorsOpt.
```


## Modula-3

**unoptimized**

```mw
MODULE Doors EXPORTS Main;

IMPORT IO, Fmt;

TYPE State = {Closed, Open};
TYPE List = ARRAY [1..100] OF State;

VAR doors := List{State.Closed, ..};

BEGIN
  FOR i := 1 TO 100 DO
    FOR j := FIRST(doors) TO LAST(doors) DO
      IF j MOD i = 0 THEN
        IF doors[j] = State.Closed THEN
          doors[j] := State.Open;
        ELSE
          doors[j] := State.Closed;
        END;
      END;
    END;
  END;

  FOR i := FIRST(doors) TO LAST(doors) DO
    IO.Put(Fmt.Int(i) & " is ");
    IF doors[i] = State.Closed THEN
      IO.Put("Closed.\n");
    ELSE
      IO.Put("Open.\n");
    END;
  END;
END Doors.
```

**optimized**

```mw
MODULE DoorsOpt EXPORTS Main;

IMPORT IO, Fmt;

TYPE State = {Closed, Open};
TYPE List = ARRAY [1..100] OF State;

VAR doors := List{State.Closed, ..};

BEGIN
  FOR i := 1 TO 10 DO
    doors[i * i] := State.Open;
  END;

  FOR i := FIRST(doors) TO LAST(doors) DO
    IO.Put(Fmt.Int(i) & " is ");
    IF doors[i] = State.Closed THEN
      IO.Put("Closed.\n");
    ELSE
      IO.Put("Open.\n");
    END;
  END;
END DoorsOpt.
```


## MontiLang

```mw
101 var l .

for l 0 endfor
arr

0 var i .
for l
    i 1 + var i var j .
    j l < var pass .
    while pass
        get j not insert j .
        j i + var j
        l < var pass .  
    endwhile
endfor
print /# show all doors #/

/# show only open doors #/
|| print .
0 var i .
for l
    get i
    if : i out | | out . . endif .
    i 1 + var i .
endfor

input . /# pause until ENTER key pressed #/
```


## MOO

```mw
is_open = make(100);
for pass in [1..100]
  for door in [pass..100]
    if (door % pass)
      continue;
    endif
    is_open[door] = !is_open[door];
  endfor
endfor

"output the result";
for door in [1..100]
  player:tell("door #", door, " is ", (is_open[door] ? "open" : "closed"), ".");
endfor
```


## Moonli

```mw
in-package :moonli-user

let open-doors = make-array(100, :initial-element, nil):

  loop :for diff :from 1 :to 100 :do
    loop :for door-num :from (diff - 1) :below 100 :by diff :do
      aref(open-doors, door-num) = not(aref(open-doors, door-num))
    end
  end loop

  loop :for door-num :below 100 :do
    format(
       t, 
       "Door #~d is ~d~%", 
       door-num + 1, (ifelse aref(open-doors, door-num) "open" "closed")
    )
  end loop

end let
```


## MoonScript

```mw
is_open = [false for door = 1,100]
 
for pass = 1,100 
    for door = pass,100,pass
        is_open[door] = not is_open[door]
  
for i,v in ipairs is_open
    print "Door #{i}: " .. if v then 'open' else 'closed'
```


## MUMPS

```mw
doors	new door,pass
	For door=1:1:100 Set door(door)=0
	For pass=1:1:100 For door=pass:pass:100 Set door(door)='door(door)
	For door=1:1:100 If door(door) Write !,"Door",$j(door,4)," is open"
	Write !,"All other doors are closed."
	Quit
Do doors
Door   1 is open
Door   4 is open
Door   9 is open
Door  16 is open
Door  25 is open
Door  36 is open
Door  49 is open
Door  64 is open
Door  81 is open
Door 100 is open
All other doors are closed.
```


## Myrddin

```mw
use std

const main = {
	var isopen	: bool[100]

	std.slfill(isopen[:], false)
	for var i = 0; i < isopen.len; i++
		for var j = i; j < isopen.len; j += i + 1
			isopen[j] = !isopen[j]
		;;
	;;

	for var i = 0; i < isopen.len; i++
		if isopen[i]
			std.put("door {} is open\n", i + 1)
		;;
	;;
}
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


## MySQL

```mw
DROP PROCEDURE IF EXISTS one_hundred_doors;

DELIMITER |

CREATE PROCEDURE one_hundred_doors (n INT)
BEGIN
  DROP TEMPORARY TABLE IF EXISTS doors; 
  CREATE TEMPORARY TABLE doors (
    id INTEGER NOT NULL,
    open BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id)
  );

  SET @i = 1;
  create_doors: LOOP
    INSERT INTO doors (id, open) values (@i, FALSE);
    SET @i = @i + 1;
    IF @i > n THEN
      LEAVE create_doors;
    END IF;
  END LOOP create_doors;

  SET @i = 1;
  toggle_doors: LOOP
    UPDATE doors SET open = NOT open WHERE MOD(id, @i) = 0;
    SET @i = @i + 1;
    IF @i > n THEN
      LEAVE toggle_doors;
    END IF;
  END LOOP toggle_doors;

  SELECT id FROM doors WHERE open;
END|

DELIMITER ;

CALL one_hundred_doors(100);
```

**Output:**

```
+-----+
| id  |
+-----+
|   1 |
|   4 |
|   9 |
|  16 |
|  25 |
|  36 |
|  49 |
|  64 |
|  81 |
| 100 |
+-----+
10 rows in set (0.02 sec)
```


## Nanoquery

```mw
// allocate a boolean array with all closed doors (false)
// we need 101 since there will technically be a door 0
doors = {false} * 101
 
// loop through all the step lengths (1-100)
for step in range(1, 100)
	// loop through all the doors, stepping by step
	for door in range(0, len(doors) - 1, step)
		// change the state of the current door
		doors[door] = !doors[door]
	end for
end for
 
// loop through and print the doors that are open, skipping door 0
for i in range(1, len(doors) - 1)
	// if the door is open, display it
	if doors[i]
		println "Door " + i + " is open."
	end if
end for
```


## NetRexx

**unoptimized**

```mw
/* NetRexx */
options replace format comments java crossref symbols binary

True  = Rexx(1 == 1)
False = Rexx(\True)

doors = False

loop i_ = 1 to 100
  loop j_ = 1 to 100
    if 0 = (j_ // i_) then doors[j_] = \doors[j_]
    end j_
  end i_

loop d_ = 1 to 100
  if doors[d_] then  state = 'open'
  else  state = 'closed'

  say 'Door Nr.' Rexx(d_).right(4) 'is' state
  end d_
```

**optimized** (Based on the Java 'optimized' version)

Translation of

:

Java

```mw
/* NetRexx */
options replace format comments java crossref symbols binary

True  = (1 == 1)
False = \True

doors = boolean[100]

loop i_ = 0 to 9
  doors[(i_ + 1) * (i_ + 1) - 1] = True;
  end i_

loop i_ = 0 to 99
  if doors[i_] then  state = 'open'
  else  state = 'closed'

  say 'Door Nr.' Rexx(i_ + 1).right(4) 'is' state
  end i_
```

**optimized 2** (Based on the Java 'optimized 2' version)

Translation of

:

Java

```mw
/* NetRexx */
options replace format comments java crossref savelog symbols binary

resultstring = ''

loop i_ = 1 to 10
  resultstring = resultstring || 'Door Nr.' Rexx(i_ * i_).right(4) 'is open\n'
  end i_

say resultstring
```

**optimized 3**

```mw
/* NetRexx */

loop i = 1 to 10
   say 'Door Nr.' i * i 'is open.'
  end i
```


## newLISP

```mw
(define (status door-num)
    (let ((x (int (sqrt door-num))))
     (if
       (= (* x x) door-num) (string "Door " door-num " Open")
       (string "Door " door-num " Closed"))))

(dolist (n (map status (sequence 1 100)))
  (println n))
```

Not optimized:

```mw
(set 'Doors (array 100))  ;; Default value: nil (Closed)

(for (x 0 99)
    (for (y x 99 (+ 1 x))
        (setf (Doors y) (not (Doors y)))))

(for (x 0 99)  ;; Display open doors
    (if (Doors x)
        (println (+ x 1) " : Open")))
```

Output:

```
1 : Open
4 : Open
9 : Open
16 : Open
25 : Open
36 : Open
49 : Open
64 : Open
81 : Open
100 : Open
```


## Nial

unoptimized solution (works with Q'Nial7):

Output of the boolean array showing the status of the doors. Truth values in Nial arrays are shown as `l`(true) and `o`(false):

```mw
     n:=100;reduce xor (count n eachright mod count n eachall<1)
looloooolooooooloooooooolooooooooooloooooooooooolooooooooooooooloooooooooooooooo

looooooooooooooooool
```

Indices of the open doors:

```mw
     true findall (n:=100;reduce xor (count n eachright mod count n eachall<1))+1
1 4 9 16 25 36 49 64 81 100
```

optimized solution:

```mw
     count 10 power 2
1 4 9 16 25 36 49 64 81 100
```


## Nim

unoptimized:

```mw
from strutils import `%`

const numDoors = 100
var doors: array[1..numDoors, bool]

for pass in 1..numDoors:
  for door in countup(pass, numDoors, pass):
    doors[door] = not doors[door]

for door in 1..numDoors:
  echo "Door $1 is $2." % [$door, if doors[door]: "open" else: "closed"]
```

Challenging C++'s compile time computation: https://rosettacode.org/wiki/100_doors#C.2B.2B *outputString* is evaluated at compile time. Check the resulting binary in case of doubt.

```mw
from strutils import `%`

const numDoors = 100
var doors {.compileTime.}: array[1..numDoors, bool]

proc calcDoors(): string =
  for pass in 1..numDoors:
    for door in countup(pass, numDoors, pass):
      doors[door] = not doors[door] 
  for door in 1..numDoors:
    result.add("Door $1 is $2.\n" % [$door, if doors[door]: "open" else: "closed"])

const outputString: string = calcDoors()

echo outputString
```


## Oberon-07

Oberon-07, by Niklaus Wirth.

```
MODULE Doors;
  IMPORT Out;
  
  PROCEDURE Do*;  (* In Oberon an asterisk after an identifier is an export mark *)
    CONST N = 100; len = N + 1;
    VAR i, j: INTEGER;
      closed: ARRAY len OF BOOLEAN;  (* Arrays in Oberon always start with index 0; closed[0] is not used *)
  BEGIN
    FOR i := 1 TO N DO closed[i] := TRUE END;
    FOR i := 1 TO N DO
      j := 1;
      WHILE j < len DO
        IF j MOD i = 0 THEN closed[j] := ~closed[j] END; INC(j)  (* ~ = NOT *)
      END
    END;
    (* Print a state diagram of all doors *)
    FOR i := 1 TO N DO 
      IF (i - 1) MOD 10 = 0 THEN Out.Ln END;
      IF closed[i] THEN Out.String("- ") ELSE Out.String("+ ") END
    END;  Out.Ln;
    (* Print the numbers of the open doors *)
    FOR i := 1 TO N DO 
      IF ~closed[i] THEN Out.Int(i, 0); Out.Char(" ") END
    END;  Out.Ln
  END Do;

END Doors.
```

Execute: Doors.Do

**Output:**

```
+ – – + – – – – + – 
– – – – – + – – – – 
– – – – + – – – – – 
– – – – – + – – – – 
– – – – – – – – + – 
– – – – – – – – – – 
– – – + – – – – – – 
– – – – – – – – – – 
+ – – – – – – – – – 
– – – – – – – – – + 
1 4 9 16 25 36 49 64 81 100 
```


## Objeck

**optimized**

```mw
bundle Default {
  class Doors {
    function : Main(args : String[]) ~ Nil {
      doors := Bool->New[100];
      
      for(pass := 0; pass < 10; pass += 1;) {
        doors[(pass + 1) * (pass + 1) - 1] := true;
      };
      
      for(i := 0; i < 100; i += 1;) {    
        IO.Console->GetInstance()->Print("Door #")->Print(i + 1)->Print(" is ");
        if(doors[i]) {
          "open."->PrintLine();
        }
        else {
          "closed."->PrintLine();
        };
      };
    }
  }
}
```


## Objective-C

**A basic implementation in Objective-C:**

This is a very basic Objective-C sample that shows the usage of standard types and classes such as NSInteger and NSMutableArray.

It uses modern Objective-C syntax such as literals, blocks, and a compiler module import statement.

```mw
@import Foundation;

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        // Create a mutable array
        NSMutableArray *doorArray = [@[] mutableCopy];
        
        // Fill the doorArray with 100 closed doors
        for (NSInteger i = 0; i < 100; ++i) {
            doorArray[i] = @NO;
        }
        
        // Do the 100 passes
        for (NSInteger pass = 0; pass < 100; ++pass) {
            for (NSInteger door = pass; door < 100; door += pass+1) {
                doorArray[door] = [doorArray[door]  isEqual: @YES] ? @NO : @YES;
            }
        }
        
        // Print the results
        [doorArray enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
            if ([obj isEqual: @YES]) {
                NSLog(@"Door number %lu is open", idx + 1);
            }
        }];
    }
}
```

**A more typical implementation in Objective-C:**

This example is more along the lines of what typical Objective-C program would look like.

Language features used include:

- MVC design pattern with separate classes for the data model, user interface, and controller (Here, main steps in to represent the controller class.)
- Class category to extend the standard NSMutableArray class to add doors without a subclass
- Class inheritance in the DoorViewClass when subclassing NSObject
- Pragma mark statements for IDE navigation in Xcode

In a real world program classes are normally separated into different files.

```mw
@import Foundation;

#pragma mark - Classes
////////////////////////////////////////////////////
// Model class header - A we are using a category to add a method to MSMutableArray
@interface NSMutableArray (DoorModelExtension)

- (void)setNumberOfDoors:(NSUInteger)doors;

@end

// Model class implementation
@implementation NSMutableArray (DoorModelExtension)

- (void)setNumberOfDoors:(NSUInteger)doors {
    // Fill the doorArray with 100 closed doors
    for (NSInteger i = 0; i < doors; ++i) {
        self[i] = @NO;
    }
}
@end
////////////////////////////////////////////////////

// View class header - A simple class to handle printing our values
@interface DoorViewClass : NSObject

- (void)printResultsOfDoorTask:(NSMutableArray *)doors;

@end

// View class implementation
@implementation DoorViewClass

- (void)printResultsOfDoorTask:(NSMutableArray *)doors {

    // Print the results, using an enumeration block for easy index tracking
    [doors enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
        if ([obj isEqual: @YES]) {
            NSLog(@"Door number %lu is open", idx + 1);
        }
    }];
}

@end
////////////////////////////////////////////////////

#pragma mark - main
// With our classes set we can use them from our controller, in this case main
int main(int argc, const char * argv[]) {
    
    // Init our classes
    NSMutableArray *doorArray = [NSMutableArray array];
    DoorViewClass *doorView = [DoorViewClass new];
    
    // Use our class category to add the doors
    [doorArray setNumberOfDoors:100];
    
    // Do the 100 passes
    for (NSUInteger pass = 0; pass < 100; ++pass) {
        for (NSUInteger door = pass; door < 100; door += pass+1) {
            doorArray[door] = [doorArray[door]  isEqual: @YES] ? @NO : @YES;
        }
    }
    
    // Print the results
    [doorView printResultsOfDoorTask:doorArray];
   
}
```


## OCaml

**unoptimized**

```mw
let max_doors = 100

let show_doors =
  Array.iteri (fun i x -> Printf.printf "Door %d is %s\n" (i+1)
                                        (if x then "open" else "closed"))

let flip_doors doors =
  for i = 1 to max_doors do
    let rec flip idx =
      if idx < max_doors then begin
        doors.(idx) <- not doors.(idx);
        flip (idx + i)
      end
    in flip (i - 1)
  done;
  doors

let () =
  show_doors (flip_doors (Array.make max_doors false))
```

**optimized**

```mw
let optimised_flip_doors doors =
  for i = 1 to int_of_float (sqrt (float_of_int max_doors)) do
    doors.(i*i - 1) <- true
  done;
  doors

let () =
  show_doors (optimised_flip_doors (Array.make max_doors false))
```

This variant is more **functional style** (loops are recursions), unoptimized, and we do rather 100 passes on first element, then 100 * second, to avoid mutable data structures and many intermediate lists.

```mw
type door = Open | Closed    (* human readable code *)

let flipdoor = function Open -> Closed | Closed -> Open

let string_of_door =       
  function Open -> "is open." | Closed -> "is closed."

let printdoors ls =
  let f i d = Printf.printf "Door %i %s\n" (i + 1) (string_of_door d)
  in List.iteri f ls

let outerlim = 100
let innerlim = 100

let rec outer cnt accu =
  let rec inner i door = match i > innerlim with (* define inner loop *)
    | true  -> door                         
    | false -> inner (i + 1) (if (cnt mod i) = 0 then flipdoor door else door)
  in (* define and do outer loop *)
  match cnt > outerlim with
  | true  -> List.rev accu
  | false -> outer  (cnt + 1)  (inner 1 Closed :: accu) (* generate new entries with inner *)

let () = printdoors (outer 1 [])
```


## Octave

```mw
doors = false(100,1);
for i = 1:100
  for j = i:i:100
    doors(j) = !doors(j);
  endfor
endfor
for i = 1:100
  if ( doors(i) )
    s = "open";
  else
    s = "closed";
  endif
  printf("%d %s\n", i, s);
endfor
```

See also the solutions in Matlab. They will work in Octave, too.


## Odin

This version was written explicitly for Odin, using some of its finer features and foregoing the enum approach for a more efficient boolean slice layout.

```mw
package doors

import "core:fmt"

main :: proc() {
	doors: [100]bool

	for every_n := 1; every_n < len(doors); every_n += 1 {
		i := every_n - 1
		for true {
			if i >= len(doors) do break

			doors[i] = !doors[i]

			i += every_n
		}
	}

	for &door, i in doors {
		if door do fmt.printf("%d ", i + 1)
	}
}
```

Output:

```
1 4 9 16 25 36 49 64 81
```

Both the below versions are essentially adapted from the **Go** version, except for the output which is more inspired by the **Ada** example.

**unoptimized**

```mw
package main

import "core:fmt"

main :: proc() {
 using fmt
  
  Door_State :: enum {Closed, Open}
  
  doors := [?]Door_State { 0..<100 = .Closed }
  
  for i in  1..=100 {
    for j := i-1; j < 100; j += i {
      if doors[j] == .Closed {
        doors[j] = .Open
      } else {
        doors[j] = .Closed
      }
    }
  }
  for state, i in doors {
    println("Door: ",int(i+1)," -> ",state)
  }
}
```

**optimized**

```mw
package main

import "core:fmt"
import "core:math"

main :: proc() {
 using fmt
  
  Door_State :: enum {Closed, Open}
  
  doors := [?]Door_State { 0..<100 = .Closed }
  
  for i in  1..=100 {
     res := math.sqrt_f64( f64(i) )
     if math.mod_f64( res, 1) == 0 {
        doors[i-1] = .Open
     } else {
        doors[i-1] = .Closed
     }
     println("Door: ", i, " -> ", doors[i-1])
  }
}
```


## Oforth

```mw
: doors
| i j l |
   100 false Array newWith dup ->l
   100 loop: i [ 
      i 100 i step: j [ l put ( j , j l at not ) ] 
      ] 
;
```


## Ol

```mw
(define (flip doors every)
   (map (lambda (door num)
            (mod (+ door (if (eq? (mod num every) 0) 1 0)) 2))
      doors
      (iota (length doors) 1)))

(define doors
   (let loop ((doors (repeat 0 100)) (n 1))
      (if (eq? n 100)
         doors
         (loop (flip doors n) (+ n 1)))))

(print "100th doors: " doors)
```

Output:

```
100th doors: (1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
```


## OmniMark

```mw
process
  local switch doors size 100 ; all initialised ('1st pass' to false)

  repeat over doors
    repeat for integer door from #item to 100 by #item
      do when doors[door] = false
        activate doors[door] ; illustrating alternative to set ... to
      else
        set doors[door] to false
      done
    again
  again

  repeat over doors
    do when doors = true
      put #error '%d(#item)%n'
    done
  again
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

**Optimised version.**

```mw
process
  local integer door initial {1}
  local integer step initial {3}

  repeat
    output "Door %d(door) is open%n"
    increment door by step
    increment step by 2
    exit when door > 100
  again
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


## Onyx

```mw
$Door dict def
1 1 100 {Door exch false put} for
$Toggle {dup Door exch get not Door up put} def
$EveryNthDoor {dup 100 {Toggle} for} def
$Run {1 1 100 {EveryNthDoor} for} def
$ShowDoor {dup `Door no. ' exch cvs cat ` is ' cat
  exch Door exch get {`open.\n'}{`shut.\n'} ifelse cat
  print flush} def
Run 1 1 100 {ShowDoor} for
```

**Output:**

```
Door no. 1 is open.
Door no. 2 is shut.
Door no. 3 is shut.
Door no. 4 is open.
Door no. 5 is shut.
Door no. 6 is shut.
Door no. 7 is shut.
Door no. 8 is shut.
Door no. 9 is open.
Door no. 10 is shut.
Door no. 11 is shut.
Door no. 12 is shut.
Door no. 13 is shut.
Door no. 14 is shut.
Door no. 15 is shut.
Door no. 16 is open.
Door no. 17 is shut.
Door no. 18 is shut.
Door no. 19 is shut.
Door no. 20 is shut.
Door no. 21 is shut.
Door no. 22 is shut.
Door no. 23 is shut.
Door no. 24 is shut.
Door no. 25 is open.
Door no. 26 is shut.
Door no. 27 is shut.
Door no. 28 is shut.
Door no. 29 is shut.
Door no. 30 is shut.
Door no. 31 is shut.
Door no. 32 is shut.
Door no. 33 is shut.
Door no. 34 is shut.
Door no. 35 is shut.
Door no. 36 is open.
Door no. 37 is shut.
Door no. 38 is shut.
Door no. 39 is shut.
Door no. 40 is shut.
Door no. 41 is shut.
Door no. 42 is shut.
Door no. 43 is shut.
Door no. 44 is shut.
Door no. 45 is shut.
Door no. 46 is shut.
Door no. 47 is shut.
Door no. 48 is shut.
Door no. 49 is open.
Door no. 50 is shut.
Door no. 51 is shut.
Door no. 52 is shut.
Door no. 53 is shut.
Door no. 54 is shut.
Door no. 55 is shut.
Door no. 56 is shut.
Door no. 57 is shut.
Door no. 58 is shut.
Door no. 59 is shut.
Door no. 60 is shut.
Door no. 61 is shut.
Door no. 62 is shut.
Door no. 63 is shut.
Door no. 64 is open.
Door no. 65 is shut.
Door no. 66 is shut.
Door no. 67 is shut.
Door no. 68 is shut.
Door no. 69 is shut.
Door no. 70 is shut.
Door no. 71 is shut.
Door no. 72 is shut.
Door no. 73 is shut.
Door no. 74 is shut.
Door no. 75 is shut.
Door no. 76 is shut.
Door no. 77 is shut.
Door no. 78 is shut.
Door no. 79 is shut.
Door no. 80 is shut.
Door no. 81 is open.
Door no. 82 is shut.
Door no. 83 is shut.
Door no. 84 is shut.
Door no. 85 is shut.
Door no. 86 is shut.
Door no. 87 is shut.
Door no. 88 is shut.
Door no. 89 is shut.
Door no. 90 is shut.
Door no. 91 is shut.
Door no. 92 is shut.
Door no. 93 is shut.
Door no. 94 is shut.
Door no. 95 is shut.
Door no. 96 is shut.
Door no. 97 is shut.
Door no. 98 is shut.
Door no. 99 is shut.
Door no. 100 is open.
```


## ooRexx

```mw
doors = .array~new(100)    -- array containing all of the doors
do i = 1 to doors~size     -- initialize with a collection of closed doors
   doors[i] = .door~new(i)
end

do inc = 1 to doors~size
  do d = inc to doors~size by inc
    doors[d]~toggle
  end
end
say "The open doors after 100 passes:"
do door over doors
  if door~isopen then say door
end

::class door           -- simple class to represent a door
::method init          -- initialize an instance of a door
  expose id state      -- instance variables of a door
  use strict arg id    -- set the id
  state = .false       -- initial state is closed

::method toggle        -- toggle the state of the door
  expose state
  state = \state

::method isopen        -- test if the door is open
  expose state
  return state

::method string        -- return a string value for a door
  expose state id
  if state then return "Door" id "is open"
  else return "Door" id "is closed"

::method state         -- return door state as a descriptive string
  expose state
  if state then return "open"
  else return "closed"
```

The two programs in the Rexx section run under ooRexx when '#' is replaced by, e.g., 'dd'. '#' is not supported by ooRexx as part of or as a symbol. Neither are @ and $.


## OpenEdge/Progress

```mw
DEFINE VARIABLE lopen   AS LOGICAL     NO-UNDO EXTENT 100.
DEFINE VARIABLE idoor   AS INTEGER     NO-UNDO.
DEFINE VARIABLE ipass   AS INTEGER     NO-UNDO.
DEFINE VARIABLE cresult AS CHARACTER   NO-UNDO.

DO ipass = 1 TO 100:
   idoor = 0.
   DO WHILE idoor <= 100:
      idoor = idoor + ipass.
      IF idoor <= 100 THEN
         lopen[ idoor ] = NOT lopen[ idoor ].
   END.
END.

DO idoor = 1 TO 100:
   cresult = cresult + STRING( lopen[ idoor ], "1  /0  " ).
   IF idoor MODULO 10 = 0 THEN
      cresult = cresult + "~r":U.
END.

MESSAGE cresult VIEW-AS ALERT-BOX.
```


## OPL

Tested with Psion Series 3a & Series 5.

```mw
REM https://github.com/Eva-Broccoli/OPL-Rosetta-Code/blob/main/A100door.opl
PROC main:
  LOCAL door%(100),i%,j%
  i%=1
  j%=1
  WHILE j%<101
    WHILE i%<101
      IF door%(i%)=0
        door%(i%)=1
      ELSE
        door%(i%)=0
      ENDIF
      i%=i%+j%
    ENDWH
    j%=j%+1
    i%=0+j%
  ENDWH
  PRINT "Open doors:",
  i%=1
  WHILE i%<101
    IF door%(i%)=1
      PRINT i%,
    ENDIF
    i%=i%+1
  ENDWH
  GET
ENDP
```


## OxygenBasic

```
def    doors 100
int    door[doors],i ,j, c
string cr,tab,pr
'
for i=1 to doors
  for j=i to doors step i
    door[j]=1-door[j]
    if door[j] then c++ else c--
  next
next
'
cr=chr(13) chr(10)
pr="Doors Open: " c cr cr 
'
for i=1 to doors
   if door[i] then pr+=i cr
next
print pr
```


## Oz

```mw
declare
  NumDoors = 100
  NumPasses = 100

  fun {NewDoor} closed end

  fun {Toggle Door}
     case Door of closed then open
     [] open then closed
     end
  end

  fun {Pass Doors I}
     {List.mapInd Doors
      fun {$ Index Door}
         if Index mod I == 0 then {Toggle Door}
         else Door
         end
      end}
  end
  
  Doors0 = {MakeList NumDoors}
  {ForAll Doors0 NewDoor}

  DoorsN = {FoldL {List.number 1 NumPasses 1} Pass Doors0}
in
  %% print open doors
  {List.forAllInd DoorsN
   proc {$ Index Door}
      if Door == open then
	 {System.showInfo "Door "#Index#" is open."}
      end
   end
  }
```

Output:

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


## PARI/GP

**Unoptimized version.**

```mw
v=vector(d=100);/*set 100 closed doors*/
for(i=1,d,forstep(j=i,d,i,v[j]=1-v[j]));
for(i=1,d,if(v[i],print("Door ",i," is open.")))
```

**Optimized version.**

```mw
for(n=1,sqrt(100),print("Door ",n^2," is open."))
```

**Unoptimized version.**

```mw
doors =vector(100);
print("open doors are : ");
for(i=1,100,for(j=i,100,doors[j]=!doors[j];j +=i-1))
for(k=1,100,if(doors[k]==1,print1(" ",k)))
```

Output:

```
Open doors are:
 1 4 9 16 25 36 49 64 81 100
```


## Pascal

```mw
Program OneHundredDoors;

var
   doors : Array[1..100] of Boolean;
   i, j	 : Integer;
   
begin
   for i := 1 to 100 do
      doors[i] := False;
   for i := 1 to 100 do begin
      j := i;
      while j <= 100 do begin
	 doors[j] := not doors[j];
	 j := j + i
      end
   end;
   for i := 1 to 100 do begin
      Write(i, ' ');
      if doors[i] then
	 WriteLn('open')
      else
	 WriteLn('closed');
   end
end.
```

**Optimized version.**

```mw
program OneHundredDoors;

{$APPTYPE CONSOLE}

uses
  math, sysutils;

var
   AOpendoors  : String;
   ACloseDoors : String;
   i	       : Integer;

begin
   for i := 1 to 100 do
   begin
      if (sqrt(i) = floor(sqrt(i))) then
        AOpenDoors := AOpenDoors + IntToStr(i) + ';'
      else
        ACloseDoors := ACloseDoors + IntToStr(i) +';';
   end;

   WriteLn('Open doors: ' + AOpenDoors);
   WriteLn('Close doors: ' + ACloseDoors);
end.
```


## PascalABC.NET

Translation of

:

F#

// 100 doors. Nigel Galloway: January 11th., 2023

type

doorState=(Open,Closed);

function

flip(n:doorState):doorState:=

if

n=Open then Closed

else

Open;

var

Doors:Array of doorState:=ArrFill(100,Closed);

begin

for

var

n:=1

to

100

do

for

var

g:=n-1

to

99 step n

do

Doors[g]:=flip(Doors[g]);

for

var

n:=0

to

99

do

if

Doors[n]=Open then write(n+1,

' '

); write

Ln

end

.

**Output:**

```
1 4 9 16 25 36 49 64 81 100
```


## Pebble

```mw
;100 doors example program for x86 DOS
;Compiles with Pebble to 95 bytes com executable

program examples\100doors

data

	int i[0]
	int d[0]

begin

	label loop

		+1 [i]
		[d] = [i] * [i]
		echo [d]
		crlf

	if [d] < 100 then loop

	pause
	kill

end
```


## Perl

**unoptimized**

Works with

:

Perl

version 5.x

```mw
my @doors;
for my $pass (1 .. 100) {
    for (1 .. 100) {
        if (0 == $_ % $pass) {
            $doors[$_] = not $doors[$_];
        };
    };
};

print "Door $_ is ", $doors[$_] ? "open" : "closed", "\n" for 1 .. 100;
```

**semi-optimized**

Works with

:

Perl

version 5.x

This version flips doors, but doesn't visit (iterate over) doors that aren't toggled. Note: I represent open doors as 0 and closed as 1 just for preference. (When I print it as a bit vector, 0 looks more like an open door to me.)

```mw
#!/usr/bin/perl
use strict;
use warnings;

my @doors = (1) x 100;
for my $N (1 .. 100) {
   $doors[$_]=1-$doors[$_] for map { $_*$N - 1 } 1 .. int(100/$N);
}
print join("\n", map { "Door $_ is Open" } grep { ! $doors[$_-1] } 1 .. 100), "\n";
print "The rest are closed\n";
```

**optimized**

Works with

:

Perl

version 5.x

```mw
print "Door $_ is open\n" for map $_**2, 1 .. 10;
```

```mw
print "Door $_ is ", qw"closed open"[int sqrt == sqrt], "\n" for 1..100;
```

```mw
while( ++$i <= 100 )
{
    $root = sqrt($i);
    if ( int( $root ) == $root )
    {
        print "Door $i is open\n";
    }
    else
    {
        print "Door $i is closed\n";
    }
}
```


## Perl5i

```mw
use perl5i::2;

package doors {

  use perl5i::2;
  use Const::Fast;

  const my $OPEN   => 1;
  const my $CLOSED => 0;

  # ----------------------------------------
  # Constructor: door->new( @args );
  # input: N - how many doors?
  # returns: door object
  #
  method new($class: @args ) {
    my $self = bless {}, $class;
    $self->_init( @args );
    return $self;
  }

  # ----------------------------------------
  # class initializer.
  # input: how many doors?
  # sets N, creates N+1 doors ( door zero is not used ).
  #
  method _init( $N ) {
    $self->{N} = $N;
    $self->{doors} = [ ($CLOSED) x ($N+1) ];
  }

  # ----------------------------------------
  # $self->toggle( $door_number );
  # input: number of door to toggle.
  # OPEN a CLOSED door; CLOSE an OPEN  door.
  #
  method toggle( $which ) {
    $self->{doors}[$which] = ( $self->{doors}[$which] == $OPEN
                               ? $CLOSED
                               : $OPEN
        		     );
  }

  # ----------------------------------------
  # $self->toggle_n( $cycle );
  # input: number.
  # Toggle doors 0, $cycle, 2 * $cycle, 3 * $cycle, .. $self->{N}
  #
  method toggle_n( $n ) {
    $self->toggle($_)
      for map { $n * $_ }
          ( 1 .. int( $self->{N} / $n) );

  }

  # ----------------------------------------
  # $self->toggle_all();
  # Toggle every door, then every other door, every third door, ...
  #
  method toggle_all() {
    $self->toggle_n( $_ ) for ( 1 .. $self->{N} );
  }

  # ----------------------------------------
  # $self->print_open();
  # Print list of which doors are open.
  #
  method print_open() {
    say join ', ', grep { $self->{doors}[$_] == $OPEN } ( 1 ... $self->{N} );
  }
}

# ----------------------------------------------------------------------
# Main Thread
#
my $doors = doors->new(100);
$doors->toggle_all();
$doors->print_open();
```


## Phix

### unoptimised

```
sequence doors = repeat(false,100)
 
for i=1 to 100 do
    for j=i to 100 by i do
        doors[j] = not doors[j]
    end for
end for
 
for i=1 to 100 do
    if doors[i] == true then
        printf(1,"Door #%d is open.\n", i)
    end if
end for
```

**Output:**

```
Door #1 is open.
Door #4 is open.
Door #9 is open.
Door #16 is open.
Door #25 is open.
Door #36 is open.
Door #49 is open.
Door #64 is open.
Door #81 is open.
Door #100 is open.
```

### optimised

```
function doors(integer n)
-- returns the perfect squares<=n
integer door = 1, step = 1
sequence res = {}
    while door<=n do
        res &= door
        step += 2
        door += step
    end while
    return res
end function
 
?doors(100)
```

**Output:**

```
{1,4,9,16,25,36,49,64,81,100}
```


## Phixmonti

```mw
101 var l                           
0 l repeat                      

l for
    var s
    s l s 3 tolist
    for
        var i
        i get not i set
    endfor
endfor

l for
    var i
    i get
    if
        i print " " print
    endif
endfor
```

Another way

```mw
100 var n   /# Number of doors #/
0 n repeat  /# Make the doors #/

n for
    dup
    sqrt int
    dup * over == if 1 swap set else drop endif
endfor

n for
    "The door " print dup print " is " print
    get if "OPEN." else "closed." endif print nl
endfor
```

Optimized

```mw
100 sqrt for dup * print " " print endfor
```


## PHL

### unoptimized

```mw
module doors;

extern printf;

@Integer main [
	@Array<@Boolean> doors = new @Array<@Boolean>.init(100);
	var i = 1;
	while (i <= 100) {
		var j = i-1;
		while (j < 100) {
			doors.set(j, doors.get(j)::not);
			j = j + i;
		}
		i = i::inc;
	}
	i = 0;
	while (i < 100) {
		printf("%i %s\n", i+1, iif(doors.get(i), "open", "closed"));
		i = i::inc;
	}
	return 0;
]
```

### optimized

Translation of

:

C#

```mw
module var;

extern printf;

@Integer main [
	var door = 1;
	var incrementer = 0;
	var current = 1;
        while (current <= 100)
        {
		printf("Door %i ", current);
		if (current == door)
		{
			printf("open\n");
			incrementer = incrementer::inc;
			door = door + 2 * incrementer + 1;
		}
		else
			printf("closed\n");
		
		current = current + 1;
            
        }
	
	return 0;
]
```


## PHP

See: Demo **optimized**

```mw
<?php
for ($i = 1; $i <= 100; $i++) {
	$root = sqrt($i);
	$state = ($root == ceil($root)) ? 'open' : 'closed';
	echo "Door {$i}: {$state}\n";
}
?>
```

**unoptimized**

```mw
<?php
$doors = array_fill(1, 100, false);
for ($pass = 1; $pass <= 100; ++$pass) {
	for ($nr = 1; $nr <= 100; ++$nr) {
		if ($nr % $pass == 0) {
			$doors[$nr] = !$doors[$nr];
		}
	}
}
for ($nr = 1; $nr <= 100; ++$nr)
	printf("Door %d: %s\n", $nr, ($doors[$nr])?'open':'closed');
?>
```


## Picat

Non-optimized:

```mw
doors(N) => 
   Doors = new_array(N),
   foreach(I in 1..N) Doors[I] := 0 end,
   foreach(I in 1..N)
     foreach(J in I..I..N)
        Doors[J] := 1^Doors[J]
     end,
     if N <= 10 then
        print_open(Doors)
     end
   end,
   println(Doors),
   print_open(Doors),
   nl.

print_open(Doors) => println([I : I in 1..Doors.length, Doors[I] == 1]).
```

optimized version 1:

```mw
doors_opt(N) =>
  foreach(I in 1..N)
     Root = sqrt(I),
     println([I, cond(Root == 1.0*round(Root), open, closed)])
  end,
  nl.
```

optimized version 2:

```mw
doors_opt2(N) => 
  println([I**2 : I in 1..N, I**2 <= N]).
```


## PicoLisp

unoptimized

```mw
(let Doors (need 100)
   (for I 100
      (for (D (nth Doors I)  D  (cdr (nth D I)))
         (set D (not (car D))) ) )
   (println Doors) )
```

optimized

```mw
(let Doors (need 100)
   (for I (sqrt 100)
      (set (nth Doors (* I I)) T) )
   (println Doors) )
```

Output in both cases:

```
(T NIL NIL T NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL
 NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL
 NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T
 NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL N
IL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T)
```

With formatting:

```mw
(let Doors (need 100)
   (for I (sqrt 100)
      (set (nth Doors (* I I)) T) )
   (make
      (for (N . D) Doors
         (when D (link N)) ) ) )
```

Output:

```
(1 4 9 16 25 36 49 64 81 100)
```


## Piet

image


## Pike

```mw
array onehundreddoors()
{
    array doors = allocate(100);
    foreach(doors; int i;)
        for(int j=i; j<100; j+=i+1)
            doors[j] = !doors[j];
    return doors;
}
```

optimized version:

```mw
array doors = map(enumerate(100,1,1), lambda(int x)
                                      {  
                                          return sqrt((float)x)%1 == 0.0; 
                                      });
```

```mw
write("%{%d %d %d %d %d %d %d %d %d %d\n%}\n", doors/10)
```

output:

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


## PL/I

```mw
declare door(100) bit (1) aligned;
declare closed bit (1) static initial ('0'b),
        open   bit (1) static initial ('1'b);
declare (i, inc) fixed binary;

door = closed;
inc = 1;
do until (inc >= 100);
   do i = inc to 100 by inc;
      door(i) = ^door(i); /* close door if open; open it if closed. */
   end;
   inc = inc+1;
end;

do i = 1 to 100;
   put skip edit ('Door ', trim(i), ' is ') (a);
   if door(i) then put edit (' open.') (a);
   else put edit (' closed.') (a);
end;
```

See also #Polyglot:PL/I and PL/M

### PL/I-80

```mw
/* Solution to the 100 doors problem in PLI-80 */

hundred_doors:
  procedure options (main);

    %replace
      open_door by '1'b,
      closed_door by '0'b,
      numdoors by 100;

    dcl
      doors(1:numdoors) bit(1),
      (i, j) fixed bin(15);

    /* all doors are initially closed */
    do i = 1 to numdoors;
      doors(i) = closed_door;
    end;

    /* cycle through at increasing intervals and flip doors */
    do i = 1 to numdoors;
      j = i;
      do while (j <= numdoors);
        doors(j) = ^doors(j);
        j = j + i;
      end;
    end;

    /* show results - open doors should all be perfect squares */
    put skip list ('The open doors are:');
    do i = 1 to numdoors;
      if doors(i) = open_door then
        put edit (i) (F(4));
    end;

end hundred_doors;
```

**Output:**

```
The open doors are:   1   4   9  16  25  36  49  64  81 100
```

See also #Polyglot:PL/I and PL/M


## PL/M

Translation of

:

ALGOL W

```
100H: /* FIND THE FIRST FEW SQUARES VIA THE UNOPTIMISED DOOR FLIPPING METHOD */

    /* BDOS SYSTEM CALL */
    BDOS: PROCEDURE( FN, ARG );
        DECLARE FN BYTE, ARG ADDRESS;
        GO TO 5;
    END BDOS;

    /* PRINTS A BYTE AS A CHARACTER */
    PRINT$CHAR: PROCEDURE( CH );
        DECLARE CH BYTE;
        CALL BDOS( 2, CH );
    END PRINT$CHAR;

    /* PRINTS A BYTE AS A NUMBER */
    PRINT$BYTE: PROCEDURE( N );
        DECLARE N BYTE;
        DECLARE ( V, D3, D2 ) BYTE;
        V  = N;
        D3 = V MOD 10;
        IF ( V := V / 10 ) <> 0 THEN DO;
            D2 = V MOD 10;
            IF ( V := V / 10 ) <> 0 THEN CALL PRINT$CHAR( '0' + V );
            CALL PRINT$CHAR( '0' + D2 );
        END;
        CALL PRINT$CHAR( '0' + D3 );
    END PRINT$BYTE;

    DECLARE DOOR$DCL LITERALLY '101';
    DECLARE FALSE    LITERALLY '0';
    DECLARE CR       LITERALLY '0DH';
    DECLARE LF       LITERALLY '0AH';

    /* ARRAY OF DOORS - DOOR( I ) IS TRUE IF OPEN, FALSE IF CLOSED */
    DECLARE DOOR( DOOR$DCL ) BYTE;
    DECLARE ( I, J )         BYTE;

    /* SET ALL DOORS TO CLOSED */
    DO I = 0 TO LAST( DOOR ); DOOR( I ) = FALSE; END;
    /* REPEATEDLY FLIP THE DOORS */
    DO I = 1 TO LAST( DOOR );
       DO J = I TO LAST( DOOR ) BY I;
          DOOR( J ) = NOT DOOR( J );
       END;
    END;
    /* DISPLAY THE RESULTS */
    DO I = 1 TO LAST( DOOR );
       IF DOOR( I ) THEN DO;
          CALL PRINT$CHAR( ' ' );
          CALL PRINT$BYTE( I );
       END;
    END;
    CALL PRINT$CHAR( CR );
    CALL PRINT$CHAR( LF );

EOF
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```

See Also #Polyglot:PL/I and PL/M


## PL/SQL

**Unoptimized**

```mw
DECLARE
  TYPE doorsarray IS VARRAY(100) OF BOOLEAN;
  doors doorsarray := doorsarray();
BEGIN

doors.EXTEND(100);  --ACCOMMODATE 100 DOORS

FOR i IN 1 .. doors.COUNT  --MAKE ALL 100 DOORS FALSE TO INITIALISE
  LOOP
     doors(i) := FALSE;                    
  END LOOP;

FOR j IN 1 .. 100 --ITERATE THRU USING MOD LOGIC AND FLIP THE DOOR RIGHT OPEN OR CLOSE
 LOOP
      FOR k IN 1 .. 100
        LOOP
                  IF MOD(k,j)=0 THEN 
                     doors(k) := NOT doors(k); 
                  END IF;
        END LOOP;
 END LOOP;
 
FOR l IN 1 .. doors.COUNT  --PRINT THE STATUS IF ALL 100 DOORS AFTER ALL ITERATION
  LOOP
       DBMS_OUTPUT.PUT_LINE('DOOR '||l||' IS -->> '||CASE WHEN SYS.DBMS_SQLTCB_INTERNAL.I_CONVERT_FROM_BOOLEAN(doors(l)) = 'TRUE' 
                                                                THEN 'OPEN' 
                                                              ELSE 'CLOSED' 
                                                        END);
  END LOOP;

END;
```


## Plain English

Library:

Plain English-output

```mw
A flag list is a doubly linked list with a flag.
A door is a flag list.
A pass is a number.

To run:
  Start up.
  Pass doors given 1000 and 1000 passes.  
  Shut down.

To pass doors given a count and some passes:
  Create some doors given the count.
  Loop.
    Add 1 to a counter.
    If the counter is greater than the passes, break.
    Go through the doors given the counter and the passes.
  Repeat.
  Output the states of the doors.
  Destroy the doors.

To create some doors given a count:
  Loop.
    Add 1 to a counter.
    If the counter is greater than the count, exit.
    Allocate memory for a door.
    Clear the door's flag.
    Append the door to the doors.
  Repeat.

To go through some doors given a number and some passes:
  Put 0 into a counter.
  Loop.
    Add the number to the counter.
    If the counter is greater than the passes, exit.
    Pick a door from the doors given the number.
    Invert the door's flag.
  Repeat.

To pick a door from some doors given a number:
  Loop.
    Add 1 to a counter.
    If the counter is greater than the number, exit.
    Get the door from the doors.
    If the door is nil, exit.
  Repeat.

To output the states of some doors:
  Loop.
    Bump a counter.
    Get a door from the doors.
    If the door is nil, exit.
    If the door's flag is set, 
      Write "Door " then the counter then " is open" 
        then the CRLF string to StdOut; 
      Repeat.
    \Write "Door " then the counter then " is closed" 
      \then the CRLF string to StdOut.
  Repeat.
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


## Pluto

The Lua sample will run unchanged in Pluto, the following uses a Pluto specific for loop that iterates through is_open.

```
local is_open = {}

for pass = 1,100 do
    for door = pass,100,pass do
        is_open[door] = not is_open[door]
    end
end

for i,v in is_open do -- would be: "for i,v in pairs(is_open) do" in Lua
    if v then io.write( string.format( " %d", i ) ) end
end
```

**Output:**

```
 1 4 9 16 25 36 49 64 81 100
```


## Pointless

```mw
output =
  range(1, 100)
  |> map(visit(100))
  |> println

----------------------------------------------------------

toggle(state) =
  if state == Closed then Open else Closed

----------------------------------------------------------
-- Door state on iteration i is recursively
-- defined in terms of previous door state

visit(i, index) = cond {
  case (i == 0) Closed
  case (index % i == 0) toggle(lastState)
  else lastState
} where lastState = visit(i - 1, index)
```

**Output:**

```
[Open, Closed, Closed, Open, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Closed, Open]
```
