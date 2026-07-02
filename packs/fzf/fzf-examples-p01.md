---
title: "Examples · junegunn/fzf Wiki · GitHub (part 1/2)"
source: https://github.com/junegunn/fzf/wiki/examples
domain: fzf
license: CC-BY-SA-4.0
tags: fzf finder, fuzzy finder, command-line interface, interactive filter
fetched: 2026-07-02
part: 1/2
---

# Examples · junegunn/fzf Wiki · GitHub

junegunn

/

fzf

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 2.8k
- Star

# Examples

Jump to bottom

Edit

New page

dAu6jARL edited this page

Jun 20, 2026

·

363 revisions

*Disclaimer: The examples are maintained by the community and are not thoroughly tested.*

To add a script:

- check it runs on bash and zsh
- add it under an appropriate category in the ToC

# Table of Contents

- General
- Command history
- System
  - i3
  - Copy current item to clipboard
  - Processes
  - dotfiles management
  - Systemctl units
  - man pages
  - Slurm
- Package management
  - Pacman/Yay
  - NPM
  - Homebrew
  - Homebrew Cask
  - DNF
  - Flatpak
  - Conda
- Filesystem navigation
  - Opening files
  - Changing directory
  - Searching file contents
  - cd
    - Integration with zsh-interactive-cd.
    - Interactive cd
  - autojump
    - Integration with autojump
  - z
    - Integration with z.
    - With fz.
    - With fasd.
  - Locate
  - Browsing
- CLI Tools
  - Git
  - jrnl
  - tmux
  - dictcc translation
  - kubectl
  - pass and pass-tomb
- Moving from other tools
  - fzf as selector menu (pipe entries like dmenu/rofi)
  - fzf as rofi replacement
  - fzf as dmenu replacement
- ctags
- ASDF
- v
  - Inspired by v. Opens files in ~/.viminfo
  - With fasd.
- Shell bookmarks
- Google Chrome
  - Browsing history
  - Bookmarks
- mpd
- Readline
- RVM
- Vagrant
- Wrapper
- LastPass CLI
- fzf-marker
- Search for academic pdfs by author, title, keywords, abstract
- BibTeX
- Docker
- buku
- Python Behave BDD
- Transmission
- Todoist CLI
- Emoji

Nice collection at https://github.com/DanielFGray/fzf-scripts

### General

```highlight
# Use fd and fzf to get the args to a command.
# Works only with zsh
# Examples:
# f mv # To move files. You can write the destination after selecting the files.
# f 'echo Selected:'
# f 'echo Selected music:' --extension mp3
# fm rm # To rm files in current directory
f() {
    sels=( "${(@f)$(fd "${fd_default[@]}" "${@:2}"| fzf)}" )
    test -n "$sels" && print -z -- "$1 ${sels[@]:q:q}"
}

# Like f, but not recursive.
fm() f "$@" --max-depth 1

# Deps
alias fz="fzf-noempty --bind 'tab:toggle,shift-tab:toggle+beginning-of-line+kill-line,ctrl-j:toggle+beginning-of-line+kill-line,ctrl-t:top' --color=light -1 -m"
fzf-noempty () {
	local in="$(</dev/stdin)"
	test -z "$in" && (
		exit 130
	) || {
		ec "$in" | fzf "$@"
	}
}
ec () {
	if [[ -n $ZSH_VERSION ]]
	then
		print -r -- "$@"
	else
		echo -E -- "$@"
	fi
}
```

Inspired by the above, suggested by Matt-A-Bennett (not tested in zsh):

```highlight
# Run command/application and choose paths/files with fzf.
# Always return control of the terminal to user (e.g. when opening GUIs).
# The full command that was used will appear in your history just like any
# other (N.B. to achieve this I write the shell's active history to
# ~/.bash_history)
#
# Usage:
# f cd [OPTION]... (hit enter, choose path)
# f cat [OPTION]... (hit enter, choose files)
# f vim [OPTION]... (hit enter, choose files)
# f vlc [OPTION]... (hit enter, choose files)

f() {
    # Store the program
    program="$1"

    # Remove first argument off the list
    shift

    # Store option flags with separating spaces, or just set as single space
    options="$@"
    if [ -z "${options}" ]; then
        options=" "
    else
        options=" $options "
    fi

    # Store the arguments from fzf
    arguments="$(fzf --multi)"

    # If no arguments passed (e.g. if Esc pressed), return to terminal
    if [ -z "${arguments}" ]; then
        return 1
    fi

    # We want the command to show up in our bash history, so write the shell's
    # active history to ~/.bash_history. Then we'll also add the command from
    # fzf, then we'll load it all back into the shell's active history
    history -w

    # ADD A REPEATABLE COMMAND TO THE BASH HISTORY ############################
    # Store the arguments in a temporary file for sanitising before being
    # entered into bash history
    : > /tmp/fzf_tmp
    for file in "${arguments[@]}"; do
        echo "$file" >> /tmp/fzf_tmp
    done

    # Put all input arguments on one line and sanitise the command by putting
    # single quotes around each argument, also first put an extra single quote
    # next to any pre-existing single quotes in the raw argument
    sed -i "s/'/''/g; s/.*/'&'/g; s/\n//g" /tmp/fzf_tmp

    # If the program is on the GUI list, add a '&' to the command history
    if [[ "$program" =~ ^(nautilus|zathura|evince|vlc|eog|kolourpaint)$ ]]; then
        sed -i '${s/$/ \&/}' /tmp/fzf_tmp
    fi

    # Grab the sanitised arguments
    arguments="$(cat /tmp/fzf_tmp)"

    # Add the command with the sanitised arguments to our .bash_history
    echo $program$options$arguments >> ~/.bash_history

    # Reload the ~/.bash_history into the shell's active history
    history -r

    # EXECUTE THE LAST COMMAND IN ~/.bash_history #############################
    fc -s -1

    # Clean up temporary variables
    rm /tmp/fzf_tmp
}
```

### Opening files

```highlight
# fe [FUZZY PATTERN] - Open the selected file with the default editor
#   - Bypass fuzzy finder if there's only one match (--select-1)
#   - Exit if there's no match (--exit-0)
fe() {
  IFS=$'\n' files=($(fzf-tmux --query="$1" --multi --select-1 --exit-0 --preview="bat --color=always {}"))
  [[ -n "$files" ]] && ${EDITOR:-vim} "${files[@]}"
}

# Modified version where you can press
#   - CTRL-O to open with `open` command,
#   - CTRL-E or Enter key to open with the $EDITOR
fo() {
  IFS=$'\n' out=("$(fzf-tmux --query="$1" --exit-0 --expect=ctrl-o,ctrl-e --preview="bat --color=always {}")")
  key=$(head -1 <<< "$out")
  file=$(head -2 <<< "$out" | tail -1)
  if [ -n "$file" ]; then
    [ "$key" = ctrl-o ] && open "$file" || ${EDITOR:-vim} "$file"
  fi
}
```

```highlight
# vf - fuzzy open with vim from anywhere
# ex: vf word1 word2 ... (even part of a file name)
# zsh autoload function
vf() {
  local files

  files=(${(f)"$(locate -Ai -0 $@ | grep -z -vE '~$' | fzf --read0 -0 -1 -m)"})

  if [[ -n $files ]]
  then
     vim -- $files
     print -l $files[1]
  fi
}
```

```highlight
# fuzzy grep open via ag
vg() {
  local file

  file="$(ag --nobreak --noheading $@ | fzf -0 -1 | awk -F: '{print $1}')"

  if [[ -n $file ]]
  then
     vim $file
  fi
}

# fuzzy grep open via ag with line number
vg() {
  local file
  local line

  read -r file line <<<"$(ag --nobreak --noheading $@ | fzf -0 -1 | awk -F: '{print $1, $2}')"

  if [[ -n $file ]]
  then
     vim $file +$line
  fi
}
```

Use `Cmd-k` to open any file and change to any directory, from anywhere: cmdk (Bash code)

### Changing directory

```highlight
# fd - cd to selected directory
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune \
                  -o -type d -print 2> /dev/null | fzf +m) &&
  cd "$dir"
}
```

```highlight
# Another fd - cd into the selected directory
# This one differs from the above, by only showing the sub directories and not
#  showing the directories within those.
fd() {
  DIR=`find * -maxdepth 0 -type d -print 2> /dev/null | fzf-tmux` \
    && cd "$DIR"
}
```

```highlight
# fda - including hidden directories
fda() {
  local dir
  dir=$(find ${1:-.} -type d 2> /dev/null | fzf +m) && cd "$dir"
}
```

```highlight
# fdr - cd to selected parent directory
fdr() {
  local declare dirs=()
  get_parent_dirs() {
    if [[ -d "${1}" ]]; then dirs+=("$1"); else return; fi
    if [[ "${1}" == '/' ]]; then
      for _dir in "${dirs[@]}"; do echo $_dir; done
    else
      get_parent_dirs $(dirname "$1")
    fi
  }
  local DIR=$(get_parent_dirs $(realpath "${1:-$PWD}") | fzf-tmux --tac)
  cd "$DIR"
}
```

```highlight
# cf - fuzzy cd from anywhere
# ex: cf word1 word2 ... (even part of a file name)
# zsh autoload function
cf() {
  local file

  file="$(locate -Ai -0 $@ | grep -z -vE '~$' | fzf --read0 -0 -1)"

  if [[ -n $file ]]
  then
     if [[ -d $file ]]
     then
        cd -- $file
     else
        cd -- ${file:h}
     fi
  fi
}
```

Suggested by @harelba and @dimonomid:

```highlight
# cdf - cd into the directory of the selected file
cdf() {
   local file
   local dir
   file=$(fzf +m -q "$1") && dir=$(dirname "$file") && cd "$dir"
}
```

```highlight
# Another CTRL-T script to select a directory and paste it into line
__fzf_select_dir ()
{
        builtin typeset READLINE_LINE_NEW="$(
                command find -L . \( -path '*/\.*' -o -fstype dev -o -fstype proc \) \
                        -prune \
                        -o -type f -print \
                        -o -type d -print \
                        -o -type l -print 2>/dev/null \
                | command sed 1d \
                | command cut -b3- \
                | env fzf -m
        )"

        if
                [[ -n $READLINE_LINE_NEW ]]
        then
                builtin bind '"\er": redraw-current-line'
                builtin bind '"\e^": magic-space'
                READLINE_LINE=${READLINE_LINE:+${READLINE_LINE:0:READLINE_POINT}}${READLINE_LINE_NEW}${READLINE_LINE:+${READLINE_LINE:READLINE_POINT}}
                READLINE_POINT=$(( READLINE_POINT + ${#READLINE_LINE_NEW} ))
        else
                builtin bind '"\er":'
                builtin bind '"\e^":'
        fi
}

builtin bind -x '"\C-x1": __fzf_select_dir'
builtin bind '"\C-t": "\C-x1\e^\er"'
```

Fuzzy cd for fish shell: https://gist.github.com/rumpelsepp/b1b416f52d6790de1aee

autojump(macOS) + fzf for fish shell: https://gist.github.com/l4u/06502cf680b9a3817efddfb0a9a6ede8

### Searching file contents

```highlight
grep --line-buffered --color=never -r "" * | fzf

# with ag - respects .agignore and .gitignore
ag --nobreak --nonumbers --noheading . | fzf

# using ripgrep combined with preview
# find-in-file - usage: fif <searchTerm>
fif() {
  if [ ! "$#" -gt 0 ]; then echo "Need a string to search for\!"; return 1; fi
  rg --files-with-matches --no-messages "$1" | fzf --preview "highlight -O ansi -l {} 2> /dev/null | rg --colors 'match:bg:yellow' --ignore-case --pretty --context 10 '$1' || rg --ignore-case --pretty --context 10 '$1' {}"
}
```

```highlight
# alternative using ripgrep-all (rga) combined with fzf-tmux preview
# This requires ripgrep-all (rga) installed: https://github.com/phiresky/ripgrep-all
# This implementation below makes use of "open" on macOS, which can be replaced by other commands if needed.
# allows to search in PDFs, E-Books, Office documents, zip, tar.gz, etc. (see https://github.com/phiresky/ripgrep-all)
# find-in-file - usage: fif <searchTerm> or fif "string with spaces" or fif "regex"
fif() {
    if [ ! "$#" -gt 0 ]; then echo "Need a string to search for!"; return 1; fi
    local file
    file="$(rga --max-count=1 --ignore-case --files-with-matches --no-messages "$*" | fzf-tmux +m --preview="rga --ignore-case --pretty --context 10 '"$*"' {}")" && echo "opening $file" && open "$file" || return 1;
}
```

Suggested by @gbstan

```highlight
#!/bin/bash

##
# Interactive search.
# Usage: `ff` or `ff <folder>`.
#
[[ -n $1 ]] && cd $1 # go to provided folder or noop
RG_DEFAULT_COMMAND="rg -i -l --hidden --no-ignore-vcs"

selected=$(
FZF_DEFAULT_COMMAND="rg --files" fzf \
  -m \
  -e \
  --ansi \
  --disabled \
  --reverse \
  --bind "ctrl-a:select-all" \
  --bind "f12:execute-silent:(subl -b {})" \
  --bind "change:reload:$RG_DEFAULT_COMMAND {q} || true" \
  --preview "rg -i --pretty --context 2 {q} {}" | cut -d":" -f1,2
)

[[ -n $selected ]] && subl $selected # open multiple files in editor
```

Suggested by @knoxknox

```highlight
#!/bin/bash
# Interactive search using ag (silver searcher)

[[ -n $1 ]] && cd $1 # go to provided folder or noop
typeset AG_DEFAULT_COMMAND="ag -i -l --hidden"
typeset IFS=$'\n'
typeset selected=($(
      fzf \
      -m \
      -e \
      --ansi \
      --disabled \
      --reverse \
      --print-query \
      --bind "change:reload:$AG_DEFAULT_COMMAND {q} || true" \
      --preview "ag -i --color --context=2 {q} {}"))
[ -n "$selected" ] && ${EDITOR} -c "/\\c${selected[0]}" ${selected[1]}
```

### Command history

```highlight
# fh - repeat history
fh() {
  eval $( ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed -E 's/ *[0-9]*\*? *//' | sed -E 's/\\/\\\\/g')
}
```

```highlight
# fh - repeat history
fh() {
  print -z $( ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed -E 's/ *[0-9]*\*? *//' | sed -E 's/\\/\\\\/g')
}
```

Replacing `eval` with `print -z` will push the arguments onto the editing buffer stack, allowing you to edit the command before running it. It also means the command you run will appear in your history rather than just `fh`. Unfortunately this only works for zsh. See below for solutions working with Bash.

#### With write to terminal capabilities

These have been tested in bash.

```highlight
# fh - repeat history
runcmd (){ perl -e 'ioctl STDOUT, 0x5412, $_ for split //, <>' ; }

fh() {
  ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed -re 's/^\s*[0-9]+\s*//' | runcmd
}

# fhe - repeat history edit
writecmd (){ perl -e 'ioctl STDOUT, 0x5412, $_ for split //, do{ chomp($_ = <>); $_ }' ; }

fhe() {
  ([ -n "$ZSH_NAME" ] && fc -l 1 || history) | fzf +s --tac | sed -re 's/^\s*[0-9]+\s*//' | writecmd
}
```

```highlight
# Another CTRL-R script to insert the selected command from history into the command line/region
__fzf_history ()
{
    builtin history -a;
    builtin history -c;
    builtin history -r;
    builtin typeset \
        READLINE_LINE_NEW="$(
            HISTTIMEFORMAT= builtin history |
            command fzf +s --tac +m -n2..,.. --tiebreak=index --toggle-sort=ctrl-r |
            command sed '
                /^ *[0-9]/ {
                    s/ *\([0-9]*\) .*/!\1/;
                    b end;
                };
                d;
                : end
            '
        )";

        if
                [[ -n $READLINE_LINE_NEW ]]
        then
                builtin bind '"\er": redraw-current-line'
                builtin bind '"\e^": magic-space'
                READLINE_LINE=${READLINE_LINE:+${READLINE_LINE:0:READLINE_POINT}}${READLINE_LINE_NEW}${READLINE_LINE:+${READLINE_LINE:READLINE_POINT}}
                READLINE_POINT=$(( READLINE_POINT + ${#READLINE_LINE_NEW} ))
        else
                builtin bind '"\er":'
                builtin bind '"\e^":'
        fi
}

builtin set -o histexpand;
builtin bind -x '"\C-x1": __fzf_history';
builtin bind '"\C-r": "\C-x1\e^\er"'
```

```highlight
# re-wrote the script above
bind '"\C-r": "\C-x1\e^\er"'
bind -x '"\C-x1": __fzf_history';

__fzf_history ()
{
__ehc $(history | fzf --tac --tiebreak=index | perl -ne 'm/^\s*([0-9]+)/ and print "!$1"')
}

__ehc()
{
if
        [[ -n $1 ]]
then
        bind '"\er": redraw-current-line'
        bind '"\e^": magic-space'
        READLINE_LINE=${READLINE_LINE:+${READLINE_LINE:0:READLINE_POINT}}${1}${READLINE_LINE:+${READLINE_LINE:READLINE_POINT}}
        READLINE_POINT=$(( READLINE_POINT + ${#1} ))
else
        bind '"\er":'
        bind '"\e^":'
fi
}
```

### Processes

```highlight
# fkill - kill process
fkill() {
  local pid
  pid=$(ps -ef | sed 1d | fzf -m | awk '{print $2}')

  if [ "x$pid" != "x" ]
  then
    echo $pid | xargs kill -${1:-9}
  fi
}
```

```highlight
# fkill - kill processes - list only the ones you can kill. Modified the earlier script.
fkill() {
    local pid
    if [ "$UID" != "0" ]; then
        pid=$(ps -f -u $UID | sed 1d | fzf -m | awk '{print $2}')
    else
        pid=$(ps -ef | sed 1d | fzf -m | awk '{print $2}')
    fi

    if [ "x$pid" != "x" ]
    then
        echo $pid | xargs kill -${1:-9}
    fi
}
```

### Systemctl units

The https://github.com/NullSense/fuzzy-sys project implements frequently used systemctl unit file manipulating commands.

### Git

List all available git commands and help with `git-commands`

```highlight
# fbr - checkout git branch
fbr() {
  local branches branch
  branches=$(git --no-pager branch -vv) &&
  branch=$(echo "$branches" | fzf +m) &&
  git checkout $(echo "$branch" | awk '{print $1}' | sed "s/.* //")
}

# fbr - checkout git branch (including remote branches)
fbr() {
  local branches branch
  branches=$(git branch --all | grep -v HEAD) &&
  branch=$(echo "$branches" |
           fzf-tmux -d $(( 2 + $(wc -l <<< "$branches") )) +m) &&
  git checkout $(echo "$branch" | sed "s/.* //" | sed "s#remotes/[^/]*/##")
}

# fbr - checkout git branch (including remote branches), sorted by most recent commit, limit 30 last branches
fbr() {
  local branches branch
  branches=$(git for-each-ref --count=30 --sort=-committerdate refs/heads/ --format="%(refname:short)") &&
  branch=$(echo "$branches" |
           fzf-tmux -d $(( 2 + $(wc -l <<< "$branches") )) +m) &&
  git checkout $(echo "$branch" | sed "s/.* //" | sed "s#remotes/[^/]*/##")
}

# fco - checkout git branch/tag
fco() {
  local tags branches target
  branches=$(
    git --no-pager branch --all \
      --format="%(if)%(HEAD)%(then)%(else)%(if:equals=HEAD)%(refname:strip=3)%(then)%(else)%1B[0;34;1mbranch%09%1B[m%(refname:short)%(end)%(end)" \
    | sed '/^$/d') || return
  tags=$(
    git --no-pager tag | awk '{print "\x1b[35;1mtag\x1b[m\t" $1}') || return
  target=$(
    (echo "$branches"; echo "$tags") |
    fzf --no-hscroll --no-multi -n 2 \
        --ansi) || return
  git checkout $(awk '{print $2}' <<<"$target" )
}

# fco_preview - checkout git branch/tag, with a preview showing the commits between the tag/branch and HEAD
fco_preview() {
  local tags branches target
  branches=$(
    git --no-pager branch --all \
      --format="%(if)%(HEAD)%(then)%(else)%(if:equals=HEAD)%(refname:strip=3)%(then)%(else)%1B[0;34;1mbranch%09%1B[m%(refname:short)%(end)%(end)" \
    | sed '/^$/d') || return
  tags=$(
    git --no-pager tag | awk '{print "\x1b[35;1mtag\x1b[m\t" $1}') || return
  target=$(
    (echo "$branches"; echo "$tags") |
    fzf --no-hscroll --no-multi -n 2 \
        --ansi --preview="git --no-pager log -150 --pretty=format:%s '..{2}'") || return
  git checkout $(awk '{print $2}' <<<"$target" )
}
```

```highlight
# fcoc - checkout git commit
fcoc() {
  local commits commit
  commits=$(git log --pretty=oneline --abbrev-commit --reverse) &&
  commit=$(echo "$commits" | fzf --tac +s +m -e) &&
  git checkout $(echo "$commit" | sed "s/ .*//")
}
```

```highlight
# fshow - git commit browser
fshow() {
  git log --graph --color=always \
      --format="%C(auto)%h%d %s %C(black)%C(bold)%cr" "$@" |
  fzf --ansi --no-sort --reverse --tiebreak=index --bind=ctrl-s:toggle-sort \
      --bind "ctrl-m:execute:
                (grep -o '[a-f0-9]\{7\}' | head -1 |
                xargs -I % sh -c 'git show --color=always % | less -R') << 'FZF-EOF'
                {}
FZF-EOF"
}
```

```highlight
# fshow_name_status - git commit browser with file status
# powered by "--read0" option and Perl.
# delta (git-delta) with 'less -I' is available for 'git show' pager, if possible.
# e.g. query '@2026', '#(', ':A:' may be available for year 2026, ref names, added file.
fshow_name_status() {
  local pager="less -I -R"
  if command -v delta &> /dev/null ; then
    pager="delta --paging always --pager \"$pager\""
  fi
  git log --color=always --name-status --date="format-local:%Y/%m/%d(%a) %T" --format="%x00%C(auto)%H %Creset@%C(cyan)%ad%x01%C(auto)%d%x01%C(magenta) %an <%ae>%x02%C(green)%B%Creset%x03" "$@" |
  perl -0 -ne \
    'if (m/\x01([^\x01]*)\x01/) { $s = $1; $s =~ s/\(/#\(/; $_ =~ s/\x01([^\x01]*)\x01/$s/; };
     if (m/\x02([^\x03]+)\x03/) { $s = $1; $s =~ s/[\r\n]+/ /gi; $_ =~ s/\x02([^\x03]+)\x03/ $s\x03/; };
     if (m/\x03([^\x03]+)$/) { $s = $1; $s =~ s/^([ACDMRTUXB])\S*\s+(\S.+)/\x1B[94m:$1:\x1B[m$2/gm; $s =~ s/^([^*].+)\r?\n/$1 /gm; s/\x03([^\x03]+)$/$s/; };
     s/\r?\n//sg;
     if (m/^.*[^\x00]\x00?$/) { print $_; }' |
  fzf --read0 --wrap --exact --ansi --no-sort --reverse --tiebreak=index --bind=ctrl-s:toggle-sort \
      --bind "ctrl-m:execute:
                (grep -o '[a-f0-9]\{7\}' | head -1 |
                xargs -I % sh -c 'git show --color=always % | $pager') << 'FZF-EOF'
                {}
FZF-EOF"
}
```

Screenshot of **fshow_name_status** is as follows. (20260506-191036-937)

```highlight
alias glNoGraph='git log --color=always --format="%C(auto)%h%d %s %C(black)%C(bold)%cr% C(auto)%an" "$@"'
_gitLogLineToHash="echo {} | grep -o '[a-f0-9]\{7\}' | head -1"
_viewGitLogLine="$_gitLogLineToHash | xargs -I % sh -c 'git show --color=always % | diff-so-fancy'"

# fcoc_preview - checkout git commit with previews
fcoc_preview() {
  local commit
  commit=$( glNoGraph |
    fzf --no-sort --reverse --tiebreak=index --no-multi \
        --ansi --preview="$_viewGitLogLine" ) &&
  git checkout $(echo "$commit" | sed "s/ .*//")
}

# fshow_preview - git commit browser with previews
fshow_preview() {
    glNoGraph |
        fzf --no-sort --reverse --tiebreak=index --no-multi \
            --ansi --preview="$_viewGitLogLine" \
                --header "enter to view, alt-y to copy hash" \
                --bind "enter:execute:$_viewGitLogLine   | less -R" \
                --bind "alt-y:execute:$_gitLogLineToHash | xclip"
}
```

Compare against `master` branch with `git-stack`

```highlight
# fcs - get git commit sha
# example usage: git rebase -i `fcs`
fcs() {
  local commits commit
  commits=$(git log --color=always --pretty=oneline --abbrev-commit --reverse) &&
  commit=$(echo "$commits" | fzf --tac +s +m -e --ansi --reverse) &&
  echo -n $(echo "$commit" | sed "s/ .*//")
}
```

```highlight
# fstash - easier way to deal with stashes
# type fstash to get a list of your stashes
# enter shows you the contents of the stash
# ctrl-d shows a diff of the stash against your current HEAD
# ctrl-b checks the stash out as a branch, for easier merging
fstash() {
  local out q k sha
  while out=$(
    git stash list --pretty="%C(yellow)%h %>(14)%Cgreen%cr %C(blue)%gs" |
    fzf --ansi --no-sort --query="$q" --print-query \
        --expect=ctrl-d,ctrl-b);
  do
    mapfile -t out <<< "$out"
    q="${out[0]}"
    k="${out[1]}"
    sha="${out[-1]}"
    sha="${sha%% *}"
    [[ -z "$sha" ]] && continue
    if [[ "$k" == 'ctrl-d' ]]; then
      git diff $sha
    elif [[ "$k" == 'ctrl-b' ]]; then
      git stash branch "stash-$sha" $sha
      break;
    else
      git stash show -p $sha
    fi
  done
}
```

Create a gitignore file from gitignore.io:

https://gist.github.com/phha/cb4f4bb07519dc494609792fb918e167

```highlight
# fgst - pick files from `git status -s`
is_in_git_repo() {
  git rev-parse HEAD > /dev/null 2>&1
}

fgst() {
  # "Nothing to see here, move along"
  is_in_git_repo || return

  local cmd="${FZF_CTRL_T_COMMAND:-"command git status -s"}"

  eval "$cmd" | FZF_DEFAULT_OPTS="--height ${FZF_TMUX_HEIGHT:-40%} --reverse $FZF_DEFAULT_OPTS $FZF_CTRL_T_OPTS" fzf -m "$@" | while read -r item; do
    echo "$item" | awk '{print $2}'
  done
  echo
}
```

Interactive fixup of a commit

```
function git-fixup () {
  git ll -n 20 | fzf | cut -f 1 | xargs git commit --no-verify --fixup
}
```

Usage:

```
git fixup
git rebase -i master --autosquash
```

Article on fixup and autosquash.

The shell plugin `forgit` implemented the frequently used commands with some improves(support `bash`, `zsh` and `fish`):

(forgit-ga)

(forgit-glo)

(forgit-gi)

Watch GitHub actions for the current branch, with selection via fzf

```highlight
# gh-watch -- watch the current actions
gh-watch() {
    gh run list \
      --branch $(git rev-parse --abbrev-ref HEAD) \
      --json status,name,databaseId |
      jq -r '.[] | select(.status != "completed") | (.databaseId | tostring) + "\t" + (.name)' |
      fzf -1 -0 | awk '{print $1}' | xargs gh run watch
}
```

### jrnl

Suggested by @windisch.

```highlight
# fjrnl - Search JRNL headlines
fjrnl() {
  title=$(jrnl --short | fzf --tac --no-sort) &&
  jrnl -on "$(echo $title | cut -c 1-16)" $1
  }
```

### ctags

```highlight
# ftags - search ctags
ftags() {
  local line
  [ -e tags ] &&
  line=$(
    awk 'BEGIN { FS="\t" } !/^!/ {print toupper($4)"\t"$1"\t"$2"\t"$3}' tags |
    cut -c1-80 | fzf --nth=1,2
  ) && ${EDITOR:-vim} $(cut -f3 <<< "$line") -c "set nocst" \
                                      -c "silent tag $(cut -f2 <<< "$line")"
}
```

```highlight
# ftags - search ctags with preview
# only works if tags-file was generated with --excmd=number
ftags() {
  local line
  [ -e tags ] &&
  line=$(
    awk 'BEGIN { FS="\t" } !/^!/ {print toupper($4)"\t"$1"\t"$2"\t"$3}' tags |
    fzf \
      --nth=1,2 \
      --with-nth=2 \
      --preview-window="50%" \
      --preview="bat {3} --color=always | tail -n +\$(echo {4} | tr -d \";\\\"\")"
  ) && ${EDITOR:-vim} $(cut -f3 <<< "$line") -c "set nocst" \
                                      -c "silent tag $(cut -f2 <<< "$line")"
}
```

### tmux

```highlight
# zsh; needs setopt re_match_pcre. You can, of course, adapt it to your own shell easily.
tmuxkillf () {
    local sessions
    sessions="$(tmux ls|fzf --exit-0 --multi)"  || return $?
    local i
    for i in "${(f@)sessions}"
    do
        [[ $i =~ '([^:]*):.*' ]] && {
            echo "Killing $match[1]"
            tmux kill-session -t "$match[1]"
        }
    done
}
```

```highlight
# tm - create new tmux session, or switch to existing one. Works from within tmux too. (@bag-man)
# `tm` will allow you to select your tmux session via fzf.
# `tm irc` will attach to the irc session (if it exists), else it will create it.

tm() {
  [[ -n "$TMUX" ]] && change="switch-client" || change="attach-session"
  if [ $1 ]; then
    tmux $change -t "$1" 2>/dev/null || (tmux new-session -d -s $1 && tmux $change -t "$1"); return
  fi
  session=$(tmux list-sessions -F "#{session_name}" 2>/dev/null | fzf --exit-0) &&  tmux $change -t "$session" || echo "No sessions found."
}
```

```highlight
# fs [FUZZY PATTERN] - Select selected tmux session
#   - Bypass fuzzy finder if there's only one match (--select-1)
#   - Exit if there's no match (--exit-0)
fs() {
  local session
  session=$(tmux list-sessions -F "#{session_name}" | \
    fzf --query="$1" --select-1 --exit-0) &&
  tmux switch-client -t "$session"
}
```

```highlight
# ftpane - switch pane (@george-b)
ftpane() {
  local panes current_window current_pane target target_window target_pane
  panes=$(tmux list-panes -s -F '#I:#P - #{pane_current_path} #{pane_current_command}')
  current_pane=$(tmux display-message -p '#I:#P')
  current_window=$(tmux display-message -p '#I')

  target=$(echo "$panes" | grep -v "$current_pane" | fzf +m --reverse) || return

  target_window=$(echo $target | awk 'BEGIN{FS=":|-"} {print$1}')
  target_pane=$(echo $target | awk 'BEGIN{FS=":|-"} {print$2}' | cut -c 1)

  if [[ $current_window -eq $target_window ]]; then
    tmux select-pane -t ${target_window}.${target_pane}
  else
    tmux select-pane -t ${target_window}.${target_pane} &&
    tmux select-window -t $target_window
  fi
}

# In tmux.conf
# bind-key 0 run "tmux split-window -l 12 'bash -ci ftpane'"
```

To search for windows and show which is currently active, add ftwind somewhere in your path. Then add eg `bind-key f run -b ftwind` to your `tmux.conf`.

### Select pane

Allows you to select pane with `bind-key + 0`. Requires `ftpane()` function.

```highlight
# Index starts from 1
set-option -g base-index 1

# select-pane (@george-b)
bind-key 0 run "tmux split-window -p 40 'bash -ci ftpane'"
```

### Search entire file system (ALT-`)

ALT-` key will split the current window and start fzf for the entire list of files. The selected files will be pasted on to the original window.

```highlight
# fzf-locate
bind-key -n 'M-`' run "tmux split-window -p 40 'tmux send-keys -t #{pane_id} \"$(locate / | fzf -m | paste -sd\\  -)\"'"
```

### kubectl

Add support for kubectl completion with fzf

```highlight
# BASH
# Tested kubectl version `v1.23.6`
# Make all kubectl completion fzf
command -v fzf >/dev/null 2>&1 && {
	source <(kubectl completion bash | sed 's#"${requestComp}" 2>/dev/null#"${requestComp}" 2>/dev/null | head -n -1 | fzf  --multi=0 #g')
}

# ZSH
# Make all kubectl completion fzf
command -v fzf >/dev/null 2>&1 && {
	source <(kubectl completion zsh | sed 's#${requestComp} 2>/dev/null#${requestComp} 2>/dev/null | head -n -1 | fzf  --multi=0 #g')
}

# FISH
# Tested kubectl version `v1.34.1`
type -q fzf >/dev/null 2>&1 && {
    kubectl completion fish | sed 's#-a \'\$__kubectl_comp_results\'$#-a \'(printf "%s\\\n" $__kubectl_comp_results | fzf --multi=0)\'#g' | source
}
```

Put this in your `.bashrc` or `.zshrc` instead of:

```highlight
source <(kubectl completion bash)
```

It will source kubectl completion with fzf support Examples:

```highlight
# Will open fzf windows with k8s objects starting with `p`
kubectl get p<tab><tab>

# Will open fzf list of pods.
kubectl get pods <tab><tab>
```

Notes:

This will make all kubectl commands use fzf for completion. This was tested with (should work with all commands):

- version `v1.23.6`
- bash
- zsh
- commands:
  - get
  - get pods
  - describe
  - describe pods
  - logs

Suggested by: @shmuel-raichman

### pass and pass-tomb

The below passfzf script is a wrapper for `pass` (the UNIX password store) and `pass-tomb`. Check the source repository for any updates.

```highlight
#!/usr/bin/env bash
# This script unlocks the pass tomb, if any, and then usess fzf to find
# passwords and copy, show, delete, rename and duplicate them, as well as
# to add or generate new passwords, and synchronize them (with git).
# Dependencies: fd, fzf, pass
# Optional dependencies: git, pass-tomb
#
# MIT License, Copyright © [2022] Mathieu Laparie <mlaparie [at] disr [dot] it>

store="$HOME/.password-store/"
swapfile="/swap/swapfile" # Set path to any swapfile not listed in /etc/fstab

# Open pass tomb, if any
if [[ -e "$HOME/.password.tomb" ]]; then
    sudo swapoff -a && sudo swapoff "${swapfile}" 2> /dev/null
    pass open 2> /dev/null
fi

# Select pass entry
main() {
    while :; do
        clear
        selection=$(fd .gpg ~/.password-store/ -d 8 \
                      | fzf --query "${tmp}" \
                            --prompt="# " \
                            --ansi \
                            --extended \
                            --no-border \
                            --with-nth 5.. \
                            --delimiter "/" \
                            --layout=reverse-list \
                            --no-multi \
                            --cycle \
                            --header='
Ret: copy, C-s: show, C-e: edit, C-r: rename, C-d: duplicate,
C-a: add, C-g: generate and copy new password, C-t: trash
C-p: git pull, M-p: git push, C-c/C-q/Esc: clear query or exit' \
                            --margin='1,2,1,2' \
                            --color='16,gutter:-1' \
                            --bind="tab:down" \
                            --bind="btab:up" \
                            --bind="ctrl-s:execute(echo 'show' > /tmp/passfzfarg)+accept" \
                            --bind="ctrl-e:execute(echo 'edit' > /tmp/passfzfarg)+accept" \
                            --bind="ctrl-r:execute(echo 'mv' > /tmp/passfzfarg)+accept" \
                            --bind="ctrl-d:execute(echo 'cp' > /tmp/passfzfarg)+accept" \
                            --bind="ctrl-a:execute(echo 'add' > /tmp/passfzfarg)+print-query" \
                            --bind="ctrl-g:execute(echo 'generate --clip' > /tmp/passfzfarg)+print-query" \
                            --bind="ctrl-t:execute(echo 'rm' > /tmp/passfzfarg)+accept" \
                            --bind="ctrl-p:abort+execute(echo 'git pull' > /tmp/passfzfarg)" \
                            --bind="alt-p:abort+execute(echo 'git push -u --all' > /tmp/passfzfarg)" \
                            --bind="ctrl-c:execute(echo 'quit' > /tmp/passfzfarg)+cancel" \
                            --bind="ctrl-q:execute(echo 'quit' > /tmp/passfzfarg)+cancel" \
                            --bind="esc:execute(echo 'quit' > /tmp/passfzfarg)+cancel")

        if [[ -f "/tmp/passfzfarg" ]]; then
            arg=$(cat /tmp/passfzfarg)
            rm /tmp/passfzfarg
        else
            arg="show --clip"
        fi

        if ! [[ -v "$selection" ]]; then
            clear
            case "$arg" in
                add)
                    printf "\033[0;32mNew password Directory/Name:\033[0m ${selection}"
                    if [[ -n "$selection" ]]; then
                        printf "\033[0;32m\nPress Return to confirm or type new Directory/Name:\033[0m "
                    fi
                    read -r
                    tmp="${REPLY:=$selection}"
                    pass ${arg} "${tmp}"
                    tmp="${selection:=$tmp}"
                    continue
                    ;;
                mv | cp)
                    tmp=${selection::-4} && tmp=${tmp#"$store"}
                    printf "\033[0;32m\nNew Directory/Name to ${arg} '${tmp}' to:\033[0m "
                    read -r
                    if [[ -n "$REPLY" ]]; then
                        pass ${arg} "${tmp}" "${REPLY}"
                    fi
                    tmp="${REPLY:=$tmp}"
                    continue
                    ;;
                "generate --clip")
                    printf "\033[0;32mNew password Directory/Name:\033[0m ${selection}"
                    if [[ -n "$selection" ]]; then
                        printf "\033[0;32m\nPress Return to confirm or type new Directory/Name:\033[0m "
                    fi
                    read -r
                    tmp="${REPLY:=$selection}"
                    printf "\033[0;32mNumber of characters:\033[0m "
                    read -r
                    pass ${arg} --in-place "${tmp}" "${REPLY}" \
                        2> /dev/null || pass ${arg} "${tmp}" "${REPLY}"
                    tmp="${selection:=$tmp}"
                    printf "\nPress any key to continue. "
                    read -rsn1
                    continue
                    ;;
                quit)
                    pkill -P $$
                    return
                    ;;
                *)
                    if [[ -n "$selection" ]]; then
                        tmp=${selection::-4} && tmp=${tmp#"$store"}
                        pass ${arg} "${tmp}"
                    else
                        pass ${arg}
                    fi
                    printf "\nPress any key to continue. "
                    read -rsn1
                    continue
                    ;;
            esac
        fi
    done
}

main

# Close pass tomb, if any
if [[ -e "$HOME/.password.tomb" ]]; then
    printf "\n"
    pass close
    sudo swapon -a && sudo swapon "${swapfile}" 2> /dev/null
fi

printf "\nPress any key to quit. " && read -rsn1
```

### ASDF

```highlight
# Install one or more versions of specified language
# e.g. `vmi rust` # => fzf multimode, tab to mark, enter to install
# if no plugin is supplied (e.g. `vmi<CR>`), fzf will list them for you
# Mnemonic [V]ersion [M]anager [I]nstall
vmi() {
  local lang=${1}

  if [[ ! $lang ]]; then
    lang=$(asdf plugin-list | fzf)
  fi

  if [[ $lang ]]; then
    local versions=$(asdf list-all $lang | fzf --tac --no-sort --multi)
    if [[ $versions ]]; then
      for version in $(echo $versions);
      do; asdf install $lang $version; done;
    fi
  fi
}
```

```highlight
# Remove one or more versions of specified language
# e.g. `vmi rust` # => fzf multimode, tab to mark, enter to remove
# if no plugin is supplied (e.g. `vmi<CR>`), fzf will list them for you
# Mnemonic [V]ersion [M]anager [C]lean
vmc() {
  local lang=${1}

  if [[ ! $lang ]]; then
    lang=$(asdf plugin-list | fzf)
  fi

  if [[ $lang ]]; then
    local versions=$(asdf list $lang | fzf -m)
    if [[ $versions ]]; then
      for version in $(echo $versions);
      do; asdf uninstall $lang $version; done;
    fi
  fi
}
```

### Homebrew

```highlight
# Install (one or multiple) selected application(s)
# using "brew search" as source input
# mnemonic [B]rew [I]nstall [P]ackage
bip() {
  local inst=$(brew search "$@" | fzf -m)

  if [[ $inst ]]; then
    for prog in $(echo $inst);
    do; brew install $prog; done;
  fi
}
```

```highlight
# Update (one or multiple) selected application(s)
# mnemonic [B]rew [U]pdate [P]ackage
bup() {
  local upd=$(brew leaves | fzf -m)

  if [[ $upd ]]; then
    for prog in $(echo $upd);
    do; brew upgrade $prog; done;
  fi
}
```

```highlight
# Delete (one or multiple) selected application(s)
# mnemonic [B]rew [C]lean [P]ackage (e.g. uninstall)
bcp() {
  local uninst=$(brew leaves | fzf -m)

  if [[ $uninst ]]; then
    for prog in $(echo $uninst);
    do; brew uninstall $prog; done;
  fi
}
```

```highlight
# filename: bi
#!/usr/bin/env zsh
# Fully manage brew installation and suppression, and then some.
# needs zsh, jq, bat
# Inspired by:
# - https://github.com/raycast/extensions/tree/main/extensions/brew
# - https://github.com/junegunn/fzf/wiki/examples#dnf

readonly wait_click="echo $'\n\e[34mPress any key to continue...' && read -rsk 1"
readonly jq_all='
	(. | map(.cask_tokens) | flatten | map(split("/")[-1] + " (cask)"))[]
	, (. | map(.formula_names) | flatten)[]
'

readonly jq_installed='(.formulae[] | .name), (.casks[] | .token + " (cask)")'

readonly tmp_file="$(mktemp)"
trap "rm -f $tmp_file" EXIT

readonly reload="reload%case \$(cat $tmp_file) in
	install) { echo Install mode; brew tap-info --json --installed | jq --raw-output '$jq_all' | sort } ;;
	*) { echo Remove mode; brew info --json=v2 --installed | jq --raw-output '$jq_installed' | sort } ;;
esac%"

readonly state="cat $tmp_file"

readonly nextstate="execute-silent%case \$(cat $tmp_file) in install) echo rm > $tmp_file ;; *) echo install > $tmp_file ;; esac%"

readonly bold="\e[1m"
readonly reset="\e[0m"
readonly italic="\e[3m"
readonly gray="\e[30m"
readonly c="\e[1;36m"
readonly d="\e[1;37m"

readonly help="\
\
${bold}${c}[${d}B${c}]${d}rew ${c}[${d}I${c}]${d}nteractive${reset}

${italic}Tab${reset}     Switch between install mode and remove mode
${italic}Enter${reset}   Select formula or cask for installation or deletion (depends on mode)

${italic}ctrl-s${reset}  Show formula or cask installation [s]ource code
${italic}ctrl-j${reset}  Show formula or cask [J]SON information
${italic}crtl-e${reset}  [E]dit formula or cask source code

${italic}?${reset}       Help (this page)
${italic}ESC${reset}     Quit
