---
title: "rsync(1) (part 4/5)"
source: https://man7.org/linux/man-pages/man1/rsync.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 4/5
---

# rsync(1)

--sockopts=OPTIONS
       This option can provide endless fun for people who like to
       tune their systems to the utmost degree.  You can set all
       sorts of socket options which may make transfers faster (or
       slower!).  Read the manpage for the setsockopt() system
       call for details on some of the options you may be able to
       set.  By default no special socket options are set.  This
       only affects direct socket connections to a remote rsync
       daemon.

       See also the daemon version of the --sockopts option.

--blocking-io
       This tells rsync to use blocking I/O when launching a
       remote shell transport.  If the remote shell is either rsh
       or remsh, rsync defaults to using blocking I/O, otherwise
       it defaults to using non-blocking I/O. (Note that ssh
       prefers non-blocking I/O.)

--outbuf=MODE
       This sets the output buffering mode.  The mode can be None
       (aka Unbuffered), Line, or Block (aka Full).  You may
       specify as little as a single letter for the mode, and use
       upper or lower case.

       The main use of this option is to change Full buffering to
       Line buffering when rsync's output is going to a file or
       pipe.

--itemize-changes, -i
       Requests a simple itemized list of the changes that are
       being made to each file, including attribute changes.  This
       is exactly the same as specifying --out-format='%i %n%L'.
       If you repeat the option, unchanged files will also be
       output, but only if the receiving rsync is at least version
       2.6.7 (you can use -vv with older versions of rsync, but
       that also turns on the output of other verbose messages).

       The "%i" escape has a cryptic output that is 11 letters
       long.  The general format is like the string YXcstpoguax,
       where Y is replaced by the type of update being done, X is
       replaced by the file-type, and the other letters represent
       attributes that may be output if they are being modified.

       The update types that replace the Y are as follows:

       o      A < means that a file is being transferred to the
              remote host (sent).

       o      A > means that a file is being transferred to the
              local host (received).

       o      A c means that a local change/creation is occurring
              for the item (such as the creation of a directory or
              the changing of a symlink, etc.).

       o      A h means that the item is a hard link to another
              item (requires --hard-links).

       o      A . means that the item is not being updated (though
              it might have attributes that are being modified).

       o      A * means that the rest of the itemized-output area
              contains a message (e.g. "deleting").

       The file-types that replace the X are: f for a file, a d
       for a directory, an L for a symlink, a D for a device, and
       a S for a special file (e.g. named sockets and fifos).

       The other letters in the string indicate if some attributes
       of the file have changed, as follows:

       o      "." - the attribute is unchanged.

       o      "+" - the file is newly created.

       o      " " - all the attributes are unchanged (all dots
              turn to spaces).

       o      "?" - the change is unknown (when the remote rsync
              is old).

       o      A letter indicates an attribute is being updated.

       The attribute that is associated with each letter is as
       follows:

       o      A c means either that a regular file has a different
              checksum (requires --checksum) or that a symlink,
              device, or special file has a changed value.  Note
              that if you are sending files to an rsync prior to
              3.0.1, this change flag will be present only for
              checksum-differing regular files.

       o      A s means the size of a regular file is different
              and will be updated by the file transfer.

       o      A t means the modification time is different and is
              being updated to the sender's value (requires
              --times).  An alternate value of T means that the
              modification time will be set to the transfer time,
              which happens when a file/symlink/device is updated
              without --times and when a symlink is changed and
              the receiver can't set its time. (Note: when using
              an rsync 3.0.0 client, you might see the s flag
              combined with t instead of the proper T flag for
              this time-setting failure.)

       o      A p means the permissions are different and are
              being updated to the sender's value (requires
              --perms).

       o      An o means the owner is different and is being
              updated to the sender's value (requires --owner and
              super-user privileges).

       o      A g means the group is different and is being
              updated to the sender's value (requires --group and
              the authority to set the group).

       o

              o      A u|n|b indicates the following information:

                     u  means the access (use) time is different
                     and is being updated to the sender's value
                     (requires --atimes)

              o      n means the create time (newness) is
                     different and is being updated to the
                     sender's value (requires --crtimes)

              o      b means that both the access and create times
                     are being updated

       o      The a means that the ACL information is being
              changed.

       o      The x means that the extended attribute information
              is being changed.

       One other output is possible: when deleting files, the "%i"
       will output the string "*deleting" for each item that is
       being removed (assuming that you are talking to a recent
       enough rsync that it logs deletions instead of outputting
       them as a verbose message).

--out-format=FORMAT
       This allows you to specify exactly what the rsync client
       outputs to the user on a per-update basis.  The format is a
       text string containing embedded single-character escape
       sequences prefixed with a percent (%) character.  A default
       format of "%n%L" is assumed if either --info=name or -v is
       specified (this tells you just the name of the file and, if
       the item is a link, where it points).  For a full list of
       the possible escape characters, see the log format setting
       in the rsyncd.conf manpage.

       Specifying the --out-format option implies the --info=name
       option, which will mention each file, dir, etc. that gets
       updated in a significant way (a transferred file, a
       recreated symlink/device, or a touched directory).  In
       addition, if the itemize-changes escape (%i) is included in
       the string (e.g. if the --itemize-changes option was used),
       the logging of names increases to mention any item that is
       changed in any way (as long as the receiving side is at
       least 2.6.4).  See the --itemize-changes option for a
       description of the output of "%i".

       Rsync will output the out-format string prior to a file's
       transfer unless one of the transfer-statistic escapes is
       requested, in which case the logging is done at the end of
       the file's transfer.  When this late logging is in effect
       and --progress is also specified, rsync will also output
       the name of the file being transferred prior to its
       progress information (followed, of course, by the out-
       format output).

--log-file=FILE
       This option causes rsync to log what it is doing to a file.
       This is similar to the logging that a daemon does, but can
       be requested for the client side and/or the server side of
       a non-daemon transfer.  If specified as a client option,
       transfer logging will be enabled with a default format of
       "%i %n%L".  See the --log-file-format option if you wish to
       override this.

       Here's an example command that requests the remote side to
       log what is happening:

           rsync -av --remote-option=--log-file=/tmp/rlog src/ dest/

       This is very useful if you need to debug why a connection
       is closing unexpectedly.

       See also the daemon version of the --log-file option.

--log-file-format=FORMAT
       This allows you to specify exactly what per-update logging
       is put into the file specified by the --log-file option
       (which must also be specified for this option to have any
       effect).  If you specify an empty string, updated files
       will not be mentioned in the log file.  For a list of the
       possible escape characters, see the log format setting in
       the rsyncd.conf manpage.

       The default FORMAT used if --log-file is specified and this
       option is not is '%i %n%L'.

       See also the daemon version of the --log-file-format
       option.

--stats
       This tells rsync to print a verbose set of statistics on
       the file transfer, allowing you to tell how effective
       rsync's delta-transfer algorithm is for your data.  This
       option is equivalent to --info=stats2 if combined with 0 or
       1 -v options, or --info=stats3 if combined with 2 or more
       -v options.

       The current statistics are as follows:

       o      Number of files is the count of all "files" (in the
              generic sense), which includes directories,
              symlinks, etc.  The total count will be followed by
              a list of counts by filetype (if the total is non-
              zero).  For example: "(reg: 5, dir: 3, link: 2, dev:
              1, special: 1)" lists the totals for regular files,
              directories, symlinks, devices, and special files.
              If any of value is 0, it is completely omitted from
              the list.

       o      Number of created files is the count of how many
              "files" (generic sense) were created (as opposed to
              updated).  The total count will be followed by a
              list of counts by filetype (if the total is non-
              zero).

       o      Number of deleted files is the count of how many
              "files" (generic sense) were deleted.  The total
              count will be followed by a list of counts by
              filetype (if the total is non-zero).  Note that this
              line is only output if deletions are in effect, and
              only if protocol 31 is being used (the default for
              rsync 3.1.x).

       o      Number of regular files transferred is the count of
              normal files that were updated via rsync's delta-
              transfer algorithm, which does not include dirs,
              symlinks, etc.  Note that rsync 3.1.0 added the word
              "regular" into this heading.

       o      Total file size is the total sum of all file sizes
              in the transfer.  This does not count any size for
              directories or special files, but does include the
              size of symlinks.

       o      Total transferred file size is the total sum of all
              files sizes for just the transferred files.

       o      Literal data is how much unmatched file-update data
              we had to send to the receiver for it to recreate
              the updated files.

       o      Matched data is how much data the receiver got
              locally when recreating the updated files.

       o      File list size is how big the file-list data was
              when the sender sent it to the receiver.  This is
              smaller than the in-memory size for the file list
              due to some compressing of duplicated data when
              rsync sends the list.

       o      File list generation time is the number of seconds
              that the sender spent creating the file list.  This
              requires a modern rsync on the sending side for this
              to be present.

       o      File list transfer time is the number of seconds
              that the sender spent sending the file list to the
              receiver.

       o      Total bytes sent is the count of all the bytes that
              rsync sent from the client side to the server side.

       o      Total bytes received is the count of all non-message
              bytes that rsync received by the client side from
              the server side. "Non-message" bytes means that we
              don't count the bytes for a verbose message that the
              server sent to us, which makes the stats more
              consistent.

--8-bit-output, -8
       This tells rsync to leave all high-bit characters unescaped
       in the output instead of trying to test them to see if
       they're valid in the current locale and escaping the
       invalid ones.  All control characters (but never tabs) are
       always escaped, regardless of this option's setting.

       The escape idiom that started in 2.6.7 is to output a
       literal backslash (\) and a hash (#), followed by exactly 3
       octal digits.  For example, a newline would output as
       "\#012".  A literal backslash that is in a filename is not
       escaped unless it is followed by a hash and 3 digits (0-9).

--human-readable, -h
       Output numbers in a more human-readable format.  There are
       3 possible levels:

       1.     output numbers with a separator between each set of
              3 digits (either a comma or a period, depending on
              if the decimal point is represented by a period or a
              comma).

       2.     output numbers in units of 1000 (with a character
              suffix for larger units -- see below).

       3.     output numbers in units of 1024.

       The default is human-readable level 1.  Each -h option
       increases the level by one.  You can take the level down to
       0 (to output numbers as pure digits) by specifying the
       --no-human-readable (--no-h) option.

       The unit letters that are appended in levels 2 and 3 are: K
       (kilo), M (mega), G (giga), T (tera), or P (peta).  For
       example, a 1234567-byte file would output as 1.23M in
       level-2 (assuming that a period is your local decimal
       point).

       Backward compatibility note: versions of rsync prior to
       3.1.0 do not support human-readable level 1, and they
       default to level 0.  Thus, specifying one or two -h options
       will behave in a comparable manner in old and new versions
       as long as you didn't specify a --no-h option prior to one
       or more -h options.  See the --list-only option for one
       difference.

--partial
       By default, rsync will delete any partially transferred
       file if the transfer is interrupted.  In some circumstances
       it is more desirable to keep partially transferred files.
       Using the --partial option tells rsync to keep the partial
       file which should make a subsequent transfer of the rest of
       the file much faster.

--partial-dir=DIR
       This option modifies the behavior of the --partial option
       while also implying that it be enabled.  This enhanced
       partial-file method puts any partially transferred files
       into the specified DIR instead of writing the partial file
       out to the destination file.  On the next transfer, rsync
       will use a file found in this dir as data to speed up the
       resumption of the transfer and then delete it after it has
       served its purpose.

       Note that if --whole-file is specified (or implied), any
       partial-dir files that are found for a file that is being
       updated will simply be removed (since rsync is sending
       files without using rsync's delta-transfer algorithm).

       Rsync will create the DIR if it is missing, but just the
       last dir -- not the whole path.  This makes it easy to use
       a relative path (such as "--partial-dir=.rsync-partial") to
       have rsync create the partial-directory in the destination
       file's directory when it is needed, and then remove it
       again when the partial file is deleted.  Note that this
       directory removal is only done for a relative pathname, as
       it is expected that an absolute path is to a directory that
       is reserved for partial-dir work.

       If the partial-dir value is not an absolute path, rsync
       will add an exclude rule at the end of all your existing
       excludes.  This will prevent the sending of any partial-dir
       files that may exist on the sending side, and will also
       prevent the untimely deletion of partial-dir items on the
       receiving side.  An example: the above --partial-dir option
       would add the equivalent of this "perishable" exclude at
       the end of any other filter rules: -f '-p .rsync-partial/'

       If you are supplying your own exclude rules, you may need
       to add your own exclude/hide/protect rule for the partial-
       dir because:

       1.     the auto-added rule may be ineffective at the end of
              your other rules, or

       2.     you may wish to override rsync's exclude choice.

       For instance, if you want to make rsync clean-up any left-
       over partial-dirs that may be lying around, you should
       specify --delete-after and add a "risk" filter rule, e.g.
       -f 'R .rsync-partial/'. Avoid using --delete-before or
       --delete-during unless you don't need rsync to use any of
       the left-over partial-dir data during the current run.

       IMPORTANT: the --partial-dir should not be writable by
       other users or it is a security risk!  E.g. AVOID "/tmp"!

       You can also set the partial-dir value the
       RSYNC_PARTIAL_DIR environment variable.  Setting this in
       the environment does not force --partial to be enabled, but
       rather it affects where partial files go when --partial is
       specified.  For instance, instead of using
       --partial-dir=.rsync-tmp along with --progress, you could
       set RSYNC_PARTIAL_DIR=.rsync-tmp in your environment and
       then use the -P option to turn on the use of the .rsync-tmp
       dir for partial transfers.  The only times that the
       --partial option does not look for this environment value
       are:

       1.     when --inplace was specified (since --inplace
              conflicts with --partial-dir), and

       2.     when --delay-updates was specified (see below).

       When a modern rsync resumes the transfer of a file in the
       partial-dir, that partial file is now updated in-place
       instead of creating yet another tmp-file copy (so it maxes
       out at dest + tmp instead of dest + partial + tmp).  This
       requires both ends of the transfer to be at least version
       3.2.0.

       For the purposes of the daemon-config's "refuse options"
       setting, --partial-dir does not imply --partial.  This is
       so that a refusal of the --partial option can be used to
       disallow the overwriting of destination files with a
       partial transfer, while still allowing the safer idiom
       provided by --partial-dir.

--delay-updates
       This option puts the temporary file from each updated file
       into a holding directory until the end of the transfer, at
       which time all the files are renamed into place in rapid
       succession.  This attempts to make the updating of the
       files a little more atomic.  By default the files are
       placed into a directory named .~tmp~ in each file's
       destination directory, but if you've specified the
       --partial-dir option, that directory will be used instead.
       See the comments in the --partial-dir section for a
       discussion of how this .~tmp~ dir will be excluded from the
       transfer, and what you can do if you want rsync to cleanup
       old .~tmp~ dirs that might be lying around.  Conflicts with
       --inplace and --append.

       This option implies --no-inc-recursive since it needs the
       full file list in memory in order to be able to iterate
       over it at the end.

       This option uses more memory on the receiving side (one bit
       per file transferred) and also requires enough free disk
       space on the receiving side to hold an additional copy of
       all the updated files.  Note also that you should not use
       an absolute path to --partial-dir unless:

       1.     there is no chance of any of the files in the
              transfer having the same name (since all the updated
              files will be put into a single directory if the
              path is absolute), and

       2.     there are no mount points in the hierarchy (since
              the delayed updates will fail if they can't be
              renamed into place).

       See also the "atomic-rsync" python script in the "support"
       subdir for an update algorithm that is even more atomic (it
       uses --link-dest and a parallel hierarchy of files).

--prune-empty-dirs, -m
       This option tells the receiving rsync to get rid of empty
       directories from the file-list, including nested
       directories that have no non-directory children.  This is
       useful for avoiding the creation of a bunch of useless
       directories when the sending rsync is recursively scanning
       a hierarchy of files using include/exclude/filter rules.

       This option can still leave empty directories on the
       receiving side if you make use of TRANSFER_RULES.

       Because the file-list is actually being pruned, this option
       also affects what directories get deleted when a delete is
       active.  However, keep in mind that excluded files and
       directories can prevent existing items from being deleted
       due to an exclude both hiding source files and protecting
       destination files.  See the perishable filter-rule option
       for how to avoid this.

       You can prevent the pruning of certain empty directories
       from the file-list by using a global "protect" filter.  For
       instance, this option would ensure that the directory
       "emptydir" was kept in the file-list:

           --filter 'protect emptydir/'

       Here's an example that copies all .pdf files in a
       hierarchy, only creating the necessary destination
       directories to hold the .pdf files, and ensures that any
       superfluous files and directories in the destination are
       removed (note the hide filter of non-directories being used
       instead of an exclude):

           rsync -avm --del --include='*.pdf' -f 'hide,! */' src/ dest

       If you didn't want to remove superfluous destination files,
       the more time-honored options of
       --include='*/' --exclude='*' would work fine in place of
       the hide-filter (if that is more natural to you).

--progress
       This option tells rsync to print information showing the
       progress of the transfer.  This gives a bored user
       something to watch.  With a modern rsync this is the same
       as specifying --info=flist2,name,progress, but any user-
       supplied settings for those info flags takes precedence
       (e.g.  --info=flist0 --progress).

       While rsync is transferring a regular file, it updates a
       progress line that looks like this:

           782448  63%  110.64kB/s    0:00:04

       In this example, the receiver has reconstructed 782448
       bytes or 63% of the sender's file, which is being
       reconstructed at a rate of 110.64 kilobytes per second, and
       the transfer will finish in 4 seconds if the current rate
       is maintained until the end.

       These statistics can be misleading if rsync's delta-
       transfer algorithm is in use.  For example, if the sender's
       file consists of the basis file followed by additional
       data, the reported rate will probably drop dramatically
       when the receiver gets to the literal data, and the
       transfer will probably take much longer to finish than the
       receiver estimated as it was finishing the matched part of
       the file.

       When the file transfer finishes, rsync replaces the
       progress line with a summary line that looks like this:

           1,238,099 100%  146.38kB/s    0:00:08  (xfr#5, to-chk=169/396)

       In this example, the file was 1,238,099 bytes long in
       total, the average rate of transfer for the whole file was
       146.38 kilobytes per second over the 8 seconds that it took
       to complete, it was the 5th transfer of a regular file
       during the current rsync session, and there are 169 more
       files for the receiver to check (to see if they are up-to-
       date or not) remaining out of the 396 total files in the
       file-list.

       In an incremental recursion scan, rsync won't know the
       total number of files in the file-list until it reaches the
       ends of the scan, but since it starts to transfer files
       during the scan, it will display a line with the text "ir-
       chk" (for incremental recursion check) instead of "to-chk"
       until the point that it knows the full size of the list, at
       which point it will switch to using "to-chk".  Thus, seeing
       "ir-chk" lets you know that the total count of files in the
       file list is still going to increase (and each time it
       does, the count of files left to check will increase by the
       number of the files added to the list).

-P     The -P option is equivalent to "--partial --progress".  Its
       purpose is to make it much easier to specify these two
       options for a long transfer that may be interrupted.

       There is also a --info=progress2 option that outputs
       statistics based on the whole transfer, rather than
       individual files.  Use this flag without outputting a
       filename (e.g. avoid -v or specify --info=name0) if you
       want to see how the transfer is doing without scrolling the
       screen with a lot of names. (You don't need to specify the
       --progress option in order to use --info=progress2.)

       Finally, you can get an instant progress report by sending
       rsync a signal of either SIGINFO or SIGVTALRM.  On BSD
       systems, a SIGINFO is generated by typing a Ctrl+T (Linux
       doesn't currently support a SIGINFO signal).  When the
       client-side process receives one of those signals, it sets
       a flag to output a single progress report which is output
       when the current file transfer finishes (so it may take a
       little time if a big file is being handled when the signal
       arrives).  A filename is output (if needed) followed by the
       --info=progress2 format of progress info.  If you don't
       know which of the 3 rsync processes is the client process,
       it's OK to signal all of them (since the non-client
       processes ignore the signal).

       CAUTION: sending SIGVTALRM to an older rsync (pre-3.2.0)
       will kill it.

--password-file=FILE
       This option allows you to provide a password for accessing
       an rsync daemon via a file or via standard input if FILE is
       -.  The file should contain just the password on the first
       line (all other lines are ignored).  Rsync will exit with
       an error if FILE is world readable or if a root-run rsync
       command finds a non-root-owned file.

       This option does not supply a password to a remote shell
       transport such as ssh; to learn how to do that, consult the
       remote shell's documentation.  When accessing an rsync
       daemon using a remote shell as the transport, this option
       only comes into effect after the remote shell finishes its
       authentication (i.e. if you have also specified a password
       in the daemon's config file).

--early-input=FILE
       This option allows rsync to send up to 5K of data to the
       "early exec" script on its stdin.  One possible use of this
       data is to give the script a secret that can be used to
       mount an encrypted filesystem (which you should unmount in
       the the "post-xfer exec" script).

       The daemon must be at least version 3.2.1.

--list-only
       This option will cause the source files to be listed
       instead of transferred.  This option is inferred if there
       is a single source arg and no destination specified, so its
       main uses are:

       1.     to turn a copy command that includes a destination
              arg into a file-listing command, or

       2.     to be able to specify more than one source arg.
              Note: be sure to include the destination.

       CAUTION: keep in mind that a source arg with a wild-card is
       expanded by the shell into multiple args, so it is never
       safe to try to specify a single wild-card arg to try to
       infer this option. A safe example is:

           rsync -av --list-only foo* dest/

       This option always uses an output format that looks similar
       to this:

           drwxrwxr-x          4,096 2022/09/30 12:53:11 support
           -rw-rw-r--             80 2005/01/11 10:37:37 support/Makefile

       The only option that affects this output style is (as of
       3.1.0) the --human-readable (-h) option.  The default is to
       output sizes as byte counts with digit separators (in a
       14-character-width column).  Specifying at least one -h
       option makes the sizes output with unit suffixes.  If you
       want old-style bytecount sizes without digit separators
       (and an 11-character-width column) use --no-h.

       Compatibility note: when requesting a remote listing of
       files from an rsync that is version 2.6.3 or older, you may
       encounter an error if you ask for a non-recursive listing.
       This is because a file listing implies the --dirs option
       w/o --recursive, and older rsyncs don't have that option.
       To avoid this problem, either specify the --no-dirs option
       (if you don't need to expand a directory's content), or
       turn on recursion and exclude the content of
       subdirectories: -r --exclude='/*/*'.

--bwlimit=RATE
       This option allows you to specify the maximum transfer rate
       for the data sent over the socket, specified in units per
       second.  The RATE value can be suffixed with a string to
       indicate a size multiplier, and may be a fractional value
       (e.g. --bwlimit=1.5m).  If no suffix is specified, the
       value will be assumed to be in units of 1024 bytes (as if
       "K" or "KiB" had been appended).  See the --max-size option
       for a description of all the available suffixes.  A value
       of 0 specifies no limit.

       For backward-compatibility reasons, the rate limit will be
       rounded to the nearest KiB unit, so no rate smaller than
       1024 bytes per second is possible.

       Rsync writes data over the socket in blocks, and this
       option both limits the size of the blocks that rsync
       writes, and tries to keep the average transfer rate at the
       requested limit.  Some burstiness may be seen where rsync
       writes out a block of data and then sleeps to bring the
       average rate into compliance.

       Due to the internal buffering of data, the --progress
       option may not be an accurate reflection on how fast the
       data is being sent.  This is because some files can show up
       as being rapidly sent when the data is quickly buffered,
       while other can show up as very slow when the flushing of
       the output buffer occurs.  This may be fixed in a future
       version.

       See also the daemon version of the --bwlimit option.

--stop-after=MINS, (--time-limit=MINS)
       This option tells rsync to stop copying when the specified
       number of minutes has elapsed.

       For maximal flexibility, rsync does not communicate this
       option to the remote rsync since it is usually enough that
       one side of the connection quits as specified.  This allows
       the option's use even when only one side of the connection
       supports it.  You can tell the remote side about the time
       limit using --remote-option (-M), should the need arise.

       The --time-limit version of this option is deprecated.

--stop-at=y-m-dTh:m
       This option tells rsync to stop copying when the specified
       point in time has been reached. The date & time can be
       fully specified in a numeric format of year-month-
       dayThour:minute (e.g. 2000-12-31T23:59) in the local
       timezone.  You may choose to separate the date numbers
       using slashes instead of dashes.

       The value can also be abbreviated in a variety of ways,
       such as specifying a 2-digit year and/or leaving off
       various values.  In all cases, the value will be taken to
       be the next possible point in time where the supplied
       information matches.  If the value specifies the current
       time or a past time, rsync exits with an error.

       For example, "1-30" specifies the next January 30th (at
       midnight local time), "14:00" specifies the next 2 P.M.,
       "1" specifies the next 1st of the month at midnight, "31"
       specifies the next month where we can stop on its 31st day,
       and ":59" specifies the next 59th minute after the hour.

       For maximal flexibility, rsync does not communicate this
       option to the remote rsync since it is usually enough that
       one side of the connection quits as specified.  This allows
       the option's use even when only one side of the connection
       supports it.  You can tell the remote side about the time
       limit using --remote-option (-M), should the need arise.
       Do keep in mind that the remote host may have a different
       default timezone than your local host.

--fsync
       Cause the receiving side to fsync each finished file.  This
       may slow down the transfer, but can help to provide peace
       of mind when updating critical files.

--write-batch=FILE
       Record a file that can later be applied to another
       identical destination with --read-batch.  See the "BATCH
       MODE" section for details, and also the --only-write-batch
       option.

       This option overrides the negotiated checksum & compress
       lists and always negotiates a choice based on old-school
       md5/md4/zlib choices.  If you want a more modern choice,
       use the --checksum-choice (--cc) and/or --compress-choice
       (--zc) options.

--only-write-batch=FILE
       Works like --write-batch, except that no updates are made
       on the destination system when creating the batch.  This
       lets you transport the changes to the destination system
       via some other means and then apply the changes via
       --read-batch.

       Note that you can feel free to write the batch directly to
       some portable media: if this media fills to capacity before
       the end of the transfer, you can just apply that partial
       transfer to the destination and repeat the whole process to
       get the rest of the changes (as long as you don't mind a
       partially updated destination system while the multi-update
       cycle is happening).

       Also note that you only save bandwidth when pushing changes
       to a remote system because this allows the batched data to
       be diverted from the sender into the batch file without
       having to flow over the wire to the receiver (when pulling,
       the sender is remote, and thus can't write the batch).

--read-batch=FILE
       Apply all of the changes stored in FILE, a file previously
       generated by --write-batch.  If FILE is -, the batch data
       will be read from standard input. See the "BATCH MODE"
       section for details.

--protocol=NUM
       Force an older protocol version to be used.  This is useful
       for creating a batch file that is compatible with an older
       version of rsync.  For instance, if rsync 2.6.4 is being
       used with the --write-batch option, but rsync 2.6.3 is what
       will be used to run the --read-batch option, you should use
       "--protocol=28" when creating the batch file to force the
       older protocol version to be used in the batch file
       (assuming you can't upgrade the rsync on the reading
       system).

--iconv=CONVERT_SPEC
       Rsync can convert filenames between character sets using
       this option.  Using a CONVERT_SPEC of "." tells rsync to
       look up the default character-set via the locale setting.
       Alternately, you can fully specify what conversion to do by
       giving a local and a remote charset separated by a comma in
       the order --iconv=LOCAL,REMOTE, e.g. --iconv=utf8,iso88591.
       This order ensures that the option will stay the same
       whether you're pushing or pulling files.  Finally, you can
       specify either --no-iconv or a CONVERT_SPEC of "-" to turn
       off any conversion.  The default setting of this option is
       site-specific, and can also be affected via the RSYNC_ICONV
       environment variable.

       For a list of what charset names your local iconv library
       supports, you can run "iconv --list".

       If you specify the --secluded-args (-s) option, rsync will
       translate the filenames you specify on the command-line
       that are being sent to the remote host.  See also the
       --files-from option.

       Note that rsync does not do any conversion of names in
       filter files (including include/exclude files).  It is up
       to you to ensure that you're specifying matching rules that
       can match on both sides of the transfer.  For instance, you
       can specify extra include/exclude rules if there are
       filename differences on the two sides that need to be
       accounted for.

       When you pass an --iconv option to an rsync daemon that
       allows it, the daemon uses the charset specified in its
       "charset" configuration parameter regardless of the remote
       charset you actually pass.  Thus, you may feel free to
       specify just the local charset for a daemon transfer (e.g.
       --iconv=utf8).

--ipv4, -4 or --ipv6, -6
       Tells rsync to prefer IPv4/IPv6 when creating sockets or
       running ssh.  This affects sockets that rsync has direct
       control over, such as the outgoing socket when directly
       contacting an rsync daemon, as well as the forwarding of
       the -4 or -6 option to ssh when rsync can deduce that ssh
       is being used as the remote shell.  For other remote shells
       you'll need to specify the "--rsh SHELL -4" option directly
       (or whatever IPv4/IPv6 hint options it uses).

       See also the daemon version of these options.

       If rsync was compiled without support for IPv6, the --ipv6
       option will have no effect.  The rsync --version output
       will contain "no IPv6" if is the case.

--checksum-seed=NUM
       Set the checksum seed to the integer NUM.  This 4 byte
       checksum seed is included in each block and MD4 file
       checksum calculation (the more modern MD5 file checksums
       don't use a seed).  By default the checksum seed is
       generated by the server and defaults to the current time().
       This option is used to set a specific checksum seed, which
       is useful for applications that want repeatable block
       checksums, or in the case where the user wants a more
       random checksum seed.  Setting NUM to 0 causes rsync to use
       the default of time() for checksum seed.


## DAEMON OPTIONS

The options allowed when starting an rsync daemon are as follows:

--daemon
       This tells rsync that it is to run as a daemon.  The daemon
       you start running may be accessed using an rsync client
       using the host::module or rsync://host/module/ syntax.

       If standard input is a socket then rsync will assume that
       it is being run via inetd, otherwise it will detach from
       the current terminal and become a background daemon.  The
       daemon will read the config file (rsyncd.conf) on each
       connect made by a client and respond to requests
       accordingly.

       See the rsyncd.conf(5) manpage for more details.

--address=ADDRESS
       By default rsync will bind to the wildcard address when run
       as a daemon with the --daemon option.  The --address option
       allows you to specify a specific IP address (or hostname)
       to bind to.  This makes virtual hosting possible in
       conjunction with the --config option.

       See also the address global option in the rsyncd.conf
       manpage and the client version of the --address option.

--bwlimit=RATE
       This option allows you to specify the maximum transfer rate
       for the data the daemon sends over the socket.  The client
       can still specify a smaller --bwlimit value, but no larger
       value will be allowed.

       See the client version of the --bwlimit option for some
       extra details.

--config=FILE
       This specifies an alternate config file than the default.
       This is only relevant when --daemon is specified.  The
       default is /etc/rsyncd.conf unless the daemon is running
       over a remote shell program and the remote user is not the
       super-user; in that case the default is rsyncd.conf in the
       current directory (typically $HOME).

--dparam=OVERRIDE, -M
       This option can be used to set a daemon-config parameter
       when starting up rsync in daemon mode.  It is equivalent to
       adding the parameter at the end of the global settings
       prior to the first module's definition.  The parameter
       names can be specified without spaces, if you so desire.
       For instance:

           rsync --daemon -M pidfile=/path/rsync.pid

--no-detach
       When running as a daemon, this option instructs rsync to
       not detach itself and become a background process.  This
       option is required when running as a service on Cygwin, and
       may also be useful when rsync is supervised by a program
       such as daemontools or AIX's System Resource Controller.
       --no-detach is also recommended when rsync is run under a
       debugger.  This option has no effect if rsync is run from
       inetd or sshd.

--port=PORT
       This specifies an alternate TCP port number for the daemon
       to listen on rather than the default of 873.

       See also the client version of the --port option and the
       port global setting in the rsyncd.conf manpage.

--log-file=FILE
       This option tells the rsync daemon to use the given log-
       file name instead of using the "log file" setting in the
       config file.

       See also the client version of the --log-file option.

--log-file-format=FORMAT
       This option tells the rsync daemon to use the given FORMAT
       string instead of using the "log format" setting in the
       config file.  It also enables "transfer logging" unless the
       string is empty, in which case transfer logging is turned
       off.

       See also the client version of the --log-file-format
       option.

--sockopts
       This overrides the socket options setting in the
       rsyncd.conf file and has the same syntax.

       See also the client version of the --sockopts option.

--verbose, -v
       This option increases the amount of information the daemon
       logs during its startup phase.  After the client connects,
       the daemon's verbosity level will be controlled by the
       options that the client used and the "max verbosity"
       setting in the module's config section.

       See also the client version of the --verbose option.

--ipv4, -4 or --ipv6, -6
       Tells rsync to prefer IPv4/IPv6 when creating the incoming
       sockets that the rsync daemon will use to listen for
       connections.  One of these options may be required in older
       versions of Linux to work around an IPv6 bug in the kernel
       (if you see an "address already in use" error when nothing
       else is using the port, try specifying --ipv6 or --ipv4
       when starting the daemon).

       See also the client version of these options.

       If rsync was compiled without support for IPv6, the --ipv6
       option will have no effect.  The rsync --version output
       will contain "no IPv6" if is the case.

--help, -h
       When specified after --daemon, print a short help page
       describing the options available for starting an rsync
       daemon.
