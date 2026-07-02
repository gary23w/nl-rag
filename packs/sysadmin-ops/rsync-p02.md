---
title: "rsync(1) (part 2/5)"
source: https://man7.org/linux/man-pages/man1/rsync.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 2/5
---

## OPTIONS

Rsync accepts both long (double-dash + word) and short (single-
dash + letter) options.  The full list of the available options
are described below.  If an option can be specified in more than
one way, the choices are comma-separated.  Some options only have
a long variant, not a short.

If the option takes a parameter, the parameter is only listed
after the long variant, even though it must also be specified for
the short.  When specifying a parameter, you can either use the
form --option=param, --option param, -o=param, -o param, or
-oparam (the latter choices assume that your option has a short
variant).

The parameter may need to be quoted in some manner for it to
survive the shell's command-line parsing.  Also keep in mind that
a leading tilde (~) in a pathname is substituted by your shell, so
make sure that you separate the option name from the pathname
using a space if you want the local shell to expand it.

--help Print a short help page describing the options available in
       rsync and exit.  You can also use -h for --help when it is
       used without any other options (since it normally means
       --human-readable).

--version, -V
       Print the rsync version plus other info and exit.  When
       repeated, the information is output is a JSON format that
       is still fairly readable (client side only).

       The output includes a list of compiled-in capabilities, a
       list of optimizations, the default list of checksum
       algorithms, the default list of compression algorithms, the
       default list of daemon auth digests, a link to the rsync
       web site, and a few other items.

--verbose, -v
       This option increases the amount of information you are
       given during the transfer.  By default, rsync works
       silently.  A single -v will give you information about what
       files are being transferred and a brief summary at the end.
       Two -v options will give you information on what files are
       being skipped and slightly more information at the end.
       More than two -v options should only be used if you are
       debugging rsync.

       The end-of-run summary tells you the number of bytes sent
       to the remote rsync (which is the receiving side on a local
       copy), the number of bytes received from the remote host,
       and the average bytes per second of the transferred data
       computed over the entire length of the rsync run. The
       second line shows the total size (in bytes), which is the
       sum of all the file sizes that rsync considered
       transferring.  It also shows a "speedup" value, which is a
       ratio of the total file size divided by the sum of the sent
       and received bytes (which is really just a feel-good
       bigger-is-better number).  Note that these byte values can
       be made more (or less) human-readable by using the
       --human-readable (or --no-human-readable) options.

       In a modern rsync, the -v option is equivalent to the
       setting of groups of --info and --debug options.  You can
       choose to use these newer options in addition to, or in
       place of using --verbose, as any fine-grained settings
       override the implied settings of -v.  Both --info and
       --debug have a way to ask for help that tells you exactly
       what flags are set for each increase in verbosity.

       However, do keep in mind that a daemon's "max verbosity"
       setting will limit how high of a level the various
       individual flags can be set on the daemon side.  For
       instance, if the max is 2, then any info and/or debug flag
       that is set to a higher value than what would be set by -vv
       will be downgraded to the -vv level in the daemon's
       logging.

--info=FLAGS
       This option lets you have fine-grained control over the
       information output you want to see.  An individual flag
       name may be followed by a level number, with 0 meaning to
       silence that output, 1 being the default output level, and
       higher numbers increasing the output of that flag (for
       those that support higher levels).  Use --info=help to see
       all the available flag names, what they output, and what
       flag names are added for each increase in the verbose
       level.  Some examples:

           rsync -a --info=progress2 src/ dest/
           rsync -avv --info=stats2,misc1,flist0 src/ dest/

       Note that --info=name's output is affected by the
       --out-format and --itemize-changes (-i) options.  See those
       options for more information on what is output and when.

       This option was added to 3.1.0, so an older rsync on the
       server side might reject your attempts at fine-grained
       control (if one or more flags needed to be send to the
       server and the server was too old to understand them).  See
       also the "max verbosity" caveat above when dealing with a
       daemon.

--debug=FLAGS
       This option lets you have fine-grained control over the
       debug output you want to see.  An individual flag name may
       be followed by a level number, with 0 meaning to silence
       that output, 1 being the default output level, and higher
       numbers increasing the output of that flag (for those that
       support higher levels).  Use --debug=help to see all the
       available flag names, what they output, and what flag names
       are added for each increase in the verbose level.  Some
       examples:

           rsync -avvv --debug=none src/ dest/
           rsync -avA --del --debug=del2,acl src/ dest/

       Note that some debug messages will only be output when the
       --stderr=all option is specified, especially those
       pertaining to I/O and buffer debugging.

       Beginning in 3.2.0, this option is no longer auto-forwarded
       to the server side in order to allow you to specify
       different debug values for each side of the transfer, as
       well as to specify a new debug option that is only present
       in one of the rsync versions.  If you want to duplicate the
       same option on both sides, using brace expansion is an easy
       way to save you some typing.  This works in zsh and bash:

           rsync -aiv {-M,}--debug=del2 src/ dest/

--stderr=errors|all|client
       This option controls which processes output to stderr and
       if info messages are also changed to stderr.  The mode
       strings can be abbreviated, so feel free to use a single
       letter value.  The 3 possible choices are:

       o      errors - (the default) causes all the rsync
              processes to send an error directly to stderr, even
              if the process is on the remote side of the
              transfer.  Info messages are sent to the client side
              via the protocol stream.  If stderr is not available
              (i.e. when directly connecting with a daemon via a
              socket) errors fall back to being sent via the
              protocol stream.

       o      all - causes all rsync messages (info and error) to
              get written directly to stderr from all (possible)
              processes.  This causes stderr to become line-
              buffered (instead of raw) and eliminates the ability
              to divide up the info and error messages by file
              handle.  For those doing debugging or using several
              levels of verbosity, this option can help to avoid
              clogging up the transfer stream (which should
              prevent any chance of a deadlock bug hanging things
              up).  It also allows --debug to enable some extra
              I/O related messages.

       o      client - causes all rsync messages to be sent to the
              client side via the protocol stream.  One client
              process outputs all messages, with errors on stderr
              and info messages on stdout.  This was the default
              in older rsync versions, but can cause error delays
              when a lot of transfer data is ahead of the
              messages.  If you're pushing files to an older
              rsync, you may want to use --stderr=all since that
              idiom has been around for several releases.

       This option was added in rsync 3.2.3.  This version also
       began the forwarding of a non-default setting to the remote
       side, though rsync uses the backward-compatible options
       --msgs2stderr and --no-msgs2stderr to represent the all and
       client settings, respectively.  A newer rsync will continue
       to accept these older option names to maintain
       compatibility.

--quiet, -q
       This option decreases the amount of information you are
       given during the transfer, notably suppressing information
       messages from the remote server.  This option is useful
       when invoking rsync from cron.

--no-motd
       This option affects the information that is output by the
       client at the start of a daemon transfer.  This suppresses
       the message-of-the-day (MOTD) text, but it also affects the
       list of modules that the daemon sends in response to the
       "rsync host::" request (due to a limitation in the rsync
       protocol), so omit this option if you want to request the
       list of modules from the daemon.

--ignore-times, -I
       Normally rsync will skip any files that are already the
       same size and have the same modification timestamp.  This
       option turns off this "quick check" behavior, causing all
       files to be updated.

       This option can be confusing compared to --ignore-existing
       and --ignore-non-existing in that that they cause rsync to
       transfer fewer files, while this option causes rsync to
       transfer more files.

--size-only
       This modifies rsync's "quick check" algorithm for finding
       files that need to be transferred, changing it from the
       default of transferring files with either a changed size or
       a changed last-modified time to just looking for files that
       have changed in size.  This is useful when starting to use
       rsync after using another mirroring system which may not
       preserve timestamps exactly.

--modify-window=NUM, -@
       When comparing two timestamps, rsync treats the timestamps
       as being equal if they differ by no more than the modify-
       window value.  The default is 0, which matches just integer
       seconds.  If you specify a negative value (and the receiver
       is at least version 3.1.3) then nanoseconds will also be
       taken into account.  Specifying 1 is useful for copies
       to/from MS Windows FAT filesystems, because FAT represents
       times with a 2-second resolution (allowing times to differ
       from the original by up to 1 second).

       If you want all your transfers to default to comparing
       nanoseconds, you can create a ~/.popt file and put these
       lines in it:

           rsync alias -a -a@-1
           rsync alias -t -t@-1

       With that as the default, you'd need to specify
       --modify-window=0 (aka -@0) to override it and ignore
       nanoseconds, e.g. if you're copying between ext3 and ext4,
       or if the receiving rsync is older than 3.1.3.

--checksum, -c
       This changes the way rsync checks if the files have been
       changed and are in need of a transfer.  Without this
       option, rsync uses a "quick check" that (by default) checks
       if each file's size and time of last modification match
       between the sender and receiver.  This option changes this
       to compare a 128-bit checksum for each file that has a
       matching size.  Generating the checksums means that both
       sides will expend a lot of disk I/O reading all the data in
       the files in the transfer, so this can slow things down
       significantly (and this is prior to any reading that will
       be done to transfer changed files)

       The sending side generates its checksums while it is doing
       the file-system scan that builds the list of the available
       files.  The receiver generates its checksums when it is
       scanning for changed files, and will checksum any file that
       has the same size as the corresponding sender's file: files
       with either a changed size or a changed checksum are
       selected for transfer.

       Note that rsync always verifies that each transferred file
       was correctly reconstructed on the receiving side by
       checking a whole-file checksum that is generated as the
       file is transferred, but that automatic after-the-transfer
       verification has nothing to do with this option's before-
       the-transfer "Does this file need to be updated?" check.

       The checksum used is auto-negotiated between the client and
       the server, but can be overridden using either the
       --checksum-choice (--cc) option or an environment variable
       that is discussed in that option's section.

--archive, -a
       This is equivalent to -rlptgoD.  It is a quick way of
       saying you want recursion and want to preserve almost
       everything.  Be aware that it does not include preserving
       ACLs (-A), xattrs (-X), atimes (-U), crtimes (-N), nor the
       finding and preserving of hardlinks (-H).

       The only exception to the above equivalence is when
       --files-from is specified, in which case -r is not implied.

--no-OPTION
       You may turn off one or more implied options by prefixing
       the option name with "no-".  Not all positive options have
       a negated opposite, but a lot do, including those that can
       be used to disable an implied option (e.g.  --no-D,
       --no-perms) or have different defaults in various
       circumstances (e.g. --no-whole-file, --no-blocking-io,
       --no-dirs).  Every valid negated option accepts both the
       short and the long option name after the "no-" prefix (e.g.
       --no-R is the same as --no-relative).

       As an example, if you want to use --archive (-a) but don't
       want --owner (-o), instead of converting -a into -rlptgD,
       you can specify -a --no-o (aka --archive --no-owner).

       The order of the options is important: if you specify
       --no-r -a, the -r option would end up being turned on, the
       opposite of -a --no-r.  Note also that the side-effects of
       the --files-from option are NOT positional, as it affects
       the default state of several options and slightly changes
       the meaning of -a (see the --files-from option for more
       details).

--recursive, -r
       This tells rsync to copy directories recursively.  See also
       --dirs (-d) for an option that allows the scanning of a
       single directory.

       See the --inc-recursive option for a discussion of the
       incremental recursion for creating the list of files to
       transfer.

--inc-recursive, --i-r
       This option explicitly enables on incremental recursion
       when scanning for files, which is enabled by default when
       using the --recursive option and both sides of the transfer
       are running rsync 3.0.0 or newer.

       Incremental recursion uses much less memory than non-
       incremental, while also beginning the transfer more quickly
       (since it doesn't need to scan the entire transfer
       hierarchy before it starts transferring files).  If no
       recursion is enabled in the source files, this option has
       no effect.

       Some options require rsync to know the full file list, so
       these options disable the incremental recursion mode.
       These include:

       o      --delete-before (the old default of --delete)

       o      --delete-after

       o      --prune-empty-dirs

       o      --delay-updates

       In order to make --delete compatible with incremental
       recursion, rsync 3.0.0 made --delete-during the default
       delete mode (which was first added in 2.6.4).

       One side-effect of incremental recursion is that any
       missing sub-directories inside a recursively-scanned
       directory are (by default) created prior to recursing into
       the sub-dirs.  This earlier creation point (compared to a
       non-incremental recursion) allows rsync to then set the
       modify time of the finished directory right away (without
       having to delay that until a bunch of recursive copying has
       finished).  However, these early directories don't yet have
       their completed mode, mtime, or ownership set -- they have
       more restrictive rights until the subdirectory's copying
       actually begins.  This early-creation idiom can be avoided
       by using the --omit-dir-times option.

       Incremental recursion can be disabled using the
       --no-inc-recursive (--no-i-r) option.

--no-inc-recursive, --no-i-r
       Disables the new incremental recursion algorithm of the
       --recursive option.  This makes rsync scan the full file
       list before it begins to transfer files.  See
       --inc-recursive for more info.

--relative, -R
       Use relative paths.  This means that the full path names
       specified on the command line are sent to the server rather
       than just the last parts of the filenames.  This is
       particularly useful when you want to send several different
       directories at the same time.  For example, if you used
       this command:

           rsync -av /foo/bar/baz.c remote:/tmp/

       would create a file named baz.c in /tmp/ on the remote
       machine.  If instead you used

           rsync -avR /foo/bar/baz.c remote:/tmp/

       then a file named /tmp/foo/bar/baz.c would be created on
       the remote machine, preserving its full path.  These extra
       path elements are called "implied directories" (i.e. the
       "foo" and the "foo/bar" directories in the above example).

       Beginning with rsync 3.0.0, rsync always sends these
       implied directories as real directories in the file list,
       even if a path element is really a symlink on the sending
       side.  This prevents some really unexpected behaviors when
       copying the full path of a file that you didn't realize had
       a symlink in its path.  If you want to duplicate a server-
       side symlink, include both the symlink via its path, and
       referent directory via its real path.  If you're dealing
       with an older rsync on the sending side, you may need to
       use the --no-implied-dirs option.

       It is also possible to limit the amount of path information
       that is sent as implied directories for each path you
       specify.  With a modern rsync on the sending side
       (beginning with 2.6.7), you can insert a dot and a slash
       into the source path, like this:

           rsync -avR /foo/./bar/baz.c remote:/tmp/

       That would create /tmp/bar/baz.c on the remote machine.
       (Note that the dot must be followed by a slash, so "/foo/."
       would not be abbreviated.) For older rsync versions, you
       would need to use a chdir to limit the source path.  For
       example, when pushing files:

           (cd /foo; rsync -avR bar/baz.c remote:/tmp/)

       (Note that the parens put the two commands into a sub-
       shell, so that the "cd" command doesn't remain in effect
       for future commands.) If you're pulling files from an older
       rsync, use this idiom (but only for a non-daemon transfer):

           rsync -avR --rsync-path="cd /foo; rsync" \
                remote:bar/baz.c /tmp/

--no-implied-dirs
       This option affects the default behavior of the --relative
       option.  When it is specified, the attributes of the
       implied directories from the source names are not included
       in the transfer.  This means that the corresponding path
       elements on the destination system are left unchanged if
       they exist, and any missing implied directories are created
       with default attributes.  This even allows these implied
       path elements to have big differences, such as being a
       symlink to a directory on the receiving side.

       For instance, if a command-line arg or a files-from entry
       told rsync to transfer the file "path/foo/file", the
       directories "path" and "path/foo" are implied when
       --relative is used.  If "path/foo" is a symlink to "bar" on
       the destination system, the receiving rsync would
       ordinarily delete "path/foo", recreate it as a directory,
       and receive the file into the new directory.  With
       --no-implied-dirs, the receiving rsync updates
       "path/foo/file" using the existing path elements, which
       means that the file ends up being created in "path/bar".
       Another way to accomplish this link preservation is to use
       the --keep-dirlinks option (which will also affect symlinks
       to directories in the rest of the transfer).

       When pulling files from an rsync older than 3.0.0, you may
       need to use this option if the sending side has a symlink
       in the path you request and you wish the implied
       directories to be transferred as normal directories.

--backup, -b
       With this option, preexisting destination files are renamed
       as each file is transferred or deleted.  You can control
       where the backup file goes and what (if any) suffix gets
       appended using the --backup-dir and --suffix options.

       If you don't specify --backup-dir:

       1.     the --omit-dir-times option will be forced on

       2.     the use of --delete (without --delete-excluded),
              causes rsync to add a "protect" filter-rule for the
              backup suffix to the end of all your existing
              filters that looks like this: -f "P *~".  This rule
              prevents previously backed-up files from being
              deleted.

       Note that if you are supplying your own filter rules, you
       may need to manually insert your own exclude/protect rule
       somewhere higher up in the list so that it has a high
       enough priority to be effective (e.g. if your rules specify
       a trailing inclusion/exclusion of *, the auto-added rule
       would never be reached).

--backup-dir=DIR
       This implies the --backup option, and tells rsync to store
       all backups in the specified directory on the receiving
       side.  This can be used for incremental backups.  You can
       additionally specify a backup suffix using the --suffix
       option (otherwise the files backed up in the specified
       directory will keep their original filenames).

       Note that if you specify a relative path, the backup
       directory will be relative to the destination directory, so
       you probably want to specify either an absolute path or a
       path that starts with "../".  If an rsync daemon is the
       receiver, the backup dir cannot go outside the module's
       path hierarchy, so take extra care not to delete it or copy
       into it.

--suffix=SUFFIX
       This option allows you to override the default backup
       suffix used with the --backup (-b) option.  The default
       suffix is a ~ if no --backup-dir was specified, otherwise
       it is an empty string.

--update, -u
       This forces rsync to skip any files which exist on the
       destination and have a modified time that is newer than the
       source file. (If an existing destination file has a
       modification time equal to the source file's, it will be
       updated if the sizes are different.)

       Note that this does not affect the copying of dirs,
       symlinks, or other special files.  Also, a difference of
       file format between the sender and receiver is always
       considered to be important enough for an update, no matter
       what date is on the objects.  In other words, if the source
       has a directory where the destination has a file, the
       transfer would occur regardless of the timestamps.

       This option is a TRANSFER RULE, so don't expect any exclude
       side effects.

       A caution for those that choose to combine --inplace with
       --update: an interrupted transfer will leave behind a
       partial file on the receiving side that has a very recent
       modified time, so re-running the transfer will probably not
       continue the interrupted file.  As such, it is usually best
       to avoid combining this with --inplace unless you have
       implemented manual steps to handle any interrupted in-
       progress files.

--inplace
       This option changes how rsync transfers a file when its
       data needs to be updated: instead of the default method of
       creating a new copy of the file and moving it into place
       when it is complete, rsync instead writes the updated data
       directly to the destination file.

       This has several effects:

       o      Hard links are not broken.  This means the new data
              will be visible through other hard links to the
              destination file.  Moreover, attempts to copy
              differing source files onto a multiply-linked
              destination file will result in a "tug of war" with
              the destination data changing back and forth.

       o      In-use binaries cannot be updated (either the OS
              will prevent this from happening, or binaries that
              attempt to swap-in their data will misbehave or
              crash).

       o      The file's data will be in an inconsistent state
              during the transfer and will be left that way if the
              transfer is interrupted or if an update fails.

       o      A file that rsync cannot write to cannot be updated.
              While a super user can update any file, a normal
              user needs to be granted write permission for the
              open of the file for writing to be successful.

       o      The efficiency of rsync's delta-transfer algorithm
              may be reduced if some data in the destination file
              is overwritten before it can be copied to a position
              later in the file.  This does not apply if you use
              --backup, since rsync is smart enough to use the
              backup file as the basis file for the transfer.

       WARNING: you should not use this option to update files
       that are being accessed by others, so be careful when
       choosing to use this for a copy.

       This option is useful for transferring large files with
       block-based changes or appended data, and also on systems
       that are disk bound, not network bound.  It can also help
       keep a copy-on-write filesystem snapshot from diverging the
       entire contents of a file that only has minor changes.

       The option implies --partial (since an interrupted transfer
       does not delete the file), but conflicts with --partial-dir
       and --delay-updates.  Prior to rsync 2.6.4 --inplace was
       also incompatible with --compare-dest and --link-dest.

--append
       This special copy mode only works to efficiently update
       files that are known to be growing larger where any
       existing content on the receiving side is also known to be
       the same as the content on the sender.  The use of --append
       can be dangerous if you aren't 100% sure that all the files
       in the transfer are shared, growing files.  You should thus
       use filter rules to ensure that you weed out any files that
       do not fit this criteria.

       Rsync updates these growing file in-place without verifying
       any of the existing content in the file (it only verifies
       the content that it is appending).  Rsync skips any files
       that exist on the receiving side that are not shorter than
       the associated file on the sending side (which means that
       new files are transferred).  It also skips any files whose
       size on the sending side gets shorter during the send
       negotiations (rsync warns about a "diminished" file when
       this happens).

       This does not interfere with the updating of a file's non-
       content attributes (e.g.  permissions, ownership, etc.)
       when the file does not need to be transferred, nor does it
       affect the updating of any directories or non-regular
       files.

--append-verify
       This special copy mode works like --append except that all
       the data in the file is included in the checksum
       verification (making it less efficient but also potentially
       safer).  This option can be dangerous if you aren't 100%
       sure that all the files in the transfer are shared, growing
       files.  See the --append option for more details.

       Note: prior to rsync 3.0.0, the --append option worked like
       --append-verify, so if you are interacting with an older
       rsync (or the transfer is using a protocol prior to 30),
       specifying either append option will initiate an
       --append-verify transfer.

--dirs, -d
       Tell the sending side to include any directories that are
       encountered.  Unlike --recursive, a directory's contents
       are not copied unless the directory name specified is "."
       or ends with a trailing slash (e.g.  ".", "dir/.", "dir/",
       etc.).  Without this option or the --recursive option,
       rsync will skip all directories it encounters (and output a
       message to that effect for each one).  If you specify both
       --dirs and --recursive, --recursive takes precedence.

       The --dirs option is implied by the --files-from option or
       the --list-only option (including an implied --list-only
       usage) if --recursive wasn't specified (so that directories
       are seen in the listing).  Specify --no-dirs (or --no-d) if
       you want to turn this off.

       There is also a backward-compatibility helper option,
       --old-dirs (--old-d) that tells rsync to use a hack of
       -r --exclude='/*/*' to get an older rsync to list a single
       directory without recursing.

--mkpath
       Create all missing path components of the destination path.

       By default, rsync allows only the final component of the
       destination path to not exist, which is an attempt to help
       you to validate your destination path.  With this option,
       rsync creates all the missing destination-path components,
       just as if mkdir -p $DEST_PATH had been run on the
       receiving side.

       When specifying a destination path, including a trailing
       slash ensures that the whole path is treated as directory
       names to be created, even when the file list has a single
       item. See the COPYING TO A DIFFERENT NAME section for full
       details on how rsync decides if a final destination-path
       component should be created as a directory or not.

       If you would like the newly-created destination dirs to
       match the dirs on the sending side, you should be using
       --relative (-R) instead of --mkpath.  For instance, the
       following two commands result in the same destination tree,
       but only the second command ensures that the
       "some/extra/path" components match the dirs on the sending
       side:

           rsync -ai --mkpath host:some/extra/path/*.c some/extra/path/
           rsync -aiR host:some/extra/path/*.c ./

--links, -l
       Add symlinks to the transferred files instead of noisily
       ignoring them with a "non-regular file" warning for each
       symlink encountered.  You can alternately silence the
       warning by specifying --info=nonreg0.

       The default handling of symlinks is to recreate each
       symlink's unchanged value on the receiving side.

       See the SYMBOLIC LINKS section for multi-option info.

--copy-links, -L
       The sender transforms each symlink encountered in the
       transfer into the referent item, following the symlink
       chain to the file or directory that it references.  If a
       symlink chain is broken, an error is output and the file is
       dropped from the transfer.

       This option supersedes any other options that affect
       symlinks in the transfer, since there are no symlinks left
       in the transfer.

       This option does not change the handling of existing
       symlinks on the receiving side, unlike versions of rsync
       prior to 2.6.3 which had the side-effect of telling the
       receiving side to also follow symlinks.  A modern rsync
       won't forward this option to a remote receiver (since only
       the sender needs to know about it), so this caveat should
       only affect someone using an rsync client older than 2.6.7
       (which is when -L stopped being forwarded to the receiver).

       See the --keep-dirlinks (-K) if you need a symlink to a
       directory to be treated as a real directory on the
       receiving side.

       See the SYMBOLIC LINKS section for multi-option info.

--copy-unsafe-links
       This tells rsync to copy the referent of symbolic links
       that point outside the copied tree.  Absolute symlinks are
       also treated like ordinary files, and so are any symlinks
       in the source path itself when --relative is used.

       Note that the cut-off point is the top of the transfer,
       which is the part of the path that rsync isn't mentioning
       in the verbose output.  If you copy "/src/subdir" to
       "/dest/" then the "subdir" directory is a name inside the
       transfer tree, not the top of the transfer (which is /src)
       so it is legal for created relative symlinks to refer to
       other names inside the /src and /dest directories.  If you
       instead copy "/src/subdir/" (with a trailing slash) to
       "/dest/subdir" that would not allow symlinks to any files
       outside of "subdir".

       Note that safe symlinks are only copied if --links was also
       specified or implied. The --copy-unsafe-links option has no
       extra effect when combined with --copy-links.

       See the SYMBOLIC LINKS section for multi-option info.

--safe-links
       This tells the receiving rsync to ignore any symbolic links
       in the transfer which point outside the copied tree.  All
       absolute symlinks are also ignored.

       Since this ignoring is happening on the receiving side, it
       will still be effective even when the sending side has
       munged symlinks (when it is using --munge-links). It also
       affects deletions, since the file being present in the
       transfer prevents any matching file on the receiver from
       being deleted when the symlink is deemed to be unsafe and
       is skipped.

       This option must be combined with --links (or --archive) to
       have any symlinks in the transfer to conditionally ignore.
       Its effect is superseded by --copy-unsafe-links.

       Using this option in conjunction with --relative may give
       unexpected results.

       See the SYMBOLIC LINKS section for multi-option info.

--munge-links
       This option affects just one side of the transfer and tells
       rsync to munge symlink values when it is receiving files or
       unmunge symlink values when it is sending files.  The
       munged values make the symlinks unusable on disk but allows
       the original contents of the symlinks to be recovered.

       The server-side rsync often enables this option without the
       client's knowledge, such as in an rsync daemon's
       configuration file or by an option given to the rrsync
       (restricted rsync) script.  When specified on the client
       side, specify the option normally if it is the client side
       that has/needs the munged symlinks, or use -M--munge-links
       to give the option to the server when it has/needs the
       munged symlinks.  Note that on a local transfer, the client
       is the sender, so specifying the option directly unmunges
       symlinks while specifying it as a remote option munges
       symlinks.

       This option has no effect when sent to a daemon via
       --remote-option because the daemon configures whether it
       wants munged symlinks via its "munge symlinks" parameter.

       The symlink value is munged/unmunged once it is in the
       transfer, so any option that transforms symlinks into non-
       symlinks occurs prior to the munging/unmunging except for
       --safe-links, which is a choice that the receiver makes, so
       it bases its decision on the munged/unmunged value.  This
       does mean that if a receiver has munging enabled, that
       using --safe-links will cause all symlinks to be ignored
       (since they are all absolute).

       The method that rsync uses to munge the symlinks is to
       prefix each one's value with the string "/rsyncd-munged/".
       This prevents the links from being used as long as the
       directory does not exist.  When this option is enabled,
       rsync will refuse to run if that path is a directory or a
       symlink to a directory (though it only checks at startup).
       See also the "munge-symlinks" python script in the support
       directory of the source code for a way to munge/unmunge one
       or more symlinks in-place.

--copy-dirlinks, -k
       This option causes the sending side to treat a symlink to a
       directory as though it were a real directory.  This is
       useful if you don't want symlinks to non-directories to be
       affected, as they would be using --copy-links.

       Without this option, if the sending side has replaced a
       directory with a symlink to a directory, the receiving side
       will delete anything that is in the way of the new symlink,
       including a directory hierarchy (as long as --force or
       --delete is in effect).

       See also --keep-dirlinks for an analogous option for the
       receiving side.

       --copy-dirlinks applies to all symlinks to directories in
       the source.  If you want to follow only a few specified
       symlinks, a trick you can use is to pass them as additional
       source args with a trailing slash, using --relative to make
       the paths match up right.  For example:

           rsync -r --relative src/./ src/./follow-me/ dest/

       This works because rsync calls lstat(2) on the source arg
       as given, and the trailing slash makes lstat(2) follow the
       symlink, giving rise to a directory in the file-list which
       overrides the symlink found during the scan of "src/./".

       See the SYMBOLIC LINKS section for multi-option info.

--keep-dirlinks, -K
       This option causes the receiving side to treat a symlink to
       a directory as though it were a real directory, but only if
       it matches a real directory from the sender.  Without this
       option, the receiver's symlink would be deleted and
       replaced with a real directory.

       For example, suppose you transfer a directory "foo" that
       contains a file "file", but "foo" is a symlink to directory
       "bar" on the receiver.  Without --keep-dirlinks, the
       receiver deletes symlink "foo", recreates it as a
       directory, and receives the file into the new directory.
       With --keep-dirlinks, the receiver keeps the symlink and
       "file" ends up in "bar".

       One note of caution: if you use --keep-dirlinks, you must
       trust all the symlinks in the copy or enable the
       --munge-links option on the receiving side!  If it is
       possible for an untrusted user to create their own symlink
       to any real directory, the user could then (on a subsequent
       copy) replace the symlink with a real directory and affect
       the content of whatever directory the symlink references.
       For backup copies, you are better off using something like
       a bind mount instead of a symlink to modify your receiving
       hierarchy.

       See also --copy-dirlinks for an analogous option for the
       sending side.

       See the SYMBOLIC LINKS section for multi-option info.

--hard-links, -H
       This tells rsync to look for hard-linked files in the
       source and link together the corresponding files on the
       destination.  Without this option, hard-linked files in the
       source are treated as though they were separate files.

       This option does NOT necessarily ensure that the pattern of
       hard links on the destination exactly matches that on the
       source.  Cases in which the destination may end up with
       extra hard links include the following:

       o      If the destination contains extraneous hard-links
              (more linking than what is present in the source
              file list), the copying algorithm will not break
              them explicitly.  However, if one or more of the
              paths have content differences, the normal file-
              update process will break those extra links (unless
              you are using the --inplace option).

       o      If you specify a --link-dest directory that contains
              hard links, the linking of the destination files
              against the --link-dest files can cause some paths
              in the destination to become linked together due to
              the --link-dest associations.

       Note that rsync can only detect hard links between files
       that are inside the transfer set.  If rsync updates a file
       that has extra hard-link connections to files outside the
       transfer, that linkage will be broken.  If you are tempted
       to use the --inplace option to avoid this breakage, be very
       careful that you know how your files are being updated so
       that you are certain that no unintended changes happen due
       to lingering hard links (and see the --inplace option for
       more caveats).

       If incremental recursion is active (see --inc-recursive),
       rsync may transfer a missing hard-linked file before it
       finds that another link for that contents exists elsewhere
       in the hierarchy.  This does not affect the accuracy of the
       transfer (i.e. which files are hard-linked together), just
       its efficiency (i.e. copying the data for a new, early copy
       of a hard-linked file that could have been found later in
       the transfer in another member of the hard-linked set of
       files).  One way to avoid this inefficiency is to disable
       incremental recursion using the --no-inc-recursive option.

--perms, -p
       This option causes the receiving rsync to set the
       destination permissions to be the same as the source
       permissions. (See also the --chmod option for a way to
       modify what rsync considers to be the source permissions.)

       When this option is off, permissions are set as follows:

       o      Existing files (including updated files) retain
              their existing permissions, though the
              --executability option might change just the execute
              permission for the file.

       o      New files get their "normal" permission bits set to
              the source file's permissions masked with the
              receiving directory's default permissions (either
              the receiving process's umask, or the permissions
              specified via the destination directory's default
              ACL), and their special permission bits disabled
              except in the case where a new directory inherits a
              setgid bit from its parent directory.

       Thus, when --perms and --executability are both disabled,
       rsync's behavior is the same as that of other file-copy
       utilities, such as cp(1) and tar(1).

       In summary: to give destination files (both old and new)
       the source permissions, use --perms.  To give new files the
       destination-default permissions (while leaving existing
       files unchanged), make sure that the --perms option is off
       and use --chmod=ugo=rwX (which ensures that all non-masked
       bits get enabled).  If you'd care to make this latter
       behavior easier to type, you could define a popt alias for
       it, such as putting this line in the file ~/.popt (the
       following defines the -Z option, and includes --no-g to use
       the default group of the destination dir):

           rsync alias -Z --no-p --no-g --chmod=ugo=rwX

       You could then use this new option in a command such as
       this one:

           rsync -avZ src/ dest/

       (Caveat: make sure that -a does not follow -Z, or it will
       re-enable the two --no-* options mentioned above.)

       The preservation of the destination's setgid bit on newly-
       created directories when --perms is off was added in rsync
       2.6.7.  Older rsync versions erroneously preserved the
       three special permission bits for newly-created files when
       --perms was off, while overriding the destination's setgid
       bit setting on a newly-created directory.  Default ACL
       observance was added to the ACL patch for rsync 2.6.7, so
       older (or non-ACL-enabled) rsyncs use the umask even if
       default ACLs are present.  (Keep in mind that it is the
       version of the receiving rsync that affects these
       behaviors.)

--executability, -E
       This option causes rsync to preserve the executability (or
       non-executability) of regular files when --perms is not
       enabled.  A regular file is considered to be executable if
       at least one 'x' is turned on in its permissions.  When an
       existing destination file's executability differs from that
       of the corresponding source file, rsync modifies the
       destination file's permissions as follows:

       o      To make a file non-executable, rsync turns off all
              its 'x' permissions.

       o      To make a file executable, rsync turns on each 'x'
              permission that has a corresponding 'r' permission
              enabled.

       If --perms is enabled, this option is ignored.

--acls, -A
       This option causes rsync to update the destination ACLs to
       be the same as the source ACLs.  The option also implies
       --perms.

       The source and destination systems must have compatible ACL
       entries for this option to work properly.  See the
       --fake-super option for a way to backup and restore ACLs
       that are not compatible.

--xattrs, -X
       This option causes rsync to update the destination extended
       attributes to be the same as the source ones.

       For systems that support extended-attribute namespaces, a
       copy being done by a super-user copies all namespaces
       except system.*.  A normal user only copies the user.*
       namespace.  To be able to backup and restore non-user
       namespaces as a normal user, see the --fake-super option.

       The above name filtering can be overridden by using one or
       more filter options with the x modifier.  When you specify
       an xattr-affecting filter rule, rsync requires that you do
       your own system/user filtering, as well as any additional
       filtering for what xattr names are copied and what names
       are allowed to be deleted.  For example, to skip the system
       namespace, you could specify:

           --filter='-x system.*'

       To skip all namespaces except the user namespace, you could
       specify a negated-user match:

           --filter='-x! user.*'

       To prevent any attributes from being deleted, you could
       specify a receiver-only rule that excludes all names:

           --filter='-xr *'

       Note that the -X option does not copy rsync's special xattr
       values (e.g.  those used by --fake-super) unless you repeat
       the option (e.g. -XX).  This "copy all xattrs" mode cannot
       be used with --fake-super.

--chmod=CHMOD
       This option tells rsync to apply one or more comma-
       separated "chmod" modes to the permission of the files in
       the transfer.  The resulting value is treated as though it
       were the permissions that the sending side supplied for the
       file, which means that this option can seem to have no
       effect on existing files if --perms is not enabled.

       In addition to the normal parsing rules specified in the
       chmod(1) manpage, you can specify an item that should only
       apply to a directory by prefixing it with a 'D', or specify
       an item that should only apply to a file by prefixing it
       with a 'F'.  For example, the following will ensure that
       all directories get marked set-gid, that no files are
       other-writable, that both are user-writable and group-
       writable, and that both have consistent executability
       across all bits:

           --chmod=Dg+s,ug+w,Fo-w,+X

       Using octal mode numbers is also allowed:

           --chmod=D2775,F664

       It is also legal to specify multiple --chmod options, as
       each additional option is just appended to the list of
       changes to make.

       See the --perms and --executability options for how the
       resulting permission value can be applied to the files in
       the transfer.

--owner, -o
       This option causes rsync to set the owner of the
       destination file to be the same as the source file, but
       only if the receiving rsync is being run as the super-user
       (see also the --super and --fake-super options).  Without
       this option, the owner of new and/or transferred files are
       set to the invoking user on the receiving side.

       The preservation of ownership will associate matching names
       by default, but may fall back to using the ID number in
       some circumstances (see also the --numeric-ids option for a
       full discussion).

--group, -g
       This option causes rsync to set the group of the
       destination file to be the same as the source file.  If the
       receiving program is not running as the super-user (or if
       --no-super was specified), only groups that the invoking
       user on the receiving side is a member of will be
       preserved.  Without this option, the group is set to the
       default group of the invoking user on the receiving side.

       The preservation of group information will associate
       matching names by default, but may fall back to using the
       ID number in some circumstances (see also the --numeric-ids
       option for a full discussion).

--devices
       This option causes rsync to transfer character and block
       device files to the remote system to recreate these
       devices.  If the receiving rsync is not being run as the
       super-user, rsync silently skips creating the device files
       (see also the --super and --fake-super options).

       By default, rsync generates a "non-regular file" warning
       for each device file encountered when this option is not
       set.  You can silence the warning by specifying
       --info=nonreg0.

--specials
       This option causes rsync to transfer special files, such as
       named sockets and fifos.  If the receiving rsync is not
       being run as the super-user, rsync silently skips creating
       the special files (see also the --super and --fake-super
       options).

       By default, rsync generates a "non-regular file" warning
       for each special file encountered when this option is not
       set.  You can silence the warning by specifying
       --info=nonreg0.

-D     The -D option is equivalent to "--devices --specials".

--copy-devices
       This tells rsync to treat a device on the sending side as a
       regular file, allowing it to be copied to a normal
       destination file (or another device if --write-devices was
       also specified).

       This option is refused by default by an rsync daemon.

--write-devices
       This tells rsync to treat a device on the receiving side as
       a regular file, allowing the writing of file data into a
       device.

       This option implies the --inplace option.

       Be careful using this, as you should know what devices are
       present on the receiving side of the transfer, especially
       when running rsync as root.

       This option is refused by default by an rsync daemon.

--times, -t
       This tells rsync to transfer modification times along with
       the files and update them on the remote system.  Note that
       if this option is not used, the optimization that excludes
       files that have not been modified cannot be effective; in
       other words, a missing -t (or -a) will cause the next
       transfer to behave as if it used --ignore-times (-I),
       causing all files to be updated (though rsync's delta-
       transfer algorithm will make the update fairly efficient if
       the files haven't actually changed, you're much better off
       using -t).

       A modern rsync that is using transfer protocol 30 or 31
       conveys a modify time using up to 8-bytes. If rsync is
       forced to speak an older protocol (perhaps due to the
       remote rsync being older than 3.0.0) a modify time is
       conveyed using 4-bytes. Prior to 3.2.7, these shorter
       values could convey a date range of 13-Dec-1901 to
       19-Jan-2038.  Beginning with 3.2.7, these 4-byte values now
       convey a date range of 1-Jan-1970 to 7-Feb-2106.  If you
       have files dated older than 1970, make sure your rsync
       executables are upgraded so that the full range of dates
       can be conveyed.

--atimes, -U
       This tells rsync to set the access (use) times of the
       destination files to the same value as the source files.

       If repeated, it also sets the --open-noatime option, which
       can help you to make the sending and receiving systems have
       the same access times on the transferred files without
       needing to run rsync an extra time after a file is
       transferred.

       Note that some older rsync versions (prior to 3.2.0) may
       have been built with a pre-release --atimes patch that does
       not imply --open-noatime when this option is repeated.

--open-noatime
       This tells rsync to open files with the O_NOATIME flag (on
       systems that support it) to avoid changing the access time
       of the files that are being transferred.  If your OS does
       not support the O_NOATIME flag then rsync will silently
       ignore this option.  Note also that some filesystems are
       mounted to avoid updating the atime on read access even
       without the O_NOATIME flag being set.

--crtimes, -N,
       This tells rsync to set the create times (newness) of the
       destination files to the same value as the source files.
       Your OS & filesystem must support the setting of arbitrary
       creation (birth) times for this option to be supported.

--omit-dir-times, -O
       This tells rsync to omit directories when it is preserving
       modification, access, and create times.  If NFS is sharing
       the directories on the receiving side, it is a good idea to
       use -O.  This option is inferred if you use --backup
       without --backup-dir.

       This option also has the side-effect of avoiding early
       creation of missing sub-directories when incremental
       recursion is enabled, as discussed in the --inc-recursive
       section.

--omit-link-times, -J
       This tells rsync to omit symlinks when it is preserving
       modification, access, and create times.

--super
       This tells the receiving side to attempt super-user
       activities even if the receiving rsync wasn't run by the
       super-user.  These activities include: preserving users via
       the --owner option, preserving all groups (not just the
       current user's groups) via the --group option, and copying
       devices via the --devices option.  This is useful for
       systems that allow such activities without being the super-
       user, and also for ensuring that you will get errors if the
       receiving side isn't being run as the super-user.  To turn
       off super-user activities, the super-user can use
       --no-super.

--fake-super
       When this option is enabled, rsync simulates super-user
       activities by saving/restoring the privileged attributes
       via special extended attributes that are attached to each
       file (as needed).  This includes the file's owner and group
       (if it is not the default), the file's device info (device
       & special files are created as empty text files), and any
       permission bits that we won't allow to be set on the real
       file (e.g. the real file gets u-s,g-s,o-t for safety) or
       that would limit the owner's access (since the real super-
       user can always access/change a file, the files we create
       can always be accessed/changed by the creating user).  This
       option also handles ACLs (if --acls was specified) and non-
       user extended attributes (if --xattrs was specified).

       This is a good way to backup data without using a super-
       user, and to store ACLs from incompatible systems.

       The --fake-super option only affects the side where the
       option is used.  To affect the remote side of a remote-
       shell connection, use the --remote-option (-M) option:

           rsync -av -M--fake-super /src/ host:/dest/

       For a local copy, this option affects both the source and
       the destination.  If you wish a local copy to enable this
       option just for the destination files, specify
       -M--fake-super.  If you wish a local copy to enable this
       option just for the source files, combine --fake-super with
       -M--super.

       This option is overridden by both --super and --no-super.

       See also the fake super setting in the daemon's rsyncd.conf
       file.

--sparse, -S
       Try to handle sparse files efficiently so they take up less
       space on the destination.  If combined with --inplace the
       file created might not end up with sparse blocks with some
       combinations of kernel version and/or filesystem type.  If
       --whole-file is in effect (e.g. for a local copy) then it
       will always work because rsync truncates the file prior to
       writing out the updated version.

       Note that versions of rsync older than 3.1.3 will reject
       the combination of --sparse and --inplace.

--preallocate
       This tells the receiver to allocate each destination file
       to its eventual size before writing data to the file.
       Rsync will only use the real filesystem-level preallocation
       support provided by Linux's fallocate(2) system call or
       Cygwin's posix_fallocate(3), not the slow glibc
       implementation that writes a null byte into each block.

       Without this option, larger files may not be entirely
       contiguous on the filesystem, but with this option rsync
       will probably copy more slowly.  If the destination is not
       an extent-supporting filesystem (such as ext4, xfs, NTFS,
       etc.), this option may have no positive effect at all.

       If combined with --sparse, the file will only have sparse
       blocks (as opposed to allocated sequences of null bytes) if
       the kernel version and filesystem type support creating
       holes in the allocated data.

--dry-run, -n
       This makes rsync perform a trial run that doesn't make any
       changes (and produces mostly the same output as a real
       run).  It is most commonly used in combination with the
       --verbose (-v) and/or --itemize-changes (-i) options to see
       what an rsync command is going to do before one actually
       runs it.

       The output of --itemize-changes is supposed to be exactly
       the same on a dry run and a subsequent real run (barring
       intentional trickery and system call failures); if it
       isn't, that's a bug.  Other output should be mostly
       unchanged, but may differ in some areas.  Notably, a dry
       run does not send the actual data for file transfers, so
       --progress has no effect, the "bytes sent", "bytes
       received", "literal data", and "matched data" statistics
       are too small, and the "speedup" value is equivalent to a
       run where no file transfers were needed.

--whole-file, -W
       This option disables rsync's delta-transfer algorithm,
       which causes all transferred files to be sent whole.  The
       transfer may be faster if this option is used when the
       bandwidth between the source and destination machines is
       higher than the bandwidth to disk (especially when the
       "disk" is actually a networked filesystem).  This is the
       default when both the source and destination are specified
       as local paths, but only if no batch-writing option is in
       effect.

--no-whole-file, --no-W
       Disable whole-file updating when it is enabled by default
       for a local transfer.  This usually slows rsync down, but
       it can be useful if you are trying to minimize the writes
       to the destination file (if combined with --inplace) or for
       testing the checksum-based update algorithm.

       See also the --whole-file option.

--checksum-choice=STR, --cc=STR
       This option overrides the checksum algorithms.  If one
       algorithm name is specified, it is used for both the
       transfer checksums and (assuming --checksum is specified)
       the pre-transfer checksums.  If two comma-separated names
       are supplied, the first name affects the transfer
       checksums, and the second name affects the pre-transfer
       checksums (-c).

       The checksum options that you may be able to use are:

       o      auto (the default automatic choice)

       o      xxh128

       o      xxh3

       o      xxh64 (aka xxhash)

       o      md5

       o      md4

       o      sha1

       o      none

       Run rsync --version to see the default checksum list
       compiled into your version (which may differ from the list
       above).

       If "none" is specified for the first (or only) name, the
       --whole-file option is forced on and no checksum
       verification is performed on the transferred data.  If
       "none" is specified for the second (or only) name, the
       --checksum option cannot be used.

       The "auto" option is the default, where rsync bases its
       algorithm choice on a negotiation between the client and
       the server as follows:

       When both sides of the transfer are at least 3.2.0, rsync
       chooses the first algorithm in the client's list of choices
       that is also in the server's list of choices.  If no common
       checksum choice is found, rsync exits with an error.  If
       the remote rsync is too old to support checksum
       negotiation, a value is chosen based on the protocol
       version (which chooses between MD5 and various flavors of
       MD4 based on protocol age).

       The default order can be customized by setting the
       environment variable RSYNC_CHECKSUM_LIST to a space-
       separated list of acceptable checksum names.  If the string
       contains a "&" character, it is separated into the "client
       string & server string", otherwise the same string applies
       to both.  If the string (or string portion) contains no
       non-whitespace characters, the default checksum list is
       used.  This method does not allow you to specify the
       transfer checksum separately from the pre-transfer
       checksum, and it discards "auto" and all unknown checksum
       names.  A list with only invalid names results in a failed
       negotiation.

       The use of the --checksum-choice option overrides this
       environment list.

--one-file-system, -x
       This tells rsync to avoid crossing a filesystem boundary
       when recursing.  This does not limit the user's ability to
       specify items to copy from multiple filesystems, just
       rsync's recursion through the hierarchy of each directory
       that the user specified, and also the analogous recursion
       on the receiving side during deletion.  Also keep in mind
       that rsync treats a "bind" mount to the same device as
       being on the same filesystem.

       If this option is repeated, rsync omits all mount-point
       directories from the copy.  Otherwise, it includes an empty
       directory at each mount-point it encounters (using the
       attributes of the mounted directory because those of the
       underlying mount-point directory are inaccessible).

       If rsync has been told to collapse symlinks (via
       --copy-links or --copy-unsafe-links), a symlink to a
       directory on another device is treated like a mount-point.
       Symlinks to non-directories are unaffected by this option.

--ignore-non-existing, --existing
       This tells rsync to skip creating files (including
       directories) that do not exist yet on the destination.  If
       this option is combined with the --ignore-existing option,
       no files will be updated (which can be useful if all you
       want to do is delete extraneous files).

       This option is a TRANSFER RULE, so don't expect any exclude
       side effects.

--ignore-existing
       This tells rsync to skip updating files that already exist
       on the destination (this does not ignore existing
       directories, or nothing would get done).  See also
       --ignore-non-existing.

       This option is a TRANSFER RULE, so don't expect any exclude
       side effects.

       This option can be useful for those doing backups using the
       --link-dest option when they need to continue a backup run
       that got interrupted.  Since a --link-dest run is copied
       into a new directory hierarchy (when it is used properly),
       using [--ignore-existing will ensure that the already-
       handled files don't get tweaked (which avoids a change in
       permissions on the hard-linked files).  This does mean that
       this option is only looking at the existing files in the
       destination hierarchy itself.

       When --info=skip2 is used rsync will output "FILENAME
       exists (INFO)" messages where the INFO indicates one of
       "type change", "sum change" (requires -c), "file change"
       (based on the quick check), "attr change", or "uptodate".
       Using --info=skip1 (which is also implied by 2 -v options)
       outputs the exists message without the INFO suffix.

--remove-source-files
       This tells rsync to remove from the sending side the files
       (meaning non-directories) that are a part of the transfer
       and have been successfully duplicated on the receiving
       side.

       Note that you should only use this option on source files
       that are quiescent.  If you are using this to move files
       that show up in a particular directory over to another
       host, make sure that the finished files get renamed into
       the source directory, not directly written into it, so that
       rsync can't possibly transfer a file that is not yet fully
       written.  If you can't first write the files into a
       different directory, you should use a naming idiom that
       lets rsync avoid transferring files that are not yet
       finished (e.g. name the file "foo.new" when it is written,
       rename it to "foo" when it is done, and then use the option
       --exclude='*.new' for the rsync transfer).

       Starting with 3.1.0, rsync will skip the sender-side
       removal (and output an error) if the file's size or modify
       time has not stayed unchanged.

       Starting with 3.2.6, a local rsync copy will ensure that
       the sender does not remove a file the receiver just
       verified, such as when the user accidentally makes the
       source and destination directory the same path.

--delete
       This tells rsync to delete extraneous files from the
       receiving side (ones that aren't on the sending side), but
       only for the directories that are being synchronized.  You
       must have asked rsync to send the whole directory (e.g.
       "dir" or "dir/") without using a wildcard for the
       directory's contents (e.g. "dir/*") since the wildcard is
       expanded by the shell and rsync thus gets a request to
       transfer individual files, not the files' parent directory.
       Files that are excluded from the transfer are also excluded
       from being deleted unless you use the --delete-excluded
       option or mark the rules as only matching on the sending
       side (see the include/exclude modifiers in the FILTER RULES
       section).

       Prior to rsync 2.6.7, this option would have no effect
       unless --recursive was enabled.  Beginning with 2.6.7,
       deletions will also occur when --dirs (-d) is enabled, but
       only for directories whose contents are being copied.

       This option can be dangerous if used incorrectly! It is a
       very good idea to first try a run using the --dry-run (-n)
       option to see what files are going to be deleted.

       If the sending side detects any I/O errors, then the
       deletion of any files at the destination will be
       automatically disabled.  This is to prevent temporary
       filesystem failures (such as NFS errors) on the sending
       side from causing a massive deletion of files on the
       destination.  You can override this with the
       --ignore-errors option.

       The --delete option may be combined with one of the
       --delete-WHEN options without conflict, as well as
       --delete-excluded.  However, if none of the --delete-WHEN
       options are specified, rsync will choose the
       --delete-during algorithm when talking to rsync 3.0.0 or
       newer, or the --delete-before algorithm when talking to an
       older rsync.  See also --delete-delay and --delete-after.

--delete-before
       Request that the file-deletions on the receiving side be
       done before the transfer starts.  See --delete (which is
       implied) for more details on file-deletion.

       Deleting before the transfer is helpful if the filesystem
       is tight for space and removing extraneous files would help
       to make the transfer possible.  However, it does introduce
       a delay before the start of the transfer, and this delay
       might cause the transfer to timeout (if --timeout was
       specified).  It also forces rsync to use the old, non-
       incremental recursion algorithm that requires rsync to scan
       all the files in the transfer into memory at once (see
       --recursive).

--delete-during, --del
       Request that the file-deletions on the receiving side be
       done incrementally as the transfer happens.  The per-
       directory delete scan is done right before each directory
       is checked for updates, so it behaves like a more efficient
       --delete-before, including doing the deletions prior to any
       per-directory filter files being updated.  This option was
       first added in rsync version 2.6.4.  See --delete (which is
       implied) for more details on file-deletion.

--delete-delay
       Request that the file-deletions on the receiving side be
       computed during the transfer (like --delete-during), and
       then removed after the transfer completes.  This is useful
       when combined with --delay-updates and/or --fuzzy, and is
       more efficient than using --delete-after (but can behave
       differently, since --delete-after computes the deletions in
       a separate pass after all updates are done).  If the number
       of removed files overflows an internal buffer, a temporary
       file will be created on the receiving side to hold the
       names (it is removed while open, so you shouldn't see it
       during the transfer).  If the creation of the temporary
       file fails, rsync will try to fall back to using
       --delete-after (which it cannot do if --recursive is doing
       an incremental scan).  See --delete (which is implied) for
       more details on file-deletion.

--delete-after
       Request that the file-deletions on the receiving side be
       done after the transfer has completed.  This is useful if
       you are sending new per-directory merge files as a part of
       the transfer and you want their exclusions to take effect
       for the delete phase of the current transfer.  It also
       forces rsync to use the old, non-incremental recursion
       algorithm that requires rsync to scan all the files in the
       transfer into memory at once (see --recursive). See
       --delete (which is implied) for more details on file-
       deletion.

       See also the --delete-delay option that might be a faster
       choice for those that just want the deletions to occur at
       the end of the transfer.

--delete-excluded
       This option turns any unqualified exclude/include rules
       into server-side rules that do not affect the receiver's
       deletions.

       By default, an exclude or include has both a server-side
       effect (to "hide" and "show" files when building the
       server's file list) and a receiver-side effect (to
       "protect" and "risk" files when deletions are occurring).
       Any rule that has no modifier to specify what sides it is
       executed on will be instead treated as if it were a server-
       side rule only, avoiding any "protect" effects of the
       rules.

       A rule can still apply to both sides even with this option
       specified if the rule is given both the sender & receiver
       modifier letters (e.g., -f'-sr foo').  Receiver-side
       protect/risk rules can also be explicitly specified to
       limit the deletions.  This saves you from having to edit a
       bunch of -f'- foo' rules into -f'-s foo' (aka -f'H foo')
       rules (not to mention the corresponding includes).

       See the FILTER RULES section for more information.  See
       --delete (which is implied) for more details on deletion.

--ignore-missing-args
       When rsync is first processing the explicitly requested
       source files (e.g.  command-line arguments or --files-from
       entries), it is normally an error if the file cannot be
       found.  This option suppresses that error, and does not try
       to transfer the file.  This does not affect subsequent
       vanished-file errors if a file was initially found to be
       present and later is no longer there.

--delete-missing-args
       This option takes the behavior of the (implied)
       --ignore-missing-args option a step farther: each missing
       arg will become a deletion request of the corresponding
       destination file on the receiving side (should it exist).
       If the destination file is a non-empty directory, it will
       only be successfully deleted if --force or --delete are in
       effect.  Other than that, this option is independent of any
       other type of delete processing.

       The missing source files are represented by special file-
       list entries which display as a "*missing" entry in the
       --list-only output.

--ignore-errors
       Tells --delete to go ahead and delete files even when there
       are I/O errors.

--force
       This option tells rsync to delete a non-empty directory
       when it is to be replaced by a non-directory.  This is only
       relevant if deletions are not active (see --delete for
       details).

       Note for older rsync versions: --force used to still be
       required when using --delete-after, and it used to be non-
       functional unless the --recursive option was also enabled.

--max-delete=NUM
       This tells rsync not to delete more than NUM files or
       directories.  If that limit is exceeded, all further
       deletions are skipped through the end of the transfer.  At
       the end, rsync outputs a warning (including a count of the
       skipped deletions) and exits with an error code of 25
       (unless some more important error condition also occurred).

       Beginning with version 3.0.0, you may specify
       --max-delete=0 to be warned about any extraneous files in
       the destination without removing any of them.  Older
       clients interpreted this as "unlimited", so if you don't
       know what version the client is, you can use the less
       obvious --max-delete=-1 as a backward-compatible way to
       specify that no deletions be allowed (though really old
       versions didn't warn when the limit was exceeded).

--max-size=SIZE
       This tells rsync to avoid transferring any file that is
       larger than the specified SIZE.  A numeric value can be
       suffixed with a string to indicate the numeric units or
       left unqualified to specify bytes.  Feel free to use a
       fractional value along with the units, such as
       --max-size=1.5m.

       This option is a TRANSFER RULE, so don't expect any exclude
       side effects.

       The first letter of a units string can be B (bytes), K
       (kilo), M (mega), G (giga), T (tera), or P (peta).  If the
       string is a single char or has "ib" added to it (e.g. "G"
       or "GiB") then the units are multiples of 1024.  If you use
       a two-letter suffix that ends with a "B" (e.g. "kb") then
       you get units that are multiples of 1000.  The string's
       letters can be any mix of upper and lower-case that you
       want to use.

       Finally, if the string ends with either "+1" or "-1", it is
       offset by one byte in the indicated direction.  The largest
       possible value is usually 8192P-1.

       Examples: --max-size=1.5mb-1 is 1499999 bytes, and
       --max-size=2g+1 is 2147483649 bytes.

       Note that rsync versions prior to 3.1.0 did not allow
       --max-size=0.

--min-size=SIZE
       This tells rsync to avoid transferring any file that is
       smaller than the specified SIZE, which can help in not
       transferring small, junk files.  See the --max-size option
       for a description of SIZE and other info.

       Note that rsync versions prior to 3.1.0 did not allow
       --min-size=0.

--max-alloc=SIZE
       By default rsync limits an individual malloc/realloc to
       about 1GB in size.  For most people this limit works just
       fine and prevents a protocol error causing rsync to request
       massive amounts of memory.  However, if you have many
       millions of files in a transfer, a large amount of server
       memory, and you don't want to split up your transfer into
       multiple parts, you can increase the per-allocation limit
       to something larger and rsync will consume more memory.

       Keep in mind that this is not a limit on the total size of
       allocated memory.  It is a sanity-check value for each
       individual allocation.

       See the --max-size option for a description of how SIZE can
       be specified.  The default suffix if none is given is
       bytes.

       Beginning in 3.2.7, a value of 0 is an easy way to specify
       SIZE_MAX (the largest limit possible).

       You can set a default value using the environment variable
       RSYNC_MAX_ALLOC using the same SIZE values as supported by
       this option.  If the remote rsync doesn't understand the
       --max-alloc option, you can override an environmental value
       by specifying --max-alloc=1g, which will make rsync avoid
       sending the option to the remote side (because "1G" is the
       default).

--block-size=SIZE, -B
       This forces the block size used in rsync's delta-transfer
       algorithm to a fixed value.  It is normally selected based
       on the size of each file being updated.  See the technical
       report for details.

       Beginning in 3.2.3 the SIZE can be specified with a suffix
       as detailed in the --max-size option.  Older versions only
       accepted a byte count.

--rsh=COMMAND, -e
       This option allows you to choose an alternative remote
       shell program to use for communication between the local
       and remote copies of rsync.  Typically, rsync is configured
       to use ssh by default, but you may prefer to use rsh on a
       local network.

       If this option is used with [user@]host::module/path, then
       the remote shell COMMAND will be used to run an rsync
       daemon on the remote host, and all data will be transmitted
       through that remote shell connection, rather than through a
       direct socket connection to a running rsync daemon on the
       remote host.  See the USING RSYNC-DAEMON FEATURES VIA A
       REMOTE-SHELL CONNECTION section above.

       Beginning with rsync 3.2.0, the RSYNC_PORT environment
       variable will be set when a daemon connection is being made
       via a remote-shell connection.  It is set to 0 if the
       default daemon port is being assumed, or it is set to the
       value of the rsync port that was specified via either the
       --port option or a non-empty port value in an rsync:// URL.
       This allows the script to discern if a non-default port is
       being requested, allowing for things such as an SSL or
       stunnel helper script to connect to a default or alternate
       port.

       Command-line arguments are permitted in COMMAND provided
       that COMMAND is presented to rsync as a single argument.
       You must use spaces (not tabs or other whitespace) to
       separate the command and args from each other, and you can
       use single- and/or double-quotes to preserve spaces in an
       argument (but not backslashes).  Note that doubling a
       single-quote inside a single-quoted string gives you a
       single-quote; likewise for double-quotes (though you need
       to pay attention to which quotes your shell is parsing and
       which quotes rsync is parsing).  Some examples:

           -e 'ssh -p 2234'
           -e 'ssh -o "ProxyCommand nohup ssh firewall nc -w1 %h %p"'

       (Note that ssh users can alternately customize site-
       specific connect options in their .ssh/config file.)

       You can also choose the remote shell program using the
       RSYNC_RSH environment variable, which accepts the same
       range of values as -e.

       See also the --blocking-io option which is affected by this
       option.

--rsync-path=PROGRAM
       Use this to specify what program is to be run on the remote
       machine to start-up rsync.  Often used when rsync is not in
       the default remote-shell's path (e.g.
       --rsync-path=/usr/local/bin/rsync).  Note that PROGRAM is
       run with the help of a shell, so it can be any program,
       script, or command sequence you'd care to run, so long as
       it does not corrupt the standard-in & standard-out that
       rsync is using to communicate.

       One tricky example is to set a different default directory
       on the remote machine for use with the --relative option.
       For instance:

           rsync -avR --rsync-path="cd /a/b && rsync" host:c/d /e/

--remote-option=OPTION, -M
       This option is used for more advanced situations where you
       want certain effects to be limited to one side of the
       transfer only.  For instance, if you want to pass
       --log-file=FILE and --fake-super to the remote system,
       specify it like this:

           rsync -av -M --log-file=foo -M--fake-super src/ dest/

       If you want to have an option affect only the local side of
       a transfer when it normally affects both sides, send its
       negation to the remote side.  Like this:

           rsync -av -x -M--no-x src/ dest/

       Be cautious using this, as it is possible to toggle an
       option that will cause rsync to have a different idea about
       what data to expect next over the socket, and that will
       make it fail in a cryptic fashion.

       Note that you should use a separate -M option for each
       remote option you want to pass.  On older rsync versions,
       the presence of any spaces in the remote-option arg could
       cause it to be split into separate remote args, but this
       requires the use of --old-args in a modern rsync.

       When performing a local transfer, the "local" side is the
       sender and the "remote" side is the receiver.

       Note some versions of the popt option-parsing library have
       a bug in them that prevents you from using an adjacent arg
       with an equal in it next to a short option letter (e.g.
       -M--log-file=/tmp/foo).  If this bug affects your version
       of popt, you can use the version of popt that is included
       with rsync.

--cvs-exclude, -C
       This is a useful shorthand for excluding a broad range of
       files that you often don't want to transfer between
       systems.  It uses a similar algorithm to CVS to determine
       if a file should be ignored.
