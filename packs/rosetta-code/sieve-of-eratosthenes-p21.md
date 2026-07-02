---
title: "Sieve of Eratosthenes (part 21/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 21/21
---

## Xojo

Place the following in the **Run** event handler of a Console application:

```mw
Dim limit, prime, i As Integer
Dim s As String
Dim t As Double
Dim sieve(100000000) As Boolean

REM Get the maximum number
While limit<1 Or limit > 100000000
  Print("Max number? [1 to 100000000]")
  s = Input
  limit = CDbl(s)
Wend

REM Do the calculations
t = Microseconds
prime = 2
While prime^2 < limit
  For i = prime*2 To limit Step prime
    sieve(i) = True
  Next
  Do
    prime = prime+1
  Loop Until Not sieve(prime)
Wend
t = Microseconds-t
Print("Compute time = "+Str(t/1000000)+" sec")
Print("Press Enter...")
s = Input

REM Display the prime numbers
For i = 1 To limit
  If Not sieve(i) Then Print(Str(i))
Next
s = Input
```

**Output:**

```
Max number? [1 to 100000000]
1000
Compute time = 0.0000501 sec
Press Enter...

1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
...
```

This version uses a dynamic array and can use (a lot) less memory. It's (a lot) slower too. Since Booleans are manually set to True, the algorithm makes more sense.

```mw
Dim limit, prime, i As Integer
Dim s As String
Dim t As Double
Dim sieve() As Boolean

REM Get the maximum number and define array
While limit<1 Or limit > 2147483647
  Print("Max number? [1 to 2147483647]")
  s = Input
  limit = CDbl(s)
Wend
t = Microseconds
For i = 0 To Limit
   Sieve.Append(True)
Next
t = Microseconds-t
Print("Memory allocation time = "+Str(t/1000000)+" sec")

REM Do the calculations
t = Microseconds
prime = 2
While prime^2 < limit
  For i = prime*2 To limit Step prime
    sieve(i) = False
  Next
  Do
    prime = prime+1
  Loop Until sieve(prime)
Wend
t = Microseconds-t
Print("Compute time = "+Str(t/1000000)+" sec")
Print("Press Enter...")
s = Input

REM Display the prime numbers
For i = 1 To limit
  If sieve(i) Then Print(Str(i))
Next
s = Input
```

**Output:**

```
Max number? [1 to 2147483647]
1000
Memory allocation time = 0.0000296 sec
Compute time = 0.0000501 sec
Press Enter...

1
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
...
```


## Woma

```mw
(sieve(n = /0 -> int; limit = /0 -> int; is_prime = [/0] -> *)) *
    i<@>range(n*n, limit+1, n)
        is_prime = is_prime[$]i,False
    <*>is_prime

(primes_upto(limit = 4 -> int)) list(int)
    primes = [] -> list
    f = [False, False] -> list(bool)
    t = [True] -> list(bool)
    u = limit - 1 -> int
    tt = t * u -> list(bool)
    is_prime = flatten(f[^]tt) -> list(bool)
    limit_sqrt = limit ** 0.5 -> float
    iter1 = int(limit_sqrt + 1.5) -> int

    n<@>range(iter1)
        is_prime[n]<?>is_prime = sieve(n, limit, is_prime)

    i,prime<@>enumerate(is_prime)
        prime<?>primes = primes[^]i
    <*>primes
```


## Wren

```mw
var sieveOfE = Fn.new { |n|
    if (n < 2) return []
    var comp = List.filled(n-1, false)
    var p = 2
    while (true) {
        var p2 = p * p
        if (p2 > n) break
        var i = p2
        while (i <= n) {
            comp[i-2] = true
            i = i + p
        }
        while (true) {
            p = p + 1
            if (!comp[p-2]) break
        }
    }
    var primes = []
    for (i in 0..n-2) {
        if (!comp[i]) primes.add(i+2)
    }
    return primes
}

System.print(sieveOfE.call(100))
```

**Output:**

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```


## XPL0

```mw
include c:\cxpl\codes;                  \intrinsic 'code' declarations
int  Size, Prime, I, Kill;
char Flag;
[Size:= IntIn(0);
Flag:= Reserve(Size+1);
for I:= 2 to Size do Flag(I):= true;
for I:= 2 to Size do
    if Flag(I) then                     \found a prime
        [Prime:= I;
        IntOut(0, Prime);  CrLf(0);
        Kill:= Prime + Prime;           \first multiple to kill
        while Kill <= Size do
                [Flag(Kill):= false;    \zero a non-prime
                Kill:= Kill + Prime;    \next multiple
                ];
        ];
]
```

**Example output:**

```
20
2
3
5
7
11
13
17

19
```


## X86-64 Assembly

### WINDOW MASM 64 bits

file macrosInclude.asm

```mw
; Sieve of Eratosthenes
; assembly X86 window
; download and install visual studio 2022 free site microsoft
; search and open  X64 native tools command prompt
; compil and link program with this command :
; ml64  cribleera.asm  /link /ENTRY:main /SUBSYSTEM:console kernel32.lib user32.lib Shell32.lib
; this program respects the 64-bit calling convention : 
; registers arguments : rcx rdx r8 r9 and stack
; registers saved : rbx,rbp,rdi,rsi, r12-r15 
; ATTENTION les registres rax,rcx,rdx,r8-r11 peuvent être
; perdus lors d'un appel de fonction 
;*********************************
; constantes
;*********************************
STD_OUTPUT_HANDLE equ -11
MAXI              equ 101
;*********************************
; macros
;*********************************
;for this file, see task include a file for X86-64 language 
include macrosInclude.asm

;*********************************
; user data
;*********************************
.data
szMessPrime    db "Prime : ",0
LGMESSPRIME      equ $ - szMessPrime - 1

szCarriageReturn  db 10,0   

align 8

hConsole       dq 0
sConvArea      db 24 dup (0)
tablePrime     db MAXI dup (0)
;*********************************
; user code fonction principale
;*********************************
.code

extern WriteFile : proc, GetStdHandle : proc, ExitProcess : proc
extern GetLastError : proc

main PROC public
    displayLib "Program X86-64 start."
	
	mov rdi, offset tablePrime
	mov rbx,2
	mov r8,1
	mov rcx,rbx
	call displayResult
B1:
    mov [rdi+rbx],r8b
	add rbx,2
	cmp rbx,MAXI
    jl B1
	mov rbx,3
	mov r12,1
B2:
	mov al,[rdi+rbx]
	cmp al,1
	je suite	
	mov rcx,rbx
	call displayResult
	mov rbp,rbx
	
B3:
    mov [rdi+rbp],r12b
	add rbp,rbx             ; add prime
    cmp rbp,MAXI
    jle B3
suite:
	add rbx,2
	cmp rbx,MAXI
    jle B2
     
finProgramme: 
    displayLib "Program end."
    sub rsp,28h
    mov rcx,0                ; return code
    call ExitProcess
main ENDP
;**************************************
;   insertion fin de ligne
;**************************************
; rcx contains value
displayResult proc            ; INFO: displayResult
    push rbx
	mov rbx,rcx
	mov rcx, offset szMessPrime
	mov rdx,LGMESSPRIME
	call afficherConsole
	mov rcx,rbx
    mov rdx,offset sConvArea
    call conversion10
	mov rdx,rax
	mov rcx, offset sConvArea
	call afficherConsole
	mov rcx, offset szCarriageReturn
    mov rdx,1
    call afficherConsole
	pop rbx
    ret
displayResult endp

;for this file, see task include a file for X86-64 language
include routinesInclude.asm
   
end
```

**Output:**

```
Program X86-64 start.
Prime : 2
Prime : 3
Prime : 5
Prime : 7
Prime : 11
Prime : 13
Prime : 17
Prime : 19
Prime : 23
Prime : 29
Prime : 31
Prime : 37
Prime : 41
Prime : 43
Prime : 47
Prime : 53
Prime : 59
Prime : 61
Prime : 67
Prime : 71
Prime : 73
Prime : 79
Prime : 83
Prime : 89
Prime : 97
Prime : 101
Program end.
```


## Yabasic

```mw
#!/usr/bin/yabasic

// ---------------------------
// Prime Sieve Benchmark --
// "Shootout" Version    --
// ---------------------------
// usage:
//     yabasic sieve8k.yab 90000

SIZE = 8192
ONN = 1 : OFF = 0
dim flags(SIZE)

sub main()
    
    cmd = peek("arguments")
    if cmd = 1 then
       iterations = val(peek$("argument"))
       if iterations = 0 then print "Argument wrong. Done 1000." : iterations = 1000 end if
    else
       print "1000 iterations."
       iterations = 1000
    end if
    
    for iter = 1 to iterations
        count = 0
        for n= 1 to SIZE : flags(n) = ONN: next n
        for i = 2 to SIZE
            if flags(i) = ONN then
               let k = i + i
               if k < SIZE then
                 for k = k to SIZE step i
                    flags(k) = OFF
                 next k
               end if
               count = count + 1                 
            end if
        next i
    next iter
    print "Count: ", count  // 1028
end sub

clear screen

print "Prime Sieve Benchmark\n"

main()

t = val(mid$(time$,10))

print "time: ", t, "\n"
print peek("millisrunning")
```


## YAMLScript

```mw
!ys-0

defn main(n=100):
  primes =: n:primes-up-to
  say: |-
    The $(primes.#) prime numbers less than $n are:
    $(text(primes):chomp)

defn primes-up-to(limit):
  :: Returns a lazy sequence of prime numbers less than limit.

  max-i =: int(limit.-- / 2)
  refs =: boolean-array(max-i true)
  root =: sqrt(limit):int.-- / 2
  ? doseq i (1 .. root)
      :when aget(refs i)
  : ? doseq
        j range(
            mul(i.++ 2 i),
            max-i,
            add(i i 1))
    : aset(refs j false)
  cons 2:
    map \((_ * 2).++):
      filter \(aget refs _):
        range(1 max-i)
```

**Output:**

```
$ ys sieve-of-eratosthenes.ys
The 25 prime numbers less than 100 are:
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```


## Zen C

Translation of

:

Wren

```mw
import "std/vec.zc"

fn sieve_of_eratosthenes(n: int) -> Vec<int> {
    let primes = Vec<int>::new();
    if n < 2 { return primes; }
    autofree let comp = (bool*)calloc(n - 1, sizeof(bool));
    let p = 2;
    loop {
        let p2 = p * p;
        if p2 > n { break; }
        let i = p2;
        while i <= n {
            comp[i - 2] = true;
            i += p;
        }
        loop {
            p++;
            if !comp[p - 2] { break; }
        }
    }
    for i in 0..(n - 1) {
        if !comp[i] { primes << (i + 2); }
    }
    return primes;
}

fn main() {
    println "Primes less than 100:";
    let primes = sieve_of_eratosthenes(100);
    for p in primes { print "{p} "; }
    println "";
}
```

**Output:**

```
Primes less than 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
```


## Zig

```mw
const std = @import("std");
const stdout = std.io.getStdOut().outStream();

pub fn main() !void {
    try sieve(1000);
}

// using a comptime limit ensures that there's no need for dynamic memory.
fn sieve(comptime limit: usize) !void {
    var prime = [_]bool{true} ** limit;
    prime[0] = false;
    prime[1] = false;
    var i: usize = 2;
    while (i*i < limit) : (i += 1) {
        if (prime[i]) {
            var j = i*i;
            while (j < limit) : (j += i)
                prime[j] = false;
        }
    }
    var c: i32 = 0;
    for (prime) |yes, p|
        if (yes) {
            c += 1;
            try stdout.print("{:5}", .{p});
            if (@rem(c, 10) == 0)
                try stdout.print("\n", .{});
        };
    try stdout.print("\n", .{});
}
```

**Output:**

```
$ zig run sieve.zig 
    2    3    5    7   11   13   17   19   23   29
   31   37   41   43   47   53   59   61   67   71
   73   79   83   89   97  101  103  107  109  113
  127  131  137  139  149  151  157  163  167  173
  179  181  191  193  197  199  211  223  227  229
  233  239  241  251  257  263  269  271  277  281
  283  293  307  311  313  317  331  337  347  349
  353  359  367  373  379  383  389  397  401  409
  419  421  431  433  439  443  449  457  461  463
  467  479  487  491  499  503  509  521  523  541
  547  557  563  569  571  577  587  593  599  601
  607  613  617  619  631  641  643  647  653  659
  661  673  677  683  691  701  709  719  727  733
  739  743  751  757  761  769  773  787  797  809
  811  821  823  827  829  839  853  857  859  863
  877  881  883  887  907  911  919  929  937  941
  947  953  967  971  977  983  991  997
```

### Odds-only bit packed version

Translation of

:

BCPL

Includes the iterator, as with the BCPL Odds-only bit packed sieve. Since it's not much extra code, the sieve object also includes methods for getting the size and testing for membership.

```mw
const std = @import("std");
const heap = std.heap;
const mem = std.mem;
const stdout = std.io.getStdOut().writer();

pub fn main() !void {
    const assert = std.debug.assert;

    var buf: [fixed_alloc_sz(1000)]u8 = undefined; // buffer big enough for 1,000 primes.
    var fba = heap.FixedBufferAllocator.init(&buf);

    const sieve = try SoE.init(1000, &fba.allocator);
    defer sieve.deinit(); // not needed for the FBA, but in general you would de-init the sieve

    // test membership functions
    assert(sieve.contains(997));
    assert(!sieve.contains(995));
    assert(!sieve.contains(994));
    assert(!sieve.contains(1009));

    try stdout.print("There are {} primes < 1000\n", .{sieve.size()});
    var c: u32 = 0;
    var iter = sieve.iterator();
    while (iter.next()) |p| {
        try stdout.print("{:5}", .{p});
        c += 1;
        if (c % 10 == 0)
            try stdout.print("\n", .{});
    }
    try stdout.print("\n", .{});
}

// return size to sieve n prmes if using the Fixed Buffer Allocator
//     adds some u64 words for FBA bookkeeping.
pub inline fn fixed_alloc_sz(limit: usize) usize {
    return (2 + limit / 128) * @sizeOf(u64);
}

pub const SoE = struct {
    const all_u64bits_on = 0xFFFF_FFFF_FFFF_FFFF;
    const empty = [_]u64{};

    sieve: []u64,
    alloc: *mem.Allocator,

    pub fn init(limit: u64, allocator: *mem.Allocator) error{OutOfMemory}!SoE {
        if (limit < 3)
            return SoE{
                .sieve = &empty,
                .alloc = allocator,
            };

        var bit_sz = (limit + 1) / 2 - 1;
        var q = bit_sz >> 6;
        var r = bit_sz & 0x3F;
        var sz = q + @boolToInt(r > 0);
        var sieve = try allocator.alloc(u64, sz);

        var i: usize = 0;
        while (i < q) : (i += 1)
            sieve[i] = all_u64bits_on;
        if (r > 0)
            sieve[q] = (@as(u64, 1) << @intCast(u6, r)) - 1;

        var bit: usize = 0;
        while (true) {
            while (sieve[bit >> 6] & @as(u64, 1) << @intCast(u6, bit & 0x3F) == 0)
                bit += 1;

            const p = 2 * bit + 3;
            q = p * p;
            if (q > limit)
                return SoE{
                    .sieve = sieve,
                    .alloc = allocator,
                };

            r = (q - 3) / 2;
            while (r < bit_sz) : (r += p)
                sieve[r >> 6] &= ~((@as(u64, 1)) << @intCast(u6, r & 0x3F));

            bit += 1;
        }
    }

    pub fn deinit(self: SoE) void {
        if (self.sieve.len > 0) {
            self.alloc.free(self.sieve);
        }
    }

    pub fn iterator(self: SoE) SoE_Iterator {
        return SoE_Iterator.init(self.sieve);
    }

    pub fn size(self: SoE) usize {
        var sz: usize = 1; // sieve doesn't include 2.
        for (self.sieve) |bits|
            sz += @popCount(u64, bits);
        return sz;
    }

    pub fn contains(self: SoE, n: u64) bool {
        if (n & 1 == 0)
            return n == 2
        else {
            const bit = (n - 3) / 2;
            const q = bit >> 6;
            const r = @intCast(u6, bit & 0x3F);
            return if (q >= self.sieve.len)
                false
            else
                self.sieve[q] & (@as(u64, 1) << r) != 0;
        }
    }
};

// Create an iterater object to enumerate primes we've generated.
const SoE_Iterator = struct {
    const Self = @This();

    start: u64,
    bits: u64,
    sieve: []const u64,

    pub fn init(sieve: []const u64) Self {
        return Self{
            .start = 0,
            .sieve = sieve,
            .bits = sieve[0],
        };
    }

    pub fn next(self: *Self) ?u64 {
        if (self.sieve.len == 0)
            return null;

        // start = 0 => first time, so yield 2.
        if (self.start == 0) {
            self.start = 3;
            return 2;
        }

        var x = self.bits;
        while (true) {
            if (x != 0) {
                const p = @ctz(u64, x) * 2 + self.start;
                x &= x - 1;
                self.bits = x;
                return p;
            } else {
                self.start += 128;
                self.sieve = self.sieve[1..];
                if (self.sieve.len == 0)
                    return null;
                x = self.sieve[0];
            }
        }
    }
};
```

**Output:**

```
There are 168 primes < 1000
    2    3    5    7   11   13   17   19   23   29
   31   37   41   43   47   53   59   61   67   71
   73   79   83   89   97  101  103  107  109  113
  127  131  137  139  149  151  157  163  167  173
  179  181  191  193  197  199  211  223  227  229
  233  239  241  251  257  263  269  271  277  281
  283  293  307  311  313  317  331  337  347  349
  353  359  367  373  379  383  389  397  401  409
  419  421  431  433  439  443  449  457  461  463
  467  479  487  491  499  503  509  521  523  541
  547  557  563  569  571  577  587  593  599  601
  607  613  617  619  631  641  643  647  653  659
  661  673  677  683  691  701  709  719  727  733
  739  743  751  757  761  769  773  787  797  809
  811  821  823  827  829  839  853  857  859  863
  877  881  883  887  907  911  919  929  937  941
  947  953  967  971  977  983  991  997
```

### Optimized version

```mw
const stdout = @import("std").io.getStdOut().writer();

const lim = 1000;
const n = lim - 2;

var primes: [n]?usize = undefined;

pub fn main() anyerror!void {
    var i: usize = 0;
    var m: usize = 0;

    while (i < n) : (i += 1) {
        primes[i] = i + 2;
    }

    i = 0;
    while (i < n) : (i += 1) {
        if (primes[i]) |prime| {
            m += 1;
            try stdout.print("{:5}", .{prime});
            if (m % 10 == 0) try stdout.print("\n", .{});
            var j: usize = i + prime;
            while (j < n) : (j += prime) {
                primes[j] = null;
            }
        }
    }
    try stdout.print("\n", .{});
}
```

**Output:**

```
$ zig run sieve.zig 
    2    3    5    7   11   13   17   19   23   29
   31   37   41   43   47   53   59   61   67   71
   73   79   83   89   97  101  103  107  109  113
  127  131  137  139  149  151  157  163  167  173
  179  181  191  193  197  199  211  223  227  229
  233  239  241  251  257  263  269  271  277  281
  283  293  307  311  313  317  331  337  347  349
  353  359  367  373  379  383  389  397  401  409
  419  421  431  433  439  443  449  457  461  463
  467  479  487  491  499  503  509  521  523  541
  547  557  563  569  571  577  587  593  599  601
  607  613  617  619  631  641  643  647  653  659
  661  673  677  683  691  701  709  719  727  733
  739  743  751  757  761  769  773  787  797  809
  811  821  823  827  829  839  853  857  859  863
  877  881  883  887  907  911  919  929  937  941
  947  953  967  971  977  983  991  997
```


## zkl

```mw
fcn sieve(limit){
   composite:=Data(limit+1).fill(1);  // bucket of bytes set to 1 (prime)
   (2).pump(limit.toFloat().sqrt()+1, Void,  // Void==no results, just loop
       composite.get, Void.Filter,  // if prime, zero multiples
      'wrap(n){ [n*n..limit,n].pump(Void,composite.set.fp1(0)) }); //composite[n*p]=0
   (2).filter(limit-1,composite.get); // bytes still 1 are prime
}
sieve(53).println();
```

The pump method is just a loop, passing results from action to action and collecting the results (ie a minimal state machine). Pumping to Void means don't collect. The Void.Filter action means if result.toBool() is False, skip else get the source input (pre any action) and pass that to the next action. Here, the first filter checks the table if src is prime, if so, the third action take the prime and does some side effects.

**Output:**

```
L(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53)
```

Retrieved from "

https://rosettacode.org/wiki/Sieve_of_Eratosthenes?oldid=404698

"
