---
title: "100 doors (part 3/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/10
---

## C

### Unoptimized with Modulus % Operator

```mw
namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main(string[] args)
        {
            // Arrays are initialized to their type default values; the default for bool is false
            // Use false to indicate closed door
            bool[] doors = new bool[100];

            //For each pass...
            for (int p = 0; p < 100; p++)//number of passes
            {
                //For each door to toggle...
                for (int d = 0; d < 100; d++)//door number
                {
                    if ((d + 1) % (p + 1) == 0)
                    {
                        doors[d] = !doors[d];
                    }
                }
            }

            //Output the results.
            Console.WriteLine("Passes Completed!!!  Here are the results:");
            for (int d = 0; d < 100; d++)
            {
                if (doors[d])
                {
                    Console.WriteLine(String.Format("Door #{0}: Open", d + 1));
                }
                else
                {
                    Console.WriteLine(String.Format("Door #{0}: Closed", d + 1));
                }
            }
            Console.ReadKey(true);
        }
    }
}
```

### Optimized for Orthogonality

(This version demonstrates a different thought pattern during development, where operation and presentation are separated. It could easily be refactored so that the operations to determine which doors are opened and to display the list of doors would be in separate methods, at which point it would become simple to extract them to separate classes and employ a DI pattern to switch the algorithm or display mechanism being used. It also keeps the calculation clear and concise.)

```mw
namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main(string[] args)
        {
            //Perform the operation.
            bool[] doors = new bool[100];
            int n = 0;
            int d;
            while ((d = (++n * n)) <= 100)
                doors[d - 1] = true;

            //Perform the presentation.
            for (d = 0; d < doors.Length; d++)
                Console.WriteLine("Door #{0}: {1}", d + 1, doors[d] ? "Open" : "Closed");
            Console.ReadKey(true);
        }
    }
}
```

### Unoptimized but Concise

```mw
namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main()
        {
            bool[] doors = new bool[100];

            //The number of passes can be 1-based, but the number of doors must be 0-based.
            for (int p = 1; p <= 100; p++)
                for (int d = p - 1; d < 100; d += p)
                    doors[d] = !doors[d];
            for (int d = 0; d < 100; d++)
                Console.WriteLine("Door #{0}: {1}", d + 1, doors[d] ? "Open" : "Closed");
            Console.ReadKey(true);
        }
    }
}
```

### Optimized for brevity

```mw
namespace ConsoleApplication1
{
    using System;
    class Program
    {
        static void Main()
        {
            double n;

            //If the current door number is the perfect square of an integer, say it is open, else say it is closed.
            for (int d = 1; d <= 100; d++)
                Console.WriteLine("Door #{0}: {1}", d, (n = Math.Sqrt(d)) == (int)n ? "Open" : "Closed");
            Console.ReadKey(true);
        }
    }
}
```

### Optimized for Flexibility

This version supports altering the number of doors through console commands. Its main intent is to be flexible and easy to use.

```mw
using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Clear();
        Console.WriteLine("Input a number of doors to calculate, then press enter");
        StartCalculator();
    }
    
    static void StartCalculator()
    {
        //The number to calculate is input here
        string input = Console.ReadLine();
        Console.Clear();
        
        try
        {
            //The program attempts to convert the string to an int
            //Exceptions will be caught on this line
            int numberOfDoors = Convert.ToInt32(input);
            
            //Will call method recursively if input number is less than 1
            if (numberOfDoors <= 0)
            {
                Console.WriteLine("Please use a number greater than 0");
                StartCalculator();
            }
            
            //The program then starts the calculation process
            Calculate(numberOfDoors);
            
            //After calculation process is finished, restart method is called
            RestartCalculator();
        }
        catch(FormatException)
        {
            //Code will be executed if the number has a decimal or has an unrecognizable symbol
            Console.WriteLine("Unable to read. Please use a real number without a decimal");
            StartCalculator();
        }
        catch (OverflowException)
        {
            //Code will be executed if number is too long
            Console.WriteLine("You number is too long");
            StartCalculator();
        }
    }
    
    static void Calculate(int numberOfDoors)
    {
        //Increases numberOfDoors by 1 since array starts at 0
        numberOfDoors++;
        
        //Dictionary key represents door number, value represents if the door is open
        //if value == true, the door is open
        Dictionary<int, bool> doors = new Dictionary<int, bool>();
        
        //Creates Dictionary size of numberOfDoors, all initialized at false
        for(int i = 0; i < numberOfDoors; i++)
        {
            doors.Add(i, false);
        }
        
        //Creates interval between doors, starting at 0, while less than numberOfDoors
        for (int doorInterval = 0; doorInterval < numberOfDoors; doorInterval++)
        {
            //Will alter every cubby at doorInterval
            //1 needs to be added since doorInterval will start at 0 and end when equal to numberOfDoors
            for(int i = 0; i < numberOfDoors; i += doorInterval + 1)
            {
                //Changes a false value to true and vice versa
                doors[i] = doors[i] ? false: true;
            }
        }
        
        //Writes each door and whether it is open or closed
        for(int i = 0; i < numberOfDoors; i++)
        {
            //Skips over door 0
            if (i == 0) continue;
            //Writes open if door value is true, writes closed if door value is false
            Console.WriteLine("Door " + (i) + " is " + (doors[i] ? "open" : "closed"));
        }
    }
    
    static void RestartCalculator()
    {   
        Console.WriteLine("Press any key to restart");
        Console.ReadKey(true);
        Main();
    }
}
```


## C++

Works with

:

GCC

version 4.1.2 20061115 (prerelease) (SUSE Linux)

**unoptimized**

```mw
#include <iostream>

int main()
{
  bool is_open[100] = { false };

  // do the 100 passes
  for (int pass = 0; pass < 100; ++pass)
    for (int door = pass; door < 100; door += pass+1)
      is_open[door] = !is_open[door];

  // output the result
  for (int door = 0; door < 100; ++door)
    std::cout << "door #" << door+1 << (is_open[door]? " is open." : " is closed.") << std::endl;
  return 0;
}
```

**optimized** This optimized version makes use of the fact that finally only the doors with square index are open, as well as the fact that ${\displaystyle (n+1)^{2}=1+3+5+\ldots +(2n+1)}$ .

```mw
#include <iostream>

int main()
{
  int square = 1, increment = 3;
  for (int door = 1; door <= 100; ++door)
  {
    std::cout << "door #" << door;
    if (door == square)
    {
      std::cout << " is open." << std::endl;
      square += increment;
      increment += 2;
    }
    else
      std::cout << " is closed." << std::endl;
  }
  return 0;
}
```

The only calculation that's really needed:

```mw
#include <iostream> //compiled with "Dev-C++" , from RaptorOne

int main()
{
    for(int i=1; i*i<=100; i++)
            std::cout<<"Door "<<i*i<<" is open!"<<std::endl;
}
```

Compile time computation using C++17 to produce fastest runtime.

```mw
#include <iostream>    // compiled with clang (tags/RELEASE_600/final)
#include <type_traits> // or g++ (GCC) 7.3.1 20180406 -- from hare1039
namespace functional_list // basic building block for template meta programming
{
struct NIL
{
	using head = NIL;
	using tail = NIL;
	friend std::ostream& operator << (std::ostream& os, NIL const) { return os; }
};

template <typename H, typename T = NIL>
struct list
{
	using head = H;
	using tail = T;
};

template <int i>
struct integer
{
	static constexpr int value = i;
	friend std::ostream& operator << (std::ostream& os, integer<i> const) { os << integer<i>::value; return os;}
};

template <typename L, int nTH> constexpr
auto at()
{
	if constexpr (nTH == 0)
		return (typename L::head){};
	else if constexpr (not std::is_same_v<typename L::tail, NIL>) 
		return at<typename L::tail, nTH - 1>();
	else
		return NIL{};
}
template <typename L, int nTH>
using at_t = decltype(at<L, nTH>());

template <typename L, typename elem> constexpr
auto prepend() { return list<elem, L>{}; }

template <typename L, typename elem>
using prepend_t = decltype(prepend<L, elem>());
	
template <int Size, typename Dat = integer<0>> constexpr
auto gen_list()
{
	if constexpr (Size == 0)
		return NIL{};
	else
	{
		using next = decltype(gen_list<Size - 1, Dat>());
		return prepend<next, Dat>();
	}
}
template <int Size, typename Dat = integer<0>>
using gen_list_t = decltype(gen_list<Size, Dat>());
	
} namespace fl = functional_list;

constexpr int door_amount = 101; // index from 1 to 100

template <typename L, int current, int moder> constexpr
auto construct_loop()
{
	using val_t = fl::at_t<L, current>;
	if constexpr (std::is_same_v<val_t, fl::NIL>)
		return fl::NIL{};
	else
	{
		constexpr int val = val_t::value;
		using val_add_t = fl::integer<val + 1>;
		using val_old_t = fl::integer<val>;
	
		if constexpr (current == door_amount)
		{
			if constexpr(current % moder == 0)
				return fl::list<val_add_t>{};
			else
				return fl::list<val_old_t>{};
		}
		else
		{
			using sub_list = decltype(construct_loop<L, current + 1, moder>());
			if constexpr(current % moder == 0)
				return fl::prepend<sub_list, val_add_t>();
			else
				return fl::prepend<sub_list, val_old_t>();
		}
	}
}

template <int iteration> constexpr
auto construct()
{
	if constexpr (iteration == 1) // door index = 1
	{
		using l = fl::gen_list_t<door_amount>;
		return construct_loop<l, 0, iteration>();
	}
	else
	{
		using prev_iter_list = decltype(construct<iteration - 1>());
		return construct_loop<prev_iter_list, 0, iteration>();
	}
}

template <typename L, int pos> constexpr
void show_ans()
{
	if constexpr (std::is_same_v<typename L::head, fl::NIL>)
		return;
	else
	{
		if constexpr (L::head::value % 2 == 1)
			std::cout << "Door " << pos << " is opened.\n";
		show_ans<typename L::tail, pos + 1>();
	}
}

int main()
{
	using result = decltype(construct<100>());
	show_ans<result, 0>();
}
```


## C1R

```mw
100_doors
```


## Caché ObjectScript

```mw
 for i=1:1:100 {
	 set doors(i) = 0
 }
 for i=1:1:100 {
	 for door=i:i:100 {
		  Set doors(door)='doors(door)
	 }
 }
 for i = 1:1:100
 {
	if doors(i)=1 write i_": open",!
 }
```

Output:

```mw
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
```


## Ceylon

```mw
shared void run() {
    print("Open doors (naive):     ``naive()``
           Open doors (optimized): ``optimized()``");
    
}

shared {Integer*} naive(Integer count = 100) {
    variable value doors = [ for (_ in 1..count) closed ];
    for (step in 1..count) {
        doors = [for (i->door in doors.indexed) let (index = i+1) if (step == 1 || step.divides(index)) then door.toggle() else door ];
    }
    return doors.indexesWhere((door) => door == opened).map(1.plusInteger);
}

shared {Integer*} optimized(Integer count = 100) =>
        { for (i in 1..count) i*i }.takeWhile(count.notSmallerThan);

shared abstract class Door(shared actual String string) of opened | closed {
    shared formal Door toggle();
}
object opened extends Door("opened") { toggle() => closed; }
object closed extends Door("closed") { toggle() => opened; }
```

**Output:**

```
Open doors (naive):     { 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 }
Open doors (optimized): { 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 }
```


## Clarion

```mw
    program

    map
    end

MAX_DOOR_NUMBER         equate(100)
CRLF                    equate('<13,10>')

Doors                   byte,dim(MAX_DOOR_NUMBER)
Pass                    byte
DoorNumber              byte
DisplayString           cstring(2000)

ResultWindow            window('Result'),at(,,133,291),center,double,auto
                            prompt('Door states:'),at(8,4),use(?PromptTitle)
                            text,at(8,16,116,266),use(DisplayString),boxed,vscroll,font('Courier New',,,,CHARSET:ANSI),readonly
                        end

    code

    Doors :=: false
    loop Pass = 1 to MAX_DOOR_NUMBER
        loop DoorNumber = Pass to MAX_DOOR_NUMBER by Pass
            Doors[DoorNumber] = choose(Doors[DoorNumber], false, true)
        end
    end

    clear(DisplayString)
    loop DoorNumber = 1 to MAX_DOOR_NUMBER
        DisplayString = DisplayString & format(DoorNumber, @n3) & ' is ' & choose(Doors[DoorNumber], 'opened', 'closed') & CRLF
    end
    open(ResultWindow)
    accept
    end
    close(ResultWindow)

    return
```


## Clio

**Unoptimized**

```mw
fn visit-doors doors step:
  if step > 100: doors
  else:
    [1:100]
      -> * fn index:
            if index % step: doors[(index - 1)]
            else: not doors[(index - 1)]
      -> visit-doors (step + 1)

[1:100] -> * n: false -> visit-doors 1 => doors
[1:100] -> * (@eager) fn i:
  doors[(i - 1)]
    -> if = true: #open
            else: #closed
    -> print #Door i #is @
```

**Optimized**

```mw
[1:100] -> * (@eager) fn i:
  i ^ 0.5
    -> eq @ (transform i: floor)
    -> if = true: #open
            else: #closed
    -> print #Door i #is @
```


## CLIPS

**Unoptimized**

```mw
(deffacts initial-state
  (door-count 100)
)

(deffunction toggle
  (?state)
  (switch ?state
    (case "open" then "closed")
    (case "closed" then "open")
  )
)

(defrule create-doors-and-visits
  (door-count ?count)
  =>
  (loop-for-count (?num 1 ?count) do
    (assert (door ?num "closed"))
    (assert (visit-from ?num ?num))
  )
  (assert (doors initialized))
)

(defrule visit
  (door-count ?max)
  ?visit <- (visit-from ?num ?step)
  ?door <- (door ?num ?state)
  =>
  (retract ?visit)
  (retract ?door)
  (assert (door ?num (toggle ?state)))
  (if
    (<= (+ ?num ?step) ?max)
    then
    (assert (visit-from (+ ?num ?step) ?step))
  )
)

(defrule start-printing
  (doors initialized)
  (not (visit-from ? ?))
  =>
  (printout t "These doors are open:" crlf)
  (assert (print-from 1))
)

(defrule print-door
  (door-count ?max)
  ?pf <- (print-from ?num)
  (door ?num ?state)
  =>
  (retract ?pf)
  (if
    (= 0 (str-compare "open" ?state))
    then
    (printout t ?num " ")
  )
  (if
    (< ?num ?max)
    then
    (assert (print-from (+ ?num 1)))
    else
    (printout t crlf "All other doors are closed." crlf)
  )
)
```

**Optimized**

```mw
(deffacts initial-state
  (door-count 100)
)

(deffunction is-square
  (?num)
  (= (sqrt ?num) (integer (sqrt ?num)))
)

(defrule check-doors
  (door-count ?count)
  =>
  (printout t "These doors are open:" crlf)
  (loop-for-count (?num 1 ?count) do
    (if (is-square ?num) then
      (printout t ?num " ")
    )
  )
  (printout t crlf "All other doors are closed." crlf)
)
```


## Clojure

**Unoptimized / mutable array**

```mw
(defn doors []
  (let [doors (into-array (repeat 100 false))]
    (doseq [pass   (range 1 101) 
            i      (range (dec pass) 100 pass) ]
      (aset doors i (not (aget doors i))))
    doors))   

(defn open-doors [] (for [[d n] (map vector (doors) (iterate inc 1)) :when d] n))

(defn print-open-doors []
  (println 
    "Open doors after 100 passes:"
    (apply str (interpose ", " (open-doors)))))
```

**Unoptimized / functional**

```mw
(defn doors []
  (reduce (fn [doors toggle-idx] (update-in doors [toggle-idx] not))
          (into [] (repeat 100 false))
          (for [pass   (range 1 101)
                i      (range (dec pass) 100 pass) ]
            i)))

(defn open-doors [] (for [[d n] (map vector (doors) (iterate inc 1)) :when d] n))

(defn print-open-doors []
  (println 
    "Open doors after 100 passes:"
    (apply str (interpose ", " (open-doors)))))
```

**Alternative Unoptimized / functional**

```mw
(defn open-doors []
  (->> (for [step (range 1 101), occ (range step 101 step)] occ)
       frequencies
       (filter (comp odd? val))
       keys
       sort))

(defn print-open-doors []
  (println 
    "Open doors after 100 passes:"
    (apply str (interpose ", " (open-doors)))))
```

**Optimized / functional**

```mw
(defn doors []
	(reduce (fn [doors idx] (assoc doors idx true)) 
	        (into [] (repeat 100 false))
	        (map #(dec (* % %)) (range 1 11))))

(defn open-doors [] (for [[d n] (map vector (doors) (iterate inc 1)) :when d] n))

(defn print-open-doors []
  (println 
    "Open doors after 100 passes:"
    (apply str (interpose ", " (open-doors)))))
```

**Alternative Optimized / functional**

```mw
(defn open-doors [] (->> (iterate inc 1) (map #(* % %)) (take-while #(<= % 100))))

(defn print-open-doors []
  (println 
    "Open doors after 100 passes:"
    (apply str (interpose ", " (open-doors)))))
```


## CLU

```mw
start_up = proc ()
    max = 100
    po: stream := stream$primary_output()
    open: array[bool] := array[bool]$fill(1, max, false)

    for pass: int in int$from_to(1, max) do
        for door: int in int$from_to_by(pass, max, pass) do
            open[door] := ~open[door]
        end
    end

    for door: int in array[bool]$indexes(open) do
        if open[door] then
            stream$putl(po, "Door " || int$unparse(door) || " is open.")
        end
    end
end start_up
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


## COBOL

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID. 100Doors.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 Current-n      PIC 9(3).
       01 StepSize       PIC 9(3).
       01 DoorTable.
          02 Doors       PIC 9(1)   OCCURS 100 TIMES.
             88 ClosedDoor          VALUE ZERO.
       01 Idx            PIC 9(3).

       PROCEDURE DIVISION.
       Begin.
           INITIALIZE DoorTable
           PERFORM VARYING StepSize FROM 1 BY 1 UNTIL StepSize > 100
             PERFORM VARYING Current-n FROM StepSize BY StepSize
                     UNTIL Current-n > 100
               SUBTRACT Doors (Current-n) FROM 1 GIVING Doors (Current-n)
             END-PERFORM
           END-PERFORM

           PERFORM VARYING Idx FROM 1 BY 1
                   UNTIL Idx > 100
             IF ClosedDoor (Idx)
               DISPLAY Idx " is closed."
             ELSE
               DISPLAY Idx " is open."
             END-IF
           END-PERFORM

           STOP RUN
           .
```


## Coco

We use the naive algorithm.

```mw
doors = [false] * 100

for pass til doors.length
    for i from pass til doors.length by pass + 1
        ! = doors[i]

for i til doors.length
    console.log 'Door %d is %s.', i + 1, if doors[i] then 'open' else 'closed'
```


## CoffeeScript

**unoptimized**:

```mw
doors = []
 
for pass in [1..100]
  for i in [pass..100] by pass
    doors[i] = !doors[i]
 
console.log "Doors #{index for index, open of doors when open} are open"
 
# matrix output
console.log doors.map (open) -> +open
```

**optimized**:

```mw
isInteger = (i) -> Math.floor(i) == i

console.log door for door in [1..100] when isInteger Math.sqrt door
```

**ultra-optimized**:

```mw
console.log Math.pow(i,2) for i in [1..10]
```


## ColdFusion

**Basic Solution: Returns List of 100 values: 1=open 0=closed**

```mw
	doorCount = 1;
	doorList = "";
	// create all doors and set all doors to open
	while (doorCount LTE 100) {
		doorList = ListAppend(doorList,"1");
		doorCount = doorCount + 1;
	}
	loopCount = 2;
	doorListLen = ListLen(doorList);
	while (loopCount LTE 100) {
		loopDoorListCount = 1;
		while (loopDoorListCount LTE 100) {
			testDoor = loopDoorListCount / loopCount;
			if (testDoor EQ Int(testDoor)) {
				checkOpen = ListGetAt(doorList,loopDoorListCount);
				if (checkOpen EQ 1) {
					doorList = ListSetAt(doorList,loopDoorListCount,"0");
				} else {
					doorList = ListSetAt(doorList,loopDoorListCount,"1");
				}
			}
			loopDoorListCount = loopDoorListCount + 1;
		}
		loopCount = loopCount + 1;
	}
```

**Squares of Integers Solution: Returns List of 100 values: 1=open 0=closed**

```mw
	doorCount = 1;
	doorList = "";
	loopCount = 1;
	while (loopCount LTE 100) {
		if (Sqr(loopCount) NEQ Int(Sqr(loopCount))) {
			doorList = ListAppend(doorList,0);
		} else {
			doorList = ListAppend(doorList,1);
		}
		loopCount = loopCount + 1;
	}
```

**Display only**

```mw
// Display all doors
<cfloop from="1" to="100" index="x">
    Door #x# Open: #YesNoFormat(ListGetAt(doorList,x))#<br />
</cfloop>

// Output only open doors
<cfloop from="1" to="100" index="x">
    <cfif ListGetAt(doorList,x) EQ 1>
        #x#<br />
    </cfif>
</cfloop>
```

**Another Route**

```mw
<Cfparam name="doorlist" default="">
<cfloop from="1" to="100" index="i">
    <Cfset doorlist = doorlist & 'c,'>
</cfloop>
<cfloop from="1" to="100" index="i">
    <Cfloop from="1" to="100" index="door" step="#i#">
    <Cfif listgetat(doorlist, door) eq 'c'>
        <Cfset doorlist = listsetat(doorlist, door, 'O')>
    <Cfelse>
        <Cfset doorlist = listsetat(doorlist, door, 'c')>
    </Cfif>
    </Cfloop>
</cfloop>
<Cfoutput>#doorlist#</Cfoutput>
```


## Comal

```mw
0010 DIM doors#(100)
0020 FOR pass#:=1 TO 100 DO
0030   FOR door#:=pass# TO 100 STEP pass# DO doors#(door#):=NOT doors#(door#)
0040 ENDFOR pass#
0050 FOR door#:=1 TO 100 DO
0060   IF doors#(door#) THEN PRINT "Door ",door#," is open."
0070 ENDFOR door#
0080 END
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


## Commodore BASIC

```mw
10 D=100: DIMD(D): P=1
20 PRINT CHR$(147);"PASS: ";P
22 FOR I=P TO D STEP P: D(I)=NOTD(I): NEXT
30 IF P=100 THEN 40
32 P=P+1: GOTO20
40 PRINT: PRINT"THE FOLLOWING DOORS ARE OPEN: "
42 FOR I=1 TO D: IF D(I)=-1 THEN PRINTI;
44 NEXT
```


## Common Lisp

**Unoptimized / functional** This is a very unoptimized version of the problem, using recursion and quite considerable list-copying. It emphasizes the functional way of solving this problem.

```mw
(defun visit-door (doors doornum value1 value2)
  "visits a door, swapping the value1 to value2 or vice-versa"
  (let ((d (copy-list doors))
        (n (- doornum 1)))
    (if (eql  (nth n d) value1)
        (setf (nth n d) value2)
      (setf (nth n d) value1))
    d))

(defun visit-every (doors num iter value1 value2)
  "visits every 'num' door in the list"
  (if (> (* iter num) (length doors))
      doors
    (visit-every (visit-door doors (* num iter) value1 value2)
                 num
                 (+ 1 iter)
                 value1
                 value2)))

(defun do-all-visits (doors cnt value1 value2)
  "Visits all doors changing the values accordingly"
  (if (< cnt 1)
      doors
    (do-all-visits (visit-every doors cnt 1 value1 value2)
                   (- cnt 1)
                   value1
                   value2)))

(defun print-doors (doors)
  "Pretty prints the doors list"
  (format T "~{~A ~A ~A ~A ~A ~A ~A ~A ~A ~A~%~}~%" doors))

(defun start (&optional (size 100))
  "Start the program"
  (let* ((open "_")
         (shut "#")
         (doors (make-list size :initial-element shut)))
    (print-doors (do-all-visits doors size open shut))))
```

**Unoptimized, imperative** This is a version that closely follows the problem description and is still quite short. Of all the presented solutions it might be closest to "idiomatic Common Lisp".

```mw
(define-modify-macro toggle () not)

(defun 100-doors ()
  (let ((doors (make-array 100)))
    (dotimes (i 100)
      (loop for j from i below 100 by (1+ i)
	 do (toggle (svref doors j))))
    (dotimes (i 100)
      (format t "door ~a: ~:[closed~;open~]~%" (1+ i) (svref doors i)))))
```

**Unoptimized,** n-doors.

```mw
(defun doors (z &optional (w (make-list z)) (n 1))
  (if (> n z) w (doors z (toggle w n z) (1+ n))))

(defun toggle (w m z)
  (loop for a in w for n from 1 to z
        collect (if (zerop (mod n m)) (not a) a)))

> (doors 100)
(T NIL NIL T NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL
 NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL
 NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL
 NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T
 NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T)
```

**Optimized,** n-doors.

```mw
(defun doors (n)
  (loop for a from 1 to n collect
        (zerop (mod (sqrt a) 1))))
 
> (doors 100)
(T NIL NIL T NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL
 NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL
 NIL NIL NIL NIL NIL NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL
 NIL NIL T NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T
 NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL NIL T)
```

**Optimized** This is an optimized version, using the perfect square algorithm.

```mw
(defun 100-doors ()
  (let ((doors (make-array 100)))
    (dotimes (i 10)
      (setf (svref doors (* i i)) t))
    (dotimes (i 100)
      (format t "door ~a: ~:[closed~;open~]~%" (1+ i) (svref doors i)))))
```

**Optimized 2** Another optimized version, with finer granular separation of functionality (might be a bit excessive).

```mw
(defun perfect-square-list (n)                       
  "Generates a list of perfect squares from 0 up to n"
  (loop for i from 1 to (isqrt n) collect (expt i 2))) 
 
(defun print-doors (doors)
  "Pretty prints the doors list"
  (format T "~{~A ~A ~A ~A ~A ~A ~A ~A ~A ~A~%~}~%" doors))

(defun open-door (doors num open)
  "Sets door at num to open"
  (setf (nth (- num 1) doors) open)) 

(defun visit-all (doors vlist open)
  "Visits and opens all the doors indicated in vlist"
  (dolist (dn vlist doors)
    (open-door doors dn open)))

(defun start2 (&optional (size 100))                        
  "Start the program"
  (print-doors
   (visit-all (make-list size :initial-element '\#)
              (perfect-square-list size)
              '_)))
```

**Optimized (2)** This version displays a much more functional solution through the use of MAPCAR.

```mw
(let  ((i 0))
    (mapcar (lambda (x)
                (if (zerop (mod (sqrt (incf i)) 1))
                    "_" "#"))
            (make-list 100)))
```


## Component Pascal

BlackBox Component Builder

```
MODULE Doors100;
IMPORT StdLog;

PROCEDURE Do*;
VAR
       i,j: INTEGER;
       closed: ARRAY 101 OF BOOLEAN;
BEGIN
       (* initialization of closed to true *)
       FOR i := 0 TO LEN(closed) - 1 DO closed[i] := TRUE END;
       (* process *)
       FOR i := 1 TO LEN(closed)  DO;
               j := 1;
               WHILE j < LEN(closed) DO
                       IF j MOD i = 0 THEN closed[j] := ~closed[j] END;INC(j)
               END
       END;
       (* print results *)
       i := 1;
       WHILE  i < LEN(closed)  DO
               IF (i - 1) MOD 10 = 0 THEN StdLog.Ln END;
               IF closed[i] THEN StdLog.String("C ") ELSE StdLog.String("O ") END;
               INC(i)
       END;
END Do;
END Doors100.
```

Execute: ^Q Doors100.Do

**Output:**

```
O C C O C C C C O C 
C C C C C O C C C C 
C C C C O C C C C C 
C C C C C O C C C C 
C C C C C C C C O C 
C C C C C C C C C C 
C C C O C C C C C C 
C C C C C C C C C C 
O C C C C C C C C C 
C C C C C C C C C O 
```


## Cowgol

```mw
include "cowgol.coh";

var doors: uint8[101];  # one extra so we can start at 1
var pass: @indexof doors;
var door: @indexof doors;

MemZero(&doors as [uint8], @bytesof doors);

pass := 1;
while pass <= 100 loop
    door := pass;
    while door <= 100 loop
        doors[door] := 1-doors[door];
        door := door + pass;
    end loop;
    pass := pass + 1;
end loop;

door := 1;
while door <= 100 loop
    if doors[door] == 1 then
        print_i8(door);
        print(" is open\n");
    end if;
    door := door + 1;
end loop;
```

**Output:**

```
1 is open
4 is open
9 is open
16 is open
25 is open
36 is open
49 is open
64 is open
81 is open
100 is open
```


## Craft Basic

```mw
do

	let i = i + 1
	print i * i, " ",

loop i * i < 100
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100 
```


## Crystal

```mw
doors = Array.new(100, false)

1.upto(100) do |i|
  i.step(by: i, to: 100) do |j|
    doors[j - 1] = !doors[j - 1]
  end
end

doors.each_with_index do |open, i|
  puts "Door #{i + 1} is #{open ? "open" : "closed"}"
end
```


## D

### Unoptimized

```mw
import std.stdio;
const N = 101; // #doors + 1
void main() {
  bool[N] doors = false;
  for(auto door=1; door<N; door++ ) {
    for(auto i=door; i<N; i+=door ) doors[i] = !doors[i];
    if (doors[door]) write(door, " ");
  }
}
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100 
```

### Optimized

The problem of the 100 doors is an algorithm to find the squares between 1 and 100.

This optimized version prints these squares using an alternative algorithm based on ${\displaystyle \sum _{i=1}^{n}(2i-1)=n^{2}}$

```mw
import std.stdio;
const N = 101; // #doors + 1
void main() {
  for( auto door=1,s=3; door<N; door+=s, s+=2 )
    write(door, " ");
}
```

**Output:**

```
1 4 9 16 25 36 49 64 81 100 
```

### Other proposals

```mw
import std.stdio, std.algorithm, std.range;

enum DoorState : bool { closed, open }
alias Doors = DoorState[];

Doors flipUnoptimized(Doors doors) pure nothrow {
    doors[] = DoorState.closed;

    foreach (immutable i; 0 .. doors.length)
        for (ulong j = i; j < doors.length; j += i + 1)
            if (doors[j] == DoorState.open)
                doors[j] = DoorState.closed;
            else
                doors[j] = DoorState.open;
    return doors;
}

Doors flipOptimized(Doors doors) pure nothrow {
    doors[] = DoorState.closed;
    for (int i = 1; i ^^ 2 <= doors.length; i++)
        doors[i ^^ 2 - 1] = DoorState.open;
    return doors;
}

void main() {
    auto doors = new Doors(100);

    foreach (const open; [doors.dup.flipUnoptimized,
                          doors.dup.flipOptimized])
        iota(1, open.length + 1).filter!(i => open[i - 1]).writeln;
}
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**Unoptimized. Demonstrates very basic language syntax/features.** Program output allows to see what the code is doing:

```mw
import std.stdio;

void printAllDoors(bool[] doors)
{
   // Prints the state of all the doors
   foreach(i, door; doors)
   {
      writeln("#: ", i + 1, (door) ? " open" : " closed");
      }
}
void main()
{
   bool[100] doors = false;   //Create 100 closed doors
   for(int a = 0; a < 100; ++a) {
      writefln("Pass #%s; visiting every %s door.", a + 1, a + 1);  // Optional
	 for(int i = a; i < 100; i += (a + 1)) {
	 writefln("Visited door %s", i + 1);  //Optional
	 doors[i] = !doors[i];
	 }
      writeln();  // Optional
      }
   printAllDoors(doors);   // Prints the state of each door
}
```


## Dafny

The InitializeDoors function demonstrates some of Dafny's advanced features.

```mw
datatype Door = Closed | Open

method InitializeDoors(n:int) returns (doors:array<Door>)
  // Precondition: n must be a valid array size.
  requires n >= 0
  // Postcondition: doors is an array, which is not an alias for any other
  // object, with a length of n, all of whose elements are Closed. The "fresh"
  // (non-alias) condition is needed to allow doors to be modified by the
  // remaining code.
  ensures doors != null && fresh(doors) && doors.Length == n
  ensures forall j :: 0 <= j < doors.Length ==> doors[j] == Closed;
{
  doors := new Door[n];
  var i := 0;
  // Invariant: i is always a valid index inside the loop, and all doors less
  // than i are Closed. These invariants are needed to ensure the second
  // postcondition.
  while i < doors.Length
    invariant i <= doors.Length
    invariant forall j :: 0 <= j < i ==> doors[j] == Closed;
  {
    doors[i] := Closed;
    i := i + 1;
  }
}

method Main ()
{
  var doors := InitializeDoors(100);

  var pass := 1;
  while pass <= doors.Length
  {
    var door := pass;
    while door < doors.Length
    {
      doors[door] := if doors[door] == Closed then Open else Closed;
      door := door + pass;
    }
    pass := pass + 1;
  }
  var i := 0;
  while i < doors.Length
  {
    print i, " is ", if doors[i] == Closed then "closed\n" else "open\n";
    i := i + 1;
  }
}
```
