---
title: "External sorting"
source: https://en.wikipedia.org/wiki/External_sorting
domain: merge-sort-algorithm
license: CC-BY-SA-4.0
tags: merge sort, stable sort, external sorting, merge algorithm
fetched: 2026-07-02
---

# External sorting

**External sorting** is a class of sorting algorithms that can handle massive amounts of data. External sorting is required when the data being sorted do not fit into the main memory of a computing device (usually RAM) and instead they must reside in the slower external memory, usually a disk drive. Thus, external sorting algorithms are external memory algorithms and thus applicable in the external memory model of computation.

External sorting algorithms generally fall into two types, distribution sorting, which resembles quicksort, and external merge sort, which resembles merge sort. External merge sort typically uses a hybrid sort-merge strategy. In the sorting phase, chunks of data small enough to fit in main memory are read, sorted, and written out to a temporary file. In the merge phase, the sorted subfiles are combined into a single larger file.

## Model

External sorting algorithms can be analyzed in the external memory model. In this model, a cache or internal memory of size M and an unbounded external memory are divided into blocks of size B, and the running time of an algorithm is determined by the number of memory transfers between internal and external memory. Like their cache-oblivious counterparts, asymptotically optimal external sorting algorithms achieve a running time (in Big O notation) of $O\left({\tfrac {N}{B}}\log _{\tfrac {M}{B}}{\tfrac {N}{B}}\right)$ .

## External merge sort

One example of external sorting is the external merge sort algorithm, which uses a K-way merge algorithm. It sorts chunks that each fit in RAM, then merges the sorted chunks together.

The algorithm first sorts M items at a time and puts the sorted lists back into external memory. It does a ${\tfrac {M}{B}}$ -way merge on those sorted lists, recursing if there is not enough main memory to merge efficiently in one pass. During a merge pass, B elements from each sorted list are in internal memory, and the minimum is repeatedly outputted.

For example, for sorting 900 megabytes of data using only 100 megabytes of RAM:

1. Read 100 MB of the data in main memory and sort by some conventional method, like quicksort.
2. Write the sorted data to disk.
3. Repeat steps 1 and 2 until all of the data is in sorted 100 MB chunks (there are 900MB / 100MB = 9 chunks), which now need to be merged into one single output file.
4. Read the first 10 MB (= 100MB / (9 chunks + 1)) of each sorted chunk into input buffers in main memory and allocate the remaining 10 MB for an output buffer. (In practice, it might provide better performance to make the output buffer larger and the input buffers slightly smaller.)
5. Perform a 9-way merge and store the result in the output buffer. Whenever the output buffer fills, write it to the final sorted file and empty it. Whenever any of the 9 input buffers empties, fill it with the next 10 MB of its associated 100 MB sorted chunk until no more data from the chunk is available.

The merge pass is key to making external merge sort work externally. The merge algorithm only makes one pass through each chunk, so chunks do not have to be loaded all at once; rather, sequential parts of the chunk are loaded as needed. And as long as the blocks read are relatively large (like the 10 MB in this example), the reads can be relatively efficient even on media with low random-read performance, like hard drives.

Historically, instead of a sort, sometimes a replacement-selection algorithm was used to perform the initial distribution, to produce on average half as many output chunks of double the length.

### Additional passes

The previous example is a two-pass sort: first sort, then merge. The sort ends with a single *k*-way merge, rather than a series of two-way merge passes as in a typical in-memory merge sort. This is because each merge pass reads and writes *every value* from and to disk, so reducing the number of passes more than compensates for the additional cost of a *k*-way merge.

The limitation to single-pass merging is that as the number of chunks increases, memory will be divided into more buffers, so each buffer is smaller. Eventually, the reads become so small that more time is spent on disk seeks than data transfer. A typical magnetic hard disk drive might have a 10 ms access time and 100 MB/s data transfer rate, so each seek takes as much time as transferring 1 MB of data.

Thus, for sorting, say, 50 GB in 100 MB of RAM, using a single 500-way merge pass isn't efficient: we can only read 100 MB / 501 ≈ 200 KB from each chunk at once, so 5/6 of the disk's time is spent seeking. Using two merge passes solves the problem. Then the sorting process might look like this:

1. Run the initial chunk-sorting pass as before to create 500×100 MB sorted chunks.
2. Run a first merge pass combining 25×100 MB chunks at a time, resulting in 20×2.5 GB sorted chunks.
3. Run a second merge pass to merge the 20×2.5 GB sorted chunks into a single 50 GB sorted result

Although this requires an additional pass over the data, each read is now 4 MB long, so only 1/5 of the disk's time is spent seeking. The improvement in data transfer efficiency during the merge passes (16.6% to 80% is almost a 5× improvement) more than makes up for the doubled number of merge passes.

Variations include using an intermediate medium like solid-state disk for some stages; the fast temporary storage needn't be big enough to hold the whole dataset, just substantially larger than available main memory. Repeating the example above with 1 GB of temporary SSD storage, the first pass could merge 10×100 MB sorted chunks read from that temporary space to write 50x1 GB sorted chunks to HDD. The high bandwidth and random-read throughput of SSDs help speed the first pass, and the HDD reads for the second pass can then be 2 MB, large enough that seeks will not take up most of the read time. SSDs can also be used as read buffers in a merge phase, allowing fewer larger reads (20MB reads in this example) from HDD storage. Given the lower cost of SSD capacity relative to RAM, SSDs can be an economical tool for sorting large inputs with very limited memory.

Like in-memory sorts, efficient external sorts require O(*n* log *n*) time: exponentially growing datasets require linearly increasing numbers of passes that each take O(n) time. Under reasonable assumptions at least 500 GB of data stored on a hard drive can be sorted using 1 GB of main memory before a third pass becomes advantageous, and many times that much data can be sorted before a fourth pass becomes useful.

Main memory size is important. Doubling memory dedicated to sorting halves the number of chunks *and* the number of reads per chunk, reducing the number of seeks required by about three-quarters. The ratio of RAM to disk storage on servers often makes it convenient to do huge sorts on a cluster of machines rather than on one machine with multiple passes. Media with high random-read performance like solid-state drives (SSDs) also increase the amount that can be sorted before additional passes improve performance.

## External distribution sort

External distribution sort is analogous to quicksort. The algorithm finds approximately ${\tfrac {M}{B}}$ pivots and uses them to divide the N elements into approximately equally sized subarrays, each of whose elements are all smaller than the next, and then recurse until the sizes of the subarrays are less than the block size. When the subarrays are less than the block size, sorting can be done quickly because all reads and writes are done in the cache, and in the external memory model requires $O(1)$ operations.

However, finding exactly ${\tfrac {M}{B}}$ pivots would not be fast enough to make the external distribution sort asymptotically optimal. Instead, we find slightly fewer pivots. To find these pivots, the algorithm splits the N input elements into ${\tfrac {N}{M}}$ chunks, and takes every ${\sqrt {\tfrac {M}{16B}}}$ elements, and recursively uses the median of medians algorithm to find ${\sqrt {\tfrac {M}{B}}}$ pivots.

There is a duality, or fundamental similarity, between merge- and distribution-based algorithms.

## Performance

The Sort Benchmark, created by computer scientist Jim Gray, compares external sorting algorithms implemented using finely tuned hardware and software. Winning implementations use several techniques:

- **Using parallelism**
  - Multiple disk drives can be used in parallel in order to improve sequential read and write speed. This can be a very cost-efficient improvement: a Sort Benchmark winner in the cost-centric Penny Sort category uses six hard drives in an otherwise midrange machine.
  - Sorting software can use multiple threads, to speed up the process on modern multicore computers.
  - Software can use asynchronous I/O so that one run of data can be sorted or merged while other runs are being read from or written to disk.
  - Multiple machines connected by fast network links can each sort part of a huge dataset in parallel.
- **Increasing hardware speed**
  - Using more RAM for sorting can reduce the number of disk seeks and avoid the need for more passes.
  - Fast external memory like solid-state drives can speed sorts, either if the data is small enough to fit entirely on SSDs or, more rarely, to accelerate sorting SSD-sized chunks in a three-pass sort.
  - *Many* other factors can affect hardware's maximum sorting speed: CPU speed and number of cores, RAM access latency, input/output bandwidth, disk read/write speed, disk seek time, and others. "Balancing" the hardware to minimize bottlenecks is an important part of designing an efficient sorting system.
  - Cost-efficiency as well as absolute speed can be critical, especially in cluster environments where lower node costs allow purchasing more nodes.
- **Increasing software speed**
  - Some Sort Benchmark entrants use a variation on radix sort for the first phase of sorting: they separate data into one of many "bins" based on the beginning of its value. Sort Benchmark data is random and especially well-suited to this optimization.
  - Compacting the input, intermediate files, and output can reduce time spent on I/O, but is not allowed in the Sort Benchmark.
  - Because the Sort Benchmark sorts long (100-byte) records using short (10-byte) keys, sorting software sometimes rearranges the keys separately from the values to reduce memory I/O volume.
