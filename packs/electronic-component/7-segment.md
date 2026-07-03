---
title: "Segment display"
source: https://en.wikipedia.org/wiki/7_segment
domain: electronic-component
license: CC-BY-SA-4.0
tags: electronic component
fetched: 2026-07-03
---

# Segment display

(Redirected from

7 segment

)

Some displays can show only digits or alphanumeric characters. They are called **segment displays**, because they are composed of several segments that switch on and off to give appearance of desired glyph. The segments are usually single LEDs or liquid crystals. They are mostly used in digital watches and pocket calculators. Common types are seven-segment displays which are used for numerals only, and alphanumeric fourteen-segment displays and sixteen-segment displays which can display numerals and Roman alphabet letters.

## Seven-segment display

A **seven-segment display** is a display device for digits and some letters. It is often used in a device to display numbers – for example in a digital clock or calculator. To a lesser extent, but still common, it is used to display alphanumeric information. Since a seven-segment display tends to be less expensive than a display that can better represent any character and even a graphic image such as a dot matrix display, the design choice to use a seven-segment display is a tradeoff to minimize cost over providing richer functionality.

### History

Seven-segment representation of figures can be found in patents as early as 1903 (in U.S. patent 1,126,641), when Carl Kinsley invented a method of telegraphically transmitting letters and numbers and having them printed on tape in a segmented format. In 1908, F. W. Wood invented an 8-segment display, which displayed the number 4 using a diagonal bar (U.S. patent 974,943). In 1910, a seven-segment display illuminated by incandescent bulbs was used on a power-plant boiler room signal panel. They were also used to show the dialed telephone number to operators during the transition from manual to automatic telephone dialing. They did not achieve widespread use until the advent of LEDs in the 1970s.

Some early seven-segment displays used incandescent filaments in an evacuated bulb; they are also known as numitrons. A variation (minitrons) made use of an evacuated potted box. Minitrons are filament segment displays that are housed in DIP (dual in-line package) packages like modern LED segment displays. They may have up to 16 segments. There were also segment displays that used small incandescent light bulbs instead of LEDs or incandescent filaments. These worked similarly to modern LED segment displays.

Vacuum fluorescent display versions were also used in the 1970s.

Many early (c. 1970s) LED seven-segment displays had each digit built on a single die. This made the digits very small. Some included magnifying lenses in the design to try to make the digits more legible. Other designs used 1 or 2 dies for every segment of the display.

Liquid-crystal display (LCD) largely superseded LED seven-segment displays. The shapes of elements in an LCD panel are arbitrary since they are formed on the display by photolithography, while LED segments tend to be simple rectangles, because they have to be physically moulded to shape, which makes it difficult to form more complex shapes. However, the easy recognition of seven-segment displays, and the comparatively high visual contrast obtained by such displays relative to dot-matrix digits, makes seven-segment multiple-digit LCD screens very common on basic calculators.

Seven-segment displays have been recommended against for critical information (i.e. information that is dangerous to health or safety if misread) due to misreading if upside down or if segments are "stuck" on or off. Backlit dot-matrix LCDs have largely superseded seven-segment displays on such equipment.

The seven-segment display has inspired type designers to produce typefaces reminiscent of that display (but more legible), such as New Alphabet, "DB LCD Temp", "ION B", etc. The seven-segment pattern is sometimes used in posters or tags, where the user either applies color to pre-printed segments, or applies color through a seven-segment digit template, to compose figures such as product prices or telephone numbers.

Seven-segment displays, which use a restricted range of letters that look like (upside-down) digits, are commonly used by school children to form words and phrases using a technique known as "calculator spelling."

- (Gas station price display) Gas station price display
- (Calculator that has a tail on the "7" digit) Calculator that has a tail on the "7" digit
- (Apollo Guidance Computer control panel reproduction) Apollo Guidance Computer control panel reproduction
- (Marantz CD63SE CD player with a vacuum fluorescent display in test mode) Marantz CD63SE CD player with a vacuum fluorescent display in test mode
- (Marantz CC-45 CD player display) Marantz CC-45 CD player display
- (A Beijing bus displaying the route number 695 using a seven-segment display) A Beijing bus displaying the route number 695 using a seven-segment display

### Implementations

Seven-segment displays may use a liquid-crystal display (LCD), a light-emitting diode (LED) for each segment, an electrochromic display, or other light-generating or -controlling techniques such as cold cathode gas discharge (neon) (Panaplex), vacuum fluorescent (VFD), incandescent filaments (Numitron), and others. For gasoline price totems and other large signs, electromechanical seven-segment displays made up of electromagnetically flipped light-reflecting segments are still commonly used. A precursor to the 7-segment display in the 1950s through the 1970s was the cold-cathode, neon-lamp-like nixie tube. Starting in 1970, RCA sold a display device known as the *Numitron* that used incandescent filaments arranged into a seven-segment display. In USSR, the first electronic calculator "Vega", which was produced from 1964, contains 20 decimal digits with seven-segment electroluminescent display.

In a simple LED package, typically all of the cathodes (negative terminals) or all of the anodes (positive terminals) of the segment LEDs are connected and brought out to a common pin; this is referred to as a "common cathode" or "common anode" device. Hence a 7 segment plus decimal point package will only require nine pins, though commercial products typically contain more pins, and/or spaces where pins would go, in order to match standard IC sockets. Integrated displays also exist, with single or multiple digits. Some of these integrated displays incorporate their own internal decoder, though most do not: each individual LED is brought out to a connecting pin as described.

Multiple-digit LED displays as used in pocket calculators and similar devices used multiplexed displays to reduce the number of I/O pins required to control the display. For example, all the anodes of the A segments of each digit position would be connected together and to a driver circuit pin, while the cathodes of all segments for each digit would be connected. To operate any particular segment of any digit, the controlling integrated circuit would turn on the cathode driver for the selected digit, and the anode drivers for the desired segments; then after a short blanking interval the next digit would be selected and new segments lit, in a sequential fashion. In this manner an eight digit display with seven segments and a decimal point would require only 8 cathode drivers and 8 anode drivers, instead of sixty-four drivers and IC pins. Often in pocket calculators the digit drive lines would be used to scan the keyboard as well, providing further savings; however, pressing multiple keys at once would produce odd results on the multiplexed display.

- (A multiplexed 4-digit, seven-segment display with only 12 pins) A multiplexed 4-digit, seven-segment display with only 12 pins
- (A 4-digit display scanning by columns to make the number 1.234) A 4-digit display scanning by columns to make the number 1.234
- (X-Ray of an 8-digit 7-segment multiplexed LED display from a 1970s calculator) X-Ray of an 8-digit 7-segment multiplexed LED display from a 1970s calculator

### Characters

The seven segments are arranged as a rectangle, with two vertical segments on each side and one horizontal segment each at the top, middle, and bottom. Often the rectangle is *oblique* (slanted), which may aid readability. In most applications, the segments are of nearly uniform shape and size (usually elongated hexagons, though trapezoids and rectangles can also be used); though in the case of adding machines, the vertical segments are longer and more oddly shaped at the ends, to try to make them more easily readable. The seven elements of the display can be lit in different combinations to represent each of the Arabic numerals.

The individual segments are referred to by the letters "a" to "g", and an optional decimal point (an "eighth segment", referred to as DP) is sometimes used for the display of non-integer numbers. A single byte can encode the full state of a seven-segment display, including the decimal point. The most popular bit encodings are *gfedcba* and *abcdefg*. In the *gfedcba* representation, a byte value of 0x06 would turn on segments "c" and "b", which would display a "1" ((1)).

#### Decimal

The numerical digits 0 to 9 are the most common characters displayed on seven-segment displays. The most common patterns used for each of these are:

Alternative patterns: The numeral 1 may be represented with the left segments, the numerals 6 and 9 may be represented without a "tail", and the numeral 7 represented *with* a "tail":

In Unicode 13.0, 10 codepoints had been given for segmented digits 0–9 in the Symbols for Legacy Computing block, to replicate early computer fonts that included seven-segment versions of the digits. The official reference shows the less-common four-segment "7" ((7*)).

#### Hexadecimal

The binary-coded decimal (BCD) 0 to 9 digit values require four binary bits to hold their values. Since four bits (24) can hold 16 values, this means hexadecimal (hex) digits can be represented by four bits too. Due to the limited number of segments in seven-segment displays, the hexadecimal digits B and D are displayed as lowercase letters to avoid confusion with 8 ((B)) and 0 ((D)) respectively. The digit "6" must also be displayed with the topmost segment as (6) to avoid ambiguity with the letter "b" ((b)).

Early decoder ICs often produced unintuitive patterns or duplicates of digits for 10-15, as they were designed to use as few gates as possible and only required to produce 0-9.

#### Letters

Many letters of the Latin alphabet can be reasonably implemented on a seven-segment display. Though not every letter is available, it is possible to create many useful words. By careful choice of words, one can sometimes work around unavailable letters. Uppercase letters "B", "I", "S", "Z", and "D" & "O" conflict with the common seven-segment representation of digits "8", "1", "5", "2", and "0" ((B), (I*), (S), (Z), (O)) respectively, and the lowercase letter "g" with digit "9" ((g*)). Upper case I ((I)) could be put on the left (as lower-case L is shown here) but this is not often done. Lowercase 'b' and 'q' are identical to the alternate numerical digits '6' and '9' ((b), (q)).

Latin alphabet

A

B

C

D

E

F

G

H

I

J

K

L

M

N

O

P

Q

R

S

T

U

V

W

X

Y

Z

Upper

Lower

Greek alphabet

Α

Β

Γ

Δ

Ε

Ζ

Η

Θ

Ι

Κ

Λ

Μ

Ν

Ξ

Ο

Π

Ρ

Σ

Τ

Υ

Φ

Χ

Ψ

Ω

Upper

Lower

The following are some English word examples seen on actual electronic equipment (first line appeared on some CD players):

,

,

,

,

,

,

,

,

,

,

,

,

,

,

,

,

,

## Eight-segment display

An **eight-segment display** is a type of display based on eight segments that can be turned on or off according to the font pattern to be produced.

### Applications

One application was in the Sharp EL-8, an early electronic calculator. The eight-segment display produces more rounded digits than a seven-segment display, yielding a more "script-like" output, with the trade-off that fewer possible alphabetic characters can be displayed because the bars *F* and *G* are merged (see table below).

### Displaying

An eight segment display can sometimes display alphabetic characters with less readability because the segments *F* and *G* are combined and the corners are rounded. The asymmetrical layout of the elements produced a distinctive "handwritten" digit style, with a half-height "0".

| Script | Characters |
|---|---|
| Latin | C, c, d, G, L, N, n, 0, o, r, U, Z, Ə |
| Greek | Γ, Ζ, Ν, Ξ, Ο, ο, Π, π |
| Cyrillic | Г, г, д, П, п, Э |
| Others | 0, (, [, ", ^, -, /, ? |

| Characters | What they display as on an eight-segment display |
|---|---|
| C, [, ( | E |
| c, L, r, г | t |
| d, U | Ɐ |
| G | 6 |
| N, Ν, λ, Π, П | A |
| n, π, п | h |
| o, ο | b |
| Z, Ζ, | e |
| 0, O, Ə, Ο, д | 8 |
| Γ, Г | F |
| Ξ | C̠ |
| Э | 9 |
| " | ˅ |
| ^ | ° |
| - | ` |
| / | μ |
| ? | P |

### Examples

- (Sharp EL-8 with eight-segment displays) Sharp EL-8 with eight-segment displays
- (Eight-segment display displaying an 8) Eight-segment display displaying an 8
- (Eight-segment display displaying a D) Eight-segment display displaying a D

## Nine-segment display

| (Nine-segment display) Nine-segment display (Alternate) Alternate (Alternate) Alternate (Alternate) Alternate |
|---|

A **nine-segment display** is a type of display based on nine segments that can be turned on or off according to the graphic pattern to be produced. It is an extension of the more common seven-segment display, having an additional two diagonal or vertical segments (one between the top and the middle, and the other between the bottom and the horizontal segments). It provides an efficient method of displaying alphanumeric characters.

The letters displayed by a nine-segment display are not consistently uppercase or lowercase in shape. A common compromise is to use a lower-case "n" instead of "N". Depending on the design of the display segments, the use of the extra two segments may be avoided whenever possible, as in the Nixxo X-Page "tall" lowercase "r" and "y".

### Uses

In some Soviet digital calculators of the 1970s, such as the Elektronika 4-71b, 9-segment displays were used to provide basic alphanumerics and avoid confusions with representing numbers in Soviet postcodes.

Digit 3

Letter З (ze)

Different segments for similar glyphs

The extra two bars were slanted forward, allowing for an appropriate-looking И, and to differentiate the numeral 3 from the letter З. The Sharp Compet calculator also uses a 9-segment display, allowing a small range of characters and symbols to be used.

Nine-segment displays are used in many Timex digital watches, and some pagers, such as the Nixxo XPage, the Arch BR502 pager, and the Scope Geo N8T. They are also used in some Epson Stylus printers, and Newport iSeries digital meters. The display used in the iSeries is unique in that it has a vertical extra segment at top, and a fully backwards-leaning slant for the extra segment at bottom. This allows for a somewhat more natural-appearing R and M.

Pinball tables produced by Bally from 1986 to 1989 used nine-segment scoring displays.

A nine-segment display has been developed for displaying Bengali and Roman numerals.

- (Nine-segment vacuum fluorescent display) Nine-segment vacuum fluorescent display
- (Postal code nine-segment sample on an envelope) Postal code nine-segment sample on an envelope
- (Postcard from Latvia just before its independence) Postcard from Latvia just before its independence

## Fourteen-segment display

A **fourteen-segment display** (**FSD**), also known as a **starburst display** or **Union Jack display**, is a type of display based on 14 segments that can be turned on or off to produce letters and numerals. It is an expansion of the more common seven-segment display, having an additional four diagonal and two vertical segments with the middle horizontal segment broken in half. A seven-segment display suffices for numerals and certain letters, but unambiguously rendering the ISO basic Latin alphabet requires more detail. A slight variation is the sixteen-segment display which allows additional legibility in displaying letters or other symbols.

A decimal point or comma may be present as an additional segment, or pair of segments; the comma (used for triple-digit groupings or as a decimal separator in many regions) is commonly formed by combining the decimal point with a closely 'attached' leftwards-descending arc-shaped segment.

Electronic alphanumeric displays may use LEDs, LCDs, or vacuum fluorescent display devices. The LED variant is typically manufactured in single or dual character packages, allowing the system designer to choose the number of characters suiting the application.

Often a character generator is used to translate 7-bit ASCII character codes to the 14 bits that indicate which of the 14 segments to turn on or off.

### Character encoding

By lighting different elements, different characters can be displayed.

In a 14-segment display, there is also an optional 15th segment which is a decimal point (denoted as "DP").

#### Decimal

Hexadecimal encoding of decimal numbers for 14-segment display

Digit

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

Hex code

0xC3F

0x406

0xDB

0x8F

0xE6

0xED

0xFD

0x1401

0xFF

0xE7

#### Latin alphabet

A 14-segment display is mostly used to display text because the 14 elements allow all Latin letters to be displayed both in upper case and lower case (with a few exceptions like "s").

Hexadecimal Encoding of Latin Alphabet for 14-segment display

Alphabet

A

B

C

D

E

F

G

H

I

J

K

L

M

N

Hex code

0xF7

0x128F

0x39

0x120F

0xF9

0xF1

0xBD

0xF6

0x1209

0x1E

0x2470

0x38

0x536

0x2136

Alphabet

O

P

Q

R

S

T

U

V

W

X

Y

Z

Hex code

0x3F

0xF3

0x203F

0x20F3

0x18D

0x1201

0x3E

0xC30

0x2836

0x2D00

0x1500

0xC09

### Applications

Multiple-segment display devices use fewer elements than a full dot-matrix display, and may produce a better character appearance where the segments are shaped appropriately. This can reduce power consumption and the number of driver components.

Fourteen-segment gas-plasma displays were used in pinball machines from 1986 through 1991 with an additional comma and period part making for a total of 16 segments.

Fourteen and sixteen-segment displays were used to produce alphanumeric characters on calculators and other embedded systems. Applications today include displays fitted to telephone Caller ID units, gymnasium equipment, VCRs, car stereos, microwave ovens, slot machines, and DVD players.

Such displays were very common on pinball machines for displaying the score and other information, before the widespread use of dot-matrix display panels.

#### Incandescent lamp

Multiple segment alphanumeric displays are nearly as old as the use of electricity. A 1908 textbook describes an alphanumeric display system using incandescent lamps and a mechanical switching arrangement. Each of 21 lamps was connected to a switch operated by a set of slotted bars, installed in a rotating drum. This *commutator* assembly could be arranged so that as the drum was rotated, different sets of switches were closed and different letters and figures could be displayed. The scheme would have been used for "talking" signs to spell out messages, but a complete set of commutator switches, drums and lamps would have been required for each letter of a message, making the resulting sign quite expensive.

#### Cold-cathode neon

A few different versions of the fourteen segment display exist as cold-cathode neon lamps. For example, one type made by Burroughs Corporation was called "Panaplex". Instead of using a filament as the incandescent versions do, these use a cathode charged to a 180 V potential which causes the electrified segment to glow a bright orange color.

#### Examples

- (A four-character 14-segment clock display. Note unbroken top and bottom segments in comparison with a sixteen-segment display.) A four-character 14-segment clock display. Note unbroken top and bottom segments in comparison with a sixteen-segment display.
- (Fourteen-segment characters on Hewlett-Packard's HP-41 range of programmable engineering calculators from the late 1970s) Fourteen-segment characters on Hewlett-Packard's HP-41 range of programmable engineering calculators from the late 1970s
- (14-segment characters on the Hewlett-Packard HP3478A multimeter) 14-segment characters on the Hewlett-Packard HP3478A multimeter
- (Fourteen-segment characters on an after-market car stereo LCD) Fourteen-segment characters on an after-market car stereo LCD
- (A Sony Mini Hi-Fi Component System which utilizes a fourteen-segment display.) An inverted, backlit fourteen-segment LCD used in a Sony MHC-EC55 mini Hi-Fi component system

## Sixteen-segment display

A **sixteen-segment display** (**SISD**) is a type of display based on sixteen segments that can be turned on or off to produce a graphic pattern. It is an extension of the more common seven-segment display, adding four diagonal and two vertical segments and splitting the three horizontal segments in half. Other variants include the fourteen-segment display which does not split the top or bottom horizontal segments, and the twenty-two-segment display that allows lower-case characters with descenders.

Often a character generator is used to translate 7-bit ASCII character codes to the 16 bits that indicate which of the 16 segments to turn on or off.

### Applications

Sixteen-segment displays were originally designed to display alphanumeric characters (Latin letters and Arabic digits). Later they were used to display Thai numerals and Persian characters. Non-electronic displays using this pattern existed as early as 1902.

Before the advent of inexpensive dot-matrix displays, sixteen and fourteen-segment displays were used to produce alphanumeric characters on calculators and other embedded systems. Later they were used on videocassette recorders (VCR), DVD players, microwave ovens, car stereos, telephone Caller ID displays, and slot machines.

Sixteen-segment displays may be based on one of several technologies, the three most common optoelectronics types being LED, LCD and VFD. The LED variant is typically manufactured in single or dual character packages, to be combined as needed into text line displays of a suitable length for the application in question; they can also be stacked to build multiline displays.

As with seven and fourteen-segment displays, a decimal point and/or comma may be present as an additional segment, or pair of segments; the comma (used for triple-digit groupings or as a decimal separator in many regions) is commonly formed by combining the decimal point with a closely 'attached' leftwards-descending arc-shaped segment. This way, a point or comma may be displayed between character positions instead of occupying a whole position by itself, which would be the case if employing the bottom middle vertical segment as a point and the bottom left diagonal segment as a comma. Such displays were very common on pinball machines for displaying the score and other information, before the widespread use of dot-matrix display panels.

#### Examples

- (A sixteen-segment display on a Beatmania IIDX arcade machine) A sixteen-segment display on a *Beatmania IIDX* arcade machine
- (An eighteen-segment vacuum fluorescent display. Two extra segments are used for lower elements of Cyrillic letters Д, Ц, Щ, Җ, Қ, Ң, Ҵ, Ҷ, Ԥ.[47]) An eighteen-segment vacuum fluorescent display. Two extra segments are used for lower elements of Cyrillic letters Д, Ц, Щ, Җ, Қ, Ң, Ҵ, Ҷ, Ԥ.
- (A sixteen-segment display on an AIM-65) A sixteen-segment display on an AIM-65
