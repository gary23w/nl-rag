---
title: "SystemVerilog DPI"
source: https://en.wikipedia.org/wiki/SystemVerilog_DPI
domain: systemverilog
license: CC-BY-SA-4.0
tags: systemverilog language, hardware verification language, rtl verification, hardware description language
fetched: 2026-07-02
---

# SystemVerilog DPI

**SystemVerilog DPI** (**Direct Programming Interface**) is an interface which can be used to interface SystemVerilog with foreign languages. These foreign languages can be C, C++, SystemC as well as others. DPIs consist of two layers: a SystemVerilog layer and a foreign language layer. Both the layers are isolated from each other.

## Explanation

Direct Programming Interface (**DPI**) allows direct inter language function calls between the SystemVerilog and Foreign language. The functions implemented in Foreign language can be called from SystemVerilog and such functions are called **Import** functions. Similarly, functions implemented in SystemVerilog can be called from Foreign language (**C/C++ or System C**); such functions are called **Export** functions. DPIs allow transfer of data between two domains through function arguments and return.

## Function import and export

1) Function Import:- A function implemented in Foreign language can be used in SystemVerilog by importing it. A Foreign language function used in SystemVerilog is called Imported function.

## Properties of imported function and task

1. An Imported function shall complete their execution instantly and consume zero simulation time. Imported task can consume time.
2. Imported function can have input, output, and inout arguments.
  - The formal input arguments shall not be modified. If such arguments are changed within a function, the changes shall not be visible outside the function.
  - Imported function shall not assume any initial values of formal output arguments. The initial value of output arguments is undetermined and implementation dependent.
  - Imported function can access the initial value of a formal inout argument. Changes that the Imported function makes to a formal inout argument shall be visible outside the function.
3. An Imported function shall not free the memory allocated by SystemVerilog code nor expect SystemVerilog code to free memory allocated by Foreign code or (Foreign Compiler).
4. A call to an Imported task can result in suspension of the currently executing thread. This occurs when an Imported task calls an Exported task, and the Exported task executes a delay control, event control or wait statement. Thus it is possible for an Imported task to be simultaneously active in multiple execution threads.
5. An Imported function or task can be equip with special properties called pure or context.

## Pure and context tasks and functions

### Pure functions

A function whose results solely depends on the value of its input arguments with no side effects is called Pure function.

#### Properties of pure functions

1. Only Non-Void functions with no output or inout arguments can be called as Pure functions.
2. Functions specified as Pure shall have no side effects, their results need to depend solely on the values of their input arguments.
3. A Pure function call can be safely eliminated if its result is not needed or if its results for the same value of input arguments is available for reuse without needing to recalculate.
4. A Pure function is assumed not to directly or indirectly perform the following:
  1. Perform any file operation.
  2. Read or Write anything in Environment Variable, Shared memory, Sockets etc.
  3. Access any persistent data like Global or Static variable.
5. An Imported task can never be declared Pure.

### Context tasks and functions

An Imported task or function which calls "Exported" tasks or functions or accesses SystemVerilog data objects other than its actual arguments is called Context task or function.

#### Properties of context tasks and functions

1) A Context Imported task or function can access (read or write) any SystemVerilog data object by calling (PLI/VPI) or by calling Export task or function. Therefore, a call to Context task or function is a barrier for SystemVerilog compiler optimization.

## Import declaration

```mw
import "DPI-C" function int calc_parity (input int a);
```

## Export declaration

```mw
export "DPI-C" my_cfunction = function myfunction;
```

## Calling Unix functions

SystemVerilog code can call Unix functions directly by importing them, with no need for a wrapper.

## DPI example

### Calling 'C' functions in SystemVerilog

#### C - code file

```mw
#include <stdio.h>
#include <stdlib.h>

extern int add(void) {
  int a = 10, b = 20;
  a = a + b;

  printf("Addition Successful and Result = %d\n", a);
  return a;
}
```

#### SystemVerilog code file

```mw
module tb_dpi;

  import "DPI-C" function int add();
  import "DPI-C" function int sleep(input int secs);
  int j;
  
  initial
  begin
    $display("Entering in SystemVerilog Initial Block");
    #20
    j = add();
    $display("Value of J = %d", j);
    $display("Sleeping for 3 seconds with Unix function");
    sleep(3);
    $display("Exiting from SystemVerilog Initial Block");
    #5 $finish;
  end
  
endmodule
```
