---
title: "99 bottles of beer (part 1/5)"
source: https://rosettacode.org/wiki/99_Bottles_of_Beer
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 1/5
---

# 99 bottles of beer

(Redirected from

99 Bottles of Beer

)

**Task**

Display the complete lyrics for the song:     **99 Bottles of Beer on the Wall**.

**The beer song**

The lyrics follow this form:

> 99 bottles of beer on the wall
> 
> 99 bottles of beer
> 
> Take one down, pass it around
> 
> 98 bottles of beer on the wall
> 
> 98 bottles of beer on the wall
> 
> 98 bottles of beer
> 
> Take one down, pass it around
> 
> 97 bottles of beer on the wall

... and so on, until reaching   **0**     (zero).

Grammatical support for   *1 bottle of beer*   is optional.

As with any puzzle, try to do it in as creative/concise/comical a way as possible (simple, obvious solutions allowed, too).

Other tasks related to string operations:

**Metrics**

- Array length
- String length
- Copy a string
- Empty string  (assignment)

**Counting**

- Word frequency
- Letter frequency
- Jewels and stones
- I before E except after C
- Bioinformatics/base count
- Count occurrences of a substring
- Count how many vowels and consonants occur in a string

**Remove/replace**

- XXXX redacted
- Conjugate a Latin verb
- Remove vowels from a string
- String interpolation (included)
- Strip block comments
- Strip comments from a string
- Strip a set of characters from a string
- Strip whitespace from a string -- top and tail
- Strip control codes and extended characters from a string

**Anagrams/Derangements/shuffling**

- Word wheel
- ABC problem
- Sattolo cycle
- Knuth shuffle
- Ordered words
- Superpermutation minimisation
- Textonyms (using a phone text pad)
- Anagrams
- Anagrams/Deranged anagrams
- Permutations/Derangements

**Find/Search/Determine**

- ABC words
- Odd words
- Word ladder
- Semordnilap
- Word search
- Wordiff  (game)
- String matching
- Tea cup rim text
- Alternade words
- Changeable words
- State name puzzle
- String comparison
- Unique characters
- Unique characters in each string
- Extract file extension
- Levenshtein distance
- Palindrome detection
- Common list elements
- Longest common suffix
- Longest common prefix
- Compare a list of strings
- Longest common substring
- Find common directory path
- Words from neighbour ones
- Change e letters to i in words
- Non-continuous subsequences
- Longest common subsequence
- Longest palindromic substrings
- Longest increasing subsequence
- Words containing "the" substring
- Sum of the digits of n is substring of n
- Determine if a string is numeric
- Determine if a string is collapsible
- Determine if a string is squeezable
- Determine if a string has all unique characters
- Determine if a string has all the same characters
- Longest substrings without repeating characters
- Find words which contains all the vowels
- Find words which contain the most consonants
- Find words which contains more than 3 vowels
- Find words whose first and last three letters are equal
- Find words with alternating vowels and consonants

**Formatting**

- Substring
- Rep-string
- Word wrap
- String case
- Align columns
- Literals/String
- Repeat a string
- Brace expansion
- Brace expansion using ranges
- Reverse a string
- Phrase reversals
- Comma quibbling
- Special characters
- String concatenation
- Substring/Top and tail
- Commatizing numbers
- Reverse words in a string
- Suffixation of decimal numbers
- Long literals, with continuations
- Numerical and alphabetical suffixes
- Abbreviations, easy
- Abbreviations, simple
- Abbreviations, automatic

**Song lyrics/poems/Mad Libs/phrases**

- Mad Libs
- Magic 8-ball
- 99 bottles of beer
- The Name Game (a song)
- The Old lady swallowed a fly
- The Twelve Days of Christmas

**Tokenize**

- Text between
- Tokenize a string
- Word break problem
- Tokenize a string with escaping
- Split a character string based on change of character

**Sequences**

- Show ASCII table
- De Bruijn sequences
- Summarize and say sequence
- Generate lower case ASCII alphabet

**See also**

- http://99-bottles-of-beer.net/
- Category:99_Bottles_of_Beer
- Category:Programming language families
- Wikipedia 99 bottles of beer


## 0815

See 99 Bottles of Beer/EsoLang


## 11l

Translation of

:

Python

```mw
L(i) (99..1).step(-1)
   print(i‘ bottles of beer on the wall’)
   print(i‘ bottles of beer’)
   print(‘Take one down, pass it around’)
   print((i - 1)" bottles of beer on the wall\n")
```


## AlphaStack

See 99 Bottles of Beer/EsoLang


## 360 Assembly

See 99 Bottles of Beer/Assembly


## 6502 Assembly

See 99 Bottles of Beer/Assembly


## 6800 Assembly

See 99 Bottles of Beer/Assembly


## 68000 Assembly

See 99 Bottles of Beer/Assembly


## 8080 Assembly

See 99 Bottles of Beer/Assembly


## 8th

```mw
\ 99 bottles of beer on the wall:
[
  "no more bottles" ,
  "one bottle" ,
  ( dup . " bottles" )
] var, bottles

: .bottles
  dup 2 n:min bottles @ caseof ;

: .beer
  .bottles . " of beer" . ;

: .wall
  .beer " on the wall" . ;

: .take
  "  Take one down and pass it around" . ;

: beers
  .wall ", " . .beer '; putc cr
  n:1- 0 max .take ", " .
  .wall '. putc cr drop ;

' beers 1 99 loop-
bye
```

A more terse alternative:

```mw
[
  ( "Just one more bottle of beer on the wall, one bottle of beer.\n" . ) ,
  ( I dup "%d bottles of beer on the wall, %d bottles of beer.\n" s:strfmt . )
] constant lyrics

: app:main
  (
    dup lyrics [2,99] rot ' n:cmp a:pigeon w:exec
    n:1- "Take one down, pass it around, %d bottles of beer on the wall.\n\n" s:strfmt .
  ) 1 99 loop-

  "No more bottles of beer on the wall, no more bottles of beer.\n" . ;
```


## AArch64 Assembly

Works with

:

as

version Raspberry Pi 3B version Buster 64 bits

```mw
/* ARM assembly AARCH64 Raspberry PI 3B */
/*  program bootleBeer64.s   */ 

/*******************************************/
/* Constantes file                         */
/*******************************************/
/* for this file see task include a file in language AArch64 assembly*/
.include "../includeConstantesARM64.inc"

.equ MAXI,   99

/*********************************/
/* Initialized data              */
/*********************************/
.data
szMessLine1:        .asciz "@ bottles of beer on the wall\n"
szMessLine2:        .ascii "@ bottles of beer\n"
                    .asciz "Take one down, pass it around\n"
szMessLine3:        .asciz "@ bottles of beer on the wall\n\n"
 
szMessLine4:       .ascii "\nNo more bottles of beer on the wall, no more bottles of beer.\n"
                   .asciz "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

szCarriageReturn:   .asciz "\n"
/*********************************/
/* UnInitialized data            */
/*********************************/
.bss
sZoneConv:        .skip 24
/*********************************/
/*  code section                 */
/*********************************/
.text
.global main 
main:                            // entry of program 
    mov x2,#MAXI
1:
    mov x0,x2
    ldr x1,qAdrsZoneConv
    bl conversion10              // call decimal conversion
    ldr x0,qAdrszMessLine1
    ldr x1,qAdrsZoneConv         // insert conversion in message
    bl strInsertAtCharInc
    bl affichageMess
    
    ldr x0,qAdrszMessLine2
    ldr x1,qAdrsZoneConv         // insert conversion in message
    bl strInsertAtCharInc
    bl affichageMess
    
    subs x0,x2,#1
    ble 2f
    ldr x1,qAdrsZoneConv
    bl conversion10              // call decimal conversion
    ldr x0,qAdrszMessLine3
    ldr x1,qAdrsZoneConv         // insert conversion in message
    bl strInsertAtCharInc
    bl affichageMess
2:
    subs x2,x2,1
    bgt 1b
 
    ldr x0,qAdrszMessLine4
    bl affichageMess

100:                                  // standard end of the program 
    mov x0, #0                        // return code
    mov x8, #EXIT                     // request to exit program
    svc #0                            // perform the system call
 
qAdrszCarriageReturn:     .quad szCarriageReturn
qAdrszMessLine1:          .quad szMessLine1
qAdrszMessLine2:          .quad szMessLine2
qAdrszMessLine3:          .quad szMessLine3
qAdrszMessLine4:          .quad szMessLine4
qAdrsZoneConv:            .quad sZoneConv

/********************************************************/
/*        File Include fonctions                        */
/********************************************************/
/* for this file see task include a file in language AArch64 assembly */
.include "../includeARM64.inc"
```


## ABAP

```mw
REPORT z99bottles.

DATA lv_no_bottles(2) TYPE n VALUE 99.

DO lv_no_bottles TIMES.
  WRITE lv_no_bottles NO-ZERO.
  WRITE ' bottles of beer on the wall'.
  NEW-LINE.
  WRITE lv_no_bottles NO-ZERO.
  WRITE ' bottles of beer'.
  NEW-LINE.
  WRITE 'Take one down, pass it around'.
  NEW-LINE.
  SUBTRACT 1 FROM lv_no_bottles.
  WRITE lv_no_bottles NO-ZERO.
  WRITE ' bottles of beer on the wall'.
  WRITE /.
ENDDO.
```

or (With ABAP 7.40)

```mw
REPORT YCL_99_BOTTLES.

DATA it_99_bottles TYPE TABLE OF string WITH EMPTY KEY.
DATA(cr_lf) = cl_abap_char_utilities=>cr_lf.
it_99_bottles = VALUE #(
    FOR i = 99 THEN i - 1 UNTIL i = 0 ( COND string( LET  lv = ( i - 1 )
                                                          lr = i && | bottles of beer on the wall|
                                                                 && cr_lf
                                                                 && i && | bottles of beer|
                                                                 && cr_lf
                                                                 && |Take one down, pass it around|
                                                                 && cr_lf
                                                                 && lv && | bottles of beer on the wall|
                                                                 && cr_lf IN WHEN 1 = 1 THEN lr )
                                      )
                         ).
cl_demo_output=>write( it_99_bottles ).
cl_demo_output=>display( ).
```


## ABC

```mw
HOW TO RETURN bottles n:
    SELECT:
        n<0: RETURN "99 bottles"
        n=0: RETURN "No more bottles"
        n=1: RETURN "1 bottle"
        n>1: RETURN "`n` bottles"

HOW TO SING VERSE n:
    WRITE "`bottles n` of beer on the wall,"/
    WRITE "`bottles n` of beer,"/
    SELECT:
        n=0: WRITE "Go to the store and buy some more,"/
        n=1: WRITE "Take it down and pass it around,"/
        n>1: WRITE "Take one down and pass it around,"/
    WRITE "`bottles (n-1)` of beer on the wall."/
    WRITE /

FOR n IN {0..99}:
    SING VERSE 99-n
```


## ACL2

See 99 Bottles of Beer/Lisp


## Acornsoft Lisp

See 99 Bottles of Beer/Lisp


## Action!

```mw
PROC Bottles(BYTE i)
  IF i=0 THEN
    Print("No more")
  ELSE
    PrintB(i)
  FI
  Print(" bottle")
  IF i#1 THEN
    Print("s")
  FI
RETURN

PROC Main()
  BYTE i=[99]

  WHILE i>0
  DO
    Bottles(i) PrintE(" of beer on the wall,")
    Bottles(i) PrintE(" of beer,")    
    Print("Take ")
    IF i>1 THEN
      Print("one")
    ELSE
      Print("it")
    FI
    PrintE(" down and pass it around,")
    i==-1
    Bottles(i) PrintE(" of beer on the wall.")
    IF i>0 THEN
      PutE()
    FI
  OD
RETURN
```

**Output:**

Screenshot from Atari 8-bit computer

```
99 bottles of beer on the wall,
99 bottles of beer,
Take one down and pass it around,
98 bottles of beer on the wall.

...

2 bottles of beer on the wall,
2 bottles of beer,
Take one down and pass it around,
1 bottle of beer on the wall.

1 bottle of beer on the wall,
1 bottle of beer,
Take it down and pass it around,
No more bottles of beer on the wall.
```


## ActionScript

```mw
for(var numBottles:uint = 99; numBottles > 0; numBottles--)
{
	trace(numBottles, " bottles of beer on the wall");
	trace(numBottles, " bottles of beer");
	trace("Take one down, pass it around");
	trace(numBottles - 1, " bottles of beer on the wall\n");		  
}
```


## Ada

### Simple version

```mw
with Ada.Text_Io; use Ada.Text_Io;
 
 procedure Bottles is
 begin
    for X in reverse 1..99 loop
       Put_Line(Integer'Image(X) & " bottles of beer on the wall");
       Put_Line(Integer'Image(X) & " bottles of beer");
       Put_Line("Take one down, pass it around");
       Put_Line(Integer'Image(X - 1) & " bottles of beer on the wall");
       New_Line;
    end loop;
 end Bottles;
```

### Concurrent version

with 1 task to print out the information and 99 tasks to specify the number of bottles

```mw
with Ada.Text_Io; use Ada.Text_Io;

procedure Tasking_99_Bottles is
   subtype Num_Bottles is Natural range 1..99;
   task Print is
      entry Set (Num_Bottles);
   end Print;
   task body Print is
      Num : Natural;
   begin
      for I in reverse Num_Bottles'range loop
         select
         accept 
            Set(I) do -- Rendezvous with Counter task I
               Num := I;
            end Set;
            Put_Line(Integer'Image(Num) & " bottles of beer on the wall");
            Put_Line(Integer'Image(Num) & " bottles of beer");
            Put_Line("Take one down, pass it around");
            Put_Line(Integer'Image(Num - 1) & " bottles of beer on the wall");
            New_Line;
         or terminate; -- end when all Counter tasks have completed
         end select;
      end loop;
   end Print;
   task type Counter(I : Num_Bottles);
   task body Counter is
   begin
      Print.Set(I);
   end Counter;
   type Task_Access is access Counter;
   
   Task_List : array(Num_Bottles) of Task_Access;
 
begin
   for I in Task_List'range loop -- Create 99 Counter tasks
      Task_List(I) := new Counter(I);
   end loop;
end Tasking_99_Bottles;
```


## Aime

```mw
integer bottles;

bottles = 99;

do {
    o_(bottles, " bottles of beer on the wall\n");
    o_(bottles, " bottles of beer\n");
    o_("Take one down, pass it around\n");
    o_(bottles -= 1, " bottles of beer on the wall\n\n");
} while (bottles);
```


## Algae

```mw
# 99 Bottles of Beer on the Wall 
# in Algae 
# bottles.A 
for (i in 99:1:1) {
    if (i != 1) {
        printf("%d bottles of beer on the wall\n";i);
        printf("%d bottles of beer...\n";i);
        printf("you take on down and pass it around...\n");
        if ( i == 2) {
            printf("%d bottles of beer on the wall\n\n";i-1);
        else
            printf("%d bottles of beer on the wall\n\n";i-1);
        }
    else
       printf("1 bottle of beer on the wall\n");
       printf("1 bottle of beer...\n");
       printf("you take on down and pass it around..\n");
       printf("no more bottles of beer on the wall!\n\n");
    }
}
```


## ALGOL 60

```mw
begin
  integer n;   

  for n:= 99 step -1 until 2 do
     begin
      outinteger(1,n);	  
	  outstring(1,"bottles of beer on the wall,");
      outinteger(1,n);
      outstring(1,"bottles of beer.\nTake one down and pass it around,");
      outstring(1,"of beer on the wall...\n\n")
     end;
  
  outstring(1," 1 bottle of beer on the wall, 1 bottle of beer.\n");
  outstring(1,"Take one down and pass it around, no more bottles of beer on the wall...\n\n");

  outstring(1,"No more bottles of beer on the wall, no more bottles of beer.\n");
  outstring(1,"Go to the store and buy some more, 99 bottles of beer on the wall.")
end
```


## ALGOL 68

```mw
FOR bottles FROM 99 BY -1 TO 1 DO
    STRING bottles now = whole(bottles,0) + " bottle" + IF bottles = 1 THEN "" ELSE "s" FI;
    STRING bottles left = IF bottles = 1 THEN "No more" ELSE whole(bottles-1,0) FI
                        + " bottle"
                        + IF bottles = 2 THEN "" ELSE "s" FI;
    print((bottles now," of beer on the wall",newline));
    print((bottles now," of beer",newline));
    print(("Take one down, pass it around",newline));
    print((bottles left," of beer on the wall",newline,newline))
OD
```


## ALGOL-M

```mw
BEGIN

COMMENT PRINT LYRICS TO "99 BOTTLES OF BEER ON THE WALL";

STRING FUNCTION BOTTLE(N); % GIVE CORRECT GRAMMATICAL FORM %
INTEGER N;
BEGIN
   IF N = 1 THEN
      BOTTLE := " BOTTLE"
   ELSE
      BOTTLE := " BOTTLES";
END;

INTEGER N;

N := 99;
WHILE N > 0 DO
   BEGIN
      WRITE(N, BOTTLE(N), " OF BEER ON THE WALL,");
      WRITEON(N, BOTTLE(N), " OF BEER");
      WRITE("TAKE ONE DOWN AND PASS IT AROUND, ");
      N := N - 1;
      IF N = 0 THEN
          WRITEON("NO MORE")
      ELSE
          WRITEON(N);
      WRITEON(BOTTLE(N), " OF BEER ON THE WALL");
      WRITE(" "); % BLANK LINE BETWEEN STANZAS %
   END;
WRITE("THANKS FOR SINGING ALONG!");

END
```


## AmigaE

```mw
PROC main()
  DEF t: PTR TO CHAR,
      s: PTR TO CHAR,
      u: PTR TO CHAR, i, x
  t := 'Take one down, pass it around\n'
  s := '\d bottle\s of beer\s\n'
  u := ' on the wall'
  FOR i := 99 TO 0 STEP -1
    ForAll({x}, [u, NIL], `WriteF(s, i, IF i <> 1 THEN 's' ELSE NIL,
                           x))
    IF i > 0 THEN WriteF(t)
  ENDFOR
ENDPROC
```


## Apache Ant

Implementation in Apache Ant, due to the limitations of Ant, this requires ant-contrib for arithmetic operations and a dummy target to keep Ant from detecting the loop.

```mw
<?xml version="1.0"?>
<project name="n bottles" default="99_bottles">

  <!-- ant-contrib.sourceforge.net for arithmetic and if -->
  <taskdef resource="net/sf/antcontrib/antcontrib.properties"/>

  <!-- start count of bottles, you can set this with
    e.g. ant -f 99.xml -Dcount=10 -->
  <property name="count" value="99"/>

  <target name="99_bottles">
    <antcall target="bottle">
      	<param name="number" value="${count}"/>
    </antcall>
  </target>

  <target name="bottle">
    <echo message="${number} bottles of beer on the wall"/>
    <echo message="${number} bottles of beer"/>
    <echo message="Take one down, pass it around"/>

    <math result="result" operand1="${number}" operation="-" operand2="1" datatype="int"/>

    <echo message="${result} bottles of beer on the wall"/>

    <if>
      <not><equals arg1="${result}" arg2="0" /></not>
      <then>
        <antcall target="bottleiterate">
          <param name="number" value="${result}"/>
        </antcall>
      </then>
    </if>
  </target>

  <target name="bottleiterate">
    <antcall target="bottle">
      	<param name="number" value="${number}"/>
    </antcall>
  </target>

</project>
```


## Apex

```mw
   for(Integer i = 99; i=0; i--){
      system.debug(i + ' bottles of beer on the wall');
      system.debug('\n');
      system.debug(i + ' bottles of beer on the wall');
      system.debug(i + ' bottles of beer');
      system.debug('take one down, pass it around');
   }
```


## APL

Works with

:

Dyalog APL

Works with

:

GNU APL

### Classic version

Translation of

:

J

```
     bob  ←  { (⍕⍵), ' bottle', (1=⍵)↓'s of beer'}
     bobw ←  {(bob ⍵) , ' on the wall'}
     beer ←  { (bobw ⍵) , ', ', (bob ⍵) , '; take one down and pass it around, ', bobw ⍵-1}
```

```
     ⍝ Dyalog APL invocation
     99↑beer¨ ⌽(1-⎕IO)+⍳99
```

```
     ⍝ GNU APL invocation (↑ and ⊃ differ, traditional APL2 meanings)
     ⊃beer¨ ⌽(1-⎕IO)+⍳99
```

### One line version

```
     ⍝ Dyalog and GNU APL
     ⍪{(⍕⍵),' bottles of beer on the wall, take one down and pass it around, ',(⍕⍵-1),' bottles of beer on the wall'}¨⌽⍳99
```


## App Inventor

### Using a 'for each <number>' block (simplest)

Note that the output label text is not displayed until the entire lyrics text has been built and there is some delay between button press and display. <CLICK HERE TO VIEW THE BLOCKS AND OUTPUT>

### Using a Clock Timer block (preferrred)

Output can be sent directly to a label with this preferred method as there is no noticeable delay between button press and output. <CLICK HERE TO VIEW THE BLOCKS AND OUTPUT>


## AppleScript

### Iteration

```mw
repeat with beerCount from 99 to 1 by -1
  set bottles to "bottles"
  if beerCount < 99 then
    if beerCount = 1 then
      set bottles to "bottle"
    end
    log "" & beerCount & " " & bottles & " of beer on the wall"
    log ""
  end
  log "" & beerCount & " " & bottles & " of beer on the wall"
  log "" & beerCount & " " & bottles & " of beer"
  log "Take one down, pass it around"
end
log "No more bottles of beer on the wall!"
```

### Declaration

```mw
-- BRIEF -----------------------------------------------------------------------
on run
    set localisations to ¬
        {"on the wall", ¬
            "Take one down, pass it around", ¬
            "Better go to the store to buy some more", "bottle"}
    
    intercalate("\n\n", ¬
        (map(curry(incantation)'s |λ|(localisations), enumFromTo(99, 0))))
end run

-- DECLARATIVE -----------------------------------------------------------------

-- incantation :: [String] -> Int -> String
on incantation(xs, n)
    script asset
        on |λ|(n)
            unwords({(n as string), item -1 of xs & cond(n ≠ 1, "s", "")})
        end |λ|
    end script
    
    script store
        on |λ|(n)
            unwords({asset's |λ|(n), item 1 of xs})
        end |λ|
    end script
    
    set {distribute, solve} to items 2 thru 3 of xs
    if n > 0 then
        unlines({store's |λ|(n), asset's |λ|(n), distribute, store's |λ|(n - 1)})
    else
        solve
    end if
end incantation

-- GENERICALLY DYSFUNCTIONAL ---------------------------------------------------

-- cond :: Bool -> a -> a -> a
on cond(bln, f, g)
    if bln then
        f
    else
        g
    end if
end cond

-- curry :: (Script|Handler) -> Script
on curry(f)
    script
        on |λ|(a)
            script
                on |λ|(b)
                    |λ|(a, b) of mReturn(f)
                end |λ|
            end script
        end |λ|
    end script
end curry

-- enumFromTo :: Int -> Int -> [Int]
on enumFromTo(m, n)
    if m > n then
        set d to -1
    else
        set d to 1
    end if
    set lst to {}
    repeat with i from m to n by d
        set end of lst to i
    end repeat
    return lst
end enumFromTo

-- intercalate :: Text -> [Text] -> Text
on intercalate(strText, lstText)
    set {dlm, my text item delimiters} to {my text item delimiters, strText}
    set strJoined to lstText as text
    set my text item delimiters to dlm
    return strJoined
end intercalate

-- map :: (a -> b) -> [a] -> [b]
on map(f, xs)
    tell mReturn(f)
        set lng to length of xs
        set lst to {}
        repeat with i from 1 to lng
            set end of lst to |λ|(item i of xs, i, xs)
        end repeat
        return lst
    end tell
end map

-- Lift 2nd class handler function into 1st class script wrapper 
-- mReturn :: Handler -> Script
on mReturn(f)
    if class of f is script then
        f
    else
        script
            property |λ| : f
        end script
    end if
end mReturn

-- unlines :: [String] -> String
on unlines(xs)
    intercalate(linefeed, xs)
end unlines

-- unwords :: [String] -> String
on unwords(xs)
    intercalate(space, xs)
end unwords
```


## Arbre

```mw
bottle(x):
  template: '
  $x bottles of beer on the wall.
  $x bottles of beer.
  Take one down and pass it around,
  $y bottles of beer on the wall.
  '

  if x==0
    template~{x: 'No more', y: 'No more'}
  else
    if x==1
      template~{x: x, y: 'No more'}
    else
      template~{x: x, y: x-1}

bottles(n):
  for x in [n..0]
    bottle(x)

99bottles():
  bottles(99) -> io
```


## Argile

```mw
use std

let X be an int
for each X from 99 down to 1
  prints X bottles of beer on the wall
  prints X bottles of beer
  prints "Take one down, pass it" around
  if X == 1
    echo No more "beer." Call da "amber lamps"
    break
  X--
  prints X bottles of beer on the wall "\n"
  X++
  .:around :. -> text {X>59 ? "around", "to me"}
  .:bottles:. -> text {X> 5 ? "bottles", (X>1 ? "buttles", "wall")}
  .:of beer:. -> text {X>11 ? "of beer", "ov beeer"}
  .:on the wall:. -> text {
    X>17 ? "on the wall", (X>1 ? "on the bwall", "in the buttle")
  }
```


## ArkScript

```mw
# try and get an argument from the command line invocation
(let arg
  (if (>= (len sys:args) 1)
    (toNumber (@ sys:args 0))
    nil))
# if no argument was passed the default value will be 100
(let i
  (if (nil? arg)
    100
    arg))

(let explode-bottles (fun (n)
  (if (> n 1) {
    (print (string:format "{} Bottles of beer on the wall\n{} bottles of beer\nTake one down, pass it around" n n))
    (print (string:format "{} Bottles of beer on the wall." (- n 1)))
    (explode-bottles (- n 1)) })
(explode-bottles i)

# alternative solution with a loop
(mut n i)
(while (> n 1) {
  (print (string:format "{} Bottles of beer on the wall\n{} bottles of beer\nTake one down, pass it around" n n))
  (set n (- n 1))
  (print (string:format "{} Bottles of beer on the wall." n)) })
```


## Aria

```mw
struct Lyrics {
    type func new(n: Int) {
        assert n > 0;
        return alloc(This) {
            .n = n,
        };
    }

    func prettyprint() {
        val suffix_n = this.n == 1 ? "" : "s";
        val suffix_n_minus_1 = this.n == 2 ? "" : "s";
        return "{0} bottle{2} of beer on the wall, {0} bottle{2} of beer.\nTake one down and pass it around, {1} bottle{3} of beer on the wall.\n".format(this.n, this.n-1, suffix_n, suffix_n_minus_1);
    }
}

struct Song {
    type func new(n: Int) {
        assert n > 0;
        return alloc(This) {
            .n = n,
        };
    }
    
    func iterator() {
        return this;
    }

    func next() {
        if this.n == 0 {
            return Box(){.done = true};
        }

        val n = this.n;
        this.n -= 1;

        return Box() {
            .done = false,
            .value = Lyrics.new(n),
        };
    }
}

func main() {
    val song = Song.new(99);
    for verse in song {
        println(verse);
    }
}
```


## ARM Assembly

See 99 Bottles of Beer/Assembly


## ArnoldC

As ArnoldC does not feature string concatenation, the numbers of bottles and the rest of the parts of the lyrics are printed on separate lines.

```mw
IT'S SHOWTIME
HEY CHRISTMAS TREE is0
YOU SET US UP @NO PROBLEMO
HEY CHRISTMAS TREE bottles
YOU SET US UP 99
STICK AROUND is0
TALK TO THE HAND bottles
TALK TO THE HAND " bottles of beer on the wall"
TALK TO THE HAND bottles
TALK TO THE HAND " bottles of beer"
TALK TO THE HAND "Take one down, pass it around"
GET TO THE CHOPPER bottles
HERE IS MY INVITATION bottles
GET DOWN 1
ENOUGH TALK
TALK TO THE HAND bottles
TALK TO THE HAND " bottles of beer on the wall"
GET TO THE CHOPPER is0
HERE IS MY INVITATION bottles
LET OFF SOME STEAM BENNET 0
ENOUGH TALK
CHILL
YOU HAVE BEEN TERMINATED
```


## Arturo

```mw
s: "s"

loop 99..1 'i [
    print ~"|i| bottle|s| of beer on the wall,"
    print ~"|i| bottle|s| of beer"
    print ~"Take one down, pass it around!"
    if 1=i-1 -> s: ""

    switch i>1 [
        print ~"|i-1| bottle|s| of beer on the wall!"
        print ""
    ] -> print "No more bottles of beer on the wall!"
]
```


## AsciiDots

```mw
 /-99#-.
/>*$_#-$_" bottles of beer on the wall, "-$_#-$" bottles of beer."\
|[-]1#-----" ,dnuora ti ssap dna nwod eno ekaT"_$-----------------/
| |
| | &-".llaw eht no reeb fo selttob 99 ,erom emos yub dna erots eht ot oG"$\
| |/$""-$"No more bottles of beer on the wall, no more bottles of beer."---/
| |\".llaw eht no reeb fo selttob erom on ,dnuora ti ssap dna nwod eno ekaT"$-".reeb fo elttob 1"$\
| |          /-$"1 bottle of beer on the wall."-$""-$_"1 bottle of beer on the wall, "------------/
| | /-------\|
| \-*--{=}-\\~$_#-$" bottles of beer on the wall."\
|   \-#1/  \-/                                    |
\----------------------------------------------""$/
```


## Astro

```mw
fun bottles(n): match __args__:
    (0) => "No more bottles"
    (1) => "1 bottle"
    (_) => "$n bottles"

for n in 99..-1..1:
    print @format"""
    {bottles n} of beer on the wall
    {bottles n} of beer
    Take one down, pass it around
    {bottles n-1} of beer on the wall\n
    """
```


## Asymptote

```mw
// Rosetta Code problem: http://rosettacode.org/wiki/99_bottles_of_beer
// by Jjuanhdez, 05/2022

int bottles = 99;

for (int i = bottles; i > 0; --i) {
    write(string(i), " bottles of beer on the wall,");
    write(string(i), " bottles of beer.");
    write("Take one down and pass it around,");
    if (i == 1) {
        write("no more bottles of beer on the wall...");
    } else {
        write(string(i-1), " bottles of beer on the wall...");
    }
}
        
write("No more bottles of beer on the wall,");
write("no more bottles of beer."); 
write("Go to the store and buy some more,");
write(" 99 bottles of beer on the wall.");
```


## ATS

```mw
//
#include
"share/atspre_staload.hats"
//
(* ****** ****** *)

fun bottles
  (n0: int): void = let
//
fun loop (n: int): void =
(
  if n > 0 then
  (
    if n0 > n then println! ();
    println! (n, " bottles of beer on the wall");
    println! (n, " bottles of beer");
    println! ("Take one down, pass it around");
    println! (n-1, " bottles of beer on the wall");
    loop (n - 1)
  ) (* end of [if] *)
)
//
in
  loop (n0)
end // end of [bottles]

(* ****** ****** *)

implement main0 () = bottles (99)
```


## AutoHotkey

See 99 Bottles of Beer/Shell


## AutoIt

See 99 Bottles of Beer/Shell


## AWK

### Regular version

If you don't want so many beers, here you can specify the starting amount. For example, just a sixpack:

```mw
# usage:  gawk  -v i=6  -f beersong.awk

function bb(n) {
	b = " bottles of beer"
	if( n==1 ) { sub("s","",b) }
	if( n==0 ) { n="No more" }
	return n b
}

BEGIN {
	if( !i ) { i = 99 }
	ow = "on the wall"
	td = "Take one down, pass it around."
	print "The beersong:\n"
	while (i > 0) {
		printf( "%s %s,\n%s.\n%s\n%s %s.\n\n", 
			bb(i), ow, bb(i), td, bb(--i), ow )
		if( i==1 ) sub( "one","it", td )
	}
	print "Go to the store and buy some more!"
}
```

**Output:**

```
The beersong:

99 bottles of beer on the wall,
99 bottles of beer.
Take one down, pass it around.
98 bottles of beer on the wall.

...

3 bottles of beer on the wall,
3 bottles of beer.
Take one down, pass it around.
2 bottles of beer on the wall.

2 bottles of beer on the wall,
2 bottles of beer.
Take one down, pass it around.
1 bottle of beer on the wall.

1 bottle of beer on the wall,
1 bottle of beer.
Take it down, pass it around.
No more bottles of beer on the wall.

Go to the store and buy some more!
```

### Bottled version

See 99-bottles-of-beer.net


## Axe

Pauses are added to accommodate the small calculator screen so all of the text can be read.

```mw
99→B
While B
 Disp B▶Dec," BOTTLES OF","BEER ON THE WALL"
 Disp B▶Dec," BOTTLES OF","BEER",i,i
 getKeyʳ
 Disp "TAKE ONE DOWN",i,"PASS IT AROUND",i
 B--
 Disp B▶Dec," BOTTLES OF","BEER ON THE WALL",i
 getKeyʳ
End
```


## Babel

```mw
-- beer.sp

{b  " bottles of beer"         <
 bi { itoa << }                <
 bb { bi ! b << w << "\n" << } <
 w  " on the wall"             <
 beer
    {<-
        { iter 1 + dup 
          <- bb ! -> 
          bi ! b << "\n" <<
          "Take one down, pass it around\n" <<
          iter bb ! "\n" << }
    -> 
    times}
    < }

-- At the prompt, type 'N beer !' (no quotes), where N is the number of stanzas you desire
```


## BabyCobol

```mw
      * Pointing out some interesting things:
      *    - BY 0 subclause of VARYING (illegal in some COBOL dialects)
      *    - PERFORM THROUGH with internal/external GO TOs
      *    - using non-reserved keywords (END, DATA)
      *    - ALTER (works the same way in COBOL)
      *    - fall-through from MANY-BOTTLES
      *    - the last NEXT SENTENCE does nothing (plays the role of EXIT)
       IDENTIFICATION DIVISION.
           PROGRAM-ID. 99 BOTTLES.
       DATA DIVISION.
       01 DATA PICTURE IS 999.
       PROCEDURE DIVISION.
           LOOP VARYING DATA FROM 99 BY 0
               PERFORM COUNT-BOTTLES THROUGH END
               DISPLAY DATA "bottles of beer"
               DISPLAY "Take one down, pass it around"
               SUBTRACT 1 FROM DATA
               IF DATA = 1
               THEN ALTER COUNT-BOTTLES TO PROCEED TO SINGLE-BOTTLE
               END
               PERFORM COUNT-BOTTLES THROUGH END
               DISPLAY ""
           END.
       NO-BOTTLES-LEFT.
           DISPLAY "No bottles of beer on the wall"
           DISPLAY ""
           DISPLAY "Go to the store and buy some more"
           DISPLAY "99 bottles of beer on the wall".
           STOP.
       COUNT-BOTTLES.
           GO TO MANY-BOTTLES.
       SINGLE-BOTTLE.
           DISPLAY DATA "bottle of beer on the wall".
           GO TO NO-BOTTLES-LEFT.
       MANY-BOTTLES.
           DISPLAY DATA "bottles of beer on the wall".
       END.
           NEXT SENTENCE.
```


## Ballerina

Translation of

:

Aime

```mw
// https://rosettacode.org/wiki/99_bottles_of_beer
import ballerina/io;

public function main() {
    foreach int i in int:range(99, 0, -1) {
        io:print(i); io:println(" bottles of beer on the wall");
        io:print(i); io:println(" bottles of beer");
        io:println("Take one down, pass it around");
        io:print(i-1); io:println(" bottles of beer on the wall\n");
    }
}
```

**Output:**

```
99 bottles of beer on the wall
99 bottles of beer
Take one down, pass it around
98 bottles of beer on the wall

...

2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottles of beer on the wall

1 bottles of beer on the wall
1 bottles of beer
Take one down, pass it around
0 bottles of beer on the wall
```


## BASIC

### Applesoft BASIC

See 99 Bottles of Beer/Basic

### BaCon

See 99 Bottles of Beer/Basic#BaCon

### BASIC256

See 99 Bottles of Beer/Basic

### BazzBasic

See 99 Bottles of Beer/Basic

### BBC BASIC

See 99 Bottles of Beer/Basic

### Commodore BASIC

See 99 Bottles of Beer/Basic#Commodore_BASIC

### Craft Basic

See 99 Bottles of Beer/Basic#Craft_Basic

### Creative Basic

See 99 Bottles of Beer/Basic

### FBSL

See 99 Bottles of Beer/Basic

### FreeBASIC

See 99 Bottles of Beer/Basic

### FUZE BASIC

See 99 Bottles of Beer/Basic

### GW-BASIC

See 99 Bottles of Beer/Basic

### Integer BASIC

See 99 Bottles of Beer/Basic

### Liberty BASIC

See 99 Bottles of Beer/Basic

### Microsoft Small Basic

See 99 Bottles of Beer/Basic

### Minimal BASIC

See 99 Bottles of Beer/Basic

### MSX Basic

See 99 Bottles of Beer/Basic

### OxygenBasic

See 99 Bottles of Beer/Basic

### PowerBASIC

See 99 Bottles of Beer/Basic

### PureBasic

See 99 Bottles of Beer/Basic

### QB64

See 99 Bottles of Beer/Basic

### QBasic

See 99 Bottles of Beer/Basic

### QuickBASIC

See 99 Bottles of Beer/Basic

### REALbasic

See 99 Bottles of Beer/Basic

### Run BASIC

See 99 Bottles of Beer/Basic

### Sinclair ZX81 BASIC

See 99 Bottles of Beer/Basic

### smart BASIC

See 99 Bottles of Beer/Basic

### TI-83 BASIC

See 99 Bottles of Beer/Basic

### TI-89 BASIC

See 99 Bottles of Beer/Basic

### Tiny BASIC

See 99 Bottles of Beer/Basic

### True BASIC

See 99 Bottles of Beer/Basic

### Visual Basic

See 99 Bottles of Beer/Basic

### Visual Basic .NET

See 99 Bottles of Beer/Basic

### XBasic

See 99 Bottles of Beer/Basic

### Yabasic

See 99 Bottles of Beer/Basic

### ZX Spectrum Basic

See 99 Bottles of Beer/Basic


## Batch File

See 99 Bottles of Beer/Shell


## Battlestar

```mw
const bottle = " bottle"
const plural = "s"
const ofbeer = " of beer"
const wall = " on the wall"
const sep = ", "
const takedown = "Take one down and pass it around, "
const u_no = "No"
const l_no = "no"
const more = " more bottles of beer"
const store = "Go to the store and buy some more, "
const dotnl = ".\n"
const nl = "\n"

// Reserve 1024 bytes in the .bss section
var x 1024

// Write two digits, based on the value in a
fun printnum
    b = a
    a >= 10
        a /= 10
        // modulo is in the d register after idiv
        b = d
        a += 48 // ASCII value for '0'
        print(chr(a))
    end
    a = b
    a += 48 // ASCII value for '0'
    print(chr(a))
end

fun main
    loop 99
        // Save loop counter for later, twice
        c -> stack
        c -> stack

        // Print the loop counter (passed in the a register)
        a = c
        printnum()

        // N, "bottles of beer on the wall, "
        x = bottle
        x += plural
        x += ofbeer
        x += wall
        x += sep
        print(x)

        // Retrieve and print the number
        stack -> a
        printnum()

        // N, "bottles of beer.\nTake one down and pass it around,"
        x = bottle
        x += plural
        x += ofbeer
        x += dotnl
        x += takedown
        print(x)

        // N-1, "bottles of beer on the wall."
        stack -> a
        a--

        // Store N-1, used just a few lines down
        a -> stack
        printnum()
        print(bottle)

        // Retrieve N-1
        stack -> a

        // Write an "s" if the count is not 1
        a != 1
            print(plural)
        end

        // Write the rest + a blank line
        x = ofbeer
        x += wall
        x += dotnl
        x += nl
        print(x)

        // Skip to the top of the loop while the counter is >= 2
        continue (c >= 2)

        // At the last two

        // "1 bottle of beer on the wall,"
        a = 1
        printnum()
        x = bottle
        x += ofbeer
        x += wall
        x += sep
        print(x)

        // "1"
        a = 1
        printnum()

        // "bottle of beer. Take one down and pass it around,"
        // "no more bottles of beer on the wall."
        // Blank line
        // "No more bottles of beer on the wall,"
        // "no more bottles of beer."
        // "Go to the store and buy some more,"
        x = bottle
        x += ofbeer
        x += dotnl
        x += takedown
        x += l_no
        x += more
        x += wall
        x += dotnl
        x += nl
        x += u_no
        x += more
        x += wall
        x += sep
        x += l_no
        x += more
        x += dotnl
        x += store
        print(x)

        // "99"
        a = 99
        printnum()

        // "bottles of beer on the wall."
        x = bottle
        x += plural
        x += ofbeer
        x += wall
        x += dotnl
        print(x)
    end
end

// vim: set syntax=c ts=4 sw=4 et:
```


## Bc

Works with

:

GNU bc

version 1.06

```mw
i = 99;
while ( 1 ) {
     print i , " bottles of beer on the wall\n";
     print i , " bottles of beer\nTake one down, pass it around\n";
     if (i == 2) {
          break
     }
     print --i , " bottles of beer on the wall\n";
}

print --i , " bottle of beer on the wall\n";
print   i , " bottle of beer on the wall\n";
print   i , " bottle of beer\nTake it down, pass it around\nno more bottles of beer on the wall\n";
quit
```


## BCPL

```mw
get "libhdr"

let number(n) be
    test n=0
        then writes("No more")
        else writen(n)

let plural(n) be
    test n=1
        then writes(" bottle")
        else writes(" bottles")
        
let bottles(n) be
$(  number(n)
    plural(n)
$)

let verse(n) be
$(  bottles(n)
    writes(" of beer on the wall,*N")
    bottles(n)
    writes(" of beer,*NTake ")
    test n=1
        then writes("it")
        else writes("one")
    writes(" down and pass it around,*N")
    bottles(n-1)
    writes(" of beer on the wall!*N*N")
$)

let start() be
    for n = 99 to 1 by -1 do verse(n)
```


## beeswax

Straightforward implementation, displaying the full lyrics given on [ http://99-bottles-of-beer.net/ ]

```mw
  >       NN      p
> d#_8~2~(P~3~.~1~>{` bottles of beer on the wall, `{` bottles of beer.`q
d`.llaw eht no reeb fo selttob `{pLM` ,dnuora ti ssap dna nwod eno ekaT`N<
q`.llaw eht no reeb fo elttob ` {<
 >        NN       >{` bottle of beer on the wall, `{` bottle of beer.`N  q
pN `.llaw eht no reeb fo selttob erom on ,dnuora ti ssap dna nwod eno ekaT`<
>N`No more bottles of beer on the wall, no more bottles of beer.`N  q
;`.llaw eht no reeb fo selttob 99 ,erom emos yub dna erots eht ot oG`<
```

A much more “economic” version that tries to avoid repetition at the price of complicated conditional jumps and self-modifying code that takes up more place than the actual strings themselves. Output is the same as in the straightforward version.

```mw
#D@.9~2~@M.7~P9zE       `N`p
DMM@.9@.~2~.++~5zE      `n`>`o`p
>0f1ff#             q   `erom `<           #h3~1z<           #h3~1z<    #h3~1z<
d_8~2~(P~3~.  ~1~>"b{>X^^^` bottle` ` of beer`@g"pX` on the wall`g"pX   `, ` @p #
               > d   <#XL#^^^^^`s`#            #  ##      #        >    `.`NN@  X#
                   b                                             <            <  <
                         >~L#^^^^`s`#      #h3~1zX    #h3~1z<#      #  #      # #
               d             #h3~1z<#            #> `.`   g"pXN @"p `Take one down and `p
>^^^^^^^^^;     .#   b              XgNN                    <       bM` ,dnuora ti ssap`<
d^^^^^^^^^^^^^^^^X~3~P(~2~8` ,erom emos yub dna erots eht ot`` oG`<
```


## Befunge

See 99 Bottles of Beer/EsoLang


## BlitzMax

```mw
local bot:int = 99

repeat
    print string(bot)+" bottles of beer on the wall,"
    print string(bot)+" bottles of beer."
    print "Take one down, pass it around,"
    bot:-1
    print string(bot)+" bottles of beer on the wall."
    print
until bot = 1

print "1 bottle of beer on the wall,"
print "1 bottle of beer."
print "Take it down, pass it around,"
print "No more bottles of beer on the wall!"
```


## BlooP

Output is always in caps in the interpreter I use, but I typed the input in correct case to spare those whose interpreter might do lowercase and don't want to have this song shouted at them ;D.

```mw
DEFINE PROCEDURE ''MINUS'' [A,B]:
BLOCK 0: BEGIN
  IF A < B, THEN:
    QUIT BLOCK 0;
  LOOP AT MOST A TIMES:
  BLOCK 1: BEGIN
    IF OUTPUT + B = A, THEN:
      QUIT BLOCK 0;
    OUTPUT <= OUTPUT + 1;
  BLOCK 1: END;
BLOCK 0: END.

DEFINE PROCEDURE ''BOTTLES'' [COUNT]:
BLOCK 0: BEGIN
	CELL(0) <= COUNT;
	LOOP COUNT + 1 TIMES:
	
	BLOCK 1: BEGIN
		
		IF CELL(0) > 1, THEN:
			PRINT[CELL(0), ' bottles of beer on the wall, ', CELL(0), ' bottles of beer. Take one down, pass it around, ', MINUS[CELL(0), 1], ' bottles of beer on the wall.'];
		
		IF CELL(0) = 1, THEN:
      PRINT['1 botle of beer on the wall, 1 bottle of beer. Take one down, pass it around, No more bottles of beer on the wall.'];
    
    IF CELL(0) = 0, THEN:
      PRINT['No more bottles of beer on the wall, no more bottles of beer. Go to the store, buy 99 more, 99 bottles of beer on the wall!'];

    CELL(0) <= MINUS[CELL(0), 1];
		
	BLOCK 1: END;
BLOCK 0: END.

BOTTLES[99];
```


## Bracmat

Copy the code to a file called BottlesOfBeer.bra. Start Bracmat and after the `{?}` prompt write `get$"BottlesOfBeer.bra"` <Enter>. Then, after the next prompt, write `!r` <Enter>. Notice that the lyrics has two more lines at the end:

```
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
```

Code to save to BottlesOfBeer.bra:

```mw
{BottlesOfBeer.bra

See http://99-bottles-of-beer.net/}

X=
  new
=   n upper nbottles lyrics
  .   99:?n
    & ( upper
      = .@(!arg:%@?a ?z)&str$(upp$!a !z)
      )
    & ( nbottles
      =   
        .   str
          $ ( (   !arg:>0
                &   !arg
                    " bottle"
                    (!arg:1&|s)
              | "no more bottles"
              )
              " of beer"
            )
      )
    & ( lyrics
      =   (upper$(nbottles$!n:?x) " on the wall, " !x ".\n")
          (   !n+-1:?n:~<0
            &   "Take one down and pass it around, "
                nbottles$!n
                " on the wall.

"
                !lyrics
          |   "Go to the store and buy some more, "
              nbottles$99
              " on the wall.
"
          )
      )
    & put$(str$!lyrics);

r=
  get'"BottlesOfBeer.bra"
& rmv$(str$(BottlesOfBeer ".bak"))
& ren$("BottlesOfBeer.bra".str$(BottlesOfBeer ".bak"))
&   put
  $ ( "{BottlesOfBeer.bra

See http://99-bottles-of-beer.net/}

"
    , "BottlesOfBeer.bra"
    , NEW
    )
& lst'(X,"BottlesOfBeer.bra",APP)
& put'(\n,"BottlesOfBeer.bra",APP)
& lst'(r,"BottlesOfBeer.bra",APP)
& put$(str$("\nnew'" X ";\n"),"BottlesOfBeer.bra",APP);

new'X;
```


## Brainf***

See 99 Bottles of Beer/EsoLang


## Brat

```mw
99.to 2 { n |
  p "#{n} bottles of beer on the wall, #{n} bottles of beer!"
  p "Take one down, pass it around, #{n - 1} bottle#{true? n > 2 's' ''} of beer on the wall."
}

p "One bottle of beer on the wall, one bottle of beer!"
p "Take one down, pass it around, no more bottles of beer on the wall."
```


## Bruijn

```mw
:import std/Combinator .
:import std/Number .
:import std/String .

main [y [[=?0 case-end case-rec]] (+99)]
	case-rec n ++ t1 ++ n ++ t2 ++ t3 ++ n ++ t1 ++ "\n" ++ (1 --0)
		n number→string 0
		t1 " bottles of beer on the wall\n"
		t2 " bottles of beer\n"
		t3 "Take one down, pass it around\n"
	case-end empty
```


## BQN

```mw
Pl ← {(𝕩≠1)/"s"}
{𝕨∾(@+10)∾𝕩}´{(•Fmt 𝕨)∾" "∾𝕩}´¨∾{
  ⟨
    ⟨𝕩,"bottle"∾(Pl 𝕩)∾" of beer on the wall"⟩
    ⟨𝕩,"bottle"∾(Pl 𝕩)∾" of beer"⟩
    ⟨"Take one down, pass it around"⟩
    ⟨𝕩-1,"bottle"∾(Pl 𝕩-1)∾" of beer on the wall"∾@+10⟩
  ⟩
}¨⌽1+↕99
```

`•Fmt` is used to convert numbers to strings.

`Pl` tells whether the number is singular or plural.

Then, the two folds join all the individual lines together.
