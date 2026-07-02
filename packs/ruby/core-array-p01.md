---
title: "class Array (part 1/4)"
source: https://ruby-doc.org/core/Array.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/4
---

# class Array

An Array object is an ordered, integer-indexed collection of objects, called *elements*; the object represents an array data structure.

An element may be any object (even another array); elements may be any mixture of objects of different types.

Important data structures that use arrays include:

- Coordinate vector.
- Matrix.
- Heap.
- Hash table.
- Deque (double-ended queue).
- Queue.
- Stack.

There are also array-like data structures:

- Associative array (see `Hash`).
- Directory (see `Dir`).
- Environment (see `ENV`).
- Set (see Set).
- String (see `String`).


## Array Indexes¶ ↑

Array indexing starts at 0, as in C or Java.

A non-negative index is an offset from the first element:

- Index 0 indicates the first element.
- Index 1 indicates the second element.
- …

A negative index is an offset, backwards, from the end of the array:

- Index -1 indicates the last element.
- Index -2 indicates the next-to-last element.
- …

### In-Range and Out-of-Range Indexes¶ ↑

A non-negative index is *in range* if and only if it is smaller than the size of the array. For a 3-element array:

- Indexes 0 through 2 are in range.
- Index 3 is out of range.

A negative index is *in range* if and only if its absolute value is not larger than the size of the array. For a 3-element array:

- Indexes -1 through -3 are in range.
- Index -4 is out of range.

### Effective Index¶ ↑

Although the effective index into an array is always an integer, some methods (both within class Array and elsewhere) accept one or more non-integer arguments that are integer-convertible objects.


## Creating Arrays¶ ↑

You can create an Array object explicitly with:

- An array literal:
  ```
[1, 'one', :one, [2, 'two', :two]]
  ```
- A %w or %W string-array Literal:
  ```
%w[foo bar baz] 
%w[1 % *]       
  ```
- A %i or %I symbol-array Literal:
  ```
%i[foo bar baz] 
%i[1 % *]       
  ```
- Method `Kernel#Array`:
  ```
Array(["a", "b"])             
Array(1..5)                   
Array(key: :value)            
Array(nil)                    
Array(1)                      
Array({:a => "a", :b => "b"}) 
  ```
- Method `Array.new`: Note that the last example above populates the array with references to the same object. This is recommended only in cases where that object is a natively immutable object such as a symbol, a numeric, `nil`, `true`, or `false`. Another way to create an array with various objects, using a block; this usage is safe for mutable objects such as hashes, strings or other arrays: Here is a way to create a multi-dimensional array:
  ```
Array.new               
Array.new(3)            
Array.new(4) {Hash.new} 
Array.new(3, true)      
  ```
  ```
Array.new(4) {|i| i.to_s } 
  ```
  ```
Array.new(3) {Array.new(3)}
  ```

A number of Ruby methods, both in the core and in the standard library, provide instance method `to_a`, which converts an object to an array.

- `ARGF#to_a`
- `Array#to_a`
- `Enumerable#to_a`
- `Hash#to_a`
- `MatchData#to_a`
- `NilClass#to_a`
- OptionParser#to_a
- `Range#to_a`
- Set#to_a
- `Struct#to_a`
- `Time#to_a`
- Benchmark::Tms#to_a
- CSV::Table#to_a
- `Enumerator::Lazy#to_a`
- Gem::List#to_a
- Gem::NameTuple#to_a
- Gem::Platform#to_a
- Gem::RequestSet::Lockfile::Tokenizer#to_a
- Gem::SourceList#to_a
- OpenSSL::X509::Extension#to_a
- OpenSSL::X509::Name#to_a
- Racc::ISet#to_a
- Rinda::RingFinger#to_a
- Ripper::Lexer::Elem#to_a
- `RubyVM::InstructionSequence#to_a`
- YAML::DBM#to_a


## Example Usage¶ ↑

In addition to the methods it mixes in through the `Enumerable` module, the `Array` class has proprietary methods for accessing, searching and otherwise manipulating arrays.

Some of the more common ones are illustrated below.


## Accessing Elements¶ ↑

Elements in an array can be retrieved using the `Array#[]` method. It can take a single integer argument (a numeric index), a pair of arguments (start and length) or a range. Negative indices start counting from the end, with -1 being the last element.

```
arr = [1, 2, 3, 4, 5, 6]
arr[2]    
arr[100]  
arr[-3]   
arr[2, 3] 
arr[1..4] 
arr[1..-3] 
```

Another way to access a particular array element is by using the `at` method

```
arr.at(0) 
```

The `slice` method works in an identical manner to `Array#[]`.

To raise an error for indices outside of the array bounds or else to provide a default value when that happens, you can use `fetch`.

```
arr = ['a', 'b', 'c', 'd', 'e', 'f']
arr.fetch(100) 
arr.fetch(100, "oops") 
```

The special methods `first` and `last` will return the first and last elements of an array, respectively.

```
arr.first 
arr.last  
```

To return the first `n` elements of an array, use `take`

```
arr.take(3) 
```

`drop` does the opposite of `take`, by returning the elements after `n` elements have been dropped:

```
arr.drop(3) 
```


## Obtaining Information about an `Array`¶ ↑

Arrays keep track of their own length at all times. To query an array about the number of elements it contains, use `length`, `count` or `size`.

```
browsers = ['Chrome', 'Firefox', 'Safari', 'Opera', 'IE']
browsers.length 
browsers.count 
```

To check whether an array contains any elements at all

```
browsers.empty? 
```

To check whether a particular item is included in the array

```
browsers.include?('Konqueror') 
```


## Adding Items to Arrays¶ ↑

Items can be added to the end of an array by using either `push` or `<<`

```
arr = [1, 2, 3, 4]
arr.push(5) 
arr << 6    
```

`unshift` will add a new item to the beginning of an array.

```
arr.unshift(0) 
```

With `insert` you can add a new element to an array at any position.

```
arr.insert(3, 'apple')  
```

Using the `insert` method, you can also insert multiple values at once:

```
arr.insert(3, 'orange', 'pear', 'grapefruit')
```


## Removing Items from an `Array`¶ ↑

The method `pop` removes the last element in an array and returns it:

```
arr =  [1, 2, 3, 4, 5, 6]
arr.pop 
arr 
```

To retrieve and at the same time remove the first item, use `shift`:

```
arr.shift 
arr 
```

To delete an element at a particular index:

```
arr.delete_at(2) 
arr 
```

To delete a particular element anywhere in an array, use `delete`:

```
arr = [1, 2, 2, 3]
arr.delete(2) 
arr 
```

A useful method if you need to remove `nil` values from an array is `compact`:

```
arr = ['foo', 0, nil, 'bar', 7, 'baz', nil]
arr.compact  
arr          
arr.compact! 
arr          
```

Another common need is to remove duplicate elements from an array.

It has the non-destructive `uniq`, and destructive method `uniq!`

```
arr = [2, 5, 6, 556, 6, 6, 8, 9, 0, 123, 556]
arr.uniq 
```


## Iterating over Arrays¶ ↑

Like all classes that include the `Enumerable` module, `Array` has an each method, which defines what elements should be iterated over and how. In case of Array’s `each`, all elements in the `Array` instance are yielded to the supplied block in sequence.

Note that this operation leaves the array unchanged.

```
arr = [1, 2, 3, 4, 5]
arr.each {|a| print a -= 10, " "}
```

Another sometimes useful iterator is `reverse_each` which will iterate over the elements in the array in reverse order.

```
words = %w[first second third fourth fifth sixth]
str = ""
words.reverse_each {|word| str += "#{word} "}
p str 
```

The `map` method can be used to create a new array based on the original array, but with the values modified by the supplied block:

```
arr.map {|a| 2*a}     
arr                   
arr.map! {|a| a**2}   
arr                   
```


## Selecting Items from an `Array`¶ ↑

Elements can be selected from an array according to criteria defined in a block. The selection can happen in a destructive or a non-destructive manner. While the destructive operations will modify the array they were called on, the non-destructive methods usually return a new array with the selected elements, but leave the original array unchanged.

### Non-destructive Selection¶ ↑

```
arr = [1, 2, 3, 4, 5, 6]
arr.select {|a| a > 3}       
arr.reject {|a| a < 3}       
arr.drop_while {|a| a < 4}   
arr                          
```

### Destructive Selection¶ ↑

`select!` and `reject!` are the corresponding destructive methods to `select` and `reject`

Similar to `select` vs. `reject`, `delete_if` and `keep_if` have the exact opposite result when supplied with the same block:

```
arr.delete_if {|a| a < 4}   
arr                         

arr = [1, 2, 3, 4, 5, 6]
arr.keep_if {|a| a < 4}   
arr                       
```
