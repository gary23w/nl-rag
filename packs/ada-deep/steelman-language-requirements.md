---
title: "Ada (programming language)"
source: https://en.wikipedia.org/wiki/Steelman_language_requirements
domain: ada-deep
license: CC-BY-SA-4.0
tags: ada language, spark language, jean ichbiah, real time computing, formal verification, steelman requirements
fetched: 2026-07-02
---

# Ada (programming language)

(Redirected from

Steelman language requirements

)

**Ada** is a structured, statically typed, imperative, and object-oriented high-level programming language, inspired by Pascal and other languages. It has built-in language support for *design by contract* (DbC), extremely strong typing, explicit concurrency, tasks, synchronous message passing, protected objects, and non-determinism. Ada improves code safety and maintainability by using the compiler to find errors in favor of runtime errors. Ada is an international technical standard, jointly defined by the International Organization for Standardization (ISO), and the International Electrotechnical Commission (IEC). As of May 2023, the standard, ISO/IEC 8652:2023, is called Ada 2022 informally.

Ada was originally designed by a team led by French computer scientist Jean Ichbiah of Honeywell under contract to the United States Department of Defense (DoD) from 1977 to 1983 to supersede over 450 programming languages then used by the DoD. Ada was named after Ada Lovelace (1815–1852), who has been credited as the first computer programmer.

## Features

Ada was originally designed for embedded and real-time systems. The Ada 95 revision, designed by S. Tucker Taft of Intermetrics between 1992 and 1995, improved support for systems, numerical, financial, and object-oriented programming (OOP).

Features of Ada include strong typing, modular programming mechanisms (packages), run-time checking, parallel processing (tasks, synchronous message passing, protected objects, and nondeterministic select statements), exception handling, and generics. Ada 95 added support for object-oriented programming, including dynamic dispatch.

The syntax of Ada minimizes choices of ways to perform basic operations, and prefers English keywords (such as `or else` and `and then`) to symbols (such as `||` and `&&`). Ada uses the basic arithmetical operators `+`, `-`, `*`, and `/`, but avoids using other symbols. Code blocks are delimited by words such as 'declare', 'begin', and 'end', where the 'end' (in most cases) is followed by the keyword of the block that it closes (e.g., `if` ... `end if`, `loop` ... `end loop`). In the case of conditional blocks this avoids a *dangling else* that could pair with the wrong nested 'if'-expression in other languages such as C or Java.

Ada is designed for developing very large software systems. Ada packages can be compiled separately. Ada package specifications (the package interface) can also be compiled separately without the implementation to check for consistency. This makes it possible to detect problems early during the design phase, before implementation starts.

A large number of compile-time checks are supported to help avoid bugs that would not be detectable until run time in some other languages or would require explicit checks to be added to the source code. For example, the syntax requires explicitly named closing of blocks to prevent errors due to mismatched end tokens. The adherence to strong typing allows detecting many common software errors (wrong parameters, range violations, invalid references, mismatched types, etc.) either during compile time, or otherwise during run time. As concurrency is part of the language specification, the compiler can in some cases detect potential deadlocks. Compilers also commonly check for misspelled identifiers, visibility of packages, redundant declarations, etc. and can provide warnings and useful suggestions on how to fix the error.

Ada also supports run-time checks to protect against access to unallocated memory, buffer overflow errors, range violations, off-by-one errors, array access errors, and other detectable bugs. These checks can be disabled in the interest of runtime efficiency, but can often be compiled efficiently. It also includes facilities to help program verification. For these reasons, Ada is sometimes used in critical systems, where any anomaly might lead to very serious consequences, e.g., accidental death, injury or severe financial loss. Examples of systems where Ada is used include avionics, air traffic control, railways, banking, military and space technology.

Ada's dynamic memory management is high-level and type-safe. Ada has no generic or untyped pointers, nor does it implicitly declare any pointer type. Instead, all dynamic memory allocation and deallocation must occur via explicitly declared *access types*. Each access type has an associated *storage pool* that handles the low-level details of memory management; the programmer can either use the default storage pool or define new ones (this is particularly relevant for non-uniform memory access). It is even possible to declare several different access types that all designate the same type but use different storage pools. Also, the language provides for *accessibility checks*, both at compile time and at run time, that ensures that an *access value* cannot outlive the type of the object it points to.

Though the semantics of the language allow automatic garbage collection of inaccessible objects, most implementations do not support it by default, as it would cause unpredictable behaviour in real-time systems. Ada supports a limited form of region-based memory management, and in Ada, destroying a storage pool also destroys all the objects in the pool.

A double dash (`--`), resembling an em dash, denotes comment text. Comments stop at end of line; there is intentionally no way to make a comment span multiple lines, to prevent unclosed comments from accidentally voiding whole sections of source code. Disabling a whole block of code therefore requires the prefixing of each line (or column) individually with `--`. While this clearly denotes disabled code by creating a column of repeated '--' down the page, it also renders the experimental dis/re-enablement of large blocks a more drawn-out process in editors without block commenting support.

The semicolon (`;`) is a statement terminator, and the null or no-operation statement is `null;`. A single `;` without a statement to terminate is not allowed.

Unlike most ISO standards, the Ada language definition (known as the *Ada Reference Manual* or *ARM*, or sometimes the *Language Reference Manual* or *LRM*) is free content. Thus, it is a common reference for Ada programmers, not only programmers implementing Ada compilers. Apart from the reference manual, there is also an extensive rationale document which explains the language design and the use of various language constructs. This document is also widely used by programmers. When the language was revised, a new rationale document was written.

One notable free software tool that is used by many Ada programmers to aid them in writing Ada source code is the GNAT Programming Studio, and GNAT which is part of the GNU Compiler Collection.

*Alire* is a package and toolchain management tool for Ada.

## History

In the 1970s the US Department of Defense (DoD) became concerned by the number of different programming languages being used for its embedded computer system projects, many of which were obsolete or hardware-dependent, and none of which supported safe modular programming. In 1975, a working group, the High Order Language Working Group (HOLWG), was formed with the intent to reduce this number by finding or creating a programming language generally suitable for the department's and the UK Ministry of Defence's requirements. After many iterations beginning with an original straw-man proposal the eventual programming language was named Ada. The total number of high-level programming languages in use for such projects fell from over 450 in 1983 to 37 by 1996.

HOLWG crafted the **Steelman language requirements**, a series of documents stating the requirements they felt a programming language should satisfy. Many existing languages were formally reviewed, but the team concluded in 1977 that no existing language met the specifications. The requirements were created by the United States Department of Defense in *The Department of Defense Common High Order Language program* in 1978. The predecessors of this document were called, in order, "Strawman", "Woodenman", "Tinman" and "Ironman". The requirements focused on the needs of embedded computer applications, and emphasised reliability, maintainability, and efficiency. Notably, they included exception handling facilities, run-time checking, and parallel computing.

It was concluded that no existing language met these criteria to a sufficient extent, so a contest was called to create a language that would be closer to fulfilling them. The design that won this contest became the Ada programming language. The resulting language followed the Steelman requirements closely, though not exactly.

Requests for proposals for a new programming language were issued and four contractors were hired to develop their proposals under the names of Red (Intermetrics led by Benjamin Brosgol), Green (Honeywell, led by Jean Ichbiah), Blue (SofTech, led by John Goodenough) and Yellow (SRI International, led by Jay Spitzen). In April 1978, after public scrutiny, the Red and Green proposals passed to the next phase. In May 1979, the Green proposal, designed by Jean Ichbiah at Honeywell, was chosen and given the name Ada—after Augusta Ada King, Countess of Lovelace, usually known as Ada Lovelace. This proposal was influenced by the language LIS that Ichbiah and his group had developed in the 1970s. The preliminary Ada reference manual was published in ACM SIGPLAN Notices in June 1979. The Military Standard reference manual was approved on December 10, 1980 (Ada Lovelace's birthday), and given the number MIL-STD-1815 in honor of Ada Lovelace's birth year. In 1981, Tony Hoare took advantage of his Turing Award speech to criticize Ada for being overly complex and hence unreliable, but subsequently seemed to recant in the foreword he wrote for an Ada textbook.

Ada attracted much attention from the programming community as a whole during its early days. Its backers and others predicted that it might become a dominant language for general purpose programming and not only defense-related work. Ichbiah publicly stated that within ten years, only two programming languages would remain: Ada and Lisp. Early Ada compilers struggled to implement the large, complex language, and both compile-time and run-time performance tended to be slow and tools primitive. Compiler vendors expended most of their efforts in passing the massive, language-conformance-testing, government-required Ada Compiler Validation Capability (ACVC) validation suite that was required in another novel feature of the Ada language effort.

The first validated Ada implementation was the NYU Ada/Ed translator, certified on April 11, 1983. NYU Ada/Ed is implemented in the high-level set language SETL. Several commercial companies began offering Ada compilers and associated development tools, including Alsys, TeleSoft, DDC-I, Advanced Computer Techniques, Tartan Laboratories, Irvine Compiler, TLD Systems, and Verdix. Computer manufacturers who had a significant business in the defense, aerospace, or related industries, also offered Ada compilers and tools on their platforms; these included Concurrent Computer Corporation, Cray Research, Inc., Digital Equipment Corporation, Harris Computer Systems, and Siemens Nixdorf Informationssysteme AG.

In 1991, the US Department of Defense began to require the use of Ada (the *Ada mandate*) for all software, though exceptions to this rule were often granted. The Department of Defense Ada mandate was effectively removed in 1997, as the DoD began to embrace commercial off-the-shelf (COTS) technology. Similar requirements existed in other NATO countries: Ada was required for NATO systems involving command and control and other functions, and Ada was the mandated or preferred language for defense-related applications in countries such as Sweden, Germany, and Canada.

By the late 1980s and early 1990s, Ada compilers had improved in performance, but there were still barriers to fully exploiting Ada's abilities, including a tasking model that was different from what most real-time programmers were used to.

Because of Ada's safety-critical support features, it is now used not only for military applications, but also in commercial projects where a software bug can have severe consequences, e.g., avionics and air traffic control, commercial rockets such as the Ariane 4 and 5, satellites and other space systems, railway transport and banking. For example, the Primary Flight Control System, the fly-by-wire system software in the Boeing 777, was written in Ada, as were the fly-by-wire systems for the aerodynamically unstable Eurofighter Typhoon, Saab Gripen, Lockheed Martin F-22 Raptor and the DFCS replacement flight control system for the Grumman F-14 Tomcat. The Canadian Automated Air Traffic System was written in 1 million lines of Ada (SLOC count). It featured advanced distributed processing, a distributed Ada database, and object-oriented design. Ada is also used in other air traffic systems, e.g., the UK's next-generation Interim Future Area Control Tools Support (iFACTS) air traffic control system is designed and implemented using SPARK Ada. It is also used in the French TVM in-cab signalling system on the TGV high-speed rail system, and the metro suburban trains in Paris, London, Hong Kong and New York City.

The Ada 95 revision of the language went beyond the Steelman requirements, targeting general-purpose systems in addition to embedded ones, and adding features supporting object-oriented programming.

## Standardization

| Year | Informal name | Official Standard |
|---|---|---|
| 1980 | Ada | ANSI MIL-STD 1815 |
| 1983 | Ada 83/87 | ANSI MIL-STD 1815A ISO/IEC 8652:1987 |
| 1995 | Ada 95 | ISO/IEC 8652:1995 |
| 2001 | ISO/IEC 8652:1995/Cor 1:2001 |   |
| 2007 | Ada 2005 | ISO/IEC 8652:1995/Amd 1:2007 |
| 2012 | Ada 2012 | ISO/IEC 8652:2012 |
| 2016 | ISO/IEC 8652:2012/Cor 1:2016 |   |
| 2023 | Ada 2022 | ISO/IEC 8652:2023 |

Preliminary Ada can be found in ACM Sigplan Notices Vol 14, No 6, June 1979

Ada was first published in 1980 as an ANSI standard ANSI/**MIL-STD 1815**. As this very first version held many errors and inconsistencies, the revised edition was published in 1983 as ANSI/MIL-STD 1815A. Without any further changes, it became an ISO standard in 1987. This version of the language is commonly known as **Ada 83**, from the date of its adoption by ANSI, but is sometimes referred to also as **Ada 87**, from the date of its adoption by ISO. There is also a French translation; DIN translated it into German as DIN 66268 in 1988.

**Ada 95**, the joint ISO/IEC/ANSI standard ISO/IEC 8652:1995 was published in February 1995, making it the first ISO standard object-oriented programming language. To help with the standard revision and future acceptance, the US Air Force funded the development of the GNAT Compiler. Presently, the GNAT Compiler is part of the GNU Compiler Collection.

Work has continued on improving and updating the technical content of the Ada language. A Technical Corrigendum to Ada 95 was published in October 2001, and a major Amendment, ISO/IEC 8652:1995/Amd 1:2007 was published on March 9, 2007, commonly known as **Ada 2005** because work on the new standard was finished that year.

At the Ada-Europe 2012 conference in Stockholm, the Ada Resource Association (ARA) and Ada-Europe announced the completion of the design of the latest version of the Ada language and the submission of the reference manual to the ISO/IEC JTC 1/SC 22/WG 9 of the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) for approval. ISO/IEC 8652:2012 (see Ada 2012 RM) was published in December 2012, known as **Ada 2012**. A technical corrigendum, ISO/IEC 8652:2012/COR 1:2016, was published (see RM 2012 with TC 1).

The Ada-based SPARK technology has been made possible by the enabling characteristics of the Ada language, including its separation of specification and implementation via packages, its support for user-defined scalar types, and its support for composite type usage without resorting to pointers. The Ada 2012 revision was especially important for SPARK, as its support for contracts as a part of the language permitted SPARK to be redesigned from the beginning towards fulfilling its goal of co-developing programs alongside their proofs of correctness.

On May 2, 2023, the Ada community saw the formal approval of publication of the **Ada 2022** edition of the programming language standard.

Despite the names Ada 83, 95 etc., legally there is only one Ada standard, the last ISO/IEC standard: with the acceptance of a new standard version, the previous one becomes withdrawn. The other names are informal ones referencing a certain edition.

Other related standards include ISO/IEC 8651-3:1988 *Information processing systems—Computer graphics—Graphical Kernel System (GKS) language bindings—Part 3: Ada*.

## Language constructs

Ada is an ALGOL-like programming language featuring control structures with reserved words such as *if*, *then*, *else*, *while*, *for*, and so on. However, Ada also has many data structuring facilities and other abstractions which were not included in the original ALGOL 60, such as type definitions, records, pointers, and enumerations. Such constructs were in part inherited from or inspired by Pascal.

### "Hello, world!" in Ada

A common example of a language's syntax is the "Hello, World!" program: (hello.adb)

```mw
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
   Put_Line ("Hello, world!");
end;
```

This program can be compiled by using the freely available open source compiler GNAT, by executing

```mw
gnatmake hello.adb
```

### Data types

Ada's type system is not based on a set of predefined primitive types but allows users to declare their own types. This declaration in turn is not based on the internal representation of the type but on describing the goal which should be achieved. This allows the compiler to determine a suitable memory size for the type, and to check for violations of the type definition at compile time and run time (i.e., range violations, buffer overruns, type consistency, etc.). Ada supports numerical types defined by a range, modulo types, aggregate types (records and arrays), and enumeration types. Access types define a reference to an instance of a specified type; untyped pointers are not permitted. Special types provided by the language are task types and protected types.

For example, a date might be represented as:

```mw
type Day_type   is range    1 ..   31;
type Month_type is range    1 ..   12;
type Year_type  is range 1800 .. 2100;
type Hours is mod 24;
type Weekday is (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday);

type Date is
   record
     Day   : Day_type;
     Month : Month_type;
     Year  : Year_type;
   end record;
```

Day_type, Month_type, Year_type, Hours are incompatible types, meaning that for instance the following expression is illegal:

```mw
Today: Day_type := 4;
Current_Month: Month_type := 10;
... Today + Current_Month ...  -- illegal
```

The predefined plus operator can only add values of the same type, so the expression is illegal.

Types can be refined by declaring subtypes:

```mw
subtype Working_Hours is Hours range 0 .. 12;            -- at most 12 Hours to work a day
subtype Working_Day is Weekday range Monday .. Friday;   -- Days to work

Work_Load: constant array(Working_Day) of Working_Hours  -- implicit type declaration
   := (Friday => 6, Monday => 4, others => 10);           -- lookup table for working hours with initialization
```

Types can have modifiers such as *limited, abstract, private* etc. Private types do not show their inner structure; objects of limited types cannot be copied. Ada 95 adds further features for object-oriented extension of types.

### Control structures

Ada is a structured programming language, meaning that the flow of control is structured into standard statements. All standard constructs and deep-level early exit are supported, so the use of the also supported "go to" commands is seldom needed.

```mw
-- while a is not equal to b, loop.
while a /= b loop
  Ada.Text_IO.Put_Line ("Waiting");
end loop;

if a > b then
  Ada.Text_IO.Put_Line ("Condition met");
else
  Ada.Text_IO.Put_Line ("Condition not met");
end if;

for i in 1 .. 10 loop
  Ada.Text_IO.Put ("Iteration: ");
  Ada.Text_IO.Put (i);
  Ada.Text_IO.Put_Line;
end loop;

loop
  a := a + 1;
  exit when a = 10;
end loop;

case i is
  when 0 => Ada.Text_IO.Put ("zero");
  when 1 => Ada.Text_IO.Put ("one");
  when 2 => Ada.Text_IO.Put ("two");
  -- case statements have to cover all possible cases:
  when others => Ada.Text_IO.Put ("none of the above");
end case;

for aWeekday in Weekday'Range loop               -- loop over an enumeration
   Put_Line ( Weekday'Image(aWeekday) );         -- output string representation of an enumeration
   if aWeekday in Working_Day then               -- check of a subtype of an enumeration
      Put_Line ( " to work for " &
               Working_Hours'Image (Work_Load(aWeekday)) ); -- access into a lookup table
   end if;
end loop;
```

### Packages, procedures and functions

Among the parts of an Ada program are packages, procedures and functions.

Functions differ from procedures in that they must return a value. Function calls cannot be used "as a statement", and their result must be assigned to a variable. However, since Ada 2012, functions are not required to be pure and may mutate their suitably declared parameters or the global state.

Example: Package specification (example.ads)

```mw
package Example is
     type Number is range 1 .. 11;
     procedure Print_and_Increment (j: in out Number);
end Example;
```

Package body (example.adb)

```mw
with Ada.Text_IO;
package body Example is

  i : Number := Number'First;

  procedure Print_and_Increment (j: in out Number) is

    function Next (k: in Number) return Number is
    begin
      return k + 1;
    end Next;

  begin
    Ada.Text_IO.Put_Line ( "The total is: " & Number'Image(j) );
    j := Next (j);
  end Print_and_Increment;

-- package initialization executed when the package is elaborated
begin
  while i < Number'Last loop
    Print_and_Increment (i);
  end loop;
end Example;
```

This program can be compiled, e.g., by using the freely available open-source compiler GNAT, by executing

```mw
gnatmake -z example.adb
```

Packages, procedures and functions can nest to any depth, and each can also be the logical outermost block.

Each package, procedure or function can have its own declarations of constants, types, variables, and other procedures, functions and packages, which can be declared in any order.

### Pragmas

A pragma is a compiler directive that conveys information to the compiler to allow specific manipulating of compiled output. Certain pragmas are built into the language, while others are implementation-specific.

Examples of common usage of compiler pragmas would be to disable certain features, such as run-time type checking or array subscript boundary checking, or to instruct the compiler to insert object code instead of a function call (as C/C++ does with inline functions).

### Generics

Section 'Generics in Ada' not found
