---
title: "HAT-trie"
source: https://en.wikipedia.org/wiki/HAT-trie
domain: trie-structure
license: CC-BY-SA-4.0
tags: prefix trie, digital tree, ternary search tree, radix tree
fetched: 2026-07-02
---

# HAT-trie

The **HAT-trie** is a type of radix trie that uses array nodes to collect individual key–value pairs under radix nodes and hash buckets into an associative array. Unlike a simple hash table, HAT-tries store key–value in an ordered collection. The original inventors are Nikolas Askitis and Ranjan Sinha. Askitis & Zobel showed that building and accessing the HAT-trie key/value collection is considerably faster than other sorted access methods and is comparable to the array hash which is an unsorted collection. This is due to the cache-friendly nature of the data structure which attempts to group access to data in time and space into the 64 byte cache line size of the modern CPU.

## Description

A new HAT-trie starts out as a NULL pointer representing an empty node. The first added key allocates the smallest array node and copies into it the key/value pair, which becomes the first root of the trie. Each subsequent key/value pair is added to the initial array node until a maximum size is reached, after which the node is burst by re-distributing its keys into a hash bucket with new underlying array nodes, one for each occupied hash slot in the bucket. The hash bucket becomes the new root of the trie. The key strings are stored in the array nodes with a length encoding byte prefixed to the key value bytes. The value associated with each key can be stored either in-line alternating with the key strings, or placed in a second array, e.g., memory immediately after and joined to the array node.

Once the trie has grown into its first hash bucket node, the hash bucket distributes new keys according to a hash function of the key value into array nodes contained underneath the bucket node. Keys continue to be added until a maximum number of keys for a particular hash bucket node is reached. The bucket contents are then re-distributed into a new radix node according to the stored key value's first character, which replaces the hash bucket node as the trie root (e.g. see Burstsort). The existing keys and values contained in the hash bucket are each shortened by one character and placed under the new radix node in a set of new array nodes.

Sorted access to the collection is provided by enumerating keys into a cursor by branching down the radix trie to assemble the leading characters, ending at either a hash bucket or an array node. Pointers to the keys contained in the hash bucket or array node are assembled into an array that is part of the cursor for sorting. Since there is a maximum number of keys in a hash bucket or array node, there is a pre-set fixed limit to the size of the cursor at all points in time. After the keys for the hash bucket or array node are exhausted by get-next (or get-previous) (see Iterator) the cursor is moved into the next radix node entry and the process repeats.
