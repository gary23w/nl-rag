---
title: "Reed–Solomon error correction (part 1/2)"
source: https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction
domain: information-theory
license: CC-BY-SA-4.0
tags: information theory, shannon entropy, channel capacity, error correction, hamming code
fetched: 2026-07-02
part: 1/2
---

# Reed–Solomon error correction

In information theory and coding theory, **Reed–Solomon codes** are a group of error-correcting codes that were introduced by Irving S. Reed and Gustave Solomon in 1960. They have many applications, including consumer technologies such as MiniDiscs, CDs, DVDs, Blu-ray discs, QR codes, Data Matrix, data transmission technologies such as DSL and WiMAX, broadcast systems such as satellite communications, DVB and ATSC, and storage systems such as RAID 6.

Reed–Solomon codes operate on a block of data treated as a set of finite-field elements called symbols. Reed–Solomon codes RS(*n*, *k*) are able to detect and correct multiple symbol errors. By adding *t* = *n* − *k* check symbols to the data, a Reed–Solomon code can detect (but not correct) any combination of up to t erroneous symbols, *or* locate and correct up to ⌊*t*/2⌋ erroneous symbols at unknown locations. As an erasure code, it can correct up to t erasures at locations that are known and provided to the algorithm, or it can detect and correct combinations of errors and erasures. Reed–Solomon codes are also suitable as multiple-burst bit-error correcting codes, since a sequence of *b* + 1 consecutive bit errors can affect at most two symbols of size b. The choice of t is up to the designer of the code and may be selected within wide limits.

There are two different Reed-Solomon encoding schemes, called original view and BCH view in this article. The history section explains the origins of this.


## History

Reed–Solomon codes were developed in 1960 by Irving S. Reed and Gustave Solomon, who were then staff members of MIT Lincoln Laboratory. Their seminal article was titled "Polynomial Codes over Certain Finite Fields". The original encoding scheme described in the Reed and Solomon article used a variable polynomial based on the message to be encoded where only a fixed set of values (evaluation points) to be encoded are known to encoder and decoder. The original theoretical decoder generated potential polynomials based on subsets of *k* (unencoded message length) out of *n* (encoded message length) values of a received message, choosing the most popular polynomial as the correct one, which was impractical for all but the simplest of cases. This was initially resolved by changing the original scheme to a BCH-code compatible scheme based on a fixed polynomial known to both encoder and decoder, but later, practical decoders based on the original scheme were developed, although initially slower than the BCH schemes. The result of this is that there are two main types of Reed–Solomon codes: ones that use the original encoding scheme and ones that use the BCH encoding scheme.

Also in 1960, a practical fixed polynomial decoder for BCH codes developed by Daniel Gorenstein and Neal Zierler was described in an MIT Lincoln Laboratory report by Zierler in January 1960 and later in an article in June 1961. The Gorenstein–Zierler decoder and the related work on BCH codes are described in a book "Error-Correcting Codes" by W. Wesley Peterson (1961). By 1963 (or possibly earlier), J.J. Stone (and others) recognized that Reed–Solomon codes could use the BCH scheme of using a fixed generator polynomial, making such codes a special class of BCH codes, but Reed–Solomon codes based on the original encoding scheme are not a class of BCH codes, and depending on the set of evaluation points, they are not even cyclic codes.

In 1969, an improved BCH scheme decoder was developed by Elwyn Berlekamp and James Massey and has since been known as the Berlekamp–Massey decoding algorithm.

In 1975, another improved BCH scheme decoder was developed by Yasuo Sugiyama, based on the extended Euclidean algorithm.

In 1977, Reed–Solomon codes were implemented in the Voyager program in the form of concatenated error correction codes. The first commercial application in mass-produced consumer products appeared in 1982 with the compact disc, where two interleaved Reed–Solomon codes are used. Today, Reed–Solomon codes are widely implemented in digital storage devices and digital communication standards, though they are being slowly replaced by Bose–Chaudhuri–Hocquenghem (BCH) codes. For example, Reed–Solomon codes are used in the Digital Video Broadcasting (DVB) standard DVB-S, in conjunction with a convolutional inner code, but BCH codes are used with LDPC in its successor, DVB-S2.

In 1986, an original scheme decoder known as the Berlekamp–Welch algorithm was developed.

In 1996, variations of original scheme decoders called list decoders or soft decoders were developed by Madhu Sudan and others, and work continues on these types of decoders (see Guruswami–Sudan list decoding algorithm).

In 2002, another original scheme decoder was developed by Shuhong Gao, based on the extended Euclidean algorithm.

Around 2015 an original scheme syndrome like decoder was developed (author unknown).


## Applications

### Data storage

Reed–Solomon coding is very widely used in mass storage systems to correct the burst errors associated with media defects.

Reed–Solomon coding is a key component of the compact disc. It was the first use of strong error correction coding in a mass-produced consumer product, and DAT and DVD use similar schemes. In the CD, two layers of Reed–Solomon coding separated by a 28-way convolutional interleaver yields a scheme called Cross-Interleaved Reed–Solomon Coding (CIRC). The first element of a CIRC decoder is a relatively weak inner (32,28) Reed–Solomon code, shortened from a (255,251) code with 8-bit symbols. This code can correct up to 2 byte errors per 32-byte block. More importantly, it flags as erasures any uncorrectable blocks, i.e., blocks with more than 2 byte errors. The decoded 28-byte blocks, with erasure indications, are then spread by the deinterleaver to different blocks of the (28,24) outer code. Thanks to the deinterleaving, an erased 28-byte block from the inner code becomes a single erased byte in each of 28 outer code blocks. The outer code easily corrects this, since it can handle up to 4 such erasures per block.

The result is a CIRC that can completely correct error bursts up to 4000 bits, or about 2.5 mm on the disc surface. This code is so strong that most CD playback errors are almost certainly caused by tracking errors that cause the laser to jump track, not by uncorrectable error bursts.

DVDs use a similar scheme, but with much larger blocks, a (208,192) inner code, and a (182,172) outer code.

Reed–Solomon error correction is also used in parchive files which are commonly posted accompanying multimedia files on USENET. The distributed online storage service Wuala (discontinued in 2015) also used Reed–Solomon when breaking up files.

### Bar code

Almost all two-dimensional bar codes such as PDF-417, MaxiCode, Datamatrix, QR Code, Aztec Code and Han Xin code use Reed–Solomon error correction to allow correct reading even if a portion of the bar code is damaged. When the bar code scanner cannot recognize a bar code symbol, it will treat it as an erasure.

Reed–Solomon coding is less common in one-dimensional bar codes, but is used by the PostBar symbology.

### Data transmission

Specialized forms of Reed–Solomon codes, specifically Cauchy-RS and Vandermonde-RS, can be used to overcome the unreliable nature of data transmission over erasure channels. The encoding process assumes a code of RS(*N*, *K*) which results in *N* codewords of length *N* symbols each storing *K* symbols of data, being generated, that are then sent over an erasure channel.

Any combination of *K* codewords received at the other end is enough to reconstruct all of the *N* codewords. The code rate is generally set to 1/2 unless the channel's erasure likelihood can be adequately modelled and is seen to be less. In conclusion, *N* is usually 2*K*, meaning that at least half of all the codewords sent must be received in order to reconstruct all of the codewords sent.

Reed–Solomon codes are also used in xDSL systems and CCSDS's Space Communications Protocol Specifications as a form of forward error correction.

### Space transmission

One significant application of Reed–Solomon coding was to encode the digital pictures sent back by the Voyager program.

Voyager introduced Reed–Solomon coding concatenated with convolutional codes, a practice that has since become very widespread in deep space and satellite (e.g., direct digital broadcasting) communications.

Viterbi decoders tend to produce errors in short bursts. Correcting these burst errors is a job best done by short or simplified Reed–Solomon codes.

Modern versions of concatenated Reed–Solomon/Viterbi-decoded convolutional coding were and are used on the Mars Pathfinder, Galileo, Mars Exploration Rover and Cassini missions, where they perform within about 1–1.5 dB of the ultimate limit, the Shannon capacity.

These concatenated codes are now being replaced by more powerful turbo codes:

| Years | Code | Mission(s) |
|---|---|---|
| 1958–present | Uncoded | Explorer, Mariner, many others |
| 1968–1978 | convolutional codes (CC) (25, 1/2) | Pioneer, Venus |
| 1969–1975 | Reed–Muller code (32, 6) | Mariner, Viking |
| 1977–present | Binary Golay code | Voyager |
| 1977–present | RS(255, 223) + CC(7, 1/2) | Voyager, Galileo, many others |
| 1989–2003 | RS(255, 223) + CC(7, 1/3) | Voyager |
| 1989–2003 | RS(255, 223) + CC(14, 1/4) | Galileo |
| 1996–present | RS + CC (15, 1/6) | Cassini, Mars Pathfinder, others |
| 2004–present | Turbo codes | Messenger, Stereo, MRO, MSL, others |
| est. 2009 | LDPC codes | Constellation, M2020, MAVEN |


## Constructions (encoding)

The Reed–Solomon code is actually a family of codes, where every code is characterised by three parameters: an alphabet size q, a block length n, and a message length k*,* with $k<n\leq q$ . The set of alphabet symbols is interpreted as the finite field F of order q , and thus, q must be a prime power. In the most useful parameterizations of the Reed–Solomon code, the block length is usually some constant multiple of the message length, that is, the rate $R={\frac {k}{n}}$ is some constant, and furthermore, the block length is either equal to the alphabet size or one less than it, i.e., $n=q$ or $n=q-1$ .

### Reed & Solomon's original view: The codeword as a sequence of values

There are different encoding procedures for the Reed–Solomon code, and thus, there are different ways to describe the set of all codewords. In the original view of Reed and Solomon, every codeword of the Reed–Solomon code is a sequence of function values of a polynomial of degree less than k . In order to obtain a codeword of the Reed–Solomon code, the message symbols (each within the q-sized alphabet) are treated as the coefficients of a polynomial p of degree less than k , over the finite field F with q elements. In turn, the polynomial p is evaluated at a set of $n\leq q$ distinct points in any order $a_{1},\dots ,a_{n}$ of the field F , and the sequence of values is the corresponding codeword. Common choices for a set of evaluation points include $\{0,1,2,\dots ,n-1\}$ , $\{0,1,\alpha ,\alpha ^{2},\dots ,\alpha ^{n-2}\}$ , or for $n<q$ , $\{1,\alpha ,\alpha ^{2},\dots ,\alpha ^{n-1}\}$ , ... , where $\alpha$ is a primitive element of F .

Formally, the set $\mathbf {C}$ of codewords of the Reed–Solomon code is defined as follows: $\mathbf {C} ={\Bigl \{}\;{\bigl (}p(a_{1}),p(a_{2}),\dots ,p(a_{n}){\bigr )}\;{\Big |}\;p{\text{ is a polynomial over }}F{\text{ of degree }}<k\;{\Bigr \}}\,.$ Since any two *distinct* polynomials of degree less than k agree in at most $k-1$ points, this means that any two codewords of the Reed–Solomon code disagree in at least $n-(k-1)=n-k+1$ positions. Furthermore, there are two polynomials that do agree in $k-1$ points but are not equal, and thus, the distance of the Reed–Solomon code is exactly $d=n-k+1$ . Then the relative distance is $\delta =d/n=1-k/n+1/n=1-R+1/n\sim 1-R$ , where $R=k/n$ is the rate. This trade-off between the relative distance and the rate is asymptotically optimal since, by the Singleton bound, *every* code satisfies $\delta +R\leq 1+1/n$ . Being a code that achieves this optimal trade-off, the Reed–Solomon code belongs to the class of maximum distance separable codes.

While the number of different polynomials of degree less than *k* and the number of different messages are both equal to $q^{k}$ , and thus every message can be uniquely mapped to such a polynomial, there are different ways of doing this encoding. The original construction of Reed & Solomon interprets the message *x* as the *coefficients* of the polynomial *p*, whereas subsequent constructions interpret the message as the *values* of the polynomial at the first *k* points $a_{1},\dots ,a_{k}$ and obtain the polynomial *p* by interpolating these values with a polynomial of degree less than *k*. The latter encoding procedure, while being slightly less efficient, has the advantage that it gives rise to a systematic code, that is, the original message is always contained as a subsequence of the codeword.

#### Simple encoding procedure: The message as a sequence of coefficients

In the original construction of Reed and Solomon, the message $m=(m_{0},\dots ,m_{k-1})\in F^{k}$ is mapped to the polynomial $p_{m}$ with $p_{m}(a)=\sum _{i=0}^{k-1}m_{i}a^{i}=m_{0}+m_{1}a+m_{2}a^{2}+\cdots +m_{k-1}a^{k-1}$ The codeword of m is obtained by evaluating $p_{m}$ at n different points $a_{0},\dots ,a_{n-1}$ of the field F . Thus the classical encoding function $C:F^{k}\to F^{n}$ for the Reed–Solomon code is defined as follows: $C(m)={\begin{bmatrix}p_{m}(a_{0})&p_{m}(a_{1})&\cdots &p_{m}(a_{n-1})\end{bmatrix}}$

This function C is a linear mapping, that is, it satisfies $C(m)=mA$ for the following $k\times n$ -matrix A with elements from F .

$C(m)=mA={\begin{bmatrix}m_{0}&m_{1}&m_{2}&\cdots &m_{k-1}\end{bmatrix}}{\begin{bmatrix}1&1&1&\dots &1\\a_{0}&a_{1}&a_{2}&\dots &a_{n-1}\\a_{0}^{2}&a_{1}^{2}&a_{2}^{2}&\dots &a_{n-1}^{2}\\\vdots &\vdots &\vdots &\ddots &\vdots \\a_{0}^{k-1}&a_{1}^{k-1}&a_{2}^{k-1}&\dots &a_{n-1}^{k-1}\end{bmatrix}}$

This matrix is a Vandermonde matrix over F . In other words, the Reed–Solomon code is a linear code, and in the classical encoding procedure, its generator matrix is A .

#### Systematic encoding procedure: The message as an initial sequence of values

There are alternative encoding procedures that produce a systematic Reed–Solomon code. One method uses Lagrange interpolation to compute polynomial $p_{m}$ such that $p_{m}(a_{i})=m_{i}{\text{ for all }}i\in \{0,\dots ,k-1\}.$ Then $p_{m}$ is evaluated at the other points $a_{k},\dots ,a_{n-1}$ .

$C(m)={\begin{bmatrix}p_{m}(a_{0})&p_{m}(a_{1})&\cdots &p_{m}(a_{n-1})\end{bmatrix}}$

This function C is a linear mapping. To generate the corresponding systematic encoding matrix G, multiply the matrix A by the inverse of A's left square submatrix.

$G=(A{\text{'s left square submatrix}})^{-1}\cdot A={\begin{bmatrix}1&0&0&\dots &0&g_{1,k+1}&\dots &g_{1,n}\\0&1&0&\dots &0&g_{2,k+1}&\dots &g_{2,n}\\0&0&1&\dots &0&g_{3,k+1}&\dots &g_{3,n}\\\vdots &\vdots &\vdots &&\vdots &\vdots &&\vdots \\0&\dots &0&\dots &1&g_{k,k+1}&\dots &g_{k,n}\end{bmatrix}}$

$C(m)=mG$ for the following $k\times n$ -matrix G with elements from F . $C(m)=mG={\begin{bmatrix}m_{0}&m_{1}&m_{2}&\cdots &m_{k-1}\end{bmatrix}}{\begin{bmatrix}1&0&0&\dots &0&g_{1,k+1}&\dots &g_{1,n}\\0&1&0&\dots &0&g_{2,k+1}&\dots &g_{2,n}\\0&0&1&\dots &0&g_{3,k+1}&\dots &g_{3,n}\\\vdots &\vdots &\vdots &&\vdots &\vdots &&\vdots \\0&\dots &0&\dots &1&g_{k,k+1}&\dots &g_{k,n}\end{bmatrix}}$

#### Discrete Fourier transform and its inverse

A discrete Fourier transform is essentially the same as the encoding procedure; it uses the generator polynomial $p_{m}$ to map a set of evaluation points into the message values as shown above: $C(m)={\begin{bmatrix}p_{m}(a_{0})&p_{m}(a_{1})&\cdots &p_{m}(a_{n-1})\end{bmatrix}}$

The inverse Fourier transform could be used to convert an error free set of *n* < *q* message values back into the encoding polynomial of *k* coefficients, with the constraint that in order for this to work, the set of evaluation points used to encode the message must be a set of increasing powers of *α*: $a_{i}=\alpha ^{i}$ $a_{0},\dots ,a_{n-1}=\{1,\alpha ,\alpha ^{2},\dots ,\alpha ^{n-1}\}$

However, Lagrange interpolation performs the same conversion without the constraint on the set of evaluation points or the requirement of an error free set of message values and is used for systematic encoding, and in one of the steps of the Gao decoder.

### The BCH view: The codeword as a sequence of coefficients

Note that BCH Code and most implementations of BCH view are most significant term first. In this view, the message is interpreted as the coefficients of a polynomial $m(x)$ :

$m(x)=m_{k-1}x^{k-1}+m_{k-2}x^{k-2}+\cdots +m_{1}x+m_{0}$

A generator polynomial $g(x)$ is defined as the polynomial whose roots are sequential powers of the Galois field primitive $\alpha$ $g(x)=\left(x-\alpha ^{i}\right)\left(x-\alpha ^{i+1}\right)\cdots \left(x-\alpha ^{i+n-k-1}\right)=x^{n-k}+g_{n-k-1}x^{n-k-1}+\cdots +g_{1}x+g_{0}$ For a "narrow sense code", $i=1$ .

Encoding computes a codeword polynomial $c(x)=c_{n-1}x^{n-1}+c_{n-2}x^{n-2}+\cdots +c_{1}x+c_{0}$ that is an exact multiple of $g(x)$ .

#### Simple encoding procedure

The sender computes a related polynomial $c(x)$ of degree $n-1$ where $n\leq q-1$ and sends the polynomial $c(x)$ . The polynomial $c(x)$ is constructed by multiplying the message polynomial $m(x)$ , which has degree $k-1$ , with the generator polynomial $g(x)$ of degree $n-k$ that is known to both the sender and the receiver. $c(x)=m(x)g(x)$ .

This function C is a linear mapping, that is, it satisfies $C(m)=mA$ for the following $k\times n$ -matrix A with elements from F .

$A={\begin{bmatrix}1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0&\cdots &\cdots &0\\0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0&\cdots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\cdots &0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0\\0&\cdots &\cdots &0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}\\\end{bmatrix}}$

$C(m)=mA$ for the following $k\times n$ matrix G with elements from F .

$c(x)=mA={\begin{bmatrix}m_{k-1}&\cdots &m_{1}&m_{0}\end{bmatrix}}{\begin{bmatrix}1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0&\cdots &\cdots &0\\0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0&\cdots &0\\\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots &\vdots \\0&\cdots &0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}&0\\0&\cdots &\cdots &0&1&g_{n-k-1}&\cdots &g_{1}&g_{0}\\\end{bmatrix}}$

#### Systematic encoding procedure

The encoding procedure for the BCH view of Reed–Solomon codes can be modified to yield a systematic encoding procedure, in which each codeword contains the message as a prefix, and simply appends error correcting symbols as a suffix. Here, instead of sending $c(x)=m(x)g(x)$ , the encoder constructs the transmitted polynomial $c(x)$ such that the coefficients of the k largest monomials are equal to the corresponding coefficients of $m(x)$ , and the lower-order coefficients of $c(x)$ are chosen in such a way that $c(x)$ becomes exactly divisible by $g(x)$ . Then the coefficients of $m(x)$ are a subsequence of the coefficients of $c(x)$ . To get a code that is overall systematic, we construct the message polynomial $c(x)$ by interpreting the message as the sequence of its coefficients.

Formally, the construction is done by multiplying $c(x)$ by $x^{t}$ to make room for the $t=n-k$ check symbols, dividing that product by $g(x)$ to find the remainder, and then compensating for that remainder by subtracting it. The t check symbols are created by computing the remainder $r(x)$ : $r(x)=c(x)\cdot x^{t}\ {\bmod {\ }}g(x).$

The remainder has degree at most $t-1$ , whereas the coefficients of $x^{t-1},x^{t-2},\dots ,x^{1},x^{0}$ in the polynomial $c(x)\cdot x^{t}$ are zero. Therefore, the following definition of the codeword $c(x)$ has the property that the first k coefficients are identical to the coefficients of $c(x)$ : $c(x)=m(x)\cdot x^{t}-r(x)\,.$

As a result, $c(x)$ is exactly divisible by $g(x)$ :

$c(x)\equiv m(x)\cdot x^{t}-r(x)\equiv r(x)-r(x)\equiv 0\mod g(x)\,.$

This function C is a linear mapping. To generate the corresponding systematic encoding matrix G, multiply the matrix A by the inverse of A's left square submatrix (or set G's left square submatrix to the identity matrix and encode each row).

$G=(A{\text{'s left square submatrix}})^{-1}\cdot A={\begin{bmatrix}1&0&0&\dots &0&g_{1,k+1}&\dots &g_{1,n}\\0&1&0&\dots &0&g_{2,k+1}&\dots &g_{2,n}\\0&0&1&\dots &0&g_{3,k+1}&\dots &g_{3,n}\\\vdots &\vdots &\vdots &&\vdots &\vdots &&\vdots \\0&\dots &0&\dots &1&g_{k,k+1}&\dots &g_{k,n}\end{bmatrix}}$

$C(m)=mG$ for the following $k\times n$ matrix G with elements from F .

$c(x)=mG={\begin{bmatrix}m_{k-1}&\ldots &m_{1}&m_{0}\end{bmatrix}}{\begin{bmatrix}1&0&0&\dots &0&g_{1,k+1}&\dots &g_{1,n}\\0&1&0&\dots &0&g_{2,k+1}&\dots &g_{2,n}\\0&0&1&\dots &0&g_{3,k+1}&\dots &g_{3,n}\\\vdots &\vdots &\vdots &&\vdots &\vdots &&\vdots \\0&\dots &0&\dots &1&g_{k,k+1}&\dots &g_{k,n}\end{bmatrix}}$


## Properties

The Reed–Solomon code is a [*n*, *k*, *n* − *k* + 1] code; in other words, it is a linear block code of length *n* (over *F*) with dimension *k* and minimum Hamming distance ${\textstyle d_{\min }=n-k+1.}$ The Reed–Solomon code is optimal in the sense that the minimum distance has the maximum value possible for a linear code of size (*n*, *k*); this is known as the Singleton bound. Such a code is also called a maximum distance separable (MDS) code.

The error-correcting ability of a Reed–Solomon code is determined by its minimum distance, or equivalently, by $n-k$ , the measure of redundancy in the block. If the locations of the error symbols are not known in advance, then a Reed–Solomon code can correct up to $(n-k)/2$ erroneous symbols, i.e., it can correct half as many errors as there are redundant symbols added to the block. Sometimes error locations are known in advance (e.g., "side information" in demodulator signal-to-noise ratios)—these are called erasures. A Reed–Solomon code (like any MDS code) is able to correct twice as many erasures as errors, and any combination of errors and erasures can be corrected as long as the relation 2*E* + *S* ≤ *n* − *k* is satisfied, where E is the number of errors and S is the number of erasures in the block.

The theoretical error bound can be described via the following formula for the AWGN channel for FSK: $P_{b}\approx {\frac {2^{m-1}}{2^{m}-1}}{\frac {1}{n}}\sum _{\ell =t+1}^{n}\ell {n \choose \ell }P_{s}^{\ell }(1-P_{s})^{n-\ell }$ and for other modulation schemes: $P_{b}\approx {\frac {1}{m}}{\frac {1}{n}}\sum _{\ell =t+1}^{n}\ell {n \choose \ell }P_{s}^{\ell }(1-P_{s})^{n-\ell }$ where ${\textstyle t={\frac {1}{2}}(d_{\min }-1)}$ , $P_{s}=1-(1-s)^{h}$ , $h={\frac {m}{\log _{2}M}}$ , s is the symbol error rate in uncoded AWGN case and M is the modulation order.

For practical uses of Reed–Solomon codes, it is common to use a finite field F with $2^{m}$ elements. In this case, each symbol can be represented as an m -bit value. The sender sends the data points as encoded blocks, and the number of symbols in the encoded block is $n=2^{m}-1$ . Thus a Reed–Solomon code operating on 8-bit symbols has $n=2^{8}-1=255$ symbols per block. (This is a very popular value because of the prevalence of byte-oriented computer systems.) The number k , with $k<n$ , of *data* symbols in the block is a design parameter. A commonly used code encodes $k=223$ eight-bit data symbols plus 32 eight-bit parity symbols in an $n=255$ -symbol block; this is denoted as a $(n,k)=(255,223)$ code, and is capable of correcting up to 16 symbol errors per block.

The Reed–Solomon code properties discussed above make them especially well-suited to applications where errors occur in bursts. This is because it does not matter to the code how many bits in a symbol are in error — if multiple bits in a symbol are corrupted it only counts as a single error. Conversely, if a data stream is not characterized by error bursts or drop-outs but by random single bit errors, a Reed–Solomon code is usually a poor choice compared to a binary code.

The Reed–Solomon code, like the convolutional code, is a transparent code. This means that if the channel symbols have been inverted somewhere along the line, the decoders will still operate. The result will be the inversion of the original data. However, the Reed–Solomon code loses its transparency when the code is shortened (*see 'Remarks' at the end of this section*). The "missing" bits in a shortened code need to be filled by either zeros or ones, depending on whether the data is complemented or not. (To put it another way, if the symbols are inverted, then the zero-fill needs to be inverted to a one-fill.) For this reason it is mandatory that the sense of the data (i.e., true or complemented) be resolved before Reed–Solomon decoding.

Whether the Reed–Solomon code is cyclic or not depends on subtle details of the construction. In the original view of Reed and Solomon, where the codewords are the values of a polynomial, one can choose the sequence of evaluation points in such a way as to make the code cyclic. In particular, if $\alpha$ is a primitive root of the field F , then by definition all non-zero elements of F take the form $\alpha ^{i}$ for $i\in \{1,\dots ,q-1\}$ , where $q=|F|$ . Each polynomial p over F gives rise to a codeword $(p(\alpha ^{1}),\dots ,p(\alpha ^{q-1}))$ . Since the function $a\mapsto p(\alpha a)$ is also a polynomial of the same degree, this function gives rise to a codeword $(p(\alpha ^{2}),\dots ,p(\alpha ^{q}))$ ; since $\alpha ^{q}=\alpha ^{1}$ holds, this codeword is the cyclic left-shift of the original codeword derived from p . So choosing a sequence of primitive root powers as the evaluation points makes the original view Reed–Solomon code cyclic. Reed–Solomon codes in the BCH view are always cyclic because BCH codes are cyclic.

### Remarks

Designers are not required to use the "natural" sizes of Reed–Solomon code blocks. A technique known as "shortening" can produce a smaller code of any desired size from a larger code. For example, the widely used (255,223) code can be converted to a (160,128) code by padding the unused portion of the source block with 95 binary zeroes and not transmitting them. At the decoder, the same portion of the block is loaded locally with binary zeroes.

The QR code, Ver 3 (29×29) uses interleaved blocks. The message has 26 data bytes and is encoded using two Reed-Solomon code blocks. Each block is a (255,233) Reed Solomon code shortened to a (35,13) code.

The Delsarte–Goethals–Seidel theorem illustrates an example of an application of shortened Reed–Solomon codes. In parallel to shortening, a technique known as puncturing allows omitting some of the encoded parity symbols.


## BCH view decoders

The decoders described in this section use the BCH view of a codeword as a sequence of coefficients. They use a fixed generator polynomial known to both encoder and decoder.

### Peterson–Gorenstein–Zierler decoder

Daniel Gorenstein and Neal Zierler developed a decoder that was described in a MIT Lincoln Laboratory report by Zierler in January 1960 and later in a paper in June 1961. The Gorenstein–Zierler decoder and the related work on BCH codes are described in the book *Error Correcting Codes* by W. Wesley Peterson (1961).

#### Formulation

The transmitted message, $(c_{0},\ldots ,c_{i},\ldots ,c_{n-1})$ , is viewed as the coefficients of a polynomial $s(x)=\sum _{i=0}^{n-1}c_{i}x^{i}.$

As a result of the Reed–Solomon encoding procedure, *s*(*x*) is divisible by the generator polynomial $g(x)=\prod _{j=1}^{n-k}(x-\alpha ^{j}),$ where *α* is a primitive element.

Since *s*(*x*) is a multiple of the generator *g*(*x*), it follows that it "inherits" all its roots: $s(x){\bmod {(}}x-\alpha ^{j})=g(x){\bmod {(}}x-\alpha ^{j})=0.$ Therefore, $s(\alpha ^{j})=0,\ j=1,2,\ldots ,n-k.$

The transmitted polynomial is corrupted in transit by an error polynomial $e(x)=\sum _{i=0}^{n-1}e_{i}x^{i}$ to produce the received polynomial $r(x)=s(x)+e(x).$

Coefficient *ei* will be zero if there is no error at that power of *x*, and nonzero if there is an error. If there are *ν* errors at distinct powers *ik* of *x*, then $e(x)=\sum _{k=1}^{\nu }e_{i_{k}}x^{i_{k}}.$

The goal of the decoder is to find the number of errors (*ν*), the positions of the errors (*ik*), and the error values at those positions (*eik*). From those, *e*(*x*) can be calculated and subtracted from *r*(*x*) to get the originally sent message *s*(*x*).

#### Syndrome decoding

The decoder starts by evaluating the polynomial as received at points $\alpha ^{1}\dots \alpha ^{n-k}$ . We call the results of that evaluation the "syndromes" *S**j*. They are defined as ${\begin{aligned}S_{j}&=r(\alpha ^{j})=s(\alpha ^{j})+e(\alpha ^{j})=0+e(\alpha ^{j})\\&=e(\alpha ^{j})\\&=\sum _{k=1}^{\nu }e_{i_{k}}{(\alpha ^{j})}^{i_{k}},\quad j=1,2,\ldots ,n-k.\end{aligned}}$ Note that $s(\alpha ^{j})=0$ because $s(x)$ has roots at $\alpha ^{j}$ , as shown in the previous section.

The advantage of looking at the syndromes is that the message polynomial drops out. In other words, the syndromes only relate to the error and are unaffected by the actual contents of the message being transmitted. If the syndromes are all zero, the algorithm stops here and reports that the message was not corrupted in transit.

#### Error locators and error values

For convenience, define the **error locators** *Xk* and **error values** *Yk* as $X_{k}=\alpha ^{i_{k}},\quad Y_{k}=e_{i_{k}}.$

Then the syndromes can be written in terms of these error locators and error values as $S_{j}=\sum _{k=1}^{\nu }Y_{k}X_{k}^{j}.$

This definition of the syndrome values is equivalent to the previous since ${(\alpha ^{j})}^{i_{k}}=\alpha ^{j\cdot i_{k}}={(\alpha ^{i_{k}})}^{j}=X_{k}^{j}$ .

The syndromes give a system of *n* − *k* ≥ 2*ν* equations in 2*ν* unknowns, but that system of equations is nonlinear in the *Xk* and does not have an obvious solution. However, if the *Xk* were known (see below), then the syndrome equations provide a linear system of equations ${\begin{bmatrix}X_{1}^{1}&X_{2}^{1}&\cdots &X_{\nu }^{1}\\X_{1}^{2}&X_{2}^{2}&\cdots &X_{\nu }^{2}\\\vdots &\vdots &\ddots &\vdots \\X_{1}^{n-k}&X_{2}^{n-k}&\cdots &X_{\nu }^{n-k}\\\end{bmatrix}}{\begin{bmatrix}Y_{1}\\Y_{2}\\\vdots \\Y_{\nu }\end{bmatrix}}={\begin{bmatrix}S_{1}\\S_{2}\\\vdots \\S_{n-k}\end{bmatrix}},$ which can easily be solved for the *Yk* error values.

Consequently, the problem is finding the *Xk*, because then the leftmost matrix would be known, and both sides of the equation could be multiplied by its inverse, yielding Y*k*

In the variant of this algorithm where the locations of the errors are already known (when it is being used as an erasure code), this is the end. The error locations (*Xk*) are already known by some other method (for example, in an FM transmission, the sections where the bitstream was unclear or overcome with interference are probabilistically determinable from frequency analysis). In this scenario, up to $n-k$ errors can be corrected.

The rest of the algorithm serves to locate the errors and will require syndrome values up to $2\nu$ , instead of just the $\nu$ used thus far. This is why twice as many error-correcting symbols need to be added as can be corrected without knowing their locations.

#### Error locator polynomial

There is a linear recurrence relation that gives rise to a system of linear equations. Solving those equations identifies those error locations *Xk*.

Define the **error locator polynomial** Λ(*x*) as $\Lambda (x)=\prod _{k=1}^{\nu }(1-xX_{k})=1+\Lambda _{1}x^{1}+\Lambda _{2}x^{2}+\cdots +\Lambda _{\nu }x^{\nu }.$

The zeros of Λ(*x*) are the reciprocals $X_{k}^{-1}$ . This follows from the above product notation construction, since if $x=X_{k}^{-1}$ , then one of the multiplied terms will be zero, $(1-X_{k}^{-1}\cdot X_{k})=1-1=0$ , making the whole polynomial evaluate to zero: $\Lambda (X_{k}^{-1})=0.$

Let j be any integer such that $1\leq j\leq \nu$ . Multiply both sides by $Y_{k}X_{k}^{j+\nu }$ , and it will still be zero: ${\begin{aligned}&Y_{k}X_{k}^{j+\nu }\Lambda (X_{k}^{-1})=0,\\&Y_{k}X_{k}^{j+\nu }(1+\Lambda _{1}X_{k}^{-1}+\Lambda _{2}X_{k}^{-2}+\cdots +\Lambda _{\nu }X_{k}^{-\nu })=0,\\&Y_{k}X_{k}^{j+\nu }+\Lambda _{1}Y_{k}X_{k}^{j+\nu }X_{k}^{-1}+\Lambda _{2}Y_{k}X_{k}^{j+\nu }X_{k}^{-2}+\cdots +\Lambda _{\nu }Y_{k}X_{k}^{j+\nu }X_{k}^{-\nu }=0,\\&Y_{k}X_{k}^{j+\nu }+\Lambda _{1}Y_{k}X_{k}^{j+\nu -1}+\Lambda _{2}Y_{k}X_{k}^{j+\nu -2}+\cdots +\Lambda _{\nu }Y_{k}X_{k}^{j}=0.\end{aligned}}$

Sum for *k* = 1 to *ν*, and it will still be zero: $\sum _{k=1}^{\nu }(Y_{k}X_{k}^{j+\nu }+\Lambda _{1}Y_{k}X_{k}^{j+\nu -1}+\Lambda _{2}Y_{k}X_{k}^{j+\nu -2}+\cdots +\Lambda _{\nu }Y_{k}X_{k}^{j})=0.$

Collect each term into its own sum: $\left(\sum _{k=1}^{\nu }Y_{k}X_{k}^{j+\nu }\right)+\left(\sum _{k=1}^{\nu }\Lambda _{1}Y_{k}X_{k}^{j+\nu -1}\right)+\left(\sum _{k=1}^{\nu }\Lambda _{2}Y_{k}X_{k}^{j+\nu -2}\right)+\cdots +\left(\sum _{k=1}^{\nu }\Lambda _{\nu }Y_{k}X_{k}^{j}\right)=0.$

Extract the constant values of $\Lambda$ that are unaffected by the summation: $\left(\sum _{k=1}^{\nu }Y_{k}X_{k}^{j+\nu }\right)+\Lambda _{1}\left(\sum _{k=1}^{\nu }Y_{k}X_{k}^{j+\nu -1}\right)+\Lambda _{2}\left(\sum _{k=1}^{\nu }Y_{k}X_{k}^{j+\nu -2}\right)+\cdots +\Lambda _{\nu }\left(\sum _{k=1}^{\nu }Y_{k}X_{k}^{j}\right)=0.$

These summations are now equivalent to the syndrome values, which we know and can substitute in. This therefore reduces to $S_{j+\nu }+\Lambda _{1}S_{j+\nu -1}+\cdots +\Lambda _{\nu -1}S_{j+1}+\Lambda _{\nu }S_{j}=0.$

Subtracting $S_{j+\nu }$ from both sides yields $S_{j}\Lambda _{\nu }+S_{j+1}\Lambda _{\nu -1}+\cdots +S_{j+\nu -1}\Lambda _{1}=-S_{j+\nu }.$

Recall that *j* was chosen to be any integer between 1 and *v* inclusive, and this equivalence is true for all such values. Therefore, we have *v* linear equations, not just one. This system of linear equations can therefore be solved for the coefficients Λ*i* of the error-location polynomial: ${\begin{bmatrix}S_{1}&S_{2}&\cdots &S_{\nu }\\S_{2}&S_{3}&\cdots &S_{\nu +1}\\\vdots &\vdots &\ddots &\vdots \\S_{\nu }&S_{\nu +1}&\cdots &S_{2\nu -1}\end{bmatrix}}{\begin{bmatrix}\Lambda _{\nu }\\\Lambda _{\nu -1}\\\vdots \\\Lambda _{1}\end{bmatrix}}={\begin{bmatrix}-S_{\nu +1}\\-S_{\nu +2}\\\vdots \\-S_{\nu +\nu }\end{bmatrix}}.$ The above assumes that the decoder knows the number of errors *ν*, but that number has not been determined yet. The PGZ decoder does not determine *ν* directly but rather searches for it by trying successive values. The decoder first assumes the largest value for a trial *ν* and sets up the linear system for that value. If the equations can be solved (i.e., the matrix determinant is nonzero), then that trial value is the number of errors. If the linear system cannot be solved, then the trial *ν* is reduced by one and the next smaller system is examined.

#### Find the roots of the error locator polynomial

Use the coefficients Λ*i* found in the last step to build the error location polynomial. The roots of the error location polynomial can be found by exhaustive search. The error locators *Xk* are the reciprocals of those roots. The order of coefficients of the error location polynomial can be reversed, in which case the roots of that reversed polynomial are the error locators $X_{k}$ (not their reciprocals $X_{k}^{-1}$ ). Chien search is an efficient implementation of this step.

#### Calculate the error values

Once the error locators *Xk* are known, the error values can be determined. This can be done by direct solution for *Yk* in the error equations matrix given above, or using the Forney algorithm.

#### Calculate the error locations

Calculate *ik* by taking the log base $\alpha$ of *Xk*. This is generally done using a precomputed lookup table.

#### Fix the errors

Finally, *e*(*x*) is generated from *ik* and *eik* and then is subtracted from *r*(*x*) to get the originally sent message *s*(*x*), with errors corrected.

#### Example

Consider the Reed–Solomon code defined in *GF*(929) with *α* = 3 and *t* = 4 (this is used in PDF417 barcodes) for a RS(7,3) code. The generator polynomial is $g(x)=(x-3)(x-3^{2})(x-3^{3})(x-3^{4})=x^{4}+809x^{3}+723x^{2}+568x+522.$ If the message polynomial is *p*(*x*) = 3 *x*2 + 2 *x* + 1, then a systematic codeword is encoded as follows: $s_{r}(x)=p(x)\,x^{t}{\bmod {g}}(x)=547x^{3}+738x^{2}+442x+455,$ $s(x)=p(x)\,x^{t}-s_{r}(x)=3x^{6}+2x^{5}+1x^{4}+382x^{3}+191x^{2}+487x+474.$ Errors in transmission might cause this to be received instead: $r(x)=s(x)+e(x)=3x^{6}+2x^{5}+123x^{4}+456x^{3}+191x^{2}+487x+474.$ The syndromes are calculated by evaluating *r* at powers of *α*: $S_{1}=r(3^{1})=3\cdot 3^{6}+2\cdot 3^{5}+123\cdot 3^{4}+456\cdot 3^{3}+191\cdot 3^{2}+487\cdot 3+474=732,$ $S_{2}=r(3^{2})=637,\quad S_{3}=r(3^{3})=762,\quad S_{4}=r(3^{4})=925,$ yielding the system ${\begin{bmatrix}732&637\\637&762\end{bmatrix}}{\begin{bmatrix}\Lambda _{2}\\\Lambda _{1}\end{bmatrix}}={\begin{bmatrix}-762\\-925\end{bmatrix}}={\begin{bmatrix}167\\004\end{bmatrix}}.$

Using Gaussian elimination, ${\begin{bmatrix}001&000\\000&001\end{bmatrix}}{\begin{bmatrix}\Lambda _{2}\\\Lambda _{1}\end{bmatrix}}={\begin{bmatrix}329\\821\end{bmatrix}},$ so $\Lambda (x)=329x^{2}+821x+001,$ with roots *x*1 = 757 = 3−3 and *x*2 = 562 = 3−4. The coefficients can be reversed: $R(x)=001x^{2}+821x+329,$ to produce roots 27 = 33 and 81 = 34 with positive exponents, but typically this isn't used. The logarithm of the inverted roots corresponds to the error locations (right to left, location 0 is the last term in the codeword).

To calculate the error values, apply the Forney algorithm: $\Omega (x)=S(x)\Lambda (x){\bmod {x}}^{4}=546x+732,$ $\Lambda '(x)=658x+821,$ $e_{1}=-\Omega (x_{1})/\Lambda '(x_{1})=074,$ $e_{2}=-\Omega (x_{2})/\Lambda '(x_{2})=122.$

Subtracting $e_{1}x^{3}+e_{2}x^{4}=74x^{3}+122x^{4}$ from the received polynomial *r*(*x*) reproduces the original codeword *s*.

### Berlekamp–Massey decoder

The Berlekamp–Massey algorithm is an alternate iterative procedure for finding the error locator polynomial. During each iteration, it calculates a discrepancy based on a current instance of Λ(*x*) with an assumed number of errors *e*: $\Delta =S_{i}+\Lambda _{1}\ S_{i-1}+\cdots +\Lambda _{e}\ S_{i-e}$ and then adjusts Λ(*x*) and *e* so that a recalculated Δ would be zero. The article Berlekamp–Massey algorithm has a detailed description of the procedure. In the following example, *C*(*x*) is used to represent Λ(*x*).

#### Example

Using the same data as the Peterson Gorenstein Zierler example above:

| *n* | *S**n*+1 | *d* | *C* | *B* | *b* | *m* |
|---|---|---|---|---|---|---|
| 0 | 732 | 732 | 197 *x* + 1 | 1 | 732 | 1 |
| 1 | 637 | 846 | 173 *x* + 1 | 1 | 732 | 2 |
| 2 | 762 | 412 | 634 *x*2 + 173 *x* + 1 | 173 *x* + 1 | 412 | 1 |
| 3 | 925 | 576 | 329 *x*2 + 821 *x* + 1 | 173 *x* + 1 | 412 | 2 |

The final value of *C* is the error locator polynomial, Λ(*x*).

### Sugiyama decoder

Another iterative method for calculating both the error locator polynomial and the error value polynomial is based on Sugiyama's adaptation of the extended Euclidean algorithm.

Define *S*(*x*), Λ(*x*), and Ω(*x*) for *t* syndromes and *e* errors: ${\begin{aligned}S(x)&=S_{t}x^{t-1}+S_{t-1}x^{t-2}+\cdots +S_{2}x+S_{1}\\[1ex]\Lambda (x)&=\Lambda _{e}x^{e}+\Lambda _{e-1}x^{e-1}+\cdots +\Lambda _{1}x+1\\[1ex]\Omega (x)&=\Omega _{e}x^{e}+\Omega _{e-1}x^{e-1}+\cdots +\Omega _{1}x+\Omega _{0}\end{aligned}}$

The key equation is: $\Lambda (x)S(x)=Q(x)x^{t}+\Omega (x)$

For *t* = 6 and *e* = 3: ${\begin{bmatrix}\Lambda _{3}S_{6}&x^{8}\\\Lambda _{2}S_{6}+\Lambda _{3}S_{5}&x^{7}\\\Lambda _{1}S_{6}+\Lambda _{2}S_{5}+\Lambda _{3}S_{4}&x^{6}\\S_{6}+\Lambda _{1}S_{5}+\Lambda _{2}S_{4}+\Lambda _{3}S_{3}&x^{5}\\S_{5}+\Lambda _{1}S_{4}+\Lambda _{2}S_{3}+\Lambda _{3}S_{2}&x^{4}\\S_{4}+\Lambda _{1}S_{3}+\Lambda _{2}S_{2}+\Lambda _{3}S_{1}&x^{3}\\S_{3}+\Lambda _{1}S_{2}+\Lambda _{2}S_{1}&x^{2}\\S_{2}+\Lambda _{1}S_{1}&x\\S_{1}\end{bmatrix}}={\begin{bmatrix}Q_{2}x^{8}\\Q_{1}x^{7}\\Q_{0}x^{6}\\0\\0\\0\\\Omega _{2}x^{2}\\\Omega _{1}x\\\Omega _{0}\end{bmatrix}}$

The middle terms are zero due to the relationship between Λ and syndromes.

The extended Euclidean algorithm can find a series of polynomials of the form

A

i

(

x

)

S

(

x

) +

B

i

(

x

)

x

t

=

R

i

(

x

)

where the degree of *R* decreases as *i* increases. Once the degree of *R**i*(*x*) < *t*/2, then

A

i

(

x

) = Λ(

x

)

B

i

(

x

) = −Q(

x

)

R

i

(

x

) = Ω(

x

).

*B*(*x*) and *Q*(*x*) don't need to be saved, so the algorithm becomes:

```
R−1 := xt
R0  := S(x)
A−1 := 0
A0  := 1
i := 0
while degree of Ri ≥ t/2
    i := i + 1
    Q := Ri-2 / Ri-1
    Ri := Ri-2 - Q Ri-1
    Ai := Ai-2 - Q Ai-1
```

to set low order term of Λ(*x*) to 1, divide Λ(*x*) and Ω(*x*) by *A**i*(0):

Λ(

x

) =

A

i

/

A

i

(0)

Ω(

x

) =

R

i

/

A

i

(0)

*A**i*(0) is the constant (low order) term of Ai.

#### Example

Using the same data as the Peterson–Gorenstein–Zierler example above:

| *i* | R*i* | A*i* |
|---|---|---|
| −1 | 001 *x*4 + 000 *x*3 + 000 *x*2 + 000 *x* + 000 | 000 |
| 0 | 925 *x*3 + 762 *x*2 + 637 *x* + 732 | 001 |
| 1 | 683 *x*2 + 676 *x* + 024 | 697 *x* + 396 |
| 2 | 673 *x* + 596 | 608 *x*2 + 704 *x* + 544 |

Λ(

x

) =

A

2

/ 544 = 329

x

2

+ 821

x

+ 001

Ω(

x

) =

R

2

/ 544 = 546

x

+ 732

### Decoder using discrete Fourier transform

A discrete Fourier transform can be used for decoding. To avoid conflict with syndrome names, let *c*(*x*) = *s*(*x*) the encoded codeword. *r*(*x*) and *e*(*x*) are the same as above. Define *C*(*x*), *E*(*x*), and *R*(*x*) as the discrete Fourier transforms of *c*(*x*), *e*(*x*), and *r*(*x*). Since *r*(*x*) = *c*(*x*) + *e*(*x*), and since a discrete Fourier transform is a linear operator, *R*(*x*) = *C*(*x*) + *E*(*x*).

Transform *r*(*x*) to *R*(*x*) using discrete Fourier transform. Since the calculation for a discrete Fourier transform is the same as the calculation for syndromes, *t* coefficients of *R*(*x*) and *E*(*x*) are the same as the syndromes: $R_{j}=E_{j}=S_{j}=r(\alpha ^{j})\qquad {\text{for }}1\leq j\leq t$

Use $R_{1}$ through $R_{t}$ as syndromes (they're the same) and generate the error locator polynomial using the methods from any of the above decoders.

Let *v* = number of errors. Generate *E*(*x*) using the known coefficients $E_{1}$ to $E_{t}$ , the error locator polynomial, and these formulas ${\begin{aligned}E_{0}&=-{\frac {1}{\Lambda _{v}}}(E_{v}+\Lambda _{1}E_{v-1}+\cdots +\Lambda _{v-1}E_{1})\\E_{j}&=-(\Lambda _{1}E_{j-1}+\Lambda _{2}E_{j-2}+\cdots +\Lambda _{v}E_{j-v})&{\text{for }}t<j<n\end{aligned}}$

Then calculate *C*(*x*) = *R*(*x*) − *E*(*x*) and take the inverse transform (polynomial interpolation) of *C*(*x*) to produce *c*(*x*).

### Decoding beyond the error-correction bound

The Singleton bound states that the minimum distance d of a linear block code of size (n,k) is upper-bounded by *n* - *k* + 1. The distance d was usually understood to limit the error-correction capability to ⌊(*d* - 1) / 2⌋. The Reed–Solomon code achieves this bound with equality, and can thus correct up to ⌊(*n* - *k*) / 2⌋ errors. However, this error-correction bound is not exact.

In 1999, Madhu Sudan and Venkatesan Guruswami at MIT published "Improved Decoding of Reed–Solomon and Algebraic-Geometry Codes" introducing an algorithm that allowed for the correction of errors beyond half the minimum distance of the code. It applies to Reed–Solomon codes and more generally to algebraic geometric codes. This algorithm produces a list of codewords (it is a list-decoding algorithm) and is based on interpolation and factorization of polynomials over *GF*(2*m*) and its extensions.

In 2023, coding theorists showed that Reed-Solomon codes defined over random evaluation points can achieve achieve list decoding capacity (up to *n* - *k* errors) over linear size alphabets with high probability. These results do not provide an algorithm for performing the decoding.

### Soft-decoding

The algebraic decoding methods described above are hard-decision methods, which means that for every symbol a hard decision is made about its value. For example, a decoder could associate with each symbol an additional value corresponding to the channel demodulator's confidence in the correctness of the symbol. The advent of LDPC and turbo codes, which employ iterated soft-decision belief propagation decoding methods to achieve error-correction performance close to the theoretical limit, has spurred interest in applying soft-decision decoding to conventional algebraic codes. In 2003, Ralf Koetter and Alexander Vardy presented a polynomial-time soft-decision algebraic list-decoding algorithm for Reed–Solomon codes, which was based upon the work by Sudan and Guruswami. In 2016, Steven J. Franke and Joseph H. Taylor published a novel soft-decision decoder.
