---
title: "Sieve of Eratosthenes (part 12/21)"
source: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 12/21
---

## Julia

Started with 2 already in the array, and then test only for odd numbers and push the prime ones onto the array.

```mw
# Returns an array of positive prime numbers less than or equal to lim
function sieve(lim :: Int)
    if lim < 2 return [] end
    limi :: Int = (lim - 1) ÷ 2 # calculate the required array size
    isprime :: Array{Bool} = trues(limi)
    llimi :: Int = (isqrt(lim) - 1) ÷ 2 # and calculate maximum root prime index
    result :: Array{Int} = [2]  #Initial array
    for i in 1:limi
        if isprime[i]
            p = i + i + 1 # 2i + 1
            if i <= llimi
                for j = (p*p-1)>>>1:p:limi # quick shift/divide in case LLVM doesn't optimize divide by 2 away
                    isprime[j] = false
                end
            end
            push!(result, p)
        end
    end
    return result
end
```

Alternate version using `findall` to get all primes at once in the end

```mw
function sieve(n::Integer)
    primes = fill(true, n)
    primes[1] = false
    for p in 2:n
        primes[p] || continue
        primes[p .* (2:n÷p)] .= false
    end
    findall(primes)
end
```

At about 35 seconds for a range of a billion on my Intel Atom i5-Z8350 CPU at 1.92 GHz (single threaded) or about 70 CPU clock cycles per culling operation, the above examples are two of the very slowest ways to compute the Sieve of Eratosthenes over any kind of a reasonable range due to a couple of factors:

1. The output primes are extracted to a result array which takes time (and memory) to construct.
2. They use the naive "one huge memory array" method, which has poor memory access speed for larger ranges.

Even though the first uses an odds-only algorithm (not noted in the text as is a requirement of the task) that reduces the number of operations by a factor of about two and a half times, it is not faster than the second, which is not odds-only due to the second being set up to take advantage of the `findall` function to directly output the indices of the remaining true values as the found primes; the second is faster due to the first taking longer to push the found primes singly to the constructed array, whereas internally the second first creates the array to the size of the counted true values and then just fills it.

Also, the first uses more memory than necessary in one byte per `Bool` where using a `BitArray` as in the second reduces this by a factor of eight.

If one is going to "crib" the MatLab algorithm as above, one may as well do it using odds-only as per the MatLab built-in. The following alternate code improves on the "Alternate" example above by making it sieve odds-only and adjusting the result array contents after to suit:

```mw
function sieve2(n :: Int)
    ni = (n - 1) ÷ 2
    isprime = trues(ni)
    for i in 1:ni
        if isprime[i]
            j = 2i * (i + 1)
            if j > ni
                m = findall(isprime)
                map!((i::Int) -> 2i + 1, m, m)
                return pushfirst!(m, 2)
            else
                p = 2i + 1
                while j <= ni
                  isprime[j] = false
                  j += p
                end
            end
        end
    end
end
```

This takes less about 18.5 seconds or 36 CPU cycles per culling operation to find the primes to a billion, but that is still quite slow compared to what can be done below. Note that the result array needs to be created then copied, created by the `findall` function, then modified in place by the `map!` function to transform the indices to primes, and finally copied by the `pushfirst!` function to add the only even prime of two to the beginning, but these operations are quire fast. However, this still consumes a lot of memory, as in about 64 Megabytes for the sieve buffer and over 400 Megabytes for the result (8-byte Int's for 64 bit execution) to sieve to a billion, and culling the huge culling buffer that doesn't fit the CPU cache sizes is what makes it slow.

### Iterator Output

The creation of an output results array is not necessary if the purpose is just to scan across the resulting primes once, they can be output using an iterator (from a `BitArray`) as in the following odds-only code:

```mw
const Prime = UInt64

struct Primes
    rangei :: Int64
    primebits :: BitArray{1}
    function Primes(n :: Int64)
        if n < 3
          if n < 2 return new(-1, falses(0)) # no elements
          else return new((0, trues(0))) end # n = 2: meaning is 1 element of 2
        end
        limi :: Int = (n - 1) ÷ 2 # calculate the required array size
        isprimes :: BitArray = trues(limi)
        @inbounds(
        for i in 1:limi
            p = i + i + 1
            start = (p * p - 1) >>> 1 # shift/divide if LLVM doesn't optimize
            if start > limi
                return new(limi, isprimes)
            end
            if isprimes[i]
                for j in start:p:limi
                  isprimes[j] = false
                end
            end
        end)
    end
end

Base.eltype(::Type{Primes}) = Prime

function Base.length(P::Primes)::Int64
    if P.rangei < 0 return 0 end
    return 1 + count(P.primebits)
end

function Base.iterate(P::Primes, state::Int = 0)::
                                        Union{Tuple{Prime, Int}, Nothing}
    lmt = P.rangei
    if state > lmt return nothing end
    if state <= 0 return (UInt64(2), 1) end
    let
        prmbts = P.primebits
        i = state
        @inbounds(
        while i <= lmt && !prmbts[i] i += 1 end)
        if i > lmt return nothing end
        return (i + i + 1, i + 1)
    end
end
```

for which using the following code:

```mw
function bench()
  @time length(Primes(100)) # warm up JIT
#  println(@time count(x->true, Primes(1000000000))) # about 1.5 seconds slower counting over iteration
  println(@time length(Primes(1000000000)))
end
bench()
```

results in the following output:

**Output:**

```
  0.000031 seconds (3 allocations: 160 bytes)
 12.214533 seconds (4 allocations: 59.605 MiB, 0.42% gc time)
50847534
```

This reduces the CPU cycles per culling cycles to about 24.4, but it's still slow due to using the one largish array. Note that counting each iterated prime takes an additional about one and a half seconds, where if all that is required is the count of primes over a range the specialized length function is much faster.

### Page Segmented Algorithm

For any kind of reasonably large range such as a billion, a page segmented version should be used with the pages sized to the CPU caches for much better memory access times. As well, the following odds-only example uses a custom bit packing algorithm for a further two times speed-up, also reducing the memory allocation delays by reusing the sieve buffers when possible (usually possible):

```mw
const Prime = UInt64
const BasePrime = UInt32
const BasePrimesArray = Array{BasePrime,1}
const SieveBuffer = Array{UInt8,1}

# contains a lazy list of a secondary base primes arrays feed
# NOT thread safe; needs a Mutex gate to make it so...
abstract type BPAS end # stands in for BasePrimesArrays, not defined yet
mutable struct BasePrimesArrays <: BPAS
    thunk :: Union{Nothing,Function} # problem with efficiency - untyped function!!!!!!!!!
    value :: Union{Nothing,Tuple{BasePrimesArray, BPAS}}
    BasePrimesArrays(thunk::Function) = new(thunk)
end
Base.eltype(::Type{BasePrimesArrays}) = BasePrime
Base.IteratorSize(::Type{BasePrimesArrays}) = Base.SizeUnknown() # "infinite"...
function Base.iterate(BPAs::BasePrimesArrays, state::BasePrimesArrays = BPAs)
    if state.thunk !== nothing
        newvalue :: Union{Nothing,Tuple{BasePrimesArray, BasePrimesArrays}} =
            state.thunk() :: Union{Nothing,Tuple{BasePrimesArray
                                                 , BasePrimesArrays}}
        state.value = newvalue
        state.thunk = nothing
        return newvalue
    end
    state.value
end

# count the number of zero bits (primes) in a byte array,
# also works for part arrays/slices, best used as an `@view`...
function countComposites(cmpsts::AbstractArray{UInt8,1})
    foldl((a, b) -> a + count_zeros(b), cmpsts; init = 0)
end

# converts an entire sieved array of bytes into an array of UInt32 primes,
# to be used as a source of base primes...
function composites2BasePrimesArray(low::Prime, cmpsts::SieveBuffer)
    limiti = length(cmpsts) * 8
    len :: Int = countComposites(cmpsts)
    rslt :: BasePrimesArray = BasePrimesArray(undef, len)
    i :: Int = 0
    j :: Int = 1
    @inbounds(
    while i < limiti
        if cmpsts[i >>> 3 + 1] & (1 << (i & 7)) == 0
            rslt[j] = low + i + i
            j += 1
        end
        i += 1
    end)
    rslt
end

# sieving work done, based on low starting value for the given buffer and
# the given lazy list of base prime arrays...
function sieveComposites(low::Prime, buffer::Array{UInt8,1},
                                     bpas::BasePrimesArrays)
    lowi :: Int = (low - 3) ÷ 2
    len :: Int = length(buffer)
    limiti :: Int = len * 8 - 1
    nexti :: Int = lowi + limiti
    for bpa::BasePrimesArray in bpas
        for bp::BasePrime in bpa
            bpint :: Int = bp
            bpi :: Int = (bpint - 3) >>> 1
            starti :: Int = 2 * bpi * (bpi + 3) + 3
            starti >= nexti && return
            if starti >= lowi starti -= lowi
            else
                r :: Int = (lowi - starti) % bpint
                starti = r == 0 ? 0 : bpint - r
            end
            lmti :: Int = limiti - 40 * bpint
            @inbounds(
            if bpint <= (len >>> 2) starti <= lmti
                for i in 1:8
                    if starti > limiti break end
                    mask = convert(UInt8,1) << (starti & 7)
                    c = starti >>> 3 + 1
                    while c <= len
                        buffer[c] |= mask
                        c += bpint
                    end
                    starti += bpint
                end
            else
                c = starti
                while c <= limiti
                    buffer[c >>> 3 + 1] |= convert(UInt8,1) << (c & 7)
                    c += bpint
                end
            end)
        end
    end
    return
end

# starts the secondary base primes feed with minimum size in bits set to 4K...
# thus, for the first buffer primes up to 8293,
# the seeded primes easily cover it as 97 squared is 9409.
function makeBasePrimesArrays() :: BasePrimesArrays
    cmpsts :: SieveBuffer = Array{UInt8,1}(undef, 512)
    function nextelem(low::Prime, bpas::BasePrimesArrays) ::
                                    Tuple{BasePrimesArray, BasePrimesArrays}
        # calculate size so that the bit span is at least as big as the
        # maximum culling prime required, rounded up to minsizebits blocks...
        reqdsize :: Int = 2 + isqrt(1 + low)
        size :: Int = (reqdsize ÷ 4096 + 1) * 4096 ÷ 8 # size in bytes
        if size > length(cmpsts) cmpsts = Array{UInt8,1}(undef, size) end
        fill!(cmpsts, 0)
        sieveComposites(low, cmpsts, bpas)
        arr :: BasePrimesArray = composites2BasePrimesArray(low, cmpsts)
        next :: Prime = low + length(cmpsts) * 8 * 2
        arr, BasePrimesArrays(() -> nextelem(next, bpas))
    end
    # pre-seeding breaks recursive race,
    # as only known base primes used for first page...
    preseedarr :: BasePrimesArray = # pre-seed to 100, can sieve to 10,000...
        [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
        , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]
    nextfunc :: Function = () ->
        (nextelem(convert(Prime,101), makeBasePrimesArrays()))
    firstfunc :: Function = () -> (preseedarr, BasePrimesArrays(nextfunc))
    BasePrimesArrays(firstfunc)
end

# an iterator over successive sieved buffer composite arrays,
# returning a tuple of the value represented by the lowest possible prime
# in the sieved composites array and the array itself;
# the array has a 16 Kilobytes minimum size (CPU L1 cache), but
# will grow so that the bit span is larger than the
# maximum culling base prime required, possibly making it larger than
# the L1 cache for large ranges, but still reasonably efficient using
# the L2 cache: very efficient up to about 16e9 range;
# reasonably efficient to about 2.56e14 for two Megabyte L2 cache = > 1 week...
struct PrimesPages
    baseprimes :: BasePrimesArrays
    PrimesPages() = new(makeBasePrimesArrays())
end
Base.eltype(::Type{PrimesPages}) = SieveBuffer
Base.IteratorSize(::Type{PrimesPages}) = Base.SizeUnknown() # "infinite"...
function Base.iterate(PP::PrimesPages,
                      state :: Tuple{Prime,SieveBuffer} =
                            ( convert(Prime,3), Array{UInt8,1}(undef,16384) ))
    (low, cmpsts) = state
    # calculate size so that the bit span is at least as big as the
    # maximum culling prime required, rounded up to minsizebits blocks...
    reqdsize :: Int = 2 + isqrt(1 + low)
    size :: Int = (reqdsize ÷ 131072 + 1) * 131072 ÷ 8 # size in bytes
    if size > length(cmpsts) cmpsts = Array{UInt8,1}(undef, size) end
    fill!(cmpsts, 0)
    sieveComposites(low, cmpsts, PP.baseprimes)
    newlow :: Prime = low + length(cmpsts) * 8 * 2
    ( low, cmpsts ), ( newlow, cmpsts )
end

function countPrimesTo(range::Prime) :: Int64
    range < 3 && ((range < 2 && return 0) || return 1)
    count :: Int64 = 1
    for ( low, cmpsts ) in PrimesPages() # almost never exits!!!
        if low + length(cmpsts) * 8 * 2 > range
            lasti :: Int = (range - low) ÷ 2
            count += countComposites(@view cmpsts[1:lasti >>> 3])
            count += count_zeros(cmpsts[lasti >>> 3 + 1] |
                                 (0xFE << (lasti & 7)))
            return count
        end
        count += countComposites(cmpsts)
    end
    count
end

# iterator over primes from above page iterator;
# unless doing something special with individual primes, usually unnecessary;
# better to do manipulations based on the composites bit arrays...
# takes at least as long to enumerate the primes as sieve them...
mutable struct PrimesPaged
    primespages :: PrimesPages
    primespageiter :: Tuple{Tuple{Prime,SieveBuffer},Tuple{Prime,SieveBuffer}}
    PrimesPaged() = let PP = PrimesPages(); new(PP, Base.iterate(PP)) end
end
Base.eltype(::Type{PrimesPaged}) = Prime
Base.IteratorSize(::Type{PrimesPaged}) = Base.SizeUnknown() # "infinite"...
function Base.iterate(PP::PrimesPaged, state::Int = -1 )
    state < 0 && return Prime(2), 0
    (low, cmpsts) = PP.primespageiter[1]
    len = length(cmpsts) * 8
    @inbounds(
    while state < len && cmpsts[state >>> 3 + 1] &
                         (UInt8(1) << (state & 7)) != 0
        state += 1
    end)
    if state >= len
        PP.primespageiter = Base.iterate(PP.primespages, PP.primespageiter[2])
        return Base.iterate(PP, 0)
    end
    low + state + state, state + 1
end
```

When tested with the following code:

```mw
function bench()
    print("( ")
    for p in PrimesPaged() p > 100 && break; print(p, " ") end
    println(")")
    countPrimesTo(Prime(100)) # warm up JIT
#=
    println(@time let count = 0
                      for p in PrimesPaged()
                          p > 1000000000 && break
                          count += 1
                      end; count end) # much slower counting over iteration
=#
    println(@time countPrimesTo(Prime(1000000000)))
end
bench()
```

it produces the following:

**Output:**

```
( 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 )
  1.947145 seconds (59 allocations: 39.078 KiB)
50847534
```

Note that "the slow way" as commented out in the code takes an extra about 4.85 seconds to count the primes to a billion, or longer to enumerate the primes than to cull the composites; this makes further work in making this yet faster pointless unless techniques such as the one used here to count the number of found primes by just counting the un-cancelled bit representations in the sieved sieve buffers are used.

This takes about 1.9 seconds to count the primes to a billion (using the fast technique), or about 3.75 clock cycles per culling operation, which is reasonably fast; this is almost 20 times faster than the first naive sieves. As written, the algorithm maintains its efficiency up to about 16 billion and then slows down as the buffer size increases beyond the CPU L1 cache size into the L2 cache size such that it takes about 436.8 seconds to sieve to 100 billion instead of the expected about 300 seconds; however, an extra feature of "double buffered sieving" could be added so that the buffer is sieved in L1 cache slices followed by a final sweep of the entire buffer by the few remaining cull operations that use the larger primes for only a slight reduction in average cycles per cull up to a range of about 2.56e14 (for this CPU). For really large ranges above that, another sieving technique known as the "bucket sieve" that sorts the culling operations by page so that processing time is not expended for values that don't "hit" a given page can be used for only a slight additional reduction in efficiency.

Additionally, maximal wheel factorization can reduce the time by about a factor of four, plus multi-processing where the work is shared across the CPU cores can produce a further speed-up by the factor of the number of cores (only three times on this four-core machine due to the clock speed reducing to 75% of the rate when all cores are used), for an additional about 12 times speed-up for this CPU. These improvements are just slightly too complex to post here.

However, even the version posted shows that the naive "one huge array" implementations should never be used for sieving ranges of over a few million, and that Julia can come very close to the speed of the fastest languages such as C/C++ for the same algorithm.

### Functional Algorithm

One of the best simple purely functional Sieve of Eratosthenes algorithms is the infinite tree folding sequence algorithm as implemented in Haskell. As Julia does not have a standard LazyList implementation or library and as a full memoizing lazy list is not required for this algorithm, the following odds-only code implements the rudiments of a Co-Inductive Stream (CIS) in its implementation:

```mw
const Thunk = Function # can't define other than as a generalized Function

struct CIS{T}
    head :: T
    tail :: Thunk # produces the next CIS{T}
    CIS{T}(head :: T, tail :: Thunk) where T = new(head, tail)
end
Base.eltype(::Type{CIS{T}}) where T = T
Base.IteratorSize(::Type{CIS{T}}) where T = Base.SizeUnknown()
function Base.iterate(C::CIS{T}, state = C) :: Tuple{T, CIS{T}} where T
    state.head, state.tail()
end

function treefoldingprimes()::CIS{Int}
    function merge(xs::CIS{Int}, ys::CIS{Int})::CIS{Int}
        x = xs.head; y = ys.head
        if x < y CIS{Int}(x, () -> merge(xs.tail(), ys))
        elseif y < x CIS{Int}(y, () -> merge(xs, ys.tail()))
        else CIS{Int}(x, () -> merge(xs.tail(), ys.tail())) end
    end
    function pmultiples(p::Int)::CIS{Int}
        adv :: Int = p + p
        next(c::Int)::CIS{Int} = CIS{Int}(c, () -> next(c + adv)); next(p * p)
    end
    function allmultiples(ps::CIS{Int})::CIS{CIS{Int}}
        CIS{CIS{Int}}(pmultiples(ps.head), () -> allmultiples(ps.tail()))
    end
    function pairs(css :: CIS{CIS{Int}})::CIS{CIS{Int}}
        nextcss = css.tail()
        CIS{CIS{Int}}(merge(css.head, nextcss.head), ()->pairs(nextcss.tail()))
    end
    function composites(css :: CIS{CIS{Int}})::CIS{Int}
        CIS{Int}(css.head.head, ()-> merge(css.head.tail(),
                                            css.tail() |> pairs |> composites))
    end
    function minusat(n::Int, cs::CIS{Int})::CIS{Int}
        if n < cs.head CIS{Int}(n, () -> minusat(n + 2, cs))
        else minusat(n + 2, cs.tail()) end
    end
    oddprimes()::CIS{Int} = CIS{Int}(3, () -> minusat(5, oddprimes()
                                        |> allmultiples |> composites))
    CIS{Int}(2, () -> oddprimes())
end
```

when tested with the following:

```mw
@time let count = 0; for p in treefoldingprimes() p > 1000000 && break; count += 1 end; count end
```

it outputs the following:

**Output:**

```
  1.791058 seconds (10.23 M allocations: 290.862 MiB, 3.64% gc time)
78498
```

At about 1.8 seconds or 4000 cycles per culling operation to calculate the number of primes up to a million, this is very slow, but that is not the fault of Julia but rather just that purely functional incremental Sieve of Eratosthenes implementations are much slower than those using mutable arrays and are only useful over quite limited ranges of a few million. For one thing, incremental algorithms have O(n log n log log n) asymptotic execution complexity rather than O(n log log n) (an extra log n factor) and for another the constant execution overhead is much larger in creating (and garbage collecting) elements in the sequences.

The time for this algorithm is quite comparable to as implemented in other functional languages such as F# and actually faster than implementing the same algorithm in C/C++, but slower than as implemented in purely functional languages such as Haskell or even in only partly functional languages such as Kotlin by a factor of ten or more; this is due to those languages having specialized memory allocation that is very fast at allocating small amounts of memory per allocation as is often a requirement of functional programming. The majority of the time spent for this algorithm is spent allocating memory, and if future versions of Julia are to be of better use in purely functional programming, improvements need to be made to the memory allocation.

### Infinite (Mutable) Iterator Using (Mutable) Dictionary

To gain some extra speed above the purely functional algorithm above, the Python'ish version as a mutable iterator embedding a mutable standard base Dictionary can be used. The following version uses a secondary delayed injection stream of "base" primes defined recursively to provide the successions of composite values in the Dictionary to be used for sieving:

```mw
const Prime = UInt64
abstract type PrimesDictAbstract end # used for forward reference
mutable struct PrimesDict <: PrimesDictAbstract
    sieve :: Dict{Prime,Prime}
    baseprimes :: PrimesDictAbstract
    lastbaseprime :: Prime
    q :: Prime
    PrimesDict() = new(Dict())
end
Base.eltype(::Type{PrimesDict}) = Prime
Base.IteratorSize(::Type{PrimesDict}) = Base.SizeUnknown() # "infinite"...
function Base.iterate(PD::PrimesDict, state::Prime = Prime(0) )
    if state < 1
        PD.baseprimes = PrimesDict()
        PD.lastbaseprime = Prime(3)
        PD.q = Prime(9)
        return Prime(2), Prime(1)
    end
    dict = PD.sieve
    while true
        state += 2
        if !haskey(dict, state)
            state < PD.q && return state, state
            p = PD.lastbaseprime # now, state = PD.q in all cases
            adv = p + p # since state is at PD.q, advance to next
            dict[state + adv] = adv # adds base prime composite stream
            # following initializes secondary base strea first time
            p <= 3 && Base.iterate(PD.baseprimes)
            p = Base.iterate(PD.baseprimes, p)[1] # next base prime
            PD.lastbaseprime = p
            PD.q = p * p
        else # advance hit composite in dictionary...
            adv = pop!(dict, state)
            next = state + adv
            while haskey(dict, next) next += adv end
            dict[next] = adv # past other composite hits in dictionary
        end
    end
end
```

The above version can be used and tested with similar code as for the functional version, but is about ten times faster at about 400 CPU clock cycles per culling operation, meaning it has a practical range ten times larger although it still has a O(n (log n) (log log n)) asymptotic performance complexity; for larger ranges such as sieving to a billion or more, this is still over a hundred times slower than the page segmented version using a page segmented sieving array.


## K

Works with NGN/K

```mw
border:100
// 2_ to filter 0 and 1
sieve::2_!border
limitarray:2_!_%border
// add until higher than border with {x<border}{x+dummy}\dummy 
multiples:{ dummy::x; {x<border}{x+dummy}\dummy }'limitarray
// filter out with sieve@&~sieve=x
// 1_dummy2 to filter out first number 2,3, etc.
// noout: to surpress output
noout:{dummy2:x; {sieve::sieve@&~sieve=x}'1_dummy2}'multiples
sieve
```

### Odds only

```mw
border:10000
// 2_ to filter 0 and 1
sieve::2_!border
// filter out odds with function
odds:{~0=2!x}
limitarray: 2_!_%border
limitarray: 2,limitarray@&odds'limitarray
// add until higher than border with {x<border}{x+dummy}\dummy 
multiples:{ dummy::x; {x<border}{x+dummy}\dummy }'limitarray
// filter out with sieve@&~sieve=x
// 1_dummy2 to filter out first number 2,3, etc.
// noout: to surpress output
noout:{dummy2:x; {sieve::sieve@&~sieve=x}'1_dummy2}'multiples
sieve
```

### Build-in function

```mw
`pri 100
```


## Klingphix

```mw
include ..\Utilitys.tlhy

%limit %i
1000 !limit
( 1 $limit ) sequence

( 2 $limit sqrt int ) [ !i $i get [ ( 2 $limit 1 - $i / int ) [ $i * false swap set ] for ] if ] for
( 1 $limit false ) remove
pstack

"Press ENTER to end " input
```


## Kotlin

```mw
import kotlin.math.sqrt

fun sieve(max: Int): List<Int> {
    val xs = (2..max).toMutableList()
    val limit = sqrt(max.toDouble()).toInt()
    for (x in 2..limit) xs -= x * x..max step x
    return xs
}

fun main(args: Array<String>) {
    println(sieve(100))
}
```

**Output:**

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

**Alternative much faster odds-only version that outputs an enumeration**

The above version is quite slow for a lot of reasons: It includes even number culling even though those will be eliminated on the first pass; It uses a list rather than an array to do the composite culling (both of the above reasons also meaning it takes more memory); It uses enumerations (for..in) to implement loops at a execution time cost per loop. It also consumes more memory in the final result output as another list.

The following code overcomes most of those problems: It only culls odd composites; it culls a bit-packed primitive array (also saving memory); It uses tailcall recursive functions for the loops, which are compiled into simple loops. It also outputs the results as an enumeration, which isn't fast but does not consume any more memory than the culling array. In this way, the program is only limited in sieving range by the maximum size limit of the culling array, although as it grows larger than the CPU cache sizes, it loses greatly in speed; however, that doesn't matter so much if just enumerating the results.

```mw
fun primesOdds(rng: Int): Iterable<Int> {
    val topi = (rng - 3) shr 1
    val lstw = topi shr 5
    val sqrtndx = (Math.sqrt(rng.toDouble()).toInt() - 3) shr 1
    val cmpsts = IntArray(lstw + 1)

    tailrec fun testloop(i: Int) {
        if (i <= sqrtndx) {
            if (cmpsts[i shr 5] and (1 shl (i and 31)) == 0) {
                val p = i + i + 3
                tailrec fun cullp(j: Int) {
                    if (j <= topi) {
                        cmpsts[j shr 5] = cmpsts[j shr 5] or (1 shl (j and 31))
                        cullp(j + p)
                    }
                }
                cullp((p * p - 3) shr 1)
            }
            testloop(i + 1)
        }
    }

    tailrec fun test(i: Int): Int {
        return if (i <= topi && cmpsts[i shr 5] and (1 shl (i and 31)) != 0) {
            test(i + 1)
        } else {
            i
        }
    }

    testloop(0)

    val iter = object : IntIterator() {
        var i = -1
        override fun nextInt(): Int {
            val oi = i
            i = test(i + 1)
            return if (oi < 0) 2 else oi + oi + 3
        }
        override fun hasNext() = i < topi
    }
    return Iterable { -> iter }
}

fun main(args: Array<String>) {
    primesOdds(100).forEach { print("$it ") }
    println()
    println(primesOdds(1000000).count())
}
```

**Output:**

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
78498
```

**Concise Functional Versions**

Ah, one might say, for such a trivial range one writes for conciseness and not for speed. Well, I say, one can still save memory and some time using odds-only and a bit-packed array, but write very clear and concise (but slower) code using nothing but higher order functions and function calling. The following code using such techniques can use the same "main" function for the same output but is about two times slower, mostly due to the extra time spent making (nested) function calls, including the function calls necessary for enumeration. Note that the effect of using the "(l .. h).forEach { .. }" is the same as the "for i in l .. h { .. }" as both use an iteration across the range but the second is just syntax sugar to make it look more imperative:

```mw
fun primesOdds(rng: Int): Iterable<Int> {
    val topi = (rng - 3) / 2 //convert to nearest index
    val size = topi / 32 + 1 //word size to include index
    val sqrtndx = (Math.sqrt(rng.toDouble()).toInt() - 3) / 2
    val cmpsts = IntArray(size)
    fun is_p(i: Int) = cmpsts[i shr 5] and (1 shl (i and 0x1F)) == 0
    fun cull(i: Int) { cmpsts[i shr 5] = cmpsts[i shr 5] or (1 shl (i and 0x1F)) }
    fun cullp(p: Int) = (((p * p - 3) / 2 .. topi).step(p)).forEach { cull(it) }
    (0 .. sqrtndx).filter { is_p(it) }.forEach { cullp(it + it + 3) }
    fun i2p(i: Int) = if (i < 0) 2 else i + i + 3
    val orng = (-1 .. topi).filter { it < 0 || is_p(it) }.map { i2p(it) }
    return Iterable { -> orng.iterator() }
}
```

The trouble with the above version is that, at least for Kotlin version 1.0, the ".filter" and ".map" extension functions for Iterable<Int> create Java "ArrayList"'s as their output (which are wrapped to return the Kotlin "List<Int>" interface), thus take a considerable amount of memory worse than the first version (using an ArrayList to store the resulting primes), since as the calculations are chained to ".map", require a second ArrayList of up to the same size while the mapping is being done. The following version uses Sequences , which aren't backed by any permanent structure, but it is another small factor slower due to the nested function calls:

```mw
fun primesOdds(rng: Int): Iterable<Int> {
    val topi = (rng - 3) / 2 //convert to nearest index
    val size = topi / 32 + 1 //word size to include index
    val sqrtndx = (Math.sqrt(rng.toDouble()).toInt() - 3) / 2
    val cmpsts = IntArray(size)
    fun is_p(i: Int) = cmpsts[i shr 5] and (1 shl (i and 0x1F)) == 0
    fun cull(i: Int) { cmpsts[i shr 5] = cmpsts[i shr 5] or (1 shl (i and 0x1F)) }
    fun iseq(high: Int, low: Int = 0, stp: Int = 1) =
            Sequence { (low .. high step(stp)).iterator() }
    fun cullp(p: Int) = iseq(topi, (p * p - 3) / 2, p).forEach { cull(it) }
    iseq(sqrtndx).filter { is_p(it) }.forEach { cullp(it + it + 3) }
    fun i2p(i: Int) = if (i < 0) 2 else i + i + 3
    val oseq = iseq(topi, -1).filter { it < 0 || is_p(it) }.map { i2p(it) }
    return Iterable { -> oseq.iterator() }
}
```

### Unbounded Versions

**An incremental odds-only sieve outputting a sequence (iterator)**

The following Sieve of Eratosthenes is not purely functional in that it uses a Mutable HashMap to store the state of succeeding composite numbers to be skipped over, but embodies the principles of an incremental implementation of the Sieve of Eratosthenes sieving odds-only and is faster than most incremental sieves due to using mutability. As with the fastest of this kind of sieve, it uses a delayed secondary primes feed as a source of base primes to generate the composite number progressions. The code as follows:

```mw
fun primesHM(): Sequence<Int> = sequence {
    yield(2)
    fun oddprms(): Sequence<Int> = sequence {
        yield(3); yield(5) // need at least 2 for initialization
        val hm = HashMap<Int,Int>()
        hm.put(9, 6)
        val bps = oddprms().iterator(); bps.next(); bps.next() // skip past 5
        yieldAll(generateSequence(SieveState(7, 5, 25)) {
            ss ->
                var n = ss.n; var q = ss.q
                n += 2
                while ( n >= q || hm.containsKey(n)) {
                    if (n >= q) {
                        val inc = ss.bp shl 1
                        hm.put(n + inc, inc)
                        val bp = bps.next(); ss.bp = bp; q = bp * bp
                    }
                    else {
                        val inc = hm.remove(n)!!
                        var next = n + inc
                        while (hm.containsKey(next)) {
                            next += inc
                        }
                        hm.put(next, inc)
                    }
                    n += 2
                }
                ss.n = n; ss.q = q
                ss
        }.map { it.n })
    }
    yieldAll(oddprms())
}
```

At about 370 clock cycles per culling operation (about 3,800 cycles per prime) on my tablet class Intel CPU, this is not blazing fast but adequate for ranges of a few millions to a hundred million and thus fine for doing things like solving Euler problems. For instance, Euler Problem 10 of summing the primes to two million can be done with the following "one-liner":

```mw
primesHM().takeWhile { it <= 2_000_000 }.map { it.toLong() }.sum()
```

to output the correct answer of the following in about 270 milliseconds for my Intel x5-Z8350 at 1.92 Gigahertz:

**Output:**

```
142913828922
```

**A purely functional Incremental Sieve of Eratosthenes that outputs a sequence (iterator)**

Following is a Kotlin implementation of the Tree Folding Incremental Sieve of Eratosthenes from an adaptation of the algorithm by Richard Bird. It is based on lazy lists, but in fact the memoization (and cost in execution time) of a lazy list is not required and the following code uses a "roll-your-own" implementation of a Co-Inductive Stream CIS). The final output is as a Sequence for convenience in using it. The code is written as purely function in that no mutation is used:

Translation of

:

Haskell

```mw
data class CIS<T>(val head: T, val tailf: () -> CIS<T>) {
  fun toSequence() = generateSequence(this) { it.tailf() } .map { it.head }
}

fun primes(): Sequence<Int> {
  fun merge(a: CIS<Int>, b: CIS<Int>): CIS<Int> {
    val ahd = a.head; val bhd = b.head
    if (ahd > bhd) return CIS(bhd) { ->merge(a, b.tailf()) }
    if (ahd < bhd) return CIS(ahd) { ->merge(a.tailf(), b) }
    return CIS(ahd) { ->merge(a.tailf(), b.tailf()) }
  }
  fun bpmults(p: Int): CIS<Int> {
    val inc = p + p
    fun mlts(c: Int): CIS<Int> = CIS(c) { ->mlts(c + inc) }
    return mlts(p * p)
  }
  fun allmults(ps: CIS<Int>): CIS<CIS<Int>> = CIS(bpmults(ps.head)) { allmults(ps.tailf()) }
  fun pairs(css: CIS<CIS<Int>>): CIS<CIS<Int>> {
    val xs = css.head; val yss = css.tailf(); val ys = yss.head
    return CIS(merge(xs, ys)) { ->pairs(yss.tailf()) }
  }
  fun union(css: CIS<CIS<Int>>): CIS<Int> {
    val xs = css.head
    return CIS(xs.head) { -> merge(xs.tailf(), union(pairs(css.tailf()))) }
  }
  tailrec fun minus(n: Int, cs: CIS<Int>): CIS<Int> =
    if (n >= cs.head) minus(n + 2, cs.tailf()) else CIS(n) { ->minus(n + 2, cs) }    
  fun oddprms(): CIS<Int> = CIS(3) { -> CIS(5) { ->minus(7, union(allmults(oddprms()))) } }
  return CIS(2) { ->oddprms() } .toSequence()
}

fun main(args: Array<String>) {
  val limit = 1000000
  val strt = System.currentTimeMillis()
  println(primes().takeWhile { it <= limit } .count())
  val stop = System.currentTimeMillis()
  println("Took ${stop - strt} milliseconds.")
}
```

The code is about five times slower than the more imperative hash table based version immediately above due to the costs of the extra levels of function calls in the functional style. The Haskell version from which this is derived is much faster due to the extensive optimizations it does to do with function/closure "lifting" as well as a Garbage Collector specifically tuned for functional code.

**An unbounded Page Segmented Sieve of Eratosthenes that can output a sequence (iterator)**

The very fastest implementations of a primes sieve are all based on bit-packed mutable arrays which can be made unbounded by setting them up so that they are a succession of sieved bit-packed arrays that have been culled of composites. The following code is an odds=only implementation that, again, uses a secondary feed of base primes that is only expanded as necessary (in this case memoized by a rudimentary lazy list structure to avoid recalculation for every base primes sweep per page segment):

```mw
internal typealias Prime = Long
internal typealias BasePrime = Int
internal typealias BasePrimeArray = IntArray
internal typealias SieveBuffer = ByteArray

// contains a lazy list of a secondary base prime arrays feed
internal data class BasePrimeArrays(val arr: BasePrimeArray,
                                     val rest: Lazy<BasePrimeArrays?>)
                                                : Sequence<BasePrimeArray> {
    override fun iterator() =
        generateSequence(this) { it.rest.value }
            .map { it.arr }.iterator()
}

// count the number of zero bits (primes) in a byte array,
fun countComposites(cmpsts: SieveBuffer): Int {
    var cnt = 0
    for (b in cmpsts) {
        cnt += java.lang.Integer.bitCount(b.toInt().and(0xFF))
    }
    return cmpsts.size.shl(3) - cnt
}

// converts an entire sieved array of bytes into an array of UInt32 primes,
// to be used as a source of base primes...
fun composites2BasePrimeArray(low: Int, cmpsts: SieveBuffer)
                                                            : BasePrimeArray {
    val lmti = cmpsts.size.shl(3)
    val len = countComposites(cmpsts)
    val rslt = BasePrimeArray(len)
    var j = 0
    for (i in 0 until lmti) {
        if (cmpsts[i.shr(3)].toInt() and 1.shl(i and 7) == 0) {
            rslt[j] = low + i + i; j++
        }
    }
    return rslt
}

// do sieving work based on low starting value for the given buffer and
// the given lazy list of base prime arrays...
fun sieveComposites(low: Prime, buffer: SieveBuffer,
                             bpas: Sequence<BasePrimeArray>) {
    val lowi = (low - 3L).shr(1)
    val len = buffer.size
    val lmti = len.shl(3)
    val nxti = lowi + lmti.toLong()
    for (bpa in bpas) {
        for (bp in bpa) {
            val bpi = (bp - 3).shr(1).toLong()
            var strti = (bpi * (bpi + 3L)).shl(1) + 3L
            if (strti >= nxti) return
            val s0 =
                if (strti >= lowi) (strti - lowi).toInt()
                else {
                    val r = (lowi - strti) % bp.toLong()
                    if (r.toInt() == 0) 0 else bp - r.toInt()
                }
            if (bp <= len.shr(3) && s0 <= lmti - bp.shl(6)) {
                val slmti = minOf(lmti, s0 + bp.shl(3))
                tailrec fun mods(s: Int) {
                    if (s < slmti) {
                        val msk = 1.shl(s and 7)
                        tailrec fun cull(c: Int) {
                            if (c < len) {
                                buffer[c] = (buffer[c].toInt() or msk).toByte()
                                cull(c + bp)
                            }
                        }
                        cull(s.shr(3)); mods(s + bp)
                    }
                }
                mods(s0)
            }
            else {
                tailrec fun cull(c: Int) {
                    if (c < lmti) {
                        val w = c.shr(3)
                        buffer[w] = (buffer[w].toInt() or 1.shl(c and 7)).toByte()
                        cull(c + bp)
                    }
                }
                cull(s0)
            }
        }
    } 
}

// starts the secondary base primes feed with minimum size in bits set to 4K...
// thus, for the first buffer primes up to 8293,
// the seeded primes easily cover it as 97 squared is 9409...
fun makeBasePrimeArrays(): Sequence<BasePrimeArray> {
    var cmpsts = SieveBuffer(512)
    fun nextelem(low: Int, bpas: Sequence<BasePrimeArray>): BasePrimeArrays {
        // calculate size so that the bit span is at least as big as the
        // maximum culling prime required, rounded up to minsizebits blocks...
        val rqdsz = 2 + Math.sqrt((1 + low).toDouble()).toInt()
        val sz = (rqdsz.shr(12) + 1).shl(9) // size iin bytes
        if (sz > cmpsts.size) cmpsts = SieveBuffer(sz)
        cmpsts.fill(0)
        sieveComposites(low.toLong(), cmpsts, bpas)
        val arr = composites2BasePrimeArray(low, cmpsts)
        val nxt = low + cmpsts.size.shl(4)
        return BasePrimeArrays(arr, lazy { ->nextelem(nxt, bpas) })
    }
    // pre-seeding breaks recursive race,
    // as only known base primes used for first page...
    var preseedarr = intArrayOf( // pre-seed to 100, can sieve to 10,000...
        3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
        , 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 )
    return BasePrimeArrays(preseedarr, lazy {->nextelem(101, makeBasePrimeArrays())})
}

// a seqence over successive sieved buffer composite arrays,
// returning a tuple of the value represented by the lowest possible prime
// in the sieved composites array and the array itself;
// the array has a 16 Kilobytes minimum size (CPU L1 cache), but
// will grow so that the bit span is larger than the
// maximum culling base prime required, possibly making it larger than
// the L1 cache for large ranges, but still reasonably efficient using
// the L2 cache: very efficient up to about 16e9 range;
// reasonably efficient to about 2.56e14 for two Megabyte L2 cache = > 1 day...
fun makeSievePages(): Sequence<Pair<Prime,SieveBuffer>> {
    val bpas = makeBasePrimeArrays() // secondary source of base prime arrays
    fun init(): SieveBuffer {
        val c = SieveBuffer(16384); sieveComposites(3L, c, bpas); return c }
    return generateSequence(Pair(3L, init())) {
        (low, cmpsts) ->
            // calculate size so that the bit span is at least as big as the
            // max culling prime required, rounded up to minsizebits blocks...
            val rqdsz = 2 + Math.sqrt((1 + low).toDouble()).toInt()
            val sz = (rqdsz.shr(17) + 1).shl(14) // size iin bytes
            val ncmpsts = if (sz > cmpsts.size) SieveBuffer(sz) else cmpsts
            ncmpsts.fill(0)
            val nlow = low + ncmpsts.size.toLong().shl(4)
            sieveComposites(nlow, ncmpsts, bpas)
            Pair(nlow, ncmpsts)
    }
}

fun countPrimesTo(range: Prime): Prime {
    if (range < 3) { if (range < 2) return 0 else return 1 }
    var count = 1L
    for ((low,cmpsts) in makeSievePages()) {
        if (low + cmpsts.size.shl(4) > range) {
            val lsti = (range - low).shr(1).toInt()
            val lstw = lsti.shr(3)
            val msk = -2.shl(lsti.and(7))
            count += 32 + lstw.shl(3)
            for (i in 0 until lstw)
                count -= java.lang.Integer.bitCount(cmpsts[i].toInt().and(0xFF))
            count -= java.lang.Integer.bitCount(cmpsts[lstw].toInt().or(msk))
            break
        } else {
            count += countComposites(cmpsts)
        }
    }
    return count
}

// sequence over primes from above page iterator;
// unless doing something special with individual primes, usually unnecessary;
// better to do manipulations based on the composites bit arrays...
// takes at least as long to enumerate the primes as sieve them...
fun primesPaged(): Sequence<Prime> = sequence {
    yield(2L)
    for ((low,cmpsts) in makeSievePages()) {
        val szbts = cmpsts.size.shl(3)
        for (i in 0 until szbts) {
            if (cmpsts[i.shr(3)].toInt() and 1.shl(i and 7) != 0) continue
            yield(low + i.shl(1).toLong())
        }
    }
}
```

For this implementation, counting the primes to a million is trivial at about 15 milliseconds on the same CPU as above, or almost too short to count.

It shows its speed in solving the Euler Problem 10 above about five times faster at about 50 milliseconds to give the same output:

It can sum the primes to 200 million or a hundred times the range in just over three seconds.

It finds the count of primes to a billion in about 16 seconds or just about 1000 times slower than to sum the primes to a range 1000 times less for an almost linear response to range as it should be.

However, much of the time (about two thirds) is spent iterating over the results rather than doing the actual work of sieving; for this sort of problem such as counting, finding the nth prime, finding occurrences of maximum prime gaps, etc., one should really use specialized function that directly manipulate the output sieve arrays. Such a function is provided by the `countPrimeTo` function, which can count the primes to a billion (50847534) in about 5.65 seconds, or about 10.6 clock cycles per culling operation or about 210 cycles per prime.

Kotlin isn't really fast even as compared to other virtual machine languages such as C# and F# on CLI but that is mostly due to limitations of the Java Virtual Machine (JVM) as to speed of generated Just In Time (JIT) compilation, handling of primitive number operations, enforced array bounds checks, etc. It will always be much slower than native code producing compilers and the (experimental) native compiler for Kotlin still isn't up to speed (pun intended), producing code that is many times slower than the code run on the JVM (December 2018).
