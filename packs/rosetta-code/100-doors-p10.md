---
title: "100 doors (part 10/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 10/10
---

## VBA

```mw
Sub Rosetta_100Doors()
Dim Door(100) As Boolean, i As Integer, j As Integer
For i = 1 To 100 Step 1
    For j = i To 100 Step i
        Door(j) = Not Door(j)
    Next j
    If Door(i) = True Then
        Debug.Print "Door " & i & " is Open"
    Else
        Debug.Print "Door " & i & " is Closed"
    End If
Next i
End Sub
<!-- /lang -->

*** USE THIS ONE, SEE COMMENTED LINES, DONT KNOW WHY EVERYBODY FOLLOWED OTHERS ANSWERS AND CODED THE PROBLEM DIFFERENTLY ***
*** ALWAYS USE AND TEST A READABLE, EASY TO COMPREHEND CODING BEFORE 'OPTIMIZING' YOUR CODE AND TEST THE 'OPTIMIZED' CODE AGAINST THE 'READABLE' ONE.
Panikkos Savvides.

Sub Rosetta_100Doors2()
Dim Door(100) As Boolean, i As Integer, j As Integer
Dim strAns As String
' There are 100 doors in a row that are all initially closed.
' You make 100 passes by the doors.
For j = 1 To 100
    ' The first time through, visit every door and toggle the door
    ' (if the door is closed, open it; if it is open, close it).
    For i = 1 To 100 Step 1
      Door(i) = Not Door(i)
    Next i
    ' The second time, only visit every 2nd door (door #2, #4, #6, ...), and toggle it.
    For i = 2 To 100 Step 2
      Door(i) = Not Door(i)
    Next i
    ' The third time, visit every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.
    For i = 3 To 100 Step 3
      Door(i) = Not Door(i)
    Next i
Next j

For j = 1 To 100
    If Door(j) = True Then
        strAns = j & strAns & ", "
    End If
Next j

If Right(strAns, 2) = ", " Then strAns = Left(strAns, Len(strAns) - 2)
If Len(strAns) = 0 Then strAns = "0"
Debug.Print "Doors [" & strAns & "] are open, the rest are closed."
' Doors [0] are open, the rest are closed., AKA ZERO DOORS OPEN
End Sub
```


## VBScript

Works with

:

Windows Script Host

version 5.7

**Unoptimized**

```mw
Dim doorIsOpen(100), pass, currentDoor, text

For currentDoor = 0 To 99
	doorIsOpen(currentDoor) = False
Next

For pass = 0 To 99
	For currentDoor = pass To 99 Step pass + 1
		doorIsOpen(currentDoor) = Not doorIsOpen(currentDoor)
	Next
Next

For currentDoor = 0 To 99
	text = "Door #" & currentDoor + 1 & " is "
	If doorIsOpen(currentDoor) Then
		text = text & "open."
	Else
		text = text & "closed."
	End If
	WScript.Echo(text)
Next
```


## Vedit macro language

**Unoptimized** This implementation uses a free edit buffer as data array and for displaying the results. A closed door is represented by a character '-' and an open door by character 'O'.

```mw
Buf_Switch(Buf_Free)
Ins_Char('-', COUNT, 100)                      // All doors closed
for (#1 = 1; #1 <= 100; #1++) {
    for (#2 = #1; #2 <= 100; #2 += #1) {
        Goto_Col(#2)
        Ins_Char((Cur_Char^0x62), OVERWRITE)   // Toggle between '-' and 'O'
    }
}
```

**Optimized**

```mw
Buf_Switch(Buf_Free)
Ins_Char('-', COUNT, 100)
for (#1=1; #1 <= 10; #1++) {
    Goto_Col(#1*#1)
    Ins_Char('O', OVERWRITE)
}
```

Output:

```
O--O----O------O--------O----------O------------O--------------O----------------O------------------O
```


## Verilog

```mw
module main;
  integer i;
  
  initial begin
    $display("Las siguientes puertas están abiertas:");
    for (i=1; i<=10; i=i+1) if (i%i*i<11) $display(i*i);
    $finish ;
  end
endmodule
```


## VHDL

**unoptimized**

```mw
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity DOORS is
	port (CLK: in std_logic; OUTPUT: out std_logic_vector(1 to 100));
end DOORS;

architecture Behavioral of DOORS is
begin
	process (CLK)
	variable TEMP: std_logic_vector(1 to 100);
	begin
		--setup closed doors
		TEMP := (others => '0');
		
		--looping through
		for i in 1 to TEMP'length loop
			for j in i to TEMP'length loop
				if (j mod i) = 0 then
					TEMP(j) := not TEMP(j);
				end if;
			end loop;
		end loop;
		
		--assign output
		OUTPUT <= TEMP;
	end process;
end Behavioral;
```

**unoptimized and synthesizable**

```mw
LIBRARY ieee;
USE ieee.std_logic_1164.all;

entity doors is
  port (
        clk   : in std_logic;
        reset : in std_logic;
        door  : buffer std_logic_vector(1 to 100)
        );
end entity doors;

architecture rtl of doors is
  signal step : integer range 1 to 101;
  signal addr : integer range 1 to 201;
begin
  proc_step: process(clk, reset)
  begin
    if reset = '1' then
      step  <= 1;
      addr  <= 1;
      door <= (others => '0');
    elsif rising_edge(clk) then
      if addr <= 100 then
        door(addr) <= not door(addr);
        addr <= addr + step;
      elsif step <= 100 then
        addr <= step + 1;
        step <= step + 1;
      end if;
    end if;
  end process;
end;
```

The synthesis requires 116 FFs plus combinatorial logic.

The result is stable after 581 clock cycles.


## Visual Basic

```mw
Public Sub Doors100()
  ' the state of a door is represented by the data type boolean (false = door closed, true = door opened)
  Dim doorstate(1 To 100) As Boolean ' the doorstate()-array is initialized by VB with value 'false'
  Dim i As Long, j As Long
  
  For i = 1 To 100
      For j = i To 100 Step i
          doorstate(j) = Not doorstate(j)
      Next j
  Next i
  
  Debug.Print "The following doors are open:"
  For i = 1 To 100
      ' print number if door is openend
      If doorstate(i) Then Debug.Print CStr(i)
  Next i
End Sub
```

Output:

```
The following doors are open:
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


## Visual Basic .NET

Works with

:

Visual Basic .NET

version 9.0+

**unoptimized**

```mw
Module Module1

   Sub Main()
       Dim doors(100) As Boolean 'Door 1 is at index 0

       For pass = 1 To 100
           For door = pass - 1 To 99 Step pass
               doors(door) = Not doors(door)
           Next
       Next

       For door = 0 To 99
           Console.WriteLine("Door # " & (door + 1) & " is " & If(doors(door), "Open", "Closed"))
       Next

       Console.ReadLine()
   End Sub

End Module
```

**optimized**

```mw
Module Module1

   Sub Main()
       Dim doors(100) As Boolean 'Door 1 is at index 0

       For i = 1 To 10
           doors(i ^ 2 - 1) = True
       Next

       For door = 0 To 99
           Console.WriteLine("Door # " & (door + 1) & " is " & If(doors(door), "Open", "Closed"))
       Next

       Console.ReadLine()
   End Sub

End Module
```


## V (Vlang)

### Unoptimized

```mw
const number_doors = 101

fn main() {
    mut closed_doors := []bool{len: number_doors, init: true} 
    for pass in 0..number_doors {
        for door := 0; door < number_doors; door += pass + 1 {
            closed_doors[door] = !closed_doors[door]
        }
    }
    for pass in 1..number_doors {
        if !closed_doors[pass] {
            println('Door #$pass Open')
        }
    }
}
```

Output:

```
Door #1 Open
Door #4 Open
Door #9 Open
Door #16 Open
Door #25 Open
Door #36 Open
Door #49 Open
Door #64 Open
Door #81 Open
Door #100 Open
```

### Optimized GO Inspired

```mw
const door_number = 100

fn main(){
    mut doors := []bool{ len: door_number, init: false } //true open false closed

    mut door_nbr := 1
    mut increment := 0

    for current in 1..( door_number + 1) {
        if current == door_nbr {
            doors[current - 1] = true
            increment++
            door_nbr += 2 * increment + 1
			print('O')
		} else {
			print('=')
		}
    }
    println('')
}
```

Output:

```
O==O====O======O========O==========O============O==============O================O==================O
```

### Optimized

```mw
import math

const number_doors = 101

fn main() {
    max_i := int(math.sqrt(f64(number_doors - 1))) + 1
    for i in 1..max_i {
        door := i * i
		println("Door ${door} open")
    }
}
```

Output:

```
Door 1 open
Door 4 open
Door 9 open
Door 16 open
Door 25 open
Door 36 open
Door 49 open
Door 64 open
Door 81 open
Door 100 open
```

### Optimized +

```mw
fn main() {
	for i in 1..11 {
		print ( " Door ${i*i} is open.\n" )
	}
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


## VTL-2

```mw
10 D=1
20 :D)=0
30 D=D+1
40 #=100>D*20
50 P=1
60 D=P
70 :D)=:D)=0
80 D=D+P
90 #=100>D*70
100 P=P+1
110 #=100>P*60
120 D=1
130 #=:D)*170
140 D=D+1
150 #=100>D*130
160 #=999
170 ?="DOOR ";
180 ?=D
190 ?=" IS OPEN"
200 #=!
```

**Output:**

```
DOOR 1 IS OPEN
DOOR 4 IS OPEN
DOOR 9 IS OPEN
DOOR 16 IS OPEN
DOOR 25 IS OPEN
DOOR 36 IS OPEN
DOOR 49 IS OPEN
DOOR 64 IS OPEN
DOOR 81 IS OPEN
DOOR 100 IS OPEN
```


## Wart

```mw
def (doors n)
  let door (table)
    for step 1 (step <= n) ++step
      for j 0 (j < n) (j <- j+step)
        zap! not door.j

    for j 0 (j < n) ++j
      when door.j
        pr j
        pr " "
```


## WDTE

```mw
let a => import 'arrays';
let s => import 'stream';
let io => import 'io';

let toggle doors m =>
	a.stream doors
	-> s.enumerate
	-> s.map (@ s n => [+ (a.at n 0) 1; a.at n 1])
	-> s.map (@ s n => switch n {
			(@ s n => == (% (a.at n 0) m) 0) => ! (a.at n 1);
			true => a.at n 1;
		})
	-> s.collect
	;

s.range 100
-> s.map false
-> s.collect : doors
-> s.range 1 100
-> s.reduce doors toggle
-> a.stream
-> s.map (@ s n => switch 0 {
		n => 'Open';
		true => 'Closed';
	} -- io.writeln io.stdout)
-> s.drain
;
```

Not the most efficient code, to say the least. This has a few more allocations than should sanely be used for a problem like this.


## Wortel

Translation of

:

JavaScript

```mw
; unoptimized
+^[
  @var doors []
  
  @for i rangei [1 100]
    @for j rangei [i 100 i]
      :!@not `j doors
  
  @for i rangei [1 100]
    @if `i doors
      !console.log "door {i} is open"
]
; optimized, map square over 1 to 10
!*^@sq @to 10
```


## Wrapl

**Unoptimized**

```mw
MOD Doors;

IMP Agg.Table;
IMP Std.String;
IMP IO.Terminal USE Out;

VAR door <- {}; EVERY door[1:to(100), "closed"];

DEF toggle(num) door[num] <- door[num] = "open" => "closed" // "open";

EVERY WITH pass <- 1:to(100), num <- pass:to(100, pass) DO toggle(num);

Out:write('Doors {door @ String.T}.');

END Doors.
```

**Optimized**

```mw
MOD Doors;

IMP IO.Terminal USE Out;

DEF open <- ALL 1:to(100) ^ 2 \ $ <= 100;
DEF closed <- ALL 1:to(100) \ NOT $ IN open;

Out:write('Doors {open} are open.\n');
Out:write('Doors {closed} are closed.\n');

END Doors.
```


## Wren

**Unoptimized**

```mw
var doors = [true] * 100
for (i in 1..100) {
    var j = i
    while (j < 100) {
        doors[j] = !doors[j]
        j = j + i + 1
    }
}

for (i in 0...100) {
    if (doors[i]) System.write("%(i + 1) ")
}
System.print()
```

**Optimized**

```mw
var door = 1
var increment = 3
while (door <= 100) {
    System.write("%(door) ")
    door = door + increment
    increment = increment + 2
}
System.print()
```

**Output:**

For both versions:

```
1 4 9 16 25 36 49 64 81 100 
```


## X86 Assembly

Works with

:

MASM 6+

```mw
		.NOLIST

; The task can be completed in 48 and "half" steps:
; On the first pass ALL doors are opened.
; On the second pass every EVEN door is closed.
; So, instead of all closed, the doors can initially be:
; Every odd door open, every even door closed and start at pass 3.
; On 51st and all the next passes, only one door is visited per pass:
; On 51st pass door 51, on 52nd pass door 52 etc.
; So, after pass 50, we can make "half a pass" starting with door 51
; and toggling every door up to and including 100.
; The code uses only volatile registers, so, no string (STOS etc) instructions.

		TITLE	100 Doors
		PAGE	, 132
		.686
		.MODEL	FLAT
		OPTION	CASEMAP:NONE

		.SFCOND
		.LIST

; =============================================================================

		.DATA?

Doors		BYTE	100 DUP ( ? )

; =============================================================================

		.CODE

Pass_Doors	PROC

		MOV	EDX, OFFSET Doors	; Initialize all doors.
		MOV	ECX, SIZEOF Doors / SIZEOF DWORD
		MOV	EAX, 01010101h		; This does first and second pass.

Close_Doors:	MOV	[ EDX ], EAX
		ADD	EDX, SIZEOF DWORD
		LOOP	Close_Doors

		MOV	ECX, 2			; Pass and step.

Pass_Loop:	MOV	EDX, OFFSET Doors

		ASSUME	EDX:PTR BYTE

Doors_Loop:	XOR	[ EDX ], 1		; Toggle this door.
		ADD	EDX, ECX                ; Advance.
		CMP	EDX, OFFSET Doors[ SIZEOF Doors ]

		JB	Doors_Loop

		INC	ECX
		CMP	ECX, SIZEOF Doors

		JB	Pass_Loop

		XOR	Doors[ SIZEOF Doors -1 ], 1 ; This is pass 100.
		RET

Pass_Doors	ENDP

; =============================================================================

		END
```


## XBasic

Works with

:

Windows XBasic

```mw
PROGRAM "100doors"
VERSION "0.0001"

IMPORT "xma"
IMPORT "xst"

DECLARE FUNCTION Entry()

FUNCTION Entry()
  maxpuertas = 100
  cont = 0
  DIM puertas[100]

  FOR p = 1 TO maxpuertas
    IF INT(SQRT(p)) = SQRT(p) THEN puertas[p] = 1
  NEXT p

  PRINT "The doors are open: ";
  FOR p = 1 TO maxpuertas
    IF puertas[p] = 1 THEN
       PRINT p; " ";
       INC cont
    END IF
  NEXT p

  PRINT CHR$(10); "Are "; STR$(cont); " open doors."

END FUNCTION
END PROGRAM
```


## Xojo

```mw
// True=Open; False=Closed
Dim doors(100) As Boolean // Booleans default to false
For j As Integer = 1 To 100
  For i As Integer = 1 to 100
    If i Mod j = 0 Then doors(i) = Not doors(i)
  Next
Next
```


## XPL0

```mw
include c:\cxpl\codes;          \intrinsic 'code' declarations
int     Door(100);              \You have 100 doors in a row
define  Open, Closed;
int     D, Pass, Step;

[for D:= 0 to 100-1 do          \that are all initially closed
        Door(D):= Closed;

Step:= 1;                       \The first time through, you visit every door
for Pass:= 1 to 100 do          \You make 100 passes by the doors
        [D:= Step-1;
        repeat  \if the door is closed, you open it; if it is open, you close it
                if Door(D)=Closed then Door(D):= Open else Door(D):= Closed;
                D:= D+Step;
        until   D>=100;
        Step:= Step+1;          \The second time you only visit every 2nd door
        ];                      \The third time, every 3rd door
                                \until you only visit the 100th door
\What state are the doors in after the last pass?
Text(0, "Open: ");              \Which are open?
for D:= 0 to 100-1 do 
        if Door(D)=Open then [IntOut(0, D+1); ChOut(0,^ )];
CrLf(0);

Text(0, "Closed: ");            \Which are closed?
for D:= 0 to 100-1 do 
        if Door(D)=Closed then [IntOut(0, D+1); ChOut(0,^ )];
CrLf(0);

\Optimized: The only doors that remain open are those that are perfect squares
Text(0, "Open: ");
D:= 1;
repeat  IntOut(0, D*D); ChOut(0,^ );
        D:= D+1;
until   D*D>100;
CrLf(0);
]
```


## XSLT 1.0

With input document ...

```mw
<hallway>
  <door number="1">closed</door>
  <door number="2">closed</door>
  <door number="3">closed</door>
  <door number="4">closed</door>
  ... etc ...
  <door number="100">closed</door>
<hallway>
```

... visually representing the initial state of the hallway, apply the following XSLT 1.0 style-sheet...

```mw
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:exsl="http://exslt.org/common"
  exclude-result-prefixes="xsl exsl">
<xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>

<xsl:template match="/*">
  <xsl:copy>
    <xsl:apply-templates select="door" />
  </xsl:copy>
</xsl:template>
      
<xsl:template match="door">
  <xsl:variable name="door-num" select="@number" />
  <xsl:variable name="knocks">
    <xsl:for-each select="/*/door">
      <xsl:if test="$door-num mod position() = 0">
        <xsl:text>!</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:variable>
  <door number="{$door-num}">
   <xsl:choose>
     <xsl:when test="string-length($knocks) mod 2 = 1">
        <xsl:text>open</xsl:text>
     </xsl:when>
     <xsl:otherwise>
        <xsl:text>closed</xsl:text>
     </xsl:otherwise>
   </xsl:choose> 
  </door>
</xsl:template>
      
</xsl:stylesheet>
```

Also see: 100 doors/XSLT


## XSLT 2.0

This XSLT 2.0 style-sheet does not use the input document.

```mw
<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>

<xsl:template match="/">
  <hallway>
    <xsl:for-each select="1 to 100">
      <xsl:variable name="door-num" select="position()" />
      <door number="{$door-num}">
        <xsl:value-of select="('closed','open')[
	    number( sum( for $pass in 1 to 100 return
	    number(($door-num mod $pass) = 0)) mod 2 = 1) + 1]" />
      </door>
    </xsl:for-each>
  </hallway>
</xsl:template>
      
</xsl:stylesheet>
```


## Yabasic

```mw
n = 100	// doors
ppa = 1	// next open door
p2 = 1

for i = 1 to n
	print "Door ", i, " is ";
	if i < p2 then
		print "closed."
	else
		ppa = ppa + 1
		p2 = ppa^2
		print "OPEN."
	end if
next
```

Optimized

```mw
for i = 1 to sqrt(100) : print "Door ", i**2, " is open" : next
```


## YAMLScript

```mw
!ys-0

defn main():
  open =:
    reduce _ ([true] * 100) (1 .. 100):
      fn(doors i):
        loop j i, doors doors:
          if j < 100:
            recur (j + i).++:
              update-in doors [j]: \(doors.$j.!)
            else: doors
  say: +"Open doors after 100 passes:\ " +
        (1 .. 100)
          .map(\(_.--:open && _))
          .filter(a)
          .join(', ')
```

**Output:**

```
$ ys 100-doors.ys
Open doors after 100 passes: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```


## Yorick

**Unoptimized, iterative**

```mw
doors = array(0, 100);
for(i = 1; i <= 100; i++)
    for(j = i; j <= 100; j += i)
        doors(j) ~= 1;
print, where(doors);
```

**Unoptimized, vectorized**

```mw
doors = array(0, 100);
for(i = 1; i <= 100; i++)
    doors(i::i) ~= 1;
print, where(doors);
```

**Optimized**

```mw
print, indgen(1:long(sqrt(100)))^2
```

All of the above output:

```
[1,4,9,16,25,36,49,64,81,100]
```


## Zen C

Translation of

:

Wren

### Unoptimized

```mw
fn main() {
    let doors: [bool; 100];
    for i in 0..100 { doors[i] = true; }
    for i in 1..=100 {
        let j = i;
        while j < 100 {
            doors[j] = !doors[j];
            j += i + 1;
        }
    }
    for i in 0..100 {
        if doors[i] { print "{i + 1} "; }
    }
    println "";
}
```

### Optimized

```mw
fn main() {
    let door = 1;
    let inc = 3;
    while door <= 100 {
        print "{door} ";
        door += inc;
        inc += 2;
    }
    println "";
}
```

**Output:**

For both versions:

```
1 4 9 16 25 36 49 64 81 100 
```


## Zig

Note: stdout is used for output, not debug.print (which is simpler, but not practical).

### Unoptimized

```mw
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    var stdout_writer = std.Io.File.stdout().writer(init.io, &.{});
    const stdout = &stdout_writer.interface;

    var doors = [_]bool{false} ** 101;
    var pass: u8 = 1;
    var door: u8 = undefined;

    while (pass <= 100) : (pass += 1) {
        door = pass;
        while (door <= 100) : (door += pass)
            doors[door] = !doors[door];
    }

    for (doors, 0..) |open, num|
        if (open)
            try stdout.print("Door {d} is open.\n", .{num});
}
```

### Optimized

```mw
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    var stdout_writer = std.Io.File.stdout().writer(init.io, &.{});
    const stdout = &stdout_writer.interface;

    var square: u8 = 1;
    var increment: u8 = 3;
    var door: u8 = 1;
    while (door <= 100) : (door += 1) {
        if (door == square) {
            try stdout.print("Door {d} is open\n", .{door});
            square += increment;
            increment += 2;
        }
    }
}
```

### Optimized with new for-loop (since Zig 0.11)

```mw
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    var stdout_writer = std.Io.File.stdout().writer(init.io, &.{});
    const stdout = &stdout_writer.interface;

    var square: u8 = 1;
    var increment: u8 = 3;
    for (1..101) |door| {
        if (door == square) {
            try stdout.print("Door {d} is open\n", .{door});
            square += increment;
            increment += 2;
        }
    }
}
```

### Really Optimized

```mw
const std = @import("std");

pub fn main(init: std.process.Init) !void {
    var stdout_writer = std.Io.File.stdout().writer(init.io, &.{});
    const stdout = &stdout_writer.interface;

    for (1..11) |door| {
        try stdout.print("Door {d} is open\n", .{door * door});
    }
}
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


## zkl

Pure brute force.

```mw
doors:=List.createLong(100,False);	// list of 100 Falses
foreach n,m in (100,[n..99,n+1]){ doors[m]=(not doors[m]); } //foreach{ foreach{} }
doors.filterNs().apply('+(1)).println();
```

The filterNs method returns the index of each item that passes the filter.

**Output:**

```
L(1,4,9,16,25,36,49,64,81,100)
```


## ZX Spectrum Basic

simple calculation

```
 10 REM 100 doors open/closed?
 20 DIM d(100)
 25 LET o=0
 30 FOR a=1 TO 100
 40 FOR b=a TO 100 STEP a
 50 LET d(b)=NOT d(b)
 55 LET o=o+(d(b)=1)-(d(b)=0)
 60 NEXT b
 70 NEXT a
 80 PRINT o;" open doors"
```

changing viewable grid

```
 10 REM 100 doors open/closed?
 20 DIM d(100)
 25 GO SUB 170
 30 FOR a=1 TO 100
 35 PRINT AT 0,0;"step ";a
 40 FOR b=a TO 100 STEP a
 45 PRINT AT 0,10;"door:";b;"  "
 50 LET d(b)=NOT d(b)
 55 GO SUB 150
 60 NEXT b
 70 NEXT a
 80 GO SUB 170
 90 STOP 
150 REM print door status
151 LET p=(b-1)/10
152 LET q=1+10*(p-INT p)
153 LET p=INT p
154 LET op=op+(d(b)=1)-(d(b)=0)
156 PRINT AT 2*p+2,2*q;d(b);AT 0,27;op;"  "
160 RETURN 
165 REM print step status
170 LET op=0
175 FOR p=0 TO 9
180 FOR q=1 TO 10
185 PRINT AT 2*p+2,2*q;d(p*10+q)
188 LET op=op+d(p*10+q)
190 NEXT q
200 NEXT p
205 PRINT AT 0,22;"open:";op;"  "
210 RETURN
```

Retrieved from "

https://rosettacode.org/wiki/100_doors?oldid=404414

"
