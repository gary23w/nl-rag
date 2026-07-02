---
title: "Bash Reference Manual (part 12/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 12/15
---

# Bash Reference Manual

Insert last argument to the previous command (the last word of the previous history entry). With a numeric argument, behave exactly like `yank-nth-arg`. Successive calls to `yank-last-arg` move back through the history list, inserting the last word (or the word specified by the argument to the first call) of each line in turn. Any numeric argument supplied to these successive calls determines the direction to move through the history. A negative argument switches the direction through the history (back or forward). This uses the history expansion facilities to extract the last word, as if the ‘!$’ history expansion had been specified.

**`operate-and-get-next (C-o)` ¶**

Accept the current line for return to the calling application as if a newline had been entered, and fetch the next line relative to the current line from the history for editing. A numeric argument, if supplied, specifies the history entry to use instead of the current line.

**`fetch-history ()` ¶**

With a numeric argument, fetch that entry from the history list and make it the current line. Without an argument, move back to the first entry in the history list.

#### 8.4.3 Commands For Changing Text

**`*end-of-file* (usually C-d)` ¶**

The character indicating end-of-file as set, for example, by `stty`. If this character is read when there are no characters on the line, and point is at the beginning of the line, Readline interprets it as the end of input and returns EOF.

**`delete-char (C-d)` ¶**

Delete the character at point. If this function is bound to the same character as the tty EOF character, as C-d commonly is, see above for the effects. This may also be bound to the Delete key on some keyboards.

**`backward-delete-char (Rubout)` ¶**

Delete the character behind the cursor. A numeric argument means to kill the characters, saving them on the kill ring, instead of deleting them.

**`forward-backward-delete-char ()` ¶**

Delete the character under the cursor, unless the cursor is at the end of the line, in which case the character behind the cursor is deleted. By default, this is not bound to a key.

**`quoted-insert (C-q or C-v)` ¶**

Add the next character typed to the line verbatim. This is how to insert key sequences like C-q, for example.

**`self-insert (a, b, A, 1, !, …)` ¶**

Insert the character typed.

**`bracketed-paste-begin ()` ¶**

This function is intended to be bound to the "bracketed paste" escape sequence sent by some terminals, and such a binding is assigned by default. It allows Readline to insert the pasted text as a single unit without treating each character as if it had been read from the keyboard. The characters are inserted as if each one was bound to `self-insert` instead of executing any editing commands.

Bracketed paste sets the region (the characters between point and the mark) to the inserted text. It sets the *active region*.

**`transpose-chars (C-t)` ¶**

Drag the character before the cursor forward over the character at the cursor, moving the cursor forward as well. If the insertion point is at the end of the line, then this transposes the last two characters of the line. Negative arguments have no effect.

**`transpose-words (M-t)` ¶**

Drag the word before point past the word after point, moving point past that word as well. If the insertion point is at the end of the line, this transposes the last two words on the line.

**`shell-transpose-words (M-C-t)` ¶**

Drag the word before point past the word after point, moving point past that word as well. If the insertion point is at the end of the line, this transposes the last two words on the line. Word boundaries are the same as `shell-forward-word` and `shell-backward-word`.

**`upcase-word (M-u)` ¶**

Uppercase the current (or following) word. With a negative argument, uppercase the previous word, but do not move the cursor.

**`downcase-word (M-l)` ¶**

Lowercase the current (or following) word. With a negative argument, lowercase the previous word, but do not move the cursor.

**`capitalize-word (M-c)` ¶**

Capitalize the current (or following) word. With a negative argument, capitalize the previous word, but do not move the cursor.

**`overwrite-mode ()` ¶**

Toggle overwrite mode. With an explicit positive numeric argument, switches to overwrite mode. With an explicit non-positive numeric argument, switches to insert mode. This command affects only `emacs` mode; `vi` mode does overwrite differently. Each call to `readline()` starts in insert mode.

In overwrite mode, characters bound to `self-insert` replace the text at point rather than pushing the text to the right. Characters bound to `backward-delete-char` replace the character before point with a space.

By default, this command is unbound, but may be bound to the Insert key on some keyboards.

#### 8.4.4 Killing And Yanking

**`kill-line (C-k)` ¶**

Kill the text from point to the end of the current line. With a negative numeric argument, kill backward from the cursor to the beginning of the line.

**`backward-kill-line (C-x Rubout)` ¶**

Kill backward from the cursor to the beginning of the current line. With a negative numeric argument, kill forward from the cursor to the end of the line.

**`unix-line-discard (C-u)` ¶**

Kill backward from the cursor to the beginning of the current line.

**`kill-whole-line ()` ¶**

Kill all characters on the current line, no matter where point is. By default, this is unbound.

**`kill-word (M-d)` ¶**

Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as `forward-word`.

**`backward-kill-word (M-DEL)` ¶**

Kill the word behind point. Word boundaries are the same as `backward-word`.

**`shell-kill-word (M-C-d)` ¶**

Kill from point to the end of the current word, or if between words, to the end of the next word. Word boundaries are the same as `shell-forward-word`.

**`shell-backward-kill-word ()` ¶**

Kill the word behind point. Word boundaries are the same as `shell-backward-word`.

**`unix-word-rubout (C-w)` ¶**

Kill the word behind point, using white space as a word boundary, saving the killed text on the kill-ring.

**`unix-filename-rubout ()` ¶**

Kill the word behind point, using white space and the slash character as the word boundaries, saving the killed text on the kill-ring.

**`delete-horizontal-space ()` ¶**

Delete all spaces and tabs around point. By default, this is unbound.

**`kill-region ()` ¶**

Kill the text in the current region. By default, this command is unbound.

**`copy-region-as-kill ()` ¶**

Copy the text in the region to the kill buffer, so it can be yanked right away. By default, this command is unbound.

**`copy-backward-word ()` ¶**

Copy the word before point to the kill buffer. The word boundaries are the same as `backward-word`. By default, this command is unbound.

**`copy-forward-word ()` ¶**

Copy the word following point to the kill buffer. The word boundaries are the same as `forward-word`. By default, this command is unbound.

**`yank (C-y)` ¶**

Yank the top of the kill ring into the buffer at point.

**`yank-pop (M-y)` ¶**

Rotate the kill-ring, and yank the new top. You can only do this if the prior command is `yank` or `yank-pop`.

#### 8.4.5 Specifying Numeric Arguments

**`digit-argument (M-0, M-1, … M--)` ¶**

Add this digit to the argument already accumulating, or start a new argument. M-- starts a negative argument.

**`universal-argument ()` ¶**

This is another way to specify an argument. If this command is followed by one or more digits, optionally with a leading minus sign, those digits define the argument. If the command is followed by digits, executing `universal-argument` again ends the numeric argument, but is otherwise ignored. As a special case, if this command is immediately followed by a character that is neither a digit nor minus sign, the argument count for the next command is multiplied by four. The argument count is initially one, so executing this function the first time makes the argument count four, a second time makes the argument count sixteen, and so on. By default, this is not bound to a key.

#### 8.4.6 Letting Readline Type For You

**`complete (TAB)` ¶**

Attempt to perform completion on the text before point. The actual completion performed is application-specific. Bash attempts completion by first checking for any programmable completions for the command word (see Programmable Completion), otherwise treating the text as a variable (if the text begins with ‘$’), username (if the text begins with ‘~’), hostname (if the text begins with ‘@’), or command (including aliases, functions, and builtins) in turn. If none of these produces a match, it falls back to filename completion.

**`possible-completions (M-?)` ¶**

List the possible completions of the text before point. When displaying completions, Readline sets the number of columns used for display to the value of `completion-display-width`, the value of the environment variable `COLUMNS`, or the screen width, in that order.

**`insert-completions (M-*)` ¶**

Insert all completions of the text before point that would have been generated by `possible-completions`, separated by a space.

**`menu-complete ()` ¶**

Similar to `complete`, but replaces the word to be completed with a single match from the list of possible completions. Repeatedly executing `menu-complete` steps through the list of possible completions, inserting each match in turn. At the end of the list of completions, `menu-complete` rings the bell (subject to the setting of `bell-style`) and restores the original text. An argument of *n* moves *n* positions forward in the list of matches; a negative argument moves backward through the list. This command is intended to be bound to TAB, but is unbound by default.

**`menu-complete-backward ()` ¶**

Identical to `menu-complete`, but moves backward through the list of possible completions, as if `menu-complete` had been given a negative argument. This command is unbound by default.

**`export-completions ()` ¶**

Perform completion on the word before point as described above and write the list of possible completions to Readline’s output stream using the following format, writing information on separate lines:

- the number of matches *N*;
- the word being completed;
- *S*:*E*, where *S* and *E* are the start and end offsets of the word in the Readline line buffer; then
- each match, one per line

If there are no matches, the first line will be “0”, and this command does not print any output after the *S*:*E*. If there is only a single match, this prints a single line containing it. If there is more than one match, this prints the common prefix of the matches, which may be empty, on the first line after the *S*:*E*, then the matches on subsequent lines. In this case, *N* will include the first line with the common prefix.

The user or application should be able to accommodate the possibility of a blank line. The intent is that the user or application reads *N* lines after the line containing *S*:*E* to obtain the match list. This command is unbound by default.

**`delete-char-or-list ()` ¶**

Deletes the character under the cursor if not at the beginning or end of the line (like `delete-char`). At the end of the line, it behaves identically to `possible-completions`. This command is unbound by default.

**`complete-filename (M-/)` ¶**

Attempt filename completion on the text before point.

**`possible-filename-completions (C-x /)` ¶**

List the possible completions of the text before point, treating it as a filename.

**`complete-username (M-~)` ¶**

Attempt completion on the text before point, treating it as a username.

**`possible-username-completions (C-x ~)` ¶**

List the possible completions of the text before point, treating it as a username.

**`complete-variable (M-$)` ¶**

Attempt completion on the text before point, treating it as a shell variable.

**`possible-variable-completions (C-x $)` ¶**

List the possible completions of the text before point, treating it as a shell variable.

**`complete-hostname (M-@)` ¶**

Attempt completion on the text before point, treating it as a hostname.

**`possible-hostname-completions (C-x @)` ¶**

List the possible completions of the text before point, treating it as a hostname.

**`complete-command (M-!)` ¶**

Attempt completion on the text before point, treating it as a command name. Command completion attempts to match the text against aliases, reserved words, shell functions, shell builtins, and finally executable filenames, in that order.

**`possible-command-completions (C-x !)` ¶**

List the possible completions of the text before point, treating it as a command name.

**`dynamic-complete-history (M-TAB)` ¶**

Attempt completion on the text before point, comparing the text against history list entries for possible completion matches.

**`dabbrev-expand ()` ¶**

Attempt menu completion on the text before point, comparing the text against lines from the history list for possible completion matches.

**`complete-into-braces (M-{)` ¶**

Perform filename completion and insert the list of possible completions enclosed within braces so the list is available to the shell (see Brace Expansion).

#### 8.4.7 Keyboard Macros

**`start-kbd-macro (C-x ()` ¶**

Begin saving the characters typed into the current keyboard macro.

**`end-kbd-macro (C-x ))` ¶**

Stop saving the characters typed into the current keyboard macro and save the definition.

**`call-last-kbd-macro (C-x e)` ¶**

Re-execute the last keyboard macro defined, by making the characters in the macro appear as if typed at the keyboard.

**`print-last-kbd-macro ()` ¶**

Print the last keyboard macro defined in a format suitable for the *inputrc* file.

#### 8.4.8 Some Miscellaneous Commands

**`re-read-init-file (C-x C-r)` ¶**

Read in the contents of the *inputrc* file, and incorporate any bindings or variable assignments found there.

**`abort (C-g)` ¶**

Abort the current editing command and ring the terminal’s bell (subject to the setting of `bell-style`).

**`do-lowercase-version (M-A, M-B, M-*x*, …)` ¶**

If the metafied character *x* is upper case, run the command that is bound to the corresponding metafied lower case character. The behavior is undefined if *x* is already lower case.

**`prefix-meta (ESC)` ¶**

Metafy the next character typed. Typing ‘ESC f’ is equivalent to typing M-f.

**`undo (C-_ or C-x C-u)` ¶**

Incremental undo, separately remembered for each line.

**`revert-line (M-r)` ¶**

Undo all changes made to this line. This is like executing the `undo` command enough times to get back to the initial state.

**`tilde-expand (M-&)` ¶**

Perform tilde expansion on the current word.

**`set-mark (C-@)` ¶**

Set the mark to the point. If a numeric argument is supplied, set the mark to that position.

**`exchange-point-and-mark (C-x C-x)` ¶**

Swap the point with the mark. Set the current cursor position to the saved position, then set the mark to the old cursor position.

**`character-search (C-])` ¶**

Read a character and move point to the next occurrence of that character. A negative argument searches for previous occurrences.

**`character-search-backward (M-C-])` ¶**

Read a character and move point to the previous occurrence of that character. A negative argument searches for subsequent occurrences.

**`skip-csi-sequence ()` ¶**

Read enough characters to consume a multi-key sequence such as those defined for keys like Home and End. CSI sequences begin with a Control Sequence Indicator (CSI), usually ESC [. If this sequence is bound to "\e[", keys producing CSI sequences have no effect unless explicitly bound to a Readline command, instead of inserting stray characters into the editing buffer. This is unbound by default, but usually bound to ESC [.

**`insert-comment (M-#)` ¶**

Without a numeric argument, insert the value of the `comment-begin` variable at the beginning of the current line. If a numeric argument is supplied, this command acts as a toggle: if the characters at the beginning of the line do not match the value of `comment-begin`, insert the value; otherwise delete the characters in `comment-begin` from the beginning of the line. In either case, the line is accepted as if a newline had been typed. The default value of `comment-begin` causes this command to make the current line a shell comment. If a numeric argument causes the comment character to be removed, the line will be executed by the shell.

**`dump-functions ()` ¶**

Print all of the functions and their key bindings to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an *inputrc* file. This command is unbound by default.

**`dump-variables ()` ¶**

Print all of the settable variables and their values to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an *inputrc* file. This command is unbound by default.

**`dump-macros ()` ¶**

Print all of the Readline key sequences bound to macros and the strings they output to the Readline output stream. If a numeric argument is supplied, the output is formatted in such a way that it can be made part of an *inputrc* file. This command is unbound by default.

**`execute-named-command (M-x)` ¶**

Read a bindable Readline command name from the input and execute the function to which it’s bound, as if the key sequence to which it was bound appeared in the input. If this function is supplied with a numeric argument, it passes that argument to the function it executes.

**`spell-correct-word (C-x s)` ¶**

Perform spelling correction on the current word, treating it as a directory or filename, in the same way as the `cdspell` shell option. Word boundaries are the same as those used by `shell-forward-word`.

**`glob-complete-word (M-g)` ¶**

Treat the word before point as a pattern for pathname expansion, with an asterisk implicitly appended, then use the pattern to generate a list of matching file names for possible completions.

**`glob-expand-word (C-x *)` ¶**

Treat the word before point as a pattern for pathname expansion, and insert the list of matching file names, replacing the word. If a numeric argument is supplied, append a ‘*’ before pathname expansion.

**`glob-list-expansions (C-x g)` ¶**

Display the list of expansions that would have been generated by `glob-expand-word`, and redisplay the line. If a numeric argument is supplied, append a ‘*’ before pathname expansion.

**`shell-expand-line (M-C-e)` ¶**

Expand the line by performing shell word expansions. This performs alias and history expansion, $’*string*’ and $"*string*" quoting, tilde expansion, parameter and variable expansion, arithmetic expansion, command and process substitution, word splitting, and quote removal. An explicit argument suppresses command and process substitution.

**`history-expand-line (M-^)` ¶**

Perform history expansion on the current line.

**`magic-space ()` ¶**

Perform history expansion on the current line and insert a space (see History Expansion).

**`alias-expand-line ()` ¶**

Perform alias expansion on the current line (see Aliases).

**`history-and-alias-expand-line ()` ¶**

Perform history and alias expansion on the current line.

**`insert-last-argument (M-. or M-_)` ¶**

A synonym for `yank-last-arg`.

**`edit-and-execute-command (C-x C-e)` ¶**

Invoke an editor on the current command line, and execute the result as shell commands. Bash attempts to invoke `$VISUAL`, `$EDITOR`, and `emacs` as the editor, in that order.

**`display-shell-version (C-x C-v)` ¶**

Display version information about the current instance of Bash.

### 8.5 Readline vi Mode

While the Readline library does not have a full set of `vi` editing functions, it does contain enough to allow simple editing of the line. The Readline `vi` mode behaves as specified in the `sh` description in the POSIX standard.

You can use the ‘set -o emacs’ and ‘set -o vi’ commands (see The Set Builtin) to switch interactively between `emacs` and `vi` editing modes, The Readline default is `emacs` mode.

When you enter a line in `vi` mode, you are already placed in ‘insertion’ mode, as if you had typed an ‘i’. Pressing ESC switches you into ‘command’ mode, where you can edit the text of the line with the standard `vi` movement keys, move to previous history lines with ‘k’ and subsequent lines with ‘j’, and so forth.

### 8.6 Programmable Completion

When the user attempts word completion for a command or an argument to a command for which a completion specification (a *compspec*) has been defined using the `complete` builtin (see Programmable Completion Builtins), Readline invokes the programmable completion facilities.

First, Bash identifies the command name. If a compspec has been defined for that command, the compspec is used to generate the list of possible completions for the word. If the command word is the empty string (completion attempted at the beginning of an empty line), Bash uses any compspec defined with the -E option to `complete`. The -I option to `complete` indicates that the command word is the first non-assignment word on the line, or after a command delimiter such as ‘;’ or ‘|’. This usually indicates command name completion.

If the command word is a full pathname, Bash searches for a compspec for the full pathname first. If there is no compspec for the full pathname, Bash attempts to find a compspec for the portion following the final slash. If those searches do not result in a compspec, or if there is no compspec for the command word, Bash uses any compspec defined with the -D option to `complete` as the default. If there is no default compspec, Bash performs alias expansion on the command word as a final resort, and attempts to find a compspec for the command word resulting from any successful expansion.

If a compspec is not found, Bash performs its default completion described above (see Letting Readline Type For You). Otherwise, once a compspec has been found, Bash uses it to generate the list of matching words.

First, Bash performs the *actions* specified by the compspec. This only returns matches which are prefixes of the word being completed. When the -f or -d option is used for filename or directory name completion, Bash uses shell the variable `FIGNORE` to filter the matches. See Bash Variables, for a description of `FIGNORE`.

Next, programmable completion generates matches specified by a pathname expansion pattern supplied as an argument to the -G option. The words generated by the pattern need not match the word being completed. Bash uses the `FIGNORE` variable to filter the matches, but does not use the `GLOBIGNORE` shell variable.

Next, completion considers the string specified as the argument to the -W option. The string is first split using the characters in the `IFS` special variable as delimiters. This honors shell quoting within the string, in order to provide a mechanism for the words to contain shell metacharacters or characters in the value of `IFS`. Each word is then expanded using brace expansion, tilde expansion, parameter and variable expansion, command substitution, and arithmetic expansion, as described above (see Shell Expansions). The results are split using the rules described above (see Word Splitting). The results of the expansion are prefix-matched against the word being completed, and the matching words become possible completions.

After these matches have been generated, Bash executes any shell function or command specified with the -F and -C options. When the command or function is invoked, Bash assigns values to the `COMP_LINE`, `COMP_POINT`, `COMP_KEY`, and `COMP_TYPE` variables as described above (see Bash Variables). If a shell function is being invoked, Bash also sets the `COMP_WORDS` and `COMP_CWORD` variables. When the function or command is invoked, the first argument ($1) is the name of the command whose arguments are being completed, the second argument ($2) is the word being completed, and the third argument ($3) is the word preceding the word being completed on the current command line. There is no filtering of the generated completions against the word being completed; the function or command has complete freedom in generating the matches and they do not need to match a prefix of the word.

Any function specified with -F is invoked first. The function may use any of the shell facilities, including the `compgen` and `compopt` builtins described below (see Programmable Completion Builtins), to generate the matches. It must put the possible completions in the `COMPREPLY` array variable, one per array element.

Next, any command specified with the -C option is invoked in an environment equivalent to command substitution. It should print a list of completions, one per line, to the standard output. Backslash will escape a newline, if necessary. These are added to the set of possible completions.

After generating all of the possible completions, Bash applies any filter specified with the -X option to the completions in the list. The filter is a pattern as used for pathname expansion; a ‘&’ in the pattern is replaced with the text of the word being completed. A literal ‘&’ may be escaped with a backslash; the backslash is removed before attempting a match. Any completion that matches the pattern is removed from the list. A leading ‘!’ negates the pattern; in this case Bash removes any completion that does not match the pattern. If the `nocasematch` shell option is enabled (see the description of `shopt` in The Shopt Builtin), Bash performs the match without regard to the case of alphabetic characters.

Finally, programmable completion adds any prefix and suffix specified with the -P and -S options, respectively, to each completion, and returns the result to Readline as the list of possible completions.

If the previously-applied actions do not generate any matches, and the -o dirnames option was supplied to `complete` when the compspec was defined, Bash attempts directory name completion.

If the -o plusdirs option was supplied to `complete` when the compspec was defined, Bash attempts directory name completion and adds any matches to the set of possible completions.

By default, if a compspec is found, whatever it generates is returned to the completion code as the full set of possible completions. The default Bash completions and the Readline default of filename completion are disabled. If the -o bashdefault option was supplied to `complete` when the compspec was defined, and the compspec generates no matches, Bash attempts its default completions. If the compspec and, if attempted, the default Bash completions generate no matches, and the -o default option was supplied to `complete` when the compspec was defined, programmable completion performs Readline’s default completion.

The options supplied to `complete` and `compopt` can control how Readline treats the completions. For instance, the -o fullquote option tells Readline to quote the matches as if they were filenames. See the description of `complete` (see Programmable Completion Builtins) for details.

When a compspec indicates that it wants directory name completion, the programmable completion functions force Readline to append a slash to completed names which are symbolic links to directories, subject to the value of the *mark-directories* Readline variable, regardless of the setting of the *mark-symlinked-directories* Readline variable.

There is some support for dynamically modifying completions. This is most useful when used in combination with a default completion specified with -D. It’s possible for shell functions executed as completion functions to indicate that completion should be retried by returning an exit status of 124. If a shell function returns 124, and changes the compspec associated with the command on which completion is being attempted (supplied as the first argument when the function is executed), programmable completion restarts from the beginning, with an attempt to find a new compspec for that command. This can be used to build a set of completions dynamically as completion is attempted, rather than loading them all at once.

For instance, assuming that there is a library of compspecs, each kept in a file corresponding to the name of the command, the following default completion function would load completions dynamically:

```
_completion_loader()
{
    . "/etc/bash_completion.d/$1.sh" >/dev/null 2>&1 && return 124
}
complete -D -F _completion_loader -o bashdefault -o default
```

### 8.7 Programmable Completion Builtins

Three builtin commands are available to manipulate the programmable completion facilities: one to specify how the arguments to a particular command are to be completed, and two to modify the completion as it is happening.

**`compgen` ¶**

```
compgen [-V varname] [option] [word]
```

Generate possible completion matches for *word* according to the *option*s, which may be any option accepted by the `complete` builtin with the exceptions of -p, -r, -D, -E, and -I, and write the matches to the standard output.

If the -V option is supplied, `compgen` stores the generated completions into the indexed array variable *varname* instead of writing them to the standard output.

When using the -F or -C options, the various shell variables set by the programmable completion facilities, while available, will not have useful values.

The matches will be generated in the same way as if the programmable completion code had generated them directly from a completion specification with the same flags. If *word* is specified, only those completions matching *word* will be displayed or stored.

The return value is true unless an invalid option is supplied, or no matches were generated.

**`complete` ¶**

```
complete [-abcdefgjksuv] [-o comp-option] [-DEI] [-A action]
[-G globpat] [-W wordlist] [-F function] [-C command]
[-X filterpat] [-P prefix] [-S suffix] name [name ...]
complete -pr [-DEI] [name ...]
```

Specify how arguments to each *name* should be completed.

If the -p option is supplied, or if no options or *name*s are supplied, print existing completion specifications in a way that allows them to be reused as input. The -r option removes a completion specification for each *name*, or, if no *name*s are supplied, all completion specifications.

The -D option indicates that other supplied options and actions should apply to the “default” command completion; that is, completion attempted on a command for which no completion has previously been defined. The -E option indicates that other supplied options and actions should apply to “empty” command completion; that is, completion attempted on a blank line. The -I option indicates that other supplied options and actions should apply to completion on the initial non-assignment word on the line, or after a command delimiter such as ‘;’ or ‘|’, which is usually command name completion. If multiple options are supplied, the -D option takes precedence over -E, and both take precedence over -I. If any of -D, -E, or -I are supplied, any other *name* arguments are ignored; these completions only apply to the case specified by the option.

The process of applying these completion specifications when word completion is attempted is described above (see Programmable Completion).

Other options, if specified, have the following meanings. The arguments to the -G, -W, and -X options (and, if necessary, the -P and -S options) should be quoted to protect them from expansion before the `complete` builtin is invoked.

**`-o *comp-option*`**

The *comp-option* controls several aspects of the compspec’s behavior beyond the simple generation of completions. *comp-option* may be one of:

**`bashdefault`**

Perform the rest of the default Bash completions if the compspec generates no matches.

**`default`**

Use Readline’s default filename completion if the compspec generates no matches.

**`dirnames`**

Perform directory name completion if the compspec generates no matches.

**`filenames`**

Tell Readline that the compspec generates filenames, so it can perform any filename-specific processing (such as adding a slash to directory names, quoting special characters, or suppressing trailing spaces). This option is intended to be used with shell functions specified with -F.

**`fullquote`**

Tell Readline to quote all the completed words even if they are not filenames.

**`noquote`**

Tell Readline not to quote the completed words if they are filenames (quoting filenames is the default).

**`nosort`**

Tell Readline not to sort the list of possible completions alphabetically.

**`nospace`**

Tell Readline not to append a space (the default) to words completed at the end of the line.

**`plusdirs`**

After generating any matches defined by the compspec, attempt directory name completion and add any matches to the results of the other actions.

**`-A *action*`**

The *action* may be one of the following to generate a list of possible completions:

**`alias`**

Alias names. May also be specified as -a.

**`arrayvar`**

Array variable names.

**`binding`**

Readline key binding names (see Bindable Readline Commands).

**`builtin`**

Names of shell builtin commands. May also be specified as -b.

**`command`**

Command names. May also be specified as -c.

**`directory`**

Directory names. May also be specified as -d.

**`disabled`**

Names of disabled shell builtins.

**`enabled`**

Names of enabled shell builtins.

**`export`**

Names of exported shell variables. May also be specified as -e.

**`file`**

File and directory names, similar to Readline’s filename completion. May also be specified as -f.

**`function`**

Names of shell functions.

**`group`**

Group names. May also be specified as -g.

**`helptopic`**

Help topics as accepted by the `help` builtin (see Bash Builtin Commands).

**`hostname`**

Hostnames, as taken from the file specified by the `HOSTFILE` shell variable (see Bash Variables).

**`job`**

Job names, if job control is active. May also be specified as -j.

**`keyword`**

Shell reserved words. May also be specified as -k.

**`running`**

Names of running jobs, if job control is active.

**`service`**

Service names. May also be specified as -s.

**`setopt`**

Valid arguments for the -o option to the `set` builtin (see The Set Builtin).

**`shopt`**

Shell option names as accepted by the `shopt` builtin (see Bash Builtin Commands).

**`signal`**

Signal names.

**`stopped`**

Names of stopped jobs, if job control is active.

**`user`**

User names. May also be specified as -u.

**`variable`**

Names of all shell variables. May also be specified as -v.

**`-C *command*`**

*command* is executed in a subshell environment, and its output is used as the possible completions. Arguments are passed as with the -F option.

**`-F *function*`**

The shell function *function* is executed in the current shell environment. When it is executed, the first argument ($1) is the name of the command whose arguments are being completed, the second argument ($2) is the word being completed, and the third argument ($3) is the word preceding the word being completed, as described above (see Programmable Completion). When `function` finishes, programmable completion retrieves the possible completions from the value of the `COMPREPLY` array variable.

**`-G *globpat*`**

Expand the filename expansion pattern *globpat* to generate the possible completions.

**`-P *prefix*`**

Add *prefix* to the beginning of each possible completion after all other options have been applied.

**`-S *suffix*`**

Append *suffix* to each possible completion after all other options have been applied.

**`-W *wordlist*`**

Split the *wordlist* using the characters in the `IFS` special variable as delimiters, and expand each resulting word. Shell quoting is honored within *wordlist* in order to provide a mechanism for the words to contain shell metacharacters or characters in the value of `IFS`. The possible completions are the members of the resultant list which match a prefix of the word being completed.

**`-X *filterpat*`**

*filterpat* is a pattern as used for filename expansion. It is applied to the list of possible completions generated by the preceding options and arguments, and each completion matching *filterpat* is removed from the list. A leading ‘!’ in *filterpat* negates the pattern; in this case, any completion not matching *filterpat* is removed.

The return value is true unless an invalid option is supplied, an option other than -p, -r, -D, -E, or -I is supplied without a *name* argument, an attempt is made to remove a completion specification for a *name* for which no specification exists, or an error occurs adding a completion specification.

**`compopt` ¶**

```
compopt [-o option] [-DEI] [+o option] [name]
```

Modify completion options for each *name* according to the *option*s, or for the currently-executing completion if no *name*s are supplied. If no *option*s are given, display the completion options for each *name* or the current completion. The possible values of *option* are those valid for the `complete` builtin described above.

The -D option indicates that other supplied options should apply to the “default” command completion; the -E option indicates that other supplied options should apply to “empty” command completion; and the -I option indicates that other supplied options should apply to completion on the initial word on the line. These are determined in the same way as the `complete` builtin.

If multiple options are supplied, the -D option takes precedence over -E, and both take precedence over -I

The return value is true unless an invalid option is supplied, an attempt is made to modify the options for a *name* for which no completion specification exists, or an output error occurs.

### 8.8 A Programmable Completion Example

The most common way to obtain additional completion functionality beyond the default actions `complete` and `compgen` provide is to use a shell function and bind it to a particular command using `complete -F`.

The following function provides completions for the `cd` builtin. It is a reasonably good example of what shell functions must do when used for completion. This function uses the word passed as `$2` to determine the directory name to complete. You can also use the `COMP_WORDS` array variable; the current word is indexed by the `COMP_CWORD` variable.

The function relies on the `complete` and `compgen` builtins to do much of the work, adding only the things that the Bash `cd` does beyond accepting basic directory names: tilde expansion (see Tilde Expansion), searching directories in *$CDPATH*, which is described above (see Bourne Shell Builtins), and basic support for the `cdable_vars` shell option (see The Shopt Builtin). `_comp_cd` modifies the value of *IFS* so that it contains only a newline to accommodate file names containing spaces and tabs – `compgen` prints the possible completions it generates one per line.

Possible completions go into the *COMPREPLY* array variable, one completion per array element. The programmable completion system retrieves the completions from there when the function returns.

```
# A completion function for the cd builtin
# based on the cd completion function from the bash_completion package
_comp_cd()
{
    local IFS=$' \t\n'    # normalize IFS
    local cur _skipdot _cdpath
    local i j k

    # Tilde expansion, which also expands tilde to full pathname
    case "$2" in
    \~*)    eval cur="$2" ;;
    *)      cur=$2 ;;
    esac

    # no cdpath or absolute pathname -- straight directory completion
    if [[ -z "${CDPATH:-}" ]] || [[ "$cur" == @(./*|../*|/*) ]]; then
        # compgen prints paths one per line; could also use while loop
        IFS=$'\n'
        COMPREPLY=( $(compgen -d -- "$cur") )
        IFS=$' \t\n'
    # CDPATH+directories in the current directory if not in CDPATH
    else
        IFS=$'\n'
        _skipdot=false
        # preprocess CDPATH to convert null directory names to .
        _cdpath=${CDPATH/#:/.:}
        _cdpath=${_cdpath//::/:.:}
        _cdpath=${_cdpath/%:/:.}
        for i in ${_cdpath//:/$'\n'}; do
            if [[ $i -ef . ]]; then _skipdot=true; fi
            k="${#COMPREPLY[@]}"
            for j in $( compgen -d -- "$i/$cur" ); do
                COMPREPLY[k++]=${j#$i/}        # cut off directory
            done
        done
        $_skipdot || COMPREPLY+=( $(compgen -d -- "$cur") )
        IFS=$' \t\n'
    fi

    # variable names if appropriate shell option set and no completions
    if shopt -q cdable_vars && [[ ${#COMPREPLY[@]} -eq 0 ]]; then
        COMPREPLY=( $(compgen -v -- "$cur") )
    fi

    return 0
}
```

We install the completion function using the -F option to `complete`:

```
# Tell readline to quote appropriate and append slashes to directories;
# use the bash default completion for other arguments
complete -o filenames -o nospace -o bashdefault -F _comp_cd cd
```

Since we’d like Bash and Readline to take care of some of the other details for us, we use several other options to tell Bash and Readline what to do. The -o filenames option tells Readline that the possible completions should be treated as filenames, and quoted appropriately. That option will also cause Readline to append a slash to filenames it can determine are directories (which is why we might want to extend `_comp_cd` to append a slash if we’re using directories found via *CDPATH*: Readline can’t tell those completions are directories). The -o nospace option tells Readline to not append a space character to the directory name, in case we want to append to it. The -o bashdefault option brings in the rest of the “Bash default” completions – possible completions that Bash adds to the default Readline set. These include things like command name completion, variable completion for words beginning with ‘$’ or ‘${’, completions containing pathname expansion patterns (see Filename Expansion), and so on.

Once installed using `complete`, `_comp_cd` will be called every time we attempt word completion for a `cd` command.

Many more examples – an extensive collection of completions for most of the common GNU, Unix, and Linux commands – are available as part of the bash_completion project. This is installed by default on many GNU/Linux distributions. Originally written by Ian Macdonald, the project now lives at https://github.com/scop/bash-completion/. There are ports for other systems such as Solaris and Mac OS X.

An older version of the bash_completion package is distributed with bash in the examples/complete subdirectory.
