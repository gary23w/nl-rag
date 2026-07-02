---
title: "ANSI escape code"
source: https://en.wikipedia.org/wiki/ANSI_escape_code
domain: chalk-terminal
license: CC-BY-SA-4.0
tags: chalk terminal, terminal string styling, ansi color output, cli text color
fetched: 2026-07-02
---

# ANSI escape code

**ANSI escape sequences** are a standard for in-band signaling to control cursor location, color, font styling, and other options on video text terminals and terminal emulators. Certain sequences of bytes, most starting with an ASCII escape character and a bracket character, are embedded into text. The terminal interprets these sequences as commands, rather than text to display verbatim. ANSI codes can change the color of text and move the cursor so text can be drawn anywhere on the screen.

ANSI sequences were introduced in the 1970s to replace vendor-specific sequences and became widespread in the computer equipment market by the early 1980s. Although hardware text terminals have become increasingly rare in the 21st century, the relevance of the ANSI standard persists because a great majority of terminal emulators and command consoles interpret at least a portion of the ANSI standard.

*ANSI* stands for "American National Standards Institute".

## History

Almost all manufacturers of video terminals added vendor-specific escape sequences to perform operations such as placing the cursor at arbitrary positions on the screen. One example is the VT52 terminal, which allowed the cursor to be placed at an x,y location on the screen by sending the `ESC` character, a `Y` character, and then two characters representing numerical values equal to the x,y location plus 32 (thus starting at the ASCII space character and avoiding the control characters). The Hazeltine 1500 had a similar feature, invoked using `~`, `DC1` and then the X and Y positions separated with a comma. While the two terminals had identical functionality in this regard, different control sequences had to be used to invoke them.

As these sequences were different for different terminals, elaborate libraries such as termcap ("terminal capabilities") and utilities such as tput had to be created so programs could use the same API to work with any terminal. In addition, many of these terminals required sending numbers (such as row and column) as the binary values of the characters; for some programming languages, and for systems that did not use ASCII internally, it was often difficult to turn a number into the correct character.

The ANSI standard attempted to address these problems by making a command set that all terminals would use and requiring all numeric information to be transmitted as ASCII numbers. The first standard in the series was **ECMA-48**, adopted in 1976. It was a continuation of a series of character coding standards, the first one being ECMA-6 from 1965, a 7-bit standard from which ISO 646 originates. The name "ANSI escape sequence" dates from 1979 when ANSI adopted ANSI X3.64. The ANSI X3L2 committee collaborated with the ECMA committee TC 1 to produce nearly identical standards. These two standards were merged into an international standard, ISO 6429. In 1994, ANSI withdrew its standard in favor of the international standard.

The first popular video terminal to support these sequences was the Digital VT100, introduced in 1978. This model was very successful in the market, which sparked a variety of VT100 clones, among the earliest and most popular of which was the much more affordable Zenith Z-19 in 1979. Others included the Qume QVT-108, Televideo TVI-970, Wyse WY-99GT as well as optional "VT100" or "VT103" or "ANSI" modes with varying degrees of compatibility on many other brands. The popularity of these gradually led to more and more software (especially bulletin board systems and other online services) assuming the escape sequences worked, leading to almost all new terminals and emulator programs supporting them.

In 1981, ANSI X3.64 was adopted for use in the US government by FIPS publication 86. Later, the US government stopped duplicating industry standards, so FIPS pub. 86 was withdrawn.

ECMA-48 has been updated several times and is currently at its 5th edition, from 1991. It is also adopted by ISO and IEC as standard **ISO/IEC 6429**. A version is adopted as a Japanese Industrial Standard, as JIS X 0211.

Related standards include ITU T.61, the Teletex standard, and the **ISO/IEC 8613**, the Open Document Architecture standard (mainly ISO/IEC 8613-6 or ITU T.416). The two systems share many escape codes with the ANSI system, with extensions that are not necessarily meaningful to computer terminals. Both systems quickly fell into disuse, but ECMA-48 does mark the extensions used in them as reserved.

## Platform support

In the early 1980s, large amounts of software directly used these sequences to update screen displays. This included everything on VMS (which assumed DEC terminals), most software designed to be portable on CP/M home computers, and significant amounts of Unix software, as it was easier to use than the termcap libraries.

Terminal emulators for communicating with remote machines almost always implement ANSI escape codes. This includes anything written to communicate with bulletin-board systems on home and personal computers. On Unix terminal emulators such as xterm also can communicate with software running on the same machine, and thus software running in X11 under a terminal emulator could assume the ability to write these sequences.

As computers got more powerful even built-in displays started supporting them, allowing software to be portable between CP/M systems. There were attempts to extend the escape sequences to support printers and as an early PDF-like document storage format, the Open Document Architecture.

The IBM PC, introduced in 1981, did not support these or any other escape sequences for updating the screen. Only a few control characters (BEL, CR, LF, BS) were interpreted by the underlying BIOS. Any display effects had to be done with BIOS calls, which were notoriously slow, or by directly manipulating the IBM PC hardware. This made any interesting software non-portable and led to the need to duplicate details of the display hardware in PC Clones.

DOS version 2.0 included an optional device driver named ANSI.SYS. Poor performance, and the fact that it was not installed by default, meant software rarely (if ever) took advantage of it.

The Windows Console did not support ANSI escape sequences, nor did Microsoft provide any method to enable them. Some replacements such as JP Software's TCC (formerly 4NT), Michael J. Mefford's ANSI.COM, Jason Hood's ANSICON and Maximus5's ConEmu enabled ANSI escape sequences. Software such as the Python colorama package or Cygwin modified text in-process as it was sent to the console, extracting the ANSI Escape sequences and emulating them with Windows calls. In 2016, Microsoft released the Windows 10 version 1511 update which unexpectedly implemented support for ANSI escape sequences, over three decades after the debut of Windows. This was done alongside Windows Subsystem for Linux, apparently to allow Unix-like terminal-based software to use the Windows Console. Windows PowerShell 5.1 enabled this by default, and PowerShell 6 made it possible to embed the necessary ESC character into a string with `e. Windows Terminal, introduced in 2019, supports the sequences by default. Since Windows 11 22H2 and Windows Terminal 1.15, Windows Terminal replaces Windows Console as the default.

## C0 control codes

Almost all users assume some functions of some single-byte characters. Initially defined as part of ASCII, the default C0 control code set is now defined in ISO 6429 (ECMA-48), making it part of the same standard as the C1 set invoked by the ANSI escape sequences (although ISO 2022 allows the ISO 6429 C0 set to be used without the ISO 6429 C1 set, and *vice versa*, provided that 0x1B is always ESC). This is used to shorten the amount of data transmitted, or to perform some functions that are unavailable from escape sequences:

| ^ | C0 | Abbr | C escape sequence | Name | Effect |
|---|---|---|---|---|---|
| ^G | 0x07 | BEL | `\a` | Bell | Makes an audible noise. |
| ^H | 0x08 | BS | `\b` | Backspace | Moves the cursor left (but may "backwards wrap" if cursor is at start of line). |
| ^I | 0x09 | HT | `\t` | Tab | Moves the cursor right to next tab stop. |
| ^J | 0x0A | LF | `\n` | Line Feed | Moves to next line, scrolls the display up if at bottom of the screen. Usually does not move horizontally, though programs should not rely on this. |
| ^L | 0x0C | FF | `\f` | Form Feed | Move a printer to top of next page. Usually does not move horizontally, though programs should not rely on this. Effect on video terminals varies. |
| ^M | 0x0D | CR | `\r` | Carriage Return | Moves the cursor to column zero. |
| ^[ | 0x1B | ESC | `\x1B`, `\033` | Escape | Starts all the escape sequences |

Escape sequences vary in length. The general format for an ANSI-compliant escape sequence is defined by ANSI X3.41 (equivalent to ECMA-35 or ISO/IEC 2022). The escape sequences consist only of bytes in the range 0x20—0x7F (all the non-control ASCII characters), and can be parsed without looking ahead. The behavior when a control character, a byte with the high bit set, or a byte that is not part of any valid sequence is encountered before the end is undefined.

## Fe Escape sequences

If the `ESC` is followed by a byte in the range 0x40 to 0x5F, the escape sequence is of type `Fe`. Its interpretation is delegated to the applicable C1 control code standard. Accordingly, all escape sequences corresponding to C1 control codes from ANSI X3.64 / ECMA-48 follow this format.

The standard says that, in 8-bit environments, the control functions corresponding to type `Fe` escape sequences (those from the set of C1 control codes) can be represented as single bytes in the 0x80–0x9F range. This is possible in character encodings conforming to the provisions for an 8-bit code made in ISO 2022, such as the ISO 8859 series. However, in character encodings used on modern devices such as UTF-8 or CP-1252, those codes are often used for other purposes, so only the 2-byte sequence is typically used. In the case of UTF-8, representing a C1 control code via the C1 Controls and Latin-1 Supplement block results in a different two-byte code (e.g. 0xC2,0x8E for U+008E), but no space is saved this way.

| Code | C1 | Abbr | Name | Effect |
|---|---|---|---|---|
| ESC N | 0x8E | SS2 | Single Shift Two | Select a single character from one of the alternative character sets. SS2 selects the G2 character set, and SS3 selects the G3 character set. In a 7-bit environment, this is followed by one or more GL bytes (0x20–0x7F) specifying a character from that set. In an 8-bit environment, these may instead be GR bytes (0xA0–0xFF). |
| ESC O | 0x8F | SS3 | Single Shift Three |   |
| ESC P | 0x90 | DCS | Device Control String | Terminated by ST. Xterm's uses of this sequence include defining User-Defined Keys, and requesting or setting Termcap/Terminfo data. |
| ESC [ | 0x9B | CSI | Control Sequence Introducer | Starts most of the useful sequences, terminated by a byte in the range 0x40 through 0x7E. |
| ESC \ | 0x9C | ST | String Terminator | Terminates strings in other controls. |
| ESC ] | 0x9D | OSC | Operating System Command | Starts a control string for the operating system to use, terminated by ST. |
| ESC X | 0x98 | SOS | Start of String | Takes an argument of a string of text, terminated by ST. The uses for these string control sequences are defined by the application or privacy discipline. These functions are rarely implemented and the arguments are ignored by xterm. Some Kermit clients allow the server to automatically execute Kermit commands on the client by embedding them in APC sequences; this is a potential security risk if the server is untrusted. |
| ESC ^ | 0x9E | PM | Privacy Message |   |
| ESC _ | 0x9F | APC | Application Program Command |   |

## Control Sequence Introducer commands

For Control Sequence Introducer, or CSI, commands, the `ESC [` (written as `\e[`, `\x1b[` or `\033[` in several programming languages) is followed by any number (including none) of "parameter bytes" in the range 0x30–0x3F (ASCII `0–9:;<=>?`), then by any number of "intermediate bytes" in the range 0x20–0x2F (ASCII space and `!"#$%&'()*+,-./`), then finally by a single "final byte" in the range 0x40–0x7E (ASCII @A–Z[\]^_`a–z{|}~).

All common sequences just use the parameters as a series of semicolon-separated numbers such as `1;2;3`. Missing numbers are treated as `0` (`1;;3` acts like the middle number is `0`, and no parameters at all in `ESC[m` acts like a `0` reset code). Some sequences (such as CUU) treat `0` as `1` in order to make missing parameters useful.

A subset of arrangements was declared "private" so that terminal manufacturers could insert their own sequences without conflicting with the standard. Sequences containing the parameter bytes `<=>?` or the final bytes 0x70–0x7E (`p–z{|}~`) are private.

The behavior of the terminal is undefined in the case where a CSI sequence contains any character outside of the range 0x20–0x7E. These illegal characters are either C0 control characters (the range 0–0x1F), DEL (0x7F), or bytes with the high bit set. Possible responses are to ignore the byte, to process it immediately, and furthermore whether to continue with the CSI sequence, to abort it immediately, or to ignore the rest of it.

| Code | Abbr | Name | Effect |
|---|---|---|---|
| CSI *n* A | CUU | Cursor Up | Moves the cursor *n* (default `1`) cells in the given direction. If the cursor is already at the edge of the screen, this has no effect. |
| CSI *n* B | CUD | Cursor Down |   |
| CSI *n* C | CUF | Cursor Forward |   |
| CSI *n* D | CUB | Cursor Back |   |
| CSI *n* E | CNL | Cursor Next Line | Moves cursor to beginning of the line *n* (default `1`) lines down. (not ANSI.SYS) |
| CSI *n* F | CPL | Cursor Previous Line | Moves cursor to beginning of the line *n* (default `1`) lines up. (not ANSI.SYS) |
| CSI *n* G | CHA | Cursor Horizontal Absolute | Moves the cursor to column *n* (default `1`). (not ANSI.SYS) |
| CSI *n* ; *m* H | CUP | Cursor Position | Moves the cursor to row *n*, column *m*. The values are 1-based, and default to `1` (top left corner) if omitted. A sequence such as `CSI ;5H` is a synonym for `CSI 1;5H` as well as `CSI 17;H` is the same as `CSI 17H` and `CSI 17;1H` |
| CSI *n* J | ED | Erase in Display | Clears part of the screen. If *n* is `0` (or missing), clear from cursor to end of screen. If *n* is `1`, clear from cursor to beginning of the screen. If *n* is `2`, clear entire screen (and moves cursor to upper left on DOS ANSI.SYS). If *n* is `3`, clear entire screen and delete all lines saved in the scrollback buffer (this feature was added for xterm and is supported by other terminal applications). |
| CSI *n* K | EL | Erase in Line | Erases part of the line. If *n* is `0` (or missing), clear from cursor to the end of the line. If *n* is `1`, clear from cursor to beginning of the line. If *n* is `2`, clear entire line. Cursor position does not change. |
| CSI *n* S | SU | Scroll Up | Scroll whole page up by *n* (default `1`) lines. New lines are added at the bottom. (not ANSI.SYS) |
| CSI *n* T | SD | Scroll Down | Scroll whole page down by *n* (default `1`) lines. New lines are added at the top. (not ANSI.SYS) |
| CSI *n* ; *m* f | HVP | Horizontal Vertical Position | Same as CUP, but counts as a format effector function (like CR or LF) rather than an editor function (like CUD or CNL). This can lead to different handling in certain terminal modes. |
| CSI *n* m | SGR | Select Graphic Rendition | Sets colors and style of the characters following this code |
| CSI 5i |   | AUX Port On | Enable aux serial port usually for local serial printer |
| CSI 4i |   | AUX Port Off | Disable aux serial port usually for local serial printer |
| CSI 6n | DSR | Device Status Report | Reports the cursor position (CPR) by transmitting `ESC[n;mR`, where *n* is the row and *m* is the column. |

| Code | Abbr | Name | Effect |
|---|---|---|---|
| CSI s | SCP, SCOSC | Save Current Cursor Position | Saves the cursor position/state in SCO console mode. In vertical split screen mode, instead used to set (as `CSI *n* ; *n* s`) or reset left and right margins. |
| CSI u | RCP, SCORC | Restore Saved Cursor Position | Restores the cursor position/state in SCO console mode. |
| CSI ? 25 h | DECTCEM |   | Shows the cursor, from the VT220. |
| CSI ? 25 l | DECTCEM |   | Hides the cursor. |
| CSI ? 1004 h |   |   | Enable reporting focus. Reports whenever terminal emulator enters or exits focus as `ESC [I` and `ESC [O`, respectively. |
| CSI ? 1004 l |   |   | Disable reporting focus. |
| CSI ? 1049 h |   |   | Enable alternative screen buffer, from xterm |
| CSI ? 1049 l |   |   | Disable alternative screen buffer, from xterm |
| CSI ? 2004 h |   |   | Turn on bracketed paste mode. In bracketed paste mode, text pasted into the terminal will be surrounded by `ESC [200~` and `ESC [201~`; programs running in the terminal should not treat characters bracketed by those sequences as commands (Vim, for example, does not treat them as commands). From xterm |
| CSI ? 2004 l |   |   | Turn off bracketed paste mode. |

## Select Graphic Rendition parameters

The control sequence `CSI *n* m`, named Select Graphic Rendition (SGR), sets display attributes. Several attributes can be set in the same sequence, separated by semicolons. Each display attribute remains in effect until a following occurrence of SGR resets it. If no codes are given, `CSI m` is treated as `CSI 0 m` (reset / normal).

| *n* | Name | Note |
|---|---|---|
| 0 | Reset *or* normal | All attributes become turned off |
| 1 | Bold or increased intensity | As with faint, the color change is a PC (SCO / CGA) invention. |
| 2 | Faint, decreased intensity, *or* dim | May be implemented as a light font weight like bold. |
| 3 | Italic | Not widely supported. Sometimes treated as inverse or blink. |
| 4 | Underline | Style extensions exist for Kitty, VTE, mintty, iTerm2 and Konsole. |
| 5 | Slow blink | Sets blinking to less than 150 times per minute |
| 6 | Rapid blink | MS-DOS ANSI.SYS, 150+ per minute; not widely supported |
| 7 | Reverse video *or* invert | Swap foreground and background colors. |
| 8 | Conceal *or* hide | Not widely supported. |
| 9 | Crossed-out, *or* strike | Characters legible but marked as if for deletion. Not supported in Terminal.app. |
| 10 | Primary (default) font |   |
| 11–19 | Alternative font | Select alternative font *n* − 10 |
| 20 | Fraktur (Gothic) | Rarely supported |
| 21 | Doubly underlined; or: not bold | Double-underline per ECMA-48, but instead disables bold intensity on several terminals, including in the Linux kernel's console before version 4.17. |
| 22 | Normal intensity | Neither bold nor faint; color changes where intensity is implemented as such. |
| 23 | Neither italic, nor blackletter |   |
| 24 | Not underlined | Neither singly nor doubly underlined |
| 25 | Not blinking | Turn blinking off |
| 26 | Proportional spacing | ITU T.61 and T.416, not known to be used on terminals |
| 27 | Not reversed |   |
| 28 | Reveal | Not concealed |
| 29 | Not crossed out |   |
| 30–37 | Set foreground color |   |
| 38 | Set foreground color | Next arguments are `5;n` or `2;r;g;b` |
| 39 | Default foreground color | Implementation defined (according to standard) |
| 40–47 | Set background color |   |
| 48 | Set background color | Next arguments are `5;n` or `2;r;g;b` |
| 49 | Default background color | Implementation defined (according to standard) |
| 50 | Disable proportional spacing | T.61 and T.416 |
| 51 | Framed | Implemented as "emoji variation selector" in mintty. |
| 52 | Encircled |   |
| 53 | Overlined | Not supported in Terminal.app |
| 54 | Neither framed nor encircled |   |
| 55 | Not overlined |   |
| 58 | Set underline color | Not in standard; implemented in Kitty, VTE, mintty, and iTerm2. Next arguments are `5;n` or `2;r;g;b`. |
| 59 | Default underline color | Not in standard; implemented in Kitty, VTE, mintty, and iTerm2. |
| 60 | Ideogram underline or right side line | Rarely supported |
| 61 | Ideogram double underline, *or* double line on the right side |   |
| 62 | Ideogram overline or left side line |   |
| 63 | Ideogram double overline, *or* double line on the left side |   |
| 64 | Ideogram stress marking |   |
| 65 | No ideogram attributes | Reset the effects of all of `60`–`64` |
| 73 | Superscript | Implemented only in mintty |
| 74 | Subscript |   |
| 75 | Neither superscript nor subscript |   |
| 90–97 | Set bright foreground color | Not in standard; originally implemented by aixterm |
| 100–107 | Set bright background color |   |

### Colors

#### 3-bit and 4-bit

The original specification only had 8 colors, and just gave them names. The SGR parameters 30–37 selected the foreground color, while 40–47 selected the background. Quite a few terminals implemented "bold" (SGR code 1) as a brighter color rather than a different font, thus providing 8 additional foreground colors. Usually you could not get these as background colors, though sometimes inverse video (SGR code 7) would allow that. Examples: to get black letters on white background use `ESC[30;47m`, to get red use `ESC[31m`, to get bright red use `ESC[1;31m`. To reset colors to their defaults, use `ESC[39;49m` (not supported on some terminals), or reset all attributes with `ESC[0m`. Later terminals added the ability to directly specify the "bright" colors with 90–97 and 100–107.

The chart below shows a few examples of how classical standards and modern terminal emulators translate the 4-bit color codes into 24-bit color codes.

FG

BG

Name

CGA/EGA/VGA

Windows Console

Windows

PowerShell&

1.0–6.0

Visual Studio Code

Windows 10

Console

Terminal.app

PuTTY

mIRC

xterm

Ubuntu

Eclipse Terminal

30

40

Black

0, 0, 0

12, 12, 12

0, 0, 0

1, 1, 1

0, 0, 0

31

41

Red

196, 0, 0

128, 0, 0

205, 49, 49

197, 15, 31

153, 0, 0

187, 0, 0

127, 0, 0

205, 0, 0

222, 56, 43

205, 0, 0

32

42

Green

0, 196, 0

0, 128, 0

13, 188, 121

19, 161, 14

0, 166, 0

0, 187, 0

0, 147, 0

0, 205, 0

57, 181, 74

0, 205, 0

33

43

Yellow

196, 126, 0

128, 128, 0

238, 237, 240

229, 229, 16

193, 156, 0

153, 153, 0

187, 187, 0

252, 127, 0

205, 205, 0

255, 199, 6

205, 205, 0

34

44

Blue

0, 0, 196

0, 0, 128

36, 114, 200

0, 55, 218

0, 0, 178

0, 0, 187

0, 0, 127

0, 0, 238

0, 111, 184

0, 0, 238

35

45

Magenta

196, 0, 196

128, 0, 128

1, 36, 86

188, 63, 188

136, 23, 152

178, 0, 178

187, 0, 187

156, 0, 156

205, 0, 205

118, 38, 113

205, 0, 205

36

46

Cyan

0, 196, 196

0, 128, 128

17, 168, 205

58, 150, 221

0, 166, 178

0, 187, 187

0, 147, 147

0, 205, 205

44, 181, 233

0, 205, 205

37

47

White

196, 196, 196

192, 192, 192

229, 229, 229

204, 204, 204

191, 191, 191

187, 187, 187

210, 210, 210

229, 229, 229

204, 204, 204

229, 229, 229

90

100

Bright Black (Gray)

78, 78, 78

128, 128, 128

102, 102, 102

118, 118, 118

102, 102, 102

85, 85, 85

127, 127, 127

127, 127, 127

128, 128, 128

0, 0, 0

91

101

Bright Red

220, 78, 78

255, 0, 0

241, 76, 76

231, 72, 86

230, 0, 0

255, 85, 85

255, 0, 0

92

102

Bright Green

78, 220, 78

0, 255, 0

35, 209, 139

22, 198, 12

0, 217, 0

85, 255, 85

0, 252, 0

0, 255, 0

93

103

Bright Yellow

243, 243, 78

255, 255, 0

245, 245, 67

249, 241, 165

230, 230, 0

255, 255, 85

255, 255, 0

94

104

Bright Blue

78, 78, 220

0, 0, 255

59, 142, 234

59, 120, 255

0, 0, 255

85, 85, 255

0, 0, 252

92, 92, 255

0, 0, 255

92, 92, 255

95

105

Bright Magenta

243, 78, 243

255, 0, 255

214, 112, 214

180, 0, 158

230, 0, 230

255, 85, 255

255, 0, 255

96

106

Bright Cyan

78, 243, 243

0, 255, 255

41, 184, 219

97, 214, 214

0, 230, 230

85, 255, 255

0, 255, 255

97

107

Bright White

255, 255, 255

229, 229, 229

242, 242, 242

230, 230, 230

255, 255, 255

#### 8-bit

As 256-color lookup tables became common on graphic cards, escape sequences were added to select from a pre-defined set of 256 colors:

```
ESC[38;5;⟨n⟩m Select foreground color      where n is a number from the table below
ESC[48;5;⟨n⟩m Select background color
  0-  7:  standard colors (as in ESC [ 30–37 m)
  8- 15:  high intensity colors (as in ESC [ 90–97 m)
 16-231:  6 × 6 × 6 cube (216 colors): 16 + 36 × r + 6 × g + b (0 ≤ r, g, b ≤ 5)
232-255:  grayscale from dark to light in 24 steps
```

The colors displayed by these values vary across terminal/emulator implementations as the recognized ECMA-48 and ITU's T.416 specifications do not define a specific color palette for this lookup table. While it is common to use the above formula for the color palette, in particular the algorithm and choice of colors for the 16-231 cube values differs between implementations. The color palette and algorithm used by XTerm is specified below as a sample.

The ITU's T.416 Information technology - Open Document Architecture (ODA) and interchange format: Character content architectures uses ":" as separator characters instead:

```
ESC[38:5:⟨n⟩m Select foreground color      where n is a number from the table below
ESC[48:5:⟨n⟩m Select background color
```

256-color mode

Foreground: ESC[38;5;#m    —    Background: ESC[48;5;#m

Standard colors

High-intensity colors

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

10

11

12

13

14

15

216 colors

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

213

214

215

216

217

218

219

220

221

222

223

224

225

226

227

228

229

230

231

Grayscale colors

232

233

234

235

236

237

238

239

240

241

242

243

244

245

246

247

248

249

250

251

252

253

254

255

To calculate the RGB values of the colors in the table above, the following Python script can be used:

```mw
# print a list of the 256-color red/green/blue values used by xterm.
#
# reference:
# https://github.com/ThomasDickey/ncurses-snapshots/blob/master/test/xterm-16color.dat
# https://github.com/ThomasDickey/xterm-snapshots/blob/master/XTerm-col.ad
# https://github.com/ThomasDickey/xterm-snapshots/blob/master/256colres.pl

print("colors 0-15 correspond to the ANSI and aixterm naming")
for code in range(0, 16):
    if code > 8:
        level = 255
    elif code == 7:
        level = 229
    else:
        level = 205
    r = 127 if code == 8 else level if (code & 1) != 0 else 92 if code == 12 else 0
    g = 127 if code == 8 else level if (code & 2) != 0 else 92 if code == 12 else 0
    b = 127 if code == 8 else 238 if code == 4 else level if (code & 4) != 0 else 0
    print(f"{code:3d}: {r:02X} {g:02X} {b:02X}")

print("colors 16-231 are a 6x6x6 color cube")
for red in range(0, 6):
    for green in range(0, 6):
        for blue in range(0, 6):
            code = 16 + (red * 36) + (green * 6) + blue
            r = red   * 40 + 55 if red   != 0 else 0
            g = green * 40 + 55 if green != 0 else 0
            b = blue  * 40 + 55 if blue  != 0 else 0
            print(f"{code:3d}: {r:02X} {g:02X} {b:02X}")

print("colors 232-255 are a grayscale ramp, intentionally leaving out black and white")
for gray in range(0, 24):
    level = gray * 10 + 8
    code = 232 + gray
    print(f"{code:3d}: {level:02X} {level:02X} {level:02X}")
```

There has also been a similar but incompatible 88-color encoding using the same escape sequence, seen in `rxvt` and `xterm-88color`. It uses a 4×4×4 color cube.

#### 24-bit

As "true color" graphic cards with 16 to 24 bits of color became common, applications began to support 24-bit colors. Terminal emulators supporting setting 24-bit foreground and background colors with escape sequences include Xterm, KDE's Konsole, and iTerm, as well as all libvte based terminals, including GNOME Terminal.

```
ESC[38;2;⟨r⟩;⟨g⟩;⟨b⟩m Select RGB foreground color
ESC[48;2;⟨r⟩;⟨g⟩;⟨b⟩m Select RGB background color
```

This syntax, initially implemented in XTerm, is based on a reading of the ISO/IEC 8613-6 specification, specifically that SGR 38 / SGR 48 followed by the parameter "2" can specify a "direct color" in RGB space.. As the first widely-used implementation, this specification of RGB values using semicolon separators is widely supported by terminal emulators that include 24-bit color support.

As with the 8-bit color codes, there is a very similar specification of 24-bit color in the ITU's T.416 Open Document Architecture (ODA) and interchange format: Character content architectures, which was adopted as ISO/IEC 8613-6 but ended up as a commercial failure. The ODA version is more elaborate and thus incompatible with the above semicolon-separated version:

- Colons are used as separators, rather than semicolons.
- The parameters after the '2' (r, g, and b) are optional and can be left empty.
- There is a leading "colorspace ID". The definition of the colorspace ID is not included in that specification, so it may be blank to represent the unspecified default. For CMYK color specifications, mintty interprets the colorspace ID parameter as specifying the maximum value which the channel values are given out of (e.g. 100 or 255).
- In addition to the '2' value after 48 to specify a Red-Green-Blue format (and the '5' above for a 0-255 indexed color), there are alternatives of '0' for implementation-defined and '1' for transparent - neither of which have any further parameters; '3' specifies colors using a Cyan-Magenta-Yellow scheme, and '4' for a Cyan-Magenta-Yellow-Black one, the latter using the position marked as "unused" for the Black component.

```
ESC[38:2:⟨Color-Space-ID⟩:⟨r⟩:⟨g⟩:⟨b⟩:⟨unused⟩:⟨CS tolerance⟩:⟨Color-Space⟩m Select RGB foreground color
ESC[48:2:⟨Color-Space-ID⟩:⟨r⟩:⟨g⟩:⟨b⟩:⟨unused⟩:⟨CS tolerance⟩:⟨Color-Space⟩m Select RGB background color
```

where `Color-Space` indicates the Color-Space associated with the given tolerance: `0` for CIELUV or `1` for CIELAB.

The semicolon-based RGB specification is the most widely supported, but both it and the RGB variant of ITU T.416 are supported by many terminal emulators.

#### Unix environment variables relating to color support

Rather than using the color support in termcap and terminfo introduced in SVr3.2 (1987), the S-Lang library (version 0.99-32, June 1996) used a separate environment variable `$COLORTERM` to indicate whether a terminal emulator could use colors at all, and later added values to indicate if it supported 24-bit color. This system, although poorly documented, became widespread enough for Fedora and RHEL to consider using it as a simpler and more universal detection mechanism compared to querying the now-updated libraries.

Some terminal emulators (urxvt, Konsole) set `$COLORFGBG` to report the color scheme of the terminal (mainly light vs. dark background). This behavior originated in S-Lang and is used by vim. Gnome-terminal refuses to add this behavior, as the syntax for the value is not agreed upon, the value cannot be changed upon a runtime change of the palette, and more "proper" xterm OSC 4/10/11 sequences already exist.

It has become conventional to use the `NO_COLOR` environment variable to disable colors unconditionally.

## Operating System Command sequences

Most Operating System Command sequences were defined by Xterm, but many are also supported by other terminal emulators. For historical reasons, Xterm can end the command with `BEL` (0x07) as well as the standard `ST` (0x9C or 0x1B 0x5C). For example, Xterm allows the icon name and window title to be set by `ESC ]0;this is the title BEL`.

A non-xterm extension is the hyperlink, `ESC ]8;;link ST` from 2017, used by VTE, iTerm2, and mintty, among others.

The Linux console uses `ESC ] P n rr gg bb` to change the palette, which, if hard-coded into an application, may hang other terminals. However, appending `ST` will be ignored by Linux and form a proper, ignorable sequence for other terminals.

## Fs Escape sequences

If the `ESC` is followed by a byte in the range 0x60—0x7E, the escape sequence is of type `Fs`. This type is used for control functions individually registered with the ISO-IR registry. A table of these is listed under ISO/IEC 2022.

## Fp Escape sequences

If the `ESC` is followed by a byte in the range 0x30—0x3F, the escape sequence is of type `Fp`, which is set apart for up to sixteen private-use control functions.

|   | Abbr | Name | Effect |
|---|---|---|---|
| ESC 7 | DECSC | DEC Save Cursor | Saves the cursor position, encoding shift state and formatting attributes. |
| ESC 8 | DECRC | DEC Restore Cursor | Restores the cursor position, encoding shift state and formatting attributes from the previous DECSC if any, otherwise resets these all to their defaults. |

## nF Escape sequences

If the `ESC` is followed by a byte in the range 0x20—0x2F, the escape sequence is of type `nF`. Said byte is followed by any number of additional bytes in this range, and then a byte in the range 0x30-0x7E. These escape sequences are further subcategorised by the low two bits of the first byte, e.g. "type `2F`" for sequences where the first byte is 0x22; and by whether the final byte is in the range 0x30—0x3F indicating private use (e.g. "type `2Fp`") or not (e.g. "type `2Ft`").

Most of the `nFt` sequences are for changing the current character set, and are listed in ISO/IEC 2022. Some others:

|   | Abbr | Name | Effect |
|---|---|---|---|
| ESC SP F | ACS6 S7C1T | Announce Code Structure 6 Send 7-bit C1 Control Character to the Host | Makes the function keys send ESC + letter instead of 8-bit C1 codes. |
| ESC SP G | ACS7 S8C1T | Announce Code Structure 7 Send 8-bit C1 Control Character to the Host | Makes the function keys send 8-bit C1 codes. |

If the first byte is '#' the public sequences are reserved for additional ISO-IR registered individual control functions. No such sequences are presently registered. Type `3Fp` sequences (which includes ones starting with '#') are available for private-use control functions.

|   | Abbr | Name | Effect |
|---|---|---|---|
| ESC # 3 | DECDHL | DEC Double-Height Letters, Top Half | Makes the current line use characters twice as tall. This code is for the top half. |
| ESC # 4 | DECDHL | DEC Double-Height Letters, Bottom Half | Makes the current line use characters twice as tall. This code is for the bottom half. |
| ESC # 5 | DECSWL | DEC Single-Width Line | Makes the current line use single-width characters, per the default behaviour. |
| ESC # 6 | DECDWL | DEC Double-Width Line | Makes the current line use double-width characters, discarding any characters in the second half of the line. |

## Examples

`CSI 2 J` — This clears the screen and, on some devices, locates the cursor to the y,x position 1,1 (upper left corner).

`CSI 32 m` — This makes text green. The green may be a dark, dull green, so you may wish to enable Bold with the sequence `CSI 1 m` which would make it bright green, or combined as `CSI 32 ; 1 m`. Some implementations use the Bold state to make the character Bright.

`CSI 0 ; 6 8 ; "DIR" ; 13 p` — This reassigns the key F10 to send to the keyboard buffer the string "DIR" and ENTER, which in the DOS command line would display the contents of the current directory. (MS-DOS ANSI.SYS only) This was sometimes used for ANSI bombs. This is a private-use code (as indicated by the letter p), using a non-standard extension to include a string-valued parameter. Following the letter of the standard would consider the sequence to end at the letter D.

`CSI s` — This saves the cursor position. Using the sequence `CSI u` will restore it to the position. Say the current cursor position is 7(y) and 10(x). The sequence `CSI s` will save those two numbers. Now you can move to a different cursor position, such as 20(y) and 3(x), using the sequence `CSI 20 ; 3 H` or `CSI 20 ; 3 f`. Now if you use the sequence CSI u the cursor position will return to 7(y) and 10(x). Some terminals require the DEC sequences `ESC 7` / `ESC 8` instead which is more widely supported.

### In shell scripting

ANSI escape codes are often used in UNIX and UNIX-like terminals to provide syntax highlighting. For example, on compatible terminals, the following *list* command color-codes file and directory names by type.

```
ls --color
```

Users can employ escape codes in their scripts by including them as part of *standard output* or *standard error*. For example, the following GNU *sed* command embellishes the output of the *make* command by displaying lines containing words starting with "WARN" in reverse video and words starting with "ERR" in bright yellow on a dark red background (letter case is ignored). The representations of the codes are highlighted.

```
make 2>&1 | sed -e 's/.*\bWARN.*/\x1b[7m&\x1b[0m/i' -e 's/.*\bERR.*/\x1b[93;41m&\x1b[0m/i'
```

The following Bash function flashes the terminal (by alternately sending reverse and normal video mode codes) until the user presses a key. It can be used to alert a programmer when a lengthy command terminates, such as with `make ; flasher` .

```mw
flasher () { while true; do printf '\e[?5h'; sleep 0.1; printf '\e[?5l'; read -s -n1 -t1 && break; done; }
```

The following command will reset the console, similar to the command `reset` on modern Linux systems; however it should work even on older Linux systems and on other (non-Linux) UNIX variants.

```mw
printf '\033c'
```

### In C

This following program creates a table of numbers from 0 to 109, each of which is displayed in the format specified by the Select Graphic Rendition escape sequence using that number as the graphic rendition code.

```mw
#include <stdio.h>

int main(void)
{
    int row, col, n;

    for (row = 0; row < 11; row++) {
        for (col = 0; col < 10; col++) {
            n = 10 * row + col;
            if (n > 109) break;
            printf("\033[%dm %3d\033[m", n, n);
        }
        printf("\n");
    }
    return 0;
}
```

## Terminal input sequences

Pressing special keys on the keyboard, as well as outputting many xterm CSI, DCS, or OSC sequences, often produces a CSI, DCS, or OSC sequence, sent from the terminal to the computer as though the user typed it.

When typing input on a terminal keypresses outside the normal main alphanumeric keyboard area can be sent to the host as ANSI sequences. For keys that have an equivalent output function, such as the cursor keys, these often mirror the output sequences. However, for most keypresses there isn't an equivalent output sequence to use.

There are several encoding schemes, and unfortunately most terminals mix sequences from different schemes, so host software has to be able to deal with input sequences using any scheme. To complicate the matter, the VT terminals themselves have two schemes of input, *normal mode* and *application mode* that can be switched by the application.

(draft section)

```
<char>                                         -> char
<esc>                                          -> esc
<esc> <esc>                                    -> Alt-esc
<esc> <char>                                   -> Alt-keypress or keycode sequence
<esc> '['                                      -> Alt-[
<esc> '[' (<modifier>) <char>                  -> keycode sequence, <modifier> is a decimal
                                                  number and defaults to 1 (xterm)
<esc> '[' (<keycode>) (';'<modifier>) '~'      -> keycode sequence, <keycode> and <modifier>
                                                  are decimal numbers and default to 1 (vt)
```

If the terminating character is '~', the first number must be present and is a keycode number, the second number is an optional modifier value. If the terminating character is a letter, the letter is the keycode value, and the optional number is the modifier value.

The modifier value defaults to 1, and after subtracting 1 is a bitmap of modifier keys being pressed: Meta+Ctrl+Alt+⇧ Shift. So, for example, `<esc>[4;2~` is ⇧ Shift+End, `<esc>[20~` is function key F9, `<esc>[5C` is Ctrl+→.

In other words, the modifier is the sum of the following numbers:

| Key pressed | Number | Comment |
|---|---|---|
|   | 1 | always added, the rest are optional |
| Shift | 1 |   |
| (Left) Alt | 2 |   |
| Control | 4 |   |
| Meta | 8 |   |

```
vt sequences:
<esc>[1~    - Home        <esc>[16~   -             <esc>[31~   - F17
<esc>[2~    - Insert      <esc>[17~   - F6          <esc>[32~   - F18
<esc>[3~    - Delete      <esc>[18~   - F7          <esc>[33~   - F19
<esc>[4~    - End         <esc>[19~   - F8          <esc>[34~   - F20
<esc>[5~    - PgUp        <esc>[20~   - F9          <esc>[35~   - 
<esc>[6~    - PgDn        <esc>[21~   - F10         
<esc>[7~    - Home        <esc>[22~   -             
<esc>[8~    - End         <esc>[23~   - F11         
<esc>[9~    -             <esc>[24~   - F12         
<esc>[10~   - F0          <esc>[25~   - F13         
<esc>[11~   - F1          <esc>[26~   - F14         
<esc>[12~   - F2          <esc>[27~   -             
<esc>[13~   - F3          <esc>[28~   - F15         
<esc>[14~   - F4          <esc>[29~   - F16         
<esc>[15~   - F5          <esc>[30~   -

xterm sequences:
<esc>[A     - Up          <esc>[K     -             <esc>[U     -
<esc>[B     - Down        <esc>[L     -             <esc>[V     -
<esc>[C     - Right       <esc>[M     -             <esc>[W     -
<esc>[D     - Left        <esc>[N     -             <esc>[X     -
<esc>[E     -             <esc>[O     -             <esc>[Y     -
<esc>[F     - End         <esc>OP     - F1          <esc>[Z     -
<esc>[G     - Keypad 5    <esc>OQ     - F2       
<esc>[H     - Home        <esc>OR     - F3       
<esc>[I     -             <esc>OS     - F4       
<esc>[J     -             <esc>[T     - 
```

`<esc>[A` to `<esc>[D` are the same as the ANSI output sequences. The `<modifier>` is normally omitted if no modifier keys are pressed, but most implementations always emit the `<modifier>` for F1–F4. (draft section)

Xterm has a comprehensive documentation page on the various function-key and mouse input sequence schemes from DEC's VT terminals and various other terminals it emulates. Thomas Dickey has added a lot of support to it over time; he also maintains a list of default keys used by other terminal emulators for comparison.

- On the Linux console, certain function keys generate sequences of the form `CSI [ *char*`. The CSI sequence should terminate on the `[`.
- Old versions of Terminator generate `SS3 1; *modifiers* *char*` when F1 – F4 are pressed with modifiers. The faulty behavior was copied from GNOME Terminal.
- xterm replies `CSI *row* ; *column* R` if asked for cursor position and `CSI 1 ; *modifiers* R` if the F3 key is pressed with modifiers, which collide in the case of `*row* == 1`. This can be avoided by using the *?* private modifier as `CSI ? 6 n`, which will be reflected in the response as `CSI ? *row* ; *column* R`.
- many terminals prepend `ESC` to any character that is typed with the alt key down. This creates ambiguity for uppercase letters and symbols `@[\]^_`, which would form C1 codes.
- Konsole generates `SS3 *modifiers* *char*` when F1 – F4 are pressed with modifiers.
- Some terminals, including iTerm2 and kitty, support reporting additional keys via an enhanced CSI u mode.
