---
title: "Getting Started · tmux/tmux Wiki · GitHub (part 2/2)"
source: https://github.com/tmux/tmux/wiki/Getting-Started
domain: tmux
license: CC-BY-SA-4.0
tags: tmux multiplexer, terminal multiplexer, terminal sessions, pane splitting
fetched: 2026-07-02
part: 2/2
---

# Getting Started · tmux/tmux Wiki · GitHub

```
:move-window -kt999
```

If there are gaps in the window list, the indexes can be renumbered with the `-r` flag to `move-window`. For example, this will change a window list of 0, 1, 3, 999 into 0, 1, 2, 3:

```
:movew -r
```

#### Resizing and zooming panes

Panes may be resized in small steps with `C-b C-Left`, `C-b C-Right`, `C-b C-Up` and `C-b C-Down` and in larger steps with `C-b M-Left`, `C-b M-Right`, `C-b M-Up` and `C-b M-Down`. These use the `resize-pane` command.

A single pane may be temporarily made to take up the whole window with `C-b z`, hiding any other panes. Pressing `C-b z` again puts the pane and window layout back to how it was. This is called zooming and unzooming. A window where a pane has been zoomed is marked with a `Z` in the status line. Commands that change the size or position of panes in a window automatically unzoom the window.

#### Window layouts

The panes in a window may be automatically arranged into one of several named layouts, these may be rotated between with the `C-b Space` key binding or chosen directly with `C-b M-1`, `C-b M-2` and so on.

The available layouts are:

| Name | Key | Description |
|---|---|---|
| even-horizontal | `C-b M-1` | Spread out evenly across |
| even-vertical | `C-b M-2` | Spread out evenly up and down |
| main-horizontal | `C-b M-3` | One large pane at the top, the rest spread out evenly across |
| main-vertical | `C-b M-4` | One large pane on the left, the rest spread out evenly up and down |
| tiled | `C-b M-5` | Tiled in the same number of rows as columns |

#### Copy and paste

tmux has its own copy and paste system. A piece of copied text is called a paste buffer. Text is copied using copy mode, entered with `C-b [`, and the most recently copied text is pasted into the active pane with `C-b ]`.

Paste buffers can be given names but by default they are assigned a name by tmux, such as `buffer0` or `buffer1`. Buffers like this are called automatic buffers and at most 50 are kept - once there are 50 buffers, the oldest is removed when another is added. If a buffer is given a name, it is called a named buffer; named buffers are not deleted no matter how many there are.

It is possible to configure tmux to send any copied text to the system clipboard: this document explains the different ways to configure this.

Copy mode freezes any output in a pane and allows text to be copied. View mode (described earlier) is a read-only form of copy mode.

Like the command prompt, copy mode uses keys similar to *emacs(1)*; however, if the `VISUAL` or `EDITOR` environment variables are set to something containing `vi`, then *vi(1)*-style keys are used instead. The following keys are some of those available in copy mode with *emacs(1)* keys:

| Key | Action |
|---|---|
| `Up`, `Down`, `Left`, `Right` | Move the cursor |
| `C-Space` | Start a selection |
| `C-w` | Copy the selection and exit copy mode |
| `q` | Exit copy mode |
| `C-g` | Stop selecting without copying, or stop searching |
| `C-a` | Move the cursor to the start of the line |
| `C-e` | Move the cursor to the end of the line |
| `C-r` | Search interactively backwards |
| `M-f` | Move the cursor to the next word |
| `M-b` | Move the cursor to the previous word |

A full list of keys for both *vi(1)* and *emacs(1)* is available in the manual page.

Once some text is copied, the most recent may be pasted with `C-b ]` or an older buffer pasted by using buffer mode, entered with `C-b =`. Buffer mode is similar to client mode and tree mode and offers a list of buffers together with a preview of their contents. As well as the navigation and tagging keys used in tree mode and client mode, buffer mode supports the following keys:

| Key | Function |
|---|---|
| `Enter` | Paste selected buffer |
| `p` | Paste selected buffer, same as `Enter` |
| `P` | Paste tagged buffers |
| `d` | Delete selected buffer |
| `D` | Delete tagged buffers |

A buffer may be renamed using the `set-buffer` command. The `-b` flag gives the existing buffer name and `-n` the new name. This converts it into a named buffer. For example, to rename `buffer0` to `mybuffer` from the command prompt:

```
:setb -bbuffer0 -nmybuffer
```

`set-buffer` can also be used to create buffers. To create a buffer called `foo` with text `bar`:

```
:setb -bfoo bar
```

`load-buffer` will load a buffer from a file:

```
:loadb -bbuffername ~/a/file
```

`set-buffer` or `load-buffer` without `-b` creates an automatic buffer.

An existing buffer can be saved to a file with `save-buffer`:

```
:saveb -bbuffer0 ~/saved_buffer
```

#### Finding windows and panes

`C-b f` prompts for some text and then enters tree mode with a filter to show only panes where that text appears in the visible content or title of the pane or in the window name. If panes are found, only those panes appear in the tree, and the text `filter: active` is shown above the preview. If no panes are found, all panes are shown in the tree and the text `filter: no matches` appears above the preview.

#### Using the mouse

tmux has rich support for the mouse. It can be used to change the active pane or window, to resize panes, to copy text, or to choose items from menus.

Support for the mouse is enabled with the `mouse` option; options and the configuration file are described in detail in the next section. To turn the mouse on from the command prompt, use the `set-option` command:

```
:set -g mouse on
```

Once the mouse is enabled:

- Pressing the left button on a pane will make that pane the active pane.
- Pressing the left button on a window name on the status line will make that the current window.
- Dragging with the left button on a pane border resizes the pane.
- Dragging with the left button inside a pane selects text; the selected text is copied when the mouse is released.
- Pressing the right button on a pane opens a menu with various commands. When the mouse button is released, the selected command is run with the pane as target. Each menu item also has a key shortcut shown in brackets.
- Pressing the right button on a window or on the session name on the status line opens a similar menu for the window or session.

### Configuring tmux

#### The configuration file

When the tmux server is started, tmux runs a file called `.tmux.conf` in the user's home directory. This file contains a list of tmux commands which are executed in order. It is important to note that `.tmux.conf` is *only* run when the server is started, not when a new session is created.

A different configuration file may be run from `.tmux.conf` or from a running tmux server using the `source-file` command, for example to run `.tmux.conf` again from a running server using the command prompt:

```
:source ~/.tmux.conf
```

Commands in a configuration file appear one per line. Any lines starting with `#` are comments and are ignored:

```
# This is a comment - the command below turns the status line off
set -g status off
```

Lines in the configuration file are processed similar to the shell, for example:

- Arguments may be enclosed in `'` or `"` to include spaces, or spaces may be escaped. These four lines do the same thing: `set -g status-left "hello word" set -g status-left "hello\ word" set -g status-left 'hello word' set -g status-left hello\ word`
- But escaping doesn't happen inside `'`s. The string here is `hello\ world` not `hello world`: `set -g status-left 'hello\ word'`
- `~` is expanded to the home directory (except inside `'`s): `source ~/myfile`
- Environment variables can be set and are also expanded (but not inside `'`s): `MYFILE=myfile source "~/$MYFILE"` Any variables set in the configuration file will be passed on to new panes created inside tmux.
- A few special characters like `\n` (newline) and `\t` (tab) are replaced. A literal `\` must be given as `\\`.

Although tmux configuration files have some features similar to the shell, they are not shell scripts and cannot use shell constructs like `$()`.

#### Key bindings

tmux key bindings are changed using the `bind-key` and `unbind-key` commands. Each key binding in tmux belongs to a named key table. There are four default key tables:

- The `root` table contains key bindings for keys pressed without the prefix key.
- The `prefix` table contains key bindings for keys pressed after the prefix key, like those mentioned so far in this document.
- The `copy-mode` table contains key bindings for keys used in copy mode with *emacs(1)*-style keys.
- The `copy-mode-vi` table contains key bindings for keys used in copy mode with *vi(1)*-style keys.

All the key bindings or those for a single table can be listed with the `list-keys` command. By default, this shows the keys as a series of `bind-key` commands. The `-T` flag gives the key table to show and the `-N` flag shows the key help, like the `C-b ?` key binding.

For example to list only keys in the `prefix` table:

```
$ tmux lsk -Tprefix
bind-key    -T prefix C-b     send-prefix
bind-key    -T prefix C-o     rotate-window
...
```

Or:

```
$ tmux lsk -Tprefix -N
C-b     Send the prefix key
C-o     Rotate through the panes
...
```

`bind-key` commands can be used to set a key binding, either interactively or most commonly from the configuration file. Like `list-keys`, `bind-key` has a `-T` flag for the key table to use. If `-T` is not given, the key is put in the `prefix` table; the `-n` flag is a shorthand for `-Troot` to use the `root` table.

For example, the `list-keys` command shows that `C-b 9` changes to window 9 using the `select-window` command:

```
$ tmux lsk -Tprefix 9
bind-key -T prefix 9 select-window -t :=9
```

A similar key binding to make `C-b M-0` change to window 10 can be added like this:

```
bind M-0 selectw -t:=10
```

The `-t` flag to `select-window` specifies the target window. In this example, the `:` means the target is a window and `=` means the name must match `10` exactly. Targets are documented further in the COMMANDS section of the manual page.

The `unbind-key` command removes a key binding. Like `bind-key` it has `-T` and `-n` flags for the key table. It is not necessary to remove a key binding before binding it again, `bind-key` will replace any existing key binding. `unbind-key` is necessary only to completely remove a key binding:

```
unbind M-0
```

#### Copy mode key bindings

Copy mode key bindings are set in the `copy-mode` and `copy-mode-vi` key tables. Copy mode has a separate set of commands which are passed using the `-X` flag to the `send-keys` command, for example the copy mode `start-of-line` command moves the cursor to the start of the line and is bound to `C-a` in the `copy-mode` key table:

```
$ tmux lsk -Tcopy-mode C-a
bind-key -T copy-mode C-a send-keys -X start-of-line
```

A full list of copy mode commands is available in the manual page. Here is a selection:

| Command | *emacs(1)* | *vi(1)* | Description |
|---|---|---|---|
| begin-selection | C-Space | Space | Start selection |
| cancel | q | q | Exit copy mode |
| clear-selection | C-g | Escape | Clear selection |
| copy-pipe |   |   | Copy and pipe to the command in the first argument |
| copy-selection-and-cancel | M-w | Enter | Copy the selection and exit copy mode |
| cursor-down | Down | j | Move the cursor down |
| cursor-left | Left | h | Move the cursor left |
| cursor-right | Right | l | Move the cursor right |
| cursor-up | Up | k | Move the cursor up |
| end-of-line | C-e | $ | Move the cursor to the end of the line |
| history-bottom | M-> | G | Move to the bottom of the history |
| history-top | M-< | g | Move to the top of the history |
| middle-line | M-r | M | Move to middle line |
| next-word-end | M-f | e | Move to the end of the next word |
| page-down | PageDown | C-f | Page down |
| page-up | PageUp | C-b | Page up |
| previous-word | M-b | b | Move to the previous word |
| rectangle-toggle | R | v | Toggle rectangle selection |
| search-again | n | n | Repeat the last search |
| search-backward |   | ? | Search backwards, the first argument is the search term |
| search-backward-incremental | C-r |   | Search backwards incrementally, usually used with the `-i` flag to `command-prompt` |
| search-forward |   | / | Search forwards, the first argument is the search term |
| search-forward-incremental | C-s |   | Search forwards incrementally |
| search-reverse | N | N | Repeat the last search but reverse the direction |
| start-of-line | C-a | 0 | Move to the start of the line |

#### Types of option

tmux is configured by setting options. There are several types of options:

- Server options which affect the entire server.
- Session options which affect one or all sessions.
- Window options which affect one or all windows.
- Pane options which affect one or all panes.
- User options which are not used by tmux but are reserved for the user.

Session and window options have both a global set of options and a set for each session or window. If the option is not present in the session or window set, the global option is used. Pane options are similar except the window options are also checked.

When configuring tmux, it is most common to set server options and global session or window options. This document only covers these.

#### Showing options

Options are displayed using the `show-options` command. The `-g` flag shows global options. It can show server, session or window options:

- `-s` shows server options:

```
$ tmux show -s
backspace C-?
buffer-limit 50
...
```

- `-g` with no other flags shows global session options:

```
$ tmux show -g
activity-action other
assume-paste-time 1
...
```

- `-g` and `-w` together show global window options:

```
$ tmux show -wg
aggressive-resize off
allow-rename off
...
```

An individual option value may be shown by giving its name to `show-option`. When an option name is given, it is not necessary to give `-s` or `-w` because tmux can work it out from the option name. For example, to show the `status` option:

```
$ tmux show -g status
status on
```

#### Changing options

Options are set or unset using the `set-option` command. Like `show-option`, it is not necessary to give `-s` or `-w` because tmux can work out it out from the option name. `-g` is necessary to set global session or window options; for server options it does nothing.

To set the `status` option:

```
set -g status off
```

Or the `default-terminal` option:

```
set -s default-terminal 'tmux-256color'
```

The `-u` flag unsets an option. Unsetting a global option restores it to its default value, for example:

```
set -gu status
```

#### Formats

Many options make use of formats. Formats provide a powerful syntax to configure how text appears, based on various attributes of the tmux server, a session, window or pane. Formats are enclosed in `#{}` in string options or as a single uppercase letter like `#F`. This is the default `status-right` with several formats:

```
$ tmux show -s status-right
status-right "#{?window_bigger,[#{window_offset_x}#,#{window_offset_y}] ,}\"#{=21:pane_title}\" %H:%M %d-%b-%y"
```

Formats are described in this document and in the manual page.

#### Embedded commands

Some options may contain embedded shell commands. This is limited to the status line options such as `status-left`. Embedded shell commands are enclosed in `#()`. They can either:

1. Print a line and exit, in which case the line will be shown in the status line and the command run at intervals to update it. For example: `set -g status-left '#(uptime)'` The maximum interval is set by the `status-interval` option but commands may also be run sooner if tmux needs. Commands will not be run more than once a second.
2. Stay running and print a line whenever needed, for example: `set -g status-left '#(while :; do uptime; sleep 1; done)'`

Note that it is not usually necessary to use an embedded command for the date and time since tmux will expand the date formats like `%H` and `%S` itself in the status line options. If a command like *date(1)* is used, any `%`s must be doubled as `%%`.

#### Colours and styles

tmux allows the colour and attribute of text to be configured with a simple syntax, this is known as the style. There are two places styles appear:

- In options, such as `status-style`.
- Enclosed in `#[]` in an option value, this is called an embedded style (see the next section).

A style has a number of terms separated by spaces or commas, the most useful are:

- `default` uses the default colour; this must appear on its own. The default colour is often set by another option, for example for embedded styles in the `status-left` option, it is `status-style`.
- `bg` sets the background colour. The colour is also given, for example `bg=red`.
- `fg` sets the foreground colour. Like `bg`, the colour is given: `fg=green`.
- `bright` or `bold`, `underscore`, `reverse`, `italics` set the attributes. These appear alone, such as: `bright,reverse`.

Colours may be one of `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white` for the standard terminal colours; `brightred`, `brightyellow` and so on for the bright variants; `colour0` to `colour255` for the colours from the 256-colour palette; `default` for the default colour; or a hexadecimal RGB colour such as `#882244`.

The remaining style terms are described in the manual page.

For example, to set the status line background to blue using the `status-style` option:

```
set -g status-style 'bg=blue'
```

#### Embedded styles

Embedded styles are included inside another option in between `#[` and `]`. Each changes the style of following text until the next embedded style or the end of the text.

For example, to put some text in red and blue in `status-left`:

```
set -g status-left 'default #[fg=red] red #[fg=blue] blue'
```

Because this is long it is also necessary to also increase the `status-left-length` option:

```
set -g status-left-length 100
```

Or embedded styles can be used conditionally, for example to show `P` in red if the prefix has been pressed or in the default style if not:

```
set -g status-left '#{?client_prefix,#[bg=red],}P#[default] [#{session_name}] '
```

#### List of useful options

This is a short list of the most commonly used tmux options, apart from style options:

| Option | Type | Description |
|---|---|---|
| `base-index` | session | If set, then windows indexes start from this instead of from 0 |
| `buffer-limit` | server | The maximum number of automatic buffers to keep, the default is 50 |
| `default-terminal` | server | The default value of the `TERM` environment variable inside tmux |
| `display-panes-time` | window | The time in milliseconds the pane numbers are shown for `C-b q` |
| `display-time` | session | The time in milliseconds for which messages on the status line are shown |
| `escape-time` | server | The time tmux waits after receiving an `Escape` key to see if it is part of a longer key sequence |
| `focus-events` | server | Whether focus key sequences are sent by tmux when the active pane changes and when received from the outside terminal if it supports them |
| `history-limit` | session | The maximum number of lines kept in the history for each pane |
| `mode-keys` | window | Whether *emacs(1)* or *vi(1)* key bindings are used in copy mode |
| `mouse` | session | If the mouse is enabled |
| `pane-border-status` | window | Whether a status line appears in every pane border: `top` or `bottom` |
| `prefix` | session | The prefix key, the default is `C-b` |
| `remain-on-exit` | window | Whether panes are automatically killed when the program running in them exits |
| `renumber-windows` | session | If `on`, windows are automatically renumbered to close any gaps in the window list |
| `set-clipboard` | server | Whether tmux should attempt to set the external *X(7)* clipboard when text is copied and if the outside terminal supports it |
| `set-titles` | session | If `on`, tmux will set the title of the outside terminal |
| `status` | session | Whether the status line is visible |
| `status-keys` | session | Whether *emacs(1)* or *vi(1)* key bindings are used at the command prompt |
| `status-interval` | session | The maximum time in seconds before the status line is redrawn |
| `status-position` | session | The position of the status line: `top` or `bottom` |
| `synchronize-panes` | window | If `on`, typing in any pane in the window is sent to all panes in the window - care should be taken with this option! |
| `terminal-overrides` | server | Any capabilities tmux should override from the `TERM` given for the outside terminal |

#### List of style and format options

This is a list of the most commonly used tmux style and format options:

| Option | Type | Description |
|---|---|---|
| `display-panes-active-colour` | session | The style of the active pane number for `C-b q` |
| `display-panes-colour` | session | The style of the pane numbers, apart from the active pane for`C-b q` |
| `message-style` | session | The style of messages shown on the status line and of the command prompt |
| `mode-style` | window | The style of the selection in copy mode |
| `pane-active-border-style` | window | The style of the active pane border |
| `pane-border-format` | window | The format of text that appears in the pane border status line if `pane-border-status` is set |
| `pane-border-style` | window | The style of the pane borders, apart from the active pane |
| `status-left-length` | session | The maximum length of the status line left |
| `status-left-style` | session | The style of the status line left |
| `status-left` | session | The format of the text in the status line left |
| `status-right-length` | session | The maximum length of the status line right |
| `status-right-style` | session | The style of the status line right |
| `status-right` | session | The format of the text in the status line right |
| `status-style` | session | The style of the status line as a whole, parts may be overridden by more specific options like `status-left-style` |
| `window-active-style` | window | The style of the default colour in the active pane in the window |
| `window-status-current-format` | window | The format of the current window in the window list |
| `window-status-current-style` | window | The style of the current window in the window list |
| `window-status-format` | window | The format of windows in the window list, apart from the current window |
| `window-status-separator` | window | The separator between windows in the window list |
| `window-status-style` | window | The style of windows in the window list, apart from the current window |
| `window-style` | window | The style of the default colour of panes in the window, apart from the active pane |

### Common configuration changes

This section shows examples of some common configuration changes for `.tmux.conf`.

#### Changing the prefix key

The prefix key is set by the `prefix` option. The `C-b` key is also bound to the `send-prefix` command in the prefix key table so pressing `C-b` twice sends it through to the active pane. To change to `C-a`:

```
set -g prefix C-a
unbind C-b
bind C-a send-prefix
```

#### Customizing the status line

There are many options for customizing the status line. The simplest options are:

- Turn the status line off: `set -g status off`
- Move it to the top: `set -g status-position top`
- Set the background colour to red: `set -g status-style bg=red`
- Change the text on the right to the time only: `set -g status-right '%H:%M'`
- Underline the current window: `set -g window-status-current-style 'underscore'`

#### Configuring the pane border

The pane border colours may be set:

```
set -g pane-border-style fg=red
set -g pane-active-border-style 'fg=red,bg=yellow'
```

Each pane may be given a status line with the `pane-border-status` option, for example to show the pane title in bold:

```
set -g pane-border-status top
set -g pane-border-format '#[bold]#{pane_title}#[default]'
```

#### *vi(1)* key bindings

tmux supports key bindings based on *vi(1)* for copy mode and the command prompt. There are two options that set the key bindings:

1. `mode-keys` sets the key bindings for copy mode. If this is set to `vi`, then the `copy-mode-vi` key table is used in copy mode; otherwise the `copy-mode` key table is used.
2. `status-keys` sets the key bindings for the command prompt.

If either of the `VISUAL` or `EDITOR` environment variables are set to something containing `vi` (such as `vi`, `vim`, `nvi`) when the tmux server is first started, both of these options are set to `vi`.

To set both to use *vi(1)* keys:

```
set -g mode-keys vi
set -g status-keys vi
```

#### Mouse copying behaviour

When dragging the mouse to copy text, tmux copies and exits copy mode when the mouse button is released. Alternative behaviours are configured by changing the `MouseDragEnd1Pane` key binding. The three most useful are:

1. Do not copy or clear the selection or exit copy mode when the mouse is released. The keyboard must be used to copy the selection:

```
unbind -Tcopy-mode MouseDragEnd1Pane
```

1. Copy and clear the selection but do not exit copy mode:

```
bind -Tcopy-mode MouseDragEnd1Pane send -X copy-selection
```

1. Copy but do not clear the selection:

```
bind -Tcopy-mode MouseDragEnd1Pane send -X copy-selection-no-clear
```

### Other features

tmux has a large set of features and commands not mentioned in this document, many allowing powerful scripting. Here is a list of some that may be worth further reading:

- Alerts: `monitor-activity`, `monitor-bell`, `monitor-silence`, `activity-action`, `bell-action` and other options.
- Options for individual session, windows and panes.
- Moving panes with `join-pane` and `break-pane`.
- Sending keys to panes with `send-keys`.
- The command prompt `history-file` option.
- Saved layout strings with `select-layout`.
- Command sequences (separated by `;`): `select-window; kill-window`.
- Configuration file syntax: `{}`, `%if` and so on.
- Mouse key bindings: `MouseDown1Pane` and so on.
- Locking: `lock-command`, `lock-after-time` and other options.
- Capturing pane content with `capture-pane` and piping with `pipe-pane`.
- Linking windows: the `link-window` command.
- Session groups: the `-t` flag to `new-session`.
- Respawing window and panes with `respawn-window` and `respawn-pane`.
- Custom menus with the `display-menu` command and custom prompts with `command-prompt` and `confirm-before`.
- Different key tables: `bind-key` and the `-T` flag to `switch-client`.
- Empty panes: the `split-window` with an empty command and `-I` to `display-message`.
- Hooks: `set-hook` and `show-hooks`.
- Synchronization for scripts with `wait-for`.
