---
title: "module Enumerable (part 1/3)"
source: https://ruby-doc.org/core/Enumerable.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 1/3
---

# module Enumerable


## What’s Here¶ ↑

Module Enumerable provides methods that are useful to a collection class for:

- Querying
- Fetching
- Searching and Filtering
- Sorting
- Iterating
- And more.…

### Methods for Querying¶ ↑

These methods return information about the Enumerable other than the elements themselves:

- `member?` (aliased as `include?`): Returns `true` if `self == object`, `false` otherwise.
- `all?`: Returns `true` if all elements meet a specified criterion; `false` otherwise.
- `any?`: Returns `true` if any element meets a specified criterion; `false` otherwise.
- `none?`: Returns `true` if no element meets a specified criterion; `false` otherwise.
- `one?`: Returns `true` if exactly one element meets a specified criterion; `false` otherwise.
- `count`: Returns the count of elements, based on an argument or block criterion, if given.
- `tally`: Returns a new `Hash` containing the counts of occurrences of each element.

### Methods for Fetching¶ ↑

These methods return entries from the Enumerable, without modifying it:

*Leading, trailing, or all elements*:

- `to_a` (aliased as `entries`): Returns all elements.
- `first`: Returns the first element or leading elements.
- `take`: Returns a specified number of leading elements.
- `drop`: Returns a specified number of trailing elements.
- `take_while`: Returns leading elements as specified by the given block.
- `drop_while`: Returns trailing elements as specified by the given block.

*Minimum and maximum value elements*:

- `min`: Returns the elements whose values are smallest among the elements, as determined by `#<=>` or a given block.
- `max`: Returns the elements whose values are largest among the elements, as determined by `#<=>` or a given block.
- `minmax`: Returns a 2-element `Array` containing the smallest and largest elements.
- `min_by`: Returns the smallest element, as determined by the given block.
- `max_by`: Returns the largest element, as determined by the given block.
- `minmax_by`: Returns the smallest and largest elements, as determined by the given block.

*Groups, slices, and partitions*:

- `group_by`: Returns a `Hash` that partitions the elements into groups.
- `partition`: Returns elements partitioned into two new Arrays, as determined by the given block.
- `slice_after`: Returns a new `Enumerator` whose entries are a partition of `self`, based either on a given `object` or a given block.
- `slice_before`: Returns a new `Enumerator` whose entries are a partition of `self`, based either on a given `object` or a given block.
- `slice_when`: Returns a new `Enumerator` whose entries are a partition of `self` based on the given block.
- `chunk`: Returns elements organized into chunks as specified by the given block.
- `chunk_while`: Returns elements organized into chunks as specified by the given block.

### Methods for Searching and Filtering¶ ↑

These methods return elements that meet a specified criterion:

- `find` (aliased as `detect`): Returns an element selected by the block.
- `find_all` (aliased as `filter`, `select`): Returns elements selected by the block.
- `find_index`: Returns the index of an element selected by a given object or block.
- `reject`: Returns elements not rejected by the block.
- `uniq`: Returns elements that are not duplicates.

### Methods for Sorting¶ ↑

These methods return elements in sorted order:

- `sort`: Returns the elements, sorted by `#<=>` or the given block.
- `sort_by`: Returns the elements, sorted by the given block.

### Methods for Iterating¶ ↑

- `each_entry`: Calls the block with each successive element (slightly different from each).
- `each_with_index`: Calls the block with each successive element and its index.
- `each_with_object`: Calls the block with each successive element and a given object.
- `each_slice`: Calls the block with successive non-overlapping slices.
- `each_cons`: Calls the block with successive overlapping slices. (different from `each_slice`).
- `reverse_each`: Calls the block with each successive element, in reverse order.

### Other Methods¶ ↑

- `collect` (aliased as `map`): Returns objects returned by the block.
- `filter_map`: Returns truthy objects returned by the block.
- `flat_map` (aliased as `collect_concat`): Returns flattened objects returned by the block.
- `grep`: Returns elements selected by a given object or objects returned by a given block.
- `grep_v`: Returns elements selected by a given object or objects returned by a given block.
- `inject` (aliased as `reduce`): Returns the object formed by combining all elements.
- `sum`: Returns the sum of the elements, using method `+`.
- `zip`: Combines each element with elements from other enumerables; returns the n-tuples or calls the block with each.
- `cycle`: Calls the block with each element, cycling repeatedly.


## Usage¶ ↑

To use module Enumerable in a collection class:

- Include it:
  ```
include Enumerable
  ```
- Implement method `#each` which must yield successive elements of the collection. The method will be called by almost any Enumerable method.

Example:

```
class Foo
  include Enumerable
  def each
    yield 1
    yield 1, 2
    yield
  end
end
Foo.new.each_entry{ |element| p element }
```

Output:

```
1
[1, 2]
nil
```


## Enumerable in Ruby Classes¶ ↑

These Ruby core classes include (or extend) Enumerable:

- `ARGF`
- `Array`
- `Dir`
- `Enumerator`
- `ENV` (extends)
- `Hash`
- `IO`
- `Range`
- `Struct`

These Ruby standard library classes include Enumerable:

- CSV
- CSV::Table
- CSV::Row
- Set

Virtually all methods in Enumerable call method `#each` in the including class:

- `Hash#each` yields the next key-value pair as a 2-element `Array`.
- `Struct#each` yields the next name-value pair as a 2-element `Array`.
- For the other classes above, `#each` yields the next object from the collection.
