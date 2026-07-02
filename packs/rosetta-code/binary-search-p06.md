---
title: "Binary search (part 6/6)"
source: https://rosettacode.org/wiki/Binary_search
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/6
---

## Simula

```mw
BEGIN

    INTEGER PROCEDURE BINARYSEARCHREC(A, LVALUE);
        INTEGER ARRAY A;
        INTEGER LVALUE; ! VALUE IS A KEY WORD ;
    BEGIN

        INTEGER PROCEDURE SEARCH(LOW, HIGH);
            INTEGER LOW, HIGH;
        BEGIN
            INTEGER MID;
            ! INVARIANTS: VALUE > A[I] FOR ALL I < LOW
                          VALUE < A[I] FOR ALL I > HIGH ;
            MID := (LOW + HIGH) // 2;
            SEARCH := IF HIGH < LOW THEN -LOW - 1
                 ELSE IF A(MID) > LVALUE THEN SEARCH(LOW, MID-1)
                 ELSE IF A(MID) < LVALUE THEN SEARCH(MID+1, HIGH)
                 ELSE MID;
        END SEARCH;

        BINARYSEARCHREC := SEARCH(LOWERBOUND(A, 1), UPPERBOUND(A, 1));
    END BINARYSEARCHREC;

    INTEGER PROCEDURE BINARYSEARCH(A, LVALUE);
        INTEGER ARRAY A;
        INTEGER LVALUE; ! VALUE IS A KEY WORD ;
    BEGIN
        INTEGER LOW, HIGH, MID;
        BOOLEAN FOUND;

        LOW := LOWERBOUND(A, 1);
        HIGH := UPPERBOUND(A, 1);
        WHILE NOT FOUND AND LOW <= HIGH DO BEGIN
            ! INVARIANTS: LVALUE > A(I) FOR ALL I < LOW
                          LVALUE < A(I) FOR ALL I > HIGH ;
            MID := (LOW + HIGH) // 2;
            IF A(MID) > LVALUE THEN
                HIGH := MID - 1
            ELSE IF A(MID) < LVALUE THEN
                LOW := MID + 1
            ELSE
                FOUND := TRUE;
        END;
        ! LVALUE WOULD BE INSERTED AT INDEX "LOW" ;
        BINARYSEARCH := IF FOUND THEN MID ELSE -LOW - 1;
    END BINARYSEARCH;

    COMMENT ** CAUTION ** ONLY WORKS FOR ARRAY LOWER BOUND=0;
    INTEGER ARRAY HAYSTACK(0:9);
    INTEGER I, J, K, NEEDLE;

    OUTTEXT("ARRAY = (");
    I := LOWERBOUND(HAYSTACK, 1);
    FOR J := 1, 6, 17, 29, 45, 78, 79, 87, 95, 100 DO BEGIN
        HAYSTACK(I) := J;
        OUTINT(HAYSTACK(I), 0);
        IF I < UPPERBOUND(HAYSTACK, 1) THEN OUTTEXT(", ");
        I := I + 1;
    END;
    OUTTEXT(")");
    OUTIMAGE;
    OUTIMAGE;

    FOR NEEDLE:= 0, 1, 7, 17, 95, 99, 100, 101 DO BEGIN

        OUTTEXT("LOOKUP RECURSIV ");
        OUTINT(NEEDLE, 3);
        OUTTEXT(" ... INDEX = ");
        K := BINARYSEARCHREC(HAYSTACK, NEEDLE);
        OUTINT(K, 3);
        IF K < 0 THEN OUTTEXT(" NOT FOUND!");
        OUTIMAGE;

        OUTTEXT("LOOKUP ITERATIV ");
        OUTINT(NEEDLE, 3);
        OUTTEXT(" ... INDEX = ");
        K := BINARYSEARCH(HAYSTACK, NEEDLE);
        OUTINT(K, 3);
        IF K < 0 THEN OUTTEXT(" NOT FOUND!");
        OUTIMAGE;

        OUTIMAGE;
    END;

END
```

**Output:**

```
ARRAY = (1, 6, 17, 29, 45, 78, 79, 87, 95, 100)

LOOKUP RECURSIV   0 ... INDEX =  -1 NOT FOUND!
LOOKUP ITERATIV   0 ... INDEX =  -1 NOT FOUND!

LOOKUP RECURSIV   1 ... INDEX =   0
LOOKUP ITERATIV   1 ... INDEX =   0

LOOKUP RECURSIV   7 ... INDEX =  -3 NOT FOUND!
LOOKUP ITERATIV   7 ... INDEX =  -3 NOT FOUND!

LOOKUP RECURSIV  17 ... INDEX =   2
LOOKUP ITERATIV  17 ... INDEX =   2

LOOKUP RECURSIV  95 ... INDEX =   8
LOOKUP ITERATIV  95 ... INDEX =   8

LOOKUP RECURSIV  99 ... INDEX = -10 NOT FOUND!
LOOKUP ITERATIV  99 ... INDEX = -10 NOT FOUND!

LOOKUP RECURSIV 100 ... INDEX =   9
LOOKUP ITERATIV 100 ... INDEX =   9

LOOKUP RECURSIV 101 ... INDEX = -11 NOT FOUND!
LOOKUP ITERATIV 101 ... INDEX = -11 NOT FOUND!
```


## SPARK

SPARK does not allow recursion, so only the iterative solution is provided. This example shows the use of a loop assertion.

All the code for this task validates with SPARK GPL 2010 and compiles and executes with GPS GPL 2010.

The Binary_Searches package is shown first. Search is a procedure, rather than a function, so that it can return a Found flag and a Position for Item, if found. This is better design than having a Position value that means 'item not found'.

There are two versions of the package provided, although the Ada code of the two versions is identical.

The first version has a postcondition that if Found is True the Position value returned is correct. This version also has a number of 'check' annotations. These are inserted to allow the Simplifier to prove all the verification conditions. See the SPARK Proof Process.

```mw
package Binary_Searches is

   subtype Item_Type is Integer; -- From specs.
   subtype Index_Type is Integer range 1 .. 100;
   type Array_Type is array (Index_Type range <>) of Item_Type;

   procedure Search (Source   : in     Array_Type;
                     Item     : in     Item_Type;
                     Found    :     out Boolean;
                     Position :     out Index_Type);
   --# derives Found,
   --#         Position from
   --#            Source,
   --#            Item;
   --# post Found -> Source (Position) = Item;
   -- If Found is False then Position is undefined.

end Binary_Searches;

package body Binary_Searches is

   procedure Search (Source   : in     Array_Type;
                     Item     : in     Item_Type;
                     Found    :     out Boolean;
                     Position :     out Index_Type)
   is
      Lower      : Index_Type; -- Lower bound of Subrange.
      Upper      : Index_Type; -- Upper bound of Subrange.
      Terminated : Boolean;
   begin
      Found := False;
      -- Default status updated on success.

      Lower      := Source'First;
      Upper      := Source'Last;
      Position   := (Lower + Upper) / 2;
      Terminated := False;

      while not Terminated loop
      --# assert Lower >= Source'First
      --#  and   Upper <= Source'Last
      --#  and   Position in Lower .. Upper
      --#  and   not Found;
         if Item < Source (Position) then
            if Position = Lower then
               -- No lower subrange.
               Terminated := True;
            else
               --# check Position > Lower;
               -- For the two following proofs.

               --# check Position - 1 >= Lower;
               --# check Lower + Position - 1 >= Lower * 2;
               --# check (Lower + Position - 1) / 2 >= Lower;
               -- For "Position >= Lower" in loop assertion.

               --# check Lower < Position;
               --# check Lower + Position - 1 <= (Position - 1) * 2;
               --# check (Lower + Position - 1) / 2 <= (Position - 1);
               -- For "Position <= Upper" in loop assertion.

               -- Switch to lower half subrange.
               Upper := Position - 1;
               Position := (Lower + Upper) / 2;
            end if;

         elsif Item > Source (Position) then
            if Position = Upper then
               -- No upper subrange.
               Terminated := True;
            else
               --# check Position < Upper;
               -- For the two following proofs.

               --# check Upper >= Position + 1;
               --# check Position + 1 + Upper >= (Position + 1) * 2;
               --# check (Position + 1 + Upper) / 2 >= (Position + 1);
               -- For "Position >= Lower" in loop assertion.

               --# check Position + 1 <= Upper;
               --# check Position + 1 + Upper <= Upper * 2;
               --# check (Position + 1 + Upper) / 2 <= Upper;
               -- For "Position <= Upper" in loop assertion.

               -- Switch to upper half subrange.
               Lower := Position + 1;
               Position := (Lower + Upper) / 2;
            end if;
         else
            Found      := True;
            Terminated := True;
         end if;
      end loop;
   end Search;

end Binary_Searches;
```

The second version of the package has a stronger postcondition on Search, which also states that if Found is False then there is no value in Source equal to Item. This postcondition cannot be proved without a precondition that Source is ordered. This version needs four user rules (see the SPARK Proof Process) to be provided to the Simplifier so that it can prove all the verification conditions.

```mw
package Binary_Searches is

   subtype Item_Type is Integer; -- From specs.
   subtype Index_Type is Integer range 1 .. 100;
   type Array_Type is array (Index_Type range <>) of Item_Type;

   --  Ordered_Between is a 'proof function'.  It does not have a code
   --  body, but its meaning is defined by a proof rule:
   --
   --    Ordered_Between (Source, Low_Bound, High_Bound)
   --      <->
   --    for all I in Index_Type range Low_Bound .. High_Bound - 1 =>
   --             (Source(I) < Source(I + 1)) ;
   --
   --# function Ordered_Between (Source               : Array_Type;
   --#                           Range_From, Range_To : Index_Type)
   --#    return Boolean;

   procedure Search (Source   : in     Array_Type;
                     Item     : in     Item_Type;
                     Found    :     out Boolean;
                     Position :     out Index_Type);
   --# derives Found,
   --#         Position from
   --#            Source,
   --#            Item;
   --# pre  Ordered_Between (Source, Source'First, Source'Last);
   --# post (Found -> (Source (Position) = Item))
   --#  and (not Found ->
   --#         (for all I in Index_Type range Source'Range
   --#                                  => (Source(I) /= Item)));

end Binary_Searches;

package body Binary_Searches is

   procedure Search (Source   : in     Array_Type;
                     Item     : in     Item_Type;
                     Found    :     out Boolean;
                     Position :     out Index_Type)
   is
      Lower      : Index_Type; -- Lower bound of Subrange.
      Upper      : Index_Type; -- Upper bound of Subrange.
      Terminated : Boolean;
   begin
      Found := False;
      -- Default status updated on success.

      Lower      := Source'First;
      Upper      := Source'Last;
      Position   := (Lower + Upper) / 2;
      Terminated := False;

      while not Terminated loop
      --# assert not Terminated
      --#   and  not Found
      --#   and  Lower >= Source'First
      --#   and  Upper <= Source'Last
      --#   and  Position in Lower .. Upper
      --#   and  (Lower = Source'First or
      --#         (Lower > Source'First and Source(Lower - 1) < Item))
      --#   and  (Upper = Source'Last or
      --#         (Upper < Source'Last and Source(Upper + 1) > Item));
         if Item < Source (Position) then
            if Position = Lower then
               -- No lower subrange.
               Terminated := True;
            else
               -- Switch to lower half subrange.
               Upper := Position - 1;
               Position := (Lower + Upper) / 2;
            end if;
         elsif Item > Source (Position) then
            if Position = Upper then
               -- No upper subrange.
               Terminated := True;
            else
               -- Switch to upper half subrange.
               Lower := Position + 1;
               Position := (Lower + Upper) / 2;
            end if;
         else
            Found      := True;
            Terminated := True;
         end if;
      end loop;
   end Search;

end Binary_Searches;
```

The user rules for this version of the package (written in FDL, a language for modelling algorithms).

```
binary_search_rule(1): (X + Y) div 2 >= X
                         may_be_deduced_from
                       [ X <= Y,
                         X >= 1,
                         Y >= 1] .

binary_search_rule(2): (X + Y) div 2 <= Y
                         may_be_deduced_from
                       [ X <= Y,
                         X >= 1,
                         Y >= 1] .

binary_search_rule(3): for_all(I_ : integer, First <= I_ and I_ <= Last
                                  -> element(S, [I_]) <> X)
                         may_be_deduced_from
                       [ ordered_between(S, First, Last),
                         P >= First,
                         P <= Last,
                         element(S, [P]) > X,
                         P = First or (P > First and element(S, [P - 1]) < X) ] .

binary_search_rule(4): for_all(I_ : integer, First <= I_ and I_ <= Last
                                  -> element(S, [I_]) <> X)
                         may_be_deduced_from
                       [ ordered_between(S, First, Last),
                         P >= First,
                         P <= Last,
                         element(S, [P]) < X,
                         P = Last or (P < Last and element(S, [P + 1]) > X) ] .
```

The test program:

```mw
with Binary_Searches;
with SPARK_IO;

--# inherit  Binary_Searches,
--#          SPARK_IO;

--# main_program;
procedure Test_Binary_Search
--# global in out SPARK_IO.Outputs;
--# derives SPARK_IO.Outputs from *;
is

   subtype Index_Type5 is Binary_Searches.Index_Type range 1 .. 5;
   subtype Index_Type7 is Binary_Searches.Index_Type range 1 .. 7;
   subtype Index_Type9 is Binary_Searches.Index_Type range 91 .. 99;
   -- Needed to define a constrained Array_Type.

   subtype Array_Type5 is Binary_Searches.Array_Type (Index_Type5);
   subtype Array_Type7 is Binary_Searches.Array_Type (Index_Type7);
   subtype Array_Type9 is Binary_Searches.Array_Type (Index_Type9);
   -- Needed to pass an array literal to Run_Search.
   -- SPARK does not allow an unconstrained type mark for that purpose.

   procedure Run_Search (Source : in     Binary_Searches.Array_Type;
                         Item   : in     Binary_Searches.Item_Type)
   --# global in out SPARK_IO.Outputs;
   --# derives SPARK_IO.Outputs from *,
   --#                               Item,
   --#                               Source;
   is
      Found    : Boolean;
      Position : Binary_Searches.Index_Type;
   begin
      SPARK_IO.Put_String (File => SPARK_IO.Standard_Output,
                           Item => "Searching for ",
                           Stop => 0);
      SPARK_IO.Put_Integer (File  => SPARK_IO.Standard_Output,
                            Item  => Item,
                            Width => 3,
                            Base  => 10);
      SPARK_IO.Put_String (File => SPARK_IO.Standard_Output,
                           Item => " in (",
                           Stop => 0);
      for Source_Index in Binary_Searches.Index_Type range Source'Range loop
         SPARK_IO.Put_Integer (File  => SPARK_IO.Standard_Output,
                               Item  => Source (Source_Index),
                               Width => 3,
                               Base  => 10);
      end loop;
      SPARK_IO.Put_String (File => SPARK_IO.Standard_Output,
                           Item => "): ",
                           Stop => 0);
      Binary_Searches.Search (Source   => Source,    -- in
                              Item     => Item,      -- in
                              Found    => Found,     -- out
                              Position => Position); -- out
      if Found then
         SPARK_IO.Put_String (File => SPARK_IO.Standard_Output,
                              Item => "found as #",
                              Stop => 0);
         SPARK_IO.Put_Integer (File  => SPARK_IO.Standard_Output,
                               Item  => Position,
                               Width => 0, -- to stick to the sibling '#' sign.
                               Base  => 10);
         SPARK_IO.Put_Line (File => SPARK_IO.Standard_Output,
                            Item => ".",
                            Stop => 0);
      else
         SPARK_IO.Put_Line (File => SPARK_IO.Standard_Output,
                            Item => "not found.",
                            Stop => 0);
      end if;
   end Run_Search;

begin
   SPARK_IO.New_Line (File => SPARK_IO.Standard_Output, Spacing => 1);
   Run_Search (Source => Array_Type5'(0, 1, 2, 3, 4), Item => 3);
   Run_Search (Source => Array_Type5'(2, 4, 6, 8, 10), Item => 3);
   Run_Search (Source => Array_Type7'(1, 2, 3, 4, 5, 6, 7), Item => 0);
   Run_Search (Source => Array_Type7'(1, 2, 3, 4, 5, 6, 7), Item => 7);
   Run_Search (Source => Array_Type9'(1, 2, 3, 4, 5, 6, 7, 8, 9), Item => 10);
   Run_Search (Source => Array_Type9'(1, 2, 3, 4, 5, 6, 7, 8, 9), Item => 1);
   Run_Search (Source => Array_Type9'(1, 2, 3, 4, 5, 6, 7, 8, 9), Item => 6);
end Test_Binary_Search;
```

Test output (for the last three tests the array is indexed from 91):

```
Searching for   3 in (  0  1  2  3  4): found as #4.
Searching for   3 in (  2  4  6  8 10): not found.
Searching for   0 in (  1  2  3  4  5  6  7): not found.
Searching for   7 in (  1  2  3  4  5  6  7): found as #7.
Searching for  10 in (  1  2  3  4  5  6  7  8  9): not found.
Searching for   1 in (  1  2  3  4  5  6  7  8  9): found as #91.
Searching for   6 in (  1  2  3  4  5  6  7  8  9): found as #96.
```


## Standard ML

**Recursive**

```mw
fun binary_search cmp (key, arr) =
  let
    fun aux slice =
      if ArraySlice.isEmpty slice then
        NONE
      else
        let
 	  val mid = ArraySlice.length slice div 2
        in
	  case cmp (ArraySlice.sub (slice, mid), key)
	  of LESS    => aux (ArraySlice.subslice (slice, mid+1, NONE))
 	   | GREATER => aux (ArraySlice.subslice (slice, 0, SOME mid))
	   | EQUAL   => SOME (#2 (ArraySlice.base slice) + mid)
        end
  in
    aux (ArraySlice.full arr)
  end
```

Usage:

```
- val a = Array.fromList [2, 3, 5, 6, 8];
val a = [|2,3,5,6,8|] : int array
- binary_search Int.compare (4, a);
val it = NONE : int option
- binary_search Int.compare (8, a);
val it = SOME 4 : int option
```

Standard ML supports proper tail-recursion; so this is effectively the same as iteration.

**Library**

Works with

:

SML/NJ

Usage:

```
- structure IntArray = struct
=   open Array
=   type elem = int
=   type array = int Array.array
=   type vector = int Vector.vector
= end;
structure IntArray :
  sig
[ ... rest omitted ]
- structure IntBSearch = BSearchFn (IntArray);
structure IntBSearch :
  sig
    structure A : <sig>
    val bsearch : ('a * A.elem -> order)
                  -> 'a * A.array -> (int * A.elem) option
  end
- val a = Array.fromList [2, 3, 5, 6, 8];
val a = [|2,3,5,6,8|] : int array
- IntBSearch.bsearch Int.compare (4, a);
val it = NONE : (int * IntArray.elem) option
- IntBSearch.bsearch Int.compare (8, a);
val it = SOME (4,8) : (int * IntArray.elem) option
```


## Swift

**Recursive**

```mw
func binarySearch<T: Comparable>(xs: [T], x: T) -> Int? {
  var recurse: ((Int, Int) -> Int?)!
  recurse = {(low, high) in switch (low + high) / 2 {
    case _ where high < low: return nil
    case let mid where xs[mid] > x: return recurse(low, mid - 1)
    case let mid where xs[mid] < x: return recurse(mid + 1, high)
    case let mid: return mid
  }}
  return recurse(0, xs.count - 1)
}
```

**Iterative**

```mw
func binarySearch<T: Comparable>(xs: [T], x: T) -> Int? {
  var (low, high) = (0, xs.count - 1)
  while low <= high {
    switch (low + high) / 2 {
      case let mid where xs[mid] > x: high = mid - 1
      case let mid where xs[mid] < x: low = mid + 1
      case let mid: return mid
    }
  }
  return nil
}
```

**Test**

```mw
func testBinarySearch(n: Int) {
  let odds = Array(stride(from: 1, through: n, by: 2))
  let result = flatMap(0...n) {binarySearch(odds, $0)}
  assert(result == Array(0..<odds.count))
  println("\(odds) are odd natural numbers")
  for it in result {
    println("\(it) is ordinal of \(odds[it])")
  }
}

testBinarySearch(12)

func flatMap<T, U>(source: [T], transform: (T) -> U?) -> [U] {
  return source.reduce([]) {(var xs, x) in if let x = transform(x) {xs.append(x)}; return xs}
}
```

Output:

```
[1, 3, 5, 7, 9, 11] are odd natural numbers
0 is ordinal of 1
1 is ordinal of 3
2 is ordinal of 5
3 is ordinal of 7
4 is ordinal of 9
5 is ordinal of 11
```


## Symsyn

```mw
a : 1 : 2 : 27 : 44 : 46 : 57 : 77 : 154 : 212

binary_search param item index size
 index saveindex
 index L
 (index + size - 1) H
 if L <= H 
    ((L + H) shr 1) M
    if base.M > item
       - 1 M H
    else
       if base.M < item
          + 1 M L
       else
          - saveindex M
          return M
       endif
    endif
    goif
 endif
 return -1

start

 call binary_search 77 @a #a
 result R

 "'result = ' R" []
```


## Tcl

ref: Tcl wiki

```mw
proc binSrch {lst x} {
    set len [llength $lst]
    if {$len == 0} {
        return -1
    } else {
        set pivotIndex [expr {$len / 2}]
        set pivotValue [lindex $lst $pivotIndex]
        if {$pivotValue == $x} {
            return $pivotIndex
        } elseif {$pivotValue < $x} {
            set recursive [binSrch [lrange $lst $pivotIndex+1 end] $x]
            return [expr {$recursive > -1 ? $recursive + $pivotIndex + 1 : -1}]
        } elseif {$pivotValue > $x} {
            set recursive [binSrch [lrange $lst 0 $pivotIndex-1] $x]
            return [expr {$recursive > -1 ? $recursive : -1}]
        }
    }
}
proc binary_search {lst x} {
    if {[set idx [binSrch $lst $x]] == -1} {
        puts "element $x not found in list"
    } else {
        puts "element $x found at index $idx"
    }
}
```

Note also that, from Tcl 8.4 onwards, the lsearch command includes the -sorted option to enable binary searching of Tcl lists.

```mw
proc binarySearch {lst x} {
    set idx [lsearch -sorted -exact $lst $x]
    if {$idx == -1} {
        puts "element $x not found in list"
    } else {
        puts "element $x found at index $idx"
    }
}
```


## UNIX Shell

**Reading values line by line**

```mw
#!/bin/ksh
# This should work on any clone of Bourne Shell, ksh is the fastest.

value=$1; [ -z "$value" ] && exit
array=()
size=0

while IFS= read -r line; do
	size=$(($size + 1))
	array[${#array[*]}]=$line
done
```

**Iterative**

```mw
left=0
right=$(($size - 1))
while	[ $left -le $right ] ; do
	mid=$((($left + $right) >> 1))
#	echo "$left	$mid(${array[$mid]})	$right"
	if	[ $value -eq ${array[$mid]} ] ; then
		echo $mid
		exit
	elif	[ $value -lt ${array[$mid]} ]; then
		right=$(($mid - 1))
	else
		left=$((mid + 1))
	fi
done
echo 'ERROR 404 : NOT FOUND'
```

**Recursive**

```mw
 No code yet
```


## UnixPipes

**Parallel**

```mw
splitter() {
   a=$1; s=$2; l=$3; r=$4;
   mid=$(expr ${#a[*]} / 2);
   echo $s ${a[*]:0:$mid} > $l
   echo $(($mid + $s)) ${a[*]:$mid} > $r
}

bsearch() {
   (to=$1; read s arr; a=($arr);
       test  ${#a[*]} -gt 1  && (splitter $a $s >(bsearch $to) >(bsearch $to)) || (test "$a" -eq "$to" && echo $a at $s)
   )
}

binsearch() {
   (read arr; echo "0 $arr" | bsearch $1)
}

echo "1 2 3 4 6 7 8 9"  | binsearch 6
```


## Vedit macro language

**Iterative**

For this implementation, the numbers to be searched must be stored in current edit buffer, one number per line. (Could be for example a csv table where the first column is used as key field.)

```mw
// Main program for testing BINARY_SEARCH
#3 = Get_Num("Value to search: ")
EOF
#2 = Cur_Line                   // hi
#1 = 1                          // lo
Call("BINARY_SEARCH")
Message("Value ") Num_Type(#3, NOCR)
if (Return_Value < 1) {
    Message(" not found\n")
} else {
    Message(" found at index ") Num_Type(Return_Value)
}
return

:BINARY_SEARCH:
while (#1 <= #2) {
    #12 = (#1 + #2) / 2
    Goto_Line(#12)
    #11 = Num_Eval()
    if (#3 == #11) {
        return(#12)             // found
    } else {
        if (#3 < #11) {
            #2 = #12-1
        } else {
            #1 = #12+1
        }
    }
}
return(0)                       // not found
```


## V (Vlang)

```mw
fn binary_search_rec(a []f64, value f64, low int, high int) int { // recursive
    if high <= low {
        return -1
    }
    mid := (low + high) / 2
    if a[mid] > value {
        return binary_search_rec(a, value, low, mid-1)
    } else if a[mid] < value {
        return binary_search_rec(a, value, mid+1, high)
    }
    return mid
}
fn binary_search_it(a []f64, value f64) int { //iterative
    mut low := 0
    mut high := a.len - 1
    for low <= high {
        mid := (low + high) / 2
        if a[mid] > value {
            high = mid - 1
        } else if a[mid] < value {
            low = mid + 1
        } else {
            return mid
        }
    }
    return -1
}
fn main() {
    f_list := [1.2,1.5,2,5,5.13,5.4,5.89,9,10]
    println(binary_search_rec(f_list,9,0,f_list.len))
    println(binary_search_rec(f_list,15,0,f_list.len))

    println(binary_search_it(f_list,9))
    println(binary_search_it(f_list,15))
}
```

**Output:**

```
7
-1
7
-1
```


## Wortel

Translation of

:

JavaScript

```mw
; Recursive
@var rec &[a v l h] [
  @if < h l @return null
  @var m @/ +h l 2
  @? {
    > `m a v @!rec[a v l -m 1]
    < `m a v @!rec[a v +1 m h]
    m
  }
]

; Iterative
@var itr &[a v] [
  @vars{l 0 h #-a}
  @while <= l h [
    @var m @/ +l h 2
    @iff {
      > `m a v :h -m 1
      < `m a v :l +m 1
      @return m
    }
  ]
  null
]
```


## Wren

```mw
class BinarySearch {
    static recursive(a, value, low, high) {
        if (high < low) return -1
        var mid = low + ((high - low)/2).floor
        if (a[mid] > value) return recursive(a, value, low, mid-1)
        if (a[mid] < value) return recursive(a, value, mid+1, high)
        return mid
    }

    static iterative(a, value) {
        var low = 0
        var high = a.count - 1
        while (low <= high) {
            var mid = low + ((high - low)/2).floor
            if (a[mid] > value) {
                high = mid - 1
            } else if (a[mid] < value) {
                low = mid + 1
            } else {
                return mid
            }
        }
        return -1
    }
}

var a = [10, 22, 45, 67, 89, 97]
System.print("array = %(a)")

System.print("\nUsing the recursive algorithm:")
for (value in [67, 93]) {
    var index = BinarySearch.recursive(a, value, 0, a.count - 1)
    if (index >= 0) {
        System.print("  %(value) was found at index %(index) of the array.")
    } else {
        System.print("  %(value) was not found in the array.")
    }
}

System.print("\nUsing the iterative algorithm:")
for (value in [22, 70]) {
    var index = BinarySearch.iterative(a, value)
    if (index >= 0) {
        System.print("  %(value) was found at index %(index) of the array.")
    } else {
        System.print("  %(value) was not found in the array.")
    }
}
```

**Output:**

```
array = [10, 22, 45, 67, 89, 97]

Using the recursive algorithm:
  67 was found at index 3 of the array.
  93 was not found in the array.

Using the iterative algorithm:
  22 was found at index 1 of the array.
  70 was not found in the array.
```


## XPL0

Translation of

:

C

Works with

:

EXPL-32

```mw
\Binary search
code CrLf=9, IntOut=11, Text=12;
def Size = 10;
integer A, X, I;

  function integer DoBinarySearch(A, N, X);
  integer A, N, X;
  integer L, H, M;
  begin
  L:= 0; H:= N - 1;
  while L <= H do
    begin
    M:= L + (H - L) / 2;
    case of 
      A(M) < X: L:= M + 1;
      A(M) > X: H:= M - 1
    other return M;
    end;
  return -1;
  end;

  function integer DoBinarySearchRec(A, X, L, H);
  integer A, X, L, H;
  integer M;
  begin
  if H < L then
    return -1;
  M:= L + (H - L) / 2;
  case of 
    A(M) > X: return DoBinarySearchRec(A, X, L, M - 1);
    A(M) < X: return DoBinarySearchRec(A, X, M + 1, H)
  other return M
  end;

  procedure PrintResult(X, IndX);
  integer X, IndX;
  begin
  IntOut(0, X);
  if IndX >= 0 then 
    begin
    Text(0, " is at index ");
    IntOut(0, IndX);
    Text(0, ".") 
    end
  else
    Text(0, " is not found.");
  CrLf(0)
  end;

begin
\Sorted data
A:= [-31, 0, 1, 2, 2, 4, 65, 83, 99, 782];
X:= 2;
I:= DoBinarySearch(A, Size, X);
PrintResult(X, I);
X:= 5;
I:= DoBinarySearchRec(A, X, 0, Size - 1);
PrintResult(X, I);
end
```

**Output:**

```
2 is at index 4.
5 is not found.
```


## YAMLScript

```mw
!ys-0

defn main(target=23 nums='1 3 5 7 9 11 13 15 17 19 21 23 25 27'):
  xs =: nums.split(/\s+/).map(N _):V
  i =: bsearch(xs target)
  if i:nil?:
    say: "$target not found"
    say: "$target found at index $i"

defn bsearch(xs target):
  loop lo 0, hi xs.#.--:
    when lo <= hi:
      mid =: quot((lo + hi) 2)
      v =: xs.$mid
      cond:
        v > target: recur(lo mid.--)
        v < target: recur(mid.++ hi)
        else: mid
```

**Output:**

```
$ ys binary-search.ys
23 found at index 11
```


## z/Arch Assembler

This optimized version for z/Arch, uses six general regs and avoid branch misspredictions for high/low cases.

```mw
*        Binary search             
BINSRCH  LA    R5,TABLE            Begin of table
         SR    R2,R2               low  = 0                                 
         LA    R3,ENTRIES-1        high = N-1
LOOP     CR    R2,R3               while (low <= high)                 
         JH    NOTFOUND            {                                   
         ARK   R4,R2,R3               mid = low + high                 
         SRL   R4,1                   mid = mid / 2
         LA    R1,1(R4)               mid + 1
         AHIK  R0,R4,-1               mid - 1
         MSFI  R4,ENTRYL              mid * length                     
         AR    R4,R5                  Table[mid]                       
         CLC   0(L'KEY,R4),SEARCH     Compare 
         JE    FOUND                  Equal? => Found                
         LOCRH R3,R0                  High?  => HIGH = MID-1           
         LOCRL R2,R1                  Low?   => LOW  = MID+1           
         J     LOOP                }
```


## Zen C

### Iterative

```mw
fn binary_search_iterative(arr: int*, value: int, low: int, high: int) -> int {
    let l = low;
    let h = high;
    
    while l <= h {
        let mid = l + (h - l) / 2;
        
        if arr[mid] > value {
            h = mid - 1;
        } else if arr[mid] < value {
            l = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
}

fn main() {
    let arr: int[10] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
    let n = 10;
    let targets: int[3] = [12, 5, 20];
    
    println "=> Iterative Binary Search";
    for target in targets {
        let index = binary_search_iterative(arr, target, 0, n - 1);
        if index != -1 {
            println "Value {target} found at index {index}.";
        } else {
            println "Value {target} not found.";
        }
    }
}
```

**Output:**

```
=> Iterative Binary Search
Value 12 found at index 5.
Value 5 not found.
Value 20 found at index 9.
```

### Recursive

```mw
fn binary_search_recursive(arr: int*, value: int, low: int, high: int) -> int {
    if high < low {
        return -1;
    }

    let mid = low + (high - low) / 2;
    
    if arr[mid] > value {
        return binary_search_recursive(arr, value, low, mid - 1);
    } else if arr[mid] < value {
        return binary_search_recursive(arr, value, mid + 1, high);
    } else {
        return mid;
    }
}

fn main() {
    let arr: int[10] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];
    let n = 10;
    let targets: int[3] = [12, 5, 20];
    
    println "=> Recursive Binary Search";
    for target in targets {
        let index = binary_search_recursive(arr, target, 0, n - 1);
        if index != -1 {
            println "Value {target} found at index {index}.";
        } else {
            println "Value {target} not found.";
        }
    }
}
```

**Output:**

```
=> Recursive Binary Search
Value 12 found at index 5.
Value 5 not found.
Value 20 found at index 9.
```


## Zig

**Works with:** 0.11.x, 0.12.0-dev.1381+61861ef39

For 0.10.x, replace @intFromPtr(...) with @ptrToInt(...) in these examples.

### With slices

#### Iterative

```mw
pub fn binarySearch(comptime T: type, input: []const T, search_value: T) ?usize {
    if (input.len == 0) return null;
    if (@sizeOf(T) == 0) return 0;

    var view: []const T = input;
    const item_ptr: *const T = item_ptr: while (view.len > 0) {
        const mid = (view.len - 1) / 2;
        const mid_elem_ptr: *const T = &view[mid];

        if (mid_elem_ptr.* > search_value)
            view = view[0..mid]
        else if (mid_elem_ptr.* < search_value)
            view = view[mid + 1 .. view.len]
        else
            break :item_ptr mid_elem_ptr;
    } else return null;

    const distance_in_bytes = @intFromPtr(item_ptr) - @intFromPtr(input.ptr);
    return (distance_in_bytes / @sizeOf(T));
}
```

#### Recursive

```mw
pub fn binarySearch(comptime T: type, input: []const T, search_value: T) ?usize {
    return binarySearchInner(T, input, search_value, @intFromPtr(input.ptr));
}

fn binarySearchInner(comptime T: type, input: []const T, search_value: T, start_address: usize) ?usize {
    if (input.len == 0) return null;
    if (@sizeOf(T) == 0) return 0;

    const mid = (input.len - 1) / 2;
    const mid_elem_ptr: *const T = &input[mid];

    return if (mid_elem_ptr.* > search_value)
        binarySearchInner(T, input[0..mid], search_value, start_address)
    else if (mid_elem_ptr.* < search_value)
        binarySearchInner(T, input[mid + 1 .. input.len], search_value, start_address)
    else
        (@intFromPtr(mid_elem_ptr) - start_address) / @sizeOf(T);
}
```

### With indexes

#### Iterative

```mw
const math = @import("std").math;

pub fn binarySearch(comptime T: type, input: []const T, search_value: T) ?usize {
    if (input.len == 0) return null;
    if (@sizeOf(T) == 0) return 0;

    var low: usize = 0;
    var high: usize = input.len - 1;
    return while (low <= high) {
        const mid = ((high - low) / 2) + low;
        const mid_elem: T = input[mid];
        if (mid_elem > search_value)
            high = math.sub(usize, mid, 1) catch break null
        else if (mid_elem < search_value)
            low = mid + 1
        else
            break mid;
    } else null;
}
```

#### Recursive

```mw
const math = @import("std").math;

pub fn binarySearch(comptime T: type, input: []const T, search_value: T) ?usize {
    if (input.len == 0) return null;
    if (@sizeOf(T) == 0) return 0;

    return binarySearchInner(T, input, search_value, 0, input.len - 1);
}

fn binarySearchInner(comptime T: type, input: []const T, search_value: T, low: usize, high: usize) ?usize {
    if (low > high) return null;

    const mid = ((high - low) / 2) + low;
    const mid_elem: T = input[mid];

    return if (mid_elem > search_value)
        binarySearchInner(T, input, search_value, low, math.sub(usize, mid, 1) catch return null)
    else if (mid_elem < search_value)
        binarySearchInner(T, input, search_value, mid + 1, high)
    else
        mid;
}
```


## zkl

This algorithm is tail recursive, which means it is both recursive and iterative (since tail recursion optimizes to a jump). Overflow is not possible because Ints (64 bit) are a lot bigger than the max length of a list.

```mw
fcn bsearch(list,value){	// list is sorted
   fcn(list,value, low,high){
      if (high < low) return(Void);	// not found
      mid:=(low + high) / 2;
      if (list[mid] > value) return(self.fcn(list,value, low,   mid-1));
      if (list[mid] < value) return(self.fcn(list,value, mid+1, high));
      return(mid);			// found
   }(list,value,0,list.len()-1);
}
```

```mw
list:=T(1,3,5,7,9,11); println("Sorted values: ",list);
foreach i in ([0..12]){
   n:=bsearch(list,i);
   if (Void==n) println("Not found: ",i);
   else println("found ",i," at index ",n);
}
```

**Output:**

```
Sorted values: L(1,3,5,7,9,11)
Not found: 0
found 1 at index 0
Not found: 2
found 3 at index 1
Not found: 4
found 5 at index 2
Not found: 6
found 7 at index 3
Not found: 8
found 9 at index 4
Not found: 10
found 11 at index 5
Not found: 12
```

Retrieved from "

https://rosettacode.org/wiki/Binary_search?oldid=404564

"
