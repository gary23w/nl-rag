---
title: "Bash Reference Manual (part 11/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 11/15
---

## 8 Command Line Editing

This chapter describes the basic features of the GNU command line editing interface. Command line editing is provided by the Readline library, which is used by several different programs, including Bash. Command line editing is enabled by default when using an interactive shell, unless the --noediting option is supplied at shell invocation. Line editing is also used when using the -e option to the `read` builtin command (see Bash Builtin Commands). By default, the line editing commands are similar to those of Emacs; a vi-style line editing interface is also available. Line editing can be enabled at any time using the -o emacs or -o vi options to the `set` builtin command (see The Set Builtin), or disabled using the +o emacs or +o vi options to `set`.

### 8.1 Introduction to Line Editing

The following paragraphs use Emacs style to describe the notation used to represent keystrokes.

The text C-k is read as ‘Control-K’ and describes the character produced when the k key is pressed while the Control key is depressed.

The text M-k is read as ‘Meta-K’ and describes the character produced when the Meta key (if you have one) is depressed, and the k key is pressed (a *meta character*), then both are released. The Meta key is labeled ALT or Option on many keyboards. On keyboards with two keys labeled ALT (usually to either side of the space bar), the ALT on the left side is generally set to work as a Meta key. One of the ALT keys may also be configured as some other modifier, such as a Compose key for typing accented characters.

On some keyboards, the Meta key modifier produces characters with the eighth bit (0200) set. You can use the `enable-meta-key` variable to control whether or not it does this, if the keyboard allows it. On many others, the terminal or terminal emulator converts the metafied key to a key sequence beginning with ESC as described in the next paragraph.

If you do not have a Meta or ALT key, or another key working as a Meta key, you can generally achieve the latter effect by typing ESC *first*, and then typing k. The ESC character is known as the *meta prefix*).

Either process is known as *metafying* the k key.

If your Meta key produces a key sequence with the ESC meta prefix, you can make M-key key bindings you specify (see `Key Bindings` in Readline Init File Syntax) do the same thing by setting the `force-meta-prefix` variable.

The text M-C-k is read as ‘Meta-Control-k’ and describes the character produced by metafying C-k.

In addition, several keys have their own names. Specifically, DEL, ESC, LFD, SPC, RET, and TAB all stand for themselves when seen in this text, or in an init file (see Readline Init File). If your keyboard lacks a LFD key, typing C-j will output the appropriate character. The RET key may be labeled Return or Enter on some keyboards.

### 8.2 Readline Interaction

Often during an interactive session you type in a long line of text, only to notice that the first word on the line is misspelled. The Readline library gives you a set of commands for manipulating the text as you type it in, allowing you to just fix your typo, and not forcing you to retype the majority of the line. Using these editing commands, you move the cursor to the place that needs correction, and delete or insert the text of the corrections. Then, when you are satisfied with the line, you simply press RET. You do not have to be at the end of the line to press RET; the entire line is accepted regardless of the location of the cursor within the line.

#### 8.2.1 Readline Bare Essentials

In order to enter characters into the line, simply type them. The typed character appears where the cursor was, and then the cursor moves one space to the right. If you mistype a character, you can use your erase character to back up and delete the mistyped character.

Sometimes you may mistype a character, and not notice the error until you have typed several other characters. In that case, you can type C-b to move the cursor to the left, and then correct your mistake. Afterwards, you can move the cursor to the right with C-f.

When you add text in the middle of a line, you will notice that characters to the right of the cursor are ‘pushed over’ to make room for the text that you have inserted. Likewise, when you delete text behind the cursor, characters to the right of the cursor are ‘pulled back’ to fill in the blank space created by the removal of the text. These are the bare essentials for editing the text of an input line:

**C-b**

Move back one character.

**C-f**

Move forward one character.

**DEL or Backspace**

Delete the character to the left of the cursor.

**C-d**

Delete the character underneath the cursor.

**Printing characters**

Insert the character into the line at the cursor.

**C-_ or C-x C-u**

Undo the last editing command. You can undo all the way back to an empty line.

Depending on your configuration, the Backspace key might be set to delete the character to the left of the cursor and the DEL key set to delete the character underneath the cursor, like C-d, rather than the character to the left of the cursor.

#### 8.2.2 Readline Movement Commands

The above table describes the most basic keystrokes that you need in order to do editing of the input line. For your convenience, many other commands are available in addition to C-b, C-f, C-d, and DEL. Here are some commands for moving more rapidly within the line.

**C-a**

Move to the start of the line.

**C-e**

Move to the end of the line.

**M-f**

Move forward a word, where a word is composed of letters and digits.

**M-b**

Move backward a word.

**C-l**

Clear the screen, reprinting the current line at the top.

Notice how C-f moves forward a character, while M-f moves forward a word. It is a loose convention that control keystrokes operate on characters while meta keystrokes operate on words.

#### 8.2.3 Readline Killing Commands

*Killing* text means to delete the text from the line, but to save it away for later use, usually by *yanking* (re-inserting) it back into the line. (‘Cut’ and ‘paste’ are more recent jargon for ‘kill’ and ‘yank’.)

If the description for a command says that it ‘kills’ text, then you can be sure that you can get the text back in a different (or the same) place later.

When you use a kill command, the text is saved in a *kill-ring*. Any number of consecutive kills save all of the killed text together, so that when you yank it back, you get it all. The kill ring is not line specific; the text that you killed on a previously typed line is available to be yanked back later, when you are typing another line.

Here is the list of commands for killing text.

**C-k**

Kill the text from the current cursor position to the end of the line.

**M-d**

Kill from the cursor to the end of the current word, or, if between words, to the end of the next word. Word boundaries are the same as those used by M-f.

**M-DEL**

Kill from the cursor to the start of the current word, or, if between words, to the start of the previous word. Word boundaries are the same as those used by M-b.

**C-w**

Kill from the cursor to the previous whitespace. This is different than M-DEL because the word boundaries differ.

Here is how to *yank* the text back into the line. Yanking means to copy the most-recently-killed text from the kill buffer into the line at the current cursor position.

**C-y**

Yank the most recently killed text back into the buffer at the cursor.

**M-y**

Rotate the kill-ring, and yank the new top. You can only do this if the prior command is C-y or M-y.

#### 8.2.4 Readline Arguments

You can pass numeric arguments to Readline commands. Sometimes the argument acts as a repeat count, other times it is the *sign* of the argument that is significant. If you pass a negative argument to a command which normally acts in a forward direction, that command will act in a backward direction. For example, to kill text back to the start of the line, you might type ‘M-- C-k’.

The general way to pass numeric arguments to a command is to type meta digits before the command. If the first ‘digit’ typed is a minus sign (‘-’), then the sign of the argument will be negative. Once you have typed one meta digit to get the argument started, you can type the remainder of the digits, and then the command. For example, to give the C-d command an argument of 10, you could type ‘M-1 0 C-d’, which will delete the next ten characters on the input line.

#### 8.2.5 Searching for Commands in the History

Readline provides commands for searching through the command history (see Bash History Facilities) for lines containing a specified string. There are two search modes: *incremental* and *non-incremental*.

Incremental searches begin before the user has finished typing the search string. As each character of the search string is typed, Readline displays the next entry from the history matching the string typed so far. An incremental search requires only as many characters as needed to find the desired history entry. When using emacs editing mode, type C-r to search backward in the history for a particular string. Typing C-s searches forward through the history. The characters present in the value of the `isearch-terminators` variable are used to terminate an incremental search. If that variable has not been assigned a value, the ESC and C-j characters terminate an incremental search. C-g aborts an incremental search and restores the original line. When the search is terminated, the history entry containing the search string becomes the current line.

To find other matching entries in the history list, type C-r or C-s as appropriate. This searches backward or forward in the history for the next entry matching the search string typed so far. Any other key sequence bound to a Readline command terminates the search and executes that command. For instance, a RET terminates the search and accepts the line, thereby executing the command from the history list. A movement command will terminate the search, make the last line found the current line, and begin editing.

Readline remembers the last incremental search string. If two C-rs are typed without any intervening characters defining a new search string, Readline uses any remembered search string.

Non-incremental searches read the entire search string before starting to search for matching history entries. The search string may be typed by the user or be part of the contents of the current line.

### 8.3 Readline Init File

Although the Readline library comes with a set of Emacs-like keybindings installed by default, it is possible to use a different set of keybindings. Any user can customize programs that use Readline by putting commands in an *inputrc* file, conventionally in their home directory. The name of this file is taken from the value of the shell variable `INPUTRC`. If that variable is unset, the default is ~/.inputrc. If that file does not exist or cannot be read, Readline looks for /etc/inputrc. The `bind` builtin command can also be used to set Readline keybindings and variables. See Bash Builtin Commands.

When a program that uses the Readline library starts up, Readline reads the init file and sets any variables and key bindings it contains.

In addition, the `C-x C-r` command re-reads this init file, thus incorporating any changes that you might have made to it.

#### 8.3.1 Readline Init File Syntax

There are only a few basic constructs allowed in the Readline init file. Blank lines are ignored. Lines beginning with a ‘#’ are comments. Lines beginning with a ‘$’ indicate conditional constructs (see Conditional Init Constructs). Other lines denote variable settings and key bindings.

**Variable Settings**

You can modify the run-time behavior of Readline by altering the values of variables in Readline using the `set` command within the init file. The syntax is simple:

```
set variable value
```

Here, for example, is how to change from the default Emacs-like key binding to use `vi` line editing commands:

```
set editing-mode vi
```

Variable names and values, where appropriate, are recognized without regard to case. Unrecognized variable names are ignored.

Boolean variables (those that can be set to on or off) are set to on if the value is null or empty, *on* (case-insensitive), or 1. Any other value results in the variable being set to off.

The `bind -V` command lists the current Readline variable names and values. See Bash Builtin Commands.

A great deal of run-time behavior is changeable with the following variables.

**`active-region-start-color` ¶**

A string variable that controls the text color and background when displaying the text in the active region (see the description of `enable-active-region` below). This string must not take up any physical character positions on the display, so it should consist only of terminal escape sequences. It is output to the terminal before displaying the text in the active region. This variable is reset to the default value whenever the terminal type changes. The default value is the string that puts the terminal in standout mode, as obtained from the terminal’s terminfo description. A sample value might be ‘\e[01;33m’.

**`active-region-end-color` ¶**

A string variable that “undoes” the effects of `active-region-start-color` and restores “normal” terminal display appearance after displaying text in the active region. This string must not take up any physical character positions on the display, so it should consist only of terminal escape sequences. It is output to the terminal after displaying the text in the active region. This variable is reset to the default value whenever the terminal type changes. The default value is the string that restores the terminal from standout mode, as obtained from the terminal’s terminfo description. A sample value might be ‘\e[0m’.

**`bell-style` ¶**

Controls what happens when Readline wants to ring the terminal bell. If set to ‘none’, Readline never rings the bell. If set to ‘visible’, Readline uses a visible bell if one is available. If set to ‘audible’ (the default), Readline attempts to ring the terminal’s bell.

**`bind-tty-special-chars` ¶**

If set to ‘on’ (the default), Readline attempts to bind the control characters that are treated specially by the kernel’s terminal driver to their Readline equivalents. These override the default Readline bindings described here. Type ‘stty -a’ at a Bash prompt to see your current terminal settings, including the special control characters (usually `cchars`).

**`blink-matching-paren` ¶**

If set to ‘on’, Readline attempts to briefly move the cursor to an opening parenthesis when a closing parenthesis is inserted. The default is ‘off’.

**`colored-completion-prefix` ¶**

If set to ‘on’, when listing completions, Readline displays the common prefix of the set of possible completions using a different color. The color definitions are taken from the value of the `LS_COLORS` environment variable. If there is a color definition in `LS_COLORS` for the custom suffix ‘readline-colored-completion-prefix’, Readline uses this color for the common prefix instead of its default. The default is ‘off’.

**`colored-stats` ¶**

If set to ‘on’, Readline displays possible completions using different colors to indicate their file type. The color definitions are taken from the value of the `LS_COLORS` environment variable. The default is ‘off’.

**`comment-begin` ¶**

The string to insert at the beginning of the line by the `insert-comment` command. The default value is `"#"`.

**`completion-display-width` ¶**

The number of screen columns used to display possible matches when performing completion. The value is ignored if it is less than 0 or greater than the terminal screen width. A value of 0 causes matches to be displayed one per line. The default value is -1.

**`completion-ignore-case` ¶**

If set to ‘on’, Readline performs filename matching and completion in a case-insensitive fashion. The default value is ‘off’.

**`completion-map-case` ¶**

If set to ‘on’, and *completion-ignore-case* is enabled, Readline treats hyphens (‘-’) and underscores (‘_’) as equivalent when performing case-insensitive filename matching and completion. The default value is ‘off’.

**`completion-prefix-display-length` ¶**

The maximum length in characters of the common prefix of a list of possible completions that is displayed without modification. When set to a value greater than zero, Readline replaces common prefixes longer than this value with an ellipsis when displaying possible completions. If a completion begins with a period, and Readline is completing filenames, it uses three underscores instead of an ellipsis.

**`completion-query-items` ¶**

The number of possible completions that determines when the user is asked whether the list of possibilities should be displayed. If the number of possible completions is greater than or equal to this value, Readline asks whether or not the user wishes to view them; otherwise, Readline simply lists the completions. This variable must be set to an integer value greater than or equal to zero. A zero value means Readline should never ask; negative values are treated as zero. The default limit is `100`.

**`convert-meta` ¶**

If set to ‘on’, Readline converts characters it reads that have the eighth bit set to an ASCII key sequence by clearing the eighth bit and prefixing an ESC character, converting them to a meta-prefixed key sequence. The default value is ‘on’, but Readline sets it to ‘off’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and may change if the locale changes. This variable also affects key bindings; see the description of `force-meta-prefix` below.

**`disable-completion` ¶**

If set to ‘On’, Readline inhibits word completion. Completion characters are inserted into the line as if they had been mapped to `self-insert`. The default is ‘off’.

**`echo-control-characters` ¶**

When set to ‘on’, on operating systems that indicate they support it, Readline echoes a character corresponding to a signal generated from the keyboard. The default is ‘on’.

**`editing-mode` ¶**

The `editing-mode` variable controls the default set of key bindings. By default, Readline starts up in emacs editing mode, where the keystrokes are most similar to Emacs. This variable can be set to either ‘emacs’ or ‘vi’.

**`emacs-mode-string` ¶**

If the *show-mode-in-prompt* variable is enabled, this string is displayed immediately before the last line of the primary prompt when emacs editing mode is active. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘\1’ and ‘\2’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘@’.

**`enable-active-region` ¶**

*point* is the current cursor position, and *mark* refers to a saved cursor position (see Commands For Moving). The text between the point and mark is referred to as the *region*. When this variable is set to ‘On’, Readline allows certain commands to designate the region as *active*. When the region is active, Readline highlights the text in the region using the value of the `active-region-start-color`, which defaults to the string that enables the terminal’s standout mode. The active region shows the text inserted by bracketed-paste and any matching text found by incremental and non-incremental history searches. The default is ‘On’.

**`enable-bracketed-paste` ¶**

When set to ‘On’, Readline configures the terminal to insert each paste into the editing buffer as a single string of characters, instead of treating each character as if it had been read from the keyboard. This is called putting the terminal into *bracketed paste mode*; it prevents Readline from executing any editing commands bound to key sequences appearing in the pasted text. The default is ‘On’.

**`enable-keypad` ¶**

When set to ‘on’, Readline tries to enable the application keypad when it is called. Some systems need this to enable the arrow keys. The default is ‘off’.

**`enable-meta-key` ¶**

When set to ‘on’, Readline tries to enable any meta modifier key the terminal claims to support when it is called. On many terminals, the Meta key is used to send eight-bit characters; this variable checks for the terminal capability that indicates the terminal can enable and disable a mode that sets the eighth bit of a character (0200) if the Meta key is held down when the character is typed (a meta character). The default is ‘on’.

**`expand-tilde` ¶**

If set to ‘on’, Readline attempts tilde expansion when it attempts word completion. The default is ‘off’.

**`force-meta-prefix` ¶**

If set to ‘on’, Readline modifies its behavior when binding key sequences containing \M- or `Meta-` (see `Key Bindings` in Readline Init File Syntax) by converting a key sequence of the form \M-*C* or `Meta-`*C* to the two-character sequence ESC *C* (adding the meta prefix). If `force-meta-prefix` is set to ‘off’ (the default), Readline uses the value of the `convert-meta` variable to determine whether to perform this conversion: if `convert-meta` is ‘on’, Readline performs the conversion described above; if it is ‘off’, Readline converts *C* to a meta character by setting the eighth bit (0200). The default is ‘off’.

**`history-preserve-point` ¶**

If set to ‘on’, the history code attempts to place the point (the current cursor position) at the same location on each history line retrieved with `previous-history` or `next-history`. The default is ‘off’.

**`history-size` ¶**

Set the maximum number of history entries saved in the history list. If set to zero, any existing history entries are deleted and no new entries are saved. If set to a value less than zero, the number of history entries is not limited. By default, Bash sets the maximum number of history entries to the value of the `HISTSIZE` shell variable. If you try to set *history-size* to a non-numeric value, the maximum number of history entries will be set to 500.

**`horizontal-scroll-mode` ¶**

Setting this variable to ‘on’ means that the text of the lines being edited will scroll horizontally on a single screen line when the lines are longer than the width of the screen, instead of wrapping onto a new screen line. This variable is automatically set to ‘on’ for terminals of height 1. By default, this variable is set to ‘off’.

**`input-meta` ¶**

If set to ‘on’, Readline enables eight-bit input (that is, it does not clear the eighth bit in the characters it reads), regardless of what the terminal claims it can support. The default value is ‘off’, but Readline sets it to ‘on’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and its value may change if the locale changes. The name `meta-flag` is a synonym for `input-meta`.

**`isearch-terminators` ¶**

The string of characters that should terminate an incremental search without subsequently executing the character as a command (see Searching for Commands in the History). If this variable has not been given a value, the characters ESC and C-j terminate an incremental search.

**`keymap` ¶**

Sets Readline’s idea of the current keymap for key binding commands. Built-in `keymap` names are `emacs`, `emacs-standard`, `emacs-meta`, `emacs-ctlx`, `vi`, `vi-move`, `vi-command`, and `vi-insert`. `vi` is equivalent to `vi-command` (`vi-move` is also a synonym); `emacs` is equivalent to `emacs-standard`. Applications may add additional names. The default value is `emacs`; the value of the `editing-mode` variable also affects the default keymap.

**`keyseq-timeout`**

Specifies the duration Readline will wait for a character when reading an ambiguous key sequence (one that can form a complete key sequence using the input read so far, or can take additional input to complete a longer key sequence). If Readline doesn’t receive any input within the timeout, it uses the shorter but complete key sequence. Readline uses this value to determine whether or not input is available on the current input source (`rl_instream` by default). The value is specified in milliseconds, so a value of 1000 means that Readline will wait one second for additional input. If this variable is set to a value less than or equal to zero, or to a non-numeric value, Readline waits until another key is pressed to decide which key sequence to complete. The default value is `500`.

**`mark-directories`**

If set to ‘on’, completed directory names have a slash appended. The default is ‘on’.

**`mark-modified-lines` ¶**

When this variable is set to ‘on’, Readline displays an asterisk (‘*’) at the start of history lines which have been modified. This variable is ‘off’ by default.

**`mark-symlinked-directories` ¶**

If set to ‘on’, completed names which are symbolic links to directories have a slash appended, subject to the value of `mark-directories`. The default is ‘off’.

**`match-hidden-files` ¶**

This variable, when set to ‘on’, forces Readline to match files whose names begin with a ‘.’ (hidden files) when performing filename completion. If set to ‘off’, the user must include the leading ‘.’ in the filename to be completed. This variable is ‘on’ by default.

**`menu-complete-display-prefix` ¶**

If set to ‘on’, menu completion displays the common prefix of the list of possible completions (which may be empty) before cycling through the list. The default is ‘off’.

**`output-meta` ¶**

If set to ‘on’, Readline displays characters with the eighth bit set directly rather than as a meta-prefixed escape sequence. The default is ‘off’, but Readline sets it to ‘on’ if the locale contains characters whose encodings may include bytes with the eighth bit set. This variable is dependent on the `LC_CTYPE` locale category, and its value may change if the locale changes.

**`page-completions` ¶**

If set to ‘on’, Readline uses an internal pager resembling *more*(1) to display a screenful of possible completions at a time. This variable is ‘on’ by default.

**`prefer-visible-bell`**

See `bell-style`.

**`print-completions-horizontally`**

If set to ‘on’, Readline displays completions with matches sorted horizontally in alphabetical order, rather than down the screen. The default is ‘off’.

**`revert-all-at-newline` ¶**

If set to ‘on’, Readline will undo all changes to history lines before returning when executing `accept-line`. By default, history lines may be modified and retain individual undo lists across calls to `readline()`. The default is ‘off’.

**`search-ignore-case` ¶**

If set to ‘on’, Readline performs incremental and non-incremental history list searches in a case-insensitive fashion. The default value is ‘off’.

**`show-all-if-ambiguous` ¶**

This alters the default behavior of the completion functions. If set to ‘on’, words which have more than one possible completion cause the matches to be listed immediately instead of ringing the bell. The default value is ‘off’.

**`show-all-if-unmodified` ¶**

This alters the default behavior of the completion functions in a fashion similar to *show-all-if-ambiguous*. If set to ‘on’, words which have more than one possible completion without any possible partial completion (the possible completions don’t share a common prefix) cause the matches to be listed immediately instead of ringing the bell. The default value is ‘off’.

**`show-mode-in-prompt` ¶**

If set to ‘on’, add a string to the beginning of the prompt indicating the editing mode: emacs, vi command, or vi insertion. The mode strings are user-settable (e.g., *emacs-mode-string*). The default value is ‘off’.

**`skip-completed-text` ¶**

If set to ‘on’, this alters the default completion behavior when inserting a single match into the line. It’s only active when performing completion in the middle of a word. If enabled, Readline does not insert characters from the completion that match characters after point in the word being completed, so portions of the word following the cursor are not duplicated. For instance, if this is enabled, attempting completion when the cursor is after the first ‘e’ in ‘Makefile’ will result in ‘Makefile’ rather than ‘Makefilefile’, assuming there is a single possible completion. The default value is ‘off’.

**`vi-cmd-mode-string` ¶**

If the *show-mode-in-prompt* variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in command mode. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘\1’ and ‘\2’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘(cmd)’.

**`vi-ins-mode-string` ¶**

If the *show-mode-in-prompt* variable is enabled, this string is displayed immediately before the last line of the primary prompt when vi editing mode is active and in insertion mode. The value is expanded like a key binding, so the standard set of meta- and control- prefixes and backslash escape sequences is available. The ‘\1’ and ‘\2’ escapes begin and end sequences of non-printing characters, which can be used to embed a terminal control sequence into the mode string. The default is ‘(ins)’.

**`visible-stats` ¶**

If set to ‘on’, a character denoting a file’s type is appended to the filename when listing possible completions. The default is ‘off’.

**Key Bindings**

The syntax for controlling key bindings in the init file is simple. First you need to find the name of the command that you want to change. The following sections contain tables of the command name, the default keybinding, if any, and a short description of what the command does.

Once you know the name of the command, simply place on a line in the init file the name of the key you wish to bind the command to, a colon, and then the name of the command. There can be no space between the key name and the colon – that will be interpreted as part of the key name. The name of the key can be expressed in different ways, depending on what you find most comfortable.

In addition to command names, Readline allows keys to be bound to a string that is inserted when the key is pressed (a *macro*). The difference between a macro and a command is that a macro is enclosed in single or double quotes.

The `bind -p` command displays Readline function names and bindings in a format that can be put directly into an initialization file. See Bash Builtin Commands.

***keyname*: *function-name* or *macro***

*keyname* is the name of a key spelled out in English. For example:

```
Control-u: universal-argument
Meta-Rubout: backward-kill-word
Control-o: "> output"
```

In the example above, C-u is bound to the function `universal-argument`, M-DEL is bound to the function `backward-kill-word`, and C-o is bound to run the macro expressed on the right hand side (that is, to insert the text ‘> output’ into the line).

This key binding syntax recognizes a number of symbolic character names: *DEL*, *ESC*, *ESCAPE*, *LFD*, *NEWLINE*, *RET*, *RETURN*, *RUBOUT* (a destructive backspace), *SPACE*, *SPC*, and *TAB*.

**"*keyseq*": *function-name* or *macro***

*keyseq* differs from *keyname* above in that strings denoting an entire key sequence can be specified, by placing the key sequence in double quotes. Some GNU Emacs style key escapes can be used, as in the following example, but none of the special character names are recognized.

```
"\C-u": universal-argument
"\C-x\C-r": re-read-init-file
"\e[11~": "Function Key 1"
```

In the above example, C-u is again bound to the function `universal-argument` (just as it was in the first example), ‘C-x C-r’ is bound to the function `re-read-init-file`, and ‘ESC [ 1 1 ~’ is bound to insert the text ‘Function Key 1’.

The following GNU Emacs style escape sequences are available when specifying key sequences:

**`\C-`**

A control prefix.

**`\M-`**

Adding the meta prefix or converting the following character to a meta character, as described above under `force-meta-prefix` (see `Variable Settings` in Readline Init File Syntax).

**`\e`**

An escape character.

**`\\`**

Backslash.

**`\"`**

", a double quotation mark.

**`\'`**

', a single quote or apostrophe.

In addition to the GNU Emacs style escape sequences, a second set of backslash escapes is available:

**`\a`**

alert (bell)

**`\b`**

backspace

**`\d`**

delete

**`\f`**

form feed

**`\n`**

newline

**`\r`**

carriage return

**`\t`**

horizontal tab

**`\v`**

vertical tab

**`\*nnn*`**

The eight-bit character whose value is the octal value *nnn* (one to three digits).

**`\x*HH*`**

The eight-bit character whose value is the hexadecimal value *HH* (one or two hex digits).

When entering the text of a macro, single or double quotes must be used to indicate a macro definition. Unquoted text is assumed to be a function name. The backslash escapes described above are expanded in the macro body. Backslash will quote any other character in the macro text, including ‘"’ and ‘'’. For example, the following binding will make ‘C-x \’ insert a single ‘\’ into the line:

```
"\C-x\\": "\\"
```

#### 8.3.2 Conditional Init Constructs

Readline implements a facility similar in spirit to the conditional compilation features of the C preprocessor which allows key bindings and variable settings to be performed as the result of tests. There are four parser directives available.

**`$if`**

The `$if` construct allows bindings to be made based on the editing mode, the terminal being used, or the application using Readline. The text of the test, after any comparison operator, extends to the end of the line; unless otherwise noted, no characters are required to isolate it.

**`mode`**

The `mode=` form of the `$if` directive is used to test whether Readline is in `emacs` or `vi` mode. This may be used in conjunction with the ‘set keymap’ command, for instance, to set bindings in the `emacs-standard` and `emacs-ctlx` keymaps only if Readline is starting out in `emacs` mode.

**`term`**

The `term=` form may be used to include terminal-specific key bindings, perhaps to bind the key sequences output by the terminal’s function keys. The word on the right side of the ‘=’ is tested against both the full name of the terminal and the portion of the terminal name before the first ‘-’. This allows `xterm` to match both `xterm` and `xterm-256color`, for instance.

**`version`**

The `version` test may be used to perform comparisons against specific Readline versions. The `version` expands to the current Readline version. The set of comparison operators includes ‘=’ (and ‘==’), ‘!=’, ‘<=’, ‘>=’, ‘<’, and ‘>’. The version number supplied on the right side of the operator consists of a major version number, an optional decimal point, and an optional minor version (e.g., ‘7.1’). If the minor version is omitted, it defaults to ‘0’. The operator may be separated from the string `version` and from the version number argument by whitespace. The following example sets a variable if the Readline version being used is 7.0 or newer:

```
$if version >= 7.0
set show-mode-in-prompt on
$endif
```

**`application`**

The *application* construct is used to include application-specific settings. Each program using the Readline library sets the *application name*, and you can test for a particular value. This could be used to bind key sequences to functions useful for a specific program. For instance, the following command adds a key sequence that quotes the current or previous word in Bash:

```
$if Bash
# Quote the current or previous word
"\C-xq": "\eb\"\ef\""
$endif
```

**`variable`**

The *variable* construct provides simple equality tests for Readline variables and values. The permitted comparison operators are ‘=’, ‘==’, and ‘!=’. The variable name must be separated from the comparison operator by whitespace; the operator may be separated from the value on the right hand side by whitespace. String and boolean variables may be tested. Boolean variables must be tested against the values *on* and *off*. The following example is equivalent to the `mode=emacs` test described above:

```
$if editing-mode == emacs
set show-mode-in-prompt on
$endif
```

**`$else`**

Commands in this branch of the `$if` directive are executed if the test fails.

**`$endif`**

This command, as seen in the previous example, terminates an `$if` command.

**`$include`**

This directive takes a single filename as an argument and reads commands and key bindings from that file. For example, the following directive reads from /etc/inputrc:

```
$include /etc/inputrc
```

#### 8.3.3 Sample Init File

Here is an example of an *inputrc* file. This illustrates key binding, variable assignment, and conditional syntax.

```
# This file controls the behavior of line input editing for
# programs that use the GNU Readline library.  Existing
# programs include FTP, Bash, and GDB.
#
# You can re-read the inputrc file with C-x C-r.
# Lines beginning with '#' are comments.
#
# First, include any system-wide bindings and variable
# assignments from /etc/Inputrc
$include /etc/Inputrc

#
# Set various bindings for emacs mode.

set editing-mode emacs 

$if mode=emacs

Meta-Control-h:	backward-kill-word	Text after the function name is ignored

#
# Arrow keys in keypad mode
#
#"\M-OD":        backward-char
#"\M-OC":        forward-char
#"\M-OA":        previous-history
#"\M-OB":        next-history
#
# Arrow keys in ANSI mode
#
"\M-[D":        backward-char
"\M-[C":        forward-char
"\M-[A":        previous-history
"\M-[B":        next-history
#
# Arrow keys in 8 bit keypad mode
#
#"\M-\C-OD":       backward-char
#"\M-\C-OC":       forward-char
#"\M-\C-OA":       previous-history
#"\M-\C-OB":       next-history
#
# Arrow keys in 8 bit ANSI mode
#
#"\M-\C-[D":       backward-char
#"\M-\C-[C":       forward-char
#"\M-\C-[A":       previous-history
#"\M-\C-[B":       next-history

C-q: quoted-insert

$endif

# An old-style binding.  This happens to be the default.
TAB: complete

# Macros that are convenient for shell interaction
$if Bash
# edit the path
"\C-xp": "PATH=${PATH}\e\C-e\C-a\ef\C-f"
# prepare to type a quoted word --
# insert open and close double quotes
# and move to just after the open quote
"\C-x\"": "\"\"\C-b"
# insert a backslash (testing backslash escapes
# in sequences and macros)
"\C-x\\": "\\"
# Quote the current or previous word
"\C-xq": "\eb\"\ef\""
# Add a binding to refresh the line, which is unbound
"\C-xr": redraw-current-line
# Edit variable on current line.
"\M-\C-v": "\C-a\C-k$\C-y\M-\C-e\C-a\C-y="
$endif

# use a visible bell if one is available
set bell-style visible

# don't strip characters to 7 bits when reading
set input-meta on

# allow iso-latin1 characters to be inserted rather
# than converted to prefix-meta sequences
set convert-meta off

# display characters with the eighth bit set directly
# rather than as meta-prefixed characters
set output-meta on

# if there are 150 or more possible completions for a word,
# ask whether or not the user wants to see all of them
set completion-query-items 150

# For FTP
$if Ftp
"\C-xg": "get \M-?"
"\C-xt": "put \M-?"
"\M-.": yank-last-arg
$endif
```

### 8.4 Bindable Readline Commands

This section describes Readline commands that may be bound to key sequences. You can list your key bindings by executing `bind -P` or, for a more terse format, suitable for an *inputrc* file, `bind -p`. (See Bash Builtin Commands.) Command names without an accompanying key sequence are unbound by default.

In the following descriptions, *point* refers to the current cursor position, and *mark* refers to a cursor position saved by the `set-mark` command. The text between the point and mark is referred to as the *region*. Readline has the concept of an *active region*: when the region is active, Readline redisplay highlights the region using the value of the `active-region-start-color` variable. The `enable-active-region` variable turns this on and off. Several commands set the region to active; those are noted below.

#### 8.4.1 Commands For Moving

**`beginning-of-line (C-a)` ¶**

Move to the start of the current line. This may also be bound to the Home key on some keyboards.

**`end-of-line (C-e)` ¶**

Move to the end of the line. This may also be bound to the End key on some keyboards.

**`forward-char (C-f)` ¶**

Move forward a character. This may also be bound to the right arrow key on some keyboards.

**`backward-char (C-b)` ¶**

Move back a character. This may also be bound to the left arrow key on some keyboards.

**`forward-word (M-f)` ¶**

Move forward to the end of the next word. Words are composed of letters and digits.

**`backward-word (M-b)` ¶**

Move back to the start of the current or previous word. Words are composed of letters and digits.

**`shell-forward-word (M-C-f)` ¶**

Move forward to the end of the next word. Words are delimited by non-quoted shell metacharacters.

**`shell-backward-word (M-C-b)` ¶**

Move back to the start of the current or previous word. Words are delimited by non-quoted shell metacharacters.

**`previous-screen-line ()` ¶**

Attempt to move point to the same physical screen column on the previous physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if point is not greater than the length of the prompt plus the screen width.

**`next-screen-line ()` ¶**

Attempt to move point to the same physical screen column on the next physical screen line. This will not have the desired effect if the current Readline line does not take up more than one physical line or if the length of the current Readline line is not greater than the length of the prompt plus the screen width.

**`clear-display (M-C-l)` ¶**

Clear the screen and, if possible, the terminal’s scrollback buffer, then redraw the current line, leaving the current line at the top of the screen.

**`clear-screen (C-l)` ¶**

Clear the screen, then redraw the current line, leaving the current line at the top of the screen. If given a numeric argument, this refreshes the current line without clearing the screen.

**`redraw-current-line ()` ¶**

Refresh the current line. By default, this is unbound.

#### 8.4.2 Commands For Manipulating The History

**`accept-line (Newline or Return)` ¶**

Accept the line regardless of where the cursor is. If this line is non-empty, add it to the history list according to the setting of the `HISTCONTROL` and `HISTIGNORE` variables. If this line is a modified history line, then restore the history line to its original state.

**`previous-history (C-p)` ¶**

Move ‘back’ through the history list, fetching the previous command. This may also be bound to the up arrow key on some keyboards.

**`next-history (C-n)` ¶**

Move ‘forward’ through the history list, fetching the next command. This may also be bound to the down arrow key on some keyboards.

**`beginning-of-history (M-<)` ¶**

Move to the first line in the history.

**`end-of-history (M->)` ¶**

Move to the end of the input history, i.e., the line currently being entered.

**`reverse-search-history (C-r)` ¶**

Search backward starting at the current line and moving ‘up’ through the history as necessary. This is an incremental search. This command sets the region to the matched text and activates the region.

**`forward-search-history (C-s)` ¶**

Search forward starting at the current line and moving ‘down’ through the history as necessary. This is an incremental search. This command sets the region to the matched text and activates the region.

**`non-incremental-reverse-search-history (M-p)` ¶**

Search backward starting at the current line and moving ‘up’ through the history as necessary using a non-incremental search for a string supplied by the user. The search string may match anywhere in a history line.

**`non-incremental-forward-search-history (M-n)` ¶**

Search forward starting at the current line and moving ‘down’ through the history as necessary using a non-incremental search for a string supplied by the user. The search string may match anywhere in a history line.

**`history-search-backward ()` ¶**

Search backward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. By default, this command is unbound, but may be bound to the Page Down key on some keyboards.

**`history-search-forward ()` ¶**

Search forward through the history for the string of characters between the start of the current line and the point. The search string must match at the beginning of a history line. This is a non-incremental search. By default, this command is unbound, but may be bound to the Page Up key on some keyboards.

**`history-substring-search-backward ()` ¶**

Search backward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. By default, this command is unbound.

**`history-substring-search-forward ()` ¶**

Search forward through the history for the string of characters between the start of the current line and the point. The search string may match anywhere in a history line. This is a non-incremental search. By default, this command is unbound.

**`yank-nth-arg (M-C-y)` ¶**

Insert the first argument to the previous command (usually the second word on the previous line) at point. With an argument *n*, insert the *n*th word from the previous command (the words in the previous command begin with word 0). A negative argument inserts the *n*th word from the end of the previous command. Once the argument *n* is computed, this uses the history expansion facilities to extract the *n*th word, as if the ‘!*n*’ history expansion had been specified.

**`yank-last-arg (M-. or M-_)` ¶**
