---
title: "Examples · junegunn/fzf Wiki · GitHub (part 2/2)"
source: https://github.com/junegunn/fzf/wiki/examples
domain: fzf
license: CC-BY-SA-4.0
tags: fzf finder, fuzzy finder, command-line interface, interactive filter
fetched: 2026-07-02
part: 2/2
---

# Examples · junegunn/fzf Wiki · GitHub

It is also advised you use auto-updates, this can be done with:

    brew autoupdate start --upgrade --cleanup --enable-notification

"

echo install > $tmp_file

{ echo "Install mode (? for help)"; brew tap-info --json --installed | jq --raw-output "$jq_all" | sort } |
	fzf --reverse --header-lines=1  --header-first --prompt="$ " \
		--bind="enter:execute(
			if [[ '{2}' == '(cask)' ]]; then
				brew \$($state) --cask {1}
			else
				brew \$($state) {1}
			fi
			$wait_click)+$reload" \
		--bind='ctrl-s:preview(
			bat --color=always $(brew edit --print-path {1}) --style=header
		)' \
		--bind="ctrl-j:preview:brew info --json=v2 {1} | jq '
			(.formulae + .casks)[0] | with_entries(select(try (.value | length > 0)))
		' | bat --plain --language=json --color=always" \
		--bind="ctrl-e:execute:
			EDITOR='code --wait' brew edit {1}
			bat --color=always --language=markdown --plain <<-MD
				To install the formulae (or cask) you edited with your changes, use:

				    brew reinstall --build-from-source {1}
			MD
			$wait_click" \
		--bind="tab:$nextstate+$reload" \
		--bind="?:preview:printf '$help'" \
		--preview='brew info {1} | bat --color=always --language=Markdown --style=plain' \
		--preview-window='bottom,wrap,<13(right)'
```

### Homebrew Cask

```highlight
# Install or open the webpage for the selected application
# using brew cask search as input source
# and display a info quickview window for the currently marked application
install() {
    local token
    token=$(brew search --casks "$1" | fzf-tmux --query="$1" +m --preview 'brew info {}')

    if [ "x$token" != "x" ]
    then
        echo "(I)nstall or open the (h)omepage of $token"
        read input
        if [ $input = "i" ] || [ $input = "I" ]; then
            brew install --cask $token
        fi
        if [ $input = "h" ] || [ $input = "H" ]; then
            brew home $token
        fi
    fi
}
```

```highlight
# Uninstall or open the webpage for the selected application
# using brew list as input source (all brew cask installed applications)
# and display a info quickview window for the currently marked application
uninstall() {
    local token
    token=$(brew list --casks | fzf-tmux --query="$1" +m --preview 'brew info {}')

    if [ "x$token" != "x" ]
    then
        echo "(U)ninstall or open the (h)omepae of $token"
        read input
        if [ $input = "u" ] || [ $input = "U" ]; then
            brew uninstall --cask $token
        fi
        if [ $input = "h" ] || [ $token = "h" ]; then
            brew home $token
        fi
    fi
}
```

### DNF

Interactively Install, Remove, Upgrade and Fuzzy search DNF packages using fzf

```highlight
#!/usr/bin/bash
readonly basename="$(basename "$0")"

if ! hash fzf &> /dev/null; then
    printf 'Error: Missing dep: fzf is required to use %s.\n' "${basename}" >&2
    exit 64
fi

#Colors
declare -r esc=$'\033'
declare -r BLUE="${esc}[1m${esc}[34m"
declare -r RED="${esc}[31m"
declare -r GREEN="${esc}[32m"
declare -r YELLOW="${esc}[33m"
declare -r CYAN="${esc}[36m"
# Base commands
readonly QRY="dnf --cacheonly --quiet repoquery "
readonly PRVW="dnf --cacheonly --quiet --color=always info"
readonly QRY_PRFX='  '
readonly QRY_SFFX=' > '
# Install mode
readonly INS_QRYS="${QRY} --qf '${CYAN}%{name}'"
readonly INS_PRVW="${PRVW}"
readonly INS_PRMPT="${CYAN}${QRY_PRFX}Install packages${QRY_SFFX}"
# Remove mode
readonly RMV_QRYS="${QRY} --installed --qf '${RED}%{name}'"
readonly RMV_PRVW="${PRVW} --installed"
readonly RMV_PRMPT="${RED}${QRY_PRFX}Remove packages${QRY_SFFX}"
# Remove-userinstalled mode
readonly RUI_QRYS="${QRY} --userinstalled --qf '${YELLOW}%{name}'"
readonly RUI_PRVW="${PRVW} --installed"
readonly RUI_PRMPT="${YELLOW}${QRY_PRFX}Remove User-Installed${QRY_SFFX}"
# Updates mode
readonly UPD_QRY="${QRY} --upgrades --qf '${GREEN}%{name}'"
readonly UPD_QRYS="if [[ $(${UPD_QRY} | wc -c) -ne 0 ]]; then ${UPD_QRY}; else echo ${GREEN}No updates available.; echo Try refreshing metadata cache...; fi"
readonly UPD_PRVW="${PRVW}"
readonly UPD_PRMPT="${GREEN}${QRY_PRFX}Upgrade packages${QRY_SFFX}"

mapfile -d '' fhelp <<-EOF

        "${basename}"
        Interactive package manager for Fedora

        Alt-i       Install mode (default)
        Alt-r       Remove mode
        Alt-e       Remove User-Installed mode
        Alt-u       Updates mode
        Alt-m       Update package metadata cache

        Enter       Confirm selection
        Tab         Mark package ()
        Shift-Tab   Unmark package
        Ctrl-a      Select all

        ?           Help (this page)
        ESC         Quit
EOF

declare tmp_file
if tmp_file="$(mktemp --tmpdir "${basename}".XXXXXX)"; then
    printf 'in' > "${tmp_file}" &&
    SHELL='/bin/bash' \
    FZF_DEFAULT_COMMAND="${INS_QRYS}" \
	fzf \
    --ansi \
	--multi \
	--query=$* \
	--header=" ${basename} | Press Alt+? for help or ESC to quit" \
	--header-first \
	--prompt="${INS_PRMPT}" \
	--marker=' ' \
	--preview-window='right,67%,wrap' \
	--preview="${INS_PRVW} {1}" \
	--bind="enter:execute(if grep -q 'in' \"${tmp_file}\"; then sudo dnf install {+};
        elif grep -q 'rm' \"${tmp_file}\"; then sudo dnf remove {+}; \
        elif grep -q 'up' \"${tmp_file}\"; then sudo dnf upgrade {+}; fi; \
        read -s -r -n1 -p $'\n${BLUE}Press any key to continue...' && printf '\n')" \
	--bind="alt-i:unbind(alt-i)+reload(${INS_QRYS})+change-preview(${INS_PRVW} {1})+change-prompt(${INS_PRMPT})+execute-silent(printf 'in' > \"${tmp_file}\")+first+rebind(alt-r,alt-e,alt-u)" \
	--bind="alt-r:unbind(alt-r)+reload(${RMV_QRYS})+change-preview(${RMV_PRVW} {1})+change-prompt(${RMV_PRMPT})+execute-silent(printf 'rm' > \"${tmp_file}\")+first+rebind(alt-i,alt-e,alt-u)" \
	--bind="alt-e:unbind(alt-e)+reload(${RUI_QRYS})+change-preview(${RUI_PRVW} {1})+change-prompt(${RUI_PRMPT})+execute-silent(printf 'rm' > \"${tmp_file}\")+first+rebind(alt-i,alt-r,alt-u)" \
	--bind="alt-u:unbind(alt-u)+reload(${UPD_QRYS})+change-preview(${UPD_PRVW} {1})+change-prompt(${UPD_PRMPT})+execute-silent(printf 'up' > \"${tmp_file}\")+first+rebind(alt-i,alt-r,alt-e)" \
	--bind="alt-m:execute(sudo dnf makecache;read -s -r -n1 -p $'\n${BLUE}Press any key to continue...' && printf '\n')" \
	--bind="alt-?:preview(printf \"${fhelp[0]}\")" \
	--bind="ctrl-a:select-all"

    rm -f "${tmp_file}" &> /dev/null
else
    printf 'Error: Failed to create tmp file. $TMPDIR (or /tmp if $TMPDIR is unset) may not be writable.\n' >&2
    exit 65
fi
```

### Flatpak

#### flatpak-widget (for zsh)

```highlight
# CLR=$(for i in {0..7}; do echo "tput setaf $i"; done)
BLK=\$(tput setaf 0); RED=\$(tput setaf 1); GRN=\$(tput setaf 2); YLW=\$(tput setaf 3); BLU=\$(tput setaf 4);
MGN=\$(tput setaf 5); CYN=\$(tput setaf 6); WHT=\$(tput setaf 7); BLD=\$(tput bold); RST=\$(tput sgr0);

AWK_VAR="awk -v BLK=${BLK} -v RED=${RED} -v GRN=${GRN} -v YLW=${YLW} -v BLU=${BLU} -v MGN=${MGN} -v CYN=${CYN} -v WHT=${WHT} -v BLD=${BLD} -v RST=${RST}"

# Searches only from flathub repository
fzf-flatpak-install-widget() {
  flatpak remote-ls flathub --cached --columns=app,name,description \
  | awk -v cyn=$(tput setaf 6) -v blu=$(tput setaf 4) -v bld=$(tput bold) -v res=$(tput sgr0) \
  '{
    app_info="";
    for(i=2;i<=NF;i++){
      app_info=cyn app_info" "$i
    };
    print blu bld $2" -" res app_info "|" $1
    }' \
  | column -t -s "|" -R0 \
  | fzf \
    --ansi \
    --with-nth=1.. \
    --prompt="Install > " \
    --preview-window "nohidden,40%,<50(down,50%,border-rounded)" \
    --preview "flatpak --system remote-info flathub {-1} | $AWK_VAR -F\":\" '{print YLW BLD \$1 RST WHT \$2}'" \
    --bind "enter:execute(flatpak install flathub {-1})" # when pressed enter it doesn't showing the key pressed but it is reading the input
  zle reset-prompt
}
bindkey '^[f^[i' fzf-flatpak-install-widget #alt-f + alt-i
zle -N fzf-flatpak-install-widget

fzf-flatpak-uninstall-widget() {
  touch /tmp/uns
  flatpak list --columns=application,name \
  | awk -v cyn=$(tput setaf 6) -v blu=$(tput setaf 4) -v bld=$(tput bold) -v res=$(tput sgr0)  \
  '{
    app_id="";
    for(i=2;i<=NF;i++){
      app_id" "$i
    };
    print bld cyn $2 " - " res blu $1
   }' \
  | column -t \
  | fzf \
    --ansi \
    --with-nth=1.. \
    --prompt="  Uninstall > " \
    --header="M-u: Uninstall | M-r: Run" \
    --header-first \
    --preview-window "nohidden,50%,<50(up,50%,border-rounded)" \
    --preview  "flatpak info {3} | $AWK_VAR -F\":\" '{print RED BLD  \$1 RST \$2}'" \
    --bind "alt-r:change-prompt(Run > )+execute-silent(touch /tmp/run && rm -r /tmp/uns)" \
    --bind "alt-u:change-prompt(Uninstall > )+execute-silent(touch /tmp/uns && rm -r /tmp/run)" \
    --bind "enter:execute(
    if [ -f /tmp/uns ]; then
      flatpak uninstall {3};
    elif [ -f /tmp/run ]; then
      flatpak run {3};
    fi
    )" # same as the install one but when pressed  entered the message is something like this
# "Proceed with these changes to the system installation? [Y/n]:" but it will uninstall the selected app weird but idk y
  rm -f /tmp/{uns,run} &> /dev/null
  zle reset-prompt
}
bindkey '^[f^[u' fzf-flatpak-uninstall-widget #alt-f + alt-u
zle -N fzf-flatpak-uninstall-widget
```

### Conda

#### conda-activate (for bash)

Fuzzy conda environment selection with python version display and `conda tree leaves` preview.

(image)

```highlight
fzf-conda-activate () {
    choice=(
        $(
            conda env list |
            sed 's/\*/ /;1,2d' |
            xargs -I {} bash -c '
                name_path=( {} );
                py_version=( $(${name_path[1]}/bin/python --version) );
                echo ${name_path[0]} ${py_version[1]} ${name_path[1]}
            ' |
            column -t |
            fzf --layout=reverse \
                --info=inline \
                --border=rounded \
                --height=40 \
                --preview-window="right:30%" \
                --preview-label=" conda tree leaves " \
                --preview=$'
                    conda tree -p {3} leaves |
                    perl -F\'[^\\w-_]\' -lae \'print for grep /./, @F;\' |
                    sort
                '
        )
    )
    [[ -n "$choice" ]] && conda activate "$choice"
}
```

### v

#### Inspired by v. Opens files in ~/.viminfo

```highlight
# v - open files in ~/.viminfo
v() {
  local files
  files=$(grep '^>' ~/.viminfo | cut -c3- |
          while read line; do
            [ -f "${line/\~/$HOME}" ] && echo "$line"
          done | fzf-tmux -d -m -q "$*" -1) && vim ${files//\~/$HOME}
}
```

#### With fasd.

Suggested by @epiloque

```highlight
v() {
  local file
  file="$(fasd -Rfl "$1" | fzf -1 -0 --no-sort +m)" && vi "${file}" || return 1
}
```

Suggested by @mazinbokhari

```
# fasd & fzf change directory - open best matched file using `fasd` if given argument, filter output of `fasd` using `fzf` else
v() {
    [ $# -gt 0 ] && fasd -f -e ${EDITOR} "$*" && return
    local file
    file="$(fasd -Rfl "$1" | fzf -1 -0 --no-sort +m)" && vi "${file}" || return 1
}
```

### cd

#### Integration with zsh-interactive-cd.

Fish like interactive tab completion for cd in zsh.

(zsh-interactive-cd-demo)

#### Interactive cd

Suggested by @mgild Like normal cd but opens an interactive navigation window when called with no arguments. For ls, use -FG instead of --color=always on osx.

```highlight
function cd() {
    if [[ "$#" != 0 ]]; then
        builtin cd "$@";
        return
    fi
    while true; do
        local lsd=$(echo ".." && ls -p | grep '/$' | sed 's;/$;;')
        local dir="$(printf '%s\n' "${lsd[@]}" |
            fzf --reverse --preview '
                __cd_nxt="$(echo {})";
                __cd_path="$(echo $(pwd)/${__cd_nxt} | sed "s;//;/;")";
                echo $__cd_path;
                echo;
                ls -p --color=always "${__cd_path}";
        ')"
        [[ ${#dir} != 0 ]] || return 0
        builtin cd "$dir" &> /dev/null
    done
}
```

### autojump

#### Integration with autojump

like normal autojump when used with arguments but displays an fzf prompt when used without

```highlight
j() {
    local preview_cmd="ls {2..}"
    if command -v exa &> /dev/null; then
        preview_cmd="exa -l {2}"
    fi

    if [[ $# -eq 0 ]]; then
                 cd "$(autojump -s | sort -k1gr | awk -F : '$1 ~ /[0-9]/ && $2 ~ /^\s*\// {print $1 $2}' | fzf --height 40% --reverse --inline-info --preview "$preview_cmd" --preview-window down:50% | cut -d$'\t' -f2- | sed 's/^\s*//')"
    else
        cd $(autojump $@)
    fi
}
```

### z

#### Integration with z.

like normal z when used with arguments but displays an fzf prompt when used without.

```highlight
unalias z 2> /dev/null
z() {
  [ $# -gt 0 ] && _z "$*" && return
  cd "$(_z -l 2>&1 | fzf --height 40% --nth 2.. --reverse --inline-info +s --tac --query "${*##-* }" | sed 's/^[0-9,.]* *//')"
}
```

Here is another version that also supports relaunching z with the arguments for the previous command as the default input by using zz

```highlight
unalias z
z() {
  if [[ -z "$*" ]]; then
    cd "$(_z -l 2>&1 | fzf +s --tac | sed 's/^[0-9,.]* *//')"
  else
    _last_z_args="$@"
    _z "$@"
  fi
}

zz() {
  cd "$(_z -l 2>&1 | sed 's/^[0-9,.]* *//' | fzf -q "$_last_z_args")"
}
```

Since z is not very optimal located on a qwerty keyboard I have these aliased as j and jj

```highlight
alias j=z
alias jj=zz
```

#### With fz.

It's yet another z integration. In this version, fuzzy search is enabled with tab completion.

(fz-demo)

#### With fasd.

Suggested by @l4u and @epiloque

```highlight
z() {
  local dir
  dir="$(fasd -Rdl "$1" | fzf -1 -0 --no-sort +m)" && cd "${dir}" || return 1
}
```

Suggested by @mazinbokhari

```
# fasd & fzf change directory - jump using `fasd` if given argument, filter output of `fasd` using `fzf` else
z() {
    [ $# -gt 0 ] && fasd_cd -d "$*" && return
    local dir
    dir="$(fasd -Rdl "$1" | fzf -1 -0 --no-sort +m)" && cd "${dir}" || return 1
}
```

### Shell bookmarks

Yet another useful application for `fzf`: shell bookmarks. It looks as follows: (cdg_demo)

See complete article for details: Fuzzy bookmarks for your shell

### Google Chrome

#### Browsing history

OSX/Linux Version:

```highlight
# c - browse chrome history
c() {
  local cols sep google_history open
  cols=$(( COLUMNS / 3 ))
  sep='{::}'

  if [ "$(uname)" = "Darwin" ]; then
    google_history="$HOME/Library/Application Support/Google/Chrome/Default/History"
    open=open
  else
    google_history="$HOME/.config/google-chrome/Default/History"
    open=xdg-open
  fi
  cp -f "$google_history" /tmp/h
  sqlite3 -separator $sep /tmp/h \
    "select substr(title, 1, $cols), url
     from urls order by last_visit_time desc" |
  awk -F $sep '{printf "%-'$cols's  \x1b[36m%s\x1b[m\n", $1, $2}' |
  fzf --ansi --multi | sed 's#.*\(https*://\)#\1#' | xargs $open > /dev/null 2> /dev/null
}
```

Windows Version:

```highlight
Function c() {
  $Columns = [int]((get-host).ui.rawui.WindowSize.Width / 3)
  $Separator ='{::}'
  $History = "$env:USERPROFILE\AppData\Local\Google\Chrome\User Data\Default\History"
  $TempFile = New-TemporaryFile
  $Query = "select substr(title, 1, $Columns), url from urls order by last_visit_time desc"
  Copy-Item $History -Destination $TempFile
  @(sqlite3 -separator "$Separator" "$TempFile" "$Query") |
  ForEach-Object {
    $Title, $Url = ($_ -split $Separator)[0, 1]
    "$($Title.PadRight($Columns))  `e[36m$Url`e[0m"
  } | fzf --ansi --multi | ForEach-Object{start-process "chrome.exe" ($_ -replace '.*(https*://)', '$1'),'--profile-directory="Default"'}
}
```

#### Bookmarks

Chrome Bookmarks browser with jq for OS X

```
# b - browse chrome bookmarks
b() {
     bookmarks_path=~/Library/Application\ Support/Google/Chrome/Default/Bookmarks

     jq_script='
        def ancestors: while(. | length >= 2; del(.[-1,-2]));
        . as $in | paths(.url?) as $key | $in | getpath($key) | {name,url, path: [$key[0:-2] | ancestors as $a | $in | getpath($a) | .name?] | reverse | join("/") } | .path + "/" + .name + "\t" + .url'

    jq -r "$jq_script" < "$bookmarks_path" \
        | sed -E $'s/(.*)\t(.*)/\\1\t\x1b[36m\\2\x1b[m/g' \
        | fzf --ansi \
        | cut -d$'\t' -f2 \
        | xargs open
}
```

Chrome Bookmarks browser with jq for Windows

```
# b - browse chrome bookmarks
Function b() {
  $Bookmarks = "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Bookmarks"

  $JqScript=@"
     def ancestors: while(. | length >= 2; del(.[-1,-2]));
     . as `$in | paths(.url?) as `$key | `$in | getpath(`$key) | {name,url, path: [`$key[0:-2] | ancestors as `$a | `$in | getpath(`$a) | .name?] | reverse | join(\`"/\`") } | .path + \`"/\`" + .name + \`"|\`" + .url
"@

     Get-Content "$Bookmarks" | jq -r "$JqScript" `
     | ForEach-Object {
       $_ -replace "(.*)\|(.*)", "`$1`t`e[36m`$2`e[0m"
      } `
     | fzf --ansi `
     | ForEach-Object {
       start-process "chrome.exe" ($_ -split "`t")[1],'--profile-directory="Default"'
      }
}
```

Chrome Bookmarks browser with ruby

https://gist.github.com/junegunn/15859538658e449b886f (for OS X)

### Browsing

```highlight
# Simple replacement for urlview in X
# https://github.com/d630/bin/blob/master/furlview
% furlview ( - | FILE ... )
```

### NPM

npm-fzf - Fuzzy search npm modules with `fzf`.

```
# run npm script (requires jq)
fns() {
  local script
  script=$(cat package.json | jq -r '.scripts | keys[] ' | sort | fzf) && npm run $(echo "$script")
}
```

### Locate

`Alt-i` to paste item from `locate /` output (zsh only):

```highlight
# ALT-I - Paste the selected entry from locate output into the command line
fzf-locate-widget() {
  local selected
  if selected=$(locate / | fzf -q "$LBUFFER"); then
    LBUFFER=$selected
  fi
  zle redisplay
}
zle     -N    fzf-locate-widget
bindkey '\ei' fzf-locate-widget
```

### mpd

You must have `mpc` installed on your computer in order to use this function.

```highlight
fmpc() {
  local song_position
  song_position=$(mpc -f "%position%) %artist% - %title%" playlist | \
    fzf-tmux --query="$1" --reverse --select-1 --exit-0 | \
    sed -n 's/^\([0-9]\+\)).*/\1/p') || return 1
  [ -n "$song_position" ] && mpc -q play $song_position
}
```

#### clerk

clerk is a simple MPD client using rofi or fzf.

### Readline

```highlight
# CTRL-X-1 - Invoke Readline functions by name
__fzf_readline ()
{
    builtin eval "
        builtin bind ' \
            \"\C-x3\": $(
                builtin bind -l | command fzf +s +m --toggle-sort=ctrl-r
            ) \
        '
    "
}

builtin bind -x '"\C-x2": __fzf_readline';
builtin bind '"\C-x1": "\C-x2\C-x3"'
```

### RVM

```highlight
# RVM integration
frb() {
  local rb
  rb=$((echo system; rvm list | grep ruby | cut -c 4-) |
       awk '{print $1}' |
       fzf-tmux -l 30 +m --reverse) && rvm use $rb
}
```

### Vagrant

You must have `jq` installed on your computer in order to use this function.

```highlight
vs(){
  #List all vagrant boxes available in the system including its status, and try to access the selected one via ssh
  cd $(cat ~/.vagrant.d/data/machine-index/index | jq '.machines[] | {name, vagrantfile_path, state}' | jq '.name + "," + .state  + "," + .vagrantfile_path'| sed 's/^"\(.*\)"$/\1/'| column -s, -t | sort -rk 2 | fzf | awk '{print $3}'); vagrant ssh
}
```

### Wrapper

When you have defined an alias or wrapper for some command, you might want to inherit the completion from a parent function. Find out the completion used for your command and do:

```highlight
_fzf_complete_myssh() {
  _fzf_complete_ssh "$@"
}
```

See also `_fzf_setup_completion` in the completion source code.

### LastPass CLI

Search through your LastPass vault with LastPass CLI and copy password to clipboard.

```highlight
$ lpass show -c --password $(lpass ls  | fzf | awk '{print $(NF)}' | sed 's/\]//g')
```

### fzf-marker

The terminal command Tweak https://github.com/pindexis/marker.git

(asciicast)

```highlight
# marker templete select
_fzf_marker_main_widget() {
  if echo "$BUFFER" | grep -q -P "{{"; then
    _fzf_marker_placeholder
  else
    local selected
    if selected=$(cat ${FZF_MARKER_CONF_DIR:-~/.config/marker}/*.txt |
      sed -e "s/\(^[a-zA-Z0-9_-]\+\)\s/${FZF_MARKER_COMMAND_COLOR:-\x1b[38;5;255m}\1\x1b[0m /" \
          -e "s/\s*\(#\+\)\(.*\)/${FZF_MARKER_COMMENT_COLOR:-\x1b[38;5;8m}  \1\2\x1b[0m/" |
      fzf --bind 'tab:down,btab:up' --height=80% --ansi -q "$LBUFFER"); then
      LBUFFER=$(echo $selected | sed 's/\s*#.*//')
    fi
    zle redisplay
  fi
}

_fzf_marker_placeholder() {
  local strp pos placeholder
  strp=$(echo $BUFFER | grep -Z -P -b -o "\{\{[\w]+\}\}")
  strp=$(echo "$strp" | head -1)
  pos=$(echo $strp | cut -d ":" -f1)
  placeholder=$(echo $strp | cut -d ":" -f2)
  if [[ -n "$1" ]]; then
    BUFFER=$(echo $BUFFER | sed -e "s/{{//" -e "s/}}//")
    CURSOR=$(($pos + ${#placeholder} - 4))
  else
    BUFFER=$(echo $BUFFER | sed "s/$placeholder//")
    CURSOR=pos
  fi
}

_fzf_marker_placeholder_widget() { _fzf_marker_placeholder "defval" }

zle -N _fzf_marker_main_widget
zle -N _fzf_marker_placeholder_widget
bindkey "${FZF_MARKER_MAIN_KEY:-\C-@}" _fzf_marker_main_widget
bindkey "${FZF_MARKER_PLACEHOLDER_KEY:-\C-v}" _fzf_marker_placeholder_widget
```

### Search for academic PDFs by author, title, journal, institution

Search for all pdf files. FZF will match the query against any text found on the first page of the PDF. For instance, one can query for author names, article title, journal, institutions, keywords. It works by extracting the text on the first page of the PDF using `pdftotext`. The selected file is then opened by the default pdf viewer.

Requires the pdftotext command line tool. Tested on Ubuntu 17.10 on bash and zsh.

The script is now given at https://github.com/bellecp/fast-p

### BibTeX

Search records in BibTeX files using FZF, select records to cite, or pretty print in markdown. With vim integration.

This plugin is at https://github.com/msprev/fzf-bibtex

### Docker

```highlight
# Select a docker container to start and attach to
function da() {
  local cid
  cid=$(docker ps -a | sed 1d | fzf -1 -q "$1" | awk '{print $1}')

  [ -n "$cid" ] && docker start "$cid" && docker attach "$cid"
}
```

```highlight
# Select a running docker container to stop
function ds() {
  local cid
  cid=$(docker ps | sed 1d | fzf -q "$1" | awk '{print $1}')

  [ -n "$cid" ] && docker stop "$cid"
}
```

```highlight
# Select a docker container to remove
function drm() {
  local cid
  cid=$(docker ps -a | sed 1d | fzf -q "$1" | awk '{print $1}')

  [ -n "$cid" ] && docker rm "$cid"
}
```

```highlight
# Same as above, but allows multi selection:
function drm() {
  docker ps -a | sed 1d | fzf -q "$1" --no-sort -m --tac | awk '{ print $1 }' | xargs -r docker rm
}
```

```highlight
# Select a docker image or images to remove
function drmi() {
  docker images | sed 1d | fzf -q "$1" --no-sort -m --tac | awk '{ print $3 }' | xargs -r docker rmi
}
```

### buku

Search and open website bookmarks stored in a buku database.

```highlight
# BUKU bookmark manager
# get bookmark ids
get_buku_ids() {
    buku -p -f 5 | fzf --tac --layout=reverse-list -m | \
      cut -d $'\t' -f 1
    # awk -F= '{print $1}'
    # cut -d $'\t' -f 1
}

# buku open
fb() {
    # save newline separated string into an array
    ids=( $(get_buku_ids) )

    echo buku --open ${ids[@]}

    [[ -z $ids ]] && return 1 # return error if has no bookmark selected

    buku --open ${ids[@]}
}

# buku update
fbu() {
    # save newline separated string into an array
    ids=( $(get_buku_ids) )

    echo buku --update ${ids[@]} $@

    [[ -z $ids ]] && return 0 # return if has no bookmark selected

    buku --update ${ids[@]} $@
}

# buku write
fbw() {
    # save newline separated string into an array
    ids=( $(get_buku_ids) )
    # print -l $ids

    # update websites
    for i in ${ids[@]}; do
        echo buku --write $i
        buku --write $i
    done
}
```

...And a nicer looking alternative, using fzfmenu.

```highlight
#!/usr/bin/env bash
# fb - buku bookmarks fzfmenu opener
buku -p -f 4 |
    awk -F $'\t' '{
        if ($4 == "")
            printf "%s \t\x1b[38;5;208m%s\033[0m\n", $2, $3
        else
            printf "%s \t\x1b[38;5;124m%s \t\x1b[38;5;208m%s\033[0m\n", $2, $4, $3
    }' |
    fzfmenu --tabstop 1 --ansi -d $'\t' --with-nth=2,3 \
        --preview-window='bottom:10%' --preview 'printf "\x1b[38;5;117m%s\033[0m\n" {1}' |
        awk '{print $1}' | xargs -d '\n' -I{} -n1 -r xdg-open '{}'
```

If you have `sqlite` installed - you can use it to query DB directly (which takes about ~2ms compared to buku's ~100ms).

To do that, replace the `buku -p -f 4` with

```highlight
sqlite3 -separator $'\t' "$HOME/.local/share/buku/bookmarks.db" "SELECT id,URL,metadata,tags FROM bookmarks" | awk -F $'\t' '{gsub(/(^,|,$)/,"",$4); printf "%s\t%s\t%s\t%s\n", $1, $2, $3, $4}'
```

Now you can bind it on some key, e.g. with sxhkd in sxhkdrc:

```
super + shift + u
	fb
```

(demo)

### i3

Fuzzy search desktop entries and launch the appropriate application.

```
i3-dmenu-desktop --dmenu=fzf
```

Display in a floating window. Add this to your i3 config file (this example uses termite, but any terminal emulator that allows setting the window title can be used):

```
bindsym $mod+d exec --no-startup-id termite -t 'fzf-menu' -e 'i3-dmenu-desktop --dmenu=fzf'
for_window [title="fzf-menu"] floating enable
```

This, however, will likely not use `FZF_DEFAULT_OPTIONS` because i3-dmenu-desktop launches fzf in a non-interactive shell, so files like .bashrc and .zshrc won't be sourced. If this is a problem for you, you can forcibly start an interactive shell. Here is an example with zsh (using urxvt instead of termite):

```
bindsym $mod+d exec --no-startup-id urxvt -title 'fzf-menu' -e i3-dmenu-desktop --dmenu='zsh -i -c fzf'
```

Better, but not good enough:

- Focus is sometimes not given to the menu, particularly if your workspace is in full screen
- Pressing this key more than once (maybe because focus was not given and we don't realise the menu was actually open) will spawn many instances of the menu, which we don't want. It would be better to give focus to the running instance instead.

Solving both problems:

```highlight
#!/usr/bin/env zsh

# WARN: Some zshisms here won't work in bash.
# Maybe some basher can provide an equivalent bash script.

focus_fmenu() { i3-msg --quiet '[title="fmenu"] focus' }

focus_fmenu && exit 0

# Extra safety in case the window exists but i3 can't focus for some reason.
# Can be left out if you don't have/want to install xdotool
xdotool search --name fmenu && exit 1 

urxvt -title 'fmenu' -e i3-dmenu-desktop --dmenu='zsh -i -c fzf' &|

# Attempt to focus newly created window
repeat 5; do
	focus_fmenu && exit 0
	sleep 0.2
done
```

Put the above script in your PATH under the name fmenu. Don't forget to include these lines in your i3 config:

```
bindsym $mod+d exec fmenu
for_window [title="fmenu"] floating enable
```

### Man pages

Quickly display a man page using fzf and fd. `MANPATH` has to be set to a single directory (usually `/usr/share/man`). Accepts an optional argument for the manual section (defaults to 1).

```highlight
man-find() {
    f=$(fd . $MANPATH/man${1:-1} -t f -x echo {/.} | fzf) && man $f
}
```

```highlight
fman() {
    man -k . | fzf --prompt='Man> ' | cut -d' ' -f1 | xargs -r man
}
```

```highlight
# Same as above, but with previews and works correctly with man pages in different sections.
function fman() {
    man -k . | fzf -q "$1" --prompt='man> '  --preview $'echo {} | tr -d \'()\' | awk \'{printf "%s ", $2} {print $1}\' | xargs -r man' | tr -d '()' | awk '{printf "%s ", $2} {print $1}' | xargs -r man
}
```

Same as above, but the preview is colored with bat

```highlight
fman() {
    man -k . | fzf -q "$1" --prompt='man> '  --preview $'echo {} | tr -d \'()\' | awk \'{printf "%s ", $2} {print $1}\' | xargs -r man | col -bx | bat -l man -p --color always' | tr -d '()' | awk '{printf "%s ", $2} {print $1}' | xargs -r man
}
# Get the colors in the opened man page itself
export MANPAGER="sh -c 'col -bx | bat -l man -p --paging always'"
```

Same as above, but for Termux (Android). man -k behaves differently in Termux, compared to Ubuntu.

```highlight
#!/data/data/com.termux/files/usr/bin/bash
export MANPAGER=~/bin/pman
man -k . | fzf --height=100% --preview-window=up -q "$1" --prompt='man> ' \
    --preview $"echo {} | perl -p -e 's/[-\w, ]*, //; s/\((\d+).*/ \1/' \
    | awk '{printf \"%s \", \$2} {print \$1}' \
    | xargs -r man \
    | col -bx | bat -l man -p --color always " \
    | perl -p -e 's/[-\w, ]*, //; s/\((\d+).*/ \1/' \
    | awk '{printf "%s ", $2} {print $1}' \
    | xargs -n 2 -r man
```

Here is ~/bin/pman:

```highlight
#!/data/data/com.termux/files/usr/bin/bash
cat $* | col -bx | bat -l man -p --paging always
```

#### fzf-man-pages widget (for zsh)

Same functionality as above

- with colored and syntax higlighting
- doesn't exit or close fzf when pressed enter

```highlight
fzf-man-widget() {
  manpage="echo {} | sed 's/\([[:alnum:][:punct:]]*\) (\([[:alnum:]]*\)).*/\2 \1/'"
  batman="${manpage} | xargs -r man | col -bx | bat --language=man --plain --color always --theme=\"Monokai Extended\""
   man -k . | sort \
   | awk -v cyan=$(tput setaf 6) -v blue=$(tput setaf 4) -v res=$(tput sgr0) -v bld=$(tput bold) '{ $1=cyan bld $1; $2=res blue $2; } 1' \
   | fzf  \
      -q "$1" \
      --ansi \
      --tiebreak=begin \
      --prompt=' Man > '  \
      --preview-window '50%,rounded,<50(up,85%,border-bottom)' \
      --preview "${batman}" \
      --bind "enter:execute(${manpage} | xargs -r man)" \
      --bind "alt-c:+change-preview(cht.sh {1})+change-prompt(ﯽ Cheat > )" \
      --bind "alt-m:+change-preview(${batman})+change-prompt( Man > )" \
      --bind "alt-t:+change-preview(tldr --color=always {1})+change-prompt(ﳁ TLDR > )"
  zle reset-prompt
}
# `Ctrl-H` keybinding to launch the widget (this widget works only on zsh, don't know how to do it on bash and fish (additionaly pressing`ctrl-backspace` will trigger the widget to be executed too because both share the same keycode)
bindkey '^h' fzf-man-widget
zle -N fzf-man-widget
# Icon used is nerdfont
```

### Python Behave BDD

Tab copy the step name.

Enter copy the step location

```highlight
fbehave() {
    behave "$@" -d -f steps 2> /dev/null | \
    awk -F " *# " '/\s*(Given|When|Then|\*)/ {print $1"\t"$2}' | \
    fzf -d "\t" --with-nth=1 \
        --bind 'enter:execute(echo {} | cut -f2 | pbcopy )' \
        --bind 'tab:execute(echo {} | cut -f1 | awk "{\$1=\$1};1" | pbcopy )'
}
```

### fzf as selector menu

Make a script like this (`~/.local/bin/fzfmenu`):

```highlight
#!/usr/bin/env bash

export FZF_DEFAULT_OPTS="--height=100% --layout=reverse --border --no-sort --prompt=\"~ \" --color=dark,hl:red:regular,fg+:white:regular,hl+:red:regular:reverse,query:white:regular,info:gray:regular,prompt:red:bold,pointer:red:bold"

exec alacritty --class="fzf-menu" -e bash -c "fzf-tmux -m $* < /proc/$$/fd/0 | awk 'BEGIN {ORS=\" \"} {print}' > /proc/$$/fd/1"
# For st instead
# st -c fzf-menu -n fzf-menu -e bash -c "fzf-tmux -m $* < /proc/$$/fd/0 | awk 'BEGIN {ORS=\" \"} {print}' > /proc/$$/fd/1"
```

1. Then to run as app launcher, use sxhkd and put in `~/.config/sxhkdrc` `# run apps launcher control + alt + s ; r dmenu_path | ~/.local/bin/fzfmenu | bash` ( You can use anything other than `dmenu_path` that gets a list of entries in `$PATH` too.)
2. To use for `Ctrl-t` for a floating menu from terminal **For bash**

```highlight
__fzfmenu__() {
  local cmd="fd -tf --max-depth=1"
  eval "$cmd" | ~/.local/bin/fzfmenu
}

__fzf-menu__() {
  local selected="$(__fzfmenu__)"
  READLINE_LINE="${READLINE_LINE:0:$READLINE_POINT}$selected${READLINE_LINE:$READLINE_POINT}"
  READLINE_POINT=$(( READLINE_POINT + ${#selected} ))
}
bind -x '"\C-t":"__fzf-menu__"'
```

**For zsh**

```highlight
__fzfmenu__(){
  local cmd="fd -tf --max-depth=1"
  eval $cmd | ~/.local/bin/fzfmenu
}
__fzf-menu__() {
  LBUFFER="${LBUFFER}$(__fzfmenu__)"
  local ret=$?
  zle reset-prompt
  return $ret
}

zle     -N    __fzf-menu__
bindkey -M emacs '^T^G' __fzf-menu__
bindkey -M vicmd '^T^G' __fzf-menu__
bindkey -M viins '^T^G' __fzf-menu__
```


## fzf as rofi replacement

https://github.com/gotbletu/shownotes/blob/master/fzf_nova/fzf-nova

download fzf-nova folder as a whole and follow the instructions in fzf-nova script

Reference video

credits @gotbletu

### fzf as dmenu replacement

Why? ...Because it's faster.

So you'll need:

1. terminal that launches fast and supports custom class or window name. St fits the bill perfectly.
2. window manager with an option to automatically put windows in center based on class or name. Most seem to have it.

```highlight
#!/usr/bin/env bash
# fzfmenu - fzf as dmenu replacement

# fifos are here to not wait for end of input
# (useful for e.g. find $HOME | fzfmenu ...)
input=$(mktemp -u --suffix .fzfmenu.input)
output=$(mktemp -u --suffix .fzfmenu.output)
mkfifo $input
mkfifo $output
chmod 600 $input $output

# it's better to use st here (starts a lot faster than pretty much everything else)
# the ugly printf | sed thing is here to make args with quotes work.
# (e.g. --preview='echo {1}').
# sadly we can't use "$@" here directly because we are inside sh -c "..." call
# already.
# you can also set window dimensions via -g '=COLSxROWS', see man st.
st -c fzfmenu -n fzfmenu -e sh -c "cat $input | fzf $(printf -- " '%s'" "$@" | sed "s/^ ''$//") | tee $output" & disown

# handle ctrl+c outside child terminal window
trap "kill $! 2>/dev/null; rm -f $input $output" EXIT

cat > $input
cat $output
```

All arguments are passed to fzf.

Don't forget to add a float/center rule for `fzfmenu` class/name to your wm's config.

Example usage.

### dotfiles management

dotbare is a command-line utility to manage your dotfiles. It heavily utilises fzf for interactive user experience. It is inspired by forgit, but focuses on dotfiles rather than generic git. By default, it wraps around git bare repository but it could also be easily integrated with a symlink/GNU stow setup.

(dotbare screenshot)

### Transmission

zsh keybinding to select a torrent with transmission-remote.

```highlight
pick_torrent() LBUFFER="transmission-remote -t ${$({
    for torrent in ${(f)"$(transmission-remote -l)"}; do
        torrent_name=$torrent[73,-1]
        [[ $torrent_name != (Name|) ]] && echo ${${${(s. .)torrent}[1]}%\*} $torrent_name
    done
} | fzf)%% *} -"
zle -N pick_torrent
bindkey '^o' pick_torrent
```

### Pacman

```highlight
# Install packages using yay (change to pacman/AUR helper of your choice)
function in() {
    yay -Slq | fzf -q "$1" -m --preview 'yay -Si {1}'| xargs -ro yay -S
}
# Remove installed packages (change to pacman/AUR helper of your choice)
function re() {
    yay -Qq | fzf -q "$1" -m --preview 'yay -Qi {1}' | xargs -ro yay -Rns
}
```

Shows version & repository, elaborate preview, bindings to show package in web, caches AUR packages list:

```highlight
# Helper function to integrate yay and fzf
yzf() {
  pos=$1
  shift
  sed "s/ /\t/g" |
    fzf --nth=$pos --multi --history="${FZF_HISTDIR:-$XDG_STATE_HOME/fzf}/history-yzf$pos" \
      --preview-window=60%,border-left \
      --bind="double-click:execute(xdg-open 'https://archlinux.org/packages/{$pos}'),alt-enter:execute(xdg-open 'https://aur.archlinux.org/packages?K={$pos}&SB=p&SO=d&PP=100')" \
       "$@" | cut -f$pos | xargs
}

# Dev note: print -s adds a shell history entry

# List installable packages into fzf and install selection
yas() {
  cache_dir="/tmp/yas-$USER"
  test "$1" = "-y" && rm -rf "$cache_dir" && shift
  mkdir -p "$cache_dir"
  preview_cache="$cache_dir/preview_{2}"
  list_cache="$cache_dir/list"
  { test "$(cat "$list_cache$@" | wc -l)" -lt 50000 && rm "$list_cache$@"; } 2>/dev/null
  pkg=$( (cat "$list_cache$@" 2>/dev/null || { pacman --color=always -Sl "$@"; yay --color=always -Sl aur "$@" } | sed 's/ [^ ]*unknown-version[^ ]*//' | tee "$list_cache$@") |
    yzf 2 --tiebreak=index --preview="cat $preview_cache 2>/dev/null | grep -v 'Querying' | grep . || yay --color always -Si {2} | tee $preview_cache")
  if test -n "$pkg"
    then echo "Installing $pkg..."
      cmd="yay -S $pkg"
      print -s "$cmd"
      eval "$cmd"
      rehash
  fi
}
# List installed packages into fzf and remove selection
# Tip: use -e to list only explicitly installed packages
yar() {
  pkg=$(yay --color=always -Q "$@" | yzf 1 --tiebreak=length --preview="yay --color always -Qli {1}")
  if test -n "$pkg"
    then echo "Removing $pkg..."
      cmd="yay -R --cascade --recursive $pkg"
      print -s "$cmd"
      eval "$cmd"
  fi
}
```

### Clipboard

Uses wl-copy to copy the current entry to the clipboard on Wayland:

```highlight
export FZF_DEFAULT_OPTS='--bind "ctrl-y:execute-silent(printf {} | cut -f 2- | wl-copy --trim-newline)"'
```

This works with `execute-silent` but not with `execute`, presumably because `execute` waits for `wl-copy` to end. Appending a `&` did not change that.

### Todoist CLI

- Todoist CLI task filitring and preview ❯ todoist --namespace --project-namespace list | fzf --preview 'todoist show {1}' | cut -d ' ' -f 1 | tr '\n' ' '
  - The command used for preview is `todoist show {1}`
    - The `show` option is used to show the task details
    - The `{1}` represents the first feild in the line -> Task ID

### Dictcc Translation

Request database file from https://www1.dict.cc/translation_file_request.php

```highlight
cat /path/to/dict.txt | tail -n +16 | fzf --tiebreak=length
```

### Emoji

emoji.txt

```highlight
emojis=$(curl -sSL 'https://git.io/JXXO7')

selected_emoji=$(echo $emojis | fzf)

echo $selected_emoji
```

### Slurm

fzf integration with some Slurm's cli utilities (zsh & bash)

#### scancel

Look for user's job IDs to easily kill running jobs

```highlight
_fzf_complete_scancel() {
        _fzf_complete --multi --header-lines=1 -- "$@" < <(squeue -u $USER)
}
_fzf_complete_scancel_post() {
        awk '{print $1}'
}
[ -n "$BASH" ] && complete -F _fzf_complete_scancel -o default -o bashdefault scancel || :
```
