---
title: "GIF - Wikipedia (part 1/2)"
source: https://en.wikipedia.org/wiki/GIF
domain: gif-format
license: CC-BY-SA-4.0
tags: gif image, lzw compression, animated gif, indexed color
fetched: 2026-07-02
part: 1/2
---

# GIF

The **Graphics Interchange Format** (**GIF**; /ɡɪf/ *GHIF* or /dʒɪf/ *JIF*, ) is a bitmap image format that was developed by a team at the online services provider CompuServe led by American computer scientist Steve Wilhite and released on June 15, 1987.

The format can contain up to 8 bits per pixel, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space. It can also represent multiple images in a file, which can be used for animations, and allows a separate palette of up to 256 colors for each frame. These palette limitations make GIF less suitable for reproducing color photographs and other images with color gradients, but well-suited for simpler images such as graphics or logos with solid areas of color.

GIF images are compressed using the Lempel–Ziv–Welch (LZW) lossless data compression technique to reduce the file size without degrading the visual quality. While once in widespread usage on the World Wide Web because of its wide implementation and portability between applications and operating systems, usage of the format has declined for space and quality reasons, often being replaced with newer formats such as PNG for static images and MP4 for videos. In this context, short video clips are sometimes termed "GIFs" despite having no relation to the original file format.


## History

CompuServe introduced GIF on 15 June 1987 to provide a color image format for their file downloading areas. This replaced their earlier run-length encoding format, which was black and white only. GIF became popular because it used Lempel–Ziv–Welch data compression. Since this was more efficient than the run-length encoding used by PCX and MacPaint, fairly large images could be downloaded reasonably quickly even with slow modems.

The original version of GIF was called 87a. This version already supported multiple images in a stream.

In 1989, CompuServe released an enhanced version, called 89a, This version added:

- support for animation delays
- transparent background colors
- storage of application-specific metadata
- allowing text labels as text (not embedding them in the graphical data). However, this feature is rarely used. Modern browsers do not support it, and there is little control over fonts and styling.

The two versions can be distinguished by looking at the first six bytes of the file (the "magic number" or signature), which, when interpreted as ASCII, read "GIF87a" or "GIF89a", respectively.

CompuServe encouraged the adoption of GIF by providing downloadable conversion utilities for many computers. By December 1987, for example, an Apple IIGS user could view pictures created on an Atari ST or Commodore 64. GIF was one of the first two image formats commonly used on Web sites, the other being the black-and-white XBM.

In September 1995, Netscape Navigator 2.0 added the ability for animated GIFs to loop.

While GIF was developed by CompuServe, it used the Lempel–Ziv–Welch (LZW) lossless data compression algorithm patented by Unisys in 1985. Controversy over the licensing agreement between Unisys and CompuServe in 1994 spurred the development of the Portable Network Graphics (PNG) standard. In 2004, all patents relating to the proprietary compression used for GIF expired.

The feature of storing multiple images in one file, accompanied by control data, is used extensively on the Web to produce simple animations.

The optional interlacing feature, which stores image scan lines out of order in such a fashion that even a partially downloaded image was somewhat recognizable, also helped GIF's popularity, as a user could abort the download if it was not what was required.

In May 2015 Facebook added support for GIF. In 2014, Twitter, also added support to GIF as well as Instagram in 2018.

In 2016, the Internet Archive released a searchable library of GIFs from their GeoCities archive.


## Terminology

As a noun, the word *GIF* is found in the newer editions of many dictionaries. In 2012, the American wing of the Oxford University Press recognized *GIF* as a verb as well, meaning "to create a GIF file", as in "GIFing was the perfect medium for sharing scenes from the Summer Olympics". The press's lexicographers voted it their word of the year, saying that GIFs have evolved into "a tool with serious applications including research and journalism".

### Pronunciation

The pronunciation of the first letter of *GIF* has been disputed since the 1990s. The most common pronunciations in English are /dʒɪf/ ⓘ (with a soft *g* as in *gin*) and /ɡɪf/ ⓘ (with a hard *g* as in *gift*), differing in the phoneme represented by the letter *G*. The creators of the format pronounced the acronym *GIF* as /dʒɪf/, with a soft *g*, with Wilhite stating that he intended for the pronunciation to deliberately echo the American peanut butter brand Jif, and CompuServe employees would often quip "choosy developers choose GIF", a spoof of Jif's television commercials. However, the word is widely pronounced as /ɡɪf/, with a hard *g*, and polls have generally shown that this hard *g* pronunciation is more prevalent.

*Dictionary.com* cites both pronunciations, indicating /dʒɪf/ as the primary pronunciation, while *Cambridge Dictionary of American English* offers only the hard-*g* pronunciation. *Merriam-Webster's Collegiate Dictionary* and Oxford Dictionaries cite both pronunciations, but place the hard *g* first: /ɡɪf, dʒɪf/. The *New Oxford American Dictionary* gave only /dʒɪf/ in its second edition but updated it to /dʒɪf, ɡɪf/ in the third edition.

The disagreement over the pronunciation has led to a heated Internet debate. On the occasion of receiving a lifetime achievement award at the 2013 Webby Awards ceremony, Wilhite publicly rejected the hard-*g* pronunciation; his speech led to more than 17,000 posts on Twitter and dozens of news articles. The White House and the TV program *Jeopardy!* also entered the debate in 2013. In February 2020, The J.M. Smucker Company, the owners of the Jif brand, partnered with the animated image database and search engine Giphy to release a limited-edition "Jif vs. GIF" (hashtagged as #JIFvsGIF) jar of peanut butter that had a label humorously declaring the soft-*g* pronunciation to refer exclusively to the peanut butter, and *GIF* to be exclusively pronounced with the hard-*g* pronunciation.


## Usage

GIFs are suitable for sharp-edged line art with a limited number of colors, such as logos. This takes advantage of the format's lossless compression, which favors flat areas of uniform color with well-defined edges. They can also be used to store low-color sprite data for games. GIFs can be used for small animations and low-resolution video clips, or as reactions in online messaging used to convey emotion and feelings in moving pictures. They are popular on social media platforms such as Tumblr, Facebook, and X (formerly known as Twitter).


## File format

Conceptually, a GIF file describes a fixed-sized graphical area (the "logical screen") populated with zero or more "images". Many GIF files have a single image that fills the entire logical screen. Others divide the logical screen into separate sub-images. The images may also function as animation frames in an animated GIF file, but again, these need not fill the entire logical screen.

GIF files start with a fixed-length header ("GIF87a" or "GIF89a") giving the version, followed by a fixed-length Logical Screen Descriptor giving the pixel dimensions and other characteristics of the logical screen. The screen descriptor may also specify the presence and size of a Global Color Table (GCT), which follows next if present.

Thereafter, the file is divided into segments of the following types, each introduced by a 1-byte sentinel:

- An image (introduced by 0x2C, an ASCII comma `','`)
- An extension block (introduced by 0x21, an ASCII exclamation point `'!'`)
- The trailer (a single byte of value 0x3B, an ASCII semicolon `';'`), which should be the last byte of the file.

An image starts with a fixed-length Image Descriptor, which may specify the presence and size of a Local Color Table (which follows next if present). The image data follows: one byte giving the bit width of the unencoded symbols (which must be at least 2 bits wide, even for bi-color images), followed by a series of sub-blocks containing the LZW-encoded data.

Extension blocks (blocks that "extend" the 87a definition via a mechanism already defined in the 87a spec) consist of the sentinel, an additional byte specifying the type of extension, and a series of sub-blocks with the extension data. Extension blocks that modify an image (like the Graphic Control Extension that specifies the optional animation delay time and optional transparent background color) must immediately precede the segment with the image they refer to.

Each sub-block begins with a byte giving the number of subsequent data bytes in the sub-block (1 to 255). The series of sub-blocks is terminated by an empty sub-block (a 0-byte).

This structure allows the file to be parsed even if not all parts are understood. A GIF marked 87a may contain extension blocks; the intent is that a decoder can read and display the file without the features covered in extensions it does not understand.

The full details of the file format are covered in the GIF specification.


## Palettes

GIF is palette-based: the colors used in an image (a frame) in the file have their RGB values defined in a palette table that can hold up to 256 entries, and the data for the image refer to the colors by their indices (0–255) in the palette table. The color definitions in the palette can be drawn from a color space of millions of shades (224 shades, 8 bits for each primary), but the maximum number of colors a frame can use is 256. This limitation was reasonable when GIF was developed because hardware that could display more than 256 colors simultaneously was rare. Simple graphics, line drawings, cartoons, and grey-scale photographs typically need fewer than 256 colors.

Each frame can designate one index as a "transparent background color": any pixel assigned this index takes on the color of the pixel in the same position from the background, which may have been determined by a previous frame of animation.

Many techniques, collectively called dithering, have been developed to approximate a wider range of colors with a small color palette by using pixels of two or more colors to approximate in-between colors. These techniques sacrifice spatial resolution to approximate deeper color resolution. While not part of the GIF specification, dithering can be used in images subsequently encoded as GIF images. This is often not an ideal solution for GIF images, both because the loss of spatial resolution typically makes an image look fuzzy on the screen, and because the dithering patterns often interfere with the compressibility of the image data, working against GIF's main purpose.

In the early days of graphical web browsers (1981-1987, see Graphics Processing Unit), graphics cards with 8-bit buffers (allowing only 256 colors) were common and it was fairly common to make GIF images using the websafe palette. This ensured predictable display, but severely limited the choice of colors. When 24-bit color became the norm, palettes could instead be populated with the optimum colors for individual images.

A small color table may suffice for small images, and keeping the color table small allows the file to be downloaded faster. Both the 87a and 89a specifications allow color tables of 2*n* colors for any *n* from 1 through 8. Most graphics applications will read and display GIF images with any of these table sizes; but some do not support all sizes when *creating* images. Tables of 2, 16, and 256 colors are widely supported.

### True color

Although GIF is almost never used for true color images, it is possible to do so. A GIF image can include multiple image blocks, each of which can have its own 256-color palette, and the blocks can be tiled to create a complete image. Alternatively, the GIF89a specification introduced the idea of a "transparent" color where each image block can include its own palette of 255 visible colors plus one transparent color. A complete image can be created by layering image blocks, with the visible portion of each layer showing through the transparent portions of the layers above.

To render a full-color image as a GIF, the original image must be broken down into smaller regions having no more than 255 or 256 different colors. Each of these regions is then stored as a separate image block with its own local palette, and when the image blocks are displayed together (either by tiling or by layering partially transparent image blocks), the complete, full-color image appears. For example, breaking an image into tiles of 16 by 16 pixels (256 pixels in total) ensures that no tile has more than the local palette limit of 256 colors, although larger tiles may be used and similar colors merged, resulting in some loss of color information.

Since each image block can have its own local color table, a GIF file having many image blocks can be very large, limiting the usefulness of full-color GIFs. Additionally, not all GIF rendering programs handle tiled or layered images correctly. Many rendering programs interpret tiles or layers as animation frames and display them in sequence as an animation with most web browsers automatically displaying the frames with a delay time of 0.1 seconds or more.


## Example GIF file

| Microsoft Paint saves a small black-and-white image as the following GIF file (illustrated enlarged). Paint does not make optimal use of GIF; due to the unnecessarily large color table (storing a full 256 colors instead of the used 2) and symbol width, this GIF file is not an efficient representation of the 15-pixel image. Although the Graphic Control Extension block declares color index 16 (hexadecimal 10) to be transparent, that index is not used in the image. The only color indices appearing in the image data are decimal 40 and 255, which the Global Color Table maps to black and white, respectively. | Sample image (enlarged), actual size 3 pixels wide by 5 high |
|---|---|

The hex numbers in the following tables are in little-endian byte order, as the format specification prescribes.

| Byte # (hex) | Hexadecimal | Text or value | Meaning |   |
|---|---|---|---|---|
| 0 | 47 49 46 38 39 61 | GIF89a | Header |   |
| Logical Screen Descriptor |   |   |   |   |
| 6 | 03 00 | 3 | Logical screen width |   |
| 8 | 05 00 | 5 | Logical screen height |   |
| A | F7 |   | GCT follows for 256 colors with resolution 3 × 8 bits/primary, the lowest 3 bits represent the bit depth minus 1, the highest true bit means that the GCT is present |   |
| B | 00 | 0 | Background color: index #0; #000000 black |   |
| C | 00 | 0 | Default pixel aspect ratio, 0:0 |   |
| Global Color Table |   |   |   |   |
| D | 00 00 00 | R (red) G (green) B (blue) 0 0 0 | Global Color Table, color #0: #000000, black |   |
| 10 | 80 00 00 | R (red) G (green) B (blue) 128 0 0 | Global Color Table, color #1: transparent bit, not used in image |   |
| ... | ... | ... | Global Color Table extends to 30A |   |
| 30A | FF FF FF | R (red) G (green) B (blue) 255 255 255 | Global Color Table, color #255: #ffffff, white |   |
| Graphic Control Extension |   |   |   |   |
| 30D | 21 | `'!'` | An Extension Block (introduced by an ASCII exclamation point `'!'`) |   |
| 30E | F9 |   | A Graphic Control Extension |   |
| 30F | 04 | 4 | Amount of GCE data, 4 bytes |   |
| 310 | 01 |   | Transparent background color; this is a bit field, the lowest bit signifies transparency |   |
| 311 | 00 00 |   | Delay for animation in hundredths of a second; **not used** |   |
| 313 | 10 | 16 | Color number of transparent pixel in GCT |   |
| 314 | 00 |   | End of GCE block |   |
| Image Descriptor |   |   |   |   |
| 315 | 2C | `','` | An Image Descriptor (introduced by 0x2C, an ASCII comma `','`) |   |
| 316 | 00 00 00 00 | (0, 0) | North-west corner position of image in logical screen |   |
| 31A | 03 00 05 00 | (3, 5) | Image width and height in pixels |   |
| 31E | 00 | 0 | Local color table bit, 0 means none |   |
| Image Data |   |   |   |   |
| 31F | 08 | 8 | Start of image, LZW minimum code size |   |
| 320 | 0B | 11 | Beginning of first data sub-block, specifying 11 bytes of encoded data to follow |   |
| 321 | 00 51 FC 1B 28 70 A0 C1 83 01 01 | <image data> | 11 bytes of image data, see field 320 |   |
| 32C | 00 | 0 | Ending data sub-block, specifying no following data bytes (and the end of the image) |   |
| Trailer |   |   |   |   |
| 32D | 3B | `';'` | File termination block indicator (an ASCII semi-colon `';'`) |   |

### Image coding

The image pixel data, scanned horizontally from top left, are converted by LZW encoding to codes that are then mapped into bytes for storing in the file. The pixel codes typically don't match the 8-bit size of the bytes, so the codes are packed into bytes by a "little-Endian" scheme: the least significant bit of the first code is stored in the least significant bit of the first byte, higher order bits of the code into higher order bits of the byte, spilling over into the low order bits of the next byte as necessary. Each subsequent code is stored starting at the least significant bit not already used.

This byte stream is stored in the file as a series of "sub-blocks". Each sub-block has a maximum length of 255 bytes and is prefixed with a byte indicating the number of data bytes in the sub-block. The series of sub-blocks is terminated by an empty sub-block (a single 0 byte, indicating a sub-block with 0 data bytes).

For the sample image above, the reversible mapping between 9-bit codes and bytes is shown below.

| 9-bit code | Byte |   |   |
|---|---|---|---|
| Hexadecimal | Binary | Binary | Hexadecimal |
| 100 | 1 00000000 | 00000000 | 00 |
| 028 | 00 0101000 | 0101000 1 | 51 |
| 0FF | 011 111111 | 111111 00 | FC |
| 103 | 1000 00011 | 00011 011 | 1B |
| 102 | 10000 0010 | 0010 1000 | 28 |
| 103 | 100000 011 | 011 10000 | 70 |
| 106 | 1000001 10 | 10 100000 | A0 |
| 107 | 10000011 1 | 1 1000001 | C1 |
|   |   | 10000011 | 83 |
| 101 | 1 00000001 | 00000001 | 01 |
|   |   | 0000000 1 | 01 |

A slight compression is evident: pixel colors defined initially by 15 bytes are exactly represented by 12 code bytes, including control codes. The encoding process that produces the 9-bit codes is shown below. A local string accumulates pixel color numbers from the palette, with no output action, as long as the local string can be found in a code table. There is special treatment of the first two pixels that arrive before the table grows from its initial size by additions of strings. After each output code, the local string is initialized to the latest pixel color (that could not be included in the output code).

```
                          Table           9-bit
                     string --> code      code    Action
                          #0 | 000h               Initialize root table of 9-bit codes
                    palette  |  :
                     colors  |  :
                        #255 | 0FFh
                         clr | 100h
                         end | 101h
                             |            100h     Clear
Pixel          Local         |
color Palette string         |
BLACK  #40     28            |            028h     1st pixel always to output
WHITE  #255    FF            |                     String found in table
                  28 FF      | 102h                Always add 1st string to table
               FF            |                     Initialize local string
WHITE  #255    FF FF         |                     String not found in table
                             |            0FFh     - output code for previous string
                  FF FF      | 103h                - add latest string to table
               FF            |                     - initialize local string
WHITE  #255    FF FF         |                     String found in table
BLACK  #40     FF FF 28      |                     String not found in table
                             |            103h     - output code for previous string
                  FF FF 28   | 104h                - add latest string to table
               28            |                     - initialize local string
WHITE  #255    28 FF         |                     String found in table
WHITE  #255    28 FF FF      |                     String not found in table
                             |            102h     - output code for previous string
                  28 FF FF   | 105h                - add latest string to table
               FF            |                     - initialize local string
WHITE  #255    FF FF         |                     String found in table
WHITE  #255    FF FF FF      |                     String not found in table
                             |            103h     - output code for previous string
                  FF FF FF   | 106h                - add latest string to table
               FF            |                     - initialize local string
WHITE  #255    FF FF         |                     String found in table
WHITE  #255    FF FF FF      |                     String found in table
WHITE  #255    FF FF FF FF   |                     String not found in table
                             |            106h     - output code for previous string
                  FF FF FF FF| 107h                - add latest string to table
               FF            |                     - initialize local string
WHITE  #255    FF FF         |                     String found in table
WHITE  #255    FF FF FF      |                     String found in table
WHITE  #255    FF FF FF FF   |                     String found in table
                                                   No more pixels
                                          107h     - output code for last string
                                          101h     End
```

For clarity, the table is shown above as being built of strings of increasing length. That scheme can function, but the table consumes an unpredictable amount of memory. Memory can be saved in practice by noting that each new string to be stored consists of a previously stored string augmented by one character. It is economical to store at each address only two words: an existing address and one character.

The LZW algorithm requires a search of the table for each pixel. A linear search through up to 4096 addresses would make the coding slow. In practice, the codes can be stored in order of numerical value; this allows each search to be done by a SAR (Successive Approximation Register, as used in some ADCs), with only 12 magnitude comparisons. For this efficiency, an extra table is needed to convert between codes and actual memory addresses; the extra table upkeep is needed only when a new code is stored, which happens at a much lower rate than pixel rate.

### Image decoding

Decoding begins by mapping the stored bytes back to 9-bit codes. These are decoded to recover the pixel colors as shown below. A table identical to the one used in the encoder is built by adding strings according to this rule:

| Yes | add string for local code, followed by first byte of string for incoming code |
|---|---|
| No | add string for local code followed by a copy of its own first byte |

```
      shift
9-bit ----> Local      Table                 Pixel
code        code   code --> string   Palette color  Action
100h               000h  | #0                       Initialize root table of 9-bit codes
                    :    | palette
                    :    | colors
                   0FFh  | #255
                   100h  | clr
                   101h  | end
028h                     |             #40   BLACK  Decode 1st pixel
0FFh        028h         |                           Incoming code found in table
                         |             #255  WHITE   - output string from table
                   102h  | 28 FF                     - add to table
103h        0FFh         |                           Incoming code not found in table
                   103h  | FF FF                     - add to table
                         |                           - output string from table
                         |             #255  WHITE
                         |             #255  WHITE
102h        103h         |                           Incoming code found in table
                         |                           - output string from table
                         |             #40   BLACK
                         |             #255  WHITE
                   104h  | FF FF 28                  - add to table
103h        102h         |                           Incoming code found in table
                         |                           - output string from table
                         |             #255  WHITE
                         |             #255  WHITE
                   105h  | 28 FF FF                  - add to table
106h        103h         |                           Incoming code not found in table
                   106h  | FF FF FF                  - add to table
                         |                           - output string from table
                         |             #255  WHITE
                         |             #255  WHITE
                         |             #255  WHITE
107h        106h         |                           Incoming code not found in table
                   107h  | FF FF FF FF               - add to table
                         |                           - output string from table
                         |             #255  WHITE
                         |             #255  WHITE
                         |             #255  WHITE
                         |             #255  WHITE
101h                     |                           End
```

### LZW code lengths

Shorter code lengths can be used for palettes smaller than the 256 colors in the example. If the palette is only 64 colors (so color indexes are 6 bits wide), the symbols can range from 0 to 63, and the symbol width can be taken to be 6 bits, with codes starting at 7 bits. In fact, the symbol width need not match the palette size: as long as the values decoded are always less than the number of colors in the palette, the symbols can be any width from 2 to 8, and the palette size any power of 2 from 2 to 256. For example, if only the first four colors (values 0 to 3) of the palette are used, the symbols can be taken to be 2 bits wide with codes starting at 3 bits.

Conversely, the symbol width could be set at 8, even if only values 0 and 1 are used; these data would only require a two-color table. Although there would be no point in encoding the file that way, something similar typically happens for bi-color images: the minimum symbol width is 2, even if only values 0 and 1 are used.

The code table initially contains codes that are one bit longer than the symbol size in order to accommodate the two special codes *clr* and *end* and codes for strings that are added during the process. When the table is full, the code length increases to give space for more strings, up to a maximum code of 4095 = FFF(hex). As the decoder builds its table, it tracks these increases in code length, and it is able to unpack incoming bytes accordingly.

### Uncompressed GIF

| A 46×46 uncompressed GIF with 7-bit symbols (128 colors, 8-bit codes). Click on the image for an explanation of the code. |
|---|

The GIF encoding process can be modified to create a file without LZW compression that is still viewable as a GIF image. This technique was introduced originally as a way to avoid patent infringement. Uncompressed GIF can also be a useful intermediate format for a graphics programmer because individual pixels are accessible for reading or painting. An uncompressed GIF file can be converted to an ordinary GIF file simply by passing it through an image editor.

The modified encoding method ignores building the LZW table and emits only the root palette codes and the codes for CLEAR and STOP. This yields a simpler encoding (a 1-to-1 correspondence between code values and palette codes) but sacrifices all of the compression: each pixel in the image generates an output code indicating its color index. When processing an uncompressed GIF, a standard GIF decoder will not be prevented from writing strings to its dictionary table, but the code width must never increase since that triggers a different packing of bits to bytes.

If the symbol width is n, the codes of width *n*+1 fall naturally into two blocks: the lower block of 2*n* codes for coding single symbols, and the upper block of 2*n* codes that will be used by the decoder for sequences of length greater than one. Of that upper block, the first two codes are already taken: 2*n* for CLEAR and 2*n* + 1 for STOP. The decoder must also be prevented from using the last code in the upper block, 2*n*+1 − 1, because when the decoder fills that slot, it will increase the code width. Thus, in the upper bloc,k there are 2*n* − 3 codes available to the decoder that won't trigger an increase in code width. Because the decoder is always one step behind in maintaining the table, it does not generate a table entry upon receiving the first code from the encoder, but it will generate one for each succeeding code. Thus, the encoder can generate 2*n* − 2 codes without triggering an increase in code width. Therefore, the encoder must emit extra CLEAR codes at intervals of 2*n* − 2 codes or fewer to make the decoder reset the coding dictionary. The GIF standard allows such extra CLEAR codes to be inserted in the image data at any time. The composite data stream is partitioned into sub-blocks that each carry from 1 to 255 bytes.

For the sample 3×5 image above, the following 9-bit codes represent "clear" (100) followed by image pixels in scan order and "stop" (101).

```
100 028 0FF 0FF 0FF 028 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 0FF 101
```

After the above codes are mapped to bytes, the uncompressed file differs from the compressed file, thus:

| Byte # (hex) | Hexadecimal | Text or value | Meaning |
|---|---|---|---|
| 320 | 14 | 20 | 20 bytes uncompressed image data follow |
| 321 | 00 51 FC FB F7 0F C5 BF 7F FF FE FD FB F7 EF DF BF 7F 01 01 |   |   |
| 335 | 00 | 0 | End of image data |


## Compression example

The trivial example of a large image of solid color demonstrates the variable-length LZW compression used in GIF files.

| Code | Pixels | Notes |   |   |   |
|---|---|---|---|---|---|
| No.Ni | ValueNi + 256 | Length(bits) | This codeNi | Accumulated⁠Ni(Ni + 1)/2⁠ | Relations using Ni only apply to same-color pixels until the coding table is full. |
| 0 | 100h | 9 |   |   | Clear code table |
| 1 | FFh | 1 | 1 | Top left pixel color chosen as the highest index of a 256-color palette |   |
| 2 | 102h | 2 | 3 |   |   |
| 3⋮255 | 103h⋮1FFh | 3⋮255 | 6⋮32640 | Last 9-bit code |   |
| 256⋮767 | 200h⋮3FFh | 10 | 256⋮767 | 32896⋮294528 | Last 10-bit code |
| 768⋮1791 | 400h⋮7FFh | 11 | 768⋮1791 | 295296⋮1604736 | Last 11-bit code |
| 1792⋮3839 | 800h⋮FFFh | 12 | 1792⋮3839 | 1606528⋮7370880 | Code table full |
| ⋮ | FFFh | 3839 | The maximum code may repeat for more same-color pixels.Overall data compression asymptotically approaches 3839 × ⁠8/12⁠ = ⁠2559+1/3⁠ |   |   |
|   | 101h |   |   | End of image data |   |

The code values shown are packed into bytes, which are then packed into blocks of up to 255 bytes. A block of image data begins with a byte that declares the number of bytes to follow. The last block of data for an image is marked by a zero block-length byte.


## Interlacing

The GIF Specification allows each image within the logical screen of a GIF file to specify that it is interlaced; i.e., that the order of the raster lines in its data block is not sequential. This allows a partial display of the image that can be recognized before the full image is painted.

An interlaced image is divided from top to bottom into strips 8 pixels high, and the rows of the image are presented in the following order:

- Pass 1: Line 0 (the top-most line) from each strip.
- Pass 2: Line 4 from each strip.
- Pass 3: Lines 2 and 6 from each strip.
- Pass 4: Lines 1, 3, 5, and 7 from each strip.

The pixels within each line are not interlaced, but presented consecutively from left to right. As with non-interlaced images, there is no break between the data for one line and the data for the next. The indicator that an image is interlaced is a bit set in the corresponding Image Descriptor block.


## Animated GIF

Although GIF was not designed as an animation medium, its ability to store multiple images in one file naturally suggested using the format to store the frames of an animation sequence. To facilitate *displaying* animations, the GIF89a spec added the Graphic Control Extension (GCE), which allows the images (frames) in the file to be painted with time delays, forming a video clip. Each frame in an animation GIF is introduced by its own GCE specifying the time delay to wait after the frame is drawn. Global information at the start of the file applies by default to all frames. The data is stream-oriented, so the file offset of the start of each GCE depends on the length of preceding data. Within each frame, the LZW-coded image data is arranged in sub-blocks of up to 255 bytes; the size of each sub-block is declared by the byte that precedes it.

By default, an animation displays the sequence of frames only once, stopping when the last frame is displayed. To enable an animation to loop, Netscape in the 1990s used the Application Extension block (intended to allow vendors to add application-specific information to the GIF file) to implement the Netscape Application Block (NAB). This block, placed immediately before the sequence of animation frames, specifies the number of times the sequence of frames should be played (1 to 65535 times) or that it should repeat continuously (zero indicates loop forever). Support for these repeating animations first appeared in Netscape Navigator version 2.0, and then spread to other browsers. Most browsers now recognize and support NAB, though it is not strictly part of the GIF89a specification.

The following example shows the structure of the animation file *Rotating earth (large).gif* shown (as a thumbnail) in the article's infobox.

| Byte # (hex) | Hexadecimal | Text or value | Meaning |
|---|---|---|---|
| 0 | 47 49 46 38 39 61 | GIF89a | Logical Screen Descriptor |
| 6 | 90 01 | 400 | Width in pixels |
| 8 | 90 01 | 400 | Height in pixels |
| A | F7 |   | GCT follows for 256 colors with resolution 3 × 8 bits/primary |
| B | 00 | 0 | Background color: #000000, black |
| C | 00 | 0 | Default pixel aspect ratio, 0:0 |
| D | 00 |   | Global Color Table |
| ⋮ |   |   |   |
| 30D | 21 | `'!'` | An Extension Block (introduced by an ASCII exclamation point `'!'`) |
| 30E | FF |   | Application Extension |
| 30F | 0B | 11 | Size of block including application name and verification bytes (always 11) |
| 310 | 4E 45 54 53 43 41 50 45 32 2E 30 | NETSCAPE2.0 | 8-byte application name plus 3 verification bytes |
| 31B | 03 | 3 | Number of bytes in the following sub-block |
| 31C | 01 | 1 | Index of the current data sub-block *(always 1 for the NETSCAPE block)* |
| 31D | FF FF | 65535 | Unsigned number of repetitions |
| 31F | 00 |   | End of the sub-block chain for the Application Extension block |
| 320 | 21 | `'!'` | An Extension Block (introduced by an ASCII exclamation point `'!'`) |
| 321 | F9 |   | Graphic Control Extension for frame #1 |
| 322 | 04 | 4 | Number of bytes (4) in the current sub-block |
| 323 | 04 | 000..... ...001.. ......0. .......0 *(broken into sections for easier reading)* | Reserved, 5 lower bits are bit field Disposal method 1: do not dispose No user input Transparent color, 0 means not given |
| 324 | 09 00 | 9 | Frame delay: 0.09 second delay before painting next frame |
| 326 | FF |   | Transparent color index *(unused in this frame)* |
| 327 | 00 |   | End of sub-block chain for Graphic Control Extension block |
| 328 | 2C | `','` | An Image Descriptor (introduced by 0x2C, an ASCII comma `','`) |
| 329 | 00 00 00 00 | (0, 0) | North-west corner position of image in logical screen: (0, 0) |
| 32D | 90 01 90 01 | (400, 400) | Frame width and height: 400 × 400 pixels |
| 331 | 00 | 0 | Local color table: 0 means none & no interlacing |
| 332 | 08 | 8 | Minimum LZW code size for Image Data of frame #1 |
| 333 | FF | 255 | Number of bytes of LZW image data in the following sub-block: 255 bytes |
| 334 | ... | <image data> | Image data, 255 bytes |
| 433 | FF | 255 | Number of bytes of LZW image data in the following sub-block, 255 bytes |
| 434 | ... | <image data> | Image data, 255 bytes |
| ⋮ |   |   | Repeat for next blocks |
| 92C0 | 00 |   | End of sub-block chain for this frame |
| 92C1 | 21 | `'!'` | An Extension Block (introduced by an ASCII exclamation point `'!'`) |
| 92C2 | F9 |   | Graphic Control Extension for frame #2 |
| ⋮ |   |   | Repeat for next frames |
| EDABD | 21 | `'!'` | An Extension Block (introduced by an ASCII exclamation point `'!'`) |
| EDABE | F9 |   | Graphic Control Extension for frame #44 |
| ⋮ |   |   | Image information and data for frame #44 |
| F48F5 | 3B |   | Trailer: Last byte in the file, signaling EOF |

The animation delay for each frame is specified in the GCE in hundredths of a second. Some economy of data is possible where a frame needs only to rewrite a few of the pixels on the display, because the Image Descriptor can define a smaller rectangle to be rescanned instead of the whole image. Browsers or other displays that do not support animated GIFs typically show only the first frame.

The size and color quality of animated GIF files can vary significantly depending on the application used to create them. Strategies for minimizing file size include using a common global color table for all frames (rather than a complete local color table for each frame) and minimizing the number of pixels covered in successive frames (so that only the pixels that change from one frame to the next are included in the latter frame). More advanced techniques involve modifying color sequences to better match the existing LZW dictionary, a form of lossy compression. Simply packing a series of independent frame images into a composite animation tends to yield large file sizes. Tools are available to minimize the file size of an existing GIF.

Metadata can be stored in GIF files as a comment block, a plain text block, or an application-specific application extension block. Several graphics editors use unofficial application extension blocks to include the data used to generate the image, so that it can be recovered for further editing.

All of these methods technically require the metadata to be broken into sub-blocks so that applications can navigate the metadata block without knowing its internal structure.

The Extensible Metadata Platform (XMP) metadata standard introduced an unofficial but now widespread "XMP Data" application extension block for including XMP data in GIF files. Since the XMP data is encoded using UTF-8 without NUL characters, there are no 0 bytes in the data. Rather than break the data into formal sub-blocks, the extension block terminates with a "magic trailer" that routes any application treating the data as sub-blocks to a final 0 byte that terminates the sub-block chain.


## Unisys and LZW patent enforcement

In 1977 and 1978, Jacob Ziv and Abraham Lempel published a pair of papers on a new class of lossless data-compression algorithms, now collectively referred to as LZ77 and LZ78. In 1983, Terry Welch developed a fast variant of LZ78 which was named Lempel–Ziv–Welch (LZW).

Welch filed a patent application for the LZW method in June 1983. The resulting patent, US4558302, granted in December 1985, was assigned to Sperry Corporation who subsequently merged with Burroughs Corporation in 1986 and formed Unisys. Further patents were obtained in the United Kingdom, France, Germany, Italy, Japan and Canada.

In addition to the above patents, Welch's 1983 patent also includes citations to several other patents that influenced it, including:

- two 1980 Japanese patents from NEC's Jun Kanatsu,
- U.S. patent 4,021,782 (1974) from John S. Hoerning,
- U.S. patent 4,366,551 (1977) from Klaus E. Holtz, and
- a 1981 German patent from Karl Eckhart Heinz.

In June 1984, an article by Welch was published in the IEEE magazine, which publicly described the LZW technique for the first time. LZW became a popular data compression technique and, when the patent was granted, Unisys entered into licensing agreements with over a hundred companies.

The popularity of LZW led CompuServe to choose it as the compression technique for their version of GIF, developed in 1987. At the time, CompuServe was not aware of the patent. Unisys became aware that the version of GIF used the LZW compression technique and entered into licensing negotiations with CompuServe in January 1993. The subsequent agreement was announced on 24 December 1994. Unisys stated that they expected all major commercial online information services companies employing the LZW patent to license the technology from Unisys at a reasonable rate, but that they would not require licensing or fees to be paid for non-commercial, non-profit GIF-based applications, including those for use on the online services.

Following this announcement, there was widespread condemnation of CompuServe and Unisys, and many software developers threatened to stop using GIF. The PNG format (see below) was developed in 1995 as an intended replacement. However, obtaining support from the makers of Web browsers and other software for the PNG format proved difficult, and it was not possible to replace GIF, although PNG has gradually increased in popularity. Therefore, GIF variations without LZW compression were developed. For instance the libungif library, based on Eric S. Raymond's giflib, allows creation of GIFs that followed the data format but avoided the compression features, thus avoiding use of the Unisys LZW patent. A 2001 *Dr. Dobb's* article described a way to achieve LZW-compatible encoding for data that would compress well under a run-length encoding mechanism without infringing on its patents.

In August 1999, Unisys changed the details of its licensing practice, announcing the option for owners of certain non-commercial and private websites to obtain licenses on payment of a one-time license fee of $5000 or $7500. Such licenses were not required for website owners or other GIF users who had used licensed software to generate GIFs. Nevertheless, Unisys was subjected to thousands of online attacks and abusive emails from users believing that they were going to be charged $5000 or sued for using GIFs on their websites. Despite giving free licenses to hundreds of non-profit organizations, schools and governments, Unisys was completely unable to generate any good publicity and continued to be condemned by individuals and organizations such as the League for Programming Freedom who started the "Burn All GIFs" campaign in 1999.

The United States LZW patent expired on 20 June 2003. The counterpart patents in the United Kingdom, France, Germany, and Italy expired on 18 June 2004, the Japanese patents expired on 20 June 2004, and the Canadian patent expired on 7 July 2004. Consequently, while Unisys has further patents and patent applications relating to improvements to the LZW technique, LZW itself (and consequently GIF) have been free to use since July 2004.
