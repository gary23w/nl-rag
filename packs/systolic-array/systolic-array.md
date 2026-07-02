---
title: "Systolic array"
source: https://en.wikipedia.org/wiki/Systolic_array
domain: systolic-array
license: CC-BY-SA-4.0
tags: systolic array, dataflow architecture, matrix multiplication hardware, array processing
fetched: 2026-07-02
---

# Systolic array

In parallel computer architectures, a **systolic array** is a homogeneous network of tightly coupled data processing units (DPUs) called cells or nodes. Each node or DPU independently computes a partial result as a function of the data received from its upstream neighbours, stores the result within itself and passes it downstream. The principles of systolic-like data flow were first seen in Colossus, which was an early computer used to break German Lorenz ciphers during World War II. Due to the classified nature of Colossus, they were independently invented by H. T. Kung and Charles Leiserson who described arrays for many dense linear algebra computations (matrix product, solving systems of linear equations, LU decomposition, etc.) for banded matrices. Early applications include computing greatest common divisors of integers and polynomials. Nowadays, they can be found in NPUs and hardware accelerators based on spatial designs. They are sometimes classified as multiple-instruction single-data (MISD) architectures under Flynn's taxonomy, but this classification is questionable because a strong argument can be made to distinguish systolic arrays from any of Flynn's four categories: SISD, SIMD, MISD, MIMD, as discussed later in this article.

The parallel input data flows through a network of hard-wired processor nodes, which combine, process, merge or sort the input data into a derived result. Because the wave-like propagation of data through a systolic array resembles the pulse of the human circulatory system, the name *systolic* was coined from medical terminology. The name is derived from systole as an analogy to the regular pumping of blood by the heart.

## Applications

Systolic arrays are often hard-wired for specific operations, such as multiply and accumulate, to perform massively parallel integration, convolution, correlation, matrix multiplication or data sorting tasks. They are also used for dynamic programming algorithms, used in DNA and protein sequence analysis.

## Architecture

A systolic array typically consists of a large monolithic network of primitive computing nodes which can be hardwired or software configured for a specific application. The nodes are usually fixed and identical, while the interconnect is programmable. The more general **wavefront** processors, by contrast, employ sophisticated and individually programmable nodes which may or may not be monolithic, depending on the array size and design parameters. The other distinction is that systolic arrays rely on synchronous data transfers, while wavefront tend to work asynchronously.

Unlike the more common Von Neumann architecture, where program execution follows a script of instructions stored in common memory, addressed and sequenced under the control of the CPU's program counter (PC), the individual nodes within a systolic array are triggered by the arrival of new data and always process the data in exactly the same way. The actual processing within each node may be hard wired or block micro coded, in which case the common node personality can be block programmable.

The systolic array paradigm with data-streams driven by data counters, is the counterpart of the Von Neumann architecture with instruction-stream driven by a program counter. Because a systolic array usually sends and receives multiple data streams, and multiple data counters are needed to generate these data streams, it supports data parallelism.

## Goals and benefits

A major benefit of systolic arrays is that all operand data and partial results are stored within (passing through) the processor array. There is no need to access external buses, main memory or internal caches during each operation as is the case with Von Neumann or Harvard sequential machines. The sequential limits on parallel performance dictated by Amdahl's Law also do not apply in the same way, because data dependencies are implicitly handled by the programmable node interconnect and there are no sequential steps in managing the highly parallel data flow.

Systolic arrays are therefore extremely good at artificial intelligence, image processing, pattern recognition, computer vision and other tasks that animal brains do particularly well. Wavefront processors in general can also be very good at machine learning by implementing self configuring neural nets in hardware.

## Classification controversy

While systolic arrays are officially classified as MISD, their classification is somewhat problematic. Because the input is typically a vector of independent values, the systolic array is definitely not SISD. Since these input values are merged and combined into the result(s) and do not maintain their independence as they would in a SIMD vector processing unit, the array cannot be classified as such. Consequently, the array cannot be classified as a MIMD either, because MIMD can be viewed as a mere collection of smaller SISD and SIMD machines.

Finally, because the data swarm is transformed as it passes through the array from node to node, the multiple nodes are not operating on the same data, which makes the MISD classification a misnomer. The other reason why a systolic array should not qualify as a **MISD** is the same as the one which disqualifies it from the SISD category: The input data is typically a vector not a **s**ingle **d**ata value, although one could argue that any given input vector is a single item of data.

In spite of all of the above, systolic arrays are often offered as a classic example of MISD architecture in textbooks on parallel computing and in engineering classes. If the array is viewed from the outside as atomic it should perhaps be classified as **SFMuDMeR** = single function, multiple data, merged result(s).

Systolic arrays use a pre-defined computational flow graph that connects their nodes. Kahn process networks use a similar flow graph, but are distinguished by the nodes working in lock-step in the systolic array: in a Kahn network, there are FIFO queues between each node.

## Detailed description

A systolic array is composed of matrix-like rows of data processing units called cells. Data processing units (DPUs) are similar to central processing units (CPUs), (except for the usual lack of a program counter, since operation is transport-triggered, i.e., by the arrival of a data object). Each cell shares the information with its neighbors immediately after processing. The systolic array is often rectangular where data flows across the array between neighbour DPUs, often with different data flowing in different directions. The data streams entering and leaving the ports of the array are generated by auto-sequencing memory units, ASMs. Each ASM includes a data counter. In embedded systems a data stream may also be input from and/or output to an external source.

Examples of 2x2 matrix multiplication in systolic array

Systolic array algorithm accumulating output values inside

DPUs

.

Systolic array algorithm pre-loading and keeping one operand stationary inside

DPUs

while computing. In the example, the green matrix is pre-loaded in the array and can be reused for subsequent multiplications.

An example of a systolic algorithm might be designed for matrix multiplication. One matrix is fed in a row at a time from the top of the array and is passed down the array, the other matrix is fed in a column at a time from the left hand side of the array and passes from left to right. Dummy values are then passed in until each processor has seen one whole row and one whole column. At this point, the result of the multiplication is stored in the array and can now be output a row or a column at a time, flowing down or across the array.

Systolic arrays are arrays of DPUs which are connected to a small number of nearest neighbour DPUs in a mesh-like topology. DPUs perform a sequence of operations on data that flows between them. Because the traditional systolic array synthesis methods have been practiced by algebraic algorithms, only uniform arrays with only linear pipes can be obtained, so that the architectures are the same in all DPUs. The consequence is that only applications with regular data dependencies can be implemented on classical systolic arrays. Like SIMD machines, clocked systolic arrays compute in "lock-step" with each processor undertaking alternate compute | communicate phases. But systolic arrays with asynchronous handshake between DPUs are called *wavefront arrays*. One well-known systolic array is Carnegie Mellon University's iWarp processor, which has been manufactured by Intel. An iWarp system has a linear array processor connected by data buses going in both directions.

## History

Systolic arrays (also known as *wavefront processors*), were first described by H. T. Kung and Charles E. Leiserson, who published the first paper describing systolic arrays in 1979. However, the first machine known to have used a similar technique was the Colossus Mark II in 1944. Colossus used parallel shift registers to pulse data, which is functionally similar to a systolic array, but it lacked the interconnected "processing elements" (PEs) that define the 1978 Kung-Leiserson architecture.

The first machine to be explicitly designed as a systolic array was the WARP computer in 1984.

## Examples

### Polynomial evaluation

Horner's rule for evaluating a polynomial is:

$y=(\ldots (((a_{n}\cdot x+a_{n-1})\cdot x+a_{n-2})\cdot x+a_{n-3})\cdot x+\ldots +a_{1})\cdot x+a_{0}.$

A linear systolic array in which the processors are arranged in pairs: one multiplies its input by x and passes the result to the right, the next adds $a_{j}$ and passes the result to the right.

### Convolution

Consider a chain of processing elements (PEs), each performing a multiply-accumulate operation. It processes input data ( $x_{i}$ ) and weights ( $w_{i}$ ) systolically, meaning data flows through the array in a regular, rhythmic manner. The weights remain stationary within each PE, while the input data and partial sums ( $y_{i}$ ) move in opposite directions.

Each PE performs the following operation: ${\begin{aligned}y_{out}&=y_{in}+w\cdot x_{in}\\x_{out}&=x_{in}\end{aligned}}$ where:

- $x_{in}$ is the input data.
- $y_{in}$ is the incoming partial sum.
- w is the weight stored in the PE.
- $x_{out}$ is the output data (passed to the next PE).
- $y_{out}$ is the updated partial sum.

From the left, the input stream is $\dots ,x_{3},0,x_{2},0,x_{1}$ , and from the right, the output stream is $y_{1},y_{2},y_{3},\dots$ . If $y_{1},x_{1}$ enter the rightmost PE simultaneously, then the leftmost PE outputs ${\begin{aligned}y_{1}&=w_{1}x_{1}+w_{2}x_{2}+w_{3}x_{3}+\cdots \\y_{2}&=w_{1}x_{2}+w_{2}x_{3}+w_{3}x_{4}+\cdots \\&\vdots \end{aligned}}$ This is the 1-dimensional convolution. Similarly, n-dimensional convolution can be computed by an n-dimensional array of PEs.

Many other implementations of the 1D convolutions are available, with different data flows.

See Figure 12 for an algorithm that performs on-the-fly least-squares using one- and two-dimensional systolic arrays.

### Sorting

Bubble sort is also an example of 1D systolic computation, although it applies N-1 passes for an array of size N. Each pass systolically moves the maximum element of a subsequence towards its final location in the sorted result.

If one is willing to use N/2 processing elements (PE) each with a comparator and two registers, elements arranged in a stack-like fashion, an array (or stream) of size N can thus be sorted in 2N time by pushing its elements in while on every level of the systolic stack the maximum of the pair of elements stored in each PE is pushed further down. And after all the elements are pushed in, the process is reversed with the minimum element in each PE being popped out (or "pushed up"), resulting in the stream of elements coming out sorted in ascending order.

Sorting input arrays of larger size (N > P) than the number of processing elements (P) is somewhat complex to do efficiently with such a system, but can be realized (by adding an external serial processor) in O(N log N/log P) time. The serial processor needs to manage a "bucket B-tree", where each node in the B-tree has P "buckets" that are eventually each sorted in O(P) time using the PEs.

## Implementations

- Inmos Transputer
- Cisco PXF network processor is internally organized as systolic array.
- Google’s TPU is also designed around a systolic array.
- Paracel FDF4T TestFinder text search system
- Paracel FDF4G GeneMatcher biological (DNA and protein) search system
- AWS Neuron architecture chips (Inferentia and Trainium) at Amazon Web Services
- Gemmini systolic array-based accelerator developed at UC Berkeley
