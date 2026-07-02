---
title: "99 bottles of beer (part 3/5)"
source: https://rosettacode.org/wiki/99_Bottles_of_Beer
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/5
---

## Cowgol

```mw
include "cowgol.coh";

sub Bottles(n: uint8) is
    if n == 0 then
        print("No more");
    else
        print_i8(n);
    end if;

    print(" bottle");
    if n != 1 then
        print("s");
    end if;
end sub;

sub Verse(n: uint8) is
    Bottles(n);
    print(" of beer on the wall,\n");
    Bottles(n);
    print(" of beer,\n");
    print("Take ");
    if n == 1 then
        print("it");
    else
        print("one");
    end if;
    print(" down and pass it around,\n");
    Bottles(n-1);
    print(" of beer on the wall.\n\n");
end sub;

var verse: uint8 := 99;
while verse > 0 loop
    Verse(verse);
    verse := verse - 1;
end loop;
```

**Output:**

```
99 bottles of beer on the wall,
99 bottles of beer,
Take one down and pass it around,
98 bottles of beer on the wall.

98 bottles of beer on the wall,
98 bottles of beer,
Take one down and pass it around,
97 bottles of beer on the wall.

97 bottles of beer on the wall,
97 bottles of beer,
Take one down and pass it around,
96 bottles of beer on the wall.

96 bottles of beer on the wall,
96 bottles of beer,
Take one down and pass it around,
95 bottles of beer on the wall.

95 bottles of beer on the wall,
95 bottles of beer,
Take one down and pass it around,
94 bottles of beer on the wall.

94 bottles of beer on the wall,
94 bottles of beer,
Take one down and pass it around,
93 bottles of beer on the wall.

93 bottles of beer on the wall,
93 bottles of beer,
Take one down and pass it around,
92 bottles of beer on the wall.

92 bottles of beer on the wall,
92 bottles of beer,
Take one down and pass it around,
91 bottles of beer on the wall.

91 bottles of beer on the wall,
91 bottles of beer,
Take one down and pass it around,
90 bottles of beer on the wall.

90 bottles of beer on the wall,
90 bottles of beer,
Take one down and pass it around,
89 bottles of beer on the wall.

89 bottles of beer on the wall,
89 bottles of beer,
Take one down and pass it around,
88 bottles of beer on the wall.

88 bottles of beer on the wall,
88 bottles of beer,
Take one down and pass it around,
87 bottles of beer on the wall.

87 bottles of beer on the wall,
87 bottles of beer,
Take one down and pass it around,
86 bottles of beer on the wall.

86 bottles of beer on the wall,
86 bottles of beer,
Take one down and pass it around,
85 bottles of beer on the wall.

85 bottles of beer on the wall,
85 bottles of beer,
Take one down and pass it around,
84 bottles of beer on the wall.

84 bottles of beer on the wall,
84 bottles of beer,
Take one down and pass it around,
83 bottles of beer on the wall.

83 bottles of beer on the wall,
83 bottles of beer,
Take one down and pass it around,
82 bottles of beer on the wall.

82 bottles of beer on the wall,
82 bottles of beer,
Take one down and pass it around,
81 bottles of beer on the wall.

81 bottles of beer on the wall,
81 bottles of beer,
Take one down and pass it around,
80 bottles of beer on the wall.

80 bottles of beer on the wall,
80 bottles of beer,
Take one down and pass it around,
79 bottles of beer on the wall.

79 bottles of beer on the wall,
79 bottles of beer,
Take one down and pass it around,
78 bottles of beer on the wall.

78 bottles of beer on the wall,
78 bottles of beer,
Take one down and pass it around,
77 bottles of beer on the wall.

77 bottles of beer on the wall,
77 bottles of beer,
Take one down and pass it around,
76 bottles of beer on the wall.

76 bottles of beer on the wall,
76 bottles of beer,
Take one down and pass it around,
75 bottles of beer on the wall.

75 bottles of beer on the wall,
75 bottles of beer,
Take one down and pass it around,
74 bottles of beer on the wall.

74 bottles of beer on the wall,
74 bottles of beer,
Take one down and pass it around,
73 bottles of beer on the wall.

73 bottles of beer on the wall,
73 bottles of beer,
Take one down and pass it around,
72 bottles of beer on the wall.

72 bottles of beer on the wall,
72 bottles of beer,
Take one down and pass it around,
71 bottles of beer on the wall.

71 bottles of beer on the wall,
71 bottles of beer,
Take one down and pass it around,
70 bottles of beer on the wall.

70 bottles of beer on the wall,
70 bottles of beer,
Take one down and pass it around,
69 bottles of beer on the wall.

69 bottles of beer on the wall,
69 bottles of beer,
Take one down and pass it around,
68 bottles of beer on the wall.

68 bottles of beer on the wall,
68 bottles of beer,
Take one down and pass it around,
67 bottles of beer on the wall.

67 bottles of beer on the wall,
67 bottles of beer,
Take one down and pass it around,
66 bottles of beer on the wall.

66 bottles of beer on the wall,
66 bottles of beer,
Take one down and pass it around,
65 bottles of beer on the wall.

65 bottles of beer on the wall,
65 bottles of beer,
Take one down and pass it around,
64 bottles of beer on the wall.

64 bottles of beer on the wall,
64 bottles of beer,
Take one down and pass it around,
63 bottles of beer on the wall.

63 bottles of beer on the wall,
63 bottles of beer,
Take one down and pass it around,
62 bottles of beer on the wall.

62 bottles of beer on the wall,
62 bottles of beer,
Take one down and pass it around,
61 bottles of beer on the wall.

61 bottles of beer on the wall,
61 bottles of beer,
Take one down and pass it around,
60 bottles of beer on the wall.

60 bottles of beer on the wall,
60 bottles of beer,
Take one down and pass it around,
59 bottles of beer on the wall.

59 bottles of beer on the wall,
59 bottles of beer,
Take one down and pass it around,
58 bottles of beer on the wall.

58 bottles of beer on the wall,
58 bottles of beer,
Take one down and pass it around,
57 bottles of beer on the wall.

57 bottles of beer on the wall,
57 bottles of beer,
Take one down and pass it around,
56 bottles of beer on the wall.

56 bottles of beer on the wall,
56 bottles of beer,
Take one down and pass it around,
55 bottles of beer on the wall.

55 bottles of beer on the wall,
55 bottles of beer,
Take one down and pass it around,
54 bottles of beer on the wall.

54 bottles of beer on the wall,
54 bottles of beer,
Take one down and pass it around,
53 bottles of beer on the wall.

53 bottles of beer on the wall,
53 bottles of beer,
Take one down and pass it around,
52 bottles of beer on the wall.

52 bottles of beer on the wall,
52 bottles of beer,
Take one down and pass it around,
51 bottles of beer on the wall.

51 bottles of beer on the wall,
51 bottles of beer,
Take one down and pass it around,
50 bottles of beer on the wall.

50 bottles of beer on the wall,
50 bottles of beer,
Take one down and pass it around,
49 bottles of beer on the wall.

49 bottles of beer on the wall,
49 bottles of beer,
Take one down and pass it around,
48 bottles of beer on the wall.

48 bottles of beer on the wall,
48 bottles of beer,
Take one down and pass it around,
47 bottles of beer on the wall.

47 bottles of beer on the wall,
47 bottles of beer,
Take one down and pass it around,
46 bottles of beer on the wall.

46 bottles of beer on the wall,
46 bottles of beer,
Take one down and pass it around,
45 bottles of beer on the wall.

45 bottles of beer on the wall,
45 bottles of beer,
Take one down and pass it around,
44 bottles of beer on the wall.

44 bottles of beer on the wall,
44 bottles of beer,
Take one down and pass it around,
43 bottles of beer on the wall.

43 bottles of beer on the wall,
43 bottles of beer,
Take one down and pass it around,
42 bottles of beer on the wall.

42 bottles of beer on the wall,
42 bottles of beer,
Take one down and pass it around,
41 bottles of beer on the wall.

41 bottles of beer on the wall,
41 bottles of beer,
Take one down and pass it around,
40 bottles of beer on the wall.

40 bottles of beer on the wall,
40 bottles of beer,
Take one down and pass it around,
39 bottles of beer on the wall.

39 bottles of beer on the wall,
39 bottles of beer,
Take one down and pass it around,
38 bottles of beer on the wall.

38 bottles of beer on the wall,
38 bottles of beer,
Take one down and pass it around,
37 bottles of beer on the wall.

37 bottles of beer on the wall,
37 bottles of beer,
Take one down and pass it around,
36 bottles of beer on the wall.

36 bottles of beer on the wall,
36 bottles of beer,
Take one down and pass it around,
35 bottles of beer on the wall.

35 bottles of beer on the wall,
35 bottles of beer,
Take one down and pass it around,
34 bottles of beer on the wall.

34 bottles of beer on the wall,
34 bottles of beer,
Take one down and pass it around,
33 bottles of beer on the wall.

33 bottles of beer on the wall,
33 bottles of beer,
Take one down and pass it around,
32 bottles of beer on the wall.

32 bottles of beer on the wall,
32 bottles of beer,
Take one down and pass it around,
31 bottles of beer on the wall.

31 bottles of beer on the wall,
31 bottles of beer,
Take one down and pass it around,
30 bottles of beer on the wall.

30 bottles of beer on the wall,
30 bottles of beer,
Take one down and pass it around,
29 bottles of beer on the wall.

29 bottles of beer on the wall,
29 bottles of beer,
Take one down and pass it around,
28 bottles of beer on the wall.

28 bottles of beer on the wall,
28 bottles of beer,
Take one down and pass it around,
27 bottles of beer on the wall.

27 bottles of beer on the wall,
27 bottles of beer,
Take one down and pass it around,
26 bottles of beer on the wall.

26 bottles of beer on the wall,
26 bottles of beer,
Take one down and pass it around,
25 bottles of beer on the wall.

25 bottles of beer on the wall,
25 bottles of beer,
Take one down and pass it around,
24 bottles of beer on the wall.

24 bottles of beer on the wall,
24 bottles of beer,
Take one down and pass it around,
23 bottles of beer on the wall.

23 bottles of beer on the wall,
23 bottles of beer,
Take one down and pass it around,
22 bottles of beer on the wall.

22 bottles of beer on the wall,
22 bottles of beer,
Take one down and pass it around,
21 bottles of beer on the wall.

21 bottles of beer on the wall,
21 bottles of beer,
Take one down and pass it around,
20 bottles of beer on the wall.

20 bottles of beer on the wall,
20 bottles of beer,
Take one down and pass it around,
19 bottles of beer on the wall.

19 bottles of beer on the wall,
19 bottles of beer,
Take one down and pass it around,
18 bottles of beer on the wall.

18 bottles of beer on the wall,
18 bottles of beer,
Take one down and pass it around,
17 bottles of beer on the wall.

17 bottles of beer on the wall,
17 bottles of beer,
Take one down and pass it around,
16 bottles of beer on the wall.

16 bottles of beer on the wall,
16 bottles of beer,
Take one down and pass it around,
15 bottles of beer on the wall.

15 bottles of beer on the wall,
15 bottles of beer,
Take one down and pass it around,
14 bottles of beer on the wall.

14 bottles of beer on the wall,
14 bottles of beer,
Take one down and pass it around,
13 bottles of beer on the wall.

13 bottles of beer on the wall,
13 bottles of beer,
Take one down and pass it around,
12 bottles of beer on the wall.

12 bottles of beer on the wall,
12 bottles of beer,
Take one down and pass it around,
11 bottles of beer on the wall.

11 bottles of beer on the wall,
11 bottles of beer,
Take one down and pass it around,
10 bottles of beer on the wall.

10 bottles of beer on the wall,
10 bottles of beer,
Take one down and pass it around,
9 bottles of beer on the wall.

9 bottles of beer on the wall,
9 bottles of beer,
Take one down and pass it around,
8 bottles of beer on the wall.

8 bottles of beer on the wall,
8 bottles of beer,
Take one down and pass it around,
7 bottles of beer on the wall.

7 bottles of beer on the wall,
7 bottles of beer,
Take one down and pass it around,
6 bottles of beer on the wall.

6 bottles of beer on the wall,
6 bottles of beer,
Take one down and pass it around,
5 bottles of beer on the wall.

5 bottles of beer on the wall,
5 bottles of beer,
Take one down and pass it around,
4 bottles of beer on the wall.

4 bottles of beer on the wall,
4 bottles of beer,
Take one down and pass it around,
3 bottles of beer on the wall.

3 bottles of beer on the wall,
3 bottles of beer,
Take one down and pass it around,
2 bottles of beer on the wall.

2 bottles of beer on the wall,
2 bottles of beer,
Take one down and pass it around,
1 bottle of beer on the wall.

1 bottle of beer on the wall,
1 bottle of beer,
Take it down and pass it around,
No more bottles of beer on the wall.
```


## Crystal

```mw
99.downto(1) do |n|                                                             
  puts "#{n} bottle#{n > 1 ? "s" : ""} of beer on the wall"                     
  puts "#{n} bottle#{n > 1 ? "s" : ""} of beer"                                 
  puts "Take one down, pass it around"                                          
  puts "#{n-1} bottle#{n > 2 ? "s" : ""} of beer on the wall\n\n" if n > 1      
end                                                                             
puts "No more bottles of beer on the wall"
```


## D

### Simple Solution

Works with

:

D

version 2

Based on Steward Gordon's code at: 99-bottles-of-beer.net.

```mw
import std.stdio;

void main() {
    int bottles = 99;

    while (bottles > 1) {
        writeln(bottles, " bottles of beer on the wall,");
        writeln(bottles, " bottles of beer.");
        writeln("Take one down, pass it around,");
        if (--bottles > 1) {
            writeln(bottles, " bottles of beer on the wall.\n");
        }        
    }
    writeln("1 bottle of beer on the wall.\n");

    writeln("No more bottles of beer on the wall,");
    writeln("no more bottles of beer.");
    writeln("Go to the store and buy some more,");
    writeln("99 bottles of beer on the wall."); 
}
```

### CTFE Solution

CTFE (Compile-Time Function Execution) is a feature of D that allows for pure functions of arbitrary complexity to be completely evaluated at compile time when every parameter is known. Note that this is distinct from the template meta-programming tricks used by some other languages, and this bottles() function could just as easily be executed during run-time. The compiled result of this program simply prints the pre-generated lyrics to the song, using a standard compiler pragma directive.

```mw
import std.stdio, std.conv;

string bottles(in size_t num) pure {
    static string bottlesRecurse(in size_t num) pure {
        return num.text ~ " bottles of beer on the wall,\n"
               ~ num.text ~ " bottles of beer!\n"
               ~ "Take one down, pass it around,\n"
               ~ (num - 1).text ~ " bottle" ~ ((num - 1 == 1) ? "" : "s")
               ~ " of beer on the wall.\n\n"
               ~ ((num > 2)
                  ? bottlesRecurse(num - 1)
                  : "1 bottle of beer on the wall,\n"
                  ~ "1 bottle of beer!\n"
                  ~ "Take one down, pass it around,\n"
                  ~ "No bottles of beer on the wall!\n\n");
    }

    return bottlesRecurse(num)
           ~ "Go to the store and buy some more...\n"
           ~ num.text ~ " bottles of beer on the wall!";
}

pragma(msg, 99.bottles);
void main() {}
```

### Template Meta-Programming Solution

Uses D template meta-programming and recursion to pre-generate the song lyrics and prints it at compile via pragma(msg,...)

```mw
module bottles;

template BeerSong(int Bottles)
{
	static if (Bottles == 1)
	{
		enum BeerSong = "1 bottle of beer on the wall\n" ~ 
		"1 bottle of beer\ntake it down, pass it around\n" ~ "
		no more bottles of beer on the wall\n";
	}
	else
	{
		enum BeerSong = Bottles.stringof ~ " bottles of beer on the wall\n" ~ 
		Bottles.stringof ~ " bottles of beer\ntake it down, pass it around\n" ~ 
		BeerSong!(Bottles-1);
	}
}

pragma(msg,BeerSong!99);

void main(){}
```


## Dart

```
String btl(int n) {
  return n==1?"bottle":"bottles";
}
main() {
  for (int i = 99; i >= 1; i--) {
    print("$i ${btl(i)} of beer on the wall");
    print("$i ${btl(i)} of beer");
    print("Take one down, pass it around");
    print("${i-1} ${btl(i-1)} of beer on the wall\n");
  }
}
```

### Making use of polymorphism

```mw
main() {
  BeerSong beerSong = BeerSong();
  //pass a 'starting point' and 'end point' as parameters respectively
  String printTheLyrics = beerSong.recite(99, 1).join('\n');
  print(printTheLyrics);
  }

class Song {
  String bottleOnTheWall(int index) {
    String bottleOnTheWallText =
        '$index bottles of beer on the wall, $index bottles of beer,';
    return bottleOnTheWallText;
  }

  String bottleTakenDown(int index) {
    String englishGrammar = (index >= 2) ? 'bottle' : 'bottles';
    String bottleTakenDownText =
        'Take one down and pass it around, ${index - 1} $englishGrammar of beer on the wall.';
    return bottleTakenDownText;
  }
}

class BeerSong extends Song {
  @override
  String bottleOnTheWall(int index) {
    String originalText = super.bottleOnTheWall(index);
    if (index < 2) {
      String bottleOnTheWallText =
          '$index bottle of beer on the wall, $index bottle of beer,';
      return bottleOnTheWallText;
    }
    return originalText;
  }

  @override
  String bottleTakenDown(int index) {
    if (index < 2) {
      String bottleTakenDownText =
          'Take it down and pass it around, no more bottles of beer on the wall.';
      return bottleTakenDownText;
    }
    String originalText = super.bottleTakenDown(index);
    return originalText;
  }

  List<String> recite(int actualBottleOnTheWall, int remainingBottleOnTheWall) {
    List<String> theLyrics = [];
    for (int index = actualBottleOnTheWall;
        index >= remainingBottleOnTheWall;
        index--) {
      String onTheWall = bottleOnTheWall(index);
      String takenDown = bottleTakenDown(index);
      theLyrics.add(onTheWall);
      theLyrics.add(takenDown);
      theLyrics.add('');
    }
    return theLyrics;
  }
}
```


## Dc

Works with

:

GNU dc

Works with

:

OpenBSD dc

```mw
[
  dnrpr
  dnlBP
  lCP
  1-dnrp
  rd2r >L
]sL

[Take one down, pass it around
]sC
[ bottles of beer
]sB
[ bottles of beer on the wall]
99

lLx

dnrpsA
dnlBP
lCP
1-
dn[ bottle of beer on the wall]p
rdnrpsA
n[ bottle of beer
]P
[Take it down, pass it around
]P
[no more bottles of beer on the wall
]P
```

Similar to the program above, but without 'n' and 'r' commands. It prints the numbers on separate lines than the strings.

Works with

:

AT&T dc

```mw
[
  plAP
  plBP
  lCP
  1-dplAP
  d2r >L
]sL

[Take one down, pass it around
]sC
[bottles of beer
]sB
[bottles of beer on the wall
]sA
99

lLx

plAP
plBP
lCP
1-
p
[bottle of beer on the wall
]P
p
[bottle of beer
]P
[Take it down, pass it around
]P
[no more bottles of beer on the wall
]P
```


## DBL

```mw
;
;===============================================================================
;       Oringinal Author: Bob Welton (welton@pui.com)
;       Language: DIBOL or DBL
;
;       Modified to work with DBL version 4
;       by Dario B.
;===============================================================================
 

        RECORD

NRBOT,D2,99                  ;Default # of bottles to 99
A2,     A2
 
 
                                PROC
;-------------------------------------------------------------------------------

        XCALL FLAGS (0007000000,1)      ;Suppress STOP message
        OPEN (1,O,"TT:")                ;Open the terminal/display

        DO FOREVER
           BEGIN
                A2=NRBOT,'ZX'
                DISPLAY (1,A2," Bottles of Beer on the wall,",10)

                A2=NRBOT,'ZX'
                DISPLAY (1,A2," Bottles of Beer,",10)
                DISPLAY (1,"   Take one down, pass it around,",10)
        
                DECR NRBOT                      ;Reduce # of bottles by 1
                IF (NRBOT.LE.1) EXITLOOP        ;If just 1 bottle left, get out

                A2=NRBOT,'ZX'
                DISPLAY (1,A2," Bottles of Beer on the wall.",10,10)
           END

        A2=NRBOT,'ZX'
        DISPLAY (1,A2," Bottle of Beer on the wall,",10,10)

        A2=NRBOT,'ZX'
        DISPLAY (1,A2," Bottle of Beer,",10)

        DISPLAY (1,"   Take one down, pass it around,",10)
        DISPLAY (1,"0 Bottles of Beer on the wall,",10)
        DISPLAY (1,"0 Bottles of Beer,",10)
        DISPLAY (1,"Go to the store and buy some more,",10)
        DISPLAY (1,"99 Bottles of Beer on the wall,",10,10,10)
        CLOSE 1
        STOP
```


## Delphi

See 99 Bottles of Beer/Pascal


## DM

Uses the [] variable insertion into strings, see [1]

```
   /client/New()
       ..()
       var/bottlestring
       for(var/i in 99 to 0)
           bottlestring = "[i || "No more"] Bottle[i != 1 ? "s" : ""] of Beer"
           src << "[bottlestring] on the wall,"
           src << "[bottlestring],"
           src << "Take [i == 1 ? "it" : "one"] down, pass it around,"
           src << "[bottlestring] on the wall,"
```


## Draco

```mw
proc nonrec bottles(byte b) void:
    if b=0 then write("No more") else write(b) fi;
    write(" bottle");
    if b~=1 then write("s") fi
corp;

proc nonrec verse(byte v) void:
    bottles(v);
    writeln(" of beer on the wall,");
    bottles(v);
    writeln(" of beer,");
    writeln("Take ",
        if v=1 then "it" else "one" fi,
        " down and pass it around");
    bottles(v-1);
    writeln(" of beer on the wall!\n");
corp;

proc nonrec main() void:
    byte v;
    for v from 99 downto 1 do verse(v) od
corp
```


## DuckDB

Works with

:

DuckDB

version V1.0

The following functional and recursive CTE solutions produce the same output.

### list_transform()

```mw
.header off
.mode list
select list_transform( range(99,-1,-1),
  n ->
    if (n = 0,
       'No more bottles of beer on the wall'   || chr(10)
          || 'no more bottles of beer.'        || chr(10)
          || 'Go to the store, buy some more!' || chr(10)
          || '99 bottles of beer on the wall.',
        n || ' bottle' || if ( n = 1, '', 's') || ' of beer on the wall'   || chr(10)
          || n || ' bottle' || if ( n = 1, '', 's') || ' of beer;'         || chr(10)
          || 'Take one down, pass it around'                               || chr(10) ) )
  .array_to_string(chr(10)) ;
```

### Recursive CTE

```mw
.header off
.mode list

with recursive cte as (
  select 99 as n, '' as s
  union all
  select n-1 as n,
    if (n = 0,
       'No more bottles of beer on the wall'   || chr(10)
          || 'no more bottles of beer.'        || chr(10)
          || 'Go to the store, buy some more!' || chr(10)
          || '99 bottles of beer on the wall.',
        n || ' bottle' || if ( n = 1, '', 's') || ' of beer on the wall'   || chr(10)
          || n || ' bottle' || if ( n = 1, '', 's') || ' of beer;'         || chr(10)
          || 'Take one down, pass it around'                               || chr(10) )
   from cte
   where n > -1
 ) select s
   from cte
   where s != ''
   order by n desc ;
```

**Output:**

```
99 bottles of beer on the wall
99 bottles of beer;
Take one down, pass it around

98 bottles of beer on the wall
98 bottles of beer;
Take one down, pass it around

...

2 bottles of beer on the wall
2 bottles of beer;
Take one down, pass it around

1 bottle of beer on the wall
1 bottle of beer;
Take one down, pass it around

No more bottles of beer on the wall
no more bottles of beer.
Go to the store, buy some more!
99 bottles of beer on the wall!
```


## Dyalect

Translation of

:

Swift

```mw
for i in 99^-1..1 {
    print("\(i) bottles of beer on the wall, \(i) bottles of beer.")
    let next = i is 1 ? "no" : i - 1
    print("Take one down and pass it around, \(next) bottles of beer on the wall.")
}
```


## Dylan

```mw
Module: bottles
define method bottles (n :: <integer>)
  for (n from 99 to 1 by -1)
    format-out("%d bottles of beer on the wall,\n"
               "%d bottles of beer\n"
               "Take one down, pass it around\n"
               "%d bottles of beer on the wall\n",
               n, n, n - 1);
  end
end method
```


## Déjà Vu

```mw
plural i:
	if = 1 i "" "s"

bottles i:
	local :s plural i
	!print( to-str i " bottle"s" of beer on the wall, " to-str i " bottle"s" of beer," )
	!print\ "You take one down, pass it around, "
	set :i -- i
	if i:
		set :s plural i
		!print( to-str i " bottle"s" of beer on the wall." )
		bottles i
	else:
		!print "no more bottles of beer on the wall, no more bottles of beer."
		!print "Go to the store and buy some more, 99 bottles of beer on the wall."

bottles 99
```


## DIBOL-11

```mw
;
;===============================================================================
========================
;       Oringinal Author: Bob Welton (welton@pui.com)
;       Language: DIBOL or DBL
;
;       Modified to work with DEC DIBOL-11
;       by Bill Gunshannon
;===============================================================================
========================

RECORD MISC
    NUMBOTTLES  ,D2,99                  ;Default # of bottles to 99

RECORD LINE1
    ANUMBOTTLES, A2
,   A32, " Bottles of Beer on the wall,"

RECORD LINE2
BNUMBOTTLES, A2
,    A32, " Bottles of Beer,"

RECORD LINE3
CNUMBOTTLES, A2
,    A32, " Bottles of Beer on the wall."
 
RECORD LINE4
DNUMBOTTLES, A2
,    A32, " Bottle of Beer on the wall,"

RECORD LINE5
ENUMBOTTLES, A2
,    A32, " Bottle of Beer,"

.PROC
    XCALL FLAGS (0007000000,1)          ;Suppress STOP message
    OPEN (8,O:C,"TT:")                  ;Open the terminal/display
    REPEAT
        BEGIN
        ANUMBOTTLES = NUMBOTTLES,'ZX'
        WRITES (8,LINE1)
        BNUMBOTTLES = NUMBOTTLES,'ZX'
        WRITES (8,LINE2)
        WRITES (8,"   Take one down, pass it around,")
        DECR NUMBOTTLES                 ;Reduce # of bottles by 1
        IF (NUMBOTTLES .LE. 1) EXITLOOP ;If just 1 bottle left, get out
        CNUMBOTTLES = NUMBOTTLES,'ZX'
        WRITES (8,LINE3)
        WRITES (8," ")
        END
      DNUMBOTTLES = NUMBOTTLES,'ZX'
      WRITES(8,LINE4)
      WRITES (8," ")
      ENUMBOTTLES = NUMBOTTLES,'ZX'
      WRITES(8,LINE5)
      WRITES (8,"   Take one down, pass it around,")
      WRITES(8,"0 Bottles of Beer on the wall,")
      WRITES(8,"0 Bottles of Beer,")
      WRITES(8,"Go to the store and buy some more,")
      WRITES(8,"99 Bottles of Beer on the wall,")

    WRITES (8," ")
    WRITES (8," ")
    SLEEP 2
    CLOSE 8
    STOP
.END
```


## E

```mw
def bottles(n) {
  return switch (n) {
    match ==0 { "No bottles" }
    match ==1 { "1 bottle" }
    match _   { `$n bottles` }
  }
}
for n in (1..99).descending() {
  println(`${bottles(n)} of beer on the wall,
${bottles(n)} of beer.
Take one down, pass it around,
${bottles(n.previous())} of beer on the wall.
`)
}
```


## EasyLang

```mw
func$ bottle num .
   if num = 1 : return "1 bottle"
   return num & " bottles"
.
i = 99
repeat
   print bottle i & " of beer on the wall"
   print bottle i & " of beer"
   print "Take one down, pass it around"
   i -= 1
   until i = 0
   print bottle i & " of beer on the wall"
   print ""
.
print "No more bottles of beer on the wall"
```


## ECL

```mw
Layout := RECORD
  UNSIGNED1 RecID1;
  UNSIGNED1 RecID2;
  STRING30  txt;
END;	
Beers := DATASET(99,TRANSFORM(Layout,
                              SELF.RecID1 := COUNTER,SELF.RecID2 := 0,SELF.txt := ''));

Layout XF(Layout L,INTEGER C) := TRANSFORM
  IsOneNext := L.RecID1-1 = 1;
  IsOne := L.RecID1 = 1;
  SELF.txt := CHOOSE(C,
                     (STRING)(L.RecID1-1) + ' bottle'+IF(IsOneNext,'','s')+' of beer on the wall',
                     'Take one down, pass it around',
                     (STRING)(L.RecID1) + ' bottle'+IF(IsOne,'','s')+' of beer',
                     (STRING)(L.RecID1) + ' bottle'+IF(IsOne,'','s')+' of beer on the wall','');
  SELF.RecID2 := C;
  SELF := L;
END;

Rev := NORMALIZE(Beers,5,XF(LEFT,COUNTER));
OUTPUT(SORT(Rev,-Recid1,-RecID2),{txt},ALL);
```


## Ecstasy

```mw
module Bottles {
    void run() {
        function String(Int) num     = i -> i==0 ? "No" : i.toString();
        function String(Int) bottles = i -> i==1 ? "bottle" : "bottles";

        @Inject Console console;
        for (Int remain : 99..1) {
            console.print($|{num(remain)} {bottles(remain)} of beer on the wall
                           |{num(remain)} {bottles(remain)} of beer
                           |Take one down, pass it around
                           |{num(remain-1)} {bottles(remain-1)} of beer on the wall
                           |
                         );
        }
    }
}
```


## Egel

```mw
import "prelude.eg"
import "io.ego"

using System
using IO

def print_rhyme =
    [ 0 ->
        print "better go to the store, and buy some more\n"
    | N ->
        let _ = print N " bottles of beer on the wall\n" in
        let _ = print N " bottles of beer\n" in
        let _ = print "take one down, pass it around\n" in
            print_rhyme (N - 1) ]

def main = print_rhyme 99
```


## EGL

```mw
program TestProgram type BasicProgram {}
	
    function main()
        for (count int from 99 to 1 decrement by 1)
            SysLib.writeStdout( bottleStr( count ) :: " of beer on the wall." );
            SysLib.writeStdout( bottleStr( count ) :: " of beer." );
            SysLib.writeStdout( "Take one down, pass it around." );
            SysLib.writeStdout( bottleStr( count - 1) :: " of beer on the wall.\n");
        end
    end
    
    private function bottleStr( count int in) returns( string )
        case ( count )
            when ( 1 )
                return( "1 bottle" );
            when ( 0 )
                return( "No more bottles" );
            otherwise
                return( count :: " bottles" );
        end
    end	
end
```


## Eiffel

```mw
class
	APPLICATION

create
	make

feature {NONE} -- Initialization

	make
		local
			bottles: INTEGER
		do
			from
				bottles := 99
			invariant
				bottles <= 99 and bottles >= 1
			until
				bottles = 1
			loop
				print (bottles)
				print (" bottles of beer on the wall,%N")
				print (bottles)
				print (" bottles of beer.%N")
				print ("Take one down, pass it around,%N")
				bottles := bottles - 1
				if bottles > 1 then
					print (bottles)
					print (" bottles of beer on the wall.%N%N")
				end
			variant
				bottles
			end
			print ("1 bottle of beer on the wall.%N%N");
			print ("No more bottles of beer on the wall,%N");
			print ("no more bottles of beer.%N");
			print ("Go to the store and buy some more,%N");
			print ("99 bottles of beer on the wall.%N");
		end

end
```

An alternative version written using the across-loop construct.

```mw
	output_lyrics
			-- Output the lyrics to 99-bottles-of-beer.
		local
			l_bottles: LINKED_LIST [INTEGER]
		do
			create l_bottles.make
			across (1 |..| 99) as ic loop l_bottles.force (ic.item) end
			across l_bottles.new_cursor.reversed as ic_bottles loop
				print (ic_bottles.item)
				print (" bottles of beer on the wall, ")
				print (ic_bottles.item)
				print (" bottles of beer.%N")
				print ("Take one down, pass it around, ")
				if ic_bottles.item > 1 then
					print (ic_bottles.item)
					print (" bottles of beer on the wall.%N%N")
				end
			end
			print ("1 bottle of beer on the wall.%N")
			print ("No more bottles of beer on the wall, no more bottles of beer.%N")
			print ("Go to the store and buy some more, 99 bottles of beer on the wall.%N")
		end
```


## Ela

```mw
open list
 
beer 1 = "1 bottle of beer on the wall\n1 bottle of beer\nTake one down, pass it around"
beer 0 = "better go to the store and buy some more."
beer v = show v ++ " bottles of beer on the wall\n"                 
         ++ show v                 
         ++" bottles of beer\nTake one down, pass it around\n"
 
map beer [99,98..0]
```


## Elan

```mw
INT VAR number of bottles;

PROCEDURE print how many bottles are on the wall (INT CONST number):
  print number;
  print bottle;
  print trailing text.

  print number:
    IF number = 0 THEN
      put ("No")
    ELSE
      put (number)
    END IF.

  print bottle:
    out ("Bottle");
    IF no <> 1 THEN
      out ("s")
    END IF.

  print trailing text:
    out (" of beer").
END PROCEDURE print how many bottles are on the wall;

say hello;
print song;
say goodbye.

say hello:
  putline ("99 Bottles of Beer");
  putline ("==================");
  line.

print song:
  FOR number of bottles FROM 99 DOWNTO 1 REPEAT
    print first line;
    print second line;
    print third line
  END REPEAT.

say goodbye:
  line;
  putline ("=====================");
  putline ("You need a ride home?");
  line.

print first line:
  print how many bottles are on the wall (number of bottles);
  out (" on the wall, ");
  print how many bottles are on the wall (number of bottles);
  line.

print second line:
  putline ("Take one down and pass it around,").

print third line:
  print how many bottles are on the wall (number of bottles - 1);
  putline (" on the wall");
  line.
```


## Elena

ELENA 6.x :

```mw
import system'routines;
import extensions;
import extensions'routines;
import extensions'text;

extension bottleOp
{
    bottleDescription()
        = self.toPrintable() + (self != 1).iif(" bottles"," bottle");
        
    bottleEnumerator() = new Variable(self).doWith::(n)
    {
        ^ new Enumerator
        {
            bool next() = n > 0;
            
            get Value() = new StringWriter()
                    .printLine(n.bottleDescription()," of beer on the wall")
                    .printLine(n.bottleDescription()," of beer")
                    .printLine("Take one down, pass it around")
                    .printLine((n.reduce(1)).bottleDescription()," of beer on the wall");
                    
            reset() {}
            
            enumerable() = weak self;
        }
    };
}

public Program()
{
    var bottles := 99;
    
    bottles.bottleEnumerator().forEach(PrintingLn)
}
```

**Output:**

```
5 bottles of beer on the wall
5 bottles of beer
Take one down, pass it around
4 bottles of beer on the wall

4 bottles of beer on the wall
4 bottles of beer
Take one down, pass it around
3 bottles of beer on the wall

3 bottles of beer on the wall
3 bottles of beer
Take one down, pass it around
2 bottles of beer on the wall

2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottle of beer on the wall

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
0 bottles of beer on the wall
```


## Elixir

```mw
defmodule Bottles do
  def run do
    Enum.each 99..1, fn idx ->
      IO.puts "#{idx} bottle#{plural(idx)} of beer on the wall"
      IO.puts "#{idx} bottle#{plural(idx)} of beer"
      IO.puts "Take one down, pass it around"
      IO.puts "#{idx - 1} bottle#{plural(idx-1)} of beer on the wall"
      IO.puts ""
    end
  end

  def plural(1), do: ""
  def plural(num), do: "s"
end

Bottles.run
```

An alternative that concatenates two enumerables to avoid pluralising/singularising again and again:

```mw
last = [
  """
  2 bottles of beer on the wall
  2 bottles of beer
  Take one down, pass it around
  1 bottle of beer on the wall
  """,
  """
  1 bottle of beer on the wall
  1 bottle of beer
  Take one down, pass it around
  No bottles of beer on the wall
  """,
  """
  No more bottles of beer on the wall
  No more bottles of beer 
  Go to the store and buy some more
  99 bottles of beer on the wall
  """
]

skeleton = fn n ->
  """
  #{n} bottles of beer on the wall
  #{n} bottles of beer
  Take one down, pass it around
  #{n - 1} bottles of beer on the wall
  """
end

99..3
|> Stream.map(skeleton)
|> Stream.concat(last)
|> Enum.intersperse("\n")
|> IO.iodata_to_binary()
|> IO.puts()
```


## Elm

```mw
module Main exposing (main)

import Html

main =
    List.range 1 100
        |> List.reverse
        |> List.map
            (\n ->
                let
                    nString =
                        String.fromInt n

                    n1String =
                        String.fromInt (n - 1)
                in
                [ nString ++ " bottles of beer on the wall"
                , nString ++ " bottles of beer"
                , "Take one down, pass it around"
                , n1String ++ " bottles of beer on the wall"
                ]
                    |> List.map Html.text
                    |> List.intersperse (Html.br [] [])
                    |> Html.p []
            )
        |> Html.div []
```


## Emacs Lisp

```mw
(let ((i 99))
  (while (> i 0)
    (message "%d bottles of beer on the wall" i)
    (message "%d bottles of beer" i)
    (message "Take one down, pass it around")
    (message "%d bottles of beer on the wall" (1- i))
    (setq i (1- i))))
```


## EMal

This version writes the lyrics as described here: https://99-bottles-of-beer.net/lyrics.html

```mw
type NinetynineBottles
int DEFAULT_BOTTLES_COUNT ← 99
model
  int initialBottlesCount, bottlesCount
  new by int ←bottlesCount
    me.initialBottlesCount ← bottlesCount
  end
  fun subject ← <|when(me.bottlesCount æ 1, "bottle", "bottles")
  fun bottles ← <|when(me.bottlesCount æ 0, "no more", text!me.bottlesCount)
  fun goToWall ← void by block
    text line ← me.bottles() + " " + me.subject() + " of beer on the wall, " + 
      me.bottles() + " " + me.subject() + " of beer."
	if me.bottlesCount æ 0 do line[0] ← line[0].upper() end # text can be modified
    writeLine(line)
  end
  fun takeOne ← logic by block
    if --me.bottlesCount < 0 do return false end # cannot take a beer down
    writeLine("Take one down and pass it around, " + me.bottles() + 
      " " + me.subject() + " of beer on the wall.")
    writeLine()
    return true
  end
  fun goToStore ← <|writeLine("Go to the store and buy some more, " + 
    me.initialBottlesCount + " bottles of beer on the wall.")
  fun play ← void by block
    for ever
      me.goToWall()
      if not me.takeOne()
        me.goToStore()
        break
      end
    end 
  end
end
NinetynineBottles(when(Runtime.args.length > 0, int!Runtime.args[0], DEFAULT_BOTTLES_COUNT)).play()
```

The output for two bottles of beer is as follows.

**Output:**

```
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 2 bottles of beer on the wall.
```


## Erlang

```mw
-module(beersong).
-export([sing/0]).
-define(TEMPLATE_0, "~s of beer on the wall, ~s of beer.~nGo to the store and buy some more, 99
bottles of beer on the wall.~n").
-define(TEMPLATE_N, "~s of beer on the wall, ~s of beer.~nTake one down and pass it around, ~s of
beer on the wall.~n~n").

create_verse(0)      -> {0, io_lib:format(?TEMPLATE_0, phrase(0))};
create_verse(Bottle) -> {Bottle, io_lib:format(?TEMPLATE_N, phrase(Bottle))}.

phrase(0)      -> ["No more bottles", "no more bottles"];
phrase(1)      -> ["1 bottle", "1 bottle", "no more bottles"];
phrase(2)      -> ["2 bottles", "2 bottles", "1 bottle"];
phrase(Bottle) -> lists:duplicate(2, integer_to_list(Bottle) ++ " bottles") ++
[integer_to_list(Bottle-1) ++ " bottles"].

bottles() -> lists:reverse(lists:seq(0,99)).

sing() ->
    lists:foreach(fun spawn_singer/1, bottles()),
    sing_verse(99).

spawn_singer(Bottle) ->
    Pid = self(), 
    spawn(fun() -> Pid ! create_verse(Bottle) end).

sing_verse(Bottle) ->
    receive
        {_, Verse} when Bottle == 0 ->
            io:format(Verse);
        {N, Verse} when Bottle == N ->
            io:format(Verse),
            sing_verse(Bottle-1)
    after 
        3000 ->
            io:format("Verse not received - re-starting singer~n"),
            spawn_singer(Bottle),
            sing_verse(Bottle)
    end.
```


## Euphoria

Works with

:

Euphoria

version 4.0.0

```mw
constant
   bottles = "bottles",
   bottle = "bottle"

procedure beers (integer how_much)
   sequence word1 = bottles, word2 = bottles
   switch how_much do
   case 2 then
      word2 = bottle
   case 1 then
      word1 = bottle
      word2 = bottle
   end switch

   printf (1,
      "%d %s of beer on the wall \n" &
      "%d %s of beer \n" &
      "Take one down, and pass it around \n" &
      "%d %s of beer on the wall \n\n",
      { how_much, word1,
        how_much, word1,
        how_much-1, word2 }
   )
end procedure

for a = 99 to 1 by -1 do
   beers (a)
end for
```

```mw
-- An alternate version

include std/console.e

sequence howmany = {"No more bottles","%d bottle","","s"}

for beer = 99 to 1 by -1 do
   display(`
   [1] bottles of beer on the wall,
   [1] bottles of beer.
   Take one down, drink it right down,
   [2][3] of beer.
   `,{beer,
      sprintf(howmany[(beer>1)+1],beer-1),
      howmany[(beer>2)+3]     
     })
end for
```

```mw
-- yet another version:

include std/console.e

object stanza = {
"[] bottles of beer on the wall,",
"[] bottles of beer,",
"take one down, and pass it around,"
}

object bottles = 99

loop do 
    display(stanza[1],bottles)
    display(stanza[2],bottles)
    display(stanza[3])
    bottles -= 1 
    display(stanza[1]&"\n",{bottles})
until bottles = 0 
end loop
```


## Extended BrainF***

See 99 Bottles of Beer/EsoLang


## F

```mw
#light
let rec bottles n =
    let (before, after) = match n with
                          | 1 -> ("bottle", "bottles")
                          | 2 -> ("bottles", "bottle")
                          | n -> ("bottles", "bottles")
    printfn "%d %s of beer on the wall" n before
    printfn "%d %s of beer" n before
    printfn "Take one down, pass it around"
    printfn "%d %s of beer on the wall\n" (n - 1) after
    if n > 1 then
        bottles (n - 1)
```


## Factor

Short & simple solution that uses common stack shuffle words & combinators, and virtual sequences (reversed iota i.e. 99..0):

```mw
USE: math.parser
100 <iota> <reversed>
[ dup 1 - [ >dec " bottles of beer" append [ " on the wall" append ] keep ] bi@
  "Take one down, pass it around" -rot
  first CHAR: - = [ 2drop "..." "why's all the rum gone??" ] when ! if leading character is "-" then replace with new string
  4array "\n" join print nl ] each
```

**Output:**

```
...
1 bottles of beer on the wall
1 bottles of beer
Take one down, pass it around
0 bottles of beer on the wall

0 bottles of beer on the wall
0 bottles of beer
...
why's all the beer gone??
```

Longer solution that defines many words and shows-off the "make" vocabulary, which is used to build-up sequences by using the special characters `#` and `%` to append values to an implicit accumulator string.

```mw
USING: io kernel make math math.parser math.ranges sequences ;

: bottle ( -- quot )
    [
        [
            [
                [ # " bottles of beer on the wall,\n" % ]
                [ # " bottles of beer.\n" % ] bi
            ] keep
            "Take one down, pass it around,\n" %
            1 - # " bottles of beer on the wall\n" %
        ] " " make print
    ] ; inline

: last-verse ( -- )
    "Go to the store and buy some more," 
    "no more bottles of beer on the wall!" [ print ] bi@ ;

: bottles ( n -- )
    1 [a,b] bottle each last-verse ;

! Usage: 99 bottles
```


## Falcon

```mw
for i in [99:1]
 > i, " bottles of beer on the wall"
 > i, " bottles of beer"
 > "Take one down, pass it around"
 > i-1, " bottles of beer on the wall\n"
end
```

A more robust version to handle plural/not plural conditions

```mw
for i in [99:1]
 plural = (i != 1) ? 's' : ""
 > @ "$i bottle$plural of beer on the wall"
 > @ "$i bottle$plural of beer"
 > "Take one down, pass it around"
 > i-1, @ " bottle$plural of beer on the wall\n"
end
```


## FALSE

See 99 Bottles of Beer/EsoLang


## Fe

```mw
(= n 99)
(while (< 0 n)
  (print n "bottles of beer on the wall")
  (print n "bottles of beer")
  (print "Take one down, pass it around")
  (= n (- n 1))
  (print n "bottles of beer on the wall\n"))
```


## ferite

copied from 99-bottles-of-beer.net.

```mw
uses "console";

number bottles = 99;
boolean looping = true;
object counter = closure {
	if (--bottles > 0) {
		return true;
	} else {
		return false;
	}
};

while (looping) {
	Console.println("${bottles} bottles of beer on the wall,");
	Console.println("${bottles} bottles of beer,");
	Console.println("Take one down, pass it around,");
	
	looping = counter.invoke();
	
	Console.println("${bottles} bottles of beer on the wall.");
```


## Fexl

```mw
\suffix=(\n eq n 1 "" "s")
\sing_count=(\n put [n " bottle" (suffix n) " of beer"])
\sing_line1=(\n sing_count n say " on the wall")
\sing_line2=(\n sing_count n nl)
\sing==
	(\n
	le n 0 ();
	sing_line1 n
	sing_line2 n
	say "Take one down, pass it around"
	\n=(- n 1)
	sing_line1 n
	nl
	sing n
	)
sing 3
```

**Output:**

```
3 bottles of beer on the wall
3 bottles of beer
Take one down, pass it around
2 bottles of beer on the wall

2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottle of beer on the wall

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
0 bottles of beer on the wall
```


## FOCAL

```mw
01.10 S N=99
01.15 D 2;T " OF BEER ON THE WALL,",!
01.20 D 2;T " OF BEER,",!
01.24 S N=N-1
01.25 T "TAKE ";I (N),1.3,1.4,1.3
01.30 T "IT";G 1.5
01.40 T "ONE"
01.50 T " DOWN AND PASS IT AROUND,",!
01.60 D 2;T " OF BEER ON THE WALL!",!!
01.70 I (N),1.8,1.15
01.80 Q

02.01 C-PRINT N BOTTLE(S)
02.10 I (N)2.2,2.2,2.3
02.20 T "NO MORE";G 2.4
02.30 D 3
02.40 T " BOTTLE";I (N-1)2.5,2.6,2.5
02.50 T "S"
02.60 R

03.01 C-PRINT 2-DIGIT NUMBER IN N
03.02 C-THIS IS NECESSARY BECAUSE T ALWAYS PREPENDS = TO NUMBERS
03.10 S A=FITR(N/10);I (A),3.3,3.2
03.20 D 4
03.30 S A=N-FITR(N/10)*10;D 4

04.01 C-PRINT DIGIT IN A
04.10 I (A-0),4.20,4.11
04.11 I (A-1),4.21,4.12
04.12 I (A-2),4.22,4.13
04.13 I (A-3),4.23,4.14
04.14 I (A-4),4.24,4.15
04.15 I (A-5),4.25,4.16
04.16 I (A-6),4.26,4.17
04.17 I (A-7),4.27,4.18
04.18 I (A-8),4.28,4.19
04.19 T "9";R
04.20 T "0";R
04.21 T "1";R
04.22 T "2";R
04.23 T "3";R
04.24 T "4";R
04.25 T "5";R
04.26 T "6";R
04.27 T "7";R
04.28 T "8";R
```


## Forth

```mw
:noname   dup . ." bottles" ;
:noname       ." 1 bottle"  ;
:noname ." no more bottles" ;
create bottles , , ,

: .bottles  dup 2 min cells bottles + @ execute ;
: .beer     .bottles ."  of beer" ;
: .wall     .beer ."  on the wall" ;
: .take     ." Take one down, pass it around" ;
: .verse    .wall cr .beer cr
         1- .take cr .wall cr ;
: verses    begin cr .verse ?dup 0= until ;

99 verses
```

Version 2: create a beer language and write the program

```mw
DECIMAL
: BOTTLES ( n -- )
        DUP
        CASE
         1 OF    ." One more bottle " DROP ENDOF
         0 OF    ." NO MORE bottles " DROP ENDOF
                 . ." bottles "    \ DEFAULT CASE
        ENDCASE ;

: ,   [CHAR] , EMIT  SPACE 100 MS CR ;
: .   [CHAR] . EMIT  300 MS  CR CR CR ;

: OF       ." of "   ;     : BEER     ." beer " ;
: ON       ." on "   ;     : THE      ." the "  ;
: WALL     ." wall" ;      : TAKE     ." take " ;
: ONE      ." one "  ;     : DOWN     ." down, " ;
: PASS     ." pass " ;     : IT       ." it "   ;
: AROUND   ." around" ;

: POPONE    1 SWAP CR ;
: DRINK     POSTPONE DO ; IMMEDIATE
: ANOTHER   S" -1 +LOOP" EVALUATE ; IMMEDIATE
: HOWMANY   S" I " EVALUATE ; IMMEDIATE
: ONELESS   S" I 1- " EVALUATE ; IMMEDIATE
: HANGOVER    ." :-("  CR QUIT ;

: BEERS ( n -- )   \ Usage:  99 BEERS
      POPONE
      DRINK
         HOWMANY BOTTLES OF BEER ON THE WALL ,
         HOWMANY BOTTLES OF BEER ,
         TAKE ONE DOWN PASS IT AROUND ,
         ONELESS BOTTLES OF BEER ON THE WALL .
      ANOTHER 
      HANGOVER ;
```

Forth Console Output

```mw
2 beers
2 bottles of beer on the wall,
2 bottles of beer ,
take one down, pass it around,
One more bottle of beer on the wall.

One more bottle of beer on the wall,
One more bottle of beer ,
take one down, pass it around,
No more bottles of beer on the wall.

 ok
```
