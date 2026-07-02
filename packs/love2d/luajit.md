---
title: "LuaJIT"
source: https://en.wikipedia.org/wiki/LuaJIT
domain: love2d
license: CC-BY-SA-4.0
tags: love2d framework, love game framework, lua game framework, luajit game
fetched: 2026-07-02
---

# LuaJIT

**LuaJIT** is a tracing just-in-time compiler and interpreter for the Lua programming language.

## History

The LuaJIT project was started in 2005 by developer Mike Pall, released under the MIT open source license.

The second major release of the compiler, 2.0.0, featured major performance increases.

LuaJIT uses rolling releases. Mike Pall, the creator and maintainer recommends using the tip of the v2.1 branch, and does not believe in releases.

Mike Pall resigned in 2015 making only occasional patching to the future 2.1 version since then.

## Notable users

- CERN, for their Methodical Accelerator Design 'next-generation' software for describing and simulating particle accelerators
- OpenResty, a fork of nginx with Lua scripting
- Neovim, a text editor based on vim that allows the use of Lua for plugins and configuration
- Kong, a web API gateway
- Cloudflare, who use LuaJIT in their web application firewall service

## Performance

LuaJIT is often the fastest Lua runtime. LuaJIT has also been named the fastest implementation of a dynamic programming language.

LuaJIT includes a Foreign Function Interface compatible with C data structures. Its use is encouraged for numerical computation.

### Tracing

LuaJIT is a tracing just-in-time compiler. LuaJIT chooses loops and function calls as trace anchors to begin recording possible hot paths. Function calls will require twice as many invocations to begin recording as a loop. Once LuaJIT begins recording, all control flow, including jumps and calls, are inlined to form a linear trace. All executed bytecode instructions are stored and incrementally converted into LuaJIT's static single-assignment intermediate representation. LuaJIT's trace compiler is often capable of inlining and removing dispatches from object orientation, operators, and type modifications.

### Internal representation

LuaJIT uses two types of internal representation. A stack-based bytecode is used for the interpreter, and a static single-assignment form is used for the just-in-time compiler. The interpreter bytecode is frequently patched by the JIT compiler, often to begin executing a compiled trace or to mark a segment of bytecode for causing too many trace aborts.

```mw
-- Loop with if-statement

local x = 0

for i=1,1e4 do
    x = x + 11
    if i%10 == 0 then -- if-statement
        x = x + 22
    end
    x = x + 33
end
```

```mw
---- TRACE 1 start Ex.lua:5
---- TRACE 1 IR
0001 int SLOAD #2 CI
0002 > num SLOAD #1 T
0003 num ADD 0002 +11
0004 int MOD 0001 +10
0005 > int NE 0004 +0
0006 + num ADD 0003 +33
0007 + int ADD 0001 +1
0008 > int LE 0007 +10000
0009 ------ LOOP ------------
0010 num ADD 0006 +11
0011 int MOD 0007 +10
0012 > int NE 0011 +0
0013 + num ADD 0010 +33
0014 + int ADD 0007 +1
0015 > int LE 0014 +10000
0016 int PHI 0007 0014
0017 num PHI 0006 0013
---- TRACE 1 stop -> loop
---- TRACE 2 start 1/4 Ex.lua:8
---- TRACE 2 IR
0001 num SLOAD #1 PI
0002 int SLOAD #2 PI
0003 num ADD 0001 +22
0004 num ADD 0003 +33
0005 int ADD 0002 +1
0006 > int LE 0005 +10000
0007 num CONV 0005 num.int
---- TRACE 2 stop -> 1
```

## Extensions

LuaJIT adds several extensions to its base implementation, Lua 5.1, most of which do not break compatibility.

- "BitOp" for binary operations on unsigned 32-bit integers (these operations are also compiled by the just-in-time compiler)
- "CoCo", which allows the VM to be fully resumable across all contexts
- A foreign function interface
- Portable bytecode (regardless of architecture, word size, or endianness, not version)
