---
title: "ANSEL"
source: https://en.wikipedia.org/wiki/ANSEL
domain: combining-character
license: CC-BY-SA-4.0
tags: combining character
fetched: 2026-07-03
---

# ANSEL

**ANSEL**, the **American National Standard for Extended Latin Alphabet Coded Character Set for Bibliographic Use**, was a character set used in text encoding. It provided a table of coded values for the representation of characters of the extended Latin alphabet in machine-readable form for thirty-five languages written in the Latin alphabet and for fifty-one romanized languages. ANSEL adds 63 graphic characters to ASCII, including 29 combining diacritic characters.

The initial revision of ANSEL was released in 1985, and before 1993 it was registered as Registration #231 in the ISO International Register of Coded Character Sets to be Used with Escape Sequences. The standard was reaffirmed in 2003 although it has been administratively withdrawn by ANSI effective 14 February 2013.

The requirement of hardware capable of overprinting accents made this mostly impossible from ever becoming a popular extended ASCII.

## Code page layout

The following table shows ANSI/NISO Z39.47-1993 (R2003). Non-ASCII characters are shown with their Unicode code point. A combining diacritic *precedes* the spacing character on which it should be superimposed (in Unicode the combining diacritic is *after* the base character).

ANSI/NISO Z39.47-1993 (R2003)

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

A

B

C

D

E

F

0x

NUL

SOH

STX

ETX

EOT

ENQ

ACK

BEL

BS

HT

LF

VT

FF

CR

SO

SI

1x

DLE

DC1

DC2

DC3

DC4

NAK

SYN

ETB

CAN

EM

SUB

ESC

FS

GS

RS

US

2x

SP

!

"

#

$

%

&

'

(

)

*

+

,

-

.

/

3x

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

:

;

<

=

>

?

4x

@

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

5x

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

[

\

]

^

_

6x

`

a

b

c

d

e

f

g

h

i

j

k

l

m

n

o

7x

p

q

r

s

t

u

v

w

x

y

z

{

|

}

~

DEL

8x

9x

Ax

Ł

0141

Ø

00D8

Đ

0110

Þ

00DE

Æ

00C6

Œ

0152

ʹ

02B9

·

00B7

♭

266D

®

00AE

±

00B1

Ơ

01A0

Ư

01AF

ʼ

02BC

Bx

ʻ

02BB

ł

0142

ø

00F8

đ

0111

þ

00FE

æ

00E6

œ

0153

ʺ

02BA

ı

0131

£

00A3

ð

00F0

ơ

01A1

ư

01B0

Cx

°

00B0

ℓ

2113

℗

2117

©

00A9

♯

266F

¿

00BF

¡

00A1

Dx

Ex

◌̉

0309

◌̀

0300

◌́

0301

◌̂

0302

◌̃

0303

◌̄

0304

◌̆

0306

◌̇

0307

◌̈

0308

◌̌

030C

◌̊

030A

◌︠

FE20

◌︡

FE21

◌̕

0315

◌̋

030B

◌̐

0310

Fx

◌̧

0327

◌̨

0328

◌̣

0323

◌̤

0324

◌̥

0325

◌̳

0333

◌̲

0332

◌̦

0326

◌̜

031C

◌̮

032E

◌︢

FE22

◌︣

FE23

◌̓

0313

## Use

### GEDCOM

The GEDCOM specification for exchanging genealogical data refers to ANSEL (ANSI/NISO Z39.47-1985) as a valid text encoding for GEDCOM files and extends it with additional characters which are shown in the following table.

| Hex | Unicode | Glyph | Description |
|---|---|---|---|
| 0xBE | 25A1 | □ | empty box |
| 0xBF | 25A0 | ■ | black box |
| 0xCD | 0065 | e | midline e |
| 0xCE | 006F | o | midline o |
| 0xCF | 00DF | ß | es zet |
| 0xFC | 0338 | ̸ | diacritic slash through char |

### MARC21

The Extended Latin character set from MARC 21 is synchronized with ANSEL but additionally supports the eszett (ß) character at C7 and the euro sign (€) at C8.
