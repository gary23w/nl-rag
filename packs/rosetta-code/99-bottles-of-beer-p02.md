---
title: "99 bottles of beer (part 2/5)"
source: https://rosettacode.org/wiki/99_Bottles_of_Beer
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 2/5
---

## C

Translation of

:

C++

### The simple solution

```mw
/*
 * 99 Bottles, C, KISS (i.e. keep it simple and straightforward) version
 */

#include <stdio.h>

int main(void)
{
  int n;

  for( n = 99; n > 2; n-- )
    printf(
      "%d bottles of beer on the wall, %d bottles of beer.\n"
      "Take one down and pass it around, %d bottles of beer on the wall.\n\n", 
       n, n, n - 1);

  printf(  
      "2 bottles of beer on the wall, 2 bottles of beer.\n"
      "Take one down and pass it around, 1 bottle of beer on the wall.\n\n"                  

      "1 bottle of beer on the wall, 1 bottle of beer.\n"
      "Take one down and pass it around, no more bottles of beer on the wall.\n\n"                  

      "No more bottles of beer on the wall, no more bottles of beer.\n" 
      "Go to the store and buy some more, 99 bottles of beer on the wall.\n");

      return 0;
}
```

### A recursive solution

```mw
#include <stdio.h>

int main(int argc, char *argv[])
{
        if(argc == 99)
                return 99;
        if(argv[0] != NULL){
                argv[0] = NULL;
                argc = 0;
        }
        argc = main(argc + 1, argv);
        printf("%d bottle%c of beer on the wall\n", argc, argc == 1?'\0': 's');
        printf("%d bottle%c of beer\n", argc, argc == 1?'\0': 's');
        printf("Take one down, pass it around\n"); 
        printf("%d bottle%c of beer on the wall\n\n", argc - 1, (argc - 1) == 1?'\0': 's');
        return argc - 1;
}
```

### Code golf

```mw
#include <stdio.h>
main(){_=100;while(--_)printf("%i bottle%s of beer in the wall,\n%i bottle%"
"s of beer.\nTake one down, pass it round,\n%s%s\n\n",_,_-1?"s":"",_,_-1?"s"
:"",_-1?(char[]){(_-1)/10?(_-1)/10+48:(_-1)%10+48,(_-1)/10?(_-1)%10+48:2+30,
(_-1)/10?32:0,0}:"",_-1?"bottles of beer in the wall":"No more beers");}
```

### A preprocessor solution

Of course, with the template metaprogramming solution, the program has still do the conversion of numbers to strings at runtime, and those function calls also cost unnecessary time. Couldn't we just compose the complete text at compile time, and just output it at run time? Well, with the preprocessor, that's indeed possible:

```mw
#include <stdlib.h>
#include <stdio.h>

#define BOTTLE(nstr) nstr " bottles of beer"

#define WALL(nstr) BOTTLE(nstr) " on the wall"

#define PART1(nstr) WALL(nstr) "\n" BOTTLE(nstr) \
                    "\nTake one down, pass it around\n"

#define PART2(nstr) WALL(nstr) "\n\n"

#define MIDDLE(nstr) PART2(nstr) PART1(nstr)

#define SONG PART1("100") CD2 PART2("0")

#define CD2 CD3("9") CD3("8") CD3("7") CD3("6") CD3("5") \
        CD3("4") CD3("3") CD3("2") CD3("1") CD4("")

#define CD3(pre) CD4(pre) MIDDLE(pre "0")

#define CD4(pre) MIDDLE(pre "9") MIDDLE(pre "8") MIDDLE(pre "7") \
 MIDDLE(pre "6") MIDDLE(pre "5") MIDDLE(pre "4") MIDDLE(pre "3") \
 MIDDLE(pre "2") MIDDLE(pre "1")

int main(void)
{
  (void) printf(SONG);
  return EXIT_SUCCESS;
}
```

An inspection of the generated executable proves that it indeed contains the complete text of the song in one block.

### The bottled version

WYSIWYG (with correct plurals and can buy some more):

```mw
      int b =99,u =1;
     #include<stdio.h>
      char *d[16],y[]
      = "#:ottle/ of"
      ":eer_ a_Go<o5"
      "st>y\x20some6"
      "_Take8;down4p"
      "a=1rou7_17 _<"
      "h;_ m?_nd_ on"
      "_085wal" "l_ "
      "b_e _ t_ss it"
      "_?4bu_ore_9, "
      "\060.""@, 9$";
     # define x  c  ^=
    #include <string.h>
   #define or(t,z) else\
  if(c==t && !(c = 0) &&\
 (c =! z)); int p(char *t)
{ char *s = t; int c; for (
d[c = 0] = y; !t && (d[c +1
]= strchr(s = d[c], '_'));*
(d[++c]++) = 0); for(t = s?
s:t;(c= *s++); c && putchar
(c)) { if (!((( x 48)& ~0xf
) && ( x 48)) ) p(d[c]), c=
0 ; or('$', p(b - 99?".\n":
"." ) && p(b - 99? t : ""))
or ('\x40', c && p( d[!!b--
+ 2])) or('/', c && p( b^1?
"s": "")) or ('\043', b++ ?
p("So6" + --b):!printf("%d"
, b ? --b : (b += 99))) or(
'S',!(++u % 3) * 32+ 78) or
('.', puts("."))}return c;}
 int main() {return p(0);}
```


## C

```mw
using System;

class Program
{
    static void Main(string[] args)
    {
        for (int i = 99; i > -1; i--)
        {
            if (i == 0)
            {
                Console.WriteLine("No more bottles of beer on the wall, no more bottles of beer.");
                Console.WriteLine("Go to the store and buy some more, 99 bottles of beer on the wall.");
                break;
            }
            if (i == 1)
            {
                Console.WriteLine("1 bottle of beer on the wall, 1 bottle of beer.");
                Console.WriteLine("Take one down and pass it around, no more bottles of beer on the wall.");
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine("{0} bottles of beer on the wall, {0} bottles of beer.", i);
                Console.WriteLine("Take one down and pass it around, {0} bottles of beer on the wall.", i - 1);
                Console.WriteLine();
            }
        }
    }
}
```

### C#6 Implementation

Works with

:

C#

version 6+

```mw
using System;
class Program
{
    static void Main()
    {
        Func<int, bool, string> f = (x, y) =>
            $"{(x == 0 ? "No more" : x.ToString())} bottle{(x == 1 ? "" : "s")} of beer{(y ? " on the wall" : "")}\r\n";
        for (int i = 99; i > 0; i--)
            Console.WriteLine($"{f(i, true)}{f(i, false)}Take one down, pass it around\r\n{f(i - 1, true)}");
    }
}
```

### Linq Implementation

Works with

:

C#

version 6+

```mw
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        Enumerable.Range(1, 99).Reverse().Select(x =>
            $"{x} bottle{(x == 1 ? "" : "s")} of beer on the wall, {x} bottle{(x == 1 ? "" : "s")} of beer!\n" +
            $"Take {(x == 1 ? "it" : "one")} down, pass it around, {(x == 1 ? "no more" : (x - 1).ToString())} bottles of beer on the wall!\n"
        ).ToList().ForEach(x => Console.WriteLine(x));
    }
}
```

### Flexible Version

```mw
using System;
using System.Globalization;
class Program
{
    const string Vessel = "bottle";
    const string Beverage = "beer";
    const string Location = "on the wall";

    private static string DefaultAction(ref int bottles)
    {
        bottles--;
        return "take one down, pass it around,";
    }

    private static string FallbackAction(ref int bottles)
    {
        bottles += 99;
        return "go to the store, buy some more,";
    }

    private static string Act(ref int bottles)
    {
        return bottles > 0 ? DefaultAction(ref bottles) : FallbackAction(ref bottles);
    }

    static void Main()
    {
        Func<int, string> plural = b => b == 1 ? "" : "s";
        Func<int, string> describeCount = b => b == 0 ? "no more" : b.ToString();
        Func<int, string> describeBottles = b => string.Format("{0} {1}{2} of {3}", describeCount(b), Vessel, plural(b), Beverage);
        Action<string> write = s => Console.WriteLine(CultureInfo.CurrentCulture.TextInfo.ToTitleCase(s));
        int bottles = 99;
        while (true)
        {
            write(string.Format("{0} {1}, {0},", describeBottles(bottles), Location));
            write(Act(ref bottles));
            write(string.Format("{0} {1}.", describeBottles(bottles), Location));
            write(string.Empty);
        }
    }
}
```

### Using Formatting

Works with

:

C#

version 3+

```mw
class songs
{
    static void Main(string[] args)
    {
        beer(3);
    }

    private static void beer(int bottles)
    {
        for (int i = bottles; i > 0; i--)
        {
            if (i > 1)
            {
                Console.Write("{0}\n{1}\n{2}\n{3}\n\n",
                    i + " bottles of beer on the wall",
                    i + " bottles of beer",
                    "Take one down, pass it around",
                    (i - 1) + " bottles of beer on the wall");
            }
            else
                Console.Write("{0}\n{1}\n{2}\n{3}\n\n",
                    i + " bottle of beer on the wall",
                    i + " bottle of beer",
                    "Take one down, pass it around",
                    (i - 1) + " bottles of beer on the wall....");
        }
    }
}
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
1 bottles of beer on the wall

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
0 bottles of beer on the wall....
```

### Using iterator blocks

Works with

:

C#

version 3+

```mw
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        BeerBottles().Take(99).ToList().ForEach(Console.WriteLine);	
    }

    static IEnumerable<String> BeerBottles()
    {
        int i = 100;
        String f = "{0}, {1}. Take one down, pass it around, {2}";
        Func<int, bool, String> booze = (c , b) => 
            String.Format("{0} bottle{1} of beer{2}", c>0 ? c.ToString() : "no more", (c==1 ? "" : "s"), b ? " on the wall" : "");
	
        while (--i >= 1) 
            yield return String.Format(f, booze(i, true), booze(i, false), booze(i - 1, true));
    }
}
```

### A Fun One

```mw
string[] bottles = { 	"80 Shilling",
			"Abita Amber",
			"Adams Broadside Ale",
			"Altenmünster Premium",
			"August Schell's SnowStorm",
			"Bah Humbug! Christmas Ale",
			"Beck's Oktoberfest",
			"Belhaven Wee Heavy",
			"Bison Chocolate Stout",
			"Blue Star Wheat Beer",
			"Bridgeport Black Strap Stout",
			"Brother Thelonius Belgian-Style Abbey Ale",
			"Capital Blonde Doppelbock",
			"Carta Blanca",
			"Celis Raspberry Wheat",
			"Christian Moerlein Select Lager",
			"Corona",
			"Czechvar",
			"Delirium Tremens",
			"Diamond Bear Southern Blonde",
			"Don De Dieu",
			"Eastside Dark",
			"Eliot Ness",
			"Flying Dog K-9 Cruiser Altitude Ale",
			"Fuller's London Porter",
			"Gaffel Kölsch",
			"Golden Horseshoe",
			"Guinness Pub Draught",
			"Hacker-Pschorr Weisse",
			"Hereford & Hops Black Spring Double Stout",
			"Highland Oatmeal Porter",
			"Ipswich Ale",
			"Iron City",
			"Jack Daniel's Amber Lager",
			"Jamaica Sunset India Pale Ale",
			"Killian's Red",
			"König Ludwig Weiss",
			"Kronenbourg 1664",
			"Lagunitas Hairy Eyball Ale",
			"Left Hand Juju Ginger",
			"Locktender Lager",
			"Magic Hat Blind Faith",
			"Missing Elf Double Bock",
			"Muskoka Cream Ale ",
			"New Glarus Cherry Stout",
			"Nostradamus Bruin",
			"Old Devil",
			"Ommegang Three Philosophers",
			"Paulaner Hefe-Weizen Dunkel",
			"Perla Chmielowa Pils",
			"Pete's Wicked Springfest",
			"Point White Biere",
			"Prostel Alkoholfrei",
			"Quilmes",
			"Rahr's Red",
			"Rebel Garnet",
			"Rickard's Red",
			"Rio Grande Elfego Bock",
			"Rogue Brutal Bitter",
			"Roswell Alien Amber Ale",
			"Russian River Pliny The Elder",
			"Samuel Adams Blackberry Witbier",
			"Samuel Smith's Taddy Porter",
			"Schlafly Pilsner",
			"Sea Dog Wild Blueberry Wheat Ale",
			"Sharp's",
			"Shiner 99",
			"Sierra Dorada",
			"Skullsplitter Orkney Ale",
			"Snake Chaser Irish Style Stout",
			"St. Arnold Bock",
			"St. Peter's Cream Stout",
			"Stag",
			"Stella Artois",
			"Stone Russian Imperial Stout",
			"Sweetwater Happy Ending Imperial Stout",
			"Taiwan Gold Medal",
			"Terrapin Big Hoppy Monster",
			"Thomas Hooker American Pale Ale",
			"Tie Die Red Ale",
			"Toohey's Premium",
			"Tsingtao",
			"Ugly Pug Black Lager",
			"Unibroue Qatre-Centieme",
			"Victoria Bitter",
			"Voll-Damm Doble Malta",
			"Wailing Wench Ale",
			"Warsteiner Dunkel",
			"Wellhead Crude Oil Stout",
			"Weyerbacher Blithering Idiot Barley-Wine Style Ale",
			"Wild Boar Amber",
			"Würzburger Oktoberfest",
			"Xingu Black Beer",
			"Yanjing",
			"Younger's Tartan Special",
			"Yuengling Black & Tan",
			"Zagorka Special",
			"Zig Zag River Lager",
			"Zywiec" };

int bottlesLeft = 99;
const int FIRST_LINE_SINGULAR = 98;
const int FINAL_LINE_SINGULAR = 97;
string firstLine = "";
string finalLine = "";

for (int i = 0; i < 99; i++)
{
	firstLine = bottlesLeft.ToString() + " bottle";
	if (i != FIRST_LINE_SINGULAR)
	    firstLine += "s";
	firstLine += " of beer on the wall, " + bottlesLeft.ToString() + " bottle";
	if (i != FIRST_LINE_SINGULAR)
	    firstLine += "s";
	firstLine += " of beer";

	Console.WriteLine(firstLine);
	Console.WriteLine("Take the " + bottles[i] + " down, pass it around,");
	bottlesLeft--;

	finalLine = bottlesLeft.ToString() + " bottle";
	if (i != FINAL_LINE_SINGULAR)
	    finalLine += "s";
	finalLine += " of beer on the wall!";

	Console.WriteLine(finalLine);
	Console.WriteLine();
	Console.ReadLine();
}
```

### Using recursion

```mw
public static void BottlesSong(int numberOfBottles)
{
    if (numberOfBottles > 0)
    {
        Console.WriteLine("{0} bottles of beer on the wall", numberOfBottles);
        Console.WriteLine("{0} bottles of beer ", numberOfBottles);
        Console.WriteLine("Take one down, pass it around");
        Console.WriteLine("{0} bottles of beer ", numberOfBottles - 1);
        Console.WriteLine();
        BottlesSong(--numberOfBottles);
    }
}
```

### Using a While Loop

```mw
static void Main(string[] args)
{
    int numBottles = 99;
    while (numBottles > 0)
    {
        if (numBottles > 1)
        {
            WriteLine("{0} bottles of beer on the wall, {0} bottles of beer.", numBottles);
            numBottles -= 1;
            WriteLine("Take one down, pass it around, {0} bottles of beer on the wall.\n", numBottles);
        }
        else
        {
            WriteLine("{0} bottle of beer on the wall, {0} bottle of beer.", numBottles);
            numBottles -= 1;
            WriteLine("Take one down, pass it around, no more bottles of beer on the wall.\n");
        }
    }
    WriteLine("No more bottles of beer on the wall, no more bottles of beer.");
    WriteLine("Go to the store to buy some more, 99 bottles of beer on the wall...");
}
```


## C/vFP16

```mw
#pragma SCH_64_16_IFP
#import <jobsched.c>

__attr(@canschedule)
volatile constricts async UVOID <__INVAR const T>base_000000 __PCON(
    impure VFCTX_t^ ct_base,
    impure MCHR_t^ sched_arg,
    __LVAR <const T>XVF_fntype_t^ f,
    <out VF_QSWitch_t>XVF_fn_t^ switchctx
) __ARGFILL {
   VF_Xsched_ILock(ct_base, $->sched);

   captured __VFObj <>VF_KeDbg^ ki = VF_Xg_KeDbg_Instance();

   captured deferred <__VF_T_Auto>__VF_Auto^ vfke = copyof VF_KeDbg_GetRstream<MCHR_t^>(captures ki);
   
   VF_Gsched_SOBFree(sched_arg);
   VF_Gsched_Alloc_U16(65535);
   VF_Msched_MChr_lim(1496);
   VF_Osched_Begin();
   VF_Fsched_Add2(%beer_000099);

   VF_Xsched_IUnlock(ct_base, $->sched);
   
   $switchctx(IMPURE_CTX, %beer_000099(%vfke));
}

__attr(@eUsesIo)
impure constricts UVOID synchronized beer_000099(
    impure __noinline <MCHR_t^>RIGHTSTREAM_t^ outrs
) __NFILL {
    pure UVOID^ uvid = __attr(@purify) $UVOID.;
    while ( 99 > ((volatile NUM_t)^(NUM_t^)(uvid))++ ) {
       VF_STM_Out_NUM((NUM_t^)uvid);
       VF_STM_Out_x(__Dynamic C"bottles on the wall.\nPut one down, pass it around\n");
    }
    
    return $__;
}
```


## C++

### The simple solution

Works with

:

g++

version 4.8.1

```mw
#include <iostream>
using std::cout;

int main() 
{
  for(int bottles(99); bottles > 0; bottles -= 1){
    cout << bottles << " bottles of beer on the wall\n"
         << bottles << " bottles of beer\n"
         << "Take one down, pass it around\n"
         << bottles - 1 << " bottles of beer on the wall\n\n";
  }
}
```

### An object-oriented solution

See: 99 Bottles of Beer/C++/Object Oriented

### A template metaprogramming solution

Of course, the output of the program always looks the same. One may therefore question why the program has to do all that tedious subtracting during runtime. Couldn't the compiler just generate the code to output the text, with ready-calculated constants? Indeed, it can, and the technique is called template metaprogramming. The following short code gives the text without containing a single variable, let alone a loop:

```mw
#include <iostream>

template<int max, int min> struct bottle_countdown
{
  static const int middle = (min + max)/2;
  static void print()
  {
    bottle_countdown<max, middle+1>::print();
    bottle_countdown<middle, min>::print();
  }
};

template<int value> struct bottle_countdown<value, value>
{
  static void print()
  {
    std::cout << value << " bottles of beer on the wall\n"
              << value << " bottles of beer\n"
              << "Take one down, pass it around\n"
              << value-1 << " bottles of beer\n\n";
  }
};

int main()
{
  bottle_countdown<100, 1>::print();
  return 0;
}
```

### A function template solution

Function templates are a different approach to template metaprogramming:

```mw
#include <iostream>

template<unsigned int N> void bottles(){
    std::cout << N << " bottles of beer on the wall\n"
              << N << " bottles of beer\n"
              << "Take one down, pass it around\n"
              << N - 1 << " bottles of beer on the wall\n\n";
    bottles<N-1>();
}

template<> void bottles<0>(){
    std::cout<<"No more bottles of beer on the wall\n"
               "No more bottles of beer\n"
               "Go to the store and buy some more\n"
               "99 bottles of beer on the wall...\n\n";
}

int main(){
    bottles<99>();
}
```

### A Recursive solution

```mw
#include <iostream>
using namespace std;
void rec(int bottles)
{
if ( bottles!=0)    
 {    
     cout << bottles << " bottles of beer on the wall" << endl; 
        cout << bottles << " bottles of beer" << endl;
        cout << "Take one down, pass it around" << endl; 
        cout << --bottles << " bottles of beer on the wall\n" << endl;    
    rec(bottles);
 }  
}

int main() 
 {   
rec(99);
system("pause");
return 0;
}
```

### A preprocessor solution

Of course, with the template metaprogramming solution, the program has still do the conversion of numbers to strings at runtime, and those function calls also cost unnecessary time. Couldn't we just compose the complete text at compile time, and just output it at run time? Well, with the preprocessor, that's indeed possible:

```mw
#include <iostream>
#include <ostream>

#define BOTTLE(nstr) nstr " bottles of beer"

#define WALL(nstr) BOTTLE(nstr) " on the wall"

#define PART1(nstr) WALL(nstr) "\n" BOTTLE(nstr) \
                    "\nTake one down, pass it around\n"

#define PART2(nstr) WALL(nstr) "\n\n"

#define MIDDLE(nstr) PART2(nstr) PART1(nstr)

#define SONG PART1("100") CD2 PART2("0")

#define CD2 CD3("9") CD3("8") CD3("7") CD3("6") CD3("5") \
        CD3("4") CD3("3") CD3("2") CD3("1") CD4("")

#define CD3(pre) CD4(pre) MIDDLE(pre "0")

#define CD4(pre) MIDDLE(pre "9") MIDDLE(pre "8") MIDDLE(pre "7") \
 MIDDLE(pre "6") MIDDLE(pre "5") MIDDLE(pre "4") MIDDLE(pre "3") \
 MIDDLE(pre "2") MIDDLE(pre "1")

int main()
{
  std::cout << SONG;
  return 0;
}
```

### Bottled Version

```mw
                          //>,_
                        //Beer Song>,_
                       #include <iostream>
                      using namespace std;
                     int main(){ for( int
                    b=-1; b<99;  cout <<
                   '\n') for ( int w=0;
                  w<3; cout << ".\n"){ 
                 if (w==2) cout << ((
                b--) ?"Take one dow"
               "n and pass it arou"
              "nd":"Go to the sto"
             "re and buy some mo"
            "re"); if (b<0) b=99
           ; do{ if (w) cout <<
          ", "; if (b) cout <<
          b;  else  cout << (
         (w) ? 'n' : 'N') <<
         "o more"; cout <<
         " bottle" ;  if
        (b!=1) cout <<
       's' ; cout <<
       " of beer";
      if (w!=1)
     cout  <<
    " on th"
   "e wall"
  ;} while
 (!w++);}
  return
       0
       ;
       }
      //
  // by barrym 2011-05-01
     // no bottles were harmed in the
            // making of this program!!!
```


## Calcscript

In Calcscript, `0` is represented by the type `Same` (which prints as `Same`).

Therefore, in order to match the output, we need to test for `0` separately.

```
(fn chk_same (n)
  (r
    (eq (- n 1) (pc 48))
    (p n .)
  )
)

(fn loop (n)
  (d
    (t n)
    (p n .) (pc 32) (puts bottles of beer on the wall)
    (p n .) (pc 32) (puts bottles of beer)
    (puts Take one down, pass it around)
    (chk_same n) (pc 32) (puts bottles of beer on the wall)
    (puts)
    (loop (- n 1))
  )
)

(loop 99)
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


## Ceylon

```mw
shared void ninetyNineBottles() {
	
	String bottles(Integer count) => 
			"``count == 0 then "No" else count`` 
			 bottle``count == 1 then "" else "s"``".normalized;
	
	for(i in 99..1) {
		print("``bottles(i)`` of beer on the wall
		       ``bottles(i)`` of beer!
		       Take one down, pass it around
		       ``bottles(i - 1)`` of beer on the wall!\n");
	}
}
```


## Chapel

copied from http://99-bottles-of-beer.net/language-chapel-1215.html, with minor modifications for chapel 1.7

Works with

:

Chapel

version 1.7.0

```mw
/***********************************************************************
 * Chapel implementation of "99 bottles of beer"
 *
 * by Brad Chamberlain and Steve Deitz
 * 07/13/2006 in Knoxville airport while waiting for flight home from
 *            HPLS workshop
 * compiles and runs with chpl compiler version 1.7.0
 * for more information, contact: chapel_info@cray.com
 * 
 *
 * Notes: 
 * o as in all good parallel computations, boundary conditions
 *   constitute the vast bulk of complexity in this code (invite Brad to
 *   tell you about his zany boundary condition simplification scheme)
 * o uses type inference for variables, arguments
 * o relies on integer->string coercions
 * o uses named argument passing (for documentation purposes only)
 ***********************************************************************/

// allow executable command-line specification of number of bottles 
// (e.g., ./a.out -snumBottles=999999)
config const numBottles = 99;
const numVerses = numBottles+1;

// a domain to describe the space of lyrics
var LyricsSpace: domain(1) = {1..numVerses};

// array of lyrics
var Lyrics: [LyricsSpace] string;

// parallel computation of lyrics array
[verse in LyricsSpace] Lyrics(verse) = computeLyric(verse);

// as in any good parallel language, I/O to stdout is serialized.
// (Note that I/O to a file could be parallelized using a parallel
// prefix computation on the verse strings' lengths with file seeking)
writeln(Lyrics);

// HELPER FUNCTIONS:

proc computeLyric(verseNum) {
  var bottleNum = numBottles - (verseNum - 1);
  var nextBottle = (bottleNum + numVerses - 1)%numVerses;
  return "\n" // disguise space used to separate elements in array I/O
       + describeBottles(bottleNum, startOfVerse=true) + " on the wall, "
       + describeBottles(bottleNum) + ".\n"
       + computeAction(bottleNum)
       + describeBottles(nextBottle) + " on the wall.\n";
}

proc describeBottles(bottleNum, startOfVerse:bool = false) {
// NOTE: bool should not be necessary here (^^^^); working around bug
  var bottleDescription = if (bottleNum) then bottleNum:string 
                                         else (if startOfVerse then "N" 
                                                               else "n") 
                                              + "o more";
  return bottleDescription 
       + " bottle" + (if (bottleNum == 1) then "" else "s") 
       + " of beer";
}

proc computeAction(bottleNum) {
  return if (bottleNum == 0) then "Go to the store and buy some more, "
                             else "Take one down and pass it around, ";
}
```


## Chef

See 99 Bottles of Beer/EsoLang


## Cind

```mw
execute() {

    // this class provides synchronization
    // to get unique number of the bottle

    class monitor giver {      
        int number = 100;    
        .get() { return --number; }
    }
    var g = new giver(); 

    // start 99 concurrently worked threads
    // each thread gets own number of the bottle and prints out his own verse
    // (notice that the output lines from the threads will be mixed together)

    {#[99] 
        int nr = g.get(); // get own number
        host.println(nr," bottles of beer on the wall, "+nr+" bottles of beer");
        host.print("Take one down, pass it around,");
        if (nr > 1) {
            host.println((nr-1)," bottles of beer on the wall.");
        }
        else {
            host.println("no more bottles of beer on the wall.");
        }
    }
    host.println("No more bottles of beer on the wall, no more bottles of beer.");
    host.println("Go to the store and buy some more, 99 bottles of beer on the wall.");
    return 0;
}
```


## Clay

```mw
/* A few options here: I could give n type Int; or specify that n is of any
   numeric type; but here I just let it go -- that way it'll work with anything
   that compares with 1 and that printTo knows how to convert to a string. And
   all checked at compile time, remember. */
getRound(n) {
    var s      = String();
    var bottle = if (n == 1) " bottle " else " bottles ";
    
    printTo(s, 
            n, bottle, "of beer on the wall\n",
            n, bottle, "of beer\n",
            "take one down, pass it around\n",
            n, bottle, "of beer on the wall!\n");
    
    return s;
}

main() {
    println(join("\n", mapped(getRound, reversed(range(100)))));
}
```


## Clio

```mw
fn bottle n:
  n -> if = 0: 'no more bottles'
     elif = 1:    n + ' bottle'
         else:    n + ' bottles'

[99:0] -> * (@eager) fn i:
  i -> bottle -> print (transform i: sentence-case) 'of beer on the wall,' @ 'of beer.'
  if i = 0:
    'Go to the store, buy some more, 99 bottles of beer on the wall.' -> print
  else:
    i - 1 -> bottle -> print 'Take one down and pass it around,' @ 'of beer on the wall.\n'
```


## CLIPS

```mw
(deffacts beer-bottles
  (bottles 99))

(deffunction bottle-count
  (?count)
  (switch ?count
    (case 0 then "No more bottles of beer")
    (case 1 then "1 more bottle of beer")
    (default (str-cat ?count " bottles of beer"))))

(defrule stanza
  ?bottles <- (bottles ?count)
  =>
  (retract ?bottles)
  (printout t (bottle-count ?count) " on the wall," crlf)
  (printout t (bottle-count ?count) "." crlf)
  (printout t "Take one down, pass it around," crlf)
  (printout t (bottle-count (- ?count 1)) " on the wall." crlf crlf)
  (if (> ?count 1) then (assert (bottles (- ?count 1)))))
```


## Clojure

```mw
(defn paragraph [num]
  (str num " bottles of beer on the wall\n" 
       num " bottles of beer\n"
       "Take one down, pass it around\n"
       (dec num) " bottles of beer on the wall.\n"))

(defn lyrics [] 
  (let [numbers (range 99 0 -1)
        paragraphs (map paragraph numbers)]
    (clojure.string/join "\n" paragraphs)))

(print (lyrics))
```

Or, using cl-format:

Translation of

:

Common Lisp

```mw
(clojure.pprint/cl-format 
  true 
  "~{~[~^~]~:*~D bottle~:P of beer on the wall~%~:*~D bottle~:P of beer
Take one down, pass it around,~%~D bottle~:P~:* of beer on the wall.~2%~}"
  (range 99 0 -1))
```


## CLU

```mw
bottles = proc (n: int) returns (string)
    if n<0 then return("99 bottles")
    elseif n=0 then return("No more bottles")
    elseif n=1 then return("1 bottle")
    else return(int$unparse(n) || " bottles")
    end
end bottles

thirdline = proc (n: int) returns (string)
    if n=0 then
        return("Go to the store and buy some more,\n")
    else
        s: string
        if n=1 then s := "it"
        else s := "one"
        end
        return("Take " || s || " down and pass it around,\n");
    end
end thirdline

verse = proc (n: int) returns (string)
    v: string := bottles(n) || " bottles of beer on the wall,\n"
    v := v || bottles(n) || " bottles of beer,\n"
    v := v || thirdline(n)
    v := v || bottles(n-1) || " bottles of beer on the wall.\n\n"
    return(v)
end verse

start_up = proc ()
    po: stream := stream$primary_output()
    
    for n: int in int$from_to_by(99, 0, -1) do
        stream$puts(po, verse(n))
    end
end start_up
```


## COBOL

Works with

:

OpenCOBOL

version 1.1

Free form version.

```mw
identification division.
program-id. ninety-nine.
environment division.
data division.
working-storage section.
01	counter	pic 99.
	88 no-bottles-left value 0.
	88 one-bottle-left value 1.

01	parts-of-counter redefines counter.
	05	tens		pic 9.
	05	digits		pic 9.

01	after-ten-words.
	05	filler	pic x(7) value spaces.
	05	filler	pic x(7) value "Twenty".
	05	filler	pic x(7) value "Thirty".
	05	filler	pic x(7) value "Forty".
	05	filler	pic x(7) value "Fifty".
	05	filler	pic x(7) value "Sixty".
	05	filler	pic x(7) value "Seventy".
	05	filler	pic x(7) value "Eighty".
	05	filler	pic x(7) value "Ninety".
	05	filler	pic x(7) value spaces.

01	after-ten-array redefines after-ten-words.
	05	atens occurs 10 times pic x(7).

01	digit-words.
	05	filler	pic x(9) value "One".
	05	filler	pic x(9) value "Two".
	05	filler	pic x(9) value "Three".
	05	filler	pic x(9) value "Four".
	05	filler	pic x(9) value "Five".
	05	filler	pic x(9) value "Six".
	05	filler	pic x(9) value "Seven".
	05	filler	pic x(9) value "Eight".
	05	filler	pic x(9) value "Nine".
	05	filler	pic x(9) value "Ten".
	05	filler	pic x(9) value "Eleven".
	05	filler	pic x(9) value "Twelve".
	05	filler	pic x(9) value "Thirteen".
	05	filler	pic x(9) value "Fourteen".
	05	filler	pic x(9) value "Fifteen".
	05	filler	pic x(9) value "Sixteen".
	05	filler	pic x(9) value "Seventeen".
	05	filler	pic x(9) value "Eighteen".
	05	filler	pic x(9) value "Nineteen".
	05	filler	pic x(9) value spaces.
	
01	digit-array redefines digit-words.
	05	adigits occurs 20 times 	pic x(9).
	
01	number-name pic x(15).

procedure division.
100-main section.
100-setup.
	perform varying counter from 99 by -1 until no-bottles-left
		perform 100-show-number
		display " of beer on the wall"
		perform 100-show-number
		display " of beer"
		display "Take " with no advancing
		if one-bottle-left 
			display "it " with no advancing
		else
			display "one " with no advancing
		end-if
		display "down and pass it round"
		subtract 1 from counter giving counter
		perform 100-show-number
		display " of beer on the wall"
		add 1 to counter giving counter
		display space
	end-perform.
	display "No more bottles of beer on the wall"
	display "No more bottles of beer"
	display "Go to the store and buy some more"
	display "Ninety Nine bottles of beer on the wall"
	stop run.
	
100-show-number.
	if no-bottles-left 
		display "No more" with no advancing
	else 
		if counter < 20
			display function trim( adigits( counter ) ) with no advancing
		else 
			if counter < 100
				move spaces to number-name
				string atens( tens ) delimited by space, space delimited by size, adigits( digits ) delimited by space into number-name
				display function trim( number-name) with no advancing
			end-if
		end-if
	end-if.
	if one-bottle-left
		display " bottle" with no advancing
	else
		display " bottles" with no advancing
	end-if.

100-end.
end-program.
```

Another free-form version, without using `DISPLAY NO ADVANCING`.

```mw
identification division.
program-id. ninety-nine.
environment division.
data division.
working-storage section.
01	counter	pic 99.
	88 no-bottles-left value 0.
	88 one-bottle-left value 1.
 
01	parts-of-counter redefines counter.
	05	tens		pic 9.
	05	digits		pic 9.
 
01	after-ten-words.
	05	filler	pic x(7) value spaces.
	05	filler	pic x(7) value "Twenty".
	05	filler	pic x(7) value "Thirty".
	05	filler	pic x(7) value "Forty".
	05	filler	pic x(7) value "Fifty".
	05	filler	pic x(7) value "Sixty".
	05	filler	pic x(7) value "Seventy".
	05	filler	pic x(7) value "Eighty".
	05	filler	pic x(7) value "Ninety".
	05	filler	pic x(7) value spaces.
 
01	after-ten-array redefines after-ten-words.
	05	atens occurs 10 times pic x(7).
 
01	digit-words.
	05	filler	pic x(9) value "One".
	05	filler	pic x(9) value "Two".
	05	filler	pic x(9) value "Three".
	05	filler	pic x(9) value "Four".
	05	filler	pic x(9) value "Five".
	05	filler	pic x(9) value "Six".
	05	filler	pic x(9) value "Seven".
	05	filler	pic x(9) value "Eight".
	05	filler	pic x(9) value "Nine".
	05	filler	pic x(9) value "Ten".
	05	filler	pic x(9) value "Eleven".
	05	filler	pic x(9) value "Twelve".
	05	filler	pic x(9) value "Thirteen".
	05	filler	pic x(9) value "Fourteen".
	05	filler	pic x(9) value "Fifteen".
	05	filler	pic x(9) value "Sixteen".
	05	filler	pic x(9) value "Seventeen".
	05	filler	pic x(9) value "Eighteen".
	05	filler	pic x(9) value "Nineteen".
	05	filler	pic x(9) value spaces.
 
01	digit-array redefines digit-words.
	05	adigits occurs 20 times 	pic x(9).
 
01	number-name pic x(15).

01	stringified pic x(30).
01	outline		pic x(50).
01  other-numbers.
	03	n	pic 999.
	03	r	pic 999.
	
procedure division.
100-main section.
100-setup.
	perform varying counter from 99 by -1 until no-bottles-left
		move spaces to outline
		perform 100-show-number
		string stringified delimited by "|", space, "of beer on the wall" into outline end-string
		display outline end-display
		move spaces to outline
		string stringified delimited by "|", space, "of beer" into outline end-string
		display outline end-display
		move spaces to outline
		move "Take" to outline
		if one-bottle-left
			string outline delimited by space, space, "it" delimited by size, space, "|" into outline end-string
		else
			string outline delimited by space, space, "one" delimited by size, space, "|" into outline end-string
		end-if
		string outline delimited by "|", "down and pass it round" delimited by size into outline end-string
		display outline end-display
		move spaces to outline
		subtract 1 from counter giving counter end-subtract
		perform 100-show-number
		string stringified delimited by "|", space, "of beer on the wall" into outline end-string
		display outline end-display
		add 1 to counter giving counter end-add
		display space end-display
	end-perform.
	display "No more bottles of beer on the wall"
	display "No more bottles of beer"
	display "Go to the store and buy some more"
	display "Ninety-Nine bottles of beer on the wall"
	stop run.
 
100-show-number.
	if no-bottles-left 
		move "No more|" to stringified
	else 
		if counter < 20
			string function trim( adigits( counter ) ), "|" into stringified
		else 
			if counter < 100
				move spaces to number-name
				string atens( tens ) delimited by space, space delimited by size, adigits( digits ) delimited by space into number-name end-string
				move function trim( number-name) to stringified
				divide counter by 10 giving n remainder r end-divide
				if r not = zero
					inspect stringified replacing first space by "-" 
				end-if
				inspect stringified replacing first space by "|" 
			end-if
		end-if
	end-if.
	if one-bottle-left
		string stringified delimited by "|", space, "bottle|" delimited by size into stringified end-string
	else
		string stringified delimited by "|", space, "bottles|" delimited by size into stringified end-string
	end-if.
 
100-end.
end-program.
```

A more concise version that adheres to the minimum guidelines. Leading zeros are not suppressed. (OpenCOBOL - 1.1.0)

```mw
program-id. ninety-nine.
data division.
working-storage section.
01  cnt       pic 99.

procedure division.

  perform varying cnt from 99 by -1 until cnt < 1
    display cnt " bottles of beer on the wall"
    display cnt " bottles of beer"
    display "Take one down, pass it around"
    subtract 1 from cnt 
    display cnt " bottles of beer on the wall"
    add 1 to cnt
    display space
  end-perform.
```


## CoffeeScript

```mw
bottlesOfBeer = (n) -> 
  "#{n} bottle#{if n is 1 then '' else 's'} of beer"

console.log """
  #{bottlesOfBeer n} on the wall
  #{bottlesOfBeer n}
  Take one down, pass it around
  #{bottlesOfBeer n - 1} on the wall
  \n""" for n in [99..1]
```

With completely different approach...

```mw
for j in [99..1]
    x=''
    x += [j,j-1,'\nTake one down, pass it around\n'," bottles of beer",' on the wall\n'][i] for i in [0,3,4,0,3,2,1,3,4]
    console.log x.replace /(1.+)s/g, '$1'
```

or as a one liner...

```mw
console.log( if (j+2)%4 then (x=Math.round j/4)+" bottle#{if x-1 then 's' else ''} of beer#{if (j+1)%4 then ' on the wall' else ''}" else "Take one down, pass it around" ) for j in [396..1]
```

or another completely different one liner

```mw
((console.log if i is 2 then "Take one down, pass it around" else "#{b-!(i-1%4)} bottle#{if 4*b+i<10 and b-i then '' else 's'} of beer#{if i%3 then ' on the wall' else ''}") for i in [4..1]) for b in [99..1]
```


## ColdFusion

### Classic tag based CFML

```mw
<cfoutput>
  <cfloop index="x" from="99" to="0" step="-1">
    <cfset plur = iif(x is 1,"",DE("s"))>
    #x# bottle#plur# of beer on the wall<br>
    #x# bottle#plur# of beer<br>
    Take one down, pass it around<br>
    #iif(x is 1,DE("No more"),"x-1")# bottle#iif(x is 2,"",DE("s"))# of beer on the wall<br><br>
  </cfloop>
</cfoutput>
```

or if you prefer: (identical output, grammatically correct to the last stanza)

### CFScript

```mw
<cfscript>
  for (x=99; x gte 1; x--) {
    plur = iif(x==1,'',DE('s'));
    WriteOutput("#x# bottle#plur# of beer on the wall<br>#x# bottle#plur# of beer<br>Take one down, pass it around<br>#iif(x is 1,DE('No more'),'x-1')# bottle#iif(x is 2,'',DE('s'))# of beer on the wall<br><br>");
  }
</cfscript>
```


## Comal

```mw
0010 DIM itone$(0:1)
0020 itone$(0):="one";itone$(1):="it"
0030 FOR b#:=99 TO 1 STEP -1 DO
0040   bottles(b#)
0050   PRINT "of beer on the wall,"
0060   bottles(b#)
0070   PRINT "of beer,"
0080   PRINT "Take ",itone$(b#=1)," down and pass it around,"
0090   bottles(b#-1)
0100   PRINT "of beer on the wall!"
0110   PRINT
0120 ENDFOR b#
0130 PROC bottles(b#) CLOSED
0140   CASE b# OF
0150   WHEN 0
0160     PRINT "No more bottles ",
0170   WHEN 1
0180     PRINT "1 bottle ",
0190   OTHERWISE
0200     PRINT b#," bottles ",
0210   ENDCASE
0220 ENDPROC bottles
0230 END
```


## Comefrom0x10

```mw
bottles = ' bottles '
remaining = 99
one_less_bottle = remaining
depluralize
  comefrom drinking if one_less_bottle is 1
  bottles = ' bottle '

drinking
  comefrom if remaining is one_less_bottle
  remaining bottles 'of beer on the wall'
  remaining bottles 'of beer'
  'Take one down, pass it around'
  one_less_bottle = remaining - 1
  one_less_bottle bottles 'of beer on the wall`n'
  remaining = remaining - 1

  comefrom if one_less_bottle is 0
  'No more bottles of beer on the wall'
```

**Output:**

```
2 bottles of beer on the wall
2 bottles of beer
Take one down, pass it around
1 bottle of beer on the wall

1 bottle of beer on the wall
1 bottle of beer
Take one down, pass it around
No more bottles of beer on the wall
```


## Common Lisp

See 99 Bottles of Beer/Lisp


## Component Pascal

See 99 Bottles of Beer/Pascal
