---
title: "JPEG (part 2/2)"
source: https://en.wikipedia.org/wiki/JPEG
domain: jpeg-xl
license: CC-BY-SA-4.0
tags: jpeg xl image, jxl codec, jpeg xl lossless, next-generation image codec
fetched: 2026-07-02
part: 2/2
---

## JPEG codec example

Although a JPEG file can be encoded in various ways, most commonly it is done with JFIF encoding. The encoding process consists of several steps:

1. The representation of the colors in the image is converted from RGB to Y′CBCR, consisting of one luma component (Y'), representing brightness, and two chroma components, (CB and CR), representing color. This step is sometimes skipped.
2. The resolution of the chroma data is reduced, usually by a factor of 2 or 3. This reflects the fact that the eye is less sensitive to fine color details than to fine brightness details.
3. The image is split into blocks of 8×8 pixels, and for each block, each of the Y, CB, and CR data undergoes the discrete cosine transform (DCT). A DCT is similar to a Fourier transform in the sense that it produces a kind of spatial frequency spectrum.
4. The amplitudes of the frequency components are quantized. Human vision is much more sensitive to small variations in color or brightness over large areas than to the strength of high-frequency brightness variations. Therefore, the magnitudes of the high-frequency components are stored with a lower accuracy than the low-frequency components. The quality setting of the encoder (for example 50 or 95 on a scale of 0–100 in the Independent JPEG Group's library) affects to what extent the resolution of each frequency component is reduced. If an excessively low quality setting is used, the high-frequency components are discarded altogether.
5. The resulting data for all 8×8 blocks is further compressed with a lossless algorithm, a variant of Huffman encoding.

The decoding process reverses these steps, except the *quantization* because it is irreversible. In the remainder of this section, the encoding and decoding processes are described in more detail.

### Encoding

Many of the options in the JPEG standard are not commonly used, and as mentioned above, most image software uses the simpler JFIF format when creating a JPEG file, which among other things specifies the encoding method. Here is a brief description of one of the more common methods of encoding when applied to an input that has 24 bits per pixel (eight each of red, green, and blue). This particular option is a lossy data compression method. They are represented in matrices below.

#### Color space transformation

First, the image should be converted from RGB (by default sRGB, but other color spaces are possible) into a different color space called Y′CBCR (or, informally, YCbCr). It has three components Y', CB and CR: the Y' component represents the brightness of a pixel, and the CB and CR components represent the chrominance (split into blue and red components). This is basically the same color space as used by digital color television as well as digital video including video DVDs. The Y′CBCR color space conversion allows greater compression without a significant effect on perceptual image quality (or greater perceptual image quality for the same compression). The compression is more efficient because the brightness information, which is more important to the eventual perceptual quality of the image, is confined to a single channel. This more closely corresponds to the perception of color in the human visual system. The color transformation also improves compression by statistical decorrelation.

A particular conversion to Y′CBCR is specified in the JFIF standard, and should be performed for the resulting JPEG file to have maximum compatibility. However, some JPEG implementations in "highest quality" mode do not apply this step and instead keep the color information in the RGB color model, where the image is stored in separate channels for red, green and blue brightness components. This results in less efficient compression, and would not likely be used when file size is especially important.

#### Downsampling

Due to the densities of color- and brightness-sensitive receptors in the human eye, humans can see considerably more fine detail in the brightness of an image (the Y' component) than in the hue and color saturation of an image (the Cb and Cr components). Using this knowledge, encoders can be designed to compress images more efficiently.

The transformation into the Y′CBCR color model enables the next usual step, which is to reduce the spatial resolution of the Cb and Cr components (called "downsampling" or "chroma subsampling"). The ratios at which the downsampling is ordinarily done for JPEG images are 4:4:4 (no downsampling), 4:2:2 (reduction by a factor of 2 in the horizontal direction), or (most commonly) 4:2:0 (reduction by a factor of 2 in both the horizontal and vertical directions). For the rest of the compression process, Y', Cb and Cr are processed separately and in a very similar manner.

#### Block splitting

After subsampling, each channel must be split into 8×8 blocks. Depending on chroma subsampling, this yields Minimum Coded Unit (MCU) blocks of size 8×8 (4:4:4 – no subsampling), 16×8 (4:2:2), or most commonly 16×16 (4:2:0). In video compression MCUs are called macroblocks.

If the data for a channel does not represent an integer number of blocks then the encoder must fill the remaining area of the incomplete blocks with some form of dummy data. Filling the edges with a fixed color (for example, black) can create ringing artifacts along the visible part of the border; repeating the edge pixels is a common technique that reduces (but does not necessarily eliminate) such artifacts, and more sophisticated border filling techniques can also be applied.

#### Discrete cosine transform

Next, each 8×8 block of each component (Y, Cb, Cr) is converted to a frequency-domain representation, using a normalized, two-dimensional type-II discrete cosine transform (DCT), see Citation 1 in discrete cosine transform. The DCT is sometimes referred to as "type-II DCT" in the context of a family of transforms as in discrete cosine transform, and the corresponding inverse (IDCT) is denoted as "type-III DCT".

As an example, one such 8×8 8-bit subimage might be:

$\left[{\begin{array}{rrrrrrrr}52&55&61&66&70&61&64&73\\63&59&55&90&109&85&69&72\\62&59&68&113&144&104&66&73\\63&58&71&122&154&106&70&69\\67&61&68&104&126&88&68&70\\79&65&60&70&77&68&58&75\\85&71&64&59&55&61&65&83\\87&79&69&68&65&76&78&94\end{array}}\right].$

Before computing the DCT of the 8×8 block, its values are shifted from a positive range to one centered on zero. For an 8-bit image, each entry in the original block falls in the range $[0,255]$ . The midpoint of the range (in this case, the value 128) is subtracted from each entry to produce a data range that is centered on zero, so that the modified range is $[-128,127]$ . This step reduces the dynamic range requirements in the DCT processing stage that follows.

This step results in the following values:

$g={\begin{array}{c}x\\\longrightarrow \\\left[{\begin{array}{rrrrrrrr}-76&-73&-67&-62&-58&-67&-64&-55\\-65&-69&-73&-38&-19&-43&-59&-56\\-66&-69&-60&-15&16&-24&-62&-55\\-65&-70&-57&-6&26&-22&-58&-59\\-61&-67&-60&-24&-2&-40&-60&-58\\-49&-63&-68&-58&-51&-60&-70&-53\\-43&-57&-64&-69&-73&-67&-63&-45\\-41&-49&-59&-60&-63&-52&-50&-34\end{array}}\right]\end{array}}{\Bigg \downarrow }y.$

The next step is to take the two-dimensional DCT, which is given by:

$\ G_{u,v}={\frac {1}{4}}\alpha (u)\alpha (v)\sum _{x=0}^{7}\sum _{y=0}^{7}g_{x,y}\cos \left[{\frac {(2x+1)u\pi }{16}}\right]\cos \left[{\frac {(2y+1)v\pi }{16}}\right]$

where

- $\ u$ is the horizontal spatial frequency, for the integers $\ 0\leq u<8$ .
- $\ v$ is the vertical spatial frequency, for the integers $\ 0\leq v<8$ .
- $\alpha (u)$ and $\alpha (v)$ are normalizing scale factors to make the transformation orthonormal with $\alpha (i)={\begin{cases}{\frac {1}{\sqrt {2}}},&{\mbox{if }}i=0\\1,&{\mbox{otherwise}}\end{cases}}$
- $\ g_{x,y}$ is the pixel value at coordinates $\ (x,y)$
- $\ G_{u,v}$ is the DCT coefficient at coordinates $\ (u,v).$

If we perform this transformation on our matrix above, we get the following (rounded to the nearest two digits beyond the decimal point):

$G={\begin{array}{c}u\\\longrightarrow \\\left[{\begin{array}{rrrrrrrr}-415.38&-30.19&-61.20&27.24&56.12&-20.10&-2.39&0.46\\4.47&-21.86&-60.76&10.25&13.15&-7.09&-8.54&4.88\\-46.83&7.37&77.13&-24.56&-28.91&9.93&5.42&-5.65\\-48.53&12.07&34.10&-14.76&-10.24&6.30&1.83&1.95\\12.12&-6.55&-13.20&-3.95&-1.87&1.75&-2.79&3.14\\-7.73&2.91&2.38&-5.94&-2.38&0.94&4.30&1.85\\-1.03&0.18&0.42&-2.42&-0.88&-3.02&4.12&-0.66\\-0.17&0.14&-1.07&-4.19&-1.17&-0.10&0.50&1.68\end{array}}\right]\end{array}}{\Bigg \downarrow }v.$

Note the top-left corner entry with the rather large magnitude. This is the DC coefficient (also called the constant component), which defines the basic hue for the entire block. The remaining 63 coefficients are the AC coefficients (also called the alternating components). The advantage of the DCT is its tendency to aggregate most of the signal in one corner of the result, as may be seen above. The quantization step to follow accentuates this effect while simultaneously reducing the overall size of the DCT coefficients, resulting in a signal that is easy to compress efficiently in the entropy stage.

The DCT temporarily increases the bit-depth of the data, since the DCT coefficients of an 8-bit/component image take up to 11 or more bits (depending on fidelity of the DCT calculation) to store. This may force the codec to temporarily use 16-bit numbers to hold these coefficients, doubling the size of the image representation at this point; these values are typically reduced back to 8-bit values by the quantization step. The temporary increase in size at this stage is not a performance concern for most JPEG implementations, since typically only a very small part of the image is stored in full DCT form at any given time during the image encoding or decoding process.

#### Quantization

The human eye is good at seeing small differences in brightness over a relatively large area, but not so good at distinguishing the exact strength of a high frequency brightness variation. This allows one to greatly reduce the amount of information in the high frequency components. This is done by simply dividing each component in the frequency domain by a constant for that component, and then rounding to the nearest integer. This rounding operation is the only lossy operation in the whole process (other than chroma subsampling) if the DCT computation is performed with sufficiently high precision. As a result of this, it is typically the case that many of the higher frequency components are rounded to zero, and many of the rest become small positive or negative numbers, which take many fewer bits to represent.

The elements in the quantization matrix control the compression ratio, with larger values producing greater compression. A typical quantization matrix (for a quality of 50% as specified in the original JPEG Standard), is as follows:

$Q={\begin{bmatrix}16&11&10&16&24&40&51&61\\12&12&14&19&26&58&60&55\\14&13&16&24&40&57&69&56\\14&17&22&29&51&87&80&62\\18&22&37&56&68&109&103&77\\24&35&55&64&81&104&113&92\\49&64&78&87&103&121&120&101\\72&92&95&98&112&100&103&99\end{bmatrix}}.$

The quantized DCT coefficients are computed with

$B_{j,k}=\mathrm {round} \left({\frac {G_{j,k}}{Q_{j,k}}}\right){\mbox{ for }}j=0,1,2,\ldots ,7;k=0,1,2,\ldots ,7$

where G is the unquantized DCT coefficients; Q is the quantization matrix above; and B is the quantized DCT coefficients.

Using this quantization matrix with the DCT coefficient matrix from above results in:

$B=\left[{\begin{array}{rrrrrrrr}-26&-3&-6&2&2&-1&0&0\\0&-2&-4&1&1&0&0&0\\-3&1&5&-1&-1&0&0&0\\-3&1&2&-1&0&0&0&0\\1&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\end{array}}\right].$

For example, using −415 (the DC coefficient) and rounding to the nearest integer

$\mathrm {round} \left({\frac {-415.37}{16}}\right)=\mathrm {round} \left(-25.96\right)=-26.$

Notice that most of the higher-frequency elements of the sub-block (i.e., those with an *x* or *y* spatial frequency greater than 4) are quantized into zero values.

#### Entropy coding

Entropy coding is a special form of lossless data compression. It involves arranging the image components in a "zigzag" order employing run-length encoding (RLE) algorithm that groups similar frequencies together, inserting length coding zeros, and then using Huffman coding on what is left.

The JPEG standard also allows, but does not require, decoders to support the use of arithmetic coding, which is mathematically superior to Huffman coding. However, this feature has rarely been used, as it was historically covered by patents requiring royalty-bearing licenses, and because it is slower to encode and decode compared to Huffman coding. Arithmetic coding typically makes files about 5–7% smaller.

The previous quantized DC coefficient is used to predict the current quantized DC coefficient. The difference between the two is encoded rather than the actual value. The encoding of the 63 quantized AC coefficients does not use such prediction differencing.

The zigzag sequence for the above quantized coefficients are shown below. (The format shown is just for ease of understanding/viewing.)

| −26 |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| −3 | 0 |   |   |   |   |   |   |
| −3 | −2 | −6 |   |   |   |   |   |
| 2 | −4 | 1 | −3 |   |   |   |   |
| 1 | 1 | 5 | 1 | 2 |   |   |   |
| −1 | 1 | −1 | 2 | 0 | 0 |   |   |
| 0 | 0 | 0 | −1 | −1 | 0 | 0 |   |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |   |
| 0 | 0 | 0 | 0 | 0 | 0 |   |   |
| 0 | 0 | 0 | 0 | 0 |   |   |   |
| 0 | 0 | 0 | 0 |   |   |   |   |
| 0 | 0 | 0 |   |   |   |   |   |
| 0 | 0 |   |   |   |   |   |   |
| 0 |   |   |   |   |   |   |   |

If the *i*-th block is represented by $B_{i}$ and positions within each block are represented by $(p,q)$ where $p=0,1,...,7$ and $q=0,1,...,7$ , then any coefficient in the DCT image can be represented as $B_{i}(p,q)$ . Thus, in the above scheme, the order of encoding pixels (for the i-th block) is $B_{i}(0,0)$ , $B_{i}(0,1)$ , $B_{i}(1,0)$ , $B_{i}(2,0)$ , $B_{i}(1,1)$ , $B_{i}(0,2)$ , $B_{i}(0,3)$ , $B_{i}(1,2)$ and so on.

This encoding mode is called baseline *sequential* encoding. Baseline JPEG also supports *progressive* encoding. While sequential encoding encodes coefficients of a single block at a time (in a zigzag manner), progressive encoding encodes similar-positioned batch of coefficients of all blocks in one go (called a *scan*), followed by the next batch of coefficients of all blocks, and so on. For example, if the image is divided into N 8×8 blocks $B_{0},B_{1},B_{2},...,B_{n-1}$ , then a 3-scan progressive encoding encodes DC component, $B_{i}(0,0)$ for all blocks, i.e., for all $i=0,1,2,...,N-1$ , in first scan. This is followed by the second scan which encoding a few more components (assuming four more components, they are $B_{i}(0,1)$ to $B_{i}(1,1)$ , still in a zigzag manner) coefficients of all blocks (so the sequence is: $B_{0}(0,1),B_{0}(1,0),B_{0}(2,0),B_{0}(1,1),B_{1}(0,1),B_{1}(1,0),...,B_{N}(2,0),B_{N}(1,1)$ ), followed by all the remained coefficients of all blocks in the last scan.

Once all similar-positioned coefficients have been encoded, the next position to be encoded is the one occurring next in the zigzag traversal as indicated in the figure above. It has been found that *baseline progressive* JPEG encoding usually gives better compression as compared to *baseline sequential* JPEG due to the ability to use different Huffman tables (see below) tailored for different frequencies on each "scan" or "pass" (which includes similar-positioned coefficients), though the difference is not too large.

In the rest of the article, it is assumed that the coefficient pattern generated is due to sequential mode.

In order to encode the above generated coefficient pattern, JPEG uses Huffman encoding. The JPEG standard provides general-purpose Huffman tables; encoders may also choose to generate Huffman tables optimized for the actual frequency distributions in images being encoded.

The process of encoding the zig-zag quantized data begins with a run-length encoding explained below, where:

- x is the non-zero, quantized AC coefficient.
- *RUNLENGTH* is the number of zeroes that came before this non-zero AC coefficient.
- *SIZE* is the number of bits required to represent x.
- *AMPLITUDE* is the bit-representation of x.

The run-length encoding works by examining each non-zero AC coefficient x and determining how many zeroes came before the previous AC coefficient. With this information, two symbols are created:

| Symbol 1 | Symbol 2 |
|---|---|
| (RUNLENGTH, SIZE) | (AMPLITUDE) |

Both *RUNLENGTH* and *SIZE* rest on the same byte, meaning that each only contains four bits of information. The higher bits deal with the number of zeroes, while the lower bits denote the number of bits necessary to encode the value of x.

This has the immediate implication of *Symbol 1* being only able store information regarding the first 15 zeroes preceding the non-zero AC coefficient. However, JPEG defines two special Huffman code words. One is for ending the sequence prematurely when the remaining coefficients are zero (called "End-of-Block" or "EOB"), and another when the run of zeroes goes beyond 15 before reaching a non-zero AC coefficient. In such a case where 16 zeroes are encountered before a given non-zero AC coefficient, *Symbol 1* is encoded "specially" as: (15, 0)(0).

The overall process continues until "EOB" – denoted by (0, 0) – is reached.

With this in mind, the sequence from earlier becomes:

(0, 2)(-3);(1, 2)(-3);(0, 2)(-2);(0, 3)(-6);(0, 2)(2);(0, 3)(-4);(0, 1)(1);(0, 2)(-3);(0, 1)(1);(0, 1)(1);

(0, 3)(5);(0, 1)(1);(0, 2)(2);(0, 1)(-1);(0, 1)(1);(0, 1)(-1);(0, 2)(2);(5, 1)(-1);(0, 1)(-1);(0, 0);

(The first value in the matrix, −26, is the DC coefficient; it is not encoded the same way. See above.)

From here, frequency calculations are made based on occurrences of the coefficients. In our example block, most of the quantized coefficients are small numbers that are not preceded immediately by a zero coefficient. These more-frequent cases will be represented by shorter code words.

### Compression ratio and artifacts

The resulting compression ratio can be varied according to need by being more or less aggressive in the divisors used in the quantization phase. Ten to one compression usually results in an image that cannot be distinguished by eye from the original. A compression ratio of 100:1 is usually possible, but will look distinctly artifacted compared to the original. The appropriate level of compression depends on the use to which the image will be put.

Those who use the World Wide Web may be familiar with the irregularities known as compression artifacts that appear in JPEG images, which may take the form of noise around contrasting edges (especially curves and corners), or "blocky" images. These are due to the quantization step of the JPEG algorithm. They are especially noticeable around sharp corners between contrasting colors (text is a good example, as it contains many such corners). The analogous artifacts in MPEG video are referred to as *mosquito noise,* as the resulting "edge busyness" and spurious dots, which change over time, resemble mosquitoes swarming around the object.

These artifacts can be reduced by choosing a lower level of compression; they may be completely avoided by saving an image using a lossless file format, though this will result in a larger file size. The images created with ray-tracing programs have noticeable blocky shapes on the terrain. Certain low-intensity compression artifacts might be acceptable when simply viewing the images, but can be emphasized if the image is subsequently processed, usually resulting in unacceptable quality. Consider the example below, demonstrating the effect of lossy compression on an edge detection processing step.

| Image | Lossless compression | Lossy compression |
|---|---|---|
| Original |   |   |
| Processed by Canny edge detector |   |   |

Some programs allow the user to vary the amount by which individual blocks are compressed. Stronger compression is applied to areas of the image that show fewer artifacts. This way it is possible to manually reduce JPEG file size with less loss of quality.

Since the quantization stage *always* results in a loss of information, JPEG standard is always a lossy compression codec. (Information is lost both in quantizing and rounding of the floating-point numbers.) Even if the quantization matrix is a matrix of ones, information will still be lost in the rounding step.

### Decoding

Decoding to display the image consists of doing all the above in reverse.

Taking the DCT coefficient matrix (after adding the difference of the DC coefficient back in)

$\left[{\begin{array}{rrrrrrrr}-26&-3&-6&2&2&-1&0&0\\0&-2&-4&1&1&0&0&0\\-3&1&5&-1&-1&0&0&0\\-3&1&2&-1&0&0&0&0\\1&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\end{array}}\right]$

and taking the entry-for-entry product with the quantization matrix from above results in

$\left[{\begin{array}{rrrrrrrr}-416&-33&-60&32&48&-40&0&0\\0&-24&-56&19&26&0&0&0\\-42&13&80&-24&-40&0&0&0\\-42&17&44&-29&0&0&0&0\\18&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\end{array}}\right]$

which closely resembles the original DCT coefficient matrix for the top-left portion.

The next step is to take the two-dimensional inverse DCT (a 2D type-III DCT), which is given by:

$f_{x,y}={\frac {1}{4}}\sum _{u=0}^{7}\sum _{v=0}^{7}\alpha (u)\alpha (v)F_{u,v}\cos \left[{\frac {(2x+1)u\pi }{16}}\right]\cos \left[{\frac {(2y+1)v\pi }{16}}\right]$

where

- $\ x$ is the pixel row, for the integers $\ 0\leq x<8$ .
- $\ y$ is the pixel column, for the integers $\ 0\leq y<8$ .
- $\ \alpha (u)$ is the normalizing scale factor defined earlier, for the integers $\ 0\leq u<8$ .
- $\ F_{u,v}$ is the approximated DCT coefficient at coordinates $\ (u,v).$
- $\ f_{x,y}$ is the reconstructed pixel value at coordinates $\ (x,y)$

Rounding the output to integer values (since the original had integer values) results in an image with values (still shifted down by 128)

Slight differences are noticeable between the original (top) and decompressed image (bottom), which is most readily seen in the bottom-left corner.

$\left[{\begin{array}{rrrrrrrr}-66&-63&-71&-68&-56&-65&-68&-46\\-71&-73&-72&-46&-20&-41&-66&-57\\-70&-78&-68&-17&20&-14&-61&-63\\-63&-73&-62&-8&27&-14&-60&-58\\-58&-65&-61&-27&-6&-40&-68&-50\\-57&-57&-64&-58&-48&-66&-72&-47\\-53&-46&-61&-74&-65&-63&-62&-45\\-47&-34&-53&-74&-60&-47&-47&-41\end{array}}\right]$

and adding 128 to each entry

$\left[{\begin{array}{rrrrrrrr}62&65&57&60&72&63&60&82\\57&55&56&82&108&87&62&71\\58&50&60&111&148&114&67&65\\65&55&66&120&155&114&68&70\\70&63&67&101&122&88&60&78\\71&71&64&70&80&62&56&81\\75&82&67&54&63&65&66&83\\81&94&75&54&68&81&81&87\end{array}}\right].$

This is the decompressed subimage. In general, the decompression process may produce values outside the original input range of $[0,255]$ . If this occurs, the decoder needs to clip the output values so as to keep them within that range to prevent overflow when storing the decompressed image with the original bit depth.

The decompressed subimage can be compared to the original subimage (also see images to the right) by taking the difference (original − uncompressed) results in the following error values:

$\left[{\begin{array}{rrrrrrrr}-10&-10&4&6&-2&-2&4&-9\\6&4&-1&8&1&-2&7&1\\4&9&8&2&-4&-10&-1&8\\-2&3&5&2&-1&-8&2&-1\\-3&-2&1&3&4&0&8&-8\\8&-6&-4&-0&-3&6&2&-6\\10&-11&-3&5&-8&-4&-1&-0\\6&-15&-6&14&-3&-5&-3&7\end{array}}\right]$

with an average absolute error of about 5 values per pixels (i.e., ${\frac {1}{64}}\sum _{x=0}^{7}\sum _{y=0}^{7}|e(x,y)|=4.8750$ ).

The error is most noticeable in the bottom-left corner where the bottom-left pixel becomes darker than the pixel to its immediate right.

### Required precision

The required implementation precision of a JPEG codec is implicitly defined through the requirements formulated for compliance to the JPEG standard. These requirements are specified in ITU.T Recommendation T.83 | ISO/IEC 10918-2. Unlike MPEG standards and many later JPEG standards, the above document defines both required implementation precisions for the encoding and the decoding process of a JPEG codec by means of a maximal tolerable error of the forwards and inverse DCT in the DCT domain as determined by reference test streams. For example, the output of a decoder implementation must not exceed an error of one quantization unit in the DCT domain when applied to the reference testing codestreams provided as part of the above standard. While unusual, and unlike many other and more modern standards, ITU.T T.83 | ISO/IEC 10918-2 does not formulate error bounds in the image domain.


## Effects of JPEG compression

JPEG compression artifacts blend well into photographs with detailed non-uniform textures, allowing higher compression ratios. Notice how a higher compression ratio first affects the high-frequency textures in the upper-left corner of the image, and how the contrasting lines become more fuzzy. The very high compression ratio severely affects the quality of the image, although the overall colors and image form are still recognizable. However, the precision of colors suffer less (for a human eye) than the precision of contours (based on luminance). This justifies the fact that images should be first transformed in a color model separating the luminance from the chromatic information, before subsampling the chromatic planes (which may also use lower quality quantization) in order to preserve the precision of the luminance plane with more information bits.

### Sample photographs

For information, the uncompressed 24-bit RGB bitmap image below (73,242 pixels) would require 219,726 bytes (excluding all other information headers). The filesizes indicated below include the internal JPEG information headers and some metadata. For highest quality images (Q=100), about 8.25 bits per color pixel is required. On grayscale images, a minimum of 6.5 bits per pixel is enough (a comparable Q=100 quality color information requires about 25% more encoded bits). The highest quality image below (Q=100) is encoded at nine bits per color pixel, the medium quality image (Q=25) uses one bit per color pixel. For most applications, the quality factor should not go below 0.75 bit per pixel (Q=12.5), as demonstrated by the low quality image. The image at lowest quality uses only 0.13 bit per pixel, and displays very poor color. This is useful when the image will be displayed in a significantly scaled-down size. A method for creating better quantization matrices for a given image quality using PSNR instead of the Q factor is described in Minguillón & Pujol (2001).

| Image | Quality | Size (bytes) | Compression ratio | Comment |
|---|---|---|---|---|
|   | Highest quality (Q = 100) | 81,447 | 2.7:1 | Extremely minor artifacts |
|   | High quality (Q = 50) | 14,679 | 15:1 | Initial signs of subimage artifacts |
|   | Medium quality (Q = 25) | 9,407 | 23:1 | Stronger artifacts; loss of high frequency information |
|   | Low quality (Q = 10) | 4,787 | 46:1 | Severe high frequency loss leads to obvious artifacts on subimage boundaries ("macroblocking") |
|   | Lowest quality (Q = 1) | 1,523 | 144:1 | Extreme loss of color and detail; the leaves are nearly unrecognizable. |

The medium quality photo uses only 4.3% of the storage space required for the uncompressed image, but has little noticeable loss of detail or visible artifacts. However, once a certain threshold of compression is passed, compressed images show increasingly visible defects. See the article on rate–distortion theory for a mathematical explanation of this threshold effect. A particular limitation of JPEG in this regard is its non-overlapped 8×8 block transform structure. More modern designs such as JPEG 2000 and JPEG XR exhibit a more graceful degradation of quality as the bit usage decreases – by using transforms with a larger spatial extent for the lower frequency coefficients and by using overlapping transform basis functions.


## Lossless further compression

From 2004 to 2008, new research emerged on ways to further compress the data contained in JPEG images without modifying the represented image. This has applications in scenarios where the original image is only available in JPEG format, and its size needs to be reduced for archiving or transmission. Standard general-purpose compression tools cannot significantly compress JPEG files.

Typically, such schemes take advantage of improvements to the naive scheme for coding DCT coefficients, which fails to take into account:

- Correlations between magnitudes of adjacent coefficients in the same block;
- Correlations between magnitudes of the same coefficient in adjacent blocks;
- Correlations between magnitudes of the same coefficient/block in different channels;
- The DC coefficients when taken together resemble a downscale version of the original image multiplied by a scaling factor. Well-known schemes for lossless coding of continuous-tone images can be applied, achieving somewhat better compression than the Huffman coded DPCM used in JPEG.

Some standard but rarely used options already exist in JPEG to improve the efficiency of coding DCT coefficients: the arithmetic coding option, and the progressive coding option (which produces lower bitrates because values for each coefficient are coded independently, and each coefficient has a significantly different distribution). Modern methods have improved on these techniques by reordering coefficients to group coefficients of larger magnitude together; using adjacent coefficients and blocks to predict new coefficient values; dividing blocks or coefficients up among a small number of independently coded models based on their statistics and adjacent values; and most recently, by decoding blocks, predicting subsequent blocks in the spatial domain, and then encoding these to generate predictions for DCT coefficients.

Typically, such methods can compress existing JPEG files between 15 and 25 percent, and for JPEGs compressed at low-quality settings, can produce improvements of up to 65%.

Several programs are available for lossless recompression of JPEG files. The files produced by such programs are not compatible with the JPEG standard and require special software to decode.

- StuffIt Deluxe 9, a proprietary archiver for Mac and Windows, released in 2005, can transcode JPEG files into the StuffIt Image Format, with a claimed file size reduction of up to 28%.
- PackJPG is a freely available tool based on the 2007 paper "Improved Redundancy Reduction for JPEG Files." As of version 2.5k of 2016, it reports a typical 20% reduction by transcoding.
- Lepton, developed by Dropbox and used in their file-storage service since 2016, replaces Huffman coding with arithmetic coding and a custom statistical model, for a 22% file size reduction. It can reconstruct a bitwise copy of the original JPEG file. The original implementation, written in C++ and distributed under the Apache License, is no longer actively maintained. Dropbox suggests users switch to a Rust reimplementation from Microsoft.
- Brunsli was developed by Google in 2017, and released as a standalone tool in 2019 under the MIT License. It claims a 22% file size reduction and can reconstruct a bitwise copy of the original JPEG file. Since then, Brunsli has been integrated into JPEG XL.
- JPEG XL is a general-purpose image format that can recompress most JPEG files and reconstruct a bitwise copy of the original JPEG file. The file size reductions are around 20% for high-quality images with 4:4:4 chroma subsampling produced by libjpeg and libjpeg-turbo. JPEG XL is an ISO/IEC standard, and several freely-licensed implementations are available.


## Derived formats for stereoscopic 3D

### JPEG Stereoscopic

JPS is a stereoscopic JPEG image used for creating 3D effects from 2D images. It contains two static images, one for the left eye and one for the right eye; encoded as two side-by-side images in a single JPEG file. JPEG Stereoscopic (JPS, extension .jps) is a JPEG-based format for stereoscopic images. It has a range of configurations stored in the JPEG APP3 marker field, but usually contains one image of double width, representing two images of identical size in cross-eyed (i.e. left frame on the right half of the image and vice versa) side-by-side arrangement. This file format can be viewed as a JPEG without any special software, or can be processed for rendering in other modes.

### JPEG Multi-Picture Format

JPEG Multi-Picture Format (MPO, extension .mpo) is a JPEG-based format for storing multiple images in a single file. It contains two or more JPEG files concatenated together. It also defines a JPEG APP2 marker segment for image description. Various devices use it to store 3D images, such as Fujifilm FinePix Real 3D W1, HTC Evo 3D, JVC GY-HMZ1U AVCHD/MVC extension camcorder, Nintendo 3DS, Panasonic Lumix DMC-TZ20, DMC-TZ30, DMC-TZ60, DMC-TS4 (FT4), and Sony DSC-HX7V. Other devices use it to store "preview images" that can be displayed on a TV.

In the last few years, due to the growing use of stereoscopic images, much effort has been spent by the scientific community to develop algorithms for stereoscopic image compression.


## Implementations

A very important implementation of a JPEG codec is the free programming library **libjpeg** of the Independent JPEG Group. It was first published in 1991 and was key for the success of the standard. This library was used in countless applications. The development went quiet in 1998; when libjpeg resurfaced with the 2009 version 7, it broke ABI compatibility with previous versions. Version 8 of 2010 introduced non-standard extensions, a decision criticized by the original IJG leader Tom Lane.

**libjpeg-turbo**, forked from the 1998 libjpeg 6b, improves on libjpeg with SIMD optimizations. Originally seen as a maintained fork of libjpeg, it has become more popular after the incompatible changes of 2009. In 2019, it became the ITU|ISO/IEC reference implementation as ISO/IEC 10918-7 and ITU-T T.873.

ISO/IEC Joint Photographic Experts Group maintains the other reference software implementation under the JPEG XT heading. It can encode both base JPEG (ISO/IEC 10918-1 and 18477–1) and JPEG XT extensions (ISO/IEC 18477 Parts 2 and 6–9), as well as JPEG-LS (ISO/IEC 14495). In 2016, "JPEG on steroids" was introduced as an option for the ISO JPEG XT reference implementation.

There is persistent interest in encoding JPEG in unconventional ways that maximize image quality for a given file size. In 2014, Mozilla created **MozJPEG** from libjpeg-turbo, a slower but higher-quality encoder intended for web images. In March 2017, Google released the open source project Guetzli, which trades off a much longer encoding time for smaller file size (similar to what Zopfli does for PNG and other lossless data formats).

In April 2024, Google introduced **Jpegli**, a new JPEG coding library that offers enhanced capabilities and a 35% compression ratio improvement at high quality compression settings, while the coding speed is comparable with MozJPEG.


## Successors

The Joint Photographic Experts Group has developed several newer standards meant to complement or replace the functionality of the original JPEG format.

### JPEG LS

Originating in 1993 and published as ISO-14495-1/ITU-T.87, JPEG LS offers a low-complexity lossless file format which was more efficient than JPEG's original lossless implementation. It also features a lossy mode close to lossless. Its functionality is largely limited to that, and largely shares the same limitations of the original JPEG in other aspects.

### JPEG 2000

JPEG 2000 was published as ISO/IEC 15444 in December 2000. It is based on a discrete wavelet transform (DWT) and was designed to completely replace the original JPEG standard and exceed it in every way. It allows up to 38 bits per colour channel and 16384 channels, more than any other format, with a multitude of colour spaces, and thus high dynamic range (HDR). Furthermore, it supports alpha transparency coding, billions-by-billions pixel images, which is also more than any other format, and lossless compression. It has significantly improved lossy compression ratio with significantly less visible artefacts at strong compression levels.

### JPEG XT

JPEG XT (ISO/IEC 18477) was published in June 2015; it extends base JPEG format with support for higher integer bit depths (up to 16 bit), high dynamic range imaging and floating-point coding, lossless coding, and alpha channel coding. Extensions are backward compatible with the base JPEG/JFIF file format and 8-bit lossy compressed image. JPEG XT uses an extensible file format based on JFIF. Extension layers are used to modify the JPEG 8-bit base layer and restore the high-resolution image. Existing software is forward compatible and can read the JPEG XT binary stream, though it would only decode the base 8-bit layer.

### JPEG XL

JPEG XL (ISO/IEC 18181) was published in 2021–2022. It replaces the JPEG format with a new DCT-based royalty-free format and allows efficient transcoding as a storage option for traditional JPEG images. The new format is designed to exceed the still image compression performance shown by HEIF HM, Daala and WebP. It supports billion-by-billion pixel images, up to 32-bit-per-component high dynamic range with the appropriate transfer functions (PQ and HLG), patch encoding of synthetic images such as bitmap fonts and gradients, animated images, alpha channel coding, and a choice of RGB/YCbCr/ICtCp color encoding.
