---
title: "fzf(1) (part 1/2)"
source: https://man.archlinux.org/man/fzf.1
domain: fzf
license: CC-BY-SA-4.0
tags: fzf finder, fuzzy finder, command-line interface, interactive filter
fetched: 2026-07-02
part: 1/2
---

# fzf(1)

| fzf(1) | fzf - a command-line fuzzy finder | fzf(1) |
|---|---|---|

# NAME

fzf - a command-line fuzzy finder

# SYNOPSIS

fzf [*options*]

# DESCRIPTION

fzf is an interactive filter program for any kind of list.

It implements a "fuzzy" matching algorithm, so you can quickly type in patterns with omitted characters and still get the results you want.

# OPTIONS


## NOTE

**Most long options have the opposite version with **--no-** prefix.**

****-x, --extended****

Extended-search mode. Enabled by default. You can disable it with

+x

or

--no-extended

.

****-e, --exact****

Enable exact-match

****-i, --ignore-case****

Case-insensitive match (default: smart-case match)

****+i, --no-ignore-case****

Case-sensitive match

****--smart-case****

Smart-case match (default). In this mode, the search is case-insensitive by default, but it becomes case-sensitive if the query contains any uppercase letters.

****--literal****

Do not normalize latin script letters for matching.

****--scheme=***SCHEME***

Choose scoring scheme tailored for different types of input.

default

Generic scoring scheme designed to work well with any type of input.

path

Additional bonus point is only given to the characters after path separator. You might want to choose this scheme over

default

if you have many files with spaces in their paths. This also sets

--tiebreak=pathname,length

, to prioritize matches occurring in the tail element of a file path.

history

Scoring scheme well suited for command history or any input where chronological ordering is important. No additional bonus points are given so that we give more weight to the chronological ordering. This also sets

--tiebreak=index

.

fzf chooses

path

scheme when the input is a TTY device, where fzf would start its built-in walker or run

$FZF_DEFAULT_COMMAND

, and there is no

reload

or

transform

action bound to

start

event. Otherwise, it chooses

default

scheme.

****--algo=***TYPE***

Fuzzy matching algorithm (default: v2)

**v2** Optimal scoring algorithm (quality) **v1** Faster but not guaranteed to find the optimal result (performance)

****-n, --nth=***N[,..]***

Comma-separated list of field index expressions for limiting search scope. See

FIELD INDEX EXPRESSION

for the details. When you use this option with

--with-nth

, the field index expressions are calculated against the transformed lines (unlike in

--preview

where fields are extracted from the original lines) because fzf doesn't allow searching against the hidden fields.

****--with-nth=***N[,..] or TEMPLATE***

Transform the presentation of each line using the field index expressions. For advanced transformation, you can provide a template containing field index expressions in curly braces. When you use a template, the trailing delimiter is stripped from each expression, giving you more control over the output.

{n}

in template evaluates to the zero-based ordinal index of the line.

e.g.

# Single expression: drop the first field

echo foo bar baz | fzf --with-nth 2..

# Use template to rearrange fields echo foo,bar,baz | fzf --delimiter , --with-nth '{n},{1},{3},{2},{1..2}'

**change-with-nth** action is only available when **--with-nth** is set. When **--with-nth** is used, fzf retains the original input lines in memory so they can be re-transformed on the fly (e.g. **--with-nth ..** to keep the original presentation). This increases memory usage, so only use **--with-nth** when you actually need field transformation.

****--accept-nth=***N[,..] or TEMPLATE***

Define which fields to print on accept. The last delimiter is stripped from the output. For advanced transformation, you can provide a template containing field index expressions in curly braces. When you use a template, the trailing delimiter is stripped from each expression, giving you more control over the output.

{n}

in template evaluates to the zero-based ordinal index of the line.

e.g.

# Single expression

echo foo bar baz | fzf --accept-nth 2

# Template echo foo bar baz | fzf --accept-nth 'Index: {n}, 1st: {1}, 2nd: {2}, 3rd: {3}'

****+s, --no-sort****

Do not sort the result

****-d, --delimiter=***STR***

Field delimiter regex for

--nth

,

--with-nth

, and field index expressions (default: AWK-style)

****--tail=NUM****

Maximum number of items to keep in memory. This is useful when you want to browse an endless stream of data (e.g. log stream) with fzf while limiting memory usage.

e.g.

# Interactive filtering of a log stream

tail -f *.log | fzf --tail 100000 --tac --no-sort --exact

****--disabled****

Do not perform search. With this option, fzf becomes a simple selector interface rather than a "fuzzy finder". You can later enable the search using

enable-search

or

toggle-search

action.

****--tiebreak=***CRI[,..]***

Comma-separated list of sort criteria to apply when the scores are tied.

**length** Prefers line with shorter length **chunk** Prefers line with shorter matched chunk (delimited by whitespaces) **pathname** Prefers line with matched substring in the file name of the path **begin** Prefers line with matched substring closer to the beginning **end** Prefers line with matched substring closer to the end **index** Prefers line that appeared earlier in the input stream

- Each criterion should appear only once in the list - **index** is only allowed at the end of the list - **index** is implicitly appended to the list when not specified - Default is **length** (or equivalently **length**,index) - If **end** is found in the list, fzf will scan each line backwards


## INPUT/OUTPUT

****--read0****

Read input delimited by ASCII NUL characters instead of newline characters

****--print0****

Print output delimited by ASCII NUL characters instead of newline characters

****--ansi****

Enable processing of ANSI color codes

****--sync****

Synchronous search for multi-staged filtering. If specified, fzf will launch the finder only after the input stream is complete and the initial filtering and the associated actions (bound to any of

start

,

load

,

result

, or

focus

) are complete.

e.g.

# Avoid rendering both fzf instances at the same time

fzf --multi | fzf --sync

# fzf will not render intermediate states (sleep 1; seq 1000000; sleep 1) | fzf --sync --query 5 --listen --bind start:up,load:up,result:up,focus:change-header:Ready

****--no-tty-default****

Make fzf search for the current TTY device via standard error instead of defaulting to

/dev/tty

. This option avoids issues when launching emacsclient from within fzf. Alternatively, you can change the default TTY device by setting

--tty-default=DEVICE_NAME

.


## GLOBAL STYLE

****--style=***PRESET***

Apply a style preset [default|minimal|full[:BORDER_STYLE]]

****--color=***[BASE_SCHEME][,COLOR_NAME[:ANSI_COLOR][:ANSI_ATTRIBUTES]]...***

Color configuration. The name of the base color scheme is followed by custom color mappings. Each entry is separated by a comma and/or whitespaces.

BASE SCHEME:

(default:

dark

on 256-color terminal, otherwise

base16

; If

NO_COLOR

is set,

bw

)

**dark**Color scheme for dark terminal **light**Color scheme for light terminal **base16**Color scheme using base 16 colors (alias: **16**) **bw**No colors (equivalent to **--no-color**)

**COLOR NAMES:** **fg**Text **list-fg**Text in the list section **selected-fg**Selected line text **preview-fg**Preview window text **bg**Background **list-bg**List section background **selected-bg**Selected line background **preview-bg**Preview window background **input-bg**Input window background **header-bg**Header window background **footer-bg**Footer window background **hl**Highlighted substrings **selected-hl**Highlighted substrings in the selected line **current-fg (fg+)**Text (current line) **current-bg (bg+)**Background (current line) **gutter**Gutter on the left **current-hl (hl+)**Highlighted substrings (current line) **alt-bg**Alternate background color to create striped lines **alt-gutter**Alternate gutter color to create the striped pattern **query (input-fg)**Query string **ghost**Ghost text (**--ghost**, **dim** applied by default) **disabled**Query string when search is disabled (**--disabled**) **info**Info line (match counters) **border**Border around the window (**--border** and **--preview**) **list-border**Border around the list section (**--list-border**) **scrollbar**Scrollbar **separator**Horizontal separator on info line **gap-line**Horizontal line on each gap **preview-border**Border around the preview window (**--preview**) **preview-scrollbar**Scrollbar **input-border**Border around the input window (**--input-border**) **header-border**Border around the header window (**--header-border**) **footer-border**Border around the footer window (**--footer-border**) **label**Border label (**--border-label**, **--list-label**, **--input-label**, and **--preview-label**) **list-label**Border label of the list section (**--list-label**) **preview-label**Border label of the preview window (**--preview-label**) **input-label**Border label of the input window (**--input-label**) **header-label**Border label of the header window (**--header-label**) **footer-label**Border label of the footer window (**--footer-label**) **prompt**Prompt **pointer**Pointer to the current line **marker**Multi-select marker **spinner**Streaming input indicator **header (header-fg)**Header **footer (footer-fg)**Footer **nth**Parts of the line specified by **--nth** (only supports attributes) **nomatch**Non-matching items in raw mode (default: **dim**)

**ANSI COLORS:** **-1**Default terminal foreground/background color (or the original color of the text) **0 ~ 15**16 base colors **black** **red** **green** **yellow** **blue** **magenta** **cyan** **white** **bright-black** (gray | grey) **bright-red** **bright-green** **bright-yellow** **bright-blue** **bright-magenta** **bright-cyan** **bright-white** **16 ~ 255**ANSI 256 colors **#rrggbb**24-bit colors

**ANSI ATTRIBUTES: (Only applies to foreground colors)** **regular**Clear previously set attributes; should precede the other ones **strip**Remove colors **bold** **underline** **underline-double** **underline-curly** **underline-dotted** **underline-dashed** **reverse** **dim** **italic** **strikethrough**

**EXAMPLES:**

**# Seoul256 theme with 8-bit colors** **# (https://github.com/junegunn/seoul256.vim)** **fzf --color='bg:237,bg+:236,info:143,border:240,spinner:108' \** **--color='hl:65,fg:252,header:65,fg+:252' \** **--color='pointer:161,marker:168,prompt:110,hl+:108'**

# Seoul256 theme with 24-bit colors fzf --color='bg:#4B4B4B,bg+:#3F3F3F,info:#BDBB72,border:#6B6B6B,spinner:#98BC99' \ --color='hl:#719872,fg:#D9D9D9,header:#719872,fg+:#D9D9D9' \ --color='pointer:#E12672,marker:#E17899,prompt:#98BEDE,hl+:#98BC99'

# Seoul256 light theme with 24-bit colors, each entry separated by whitespaces fzf --style full --color=' fg:#616161 fg+:#616161 bg:#ffffff bg+:#e9e9e9 alt-bg:#f1f1f1 hl:#719872 hl+:#719899 pointer:#e12672 marker:#e17899 header:#719872 spinner:#719899 info:#727100 prompt:#0099bd query:#616161 border:#e1e1e1 '

****--no-color****

Disable colors

****--no-bold****

Do not use bold text

****--black****

Use black background


## DISPLAY MODE

****--height=***[~][-]HEIGHT[%]***

Display fzf window below the cursor with the given height instead of using the full screen.

If a negative value is specified, the height is calculated as the terminal height minus the given value.

fzf --height=-1

When prefixed with **~**, fzf will automatically determine the height in the range according to the input size. You can combine **~** with a negative value.

# Will not take up 100% of the screen seq 5 | fzf --height=~100%

# Adapt to input size, up to terminal height minus 1 seq 5 | fzf --height=~-1

Adaptive height has the following limitations: * Cannot be used with top/bottom margin and padding given in percent size * It will not find the right size when there are multi-line items

****--min-height=***HEIGHT[+]***

Minimum height when

--height

is given as a percentage. Add

+

to automatically increase the value according to the other layout options so that the specified number of items are visible in the list section (default:

10+

). Ignored when

--height

is not specified or set as an absolute value.

****--popup***[=[center|top|bottom|left|right][,SIZE[%]][,SIZE[%]][,border-native]]***

Start fzf in a tmux popup or in a Zellij floating pane (default

center,50%

). Requires tmux 3.3+ or Zellij 0.44+. This option is ignored if you are not running fzf inside tmux or Zellij.

--tmux

is an alias for this option.

e.g. **# Popup in the center with 70% width and height** **fzf --popup 70%**

# Popup on the left with 40% width and 100% height fzf --popup right,40%

# Popup on the bottom with 100% width and 30% height fzf --popup bottom,30%

# Popup on the top with 80% width and 40% height fzf --popup top,80%,40%

# Popup with a native tmux or Zellij border in the center with 80% width and height fzf --popup center,80%,border-native


## LAYOUT

****--layout=***LAYOUT***

Choose the layout (default: default)

**default** Display from the bottom of the screen **reverse** Display from the top of the screen **reverse-list** Display from the top of the screen, prompt at the bottom

****--reverse****

A synonym for

--layout=reverse

****--margin=***MARGIN***

Comma-separated expression for margins around the finder.

TRBL

Same margin for top, right, bottom, and left

TB,RL

Vertical, horizontal margin

T,RL,B

Top, horizontal, bottom margin

T,R,B,L

Top, right, bottom, left margin

Each part can be given in absolute number or in percentage relative to the terminal size with **%** suffix.

e.g. **fzf --margin 10%** **fzf --margin 1,5%**

****--padding=***PADDING***

Comma-separated expression for padding inside the border. Padding is distinguishable from margin only when

--border

option is used.

e.g. **fzf --margin 5% --padding 5% --border --preview 'cat {}' \** **--color bg:#222222,preview-bg:#333333**

TRBL

Same padding for top, right, bottom, and left

TB,RL

Vertical, horizontal padding

T,RL,B

Top, horizontal, bottom padding

T,R,B,L

Top, right, bottom, left padding

****--border***[=STYLE]***

Draw border around the finder

**rounded** Border with rounded corners (default) **sharp** Border with sharp corners **bold** Border with bold lines **double** Border with double lines **dashed** Border with dashed lines and rounded corners **block** Border using block elements; suitable when using different background colors **thinblock** Border using legacy computing symbols; may not be displayed on some terminals **horizontal** Horizontal lines above and below the finder **vertical** Vertical lines on each side of the finder **line** Single line border (position automatically determined) **top** (up) **bottom** (down) **left** **right** **none**

If you use a terminal emulator where each box-drawing character takes 2 columns, try setting **--ambidouble**. If the border is still not properly rendered, set **--no-unicode**.

**line** style draws a single separator line at the top when **--height** is used.

****--border-label***[=LABEL]***

Label to print on the horizontal border line. Should be used with one of the following

--border

options.

*** rounded** *** sharp** *** bold** *** double** *** horizontal** *** top** (up) *** bottom** (down)

e.g. **# ANSI color codes are supported** **# (with https://github.com/busyloop/lolcat)** **label=$(curl -s http://metaphorpsum.com/sentences/1 | lolcat -f)**

# Border label at the center fzf --height=10 --border --border-label="╢ $label ╟" --color=label:italic:black

# Left-aligned (positive integer) fzf --height=10 --border --border-label="╢ $label ╟" --border-label-pos=3 --color=label:italic:black

# Right-aligned (negative integer) on the bottom line (:bottom) fzf --height=10 --border --border-label="╢ $label ╟" --border-label-pos=-3:bottom --color=label:italic:black

****--border-label-pos***[=N[:top|bottom]]***

Position of the border label on the border line. Specify a positive integer as the column position from the left. Specify a negative integer to right-align the label. Label is printed on the top border line by default, add

:bottom

to put it on the border line on the bottom. The default value

0 (or

center

) will put the label at the center of the border line.


## LIST SECTION

****-m, --multi***[=MAX]***

Enable multi-select with tab/shift-tab. It optionally takes an integer argument which denotes the maximum number of items that can be selected.

****+m, --no-multi****

Disable multi-select

****--highlight-line****

Highlight the whole current line

****--cycle****

Enable cyclic scroll

****--wrap***[=MODE]***

Enable line wrap.

MODE

can be

char

(default) or

word

.

word

mode wraps lines at word boundaries (spaces and tabs) instead of at arbitrary character positions.

--wrap-word

is a synonym for

--wrap=word

.

****--wrap-sign***=INDICATOR***

Indicator for wrapped lines. The default is '↳ ' or '> ' depending on

--no-unicode

.

****--no-multi-line****

Disable multi-line display of items when using

--read0

****--raw****

Enable raw mode where non-matching items are also displayed in a dimmed color.

****--track****

Make fzf track the current selection when the result list is updated. This can be useful when browsing logs using fzf with sorting disabled. It is not recommended to use this option with

--tac

as the resulting behavior can be confusing.

When **--id-nth** is also set, fzf enables field-based tracking across **reload**s. See **--id-nth** for details.

Without **--id-nth**, **--track** uses index-based tracking that does not persist across reloads.

e.g.

# Index-based tracking (does not persist across reloads)

git log --oneline --graph --color=always | nl |

fzf --ansi --track --no-sort --layout=reverse-list

**# Track by first field (e.g. pod name) across reloads** **kubectl get pods | fzf --track --id-nth 1 --header-lines=1 \** **--bind 'ctrl-r:reload:kubectl get pods'**

****--id-nth=***N[,..]***

Define item identity fields for cross-reload operations. When set, fzf uses the specified fields to identify items across

reload

and

reload-sync

.

With **--track**, fzf extracts the tracking key from the current item using the nth expression and searches for a matching item in the reloaded list. While searching, the UI is blocked (query input and cursor movement are disabled, and the prompt is dimmed). With **reload**, the blocked state clears as soon as the match is found in the stream. With **reload-sync**, the blocked state persists until the entire stream is complete. Press **Escape** or **Ctrl-C** to cancel the blocked state without quitting fzf.

The info line shows **+T*** (or **+t*** for one-off tracking) while the search is in progress.

With **--multi**, selected items are preserved across **reload-sync** by matching their identity fields in the reloaded list.

e.g.

# Track and preserve selections by pod name across reloads

kubectl get pods | fzf --multi --track --id-nth 1 --header-lines=1 \

--bind 'ctrl-r:reload-sync:kubectl get pods'

****--tac****

Reverse the order of the input

e.g.

history | fzf --tac --no-sort

****--gap***[=N]***

Render empty lines between each item

****--gap-line***[=STR]***

The given string will be repeated to draw a horizontal line on each gap (default: '┈' or '-' depending on

--no-unicode

).

****--freeze-left=***N***

Number of fields to freeze on the left.

****--freeze-right=***N***

Number of fields to freeze on the right.

****--keep-right****

Keep the right end of the line visible when it's too long. Effective only when the query string is empty. Use

--freeze-right=1

instead if you want the last field to be always visible even with a non-empty query.

****--scroll-off=***LINES***

Number of screen lines to keep above or below when scrolling to the top or to the bottom (default: 3).

****--no-hscroll****

Disable horizontal scroll

****--hscroll-off=***COLS***

Number of screen columns to keep to the right of the highlighted substring (default: 10). Setting it to a large value will cause the text to be positioned on the center of the screen.

****--jump-labels=***CHARS***

Label characters for

jump

mode.

****--gutter=***CHAR***

Character used for the gutter column (default: '▌' unless

--no-unicode

is given)

****--gutter-raw=***CHAR***

Character used for the gutter column in raw mode (default: '▖' unless

--no-unicode

is given)

****--pointer=***STR***

Pointer to the current line (default: '▌' or '>' depending on

--no-unicode

)

****--marker=***STR***

Multi-select marker (default: '┃' or '>' depending on

--no-unicode

)

****--marker-multi-line=***STR***

Multi-select marker for multi-line entries. 3 elements for top, middle, and bottom. (default: '╻┃╹' or '.|'' depending on

--no-unicode

)

****--ellipsis=***STR***

Ellipsis to show when line is truncated (default: '··')

****--tabstop=***SPACES***

Number of spaces for a tab character (default: 8)

****--scrollbar=***CHAR1[CHAR2]***

Use the given character to render scrollbar. (default: '│' or ':' depending on

--no-unicode

). The optional

CHAR2

is used to render scrollbar of the preview window.

****--no-scrollbar****

Do not display scrollbar. A synonym for

--scrollbar=''

****--list-border***[=STYLE]***

Draw border around the list section.

line

style is not supported for this border.

****--list-label***[=LABEL]***

Label to print on the list border

****--list-label-pos***[=N[:top|bottom]]***

Position of the list label


## INPUT SECTION

****--no-input****

Disable and hide the input section. You can no longer type in queries. To trigger a search, use

search

action. You can later show the input section using

show-input

or

toggle-input

action, and hide it again using

hide-input

, or

toggle-input

.

****--prompt=***STR***

Input prompt (default: '> ')

****--info=***STYLE***

Determines the display style of the finder info. (e.g. match counter, loading indicator, etc.)

**default** On the left end of the horizontal separator **right** On the right end of the horizontal separator **hidden** Do not display finder info **inline** After the prompt with the default prefix ' < ' **inline:PREFIX** After the prompt with a non-default prefix **inline-right** On the right end of the prompt line **inline-right:PREFIX** On the right end of the prompt line with a custom prefix

****--info-command=***COMMAND***

Command to generate the finder info line. The command runs synchronously and blocks the UI until completion, so make sure that it's fast. ANSI color codes are supported.

$FZF_INFO

variable is set to the original info text. For additional environment variables available to the command, see the section ENVIRONMENT VARIABLES EXPORTED TO CHILD PROCESSES.

e.g. **# Prepend the current cursor position in yellow** **fzf --info-command='printf "\x1b[33;1m$FZF_POS\x1b[m/$FZF_INFO 💛"'**

****--no-info****

A synonym for

--info=hidden

****--separator=***STR***

The given string will be repeated to form the horizontal separator on the info line (default: '─' or '-' depending on

--no-unicode

).

ANSI color codes are supported.

****--no-separator****

Do not display horizontal separator on the info line. A synonym for

--separator=''

****--ghost=***TEXT***

Ghost text to display when the input is empty

****--filepath-word****

Make word-wise movements and actions respect path separators. The following actions are affected:

**backward-kill-word** **backward-word** **forward-word** **kill-word**

****--input-border***[=STYLE]***

Draw border around the input section.

line

style draws a single separator line between the input section and the list section.

****--input-label***[=LABEL]***

Label to print on the input border

****--input-label-pos***[=N[:top|bottom]]***

Position of the input label


## PREVIEW WINDOW

****--preview=***COMMAND***

Execute the given command for the current line and display the result on the preview window.

{}

in the command is the placeholder that is replaced to the single-quoted string of the current line. To transform the replacement string, specify field index expressions between the braces (See

FIELD INDEX

EXPRESSION

for the details).

e.g.

fzf --preview='head -$LINES {}'

ls -l | fzf --preview="echo user={3} when={-4..-2}; cat {-1}" --header-lines=1

fzf exports **$FZF_PREVIEW_LINES** and **$FZF_PREVIEW_COLUMNS** so that they represent the exact size of the preview window. (It also overrides **$LINES** and **$COLUMNS** with the same values but they can be reset by the default shell, so prefer to refer to the ones with **FZF_PREVIEW_** prefix.)

fzf also exports **$FZF_PREVIEW_TOP** and **$FZF_PREVIEW_LEFT** so that the preview command can determine the position of the preview window.

A placeholder expression starting with **+** flag will be replaced to the space-separated list of the selected items (or the current item if no selection was made) individually quoted.

e.g. **fzf --multi --preview='head -10 {+}'** **git log --oneline | fzf --multi --preview 'git show {+1}'**

Similarly, a placeholder expression starting with ***** flag will be replaced to the space-separated list of all matched items individually quoted.

Each expression expands to a quoted string, so that it's safe to pass it as an argument to an external command. So you should not manually add quotes around the curly braces. But if you don't want this behavior, you can put **r** flag (raw) in the expression (e.g. **{r}**, **{r1}**, etc). Use it with caution as unquoted output can lead to broken commands.

When using a field index expression, leading and trailing whitespace is stripped from the replacement string. To preserve the whitespace, use the **s** flag.

A placeholder expression with **f** flag is replaced to the path of a temporary file that holds the evaluated list. This is useful when you pass a large number of items and the length of the evaluated string may exceed **ARG_MAX**.

e.g. **# See the sum of all the matched numbers** **# This won't work properly without 'f' flag due to ARG_MAX limit.** **seq 100000 | fzf --preview "awk '{sum+=\$1} END {print sum}' {*f}"**

**# Use {+f} to get the selected items as a line-separated list** **seq 100 | fzf --multi --bind 'enter:become:cat {+f}'**

Also,

* **{q}** is replaced to the current query string * **{q}** can contain field index expressions. e.g. **{q:1}**, **{q:2..}**, etc. * **{n}** is replaced to the zero-based ordinal index of the current item. Use **{+n}** if you want all index numbers when multiple lines are selected.

Note that you can escape a placeholder pattern by prepending a backslash.

Preview window will be updated even when there is no match for the current query if any of the placeholder expressions evaluates to a non-empty string or **{q}** is in the command template.

Since 0.24.0, fzf can render partial preview content before the preview command completes. ANSI escape sequence for clearing the display (**CSI 2 J**) is supported, so you can use it to implement preview window that is constantly updating.

e.g. **fzf --preview 'for i in $(seq 100000); do** **(( i % 200 == 0 )) && printf "\033[2J"** **echo "$i"** **sleep 0.01** **done'**

fzf has experimental support for Kitty graphics protocol and Sixel graphics. The following example uses https://github.com/junegunn/fzf/blob/master/bin/fzf-preview.sh script to render an image using either of the protocols inside the preview window.

e.g. **fzf --preview='fzf-preview.sh {}'**

****--preview-border***[=STYLE]***

Short for

--preview-window=border-STYLE

.

line

style draws a single separator line between the preview window and the rest of the interface.

****--preview-label***[=LABEL]***

Label to print on the horizontal border line of the preview window. Should be used with one of the following

--preview-window

options.

*** border-rounded (default on non-Windows platforms)** *** border-sharp (default on Windows)** *** border-bold** *** border-double** *** border-dashed** *** border-block** *** border-thinblock** *** border-horizontal** *** border-top** *** border-bottom**

****--preview-wrap-sign***=INDICATOR***

Indicator for wrapped lines in the preview window. If not set, the value of

--wrap-sign

is used.

****--preview-label-pos***[=N[:top|bottom]]***

Position of the border label on the border line of the preview window. Specify a positive integer as the column position from the left. Specify a negative integer to right-align the label. Label is printed on the top border line by default, add

:bottom

to put it on the border line on the bottom. The default value 0 (or

center

) will put the label at the center of the border line.

****--preview-window=***[POSITION][,SIZE[%]][,border-STYLE][,[no]wrap][,wrap-word][,[no]follow][,[no]cycle][,[no]info][,[no]hidden][,+SCROLL[OFFSETS][/DENOM]][,~HEADER_LINES][,default][,<SIZE_THRESHOLD(ALTERNATIVE_LAYOUT)]***

POSITION: (default: right)

up

down

left

right

next

Determines the layout of the preview window.

* **next** places the preview window adjacent to the input section, on the list side: above the input in the default layout, below the input in **--layout=reverse**.

* If the argument contains **:hidden**, the preview window will be hidden by default until **toggle-preview** action is triggered.

* If size is given as 0, preview window will not be visible, but fzf will still execute the command in the background.

* Long lines are truncated by default. Line wrap can be enabled with **wrap** flag. **wrap-word** flag enables word-level wrapping, which breaks lines at word boundaries instead of mid-word.

* Preview window will automatically scroll to the bottom when **follow** flag is set, similarly to how **tail -f** works.

e.g.

fzf --preview-window follow --preview 'for i in $(seq 100000); do

echo "$i"

sleep 0.01

(( i % 300 == 0 )) && printf "\033[2J"

done'

* Cyclic scrolling is enabled with **cycle** flag.

* To hide the scroll offset information on the top right corner, specify **noinfo**.

* To change the style of the border of the preview window, specify one of the options for **--border** with **border-** prefix. e.g. **border-rounded** (border with rounded edges, default), **border-sharp** (border with sharp edges), **border-left**, **border-none**, etc.

* In addition to the other border styles, **border-line** style is also supported, which draws a single separator line between the preview window and the rest of the interface.

* **[:+SCROLL[OFFSETS][/DENOM]]** determines the initial scroll offset of the preview window.

- **SCROLL** can be either a numeric integer or a single-field index expression that refers to a numeric integer or {n} to refer to the zero-based ordinal index of the current item.

- The optional **OFFSETS** part is for adjusting the base offset. It should be given as a series of signed integers (**-INTEGER** or **+INTEGER**).

- The final **/DENOM** part is for specifying a fraction of the preview window height.

* **~HEADER_LINES** keeps the top N lines as the fixed header so that they are always visible.

* **default** resets all options previously set to the default.

e.g.

# Non-default scroll window positions and sizes

fzf --preview="head {}" --preview-window=up,30%

fzf --preview="file {}" --preview-window=down,1

# Initial scroll offset is set to the line number of each line of # git grep output *minus* 5 lines (-5) git grep --line-number '' | fzf --delimiter : --preview 'nl {1}' --preview-window '+{2}-5'

# Preview with bat, matching line in the middle of the window below # the fixed header of the top 3 lines # # ~3 Top 3 lines as the fixed header # +{2} Base scroll offset extracted from the second field # +3 Extra offset to compensate for the 3-line header # /2 Put in the middle of the preview area # git grep --line-number '' | fzf --delimiter : \ --preview 'bat --style=full --color=always --highlight-line {2} {1}' \ --preview-window '~3,+{2}+3/2'

# Display top 3 lines as the fixed header fzf --preview 'bat --style=full --color=always {}' --preview-window '~3'

* You can specify an alternative set of options that are used only when the size of the preview window is below a certain threshold. Note that only one alternative layout is allowed.

e.g.

fzf --preview 'cat {}' --preview-window 'right,border-left,<30(up,30%,border-bottom)'


## HEADER

****--header=***STR***

The given string will be printed as the sticky header. The lines are displayed in the given order from top to bottom regardless of

--layout

option, and are not affected by

--with-nth

. ANSI color codes are processed even when

--ansi

is not set.

****--header-lines=***N***

The first N lines of the input are treated as the sticky header. When

--with-nth

is set, the lines are transformed just like the other lines that follow.

****--header-first****

Print header before the prompt line. When both normal header and header lines (

--header-lines

) are present, this applies only to the normal header.

****--header-border***[=STYLE]***

Draw border around the header section.

line

style draws a single separator line between the header window and the list section.

inline

style embeds the header inside the list border frame, joined to the list section by a horizontal separator; it requires a

--list-border

shape that has both top and bottom segments (rounded / sharp / bold / double / dashed / block / thinblock / horizontal) and falls back to

line

otherwise. When the list border also has side segments, the separator joins them with T-junctions;

horizontal

has no side borders, so the separator is drawn without T-junction endpoints. Takes precedence over

--header-first

(the section stays inside the list frame), and when

--header-lines

is also set

--header-lines-border

must also be

inline

.

****--header-label***[=LABEL]***

Label to print on the header border

****--header-label-pos***[=N[:top|bottom]]***

Position of the header label

****--header-lines-border***[=STYLE]***

Display header from

--header-lines

with a separate border. Pass

none

to still separate the header lines but without a border. To combine two headers, use

--no-header-lines-border

.

line

style draws a single separator line between the header lines and the list section.

inline

style embeds the header lines inside the list border frame with a horizontal separator; it requires a

--list-border

shape that has both top and bottom segments, falls back to

line

otherwise.

****--footer=***STR***

The given string will be printed as the sticky footer. The lines are displayed in the given order from top to bottom regardless of

--layout

option, and are not affected by

--with-nth

. ANSI color codes are processed even when

--ansi

is not set.

Draw border around the footer section.

line

style draws a single separator line between the footer and the list section.

inline

style embeds the footer inside the list border frame with a horizontal separator; it requires a

--list-border

shape that has both top and bottom segments and falls back to

line

otherwise.

****--footer-label***[=LABEL]***

Label to print on the footer border

****--footer-label-pos***[=N[:top|bottom]]***

Position of the footer label


## SCRIPTING

****-q, --query=***STR***

Start the finder with the given query

****-1, --select-1****

If there is only one match for the initial query (

--query

), do not start interactive finder and automatically select the only match

****-0, --exit-0****

If there is no match for the initial query (

--query

), do not start interactive finder and exit immediately

****-f, --filter=***STR***

Filter mode. Do not start interactive finder. When used with

--no-sort

, fzf becomes a fuzzy-version of grep.

****--print-query****

Print query as the first line

****--expect=***KEY[,..]***

Comma-separated list of keys that can be used to complete fzf in addition to the default enter key. When this option is set, fzf will print the name of the key pressed as the first line of its output (or as the second line if

--print-query

is also used). The line will be empty if fzf is completed with the default enter key. If

--expect

option is specified multiple times, fzf will expect the union of the keys.

--no-expect

will clear the list.

e.g. **fzf --expect=ctrl-v,ctrl-t,alt-s --expect=f1,f2,~,@**

This option is not compatible with **--bind** on the same key and will take precedence over it. To combine the two, use **print** action.

e.g. **fzf --multi \** **--bind 'enter:print()+accept,ctrl-y:select-all+print(ctrl-y)+accept'**

****--no-clear****

Do not clear finder interface on exit. If fzf was started in full screen mode, it will not switch back to the original screen, so you'll have to manually run

tput rmcup

to return. This option can be used to avoid flickering of the screen when your application needs to start fzf multiple times in order. (Note that in most cases, it is preferable to use

reload

action instead.)

e.g. **foo=$(seq 100 | fzf --no-clear) || (** **# Need to manually switch back to the main screen when cancelled** **tput rmcup** **exit 1** **) && seq "$foo" 100 | fzf**


## KEY/EVENT BINDING

****--bind=***BINDINGS***

Comma-separated list of custom key/event bindings. See

KEY/EVENT BINDINGS

for the details.


## ADVANCED

****--with-shell=STR****

Shell command and flags to start child processes with. On *nix Systems, the default value is

$SHELL -c

if

$SHELL

is set, otherwise

sh -c

. On Windows, the default value is

cmd /s/c

when

$SHELL

is not set.

****--listen[=SOCKET_PATH|[ADDR:]PORT] --listen-unsafe[=[ADDR:]PORT]****

Start HTTP server and listen on the given address or Unix socket. It allows external processes to send actions to perform via POST method and query the program state via GET method. For the argument to be recognized as a socket path, it must have

.sock

extension.

- If the port number is omitted or given as 0, fzf will automatically choose a port and export it as **FZF_PORT** environment variable to the child processes.

- If a Unix socket path is given, fzf will create a Unix domain socket at the given path. The existing file will be removed. The path to the socket file is exported as **FZF_SOCK** environment variable.

- If **FZF_API_KEY** environment variable is set, the server would require sending an API key with the same value in the **x-api-key** HTTP header.

- **FZF_API_KEY** is required for a non-localhost listen address.

- To allow remote process execution, use **--listen-unsafe**.

e.g. **# Start HTTP server on port 6266** **fzf --listen 6266**

# Send action to the server curl -XPOST localhost:6266 -d 'reload(seq 100)+change-prompt(hundred> )'

# Start HTTP server on port 6266 with remote connections allowed # * Listening on non-localhost address requires using an API key export FZF_API_KEY="$(head -c 32 /dev/urandom | base64)" fzf --listen 0.0.0.0:6266

# Send an authenticated action curl -XPOST localhost:6266 -H "x-api-key: $FZF_API_KEY" -d 'change-query(yo)'

# Choose port automatically and export it as $FZF_PORT to the child process fzf --listen --bind 'start:execute-silent:echo $FZF_PORT > /tmp/fzf-port'

# Get program state in JSON format (experimental) # - GET Parameters: # - limit: number of items to return (default: 100) # - offset: number of items to skip (default: 0) curl localhost:6266

# Automatically select items with .txt extension fzf --multi --sync --listen --bind 'load:transform: pos=1 curl -s localhost:$FZF_PORT?limit=1000 | jq -r .matches[].text | while read -r text; do if [[ $text =~ \.txt$ ]]; then echo -n "+pos($pos)+select" fi pos=$((pos + 1)) done echo +first '

Here is an example script that uses a Unix socket instead of a TCP port.

**fzf --listen=/tmp/fzf.sock**

# GET curl --unix-socket /tmp/fzf.sock http

# POST curl --unix-socket /tmp/fzf.sock http -d up

****--threads=***N***

Number of matcher threads to use. The default value is

min(8 * NUM_CPU, 32)

.

****--bench=***DURATION***

Repeatedly run

--filter

for the given duration and print timing statistics. Must be used with

--filter

.

e.g. **cat /usr/share/dict/words | fzf --filter abc --bench 10s**


## DIRECTORY TRAVERSAL

****--walker=[file][,dir][,follow][,hidden]****

Determines the behavior of the built-in directory walker that is used when

$FZF_DEFAULT_COMMAND

is not set. The default value is

file,follow,hidden

.

* **file**: Include files in the search result * **dir**: Include directories in the search result * **hidden**: Include and follow hidden directories * **follow**: Follow symbolic links

****--walker-root=DIR [...]****

List of directory names to start the built-in directory walker. The default value is the current working directory.

****--walker-skip=DIRS****

Comma-separated list of directory names to skip during the directory walk. The default value is

.git,node_modules

.


## HISTORY

****--history=***HISTORY_FILE***

Load search history from the specified file and update the file on completion. When enabled,

CTRL-N

and

CTRL-P

are automatically remapped to

next-history

and

prev-history

.

****--history-size=***N***

Maximum number of entries in the history file (default: 1000). The file is automatically truncated when the number of the lines exceeds the value.

e.g.

gem list | fzf --with-shell 'ruby -e' --preview 'pp Gem::Specification.find_by_name({1})'


## SHELL INTEGRATION

****--bash****

Print script to set up Bash shell integration

e.g. **eval "$(fzf --bash)"**

****--zsh****

Print script to set up Zsh shell integration

e.g. **source <(fzf --zsh)**

****--fish****

Print script to set up Fish shell integration

e.g. **fzf --fish | source**

****--nushell****

Print script to set up Nushell shell integration

e.g. **fzf --nushell | save -f ~/.config/nushell/autoload/_fzf_integration.nu**


## OTHERS

****--no-mouse****

Disable mouse

****--no-unicode****

Use ASCII characters instead of Unicode drawing characters to draw borders, the spinner and the horizontal separator.

****--ambidouble****

Set this option if your terminal displays ambiguous width characters (e.g. box-drawing characters for borders) as 2 columns.


## HELP

****--version****

Display version information and exit

****--help****

Show help message

****--man****

Show man page

# ENVIRONMENT VARIABLES

****FZF_DEFAULT_COMMAND****

Default command to use when input is a TTY device. On *nix systems, fzf runs the command with

$SHELL -c

if

SHELL

is set, otherwise with

sh

-c

, so in this case make sure that the command is POSIX-compliant.

****FZF_DEFAULT_OPTS****

Default options.

e.g.

export FZF_DEFAULT_OPTS="--layout=reverse --border --cycle"

****FZF_DEFAULT_OPTS_FILE****

The location of the file that contains the default options.

e.g.

export FZF_DEFAULT_OPTS_FILE=~/.fzfrc

****FZF_API_KEY****

Can be used to require an API key when using

--listen

option. If not set, no authentication will be required by the server. You can set this value if you need to protect against DNS rebinding and privilege escalation attacks.

# EXIT STATUS

**0** Normal exit **1** No match **2** Error **126** Permission denied error from **become** action **127** Invalid shell command for **become** action **130** Interrupted with **CTRL-C** or **ESC**

# FIELD INDEX EXPRESSION

A field index expression can be a non-zero integer or a range expression ([BEGIN]..[END]). **--nth** and **--with-nth** take a comma-separated list of field index expressions.


## Examples

**1** The 1st field **2** The 2nd field **-1** The last field **-2** The 2nd to last field **3..5** From the 3rd field to the 5th field **2..** From the 2nd field to the last field **..-3** From the 1st field to the 3rd to the last field **..** All the fields

# ENVIRONMENT VARIABLES EXPORTED TO CHILD PROCESSES

fzf exports the following environment variables to its child processes.

**FZF_LINES** Number of lines fzf takes up excluding padding and margin **FZF_COLUMNS** Number of columns fzf takes up excluding padding and margin **FZF_DIRECTION** Direction of the list (**up** or **down**) **FZF_TOTAL_COUNT** Total number of items **FZF_MATCH_COUNT** Number of matched items **FZF_SELECT_COUNT** Number of selected items **FZF_POS** Vertical position of the cursor in the list starting from 1 **FZF_CURRENT_ITEM** Text of the current item (unset if the list is empty) **FZF_WRAP** The line wrapping mode (char, word) when enabled **FZF_QUERY** Current query string **FZF_INPUT_STATE** Current input state (enabled, disabled, hidden) **FZF_NTH** Current --nth option **FZF_WITH_NTH** Current --with-nth option **FZF_PROMPT** Prompt string **FZF_GHOST** Ghost string **FZF_POINTER** Pointer string **FZF_PREVIEW_LABEL** Preview label string **FZF_BORDER_LABEL** Border label string **FZF_LIST_LABEL** List label string **FZF_INPUT_LABEL** Input label string **FZF_HEADER_LABEL** Header label string **FZF_ACTION** The name of the last action performed **FZF_KEY** The name of the last key pressed **FZF_IDLE_TIME** Whole seconds since the last user activity **FZF_IDLE_TIME_MS** Milliseconds since the last user activity **FZF_PORT** Port number when --listen option is used **FZF_SOCK** Unix socket path when --listen option is used **FZF_PREVIEW_TOP** Top position of the preview window **FZF_PREVIEW_LEFT** Left position of the preview window **FZF_PREVIEW_LINES** Number of lines in the preview window **FZF_PREVIEW_COLUMNS** Number of columns in the preview window **FZF_RAW** Only in raw mode. 1 if the current item matches, 0 otherwise

**FZF_CURRENT_ITEM** is omitted when the item contains a NUL byte, because exec(2) cannot pass it.

Unless specified otherwise, fzf will start in "extended-search mode". In this mode, you can specify multiple patterns delimited by spaces, such as: **'wild** **^music .mp3$ sbtrkt !rmx**

You can prepend a backslash to a space (**\**) to match a literal space character.


## Exact-match (quoted)

A term that is prefixed by a single-quote character (**'**) is interpreted as an "exact-match" (or "non-fuzzy") term. fzf will search for the exact occurrences of the string.


## Anchored-match

A term can be prefixed by **^**, or suffixed by **$** to become an anchored-match term. Then fzf will search for the lines that start with or end with the given string. An anchored-match term is also an exact-match term.


## Exact-boundary-match (quoted both ends)

A single-quoted term is interpreted as an "exact-boundary-match". fzf will search for the exact occurrences of the string with both ends at the word boundaries. Unlike in regular expressions, this also sees an underscore as a word boundary. But the words around underscores are ranked lower and appear later in the result than the other words around the other types of word boundaries.

1. xxx foo xxx (highest score) 2. xxx foo_xxx 3. xxx_foo xxx 4. xxx_foo_xxx (lowest score)


## Negation

If a term is prefixed by **!**, fzf will exclude the lines that satisfy the term from the result. In this case, fzf performs exact match by default.


## Exact-match by default

If you don't prefer fuzzy matching and do not wish to "quote" (prefixing with **'**) every word, start fzf with **-e** or **--exact** option. Note that when **--exact** is set, **'**-prefix "unquotes" the term.
