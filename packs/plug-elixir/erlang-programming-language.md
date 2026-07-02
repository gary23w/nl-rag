---
title: "Erlang (programming language)"
source: https://en.wikipedia.org/wiki/Erlang_(programming_language)
domain: plug-elixir
license: CC-BY-SA-4.0
tags: plug elixir specification, elixir middleware composition, erlang web adapter, plug connection pipeline
fetched: 2026-07-02
---

# Erlang (programming language)

**Erlang** (/ˈɜːrlæŋ/ *UR-lang*) is a general-purpose, concurrent, functional high-level programming language, and a garbage-collected runtime system. The term Erlang is used interchangeably with Erlang/OTP, or Open Telecom Platform (OTP), which consists of the Erlang runtime system, several ready-to-use components (OTP) mainly written in Erlang, and a set of design principles for Erlang programs.

The Erlang runtime system is designed for systems with these traits:

- Distributed
- Fault-tolerant
- Soft real-time
- Highly available, non-stop applications
- Hot swapping, where code can be changed without stopping a system.

The Erlang programming language has data, pattern matching, and functional programming. The sequential subset of the Erlang language supports eager evaluation, single assignment, and dynamic typing.

A normal Erlang application is built out of hundreds of small Erlang processes.

It was originally proprietary software within Ericsson, developed by Joe Armstrong, Robert Virding, and Mike Williams in 1986, but was released as free and open-source software in 1998. Erlang/OTP is supported and maintained by the Open Telecom Platform (OTP) product unit at Ericsson.

## History

The name *Erlang*, attributed to Bjarne Däcker, has been presumed by those working on the telephony switches (for whom the language was designed) to be a reference to Danish mathematician and engineer Agner Krarup Erlang and a syllabic abbreviation of "Ericsson Language". Erlang was designed with the aim of improving the development of telephony applications. The initial version of Erlang was implemented in Prolog and was influenced by the programming language PLEX used in earlier Ericsson exchanges. By 1988 Erlang had proven that it was suitable for prototyping telephone exchanges, but the Prolog interpreter was far too slow. One group within Ericsson estimated that it would need to be 40 times faster to be suitable for production use. In 1992, work began on the BEAM virtual machine (VM), which compiles Erlang to C using a mix of natively compiled code and threaded code to strike a balance between performance and disk space. According to co-inventor Joe Armstrong, the language went from laboratory product to real applications following the collapse of the next-generation AXE telephone exchange named *AXE-N* in 1995. As a result, Erlang was chosen for the next Asynchronous Transfer Mode (ATM) exchange *AXD*.

In February 1998, Ericsson Radio Systems banned the in-house use of Erlang for new products, citing a preference for non-proprietary languages. The ban caused Armstrong and others to make plans to leave Ericsson. In March 1998 Ericsson announced the AXD301 switch, containing over a million lines of Erlang and reported to achieve a high availability of nine "9"s. In December 1998, the implementation of Erlang was open-sourced and most of the Erlang team resigned to form a new company, Bluetail AB. Ericsson eventually relaxed the ban and re-hired Armstrong in 2004.

In 2006, native symmetric multiprocessing support was added to the runtime system and VM.

### Processes

Erlang applications are built of very lightweight Erlang processes in the Erlang runtime system. The Erlang runtime system provides strict process isolation between Erlang processes (this includes data and garbage collection, separated individually by each Erlang process) and transparent communication between processes (see Location transparency) on different Erlang nodes (on different hosts).

Joe Armstrong, co-inventor of Erlang, summarized the principles of processes in his PhD thesis:

- Everything is a process.
- Processes are strongly isolated.
- Process creation and destruction is a lightweight operation.
- Message passing is the only way for processes to interact.
- Processes have unique names.
- If you know the name of a process you can send it a message.
- Processes share no resources.
- Error handling is non-local.
- Processes do what they are supposed to do or fail.

Joe Armstrong remarked in an interview with Rackspace in 2013: "If Java is 'write once, run anywhere', then Erlang is 'write once, run forever'."

### Usage

In 2014, Ericsson reported Erlang was being used in its support nodes, and in GPRS, 3G and LTE mobile networks worldwide and also by Nortel and Deutsche Telekom.

Erlang is used in RabbitMQ. As Tim Bray, director of Web Technologies at Sun Microsystems, expressed in his keynote at O'Reilly Open Source Convention (OSCON) in July 2008:

> If somebody came to me and wanted to pay me a lot of money to build a large scale message handling system that really had to be up all the time, could never afford to go down for years at a time, I would unhesitatingly choose Erlang to build it in.

Erlang is the programming language used to code WhatsApp.

It is also the language of choice for Ejabberd – an XMPP messaging server.

Elixir is a programming language that compiles into BEAM byte code (via Erlang Abstract Format).

Since being released as open source, Erlang has been spreading beyond telecoms, establishing itself in other vertical markets such as FinTech, gaming, healthcare, automotive, Internet of Things and blockchain. Apart from WhatsApp, there are other companies listed as Erlang's success stories, including Vocalink (a MasterCard company), Goldman Sachs, Nintendo, AdRoll, Grindr, BT Mobile, Samsung, OpenX, and SITA.

## Functional programming examples

### Factorial

A factorial algorithm implemented in Erlang:

```mw
-module(fact). % This is the file 'fact.erl', the module and the filename must match
-export([fac/1]). % This exports the function 'fac' of arity 1 (1 parameter, no type, no name)

fac(0) -> 1; % If 0, then return 1, otherwise (note the semicolon ; meaning 'else')
fac(N) when N > 0, is_integer(N) -> N * fac(N-1).
% Recursively determine, then return the result
% (note the period . meaning 'endif' or 'function end')
%% This function will crash if anything other than a nonnegative integer is given.
%% It illustrates the "Let it crash" philosophy of Erlang.
```

### Fibonacci sequence

A tail recursive algorithm that produces the Fibonacci sequence:

```mw
%% The module declaration must match the file name "series.erl" 
-module(series).

%% The export statement contains a list of all those functions that form
%% the module's public API.  In this case, this module exposes a single
%% function called fib that takes 1 argument (I.E. has an arity of 1)
%% The general syntax for -export is a list containing the name and
%% arity of each public function
-export([fib/1]).

%% ---------------------------------------------------------------------
%% Public API
%% ---------------------------------------------------------------------

%% Handle cases in which fib/1 receives specific values
%% The order in which these function signatures are declared is a vital
%% part of this module's functionality

%% If fib/1 receives a negative number, then return the atom err_neg_val
%% Normally, such defensive coding is discouraged due to Erlang's 'Let
%% it Crash' philosophy, but here the result would be an infinite loop.
fib(N) when N < 0 -> err_neg_val;

%% If fib/1 is passed precisely the integer 0, then return 0
fib(0) -> 0;

%% For all other values, call the private function fib_int/3 to perform
%% the calculation
fib(N) -> fib_int(N-1, 0, 1).

%% ---------------------------------------------------------------------
%% Private API
%% ---------------------------------------------------------------------

%% If fib_int/3 receives 0 as its first argument, then we're done, so
%% return the value in argument B. The second argument is denoted _ to
%% disregard its value.
fib_int(0, _, B) -> B;

%% For all other argument combinations, recursively call fib_int/3
%% where each call does the following:
%%  - decrement counter N
%%  - pass the third argument as the new second argument
%%  - pass the sum of the second and third arguments as the new
%%    third argument
fib_int(N, A, B) -> fib_int(N-1, B, A+B).
```

Omitting the comments gives a much shorter program.

```mw
-module(series).
-export([fib/1]).

fib(N) when N < 0 -> err_neg_val;
fib(0) -> 0;
fib(N) -> fib_int(N-1, 0, 1).

fib_int(0, _, B) -> B;
fib_int(N, A, B) -> fib_int(N-1, B, A+B).
```

### Quicksort

Quicksort in Erlang, using list comprehension:

```mw
%% qsort:qsort(List)
%% Sort a list of items
-module(qsort).     % This is the file 'qsort.erl'
-export([qsort/1]). % A function 'qsort' with 1 parameter is exported (no type, no name)

qsort([]) -> []; % If the list [] is empty, return an empty list (nothing to sort)
qsort([Pivot|Rest]) ->
    % Compose recursively a list with 'Front' for all elements that should be before 'Pivot'
    % then 'Pivot' then 'Back' for all elements that should be after 'Pivot'
    qsort([Front || Front <- Rest, Front < Pivot]) ++ 
    [Pivot] ++
    qsort([Back || Back <- Rest, Back >= Pivot]).
```

The above example recursively invokes the function `qsort` until nothing remains to be sorted. The expression `[Front || Front <- Rest, Front < Pivot]` is a list comprehension, meaning "Construct a list of elements `Front` such that `Front` is a member of `Rest`, and `Front` is less than `Pivot`." `++` is the list concatenation operator.

A comparison function can be used for more complicated structures for the sake of readability.

The following code would sort lists according to length:

```mw
% This is file 'listsort.erl' (the compiler is made this way)
-module(listsort).
% Export 'by_length' with 1 parameter (don't care about the type and name)
-export([by_length/1]).

by_length(Lists) -> % Use 'qsort/2' and provides an anonymous function as a parameter
   qsort(Lists, fun(A,B) -> length(A) < length(B) end).

qsort([], _)-> []; % If list is empty, return an empty list (ignore the second parameter)
qsort([Pivot|Rest], Smaller) ->
    % Partition list with 'Smaller' elements in front of 'Pivot' and not-'Smaller' elements
    % after 'Pivot' and sort the sublists.
    qsort([X || X <- Rest, Smaller(X,Pivot)], Smaller)
    ++ [Pivot] ++
    qsort([Y || Y <- Rest, not(Smaller(Y, Pivot))], Smaller).
```

A `Pivot` is taken from the first parameter given to `qsort()` and the rest of `Lists` is named `Rest`. Note that the expression

```mw
[X || X <- Rest, Smaller(X,Pivot)]
```

is no different in form from

```mw
[Front || Front <- Rest, Front < Pivot]
```

(in the previous example) except for the use of a comparison function in the last part, saying "Construct a list of elements `X` such that `X` is a member of `Rest`, and `Smaller` is true", with `Smaller` being defined earlier as

```mw
fun(A,B) -> length(A) < length(B) end
```

The anonymous function is named `Smaller` in the parameter list of the second definition of `qsort` so that it can be referenced by that name within that function. It is not named in the first definition of `qsort`, which deals with the base case of an empty list and thus has no need of this function, let alone a name for it.

## Data types

Erlang has eight primitive data types:

**Integers**

Integers are written as sequences of decimal digits, for example, 12, 12375 and -23427 are integers. Integer arithmetic is exact and only limited by available memory on the machine. (This is called

arbitrary-precision arithmetic

.)

**Atoms**

Atoms are used within a program to denote distinguished values. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. Atoms can contain any character if they are enclosed within single quotes and an escape convention exists which allows any character to be used within an atom. Atoms are never garbage collected and should be used with caution, especially if using dynamic atom generation.

**Floats**

Floating point numbers use the

IEEE 754 64-bit representation

.

**References**

References are globally unique symbols whose only property is that they can be compared for equality. They are created by evaluating the Erlang primitive

make_ref()

.

**Binaries**

A binary is a sequence of bytes. Binaries provide a space-efficient way of storing binary data. Erlang primitives exist for composing and decomposing binaries and for efficient input/output of binaries.

**Pids**

Pid is short for

process identifier

– a Pid is created by the Erlang primitive

spawn(...)

Pids are references to Erlang processes.

**Ports**

Ports are used to communicate with the external world. Ports are created with the built-in function

open_port

. Messages can be sent to and received from ports, but these messages must obey the so-called "port protocol."

**Funs**

Funs are function

closures

. Funs are created by expressions of the form:

fun(...) -> ... end

.

And three compound data types:

**Tuples**

Tuples are containers for a fixed number of Erlang data types. The syntax

{D1,D2,...,Dn}

denotes a tuple whose arguments are

D1, D2, ... Dn.

The arguments can be primitive data types or compound data types. Any element of a tuple can be accessed in constant time.

**Lists**

Lists are containers for a variable number of Erlang data types. The syntax

[Dh|Dt]

denotes a list whose first element is

Dh

, and whose remaining elements are the list

Dt

. The syntax

[]

denotes an empty list. The syntax

[D1,D2,..,Dn]

is short for

[D1|[D2|..|[Dn|[]]]]

. The first element of a list can be accessed in constant time. The first element of a list is called the

head

of the list. The remainder of a list when its head has been removed is called the

tail

of the list.

**Maps**

Maps contain a variable number of key-value associations. The syntax is

#{Key1=>Value1,...,KeyN=>ValueN}

.

Two forms of syntactic sugar are provided:

**Strings**

Strings are written as doubly quoted lists of characters. This is syntactic sugar for a list of the integer

Unicode

code points for the characters in the string. Thus, for example, the string "cat" is shorthand for

[99,97,116]

.

**Records**

Records provide a convenient way for associating a tag with each of the elements in a tuple. This allows one to refer to an element of a tuple by name and not by position. A pre-compiler takes the record definition and replaces it with the appropriate tuple reference.

## "Let it crash" coding style

Erlang is designed with a mechanism that makes it easy for external processes to monitor for crashes (or hardware failures), rather than an in-process mechanism like exception handling used in many other programming languages. Crashes are reported like other messages, which is the only way processes can communicate with each other, and subprocesses can be spawned cheaply (see below). The "let it crash" philosophy prefers that a process be completely restarted rather than trying to recover from a serious failure. Though it still requires handling of errors, this philosophy results in less code devoted to defensive programming where error-handling code is highly contextual and specific.

### Supervisor trees

A typical Erlang application is written in the form of a supervisor tree. This architecture is based on a hierarchy of processes in which the top level process is known as a "supervisor". The supervisor then spawns multiple child processes that act either as workers or more, lower level supervisors. Such hierarchies can exist to arbitrary depths and have proven to provide a highly scalable and fault-tolerant environment within which application functionality can be implemented.

Within a supervisor tree, all supervisor processes are responsible for managing the lifecycle of their child processes, and this includes handling situations in which those child processes crash. Any process can become a supervisor by first spawning a child process, then calling `erlang:monitor/2` on that process. If the monitored process then crashes, the supervisor will receive a message containing a tuple whose first member is the atom `'DOWN'`. The supervisor is responsible firstly for listening for such messages and for taking the appropriate action to correct the error condition.

## Concurrency and distribution orientation

Erlang's main strength is support for concurrency. It has a small but powerful set of primitives to create processes and communicate among them. Erlang is conceptually similar to the language occam, though it recasts the ideas of communicating sequential processes (CSP) in a functional framework and uses asynchronous message passing. Processes are the primary means to structure an Erlang application. They are neither operating system processes nor threads, but lightweight processes that are scheduled by BEAM. Like operating system processes (but unlike operating system threads), they share no state with each other. The estimated minimal overhead for each is 300 words. Thus, many processes can be created without degrading performance. In 2005, a benchmark with 20 million processes was successfully performed with 64-bit Erlang on a machine with 16 GB random-access memory (RAM; total 800 bytes/process). Erlang has supported symmetric multiprocessing since release R11B of May 2006.

While threads need external library support in most languages, Erlang provides language-level features to create and manage processes with the goal of simplifying concurrent programming. Though all concurrency is explicit in Erlang, processes communicate using message passing instead of shared variables, which removes the need for explicit locks (a locking scheme is still used internally by the VM).

Inter-process communication works via a shared-nothing asynchronous message passing system: every process has a "mailbox", a queue of messages that have been sent by other processes and not yet consumed. A process uses the `receive` primitive to retrieve messages that match desired patterns. A message-handling routine tests messages in turn against each pattern, until one of them matches. When the message is consumed and removed from the mailbox the process resumes execution. A message may comprise any Erlang structure, including primitives (integers, floats, characters, atoms), tuples, lists, and functions.

The code example below shows the built-in support for distributed processes:

```mw
 % Create a process and invoke the function web:start_server(Port, MaxConnections)
 ServerProcess = spawn(web, start_server, [Port, MaxConnections]),

 % Create a remote process and invoke the function
 % web:start_server(Port, MaxConnections) on machine RemoteNode
 RemoteProcess = spawn(RemoteNode, web, start_server, [Port, MaxConnections]),

 % Send a message to ServerProcess (asynchronously). The message consists of a tuple
 % with the atom "pause" and the number "10".
 ServerProcess ! {pause, 10},

 % Receive messages sent to this process
 receive
         a_message -> do_something;
         {data, DataContent} -> handle(DataContent);
         {hello, Text} -> io:format("Got hello message: ~s", [Text]);
         {goodbye, Text} -> io:format("Got goodbye message: ~s", [Text])
 end.
```

As the example shows, processes may be created on remote nodes, and communication with them is transparent in the sense that communication with remote processes works exactly as communication with local processes.

Concurrency supports the primary method of error-handling in Erlang. When a process crashes, it neatly exits and sends a message to the controlling process which can then take action, such as starting a new process that takes over the old process's task.

## Implementation

The official reference implementation of Erlang uses BEAM. BEAM is included in the official distribution of Erlang, called Erlang/OTP. BEAM executes bytecode which is converted to threaded code at load time. It also includes a native code compiler on most platforms, developed by the High Performance Erlang Project (HiPE) at Uppsala University. Since October 2001 the HiPE system is fully integrated in Ericsson's Open Source Erlang/OTP system. It also supports interpreting, directly from source code via abstract syntax tree, via script as of R11B-5 release of Erlang.

## Hot code loading and modules

Erlang supports language-level Dynamic Software Updating. To implement this, code is loaded and managed as "module" units; the module is a compilation unit. The system can keep two versions of a module in memory at the same time, and processes can concurrently run code from each. The versions are referred to as the "new" and the "old" version. A process will not move into the new version until it makes an external call to its module.

An example of the mechanism of hot code loading:

```mw
  %% A process whose only job is to keep a counter.
  %% First version
  -module(counter).
  -export([start/0, codeswitch/1]).

  start() -> loop(0).

  loop(Sum) ->
    receive
       {increment, Count} ->
          loop(Sum+Count);
       {counter, Pid} ->
          Pid ! {counter, Sum},
          loop(Sum);
       code_switch ->
          ?MODULE:codeswitch(Sum)
          % Force the use of 'codeswitch/1' from the latest MODULE version
    end.

  codeswitch(Sum) -> loop(Sum).
```

For the second version, we add the possibility to reset the count to zero.

```mw
  %% Second version
  -module(counter).
  -export([start/0, codeswitch/1]).

  start() -> loop(0).

  loop(Sum) ->
    receive
       {increment, Count} ->
          loop(Sum+Count);
       reset ->
          loop(0);
       {counter, Pid} ->
          Pid ! {counter, Sum},
          loop(Sum);
       code_switch ->
          ?MODULE:codeswitch(Sum)
    end.

  codeswitch(Sum) -> loop(Sum).
```

Only when receiving a message consisting of the atom `code_switch` will the loop execute an external call to codeswitch/1 (`?MODULE` is a preprocessor macro for the current module). If there is a new version of the *counter* module in memory, then its codeswitch/1 function will be called. The practice of having a specific entry-point into a new version allows the programmer to transform state to what is needed in the newer version. In the example, the state is kept as an integer.

In practice, systems are built up using design principles from the Open Telecom Platform, which leads to more code upgradable designs. Successful hot code loading is exacting. Code must be written with care to make use of Erlang's facilities.

## Distribution

In 1998, Ericsson released Erlang as free and open-source software to ensure its independence from a single vendor and to increase awareness of the language. Erlang, together with libraries and the real-time distributed database Mnesia, forms the OTP collection of libraries. Ericsson and a few other companies support Erlang commercially.

Since the open source release, Erlang has been used by several firms worldwide, including Nortel and Deutsche Telekom. Although Erlang was designed to fill a niche and has remained an obscure language for most of its existence, its popularity is growing due to demand for concurrent services. Erlang has found some use in fielding massively multiplayer online role-playing game (MMORPG) servers.
