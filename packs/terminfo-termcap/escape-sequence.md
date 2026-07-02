---
title: "Escape sequence"
source: https://en.wikipedia.org/wiki/Escape_sequence
domain: terminfo-termcap
license: CC-BY-SA-4.0
tags: terminfo database, termcap capabilities, terminal capability database, terminal control codes
fetched: 2026-07-02
---

# Escape sequence

In computing, an **escape sequence** is a sequence of characters that has a special semantic meaning based on an established convention that specifies an escape character prefix in addition to the syntax of the rest of the text of a sequence. A convention can define any particular character code as a sequence prefix. Some conventions use a normal, printable character such as backslash (\) or ampersand (&). Others use a non-printable (a.k.a. control) character such as ASCII *escape*.

Escape sequences date back at least to the 1874 Baudot code.

## Examples

### Data transmission

A common use of an escape sequence is to remove control characters from a data stream so that it does not cause its control function by mistake. The control character is replaced with an escape character and one or more other subsequent characters. After escaping the normal context in which the control character would have caused an action, the sequence is replaced by the removed character. To transmit the escape character itself, two copies are sent.

### Text literal

An escape sequence is often used in character and string literals, to express characters that are not printable or clash with the syntax of characters or strings. For example, control characters might not be allowed in a source file or may have undesirable side-effects if typed into a command.

A feature of C and many programming languages influenced by it is that the beginning of an escape sequence in such text literals is marked by a backslash (`\`). Common examples of these C-style escape sequences include `\r`, `\n` and `\t` for the carriage return, newline, and tab characters, respectively. To account for the fact that using a printable character for escape causes that character to lose its normal meaning, a sequence of two backslash characters (`\\`) is provided to express a single backslash. There is also an escape sequence that expresses any character by its ASCII-code value. For example, the backslash can be expressed as either `\x5c` or `\134`, which specify the character code value in hexadecimal and octal notations, respectively. Likewise, the lowercase *e* can be expressed as `\145` and the digit 7 as `\067`.

A backslash immediately followed by a newline (which is necessarily outside of a string literal) does not mark an escape sequence. Instead, it can be thought of as meaning "Disregard the newline": the C preprocessor joins the line with the subsequent line.

### Quoting escape

When an escape character is needed within a string literal, there are two common strategies:

- Doubled delimiter – For example, `'He didn''t do it.'`)
- Secondary escape sequence – For example, the command prompt command `echo Cut^&Paste` outputs "Cut&Paste" in by escaping the ampersand operator with a caret (`^`)

In C and many related languages, the escape character is the backslash (`\`). The single quotation mark character can be coded as `'\''` since `'''` is not valid. As a string literal is delimited by double-quotes (`"`) the content cannot contain a double-quote unless it is escaped (`"\""`) or via a sequence that specifies the code of the double-quote character (`\x22`).

In Perl or Python 2, the following is invalid syntax:

```mw
print "Nancy said "Hello World!" to the crowd."
```

This can be fixed by inserted backslash to escape:

```mw
print "Nancy said \"Hello World!\" to the crowd."
```

Alternatively, the following uses "\x" to indicate the subsequent two characters are hexadecimal digits; "22" being the hexadecimal ASCII value for double-quote.

```mw
print "Nancy said \x22Hello World!\x22 to the crowd."
```

C, C++, Java, and Ruby allow the same two backslash escape styles. PostScript and rich text format (RTF) also use backslash escapes. The quoted-printable encoding uses the equals sign as an escape character. URL and URI use percent-encoding to quote characters with a special meaning, as for non-ASCII characters.

### ANSI escape sequences

The VT52 terminal used simple digraph commands like escape-A. Without the escape character prefix, `A` simply meant the letter `A`, but as part of the escape sequence `escape-A`, it had a different meaning. The VT52 also supported parameters. It was not a straightforward control language encoded as substitution.

The later VT100 terminal implemented the more sophisticated ANSI escape sequences standard (now ECMA-48) for functions such as controlling cursor movement, character set, and display enhancements. The HP 2640 series had perhaps the most elaborate escape sequences for block and character modes, programming keys and their soft labels, graphics vectors, and even saving data to tape or disk files.

In Windows (and MS-DOS), a utility, ANSI.SYS, can be used to enable ANSI escape sequence support. In DOS via `$e` in the PROMPT command), and in 16-bit Windows via a command window. In Unix and Unix-like systems, the ANSI escape sequences are generally supported by the shell. The rise of GUI applications has reduced the use of escape sequences, yet the ability to provide full-screen, text-based applications is still available.

### Control sequence

A control sequence is a sequence of characters that changes the state of a computer peripheral instead of conveying the normal information that the characters represent. In an ANSI escape sequence, the escape sequence prefix, called control sequence introducer, can be either ASCII ESC (decimal 27) followed by `[` or CSI (decimal 155). Notable systems that did not use an escape character for control sequences include:

- The Hayes command set defines a modal control sequence, `+++`, which switches from command to online mode. To ensure that the sequence is interpreted as a control sequence instead of embedded in content, the sender stops communication for one second before and after sending `+++`. When the modem detects condition, it switches from normal mode (sending characters to the phone) to a command mode in which the data is interpreted a command. Sending the O command switches back to the normal mode.
- Data General terminal control sequences, but they often were still called escape sequences, and the very common use of "escaping" special characters in programming languages and command-line parameters today often use the "backslash" character to begin the sequence.

Escape sequences in communications are commonly used when a computer and a peripheral have only a single channel through which to send information back and forth (so escape sequences are an example of in-band signaling). They were common when most dumb terminals used ASCII with 7 data bits for communication, and sometimes would be used to switch to a different character set for "foreign" or graphics characters that would otherwise been restricted by the 128 codes available in 7 data bits. Even relatively "dumb" terminals responded to some escape sequences, including the original mechanical Teletype printers (on which "glass Teletypes" or VDUs were based) responded to characters 27 and 31 to alternate between letters and figures modes.

### Esc key

Many computer keyboards have an Esc key (where *Esc* is short for *escape*) even though it is generally not used for entering an escape sequence. The vi text editor uses the key to exit from input mode. Some application use the key to cancel an operation or navigate up a level of a nested context.
