---
title: "Gray code (part 2/2)"
source: https://en.wikipedia.org/wiki/Gray_code
domain: rotary-encoders
license: CC-BY-SA-4.0
tags: rotary encoder, incremental encoder, gray code, resolver device
fetched: 2026-07-02
part: 2/2
---

## Special types of Gray codes

In practice, "Gray code" almost always refers to a binary-reflected Gray code (BRGC). However, mathematicians have discovered other kinds of Gray codes. Like BRGCs, each consists of a list of words, where each word differs from the next in only one digit (each word has a Hamming distance of 1 from the next word).

### Gray codes with *n* bits and of length less than 2*n*

It is possible to construct binary Gray codes with *n* bits with a length of less than 2*n*, if the length is even. One possibility is to start with a balanced Gray code and remove pairs of values at either the beginning and the end, or in the middle. OEIS sequence A290772 gives the number of possible Gray sequences of length 2*n* that include zero and use the minimum number of bits.

### *n*-ary Gray code

| *Ternary number → ternary Gray code* 0 → 000 1 → 001 2 → 002 10 → 012 11 → 011 12 → 010 20 → 020 21 → 021 22 → 022 100 → 122 101 → 121 102 → 120 110 → 110 111 → 111 112 → 112 120 → 102 121 → 101 122 → 100 200 → 200 201 → 201 202 → 202 210 → 212 211 → 211 212 → 210 220 → 220 221 → 221 222 → 222 |
|---|

There are many specialized types of Gray codes other than the binary-reflected Gray code. One such type of Gray code is the ***n*-ary Gray code**, also known as a **non-Boolean Gray code**. As the name implies, this type of Gray code uses non-Boolean values in its encodings.

For example, a 3-ary (ternary) Gray code would use the values 0,1,2. The (*n*, *k*)-*Gray code* is the *n*-ary Gray code with *k* digits. The sequence of elements in the (3, 2)-Gray code is: 00,01,02,12,11,10,20,21,22. The (*n*, *k*)-Gray code may be constructed recursively, as the BRGC, or may be constructed iteratively. An algorithm to iteratively generate the (*N*, *k*)-Gray code is presented (in C):

```mw
// inputs: base, digits, value
// output: Gray
// Convert a value to a Gray code with the given base and digits.
// Iterating through a sequence of values would result in a sequence
// of Gray codes in which only one digit changes at a time.
void toGray(unsigned base, unsigned digits, unsigned value, unsigned gray[digits])
{ 
	unsigned baseN[digits];	// Stores the ordinary base-N number, one digit per entry
	unsigned i;		// The loop variable
 
	// Put the normal baseN number into the baseN array. For base 10, 109 
	// would be stored as [9,0,1]
	for (i = 0; i < digits; i++) {
		baseN[i] = value % base;
		value    = value / base;
	}
 
	// Convert the normal baseN number into the Gray code equivalent. Note that
	// the loop starts at the most significant digit and goes down.
	unsigned shift = 0;
	while (i--) {
		// The Gray digit gets shifted down by the sum of the higher
		// digits.
		gray[i] = (baseN[i] + shift) % base;
		shift = shift + base - gray[i];	// Subtract from base so shift is positive
	}
}
// EXAMPLES
// input: value = 1899, base = 10, digits = 4
// output: baseN[] = [9,9,8,1], gray[] = [0,1,7,1]
// input: value = 1900, base = 10, digits = 4
// output: baseN[] = [0,0,9,1], gray[] = [0,1,8,1]
```

There are other Gray code algorithms for (*n*, *k*)-Gray codes. The (*n*, *k*)-Gray code produced by the above algorithm is always cyclical; some algorithms, such as that by Guan, lack this property when *k* is odd. On the other hand, while only one digit at a time changes with this method, it can change by wrapping (looping from *n* − 1 to 0). In Guan's algorithm, the count alternately rises and falls, so that the numeric difference between two Gray code digits is always one.

Gray codes are not uniquely defined, because a permutation of the columns of such a code is a Gray code too. The above procedure produces a code in which the lower the significance of a digit, the more often it changes, making it similar to normal counting methods.

See also Skew binary number system, a variant ternary number system where at most two digits change on each increment, as each increment can be done with at most one digit carry operation.

### Balanced Gray code

Although the binary reflected Gray code is useful in many scenarios, it is not optimal in certain cases because of a lack of "uniformity". In **balanced Gray codes**, the number of changes in different coordinate positions are as close as possible. To make this more precise, let *G* be an *R*-ary complete Gray cycle having transition sequence $(\delta _{k})$ ; the *transition counts* (*spectrum*) of *G* are the collection of integers defined by

$\lambda _{k}=|\{j\in \mathbb {Z} _{R^{n}}:\delta _{j}=k\}|\,,{\text{ for }}k\in \mathbb {Z} _{n}$

A Gray code is *uniform* or *uniformly balanced* if its transition counts are all equal, in which case we have $\lambda _{k}={\tfrac {R^{n}}{n}}$ for all *k*. Clearly, when $R=2$ , such codes exist only if *n* is a power of 2. If *n* is not a power of 2, it is possible to construct *well-balanced* binary codes where the difference between two transition counts is at most 2; so that (combining both cases) every transition count is either $2\left\lfloor {\tfrac {2^{n}}{2n}}\right\rfloor$ or $2\left\lceil {\tfrac {2^{n}}{2n}}\right\rceil$ . Gray codes can also be *exponentially balanced* if all of their transition counts are adjacent powers of two, and such codes exist for every power of two.

For example, a balanced 4-bit Gray code has 16 transitions, which can be evenly distributed among all four positions (four transitions per position), making it uniformly balanced:

0

1

1 1 1 1 1

0

0 0 0 0 0

1

1

0

0 0

1

1 1 1

0

0

1

1 1 1

0

0 0 0

0 0 0 0

1

1 1 1 1

0

0

1

1 1

0

0

0

0 0

1

1

0

0 0 0 0

1

1 1 1 1 1

whereas a balanced 5-bit Gray code has a total of 32 transitions, which cannot be evenly distributed among the positions. In this example, four positions have six transitions each, and one has eight:

1

1 1 1 1

0

0 0 0

1

1 1 1 1 1

0

0

1

1 1 1 1

0

0 0 0 0 0 0 0 0 0

0 0 0

1

1 1 1 1 1 1 1

0

0 0 0 0 0 0

1

1 1 1 1 1

0

0 0

1

1

0

0 0

1 1

0

0

1

1 1

0

0 0 0 0 0

1

1 1

0

0 0

1

1 1 1 1 1

0

0 0 0 0

1

1

1

0

0 0 0 0 0 0

1

1 1 1 1 1

0

0 0 0 0 0

1

1 1 1 1 1 1 1

0

0 0

1

1 1 1 1 1 1

0

0 0 0

1

1

0

0 0 0 0 0 0 0 0

1

1

0

0 0

1

1 1 1 1 1

We will now show a construction and implementation for well-balanced binary Gray codes which allows us to generate an *n*-digit balanced Gray code for every *n*. The main principle is to inductively construct an (*n* + 2)-digit Gray code $G'$ given an *n*-digit Gray code *G* in such a way that the balanced property is preserved. To do this, we consider partitions of $G=g_{0},\ldots ,g_{2^{n}-1}$ into an even number *L* of non-empty blocks of the form

$\left\{g_{0}\right\},\left\{g_{1},\ldots ,g_{k_{2}}\right\},\left\{g_{k_{2}+1},\ldots ,g_{k_{3}}\right\},\ldots ,\left\{g_{k_{L-2}+1},\ldots ,g_{-2}\right\},\left\{g_{-1}\right\}$

where $k_{1}=0$ , $k_{L-1}=-2$ , and $k_{L}\equiv -1{\pmod {2^{n}}}$ ). This partition induces an $(n+2)$ -digit Gray code given by

${\begin{aligned}&{\mathtt {00}}g_{0},\\&{\mathtt {00}}g_{1},\ldots ,{\mathtt {00}}g_{k_{2}},{\mathtt {01}}g_{k_{2}},\ldots ,{\mathtt {01}}g_{1},{\mathtt {11}}g_{1},\ldots ,{\mathtt {11}}g_{k_{2}},\\&{\mathtt {11}}g_{k_{2}+1},\ldots ,{\mathtt {11}}g_{k_{3}},{\mathtt {01}}g_{k_{3}},\ldots ,{\mathtt {01}}g_{k_{2}+1},{\mathtt {00}}g_{k_{2}+1},\ldots ,{\mathtt {00}}g_{k_{3}},\ldots ,\\&{\mathtt {00}}g_{-2},{\mathtt {00}}g_{-1},{\mathtt {10}}g_{-1},{\mathtt {10}}g_{-2},\ldots ,{\mathtt {10}}g_{0},{\mathtt {11}}g_{0},{\mathtt {11}}g_{-1},{\mathtt {01}}g_{-1},{\mathtt {01}}g_{0}\end{aligned}}$

If we define the *transition multiplicities*

$m_{i}=\left|\left\{j:\delta _{k_{j}}=i,1\leq j\leq L\right\}\right|$

to be the number of times the digit in position *i* changes between consecutive blocks in a partition, then for the (*n* + 2)-digit Gray code induced by this partition the transition spectrum $\lambda '_{i}$ is

$\lambda '_{i}={\begin{cases}4\lambda _{i}-2m_{i},&{\text{if }}0\leq i<n\\L,&{\text{ otherwise }}\end{cases}}$

The delicate part of this construction is to find an adequate partitioning of a balanced *n*-digit Gray code such that the code induced by it remains balanced, but for this only the transition multiplicities matter; joining two consecutive blocks over a digit i transition and splitting another block at another digit i transition produces a different Gray code with exactly the same transition spectrum $\lambda '_{i}$ , so one may for example designate the first $m_{i}$ transitions at digit i as those that fall between two blocks. Uniform codes can be found when $R\equiv 0{\pmod {4}}$ and $R^{n}\equiv 0{\pmod {n}}$ , and this construction can be extended to the *R*-ary case as well.

### Long run Gray codes

Long run (or *maximum gap*) Gray codes maximize the distance between consecutive changes of digits in the same position. That is, the minimum run-length of any bit remains unchanged for as long as possible.

### Monotonic Gray codes

Monotonic codes are useful in the theory of interconnection networks, especially for minimizing dilation for linear arrays of processors. If we define the *weight* of a binary string to be the number of 1s in the string, then although we clearly cannot have a Gray code with strictly increasing weight, we may want to approximate this by having the code run through two adjacent weights before reaching the next one.

We can formalize the concept of monotone Gray codes as follows: consider the partition of the hypercube $Q_{n}=(V_{n},E_{n})$ into *levels* of vertices that have equal weight, i.e.

$V_{n}(i)=\{v\in V_{n}:v{\text{ has weight }}i\}$

for $0\leq i\leq n$ . These levels satisfy $|V_{n}(i)|=\textstyle {\binom {n}{i}}$ . Let $Q_{n}(i)$ be the subgraph of $Q_{n}$ induced by $V_{n}(i)\cup V_{n}(i+1)$ , and let $E_{n}(i)$ be the edges in $Q_{n}(i)$ . A monotonic Gray code is then a Hamiltonian path in $Q_{n}$ such that whenever $\delta _{1}\in E_{n}(i)$ comes before $\delta _{2}\in E_{n}(j)$ in the path, then $i\leq j$ .

An elegant construction of monotonic *n*-digit Gray codes for any *n* is based on the idea of recursively building subpaths $P_{n,j}$ of length $2\textstyle {\binom {n}{j}}$ having edges in $E_{n}(j)$ . We define $P_{1,0}=({\mathtt {0}},{\mathtt {1}})$ , $P_{n,j}=\emptyset$ whenever $j<0$ or $j\geq n$ , and

$P_{n+1,j}={\mathtt {1}}P_{n,j-1}^{\pi _{n}},{\mathtt {0}}P_{n,j}$

otherwise. Here, $\pi _{n}$ is a suitably defined permutation and $P^{\pi }$ refers to the path *P* with its coordinates permuted by $\pi$ . These paths give rise to two monotonic *n*-digit Gray codes $G_{n}^{(1)}$ and $G_{n}^{(2)}$ given by

$G_{n}^{(1)}=P_{n,0}P_{n,1}^{R}P_{n,2}P_{n,3}^{R}\cdots {\text{ and }}G_{n}^{(2)}=P_{n,0}^{R}P_{n,1}P_{n,2}^{R}P_{n,3}\cdots$

The choice of $\pi _{n}$ which ensures that these codes are indeed Gray codes turns out to be $\pi _{n}=E^{-1}\left(\pi _{n-1}^{2}\right)$ . The first few values of $P_{n,j}$ are shown in the table below.

| $P_{n,j}$ | *j* = 0 | *j* = 1 | *j* = 2 | *j* = 3 |
|---|---|---|---|---|
| *n* = 1 | 0, 1 |   |   |   |
| *n* = 2 | 00, 01 | 10, 11 |   |   |
| *n* = 3 | 000, 001 | 100, 110, 010, 011 | 101, 111 |   |
| *n* = 4 | 0000, 0001 | 1000, 1100, 0100, 0110, 0010, 0011 | 1010, 1011, 1001, 1101, 0101, 0111 | 1110, 1111 |

These monotonic Gray codes can be efficiently implemented in such a way that each subsequent element can be generated in *O*(*n*) time. The algorithm is most easily described using coroutines.

Monotonic codes have an interesting connection to the Lovász conjecture, which states that every connected vertex-transitive graph contains a Hamiltonian path. The "middle-level" subgraph $Q_{2n+1}(n)$ is vertex-transitive (that is, its automorphism group is transitive, so that each vertex has the same "local environment" and cannot be differentiated from the others, since we can relabel the coordinates as well as the binary digits to obtain an automorphism) and the problem of finding a Hamiltonian path in this subgraph is called the "middle-levels problem", which can provide insights into the more general conjecture. The question has been answered affirmatively for $n\leq 15$ , and the preceding construction for monotonic codes ensures a Hamiltonian path of length at least 0.839‍*N*, where *N* is the number of vertices in the middle-level subgraph.

### Beckett–Gray code

Another type of Gray code, the **Beckett–Gray code**, is named for Irish playwright Samuel Beckett, who was interested in symmetry. His play "Quad" features four actors and is divided into sixteen time periods. Each period ends with one of the four actors entering or leaving the stage. The play begins and ends with an empty stage, and Beckett wanted each subset of actors to appear on stage exactly once. Clearly the set of actors currently on stage can be represented by a 4-bit binary Gray code. Beckett, however, placed an additional restriction on the script: he wished the actors to enter and exit so that the actor who had been on stage the longest would always be the one to exit. The actors could then be represented by a FIFO queue, so that (of the actors onstage) the actor being dequeued is always the one who was enqueued first. Beckett was unable to find a Beckett–Gray code for his play, and indeed, an exhaustive listing of all possible sequences reveals that no such code exists for *n* = 4. It is known today that such codes do exist for *n* = 2, 5, 6, 7, and 8, and do not exist for *n* = 3 or 4. An example of an 8-bit Beckett–Gray code can be found in Donald Knuth's *Art of Computer Programming*. According to Sawada and Wong, the search space for *n* = 6 can be explored in 15 hours, and more than 9500 solutions for the case *n* = 7 have been found.

### Snake-in-the-box codes

Snake-in-the-box codes, or *snakes*, are the sequences of nodes of induced paths in an *n*-dimensional hypercube graph, and coil-in-the-box codes, or *coils*, are the sequences of nodes of induced cycles in a hypercube. Viewed as Gray codes, these sequences have the property of being able to detect any single-bit coding error. Codes of this type were first described by William H. Kautz in the late 1950s; since then, there has been much research on finding the code with the largest possible number of codewords for a given hypercube dimension.

### Single-track Gray code

Yet another kind of Gray code is the **single-track Gray code** (STGC) developed by Norman B. Spedding and refined by Hiltgen, Paterson and Brandestini in *Single-track Gray Codes* (1996). The STGC is a cyclical list of *P* unique binary encodings of length n such that two consecutive words differ in exactly one position, and when the list is examined as a *P* × *n* matrix, each column is a cyclic shift of the first column.

The name comes from their use with rotary encoders, where a number of tracks are being sensed by contacts, resulting for each in an output of 0 or 1. To reduce noise due to different contacts not switching at exactly the same moment in time, one preferably sets up the tracks so that the data output by the contacts are in Gray code. To get high angular accuracy, one needs lots of contacts; in order to achieve at least 1° accuracy, one needs at least 360 distinct positions per revolution, which requires a minimum of 9 bits of data, and thus the same number of contacts.

If all contacts are placed at the same angular position, then 9 tracks are needed to get a standard BRGC with at least 1° accuracy. However, if the manufacturer moves a contact to a different angular position (but at the same distance from the center shaft), then the corresponding "ring pattern" needs to be rotated the same angle to give the same output. If the most significant bit (the inner ring in Figure 1) is rotated enough, it exactly matches the next ring out. Since both rings are then identical, the inner ring can be cut out, and the sensor for that ring moved to the remaining, identical ring (but offset at that angle from the other sensor on that ring). Those two sensors on a single ring make a quadrature encoder. That reduces the number of tracks for a "1° resolution" angular encoder to 8 tracks. Reducing the number of tracks still further cannot be done with BRGC.

For many years, Torsten Sillke and other mathematicians believed that it was impossible to encode position on a single track such that consecutive positions differed at only a single sensor, except for the 2-sensor, 1-track quadrature encoder. So for applications where 8 tracks were too bulky, people used single-track incremental encoders (quadrature encoders) or 2-track "quadrature encoder + reference notch" encoders.

Norman B. Spedding, however, registered a patent in 1994 with several examples showing that it was possible. Although it is not possible to distinguish 2*n* positions with *n* sensors on a single track, it *is* possible to distinguish close to that many. Etzion and Paterson conjecture that when *n* is itself a power of 2, *n* sensors can distinguish at most 2*n* − 2*n* positions and that for prime *n* the limit is 2*n* − 2 positions. The authors went on to generate a 504-position single track code of length 9 which they believe is optimal. Since this number is larger than 28 = 256, more than 8 sensors are required by any code, although a BRGC could distinguish 512 positions with 9 sensors.

An STGC for *P* = 30 and *n* = 5 is reproduced here:

Single-track Gray code for 30 positions

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

0°

10000

72°

01000

144°

00100

216°

00010

288°

00001

12°

10100

84°

01010

156°

00101

228°

10010

300°

01001

24°

11100

96°

01110

168°

00111

240°

10011

312°

11001

36°

11110

108°

01111

180°

10111

252°

11011

324°

11101

48°

11010

120°

01101

192°

10110

264°

01011

336°

10101

60°

11000

132°

01100

204°

00110

276°

00011

348°

10001

Each column is a cyclic shift of the first column, and from any row to the next row only one bit changes. The single-track nature (like a code chain) is useful in the fabrication of these wheels (compared to BRGC), as only one track is needed, thus reducing their cost and size. The Gray code nature is useful (compared to chain codes, also called De Bruijn sequences), as only one sensor will change at any one time, so the uncertainty during a transition between two discrete states will only be plus or minus one unit of angular measurement the device is capable of resolving.

Since this 30 degree example was added, there has been a lot of interest in examples with higher angular resolution. In 2008, Gary Williams, based on previous work, discovered a 9-bit single track Gray code that gives a 1 degree resolution. This Gray code was used to design an actual device which was published on the site Thingiverse. This device was designed by etzenseep (Florian Bauer) in September 2022.

An STGC for *P* = 360 and *n* = 9 is reproduced here:

Single-track Gray code for 360 positions

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

Angle

Code

0°

100000001

40°

000000011

80°

000000110

120°

000001100

160°

000011000

200°

000110000

240°

001100000

280°

011000000

320°

110000000

1°

110000001

41°

100000011

81°

000000111

121°

000001110

161°

000011100

201°

000111000

241°

001110000

281°

011100000

321°

111000000

2°

111000001

42°

110000011

82°

100000111

122°

000001111

162°

000011110

202°

000111100

242°

001111000

282°

011110000

322°

111100000

3°

111000011

43°

110000111

83°

100001111

123°

000011111

163°

000111110

203°

001111100

243°

011111000

283°

111110000

323°

111100001

4°

111000111

44°

110001111

84°

100011111

124°

000111111

164°

001111110

204°

011111100

244°

111111000

284°

111110001

324°

111100011

5°

111001111

45°

110011111

85°

100111111

125°

001111111

165°

011111110

205°

111111100

245°

111111001

285°

111110011

325°

111100111

6°

111011111

46°

110111111

86°

101111111

126°

011111111

166°

111111110

206°

111111101

246°

111111011

286°

111110111

326°

111101111

7°

111011011

47°

110110111

87°

101101111

127°

011011111

167°

110111110

207°

101111101

247°

011111011

287°

111110110

327°

111101101

8°

101011011

48°

010110111

88°

101101110

128°

011011101

168°

110111010

208°

101110101

248°

011101011

288°

111010110

328°

110101101

9°

101011111

49°

010111111

89°

101111110

129°

011111101

169°

111111010

209°

111110101

249°

111101011

289°

111010111

329°

110101111

10°

101011101

50°

010111011

90°

101110110

130°

011101101

170°

111011010

210°

110110101

250°

101101011

290°

011010111

330°

110101110

11°

101010101

51°

010101011

91°

101010110

131°

010101101

171°

101011010

211°

010110101

251°

101101010

291°

011010101

331°

110101010

12°

101010111

52°

010101111

92°

101011110

132°

010111101

172°

101111010

212°

011110101

252°

111101010

292°

111010101

332°

110101011

13°

101110111

53°

011101111

93°

111011110

133°

110111101

173°

101111011

213°

011110111

253°

111101110

293°

111011101

333°

110111011

14°

001110111

54°

011101110

94°

111011100

134°

110111001

174°

101110011

214°

011100111

254°

111001110

294°

110011101

334°

100111011

15°

001010111

55°

010101110

95°

101011100

135°

010111001

175°

101110010

215°

011100101

255°

111001010

295°

110010101

335°

100101011

16°

001011111

56°

010111110

96°

101111100

136°

011111001

176°

111110010

216°

111100101

256°

111001011

296°

110010111

336°

100101111

17°

001011011

57°

010110110

97°

101101100

137°

011011001

177°

110110010

217°

101100101

257°

011001011

297°

110010110

337°

100101101

18°

001011001

58°

010110010

98°

101100100

138°

011001001

178°

110010010

218°

100100101

258°

001001011

298°

010010110

338°

100101100

19°

001111001

59°

011110010

99°

111100100

139°

111001001

179°

110010011

219°

100100111

259°

001001111

299°

010011110

339°

100111100

20°

001111101

60°

011111010

100°

111110100

140°

111101001

180°

111010011

220°

110100111

260°

101001111

300°

010011111

340°

100111110

21°

000111101

61°

001111010

101°

011110100

141°

111101000

181°

111010001

221°

110100011

261°

101000111

301°

010001111

341°

100011110

22°

000110101

62°

001101010

102°

011010100

142°

110101000

182°

101010001

222°

010100011

262°

101000110

302°

010001101

342°

100011010

23°

000100101

63°

001001010

103°

010010100

143°

100101000

183°

001010001

223°

010100010

263°

101000100

303°

010001001

343°

100010010

24°

000101101

64°

001011010

104°

010110100

144°

101101000

184°

011010001

224°

110100010

264°

101000101

304°

010001011

344°

100010110

25°

000101001

65°

001010010

105°

010100100

145°

101001000

185°

010010001

225°

100100010

265°

001000101

305°

010001010

345°

100010100

26°

000111001

66°

001110010

106°

011100100

146°

111001000

186°

110010001

226°

100100011

266°

001000111

306°

010001110

346°

100011100

27°

000110001

67°

001100010

107°

011000100

147°

110001000

187°

100010001

227°

000100011

267°

001000110

307°

010001100

347°

100011000

28°

000010001

68°

000100010

108°

001000100

148°

010001000

188°

100010000

228°

000100001

268°

001000010

308°

010000100

348°

100001000

29°

000011001

69°

000110010

109°

001100100

149°

011001000

189°

110010000

229°

100100001

269°

001000011

309°

010000110

349°

100001100

30°

000001001

70°

000010010

110°

000100100

150°

001001000

190°

010010000

230°

100100000

270°

001000001

310°

010000010

350°

100000100

31°

100001001

71°

000010011

111°

000100110

151°

001001100

191°

010011000

231°

100110000

271°

001100001

311°

011000010

351°

110000100

32°

100001101

72°

000011011

112°

000110110

152°

001101100

192°

011011000

232°

110110000

272°

101100001

312°

011000011

352°

110000110

33°

100000101

73°

000001011

113°

000010110

153°

000101100

193°

001011000

233°

010110000

273°

101100000

313°

011000001

353°

110000010

34°

110000101

74°

100001011

114°

000010111

154°

000101110

194°

001011100

234°

010111000

274°

101110000

314°

011100001

354°

111000010

35°

010000101

75°

100001010

115°

000010101

155°

000101010

195°

001010100

235°

010101000

275°

101010000

315°

010100001

355°

101000010

36°

010000111

76°

100001110

116°

000011101

156°

000111010

196°

001110100

236°

011101000

276°

111010000

316°

110100001

356°

101000011

37°

010000011

77°

100000110

117°

000001101

157°

000011010

197°

000110100

237°

001101000

277°

011010000

317°

110100000

357°

101000001

38°

010000001

78°

100000010

118°

000000101

158°

000001010

198°

000010100

238°

000101000

278°

001010000

318°

010100000

358°

101000000

39°

000000001

79°

000000010

119°

000000100

159°

000001000

199°

000010000

239°

000100000

279°

001000000

319°

010000000

359°

100000000

| Starting angle | Ending angle | Length |   |
|---|---|---|---|
| 3 | 4 | 2 |   |
| 23 | 28 | 6 |   |
| 31 | 37 | 7 |   |
| 44 | 48 | 5 |   |
| 56 | 60 | 5 |   |
| 64 | 71 | 8 |   |
| 74 | 76 | 3 |   |
| 88 | 91 | 4 |   |
| 94 | 96 | 3 |   |
| 99 | 104 | 6 |   |
| 110 | 115 | 6 |   |
| 131 | 134 | 4 |   |
| 138 | 154 | 17 |   |
| 173 | 181 | 9 |   |
| 186 | 187 | 2 |   |
| 220 | 238 | 19 |   |
| 242 | 246 | 5 |   |
| 273 | 279 | 7 |   |
| 286 | 289 | 4 |   |
| 307 | 360 | 54 |   |

### Two-dimensional Gray code

Two-dimensional Gray codes are used in communication to minimize the number of bit errors in quadrature amplitude modulation (QAM) adjacent points in the constellation. In a typical encoding the horizontal and vertical adjacent constellation points differ by a single bit, and diagonal adjacent points differ by 2 bits.

Two-dimensional Gray codes also have uses in location identifications schemes, where the code would be applied to area maps such as a Mercator projection of the earth's surface and an appropriate cyclic two-dimensional distance function such as the Mannheim metric be used to calculate the distance between two encoded locations, thereby combining the characteristics of the Hamming distance with the cyclic continuation of a Mercator projection.

### Excess Gray code

If a subsection of a specific codevalue is extracted from that value, for example the last 3 bits of a 4-bit Gray code, the resulting code will be an "excess Gray code". This code shows the property of counting backwards in those extracted bits if the original value is further increased. Reason for this is that Gray-encoded values do not show the behaviour of overflow, known from classic binary encoding, when increasing past the "highest" value.

Example: The highest 3-bit Gray code, 7, is encoded as (0)100. Adding 1 results in number 8, encoded in Gray as 1100. The last 3 bits do not overflow and count backwards if you further increase the original 4 bit code.

When working with sensors that output multiple, Gray-encoded values in a serial fashion, one should therefore pay attention whether the sensor produces those multiple values encoded in 1 single Gray code or as separate ones, as otherwise the values might appear to be counting backwards when an "overflow" is expected.


## Gray isometry

The bijective mapping { 0 ↔ 00, 1 ↔ 01, 2 ↔ 11, 3 ↔ 10 } establishes an isometry between the metric space over the finite field $\mathbb {Z} _{2}^{2}$ with the metric given by the Hamming distance and the metric space over the finite ring $\mathbb {Z} _{4}$ (the usual modular arithmetic) with the metric given by the Lee distance. The mapping is suitably extended to an isometry of the Hamming spaces $\mathbb {Z} _{2}^{2m}$ and $\mathbb {Z} _{4}^{m}$ . Its importance lies in establishing a correspondence between various "good" but not necessarily linear codes as Gray-map images in $\mathbb {Z} _{2}^{2}$ of ring-linear codes from $\mathbb {Z} _{4}$ .

There are a number of binary codes similar to Gray codes, including:

- Datex codes or Giannini codes (1954), as described by Carl P. Spaulding, use a variant of O'Brien code II.
- Codes used by Varec (c. 1954), use a variant of O'Brien code I as well as base-12 and base-16 Gray code variants.
- Lucal code (1959) aka modified reflected binary code (MRB)
- Gillham code (1961/1962), uses a variant of Datex code and O'Brien code II.
- Leslie and Russell code (1964)
- Royal Radar Establishment code
- Hoklas code (1988)

The following binary-coded decimal (BCD) codes are Gray code variants as well:

- Petherick code (1953), also known as Royal Aircraft Establishment (RAE) code.
- O'Brien codes I and II (1955) (An O'Brien type-I code was already described by Frederic A. Foss of IBM and used by Varec in 1954. Later, it was also known as Watts code or Watts reflected decimal (WRD) code and is sometimes ambiguously referred to as reflected binary modified Gray code. An O'Brien type-II code was already used by Datex in 1954.)
- Excess-3 Gray code (1956) (aka Gray excess-3 code, Gray 3-excess code, reflex excess-3 code, excess Gray code, Gray excess code, 10-excess-3 Gray code or Gray–Stibitz code), described by Frank P. Turvey Jr. of ITT.
- Tompkins codes I and II (1956)
- Glixon code (1957), sometimes ambiguously also called modified Gray code

4-bit unit-distance BCD codes

Name

Bit

0

1

2

3

4

5

6

7

8

9

Weights

Tracks

Compl.

Cyclic

5s

Comment

Gray BCD

4

0

0

0

0

0

0

0

0

1

1

0–3

4 (3

)

No

(2, 4, 8, 16)

No

3

0

0

0

0

1

1

1

1

1

1

2

0

0

1

1

1

1

0

0

0

0

1

0

1

1

0

0

1

1

0

0

1

Paul

4

1

0

0

0

0

0

0

0

1

1

1–3

4 (3

)

No

2, 10

No

3

0

0

0

0

1

1

1

1

1

1

2

0

0

1

1

1

1

0

0

0

0

1

1

1

1

0

0

1

1

0

0

1

Glixon

4

0

0

0

0

0

0

0

0

1

1

0–3

4

No

2, 4, 8, 10

(shifted +1)

3

0

0

0

0

1

1

1

1

1

0

2

0

0

1

1

1

1

0

0

0

0

1

0

1

1

0

0

1

1

0

0

0

Tompkins I

4

0

0

0

0

0

1

1

1

1

1

0–4

2

No

2, 4, 10

Yes

3

0

0

0

0

1

1

1

1

1

0

2

0

0

1

1

1

1

1

0

0

0

1

0

1

1

0

0

0

1

1

0

0

O'Brien I

(Watts)

4

0

0

0

0

0

1

1

1

1

1

0–3

4

9

2, 4, 10

Yes

3

0

0

0

0

1

1

0

0

0

0

2

0

0

1

1

1

1

1

1

0

0

1

0

1

1

0

0

0

0

1

1

0

Petherick

(RAE)

4

0

0

0

0

0

1

1

1

1

1

1–3

3

9

2, 10

Yes

3

1

0

0

0

1

1

0

0

0

1

2

0

0

1

1

1

1

1

1

0

0

1

1

1

1

0

0

0

0

1

1

1

O'Brien II

4

0

0

0

0

0

1

1

1

1

1

1–3

3

9

2, 10

Yes

3

0

0

0

1

1

1

1

0

0

0

2

0

1

1

1

0

0

1

1

1

0

1

1

1

0

0

0

0

0

0

1

1

Susskind

4

0

0

0

0

0

1

1

1

1

1

1–4

3

9

2, 10

Yes

3

0

0

1

1

1

1

1

1

0

0

2

0

1

1

1

0

0

1

1

1

0

1

1

1

1

0

0

0

0

1

1

1

Klar

4

0

0

0

0

0

1

1

1

1

1

0–4

4 (3

)

9

2, 10

Yes

3

0

0

0

1

1

1

1

0

0

0

2

0

0

1

1

1

1

1

1

0

0

1

0

1

1

1

0

0

1

1

1

0

Tompkins II

4

0

0

0

0

0

1

1

1

1

1

1–3

2

9

2, 10

Yes

3

0

0

1

1

1

1

1

0

0

0

2

1

1

1

0

0

0

0

0

1

1

1

0

1

1

1

0

0

1

1

1

0

Excess-3 Gray

4

0

0

0

0

0

1

1

1

1

1

1–4

4

9

2, 10

Yes

3

0

1

1

1

1

1

1

1

1

0

2

1

1

1

0

0

0

0

1

1

1

1

0

0

1

1

0

0

1

1

0

0
