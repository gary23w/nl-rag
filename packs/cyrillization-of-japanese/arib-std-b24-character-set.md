---
title: "ARIB STD B24 character set"
source: https://en.wikipedia.org/wiki/ARIB_STD_B24_character_set
domain: cyrillization-of-japanese
license: CC-BY-SA-4.0
tags: cyrillization of japanese
fetched: 2026-07-03
---

# ARIB STD B24 character set

Volume 1 of the Association of Radio Industries and Businesses (ARIB) STD-B24 standard for Broadcast Markup Language specifies, amongst other details, a character encoding for use in Japanese-language broadcasting. It was introduced on 1999-10-26. The latest revision is version 6.3 as of 2016-07-06.

It includes a number of **ARIB extended characters** (ARIB外字, *ARIB gaiji*) not found in the base standards (JIS X 0208 and JIS X 0201). It was the source standard for many symbol characters which were added to Unicode, including portions of the Miscellaneous Symbols, Enclosed Alphanumeric Supplement and Enclosed Ideographic Supplement blocks. Its contributions partially overlap the Unicode emoji, but were added a year earlier, in Unicode 5.2.

Fascicle 1 of the ARIB STD-B62 standard, published in 2014, defines Unicode mappings for a selection of the B24 extended characters (excluding, for example, those duplicated by JIS X 0213), as well as a few extended Kanji. It also includes a mapping of utilised characters outside the Basic Multilingual Plane to the BMP's private use area.

## Sets and codes

The ARIB STD B24 standard defines multiple character sets and a method of switching between them. These include a Kanji set (an extension of JIS X 0208), an Alphanumeric set, a Hiragana set, Katakana sets of two distinct layouts and four mosaic sets. The sets are selected using ISO 2022 mechanisms for 94-sets, using the following codes (proportional sets use the same layout as the corresponding non-proportional ones):

| Set | Type | Code (column/line) | Code (hexadecimal) | Code (ASCII character) | Comments |
|---|---|---|---|---|---|
| Kanji | 2-byte | 4/2 | 42 | `B` | The escape code `B` used for the ARIB Kanji set is used for the 1983 version of JIS C 6226 (JIS X 0208, of which the ARIB Kanji set is an extension) in ISO-2022-JP. |
| Alphanumeric | 1-byte | 4/10 | 4A | `J` | JIS_C6220-ro (ISO646-JP, JIS X 0201 Roman set). Similar to ASCII, with two assignments differing. Escape code `J` matches usage in ISO-2022-JP. |
| Proportional alphanumeric | 1-byte | 3/6 | 36 | `6` |   |
| Hiragana | 1-byte | 3/0 | 30 | `0` | Hiragana themselves follow the same layout as row 4 of JIS X 0208, but without a lead byte. Also adds several additional assignments for punctuation. |
| Proportional Hiragana | 1-byte | 3/7 | 37 | `7` |   |
| Katakana | 1-byte | 3/1 | 31 | `1` | Katakana themselves follow the same layout as row 5 of JIS X 0208, but without a lead byte. Also adds several additional assignments for punctuation. |
| Proportional Katakana | 1-byte | 3/8 | 38 | `8` |   |
| JIS X 0201 Katakana | 1-byte | 4/9 | 49 | `I` | JIS_C6220-jp (JIS X 0201 Kana set). Escape code matches usage in ISO-2022-JP-3. |
| Mosaic A | 1-byte | 3/2 | 32 | `2` | Pseudographics (ISO-IR-71) |
| Mosaic B | 1-byte | 3/3 | 33 | `3` | Pseudographics (ISO-IR-137) |
| Mosaic C | 1-byte | 3/4 | 34 | `4` | Non-spacing pseudographics (ISO-IR-71 subset with separated mosaic blocks) |
| Mosaic D | 1-byte | 3/5 | 35 | `5` | Non-spacing pseudographics |

## Code charts

### Kanji (double-byte) set

This is a double-byte character set extending JIS X 0208.

#### Lead byte

The encoding bytes correspond to the row or cell number plus 0x20, or 32 in decimal (see below). Hence, the code set starting with 0x21 has a row number of 1, and its cell 1 has a continuation byte of 0x21 (or 33), and so forth. Most of the code corresponds to JIS X 0208.

ARIB STD-B24 Kanji (double-byte) set (lead bytes)

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

2x

SP

1-_

2-_

3-_

4-_

5-_

6-_

7-_

8-_

9-_

10-_

11-_

12-_

13-_

14-_

15-_

3x

16-_

17-_

18-_

19-_

20-_

21-_

22-_

23-_

24-_

25-_

26-_

27-_

28-_

29-_

30-_

31-_

4x

32-_

33-_

34-_

35-_

36-_

37-_

38-_

39-_

40-_

41-_

42-_

43-_

44-_

45-_

46-_

47-_

5x

48-_

49-_

50-_

51-_

52-_

53-_

54-_

55-_

56-_

57-_

58-_

59-_

60-_

61-_

62-_

63-_

6x

64-_

65-_

66-_

67-_

68-_

69-_

70-_

71-_

72-_

73-_

74-_

75-_

76-_

77-_

78-_

79-_

7x

80-_

81-_

82-_

83-_

84-_

85-_

86-_

87-_

88-_

89-_

90-_

91-_

92-_

93-_

94-_

DEL

Unused lead byte

Lead byte

Differences from JIS X 0208

#### Character sets 0x21-0x74 (row numbers 1-84: punctuation, alphabets, numbers, Kana, Kanji)

#### Character set 0x75–0x76 (row numbers 85–86, additional kanji)

This part is the source standard for a small number of CJK Unified Ideographs in Unicode, where it is designated with the `JARIB-` source prefix in the Unihan database.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x75)

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

2x

㐂

3402

𠅘

20158

份

4EFD

仿

4EFF

侚

4F9A

俉

4FC9

傜

509C

儞

511E

冼

51BC

㔟

351F

匇

5307

卡

5361

卬

536C

詹

8A79

𠮷

20BB7

3x

呍

544D

咖

5496

咜

549C

咩

54A9

唎

550E

啊

554A

噲

5672

囤

56E4

圳

5733

圴

5734

塚

FA10

墀

5880

姤

59E4

娣

5A23

婕

5A55

寬

5BEC

4x

﨑

FA11

㟢

37E2

庬

5EAC

弴

5F34

彅

5F45

德

5FB7

怗

6017

恵

FA6B

愰

6130

昤

6624

曈

66C8

曙

66D9

曺

66FA

曻

66FB

桒

6852

鿄

9FC4

5x

椑

6911

椻

693B

橅

6A45

檑

6A91

櫛

6ADB

𣏌

233CC

𣏾

233FE

𣗄

235C4

毱

6BF1

泠

6CE0

洮

6D2E

海

FA45

涿

6DBF

淊

6DCA

淸

6DF8

渚

FA46

6x

潞

6F5E

濹

6FF9

灤

7064

𤋮

FA6C

𤋮

242EE

煇

7147

燁

71C1

爀

7200

玟

739F

玨

73A8

珉

73C9

珖

73D6

琛

741B

琡

7421

琢

FA4A

琦

7426

7x

琪

742A

琬

742C

琹

7439

瑋

744B

㻚

3EDA

畵

7575

疁

7581

睲

7772

䂓

4093

磈

78C8

磠

78E0

祇

7947

禮

79AE

鿆

9FC6

䄃

4103

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x76)

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

2x

鿅

9FC5

秚

79DA

稞

7A1E

筿

7B7F

簱

7C31

䉤

4264

綋

7D8B

羡

7FA1

脘

8118

脺

813A

舘

FA6D

芮

82AE

葛

845B

蓜

84DC

蓬

84EC

3x

蕙

8559

藎

85CE

蝕

8755

蟬

87EC

蠋

880B

裵

88F5

角

89D2

諶

8AF6

跎

8DCE

辻

8FBB

迶

8FF6

郝

90DD

鄧

9127

鄭

912D

醲

91B2

鈳

9233

4x

銈

9288

錡

9321

鍈

9348

閒

9592

雞

96DE

餃

9903

饀

9940

髙

9AD9

鯖

9BD6

鷗

9DD7

麴

9EB4

麵

9EB5

5x

6x

7x

#### Character set 0x7A (row number 90, traffic symbols)

Characters 90-45 through 90-63 and 90-66 through 90-84 (shown below shaded) are listed in the B24 standard only in table 7-10 (the list of extension characters), and are also the only characters in rows 90 through 91 which are not transport-related symbols; this is noted in the B24 standard in an endnote to table 7-10. The remainder of the extensions are listed in both table 7-4 (the double-byte code chart) and table 7-10.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x7A)

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

2x

⛌

26CC

⛍

26CD

❗

︎

2757

⛏

26CF

⛐

26D0

⛑

26D1

⛒

26D2

⛕

26D5

⛓

26D3

⛔

︎

26D4

3x

🅿

1F17F

🆊

1F18A

⛖

26D6

⛗

26D7

⛘

26D8

⛙

26D9

⛚

26DA

⛛

26DB

⛜

26DC

⛝

26DD

⛞

26DE

⛟

26DF

⛠

26E0

⛡

26E1

4x

⭕

︎

2B55

㉈

3248

㉉

3249

㉊

324A

㉋

324B

㉌

324C

㉍

324D

㉎

324E

㉏

324F

⒑

2491

⒒

2492

⒓

2493

5x

🅊

1F14A

🅌

1F14C

🄿

1F13F

🅆

1F146

🅋

1F14B

🈐

1F210

🈑

1F211

🈒

1F212

🈓

1F213

🅂

1F142

🈔

1F214

🈕

1F215

🈖

1F216

🅍

1F14D

🄱

1F131

🄽

1F13D

6x

⬛

︎

2B1B

⬤

2B24

🈗

1F217

🈘

1F218

🈙

1F219

🈚

︎

1F21A

🈛

1F21B

⚿

26BF

🈜

1F21C

🈝

1F21D

🈞

1F21E

🈟

1F21F

🈠

1F220

🈡

1F221

🈢

1F222

🈣

1F223

7x

🈤

1F224

🈥

1F225

🅎

1F14E

㊙

3299

🈀

1F200

Additions from table 7-10 not in table 7-4.

#### Character set 0x7B (row number 91, map symbols)

Characters from ARIB STD-B24 which were not retained in ARIB STD-B62 are shown shaded.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x7B)

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

2x

⛣

26E3

⭖

2B56

⭗

2B57

⭘

2B58

⭙

2B59

☓

2613

㊋

328B

〒

3012

⛨

26E8

㉆

3246

㉅

3245

⛩

26E9

࿖

0FD6

⛪

︎

26EA

⛫

26EB

3x

⛬

26EC

♨

2668

⛭

26ED

⛮

26EE

⛯

26EF

⚓

︎

2693

✈

2708

⛰

26F0

⛱

26F1

⛲

︎

26F2

⛳

︎

26F3

⛴

26F4

⛵

︎

26F5

🅗

1F157

Ⓓ

24B9

Ⓢ

24C8

4x

⛶

26F6

🅟

1F15F

🆋

1F18B

🆍

1F18D

🆌

1F18C

🅹

1F179

⛷

26F7

⛸

26F8

⛹

26F9

⛺

︎

26FA

🅻

1F17B

☎

260E

⛻

26FB

⛼

26FC

⛽

︎

26FD

⛾

26FE

5x

🅼

1F17C

⛿

26FF

6x

7x

Not in ARIB STD-B62

#### Character set 0x7C (row number 92, units, enclosed forms, list markers, arrows)

Characters from ARIB STD-B24 which were not retained in ARIB STD-B62 are shown shaded.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x7C)

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

2x

➡

27A1

⬅

2B05

⬆

2B06

⬇

2B07

⬯

2B2F

⬮

2B2E

年

5E74

月

6708

日

65E5

円

5186

㎡

33A1

㎥

33A5

㎝

339D

㎠

33A0

㎤

33A4

3x

🄀

1F100

⒈

2488

⒉

2489

⒊

248A

⒋

248B

⒌

248C

⒍

248D

⒎

248E

⒏

248F

⒐

2490

氏

副

元

故

前

新

4x

🄁

1F101

🄂

1F102

🄃

1F103

🄄

1F104

🄅

1F105

🄆

1F106

🄇

1F107

🄈

1F108

🄉

1F109

🄊

1F10A

㈳

3233

㈶

3236

㈲

3232

㈱

3231

㈹

3239

㉄

3244

5x

▶

25B6

◀

25C0

〖

3016

〗

3017

⟐

27D0

²

00B2

³

00B3

🄭

1F12D

(vn)

(ob)

(cb)

(ce

mb)

(hp)

(br)

(p)

6x

(s)

(ms)

(t)

(bs)

(b)

(tb)

(tp)

(ds)

(ag)

(eg)

(vo)

(fl)

(ke

y)

(sa

x)

7x

(sy

n)

(or

g)

(pe

r)

🄬

1F12C

🄫

1F12B

㉇

3247

🆐

1F190

🈦

1F226

℻

213B

Not in ARIB STD-B62

#### Character set 0x7D (row number 93, game and weather symbols, fractions, units, enclosed forms)

Characters from ARIB STD-B24 which were not retained in ARIB STD-B62 are shown shaded.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x7D)

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

2x

㈪

322A

㈫

322B

㈬

322C

㈭

322D

㈮

322E

㈯

322F

㈰

3230

㈷

3237

㍾

337E

㍽

337D

㍼

337C

㍻

337B

№

2116

℡

2121

〶

3036

3x

⚾

︎

26BE

🉀

1F240

🉁

1F241

🉂

1F242

🉃

1F243

🉄

1F244

🉅

1F245

🉆

1F246

🉇

1F247

🉈

1F248

🄪

1F12A

🈧

1F227

🈨

1F228

🈩

1F229

🈔

1F214

🈪

1F22A

4x

🈫

1F22B

🈬

1F22C

🈭

1F22D

🈮

1F22E

🈯

︎

1F22F

🈰

1F230

🈱

1F231

ℓ

2113

㎏

338F

㎐

3390

㏊

33CA

㎞

339E

㎢

33A2

㍱

3371

5x

½

00BD

↉

2189

⅓

2153

⅔

2154

¼

00BC

¾

00BE

⅕

2155

⅖

2156

⅗

2157

⅘

2158

⅙

2159

⅚

215A

⅐

2150

⅛

215B

⅑

2151

⅒

2152

6x

☀

2600

☁

2601

☂

2602

⛄

︎

26C4

☖

2616

☗

2617

⛉

26C9

⛊

26CA

♦

2666

♥

2665

♣

2663

♠

2660

⛋

26CB

⨀

2A00

‼

203C

⁉

2049

7x

⛅

︎

26C5

☔

︎

2614

⛆

26C6

☃

2603

⛇

26C7

⚡

︎

26A1

⛈

26C8

⚞

269E

⚟

269F

♬

266C

☎

260E

Not in ARIB STD-B62

#### Character set 0x7E (row number 94, list markers)

Characters from ARIB STD-B24 which were not retained in ARIB STD-B62 are shown shaded.

ARIB STD-B24 Kanji (double-byte) set (prefixed with 0x7E)

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

2x

Ⅰ

2160

Ⅱ

2161

Ⅲ

2162

Ⅳ

2163

Ⅴ

2164

Ⅵ

2165

Ⅶ

2166

Ⅷ

2167

Ⅸ

2168

Ⅹ

2169

Ⅺ

216A

Ⅻ

216B

⑰

2470

⑱

2471

⑲

2472

3x

⑳

2473

⑴

2474

⑵

2475

⑶

2476

⑷

2477

⑸

2478

⑹

2479

⑺

247A

⑻

247B

⑼

247C

⑽

247D

⑾

247E

⑿

247F

㉑

3251

㉒

3252

㉓

3253

4x

㉔

3254

🄐

1F110

🄑

1F111

🄒

1F112

🄓

1F113

🄔

1F114

🄕

1F115

🄖

1F116

🄗

1F117

🄘

1F118

🄙

1F119

🄚

1F11A

🄛

1F11B

🄜

1F11C

🄝

1F11D

🄞

1F11E

5x

🄟

1F11F

🄠

1F120

🄡

1F121

🄢

1F122

🄣

1F123

🄤

1F124

🄥

1F125

🄦

1F126

🄧

1F127

🄨

1F128

🄩

1F129

㉕

3255

㉖

3256

㉗

3257

㉘

3258

㉙

3259

6x

㉚

325A

①

2460

②

2461

③

2462

④

2463

⑤

2464

⑥

2465

⑦

2466

⑧

2467

⑨

2468

⑩

2469

⑪

246A

⑫

246B

⑬

246C

⑭

246D

⑮

246E

7x

⑯

246F

❶

2776

❷

2777

❸

2778

❹

2779

❺

277A

❻

277B

❼

277C

❽

277D

❾

277E

❿

277F

⓫

24EB

⓬

24EC

㉛

325B

Not in ARIB STD-B62

### Single-byte sets

#### Alphanumeric set

ARIB STD-B24 Alphanumeric set

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

2x

!

0021

"

0022

#

0023

$

0024

%

0025

&

0026

'

0027

(

0028

)

0029

*

002A

+

002B

,

002C

-

002D

.

002E

/

002F

3x

0

0030

1

0031

2

0032

3

0033

4

0034

5

0035

6

0036

7

0037

8

0038

9

0039

:

003A

;

003B

<

003C

=

003D

>

003E

?

003F

4x

@

0040

A

0041

B

0042

C

0043

D

0044

E

0045

F

0046

G

0047

H

0048

I

0049

J

004A

K

004B

L

004C

M

004D

N

004E

O

004F

5x

P

0050

Q

0051

R

0052

S

0053

T

0054

U

0055

V

0056

W

0057

X

0058

Y

0059

Z

005A

[

005B

¥

00A5

]

005D

^

005E

_

005F

6x

`

0060

a

0061

b

0062

c

0063

d

0064

e

0065

f

0066

g

0067

h

0068

i

0069

j

006A

k

006B

l

006C

m

006D

n

006E

o

006F

7x

p

0070

q

0071

r

0072

s

0073

t

0074

u

0075

v

0076

w

0077

x

0078

y

0079

z

007A

{

007B

|

007C

}

007D

‾

203E

Differences from

US-ASCII

#### Hiragana set

ARIB STD-B24 Hiragana set

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

2x

ぁ

3041

あ

3042

ぃ

3043

い

3044

ぅ

3045

う

3046

ぇ

3047

え

3048

ぉ

3049

お

304A

か

304B

が

304C

き

304D

ぎ

304E

く

304F

3x

ぐ

3050

け

3051

げ

3052

こ

3053

ご

3054

さ

3055

ざ

3056

し

3057

じ

3058

す

3059

ず

305A

せ

305B

ぜ

305C

そ

305D

ぞ

305E

た

305F

4x

だ

3060

ち

3061

ぢ

3062

っ

3063

つ

3064

づ

3065

て

3066

で

3067

と

3068

ど

3069

な

306A

に

306B

ぬ

306C

ね

306D

の

306E

は

306F

5x

ば

3070

ぱ

3071

ひ

3072

び

3073

ぴ

3074

ふ

3075

ぶ

3076

ぷ

3077

へ

3078

べ

3079

ぺ

307A

ほ

307B

ぼ

307C

ぽ

307D

ま

307E

み

307F

6x

む

3080

め

3081

も

3082

ゃ

3083

や

3084

ゅ

3085

ゆ

3086

ょ

3087

よ

3088

ら

3089

り

308A

る

308B

れ

308C

ろ

308D

ゎ

308E

わ

308F

7x

ゐ

3090

ゑ

3091

を

3092

ん

3093

ゝ

309D

ゞ

309E

ー

30FC

。

3002

「

300C

」

300D

、

3001

・

30FB

Character allocations not following row 4 of JIS X 0208

#### Katakana set

ARIB STD-B24 Katakana set

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

2x

ァ

30A1

ア

30A2

ィ

30A3

イ

30A4

ゥ

30A5

ウ

30A6

ェ

30A7

エ

30A8

ォ

30A9

オ

30AA

カ

30AB

ガ

30AC

キ

30AD

ギ

30AE

ク

30AF

3x

グ

30B0

ケ

30B1

ゲ

30B2

コ

30B3

ゴ

30B4

サ

30B5

ザ

30B6

シ

30B7

ジ

30B8

ス

30B9

ズ

30BA

セ

30BB

ゼ

30BC

ソ

30BD

ゾ

30BE

タ

30BF

4x

ダ

30C0

チ

30C1

ヂ

30C2

ッ

30C3

ツ

30C4

ヅ

30C5

テ

30C6

デ

30C7

ト

30C8

ド

30C9

ナ

30CA

ニ

30CB

ヌ

30CC

ネ

30CD

ノ

30CE

ハ

30CF

5x

バ

30D0

パ

30D1

ヒ

30D2

ビ

30D3

ピ

30D4

フ

30D5

ブ

30D6

プ

30D7

ヘ

30D8

ベ

30D9

ペ

30DA

ホ

30DB

ボ

30DC

ポ

30DD

マ

30DE

ミ

30DF

6x

ム

30E0

メ

30E1

モ

30E2

ャ

30E3

ヤ

30E4

ュ

30E5

ユ

30E6

ョ

30E7

ヨ

30E8

ラ

30E9

リ

30EA

ル

30EB

レ

30EC

ロ

30ED

ヮ

30EE

ワ

30EF

7x

ヰ

30F0

ヱ

30F1

ヲ

30F2

ン

30F3

ヴ

30F4

ヵ

30F5

ヶ

30F6

ヽ

30FD

ヾ

30FE

ー

30FC

。

3002

「

300C

」

300D

、

3001

・

30FB

Character allocations not following row 5 of JIS X 0208

#### JIS X 0201 Katakana set

ARIB STD-B24 JIS X 0201 Katakana set

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

2x

｡

FF61

｢

FF62

｣

FF63

､

FF64

･

FF65

ｦ

FF66

ｧ

FF67

ｨ

FF68

ｩ

FF69

ｪ

FF6A

ｫ

FF6B

ｬ

FF6C

ｭ

FF6D

ｮ

FF6E

ｯ

FF6F

3x

ｰ

FF70

ｱ

FF71

ｲ

FF72

ｳ

FF73

ｴ

FF74

ｵ

FF75

ｶ

FF76

ｷ

FF77

ｸ

FF78

ｹ

FF79

ｺ

FF7A

ｻ

FF7B

ｼ

FF7C

ｽ

FF7D

ｾ

FF7E

ｿ

FF7F

4x

ﾀ

FF80

ﾁ

FF81

ﾂ

FF82

ﾃ

FF83

ﾄ

FF84

ﾅ

FF85

ﾆ

FF86

ﾇ

FF87

ﾈ

FF88

ﾉ

FF89

ﾊ

FF8A

ﾋ

FF8B

ﾌ

FF8C

ﾍ

FF8D

ﾎ

FF8E

ﾏ

FF8F

5x

ﾐ

FF90

ﾑ

FF91

ﾒ

FF92

ﾓ

FF93

ﾔ

FF94

ﾕ

FF95

ﾖ

FF96

ﾗ

FF97

ﾘ

FF98

ﾙ

FF99

ﾚ

FF9A

ﾛ

FF9B

ﾜ

FF9C

ﾝ

FF9D

ﾞ

FF9E

ﾟ

FF9F

6x

7x

#### Mosaic sets

ARIB STD-B24 Mosaic Set A

(ISO-IR-71)

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

2x

🬀

1FB00

🬁

1FB01

🬂

1FB02

🬃

1FB03

🬄

1FB04

🬅

1FB05

🬆

1FB06

🬇

1FB07

🬈

1FB08

🬉

1FB09

🬊

1FB0A

🬋

1FB0B

🬌

1FB0C

🬍

1FB0D

🬎

1FB0E

3x

🬏

1FB0F

🬐

1FB10

🬑

1FB11

🬒

1FB12

🬓

1FB13

▌

258C

🬔

1FB14

🬕

1FB15

🬖

1FB16

🬗

1FB17

🬘

1FB18

🬙

1FB19

🬚

1FB1A

🬛

1FB1B

🬜

1FB1C

🬝

1FB1D

4x

🬼

1FB3C

🬽

1FB3D

🬾

1FB3E

🬿

1FB3F

🭀

1FB40

◣

25E3

🭁

1FB41

🭂

1FB42

🭃

1FB43

🭄

1FB44

🭅

1FB45

🭆

1FB46

🭨

1FB68

🭩

1FB69

🭰

1FB70

🮕

1FB95

5x

🭇

1FB47

🭈

1FB48

🭉

1FB49

🭊

1FB4A

🭋

1FB4B

◢

25E2

🭌

1FB4C

🭍

1FB4D

🭎

1FB4E

🭏

1FB4F

🭐

1FB50

🭑

1FB51

🭪

1FB6A

🭫

1FB6B

🭵

1FB75

█

2588

6x

🬞

1FB1E

🬟

1FB1F

🬠

1FB20

🬡

1FB21

🬢

1FB22

🬣

1FB23

🬤

1FB24

🬥

1FB25

🬦

1FB26

🬧

1FB27

▐

2590

🬨

1FB28

🬩

1FB29

🬪

1FB2A

🬫

1FB2B

🬬

1FB2C

7x

🬭

1FB2D

🬮

1FB2E

🬯

1FB2F

🬰

1FB30

🬱

1FB31

🬲

1FB32

🬳

1FB33

🬴

1FB34

🬵

1FB35

🬶

1FB36

🬷

1FB37

🬸

1FB38

🬹

1FB39

🬺

1FB3A

🬻

1FB3B

ARIB STD-B24 Mosaic Set B

(ISO-IR-137)

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

2x

▖

2596

▪

25AA

𜹇

1CE47

▟

259F

�

�

▶

25B6

�

🠷

1F837

�

�

🮛

1FB9B

🯣

1FBE3

🯫

1FBEB

�

3x

▄

2584

▗

2597

▬

25AC

𜹐

1CE50

▙

2599

�

�

◀

25C0

�

🠵

1F835

�

�

🮚

1FB9A

🯡

1FBE1

🯩

1FBE9

�

4x

5x

6x

🭒

1FB52

🭓

1FB53

🭔

1FB54

🭕

1FB55

🭖

1FB56

◥

25E5

🭗

1FB57

🭘

1FB58

🭙

1FB59

🭚

1FB5A

🭛

1FB5B

🭜

1FB5C

🭬

1FB6C

🭭

1FB6D

7x

🭝

1FB5D

🭞

1FB5E

🭟

1FB5F

🭠

1FB60

🭡

1FB61

◤

25E4

🭢

1FB62

🭣

1FB63

🭤

1FB64

🭥

1FB65

🭦

1FB66

🭧

1FB67

🭮

1FB6E

🭯

1FB6F

� Not in Unicode

ARIB STD-B24 Mosaic Set C

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

2x

𜹑

1CE51

𜹒

1CE52

𜹓

1CE53

𜹔

1CE54

𜹕

1CE55

𜹖

1CE56

𜹗

1CE57

𜹘

1CE58

𜹙

1CE59

𜹚

1CE5A

𜹛

1CE5B

𜹜

1CE5C

𜹝

1CE5D

𜹞

1CE5E

𜹟

1CE5F

3x

𜹠

1CE60

𜹡

1CE61

𜹢

1CE62

𜹣

1CE63

𜹤

1CE64

𜹥

1CE65

𜹦

1CE66

𜹧

1CE67

𜹨

1CE68

𜹩

1CE69

𜹪

1CE6A

𜹫

1CE6B

𜹬

1CE6C

𜹭

1CE6D

𜹮

1CE6E

𜹯

1CE6F

4x

5x

𜺏

1CE8F

6x

𜹰

1CE70

𜹱

1CE71

𜹲

1CE72

𜹳

1CE73

𜹴

1CE74

𜹵

1CE75

𜹶

1CE76

𜹷

1CE77

𜹸

1CE78

𜹹

1CE79

𜹺

1CE7A

𜹻

1CE7B

𜹼

1CE7C

𜹽

1CE7D

𜹾

1CE7E

𜹿

1CE7F

7x

𜺀

1CE80

𜺁

1CE81

𜺂

1CE82

𜺃

1CE83

𜺄

1CE84

𜺅

1CE85

𜺆

1CE86

𜺇

1CE87

𜺈

1CE88

𜺉

1CE89

𜺊

1CE8A

𜺋

1CE8B

𜺌

1CE8C

𜺍

1CE8D

𜺎

1CE8E

Most of ARIB STD-B24 Mosaic Set D does not exist in Unicode.

## Shift_JIS variant

In addition to the modified ISO 2022 encoding, the B24 standard also specifies a Shift JIS encoding following JIS X 0208:1997, but with the addition of the extended characters in the kanji set.

| First byte 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 ␀ ␁ ␂ ␃ ␄ ␅ ␆ ␇ ␈ ␉ ␊ ␋ ␌ ␍ ␎ ␏ 1 ␐ ␑ ␒ ␓ ␔ ␕ ␖ ␗ ␘ ␙ ␚ ␛ ␜ ␝ ␞ ␟ 2 ␠ ! " # $ % & ' ( ) * + , - . / 3 0 1 2 3 4 5 6 7 8 9 : ; < = > ? 4 @ A B C D E F G H I J K L M N O 5 P Q R S T U V W X Y Z [ ¥ ] ^ _ 6 ` a b c d e f g h i j k l m n o 7 p q r s t u v w x y z { \| } ‾ ␡ 8 9 A ｡ ｢ ｣ ､ ･ ｦ ｧ ｨ ｩ ｪ ｫ ｬ ｭ ｮ ｯ B ｰ ｱ ｲ ｳ ｴ ｵ ｶ ｷ ｸ ｹ ｺ ｻ ｼ ｽ ｾ ｿ C ﾀ ﾁ ﾂ ﾃ ﾄ ﾅ ﾆ ﾇ ﾈ ﾉ ﾊ ﾋ ﾌ ﾍ ﾎ ﾏ D ﾐ ﾑ ﾒ ﾓ ﾔ ﾕ ﾖ ﾗ ﾘ ﾙ ﾚ ﾛ ﾜ ﾝ ﾞ ﾟ E F | Second byte 0 1 2 3 4 5 6 7 8 9 A B C D E F 0 1 2 3 4 5 6 7 8 9 A B C D E F |
|---|---|
|   |   |
| Non printable ASCII character Unaltered ASCII character Modified ASCII character Single-byte half-width katakana First byte of a double-byte character, used by JIS X 0208 First byte of an ARIB extended character Not used as first byte, unallocated space in JIS X 0208 Not used as first byte Second byte of a double-byte character whose first half of the JIS sequence was odd Second byte of a double-byte character whose first half of the JIS sequence was even Unused as second byte of a double-byte character |   |
