---
title: "ps(1) (part 2/2)"
source: https://man7.org/linux/man-pages/man1/ps.1.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 2/2
---

## STANDARD FORMAT SPECIFIERS

Here are the different keywords that may be used to control the
output format (e.g., with option -o) or to sort the selected
processes with the GNU-style --sort option.

For example: ps -eo pid,user,args --sort user

This version of ps tries to recognize most of the keywords used in
other implementations of ps.

The following user-defined format specifiers may contain spaces:
args, cmd, comm, command, fname, ucmd, ucomm, lstart, bsdstart,
start.

Some keywords may not be available for sorting.

Code         Header     Description
───────────────────────────────────────────────────────────────────
%cpu         %CPU       cpu utilization of the process in "##.#"
                        format.  Currently, it is the CPU time
                        used divided by the time the process has
                        been running (cputime/realtime ratio),
                        expressed as a percentage.  It will not
                        add up to 100% unless you are lucky.
                        (alias pcpu).

%mem         %MEM       ratio of the process's resident set size
                        to the physical memory on the machine,
                        expressed as a percentage.  (alias pmem).

ag_id        AGID       The autogroup identifier associated with a
                        process which operates in conjunction with
                        the CFS scheduler to improve interactive
                        desktop performance.

ag_nice      AGNI       The autogroup nice value which affects
                        scheduling of all processes in that group.

args         COMMAND    A command with all its arguments as a
                        string.  Modifications to the arguments
                        may be shown.  The column contents may
                        include spaces.  A process marked
                        “<defunct>” is partly dead, waiting to be
                        fully destroyed by its parent.  Sometimes
                        the process arguments will be unavailable;
                        when this happens, ps instead reports the
                        executable name in brackets.  (alias cmd,
                        command).  See also the comm format
                        keyword, the -f option, and the c option.

                        When specified last, this column will
                        extend to the edge of the display.  If ps
                        can not determine the display width, as
                        when output is redirected (piped) into a
                        file or another command, the output width
                        is undefined (it may be 80, unlimited,
                        determined by the TERM variable, and so
                        on).  The COLUMNS environment variable,
                        which can be overridden with the --cols,
                        --columns or --width option may be used to
                        exactly determine the width in this case.
                        The w or -w option may be also be used to
                        adjust width.

blocked      BLOCKED    mask of the blocked signals, see
                        signal(7).  According to the width of the
                        field, a 32 or 64-bit mask in hexadecimal
                        format is displayed, unless the --signames
                        option is used.  (alias sig_block,
                        sigmask).

bsdstart     START      time the command started.  If the process
                        was started less than 24 hours ago, the
                        output format is " HH:MM", else it is "
                        Mmm:SS" (where Mmm is the three letters of
                        the month).  See also
                        lstart, start, start_time, and stime.

bsdtime      TIME       accumulated cpu time, user + system.  The
                        display format is usually "MMM:SS", but
                        can be shifted to the right if the process
                        used more than 999 minutes of cpu time.

c            C          processor utilization.  Currently, this is
                        the integer value of the percent usage
                        over the lifetime of the process.  (see
                        %cpu).

caught       CAUGHT     mask of the caught signals, see signal(7).
                        According to the width of the field, a 32
                        or 64 bits mask in hexadecimal format is
                        displayed, unless the --signames option is
                        used.  (alias sig_catch, sigcatch).

cgname       CGNAME     display name of control groups to which
                        the process belongs.

cgroup       CGROUP     display control groups to which the
                        process belongs.

cgroupns     CGROUPNS   Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

class        CLS        scheduling class of the process.  (alias
                        policy, cls).  Field's possible values
                        are:

                                 -    not reported
                                 TS   SCHED_OTHER
                                 FF   SCHED_FIFO
                                 RR   SCHED_RR
                                 B    SCHED_BATCH
                                 ISO  SCHED_ISO
                                 IDL  SCHED_IDLE
                                 DLN  SCHED_DEADLINE
                                 ?    unknown value

cls          CLS        scheduling class of the process.  (alias
                        policy, cls).  Field's possible values
                        are:

                                 -    not reported
                                 TS   SCHED_OTHER
                                 FF   SCHED_FIFO
                                 RR   SCHED_RR
                                 B    SCHED_BATCH
                                 ISO  SCHED_ISO
                                 IDL  SCHED_IDLE
                                 DLN  SCHED_DEADLINE
                                 ?    unknown value

cmd          CMD        see args.  (alias args, command).

comm         COMMAND    command name (only the executable name).
                        The output in this column may contain
                        spaces.  (alias ucmd, ucomm).  See also
                        the args format keyword, the -f option,
                        and the c option.

                        When specified last, this column will
                        extend to the edge of the display.  If ps
                        can not determine display width, as when
                        output is redirected (piped) into a file
                        or another command, the output width is
                        undefined (it may be 80, unlimited,
                        determined by the TERM variable, and so
                        on).  The COLUMNS environment variable or
                        --cols option may be used to exactly
                        determine the width in this case.  The
                        w or -w option may be also be used to
                        adjust width.

command      COMMAND    See args.  (alias args, command).

cp           CP         per-mill (tenths of a percent) CPU usage.
                        (see %cpu).

cpu          CPU        See psr.  (alias cpuid, lastcpu, psr).

cpuid        CPUID      See psr.  (alias cpu, lastcpu, psr).

cputime      TIME       cumulative CPU time, "[DD-]hh:mm:ss"
                        format.  (alias time).

cputimes     TIME       cumulative CPU time in seconds (alias
                        times).

cuc          %CUC       The CPU utilization of a process,
                        including dead children, in an extended
                        "##.###" format.  (see also %cpu, c, cp,
                        cuu, pcpu).

cuu          %CUU       The CPU utilization of a process in an
                        extended "##.###" format.  (see also %cpu,
                        c, cp, cuc, pcpu).

docker       DOCKER     The abbreviated id of the docker container
                        within which a task is running.  If a
                        process is not running inside a container,
                        a dash ('-') will be shown.

drs          DRS        data resident set size, the amount of
                        private memory reserved by a process.  It
                        is also known as DATA.  Such memory may
                        not yet be mapped to rss but will always
                        be included in the vsz amount.

egid         EGID       effective group ID number of the process
                        as a decimal integer.  (alias gid).

egroup       EGROUP     effective group ID of the process.  This
                        will be the textual group ID, if it can be
                        obtained and the field width permits, or a
                        decimal representation otherwise.  (alias
                        group).

eip          EIP        instruction pointer.  As of kernel 4.9.xx
                        will be zeroed out unless task is exiting
                        or being core dumped.

esp          ESP        stack pointer.  As of kernel 4.9.xx will
                        be zeroed out unless task is exiting or
                        being core dumped.

etime        ELAPSED    elapsed time since the process was
                        started, in the form [[DD-]hh:]mm:ss.

etimes       ELAPSED    elapsed time since the process was
                        started, in seconds.

environ      ENVIRON    environment variables for the process.
euid         EUID       effective user ID (alias uid).

euser        EUSER      effective user name.  This will be the
                        textual user ID, if it can be obtained and
                        the field width permits, or a decimal
                        representation otherwise.  The n option
                        can be used to force the decimal
                        representation.  (alias uname, user).

exe          EXE        path to the executable.  Useful if path
                        cannot be printed via cmd, comm or args
                        format options.

f            F          flags associated with the process, see the
                        PROCESS FLAGS section.  (alias flag,
                        flags).

fds          FDS        total open file descriptors.

fgid         FGID       filesystem access group ID.  (alias
                        fsgid).

fgroup       FGROUP     filesystem access group ID.  This will be
                        the textual group ID, if it can be
                        obtained and the field width permits, or a
                        decimal representation otherwise.  (alias
                        fsgroup).

flag         F          see f.  (alias f, flags).

flags        F          see f.  (alias f, flag).

fname        COMMAND    first 8 bytes of the base name of the
                        process's executable file.  The output in
                        this column may contain spaces.

fuid         FUID       filesystem access user ID.  (alias fsuid).

fuser        FUSER      filesystem access user ID.  This will be
                        the textual user ID, if it can be obtained
                        and the field width permits, or a decimal
                        representation otherwise.

gid          GID        see egid.  (alias egid).

group        GROUP      see egroup.  (alias egroup).

htprv        HTPRV      The amount of private memory backed by
                        hugetlbfs page which is not counted in the
                        rss or pss format options.

htshr        HTSHR      The amount of shared memory backed by
                        hugetlbfs page which is not counted in the
                        rss or pss format options.

ignored      IGNORED    mask of the ignored signals, see
                        signal(7).  According to the width of the
                        field, a 32 or 64 bits mask in hexadecimal
                        format is displayed, unless the --signames
                        option is used.  (alias sig_ignore,
                        sigignore).

ipcns        IPCNS      Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

label        LABEL      security label, most commonly used for
                        SELinux context data.  This is for the
                        Mandatory Access Control ("MAC") found on
                        high-security systems.

lastcpu      C          See psr.  (alias cpu, cpuid, psr).

lstart       STARTED    time the command started.  This will be in
                        the form "DDD mmm HH:MM:SS YYY" unless
                        changed by the -D option.

lsession     SESSION    displays the login session identifier of a
                        process, if systemd support has been
                        included.

luid         LUID       displays Login ID associated with a
                        process.

lwp          LWP        light weight process (thread) ID of the
                        dispatchable entity (alias spid, tid).
                        See tid for additional information.

lxc          LXC        The name of the lxc container within which
                        a task is running.  If a process is not
                        running inside a container, a dash ('-')
                        will be shown.

machine      MACHINE    displays the machine name for processes
                        assigned to VM or container, if systemd
                        support has been included.

maj_flt      MAJFLT     The number of major page faults that have
                        occurred with this process.

min_flt      MINFLT     The number of minor page faults that have
                        occurred with this process.

mntns        MNTNS      Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

netns        NETNS      Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

ni           NI         nice value.  This ranges from 19 (nicest)
                        to -20 (not nice to others), see nice(1).
                        (alias nice).

nice         NI         see ni.(alias ni).

nlwp         NLWP       number of lwps (threads) in the process.
                        (alias thcount).

numa         NUMA       The node associated with the most recently
                        used processor.  A -1 means that NUMA
                        information is unavailable.

nwchan       WCHAN      address of the kernel function where the
                        process is sleeping (use wchan if you want
                        the kernel function name).

oom          OOM        Out of Memory Score.  The value, ranging
                        from 0 to +1000, used to select task(s) to
                        kill when memory is exhausted.

oomadj       OOMADJ     Out of Memory Adjustment Factor.  The
                        value is added to the current out of
                        memory score which is then used to
                        determine which task to kill when memory
                        is exhausted.

ouid         OWNER      displays the Unix user identifier of the
                        owner of the session of a process, if
                        systemd support has been included.

pcap         PCAP       Permitted Capabilities of the process,
                        displayed as a hexadecimal bitmask.  See
                        capabilities(7).

pcaps        PCAPS      Permitted Capabilities of the process,
                        displayed as a string of capability names.
                        See capabilities(7).

pcpu         %CPU       see %cpu.  (alias %cpu).

pending      PENDING    mask of the pending signals.  See
                        signal(7).  Signals pending on the process
                        are distinct from signals pending on
                        individual threads.  Use the m option or
                        the -m option to see both.  According to
                        the width of the field, a 32 or 64 bits
                        mask in hexadecimal format is displayed,
                        unless the --signames option is used.
                        (alias sig).

pgid         PGID       process group ID or, equivalently, the
                        process ID of the process group leader.
                        (alias pgrp).

pgrp         PGRP       see pgid.  (alias pgid).

pid          PID        a number representing the process ID
                        (alias tgid).

pidns        PIDNS      Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

pmem         %MEM       see %mem.  (alias %mem).

policy       POL        scheduling class of the process.  (alias
                        class, cls).  Possible values are:

                                 -    not reported
                                 TS   SCHED_OTHER
                                 FF   SCHED_FIFO
                                 RR   SCHED_RR
                                 B    SCHED_BATCH
                                 ISO  SCHED_ISO
                                 IDL  SCHED_IDLE
                                 DLN  SCHED_DEADLINE
                                 ?    unknown value

ppid         PPID       parent process ID.

pri          PRI        priority of the process.  Higher number
                        means higher priority.

psr          PSR        processor that process last executed on.
                        (alias cpu, cpuid, lastcpu).

pss          PSS        Proportional share size, the non-swapped
                        physical memory, with shared memory
                        proportionally accounted to all tasks
                        mapping it.

rbytes       RBYTES     Number of bytes which this process really
                        did cause to be fetched from the storage
                        layer.

rchars       RCHARS     Number of bytes which this task has caused
                        to be read from storage.

rgid         RGID       real group ID.

rgroup       RGROUP     real group name.  This will be the textual
                        group ID, if it can be obtained and the
                        field width permits, or a decimal
                        representation otherwise.

rops         ROPS       Number of read I/O operations—that is,
                        system calls such as read(2) and pread(2).

rss          RSS        resident set size, the non-swapped
                        physical memory that a task has used (in
                        kibibytes).  (alias rssize, rsz).

rssize       RSS        see rss.  (alias rss, rsz).

rsz          RSZ        see rss.  (alias rss, rssize).

rtprio       RTPRIO     realtime priority.

ruid         RUID       real user ID.

ruser        RUSER      real user ID.  This will be the textual
                        user ID, if it can be obtained and the
                        field width permits, or a decimal
                        representation otherwise.

s            S          minimal state display (one character).
                        See section PROCESS STATE CODES for the
                        different values.  See also stat if you
                        want additional information displayed.
                        (alias state).

sched        SCH        scheduling policy of the process.  The
                        policies SCHED_OTHER (SCHED_NORMAL),
                        SCHED_FIFO, SCHED_RR, SCHED_BATCH,
                        SCHED_ISO, SCHED_IDLE and SCHED_DEADLINE
                        are respectively displayed as 0, 1, 2, 3,
                        4, 5 and 6.

seat         SEAT       displays the identifier associated with
                        all hardware devices assigned to a
                        specific workplace, if systemd support has
                        been included.

sess         SESS       session ID or, equivalently, the process
                        ID of the session leader.  (alias session,
                        sid).

sgi_p        P          processor that the process is currently
                        executing on.  Displays "*" if the process
                        is not currently running or runnable.

sgid         SGID       saved group ID.  (alias svgid).

sgroup       SGROUP     saved group name.  This will be the
                        textual group ID, if it can be obtained
                        and the field width permits, or a decimal
                        representation otherwise.

sid          SID        see sess.  (alias sess, session).

sig          PENDING    see pending.  (alias pending, sig_pend).

sigcatch     CAUGHT     see caught.  (alias caught, sig_catch).

sigignore    IGNORED    see ignored.  (alias ignored, sig_ignore).

sigmask      BLOCKED    see blocked.  (alias blocked, sig_block).

size         SIZE       approximate amount of swap space that
                        would be required if the process were to
                        dirty all writable pages and then be
                        swapped out.  This number is very rough!

slice        SLICE      displays the slice unit which a process
                        belongs to, if systemd support has been
                        included.

spid         SPID       see lwp.  (alias lwp, tid).

stackp       STACKP     address of the bottom (start) of stack for
                        the process.

start        STARTED    time the command started.  If the process
                        was started less than 24 hours ago, the
                        output format is "HH:MM:SS", else it is
                        "  Mmm dd" (where Mmm is a three-letter
                        month name).  See also bsdstart, start,
                        start_time, and stime.

start_time   START      starting time or date of the process.
                        Only the year will be displayed if the
                        process was not started the same year ps
                        was invoked, or "MmmDD" if it was not
                        started the same day, or "HH:MM"
                        otherwise.  See also bsdstart, start,
                        lstart, and stime.

stat         STAT       multi-character process state.  See
                        section PROCESS STATE CODES for the
                        different values meaning.  See also
                        s and state if you just want the first
                        character displayed.

state        S          see s. (alias s).

stime        STIME      see start_time.  (alias start_time).

suid         SUID       saved user ID.  (alias svuid).

supgid       SUPGID     group ids of supplementary groups, if any.
                        See getgroups(2).

supgrp       SUPGRP     group names of supplementary groups, if
                        any.  See getgroups(2).

suser        SUSER      saved user name.  This will be the textual
                        user ID, if it can be obtained and the
                        field width permits, or a decimal
                        representation otherwise.  (alias svuser).

svgid        SVGID      see sgid.  (alias sgid).

svuid        SVUID      see suid.  (alias suid).

sz           SZ         size in physical pages of the core image
                        of the process.  This includes text, data,
                        and stack space.  Device mappings are
                        currently excluded; this is subject to
                        change.  See vsz and rss.

tgid         TGID       a number representing the thread group to
                        which a task belongs (alias pid).  It is
                        the process ID of the thread group leader.

thcount      THCNT      see nlwp.  (alias nlwp).  number of kernel
                        threads owned by the process.

tid          TID        the unique number representing a
                        dispatchable entity (alias spid, tid).
                        This value may also appear as: a process
                        ID (pid); a process group ID (pgrp); a
                        session ID for the session leader (sid); a
                        thread group ID for the thread group
                        leader (tgid); and a tty process group ID
                        for the process group leader (tpgid).

time         TIME       cumulative CPU time, "[DD-]HH:MM:SS"
                        format.  (alias cputime).

timens       TIMENS     Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

times        TIME       cumulative CPU time in seconds (alias
                        cputimes).

tname        TTY        controlling tty (terminal).  (alias tt,
                        tty).

tpgid        TPGID      ID of the foreground process group on the
                        tty (terminal) that the process is
                        connected to, or -1 if the process is not
                        connected to a tty.

trs          TRS        text resident set size, the amount of
                        physical memory devoted to executable
                        code.

tt           TT         controlling tty (terminal).  (alias tname,
                        tty).

tty          TT         controlling tty (terminal).  (alias tname,
                        tt).

ucmd         CMD        see comm.  (alias comm, ucomm).

ucomm        COMMAND    see comm.  (alias comm, ucmd).

uid          UID        see euid.  (alias euid).

uname        USER       see euser.  (alias euser, user).

unit         UNIT       displays unit which a process belongs to,
                        if systemd support has been included.

user         USER       see euser.  (alias euser, uname).

userns       USERNS     Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

uss          USS        Unique set size, the non-swapped physical
                        memory, which is not shared with an
                        another task.

utsns        UTSNS      Unique inode number describing the
                        namespace the process belongs to.  See
                        namespaces(7).

uunit        UUNIT      displays user unit which a process belongs
                        to, if systemd support has been included.

vsize        VSZ        see vsz.  (alias vsz).

vsz          VSZ        virtual memory size of the process in KiB
                        (1024-byte units).  Device mappings are
                        currently excluded; this is subject to
                        change.  (alias vsize).

wbytes       WBYTES     Number of bytes which this process caused
                        to be sent to the storage layer.

wcbytes      WCBYTES    Number of cancelled write bytes.

wchan        WCHAN      name of the kernel function in which the
                        process is sleeping.

wchars       WCHARS     Number of bytes which this task has
                        caused, or shall cause to be written to
                        disk.

wops         WOPS       Number of write I/O operations—that is,
                        system calls such as write(2) and
                        pwrite(2).


## ENVIRONMENT VARIABLES

The following environment variables could affect ps:

COLUMNS
   Override default display width.

LINES
   Override default display height.

PS_PERSONALITY
   Set to one of posix, old, linux, bsd, sun, digital... (see
   section PERSONALITY below).

CMD_ENV
   Set to one of posix, old, linux, bsd, sun, digital... (see
   section PERSONALITY below).

I_WANT_A_BROKEN_PS
   Force obsolete command line interpretation.

LC_TIME
   Date format.

LIBPROC_HIDE_KERNEL
   Set this to any value to hide kernel threads normally displayed
   with the -e option. This is equivalent to selecting --ppid 2 -p
   2 --deselect instead. Also works in BSD mode.

PS_COLORS
   Not currently supported.

PS_FORMAT
   Default output format override. You may set this to a format
   string of the type used for the -o option.  The DefSysV and
   DefBSD values are particularly useful.

POSIXLY_CORRECT
   Don't find excuses to ignore bad "features".

POSIX2
   When set to "on", acts as POSIXLY_CORRECT.

UNIX95
   Don't find excuses to ignore bad "features".

_XPG
   Cancel CMD_ENV=irix non-standard behavior.

In general, it is a bad idea to set these variables.  The one
exception is CMD_ENV or PS_PERSONALITY, which could be set to
Linux for normal systems.  Without that setting, ps follows the
useless and bad parts of the Unix98 standard.


## PERSONALITY

390        like the OS/390 OpenEdition ps
aix        like AIX ps
bsd        like FreeBSD ps (totally non-standard)
compaq     like Digital Unix ps
debian     like the old Debian ps
digital    like Tru64 (was Digital Unix, was OSF/1) ps
gnu        like the old Debian ps
hp         like HP-UX ps
hpux       like HP-UX ps
irix       like Irix ps
linux      ***** recommended *****
old        like the original Linux ps (totally non-standard)
os390      like OS/390 Open Edition ps
posix      standard
s390       like OS/390 Open Edition ps
sco        like SCO ps
sgi        like Irix ps
solaris2   like Solaris 2+ (SunOS 5) ps
sunos4     like SunOS 4 (Solaris 1) ps (totally non-standard)
svr4       standard
sysv       standard
tru64      like Tru64 (was Digital Unix, was OSF/1) ps
unix       standard
unix95     standard
unix98     standard


## BUGS

The fields bsdstart and start will only show the abbreviated month
name in English. The fields lstart and stime will show the
abbreviated month name in the configured locale but may exceed the
column width due to the different lengths for abbreviated month
and day names across languages.


## SEE ALSO

pgrep(1), pstree(1), top(1), strftime(3), proc(5),
capabilities(7).


## STANDARDS

This ps conforms to the following standards.

•   Version 2 of the Single Unix Specification

•   The Open Group Technical Standard Base Specifications, Issue 6

•   IEEE Std 1003.1, 2004 Edition

•   X/Open System Interfaces Extension [UP XSI]

•   ISO/IEC 9945:2003


## AUTHOR

ps was originally written by Branko Lankester ⟨lankeste@fwi.uva.
nl⟩.  Michael K. Johnson ⟨johnsonm@redhat.com⟩ re-wrote it
significantly to use the proc filesystem, changing a few things in
the process.  Michael Shields ⟨mjshield@nyx.cs.du.edu⟩ added the
pid-list feature.  Charles Blake ⟨cblake@bbn.com⟩ added
multi-level sorting, the dirent-style library, the device
name-to-number mmaped database, the approximate binary search
directly on System.map, and many code and documentation cleanups.
David Mossberger-Tang wrote the generic BFD support for psupdate.
Albert Cahalan ⟨albert@users.sf.net⟩ rewrote ps for full Unix98
and BSD support, along with some ugly hacks for obsolete and
foreign syntax.

Please send bug reports to ⟨procps@freelists.org⟩.  No
subscription is required or suggested.
