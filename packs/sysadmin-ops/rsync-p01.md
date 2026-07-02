---
title: "rsync(1) (part 1/5)"
source: https://man7.org/linux/man-pages/man1/rsync.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 1/5
---

# rsync(1) — Linux manual page

rsync(1)                      User Commands                      rsync(1)


## NAME

rsync - a fast, versatile, remote (and local) file-copying tool


## SYNOPSIS

Local:
    rsync [OPTION...] SRC... [DEST]

Access via remote shell:
    Pull:
        rsync [OPTION...] [USER@]HOST:SRC... [DEST]
    Push:
        rsync [OPTION...] SRC... [USER@]HOST:DEST

Access via rsync daemon:
    Pull:
        rsync [OPTION...] [USER@]HOST::SRC... [DEST]
        rsync [OPTION...] rsync://[USER@]HOST[:PORT]/SRC... [DEST]
    Push:
        rsync [OPTION...] SRC... [USER@]HOST::DEST
        rsync [OPTION...] SRC... rsync://[USER@]HOST[:PORT]/DEST)

Usages with just one SRC arg and no DEST arg will list the source
files instead of copying.

The online version of this manpage (that includes cross-linking of
topics) is available at 
⟨https://download.samba.org/pub/rsync/rsync.1⟩.


## DESCRIPTION

Rsync is a fast and extraordinarily versatile file copying tool.
It can copy locally, to/from another host over any remote shell,
or to/from a remote rsync daemon.  It offers a large number of
options that control every aspect of its behavior and permit very
flexible specification of the set of files to be copied.  It is
famous for its delta-transfer algorithm, which reduces the amount
of data sent over the network by sending only the differences
between the source files and the existing files in the
destination.  Rsync is widely used for backups and mirroring and
as an improved copy command for everyday use.

Rsync finds files that need to be transferred using a "quick
check" algorithm (by default) that looks for files that have
changed in size or in last-modified time.  Any changes in the
other preserved attributes (as requested by options) are made on
the destination file directly when the quick check indicates that
the file's data does not need to be updated.

Some of the additional features of rsync are:

o      support for copying links, devices, owners, groups, and
       permissions

o      exclude and exclude-from options similar to GNU tar

o      a CVS exclude mode for ignoring the same files that CVS
       would ignore

o      can use any transparent remote shell, including ssh or rsh

o      does not require super-user privileges

o      pipelining of file transfers to minimize latency costs

o      support for anonymous or authenticated rsync daemons (ideal
       for mirroring)


## GENERAL

Rsync copies files either to or from a remote host, or locally on
the current host (it does not support copying files between two
remote hosts).

There are two different ways for rsync to contact a remote system:
using a remote-shell program as the transport (such as ssh or rsh)
or contacting an rsync daemon directly via TCP.  The remote-shell
transport is used whenever the source or destination path contains
a single colon (:) separator after a host specification.
Contacting an rsync daemon directly happens when the source or
destination path contains a double colon (::) separator after a
host specification, OR when an rsync:// URL is specified (see also
the USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION
section for an exception to this latter rule).

As a special case, if a single source arg is specified without a
destination, the files are listed in an output format similar to
"ls -l".

As expected, if neither the source or destination path specify a
remote host, the copy occurs locally (see also the --list-only
option).

Rsync refers to the local side as the client and the remote side
as the server.  Don't confuse server with an rsync daemon.  A
daemon is always a server, but a server can be either a daemon or
a remote-shell spawned process.


## SETUP

See the file README.md for installation instructions.

Once installed, you can use rsync to any machine that you can
access via a remote shell (as well as some that you can access
using the rsync daemon-mode protocol).  For remote transfers, a
modern rsync uses ssh for its communications, but it may have been
configured to use a different remote shell by default, such as rsh
or remsh.

You can also specify any remote shell you like, either by using
the -e command line option, or by setting the RSYNC_RSH
environment variable.

Note that rsync must be installed on both the source and
destination machines.


## USAGE

You use rsync in the same way you use rcp.  You must specify a
source and a destination, one of which may be remote.

Perhaps the best way to explain the syntax is with some examples:

    rsync -t *.c foo:src/

This would transfer all files matching the pattern *.c from the
current directory to the directory src on the machine foo.  If any
of the files already exist on the remote system then the rsync
remote-update protocol is used to update the file by sending only
the differences in the data.  Note that the expansion of wildcards
on the command-line (*.c) into a list of files is handled by the
shell before it runs rsync and not by rsync itself (exactly the
same as all other Posix-style programs).

    rsync -avz foo:src/bar /data/tmp

This would recursively transfer all files from the directory
src/bar on the machine foo into the /data/tmp/bar directory on the
local machine.  The files are transferred in archive mode, which
ensures that symbolic links, devices, attributes, permissions,
ownerships, etc. are preserved in the transfer.  Additionally,
compression will be used to reduce the size of data portions of
the transfer.

    rsync -avz foo:src/bar/ /data/tmp

A trailing slash on the source changes this behavior to avoid
creating an additional directory level at the destination.  You
can think of a trailing / on a source as meaning "copy the
contents of this directory" as opposed to "copy the directory by
name", but in both cases the attributes of the containing
directory are transferred to the containing directory on the
destination.  In other words, each of the following commands
copies the files in the same way, including their setting of the
attributes of /dest/foo:

    rsync -av /src/foo /dest
    rsync -av /src/foo/ /dest/foo

Note also that host and module references don't require a trailing
slash to copy the contents of the default directory.  For example,
both of these copy the remote directory's contents into "/dest":

    rsync -av host: /dest
    rsync -av host::module /dest

You can also use rsync in local-only mode, where both the source
and destination don't have a ':' in the name.  In this case it
behaves like an improved copy command.

Finally, you can list all the (listable) modules available from a
particular rsync daemon by leaving off the module name:

    rsync somehost.mydomain.com::


## COPYING TO A DIFFERENT NAME

When you want to copy a directory to a different name, use a
trailing slash on the source directory to put the contents of the
directory into any destination directory you like:

    rsync -ai foo/ bar/

Rsync also has the ability to customize a destination file's name
when copying a single item.  The rules for this are:

o      The transfer list must consist of a single item (either a
       file or an empty directory)

o      The final element of the destination path must not exist as
       a directory

o      The destination path must not have been specified with a
       trailing slash

Under those circumstances, rsync will set the name of the
destination's single item to the last element of the destination
path.  Keep in mind that it is best to only use this idiom when
copying a file and use the above trailing-slash idiom when copying
a directory.

The following example copies the foo.c file as bar.c in the save
dir (assuming that bar.c isn't a directory):

    rsync -ai src/foo.c save/bar.c

The single-item copy rule might accidentally bite you if you
unknowingly copy a single item and specify a destination dir that
doesn't exist (without using a trailing slash).  For example, if
src/*.c matches one file and save/dir doesn't exist, this will
confuse you by naming the destination file save/dir:

    rsync -ai src/*.c save/dir

To prevent such an accident, either make sure the destination dir
exists or specify the destination path with a trailing slash:

    rsync -ai src/*.c save/dir/


## SORTED TRANSFER ORDER

Rsync always sorts the specified filenames into its internal
transfer list.  This handles the merging together of the contents
of identically named directories, makes it easy to remove
duplicate filenames. It can, however, confuse someone when the
files are transferred in a different order than what was given on
the command-line.

If you need a particular file to be transferred prior to another,
either separate the files into different rsync calls, or consider
using --delay-updates (which doesn't affect the sorted transfer
order, but does make the final file-updating phase happen much
more rapidly).


## MULTI-HOST SECURITY

Rsync takes steps to ensure that the file requests that are shared
in a transfer are protected against various security issues.  Most
of the potential problems arise on the receiving side where rsync
takes steps to ensure that the list of files being transferred
remains within the bounds of what was requested.

Toward this end, rsync 3.1.2 and later have aborted when a file
list contains an absolute or relative path that tries to escape
out of the top of the transfer.  Also, beginning with version
3.2.5, rsync does two more safety checks of the file list to (1)
ensure that no extra source arguments were added into the transfer
other than those that the client requested and (2) ensure that the
file list obeys the exclude rules that were sent to the sender.

For those that don't yet have a 3.2.5 client rsync (or those that
want to be extra careful), it is safest to do a copy into a
dedicated destination directory for the remote files when you
don't trust the remote host.  For example, instead of doing an
rsync copy into your home directory:

    rsync -aiv host1:dir1 ~

Dedicate a "host1-files" dir to the remote content:

    rsync -aiv host1:dir1 ~/host1-files

See the --trust-sender option for additional details.

CAUTION: it is not particularly safe to use rsync to copy files
from a case-preserving filesystem to a case-ignoring filesystem.
If you must perform such a copy, you should either disable
symlinks via --no-links or enable the munging of symlinks via
--munge-links (and make sure you use the right local or remote
option).  This will prevent rsync from doing potentially dangerous
things if a symlink name overlaps with a file or directory. It
does not, however, ensure that you get a full copy of all the
files (since that may not be possible when the names overlap). A
potentially better solution is to list all the source files and
create a safe list of filenames that you pass to the --files-from
option.  Any files that conflict in name would need to be copied
to different destination directories using more than one copy.

While a copy of a case-ignoring filesystem to a case-ignoring
filesystem can work out fairly well, if no --delete-during or
--delete-before option is active, rsync can potentially update an
existing file on the receiving side without noticing that the
upper-/lower-case of the filename should be changed to match the
sender.


## ADVANCED USAGE

The syntax for requesting multiple files from a remote host is
done by specifying additional remote-host args in the same style
as the first, or with the hostname omitted.  For instance, all
these work:

    rsync -aiv host:file1 :file2 host:file{3,4} /dest/
    rsync -aiv host::modname/file{1,2} host::modname/extra /dest/
    rsync -aiv host::modname/first ::extra-file{1,2} /dest/

Note that a daemon connection only supports accessing one module
per copy command, so if the start of a follow-up path doesn't
begin with the modname of the first path, it is assumed to be a
path in the module (such as the extra-file1 & extra-file2 that are
grabbed above).

Really old versions of rsync (2.6.9 and before) only allowed
specifying one remote-source arg, so some people have instead
relied on the remote-shell performing space splitting to break up
an arg into multiple paths. Such unintuitive behavior is no longer
supported by default (though you can request it, as described
below).

Starting in 3.2.4, filenames are passed to a remote shell in such
a way as to preserve the characters you give it. Thus, if you ask
for a file with spaces in the name, that's what the remote rsync
looks for:

    rsync -aiv host:'a simple file.pdf' /dest/

If you use scripts that have been written to manually apply extra
quoting to the remote rsync args (or to require remote arg
splitting), you can ask rsync to let your script handle the extra
escaping.  This is done by either adding the --old-args option to
the rsync runs in the script (which requires a new rsync) or
exporting RSYNC_OLD_ARGS=1 and RSYNC_PROTECT_ARGS=0 (which works
with old or new rsync versions).


## CONNECTING TO AN RSYNC DAEMON

It is also possible to use rsync without a remote shell as the
transport.  In this case you will directly connect to a remote
rsync daemon, typically using TCP port 873. (This obviously
requires the daemon to be running on the remote system, so refer
to the STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS section
below for information on that.)

Using rsync in this way is the same as using it with a remote
shell except that:

o      Use either double-colon syntax or rsync:// URL syntax
       instead of the single-colon (remote shell) syntax.

o      The first element of the "path" is actually a module name.

o      Additional remote source args can use an abbreviated syntax
       that omits the hostname and/or the module name, as
       discussed in ADVANCED USAGE.

o      The remote daemon may print a "message of the day" when you
       connect.

o      If you specify only the host (with no module or path) then
       a list of accessible modules on the daemon is output.

o      If you specify a remote source path but no destination, a
       listing of the matching files on the remote daemon is
       output.

o      The --rsh (-e) option must be omitted to avoid changing the
       connection style from using a socket connection to USING
       RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION.

An example that copies all the files in a remote module named
"src":

    rsync -av host::src /dest

Some modules on the remote daemon may require authentication.  If
so, you will receive a password prompt when you connect.  You can
avoid the password prompt by setting the environment variable
RSYNC_PASSWORD to the password you want to use or using the
--password-file option.  This may be useful when scripting rsync.

WARNING: On some systems environment variables are visible to all
users.  On those systems using --password-file is recommended.

You may establish the connection via a web proxy by setting the
environment variable RSYNC_PROXY to a hostname:port pair pointing
to your web proxy.  Note that your web proxy's configuration must
support proxy connections to port 873.

You may also establish a daemon connection using a program as a
proxy by setting the environment variable RSYNC_CONNECT_PROG to
the commands you wish to run in place of making a direct socket
connection.  The string may contain the escape "%H" to represent
the hostname specified in the rsync command (so use "%%" if you
need a single "%" in your string).  For example:

    export RSYNC_CONNECT_PROG='ssh proxyhost nc %H 873'
    rsync -av targethost1::module/src/ /dest/
    rsync -av rsync://targethost2/module/src/ /dest/

The command specified above uses ssh to run nc (netcat) on a
proxyhost, which forwards all data to port 873 (the rsync daemon)
on the targethost (%H).

Note also that if the RSYNC_SHELL environment variable is set,
that program will be used to run the RSYNC_CONNECT_PROG command
instead of using the default shell of the system() call.


## USING RSYNC-DAEMON FEATURES VIA A REMOTE-SHELL CONNECTION         top

It is sometimes useful to use various features of an rsync daemon
(such as named modules) without actually allowing any new socket
connections into a system (other than what is already required to
allow remote-shell access).  Rsync supports connecting to a host
using a remote shell and then spawning a single-use "daemon"
server that expects to read its config file in the home dir of the
remote user.  This can be useful if you want to encrypt a daemon-
style transfer's data, but since the daemon is started up fresh by
the remote user, you may not be able to use features such as
chroot or change the uid used by the daemon. (For another way to
encrypt a daemon transfer, consider using ssh to tunnel a local
port to a remote machine and configure a normal rsync daemon on
that remote host to only allow connections from "localhost".)

From the user's perspective, a daemon transfer via a remote-shell
connection uses nearly the same command-line syntax as a normal
rsync-daemon transfer, with the only exception being that you must
explicitly set the remote shell program on the command-line with
the --rsh=COMMAND option. (Setting the RSYNC_RSH in the
environment will not turn on this functionality.) For example:

    rsync -av --rsh=ssh host::module /dest

If you need to specify a different remote-shell user, keep in mind
that the user@ prefix in front of the host is specifying the
rsync-user value (for a module that requires user-based
authentication).  This means that you must give the '-l user'
option to ssh when specifying the remote-shell, as in this example
that uses the short version of the --rsh option:

    rsync -av -e "ssh -l ssh-user" rsync-user@host::module /dest

The "ssh-user" will be used at the ssh level; the "rsync-user"
will be used to log-in to the "module".

In this setup, the daemon is started by the ssh command that is
accessing the system (which can be forced via the
~/.ssh/authorized_keys file, if desired).  However, when accessing
a daemon directly, it needs to be started beforehand.


## STARTING AN RSYNC DAEMON TO ACCEPT CONNECTIONS         top

In order to connect to an rsync daemon, the remote system needs to
have a daemon already running (or it needs to have configured
something like inetd to spawn an rsync daemon for incoming
connections on a particular port).  For full information on how to
start a daemon that will handling incoming socket connections, see
the rsyncd.conf(5) manpage -- that is the config file for the
daemon, and it contains the full details for how to run the daemon
(including stand-alone and inetd configurations).

If you're using one of the remote-shell transports for the
transfer, there is no need to manually start an rsync daemon.


## EXAMPLES

Here are some examples of how rsync can be used.

To backup a home directory, which consists of large MS Word files
and mail folders, a per-user cron job can be used that runs this
each day:

    rsync -aiz . bkhost:backup/joe/

To move some files from a remote host to the local host, you could
run:

    rsync -aiv --remove-source-files rhost:/tmp/{file1,file2}.c ~/src/


## OPTION SUMMARY

Here is a short summary of the options available in rsync.  Each
option also has its own detailed description later in this
manpage.

--verbose, -v            increase verbosity
--info=FLAGS             fine-grained informational verbosity
--debug=FLAGS            fine-grained debug verbosity
--stderr=e|a|c           change stderr output mode (default: errors)
--quiet, -q              suppress non-error messages
--no-motd                suppress daemon-mode MOTD
--checksum, -c           skip based on checksum, not mod-time & size
--archive, -a            archive mode is -rlptgoD (no -A,-X,-U,-N,-H)
--no-OPTION              turn off an implied OPTION (e.g. --no-D)
--recursive, -r          recurse into directories
--relative, -R           use relative path names
--no-implied-dirs        don't send implied dirs with --relative
--backup, -b             make backups (see --suffix & --backup-dir)
--backup-dir=DIR         make backups into hierarchy based in DIR
--suffix=SUFFIX          backup suffix (default ~ w/o --backup-dir)
--update, -u             skip files that are newer on the receiver
--inplace                update destination files in-place
--append                 append data onto shorter files
--append-verify          --append w/old data in file checksum
--dirs, -d               transfer directories without recursing
--old-dirs, --old-d      works like --dirs when talking to old rsync
--mkpath                 create destination's missing path components
--links, -l              copy symlinks as symlinks
--copy-links, -L         transform symlink into referent file/dir
--copy-unsafe-links      only "unsafe" symlinks are transformed
--safe-links             ignore symlinks that point outside the tree
--munge-links            munge symlinks to make them safe & unusable
--copy-dirlinks, -k      transform symlink to dir into referent dir
--keep-dirlinks, -K      treat symlinked dir on receiver as dir
--hard-links, -H         preserve hard links
--perms, -p              preserve permissions
--executability, -E      preserve executability
--chmod=CHMOD            affect file and/or directory permissions
--acls, -A               preserve ACLs (implies --perms)
--xattrs, -X             preserve extended attributes
--owner, -o              preserve owner (super-user only)
--group, -g              preserve group
--devices                preserve device files (super-user only)
--copy-devices           copy device contents as a regular file
--write-devices          write to devices as files (implies --inplace)
--specials               preserve special files
-D                       same as --devices --specials
--times, -t              preserve modification times
--atimes, -U             preserve access (use) times
--open-noatime           avoid changing the atime on opened files
--crtimes, -N            preserve create times (newness)
--omit-dir-times, -O     omit directories from --times
--omit-link-times, -J    omit symlinks from --times
--super                  receiver attempts super-user activities
--fake-super             store/recover privileged attrs using xattrs
--sparse, -S             turn sequences of nulls into sparse blocks
--preallocate            allocate dest files before writing them
--dry-run, -n            perform a trial run with no changes made
--whole-file, -W         copy files whole (w/o delta-xfer algorithm)
--checksum-choice=STR    choose the checksum algorithm (aka --cc)
--one-file-system, -x    don't cross filesystem boundaries
--block-size=SIZE, -B    force a fixed checksum block-size
--rsh=COMMAND, -e        specify the remote shell to use
--rsync-path=PROGRAM     specify the rsync to run on remote machine
--existing               skip creating new files on receiver
--ignore-existing        skip updating files that exist on receiver
--remove-source-files    sender removes synchronized files (non-dir)
--del                    an alias for --delete-during
--delete                 delete extraneous files from dest dirs
--delete-before          receiver deletes before xfer, not during
--delete-during          receiver deletes during the transfer
--delete-delay           find deletions during, delete after
--delete-after           receiver deletes after transfer, not during
--delete-excluded        also delete excluded files from dest dirs
--ignore-missing-args    ignore missing source args without error
--delete-missing-args    delete missing source args from destination
--ignore-errors          delete even if there are I/O errors
--force                  force deletion of dirs even if not empty
--max-delete=NUM         don't delete more than NUM files
--max-size=SIZE          don't transfer any file larger than SIZE
--min-size=SIZE          don't transfer any file smaller than SIZE
--max-alloc=SIZE         change a limit relating to memory alloc
--partial                keep partially transferred files
--partial-dir=DIR        put a partially transferred file into DIR
--delay-updates          put all updated files into place at end
--prune-empty-dirs, -m   prune empty directory chains from file-list
--numeric-ids            don't map uid/gid values by user/group name
--usermap=STRING         custom username mapping
--groupmap=STRING        custom groupname mapping
--chown=USER:GROUP       simple username/groupname mapping
--timeout=SECONDS        set I/O timeout in seconds
--contimeout=SECONDS     set daemon connection timeout in seconds
--ignore-times, -I       don't skip files that match size and time
--size-only              skip files that match in size
--modify-window=NUM, -@  set the accuracy for mod-time comparisons
--temp-dir=DIR, -T       create temporary files in directory DIR
--fuzzy, -y              find similar file for basis if no dest file
--compare-dest=DIR       also compare destination files relative to DIR
--copy-dest=DIR          ... and include copies of unchanged files
--link-dest=DIR          hardlink to files in DIR when unchanged
--compress, -z           compress file data during the transfer
--compress-choice=STR    choose the compression algorithm (aka --zc)
--compress-level=NUM     explicitly set compression level (aka --zl)
--compress-threads=NUM   explicitly set compression threads (aka --zt)
--skip-compress=LIST     skip compressing files with suffix in LIST
--cvs-exclude, -C        auto-ignore files in the same way CVS does
--filter=RULE, -f        add a file-filtering RULE
-F                       same as --filter='dir-merge /.rsync-filter'
                         repeated: --filter='- .rsync-filter'
--exclude=PATTERN        exclude files matching PATTERN
--exclude-from=FILE      read exclude patterns from FILE
--include=PATTERN        don't exclude files matching PATTERN
--include-from=FILE      read include patterns from FILE
--files-from=FILE        read list of source-file names from FILE
--from0, -0              all *-from/filter files are delimited by 0s
--old-args               disable the modern arg-protection idiom
--secluded-args, -s      use the protocol to safely send the args
--trust-sender           trust the remote sender's file list
--copy-as=USER[:GROUP]   specify user & optional group for the copy
--address=ADDRESS        bind address for outgoing socket to daemon
--port=PORT              specify double-colon alternate port number
--sockopts=OPTIONS       specify custom TCP options
--blocking-io            use blocking I/O for the remote shell
--outbuf=N|L|B           set out buffering to None, Line, or Block
--stats                  give some file-transfer stats
--8-bit-output, -8       leave high-bit chars unescaped in output
--human-readable, -h     output numbers in a human-readable format
--progress               show progress during transfer
-P                       same as --partial --progress
--itemize-changes, -i    output a change-summary for all updates
--remote-option=OPT, -M  send OPTION to the remote side only
--out-format=FORMAT      output updates using the specified FORMAT
--log-file=FILE          log what we're doing to the specified FILE
--log-file-format=FMT    log updates using the specified FMT
--password-file=FILE     read daemon-access password from FILE
--early-input=FILE       use FILE for daemon's early exec input
--list-only              list the files instead of copying them
--bwlimit=RATE           limit socket I/O bandwidth
--stop-after=MINS        Stop rsync after MINS minutes have elapsed
--stop-at=y-m-dTh:m      Stop rsync at the specified point in time
--fsync                  fsync every written file
--write-batch=FILE       write a batched update to FILE
--only-write-batch=FILE  like --write-batch but w/o updating dest
--read-batch=FILE        read a batched update from FILE
--protocol=NUM           force an older protocol version to be used
--iconv=CONVERT_SPEC     request charset conversion of filenames
--checksum-seed=NUM      set block/file checksum seed (advanced)
--ipv4, -4               prefer IPv4
--ipv6, -6               prefer IPv6
--version, -V            print the version + other info and exit
--help, -h (*)           show this help (* -h is help only on its own)

Rsync can also be run as a daemon, in which case the following
options are accepted:

--daemon                 run as an rsync daemon
--address=ADDRESS        bind to the specified address
--bwlimit=RATE           limit socket I/O bandwidth
--config=FILE            specify alternate rsyncd.conf file
--dparam=OVERRIDE, -M    override global daemon config parameter
--no-detach              do not detach from the parent
--port=PORT              listen on alternate port number
--log-file=FILE          override the "log file" setting
--log-file-format=FMT    override the "log format" setting
--sockopts=OPTIONS       specify custom TCP options
--verbose, -v            increase verbosity
--ipv4, -4               prefer IPv4
--ipv6, -6               prefer IPv6
--help, -h               show this help (when used with --daemon)
