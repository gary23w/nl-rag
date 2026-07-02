---
title: "Linear hashing"
source: https://en.wikipedia.org/wiki/Linear_hashing
domain: dynamic-hash-index
license: CC-BY-SA-4.0
tags: extendible hashing, linear hashing, spiral hashing, dynamic hash index
fetched: 2026-07-02
---

# Linear hashing

**Linear hashing** (**LH**) is a dynamic data structure which implements a hash table and grows or shrinks one bucket at a time. It was invented by Witold Litwin in 1980. It has been analyzed by Baeza-Yates and Soza-Pollman. It is the first in a number of schemes known as dynamic hashing such as Larson's Linear Hashing with Partial Extensions, Linear Hashing with Priority Splitting, Linear Hashing with Partial Expansions and Priority Splitting, or Recursive Linear Hashing.

The file structure of a dynamic hashing data structure adapts itself to changes in the size of the file, so expensive periodic file reorganization is avoided. A Linear Hashing file expands by splitting a predetermined bucket into two and shrinks by merging two predetermined buckets into one. The trigger for a reconstruction depends on the flavor of the scheme; it could be an overflow at a bucket or load factor (i.e., the number of records divided by the number of buckets) moving outside of a predetermined range. In Linear Hashing there are two types of buckets, those that are to be split and those already split. While extendible hashing splits only overflowing buckets, spiral hashing (a.k.a. spiral storage) distributes records unevenly over the buckets such that buckets with high costs of insertion, deletion, or retrieval are earliest in line for a split.

Linear Hashing has also been made into a scalable distributed data structure, **LH***. In LH*, each bucket resides at a different server. LH* itself has been expanded to provide data availability in the presence of failed buckets. Key based operations (inserts, deletes, updates, reads) in LH and LH* take maximum constant time independent of the number of buckets and hence of records.

## Algorithm details

Records in LH or LH* consists of a key and a content, the latter basically all the other attributes of the record. They are stored in buckets. For example, in Ellis' implementation, a bucket is a linked list of records. The file allows the key based CRUD operations create or insert, read, update, and delete as well as a scan operations that scans all records, for example to do a database select operation on a non-key attribute. Records are stored in buckets whose numbering starts with 0.

The key distinction from schemes such as Fagin's extendible hashing is that as the file expands due to insertions, only one bucket is split at a time, and the order in which buckets are split is already predetermined.

### Hash functions

The hash function $h_{i}(c)$ returns the 0-based index of the bucket that contains the record with key c . When a bucket which uses the hash function $h_{i}$ is split into two new buckets, the hash function $h_{i}$ is replaced with $h_{i+1}$ for both of those new buckets. At any time, at most two hash functions $h_{l}$ and $h_{l+1}$ are used; such that l corresponds to the current **level**. The family of hash functions $h_{i}(c)$ is also referred to as the dynamic hash function.

Typically, the value of i in $h_{i}$ corresponds to the number of rightmost binary digits of the key c that are used to segregate the buckets. This dynamic hash function can be expressed arithmetically as ${\textstyle h_{i}(c)\mapsto (c{\bmod {2}}^{i})}$ . Note that when the total number of buckets is equal to one, $i=0$ .

Complete the calculations below to determine the correct hashing function for the given hashing key c .

```mw
# l represents the current level
# s represents the split pointer index
a = h_l(c)
if (a < s): a = h_{l+1}(c)
```

### Split control

Linear hashing algorithms may use only controlled splits or both controlled and uncontrolled splits.

**Controlled splitting** occurs if a split is performed whenever the load factor, which is monitored by the file, exceeds a predetermined threshold. If the hash index uses controlled splitting, the buckets are allowed to overflow by using linked overflow blocks. When the *load factor* surpasses a set threshold, the *split pointer's* designated bucket is split. Instead of using the load factor, this threshold can also be expressed as an occupancy percentage, in which case, the maximum number of records in the hash index equals (occupancy percentage)*(max records per non-overflowed bucket)*(number of buckets).

An **uncontrolled split** occurs when a split is performed whenever a bucket overflows, in which case that bucket would be split into two separate buckets.

**File contraction** occurs in some LH algorithm implementations if a controlled split causes the load factor to sink below a threshold. In this case, a merge operation would be triggered which would undo the last split, and reset the file state.

### Split pointer

The index of the next bucket to be split is part of the file state and called the **split pointer** s . The split pointer corresponds to the first bucket that uses the hash function $h_{l}$ instead of $h_{l+1}$ .

For example, if numerical records are inserted into the hash index according to their farthest right binary digits, the bucket corresponding with the appended bucket will be split. Thus, if we have the buckets labelled as 000, 001, 10, 11, 100, 101, we would split the bucket 10 because we are appending and creating the next sequential bucket 110. This would give us the buckets 000, 001, 010, 11, 100, 101, 110.

When a bucket is split, split pointer and possibly the level are updated according to the following, such that the level is 0 when the linear hashing index only has 1 bucket.

```mw
# l represents the current level
# s represents the split pointer index
s = s + 1
if (s >= 2^l): 
    l = l + 1
    s = 0
```

### LH*

The main contribution of LH* is to allow a client of an LH* file to find the bucket where the record resides even if the client does not know the file state. Clients in fact store their version of the file state, which is initially just the knowledge of the first bucket, namely Bucket 0. Based on their file state, a client calculates the address of a key and sends a request to that bucket. At the bucket, the request is checked and if the record is not at the bucket, it is forwarded. In a reasonably stable system, that is, if there is only one split or merge going on while the request is processed, it can be shown that there are at most two forwards. After a forward, the final bucket sends an Image Adjustment Message to the client whose state is now closer to the state of the distributed file. While forwards are reasonably rare for active clients, their number can be even further reduced by additional information exchange between servers and clients

## Other properties

### File state calculation

The file state consists of split pointer s and level l . If the original file started with $N=1$ buckets, then the number of buckets n and the file state are related via

$n=2^{l}+s$ .

## Adoption in language systems

Griswold and Townsend discussed the adoption of linear hashing in the Icon language. They discussed the implementation alternatives of dynamic array algorithm used in linear hashing, and presented performance comparisons using a list of Icon benchmark applications.

## Adoption in database systems

Linear hashing is used in the Berkeley database system (BDB), which in turn is used by many software systems, using a C implementation derived from the CACM article and first published on the Usenet in 1988 by Esmond Pitt.
