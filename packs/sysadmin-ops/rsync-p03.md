---
title: "rsync(1) (part 3/5)"
source: https://man7.org/linux/man-pages/man1/rsync.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 3/5
---

# rsync(1)

The exclude list is initialized to exclude the following
       items (these initial items are marked as perishable -- see
       the FILTER RULES section):

           RCS SCCS CVS CVS.adm RCSLOG cvslog.*  tags TAGS
           .make.state .nse_depinfo *~ #* .#* ,* _$* *$ *.old
           *.bak *.BAK *.orig *.rej .del-* *.a *.olb *.o *.obj
           *.so *.exe *.Z *.elc *.ln core .svn/ .git/ .hg/ .bzr/

       then, files listed in a $HOME/.cvsignore are added to the
       list and any files listed in the CVSIGNORE environment
       variable (all cvsignore names are delimited by whitespace).

       Finally, any file is ignored if it is in the same directory
       as a .cvsignore file and matches one of the patterns listed
       therein.  Unlike rsync's filter/exclude files, these
       patterns are split on whitespace.  See the cvs(1) manual
       for more information.

       If you're combining -C with your own --filter rules, you
       should note that these CVS excludes are appended at the end
       of your own rules, regardless of where the -C was placed on
       the command-line.  This makes them a lower priority than
       any rules you specified explicitly.  If you want to control
       where these CVS excludes get inserted into your filter
       rules, you should omit the -C as a command-line option and
       use a combination of --filter=:C and --filter=-C (either on
       your command-line or by putting the ":C" and "-C" rules
       into a filter file with your other rules).  The first
       option turns on the per-directory scanning for the
       .cvsignore file.  The second option does a one-time import
       of the CVS excludes mentioned above.

--filter=RULE, -f
       This option allows you to add rules to selectively exclude
       certain files from the list of files to be transferred.
       This is most useful in combination with a recursive
       transfer.

       You may use as many --filter options on the command line as
       you like to build up the list of files to exclude.  If the
       filter contains whitespace, be sure to quote it so that the
       shell gives the rule to rsync as a single argument.  The
       text below also mentions that you can use an underscore to
       replace the space that separates a rule from its arg.

       See the FILTER RULES section for detailed information on
       this option.

-F     The -F option is a shorthand for adding two --filter rules
       to your command.  The first time it is used is a shorthand
       for this rule:

           --filter='dir-merge /.rsync-filter'

       This tells rsync to look for per-directory .rsync-filter
       files that have been sprinkled through the hierarchy and
       use their rules to filter the files in the transfer.  If -F
       is repeated, it is a shorthand for this rule:

           --filter='exclude .rsync-filter'

       This filters out the .rsync-filter files themselves from
       the transfer.

       See the FILTER RULES section for detailed information on
       how these options work.

--exclude=PATTERN
       This option is a simplified form of the --filter option
       that specifies an exclude rule and does not allow the full
       rule-parsing syntax of normal filter rules.  This is
       equivalent to specifying -f'- PATTERN'.

       See the FILTER RULES section for detailed information on
       this option.

--exclude-from=FILE
       This option is related to the --exclude option, but it
       specifies a FILE that contains exclude patterns (one per
       line).  Blank lines in the file are ignored, as are whole-
       line comments that start with ';' or '#' (filename rules
       that contain those characters are unaffected).

       If a line begins with "- " (dash, space) or "+ " (plus,
       space), then the type of rule is being explicitly specified
       as an exclude or an include (respectively).  Any rules
       without such a prefix are taken to be an exclude.

       If a line consists of just "!", then the current filter
       rules are cleared before adding any further rules.

       If FILE is '-', the list will be read from standard input.

--include=PATTERN
       This option is a simplified form of the --filter option
       that specifies an include rule and does not allow the full
       rule-parsing syntax of normal filter rules.  This is
       equivalent to specifying -f'+ PATTERN'.

       See the FILTER RULES section for detailed information on
       this option.

--include-from=FILE
       This option is related to the --include option, but it
       specifies a FILE that contains include patterns (one per
       line).  Blank lines in the file are ignored, as are whole-
       line comments that start with ';' or '#' (filename rules
       that contain those characters are unaffected).

       If a line begins with "- " (dash, space) or "+ " (plus,
       space), then the type of rule is being explicitly specified
       as an exclude or an include (respectively).  Any rules
       without such a prefix are taken to be an include.

       If a line consists of just "!", then the current filter
       rules are cleared before adding any further rules.

       If FILE is '-', the list will be read from standard input.

--files-from=FILE
       Using this option allows you to specify the exact list of
       files to transfer (as read from the specified FILE or '-'
       for standard input).  It also tweaks the default behavior
       of rsync to make transferring just the specified files and
       directories easier:

       o      The --relative (-R) option is implied, which
              preserves the path information that is specified for
              each item in the file (use --no-relative or --no-R
              if you want to turn that off).

       o      The --dirs (-d) option is implied, which will create
              directories specified in the list on the destination
              rather than noisily skipping them (use --no-dirs or
              --no-d if you want to turn that off).

       o      The --archive (-a) option's behavior does not imply
              --recursive (-r), so specify it explicitly, if you
              want it.

       o      These side-effects change the default state of
              rsync, so the position of the --files-from option on
              the command-line has no bearing on how other options
              are parsed (e.g. -a works the same before or after
              --files-from, as does --no-R and all other options).

       The filenames that are read from the FILE are all relative
       to the source dir -- any leading slashes are removed and no
       ".." references are allowed to go higher than the source
       dir.  For example, take this command:

           rsync -a --files-from=/tmp/foo /usr remote:/backup

       If /tmp/foo contains the string "bin" (or even "/bin"), the
       /usr/bin directory will be created as /backup/bin on the
       remote host.  If it contains "bin/" (note the trailing
       slash), the immediate contents of the directory would also
       be sent (without needing to be explicitly mentioned in the
       file -- this began in version 2.6.4).  In both cases, if
       the -r option was enabled, that dir's entire hierarchy
       would also be transferred (keep in mind that -r needs to be
       specified explicitly with --files-from, since it is not
       implied by -a.  Also note that the effect of the (enabled
       by default) -r option is to duplicate only the path info
       that is read from the file -- it does not force the
       duplication of the source-spec path (/usr in this case).

       In addition, the --files-from file can be read from the
       remote host instead of the local host if you specify a
       "host:" in front of the file (the host must match one end
       of the transfer).  As a short-cut, you can specify just a
       prefix of ":" to mean "use the remote end of the transfer".
       For example:

           rsync -a --files-from=:/path/file-list src:/ /tmp/copy

       This would copy all the files specified in the /path/file-
       list file that was located on the remote "src" host.

       If the --iconv and --secluded-args options are specified
       and the --files-from filenames are being sent from one host
       to another, the filenames will be translated from the
       sending host's charset to the receiving host's charset.

       NOTE: sorting the list of files in the --files-from input
       helps rsync to be more efficient, as it will avoid re-
       visiting the path elements that are shared between adjacent
       entries.  If the input is not sorted, some path elements
       (implied directories) may end up being scanned multiple
       times, and rsync will eventually unduplicate them after
       they get turned into file-list elements.

--from0, -0
       This tells rsync that the rules/filenames it reads from a
       file are terminated by a null ('\0') character, not a NL,
       CR, or CR+LF.  This affects --exclude-from, --include-from,
       --files-from, and any merged files specified in a --filter
       rule.  It does not affect --cvs-exclude (since all names
       read from a .cvsignore file are split on whitespace).

--old-args
       This option tells rsync to stop trying to protect the arg
       values on the remote side from unintended word-splitting or
       other misinterpretation.  It also allows the client to
       treat an empty arg as a "." instead of generating an error.

       The default in a modern rsync is for "shell-active"
       characters (including spaces) to be backslash-escaped in
       the args that are sent to the remote shell.  The wildcard
       characters *, ?, [, & ] are not escaped in filename args
       (allowing them to expand into multiple filenames) while
       being protected in option args, such as --usermap.

       If you have a script that wants to use old-style arg
       splitting in its filenames, specify this option once.  If
       the remote shell has a problem with any backslash escapes
       at all, specify this option twice.

       You may also control this setting via the RSYNC_OLD_ARGS
       environment variable.  If it has the value "1", rsync will
       default to a single-option setting.  If it has the value
       "2" (or more), rsync will default to a repeated-option
       setting.  If it is "0", you'll get the default escaping
       behavior.  The environment is always overridden by manually
       specified positive or negative options (the negative is
       --no-old-args).

       Note that this option also disables the extra safety check
       added in 3.2.5 that ensures that a remote sender isn't
       including extra top-level items in the file-list that you
       didn't request.  This side-effect is necessary because we
       can't know for sure what names to expect when the remote
       shell is interpreting the args.

       This option conflicts with the --secluded-args option.

--secluded-args, -s
       This option sends all filenames and most options to the
       remote rsync via the protocol (not the remote shell command
       line) which avoids letting the remote shell modify them.
       Wildcards are expanded on the remote host by rsync instead
       of a shell.

       This is similar to the default backslash-escaping of args
       that was added in 3.2.4 (see --old-args) in that it
       prevents things like space splitting and unwanted special-
       character side-effects. However, it has the drawbacks of
       being incompatible with older rsync versions (prior to
       3.0.0) and of being refused by restricted shells that want
       to be able to inspect all the option values for safety.

       This option is useful for those times that you need the
       argument's character set to be converted for the remote
       host, if the remote shell is incompatible with the default
       backslash-escpaing method, or there is some other reason
       that you want the majority of the options and arguments to
       bypass the command-line of the remote shell.

       If you combine this option with --iconv, the args related
       to the remote side will be translated from the local to the
       remote character-set.  The translation happens before wild-
       cards are expanded.  See also the --files-from option.

       You may also control this setting via the
       RSYNC_PROTECT_ARGS environment variable.  If it has a non-
       zero value, this setting will be enabled by default,
       otherwise it will be disabled by default.  Either state is
       overridden by a manually specified positive or negative
       version of this option (note that --no-s and
       --no-secluded-args are the negative versions).  This
       environment variable is also superseded by a non-zero
       RSYNC_OLD_ARGS export.

       This option conflicts with the --old-args option.

       This option used to be called --protect-args (before 3.2.6)
       and that older name can still be used (though specifying it
       as -s is always the easiest and most compatible choice).

--trust-sender
       This option disables two extra validation checks that a
       local client performs on the file list generated by a
       remote sender.  This option should only be used if you
       trust the sender to not put something malicious in the file
       list (something that could possibly be done via a modified
       rsync, a modified shell, or some other similar
       manipulation).

       Normally, the rsync client (as of version 3.2.5) runs two
       extra validation checks when pulling files from a remote
       rsync:

       o      It verifies that additional arg items didn't get
              added at the top of the transfer.

       o      It verifies that none of the items in the file list
              are names that should have been excluded (if filter
              rules were specified).

       Note that various options can turn off one or both of these
       checks if the option interferes with the validation.  For
       instance:

       o      Using a per-directory filter file reads filter rules
              that only the server knows about, so the filter
              checking is disabled.

       o      Using the --old-args option allows the sender to
              manipulate the requested args, so the arg checking
              is disabled.

       o      Reading the files-from list from the server side
              means that the client doesn't know the arg list, so
              the arg checking is disabled.

       o      Using --read-batch disables both checks since the
              batch file's contents will have been verified when
              it was created.

       This option may help an under-powered client server if the
       extra pattern matching is slowing things down on a huge
       transfer.  It can also be used to work around a currently-
       unknown bug in the verification logic for a transfer from a
       trusted sender.

       When using this option it is a good idea to specify a
       dedicated destination directory, as discussed in the MULTI-
       HOST SECURITY section.

--copy-as=USER[:GROUP]
       This option instructs rsync to use the USER and (if
       specified after a colon) the GROUP for the copy operations.
       This only works if the user that is running rsync has the
       ability to change users.  If the group is not specified
       then the user's default groups are used.

       This option can help to reduce the risk of an rsync being
       run as root into or out of a directory that might have live
       changes happening to it and you want to make sure that
       root-level read or write actions of system files are not
       possible.  While you could alternatively run all of rsync
       as the specified user, sometimes you need the root-level
       host-access credentials to be used, so this allows rsync to
       drop root for the copying part of the operation after the
       remote-shell or daemon connection is established.

       The option only affects one side of the transfer unless the
       transfer is local, in which case it affects both sides.
       Use the --remote-option to affect the remote side, such as
       -M--copy-as=joe.  For a local transfer, the lsh (or lsh.sh)
       support file provides a local-shell helper script that can
       be used to allow a "localhost:" or "lh:" host-spec to be
       specified without needing to setup any remote shells,
       allowing you to specify remote options that affect the side
       of the transfer that is using the host-spec (and using
       hostname "lh" avoids the overriding of the remote directory
       to the user's home dir).

       For example, the following rsync writes the local files as
       user "joe":

           sudo rsync -aiv --copy-as=joe host1:backups/joe/ /home/joe/

       This makes all files owned by user "joe", limits the groups
       to those that are available to that user, and makes it
       impossible for the joe user to do a timed exploit of the
       path to induce a change to a file that the joe user has no
       permissions to change.

       The following command does a local copy into the "dest/"
       dir as user "joe" (assuming you've installed support/lsh
       into a dir on your $PATH):

           sudo rsync -aive lsh -M--copy-as=joe src/ lh:dest/

--temp-dir=DIR, -T
       This option instructs rsync to use DIR as a scratch
       directory when creating temporary copies of the files
       transferred on the receiving side.  The default behavior is
       to create each temporary file in the same directory as the
       associated destination file.  Beginning with rsync 3.1.1,
       the temp-file names inside the specified DIR will not be
       prefixed with an extra dot (though they will still have a
       random suffix added).

       This option is most often used when the receiving disk
       partition does not have enough free space to hold a copy of
       the largest file in the transfer.  In this case (i.e. when
       the scratch directory is on a different disk partition),
       rsync will not be able to rename each received temporary
       file over the top of the associated destination file, but
       instead must copy it into place.  Rsync does this by
       copying the file over the top of the destination file,
       which means that the destination file will contain
       truncated data during this copy.  If this were not done
       this way (even if the destination file were first removed,
       the data locally copied to a temporary file in the
       destination directory, and then renamed into place) it
       would be possible for the old file to continue taking up
       disk space (if someone had it open), and thus there might
       not be enough room to fit the new version on the disk at
       the same time.

       If you are using this option for reasons other than a
       shortage of disk space, you may wish to combine it with the
       --delay-updates option, which will ensure that all copied
       files get put into subdirectories in the destination
       hierarchy, awaiting the end of the transfer.  If you don't
       have enough room to duplicate all the arriving files on the
       destination partition, another way to tell rsync that you
       aren't overly concerned about disk space is to use the
       --partial-dir option with a relative path; because this
       tells rsync that it is OK to stash off a copy of a single
       file in a subdir in the destination hierarchy, rsync will
       use the partial-dir as a staging area to bring over the
       copied file, and then rename it into place from there.
       (Specifying a --partial-dir with an absolute path does not
       have this side-effect.)

--fuzzy, -y
       This option tells rsync that it should look for a basis
       file for any destination file that is missing.  The current
       algorithm looks in the same directory as the destination
       file for either a file that has an identical size and
       modified-time, or a similarly-named file.  If found, rsync
       uses the fuzzy basis file to try to speed up the transfer.

       If the option is repeated, the fuzzy scan will also be done
       in any matching alternate destination directories that are
       specified via --compare-dest, --copy-dest, or --link-dest.

       Note that the use of the --delete option might get rid of
       any potential fuzzy-match files, so either use
       --delete-after or specify some filename exclusions if you
       need to prevent this.

--compare-dest=DIR
       This option instructs rsync to use DIR on the destination
       machine as an additional hierarchy to compare destination
       files against doing transfers (if the files are missing in
       the destination directory).  If a file is found in DIR that
       is identical to the sender's file, the file will NOT be
       transferred to the destination directory.  This is useful
       for creating a sparse backup of just files that have
       changed from an earlier backup.  This option is typically
       used to copy into an empty (or newly created) directory.

       Beginning in version 2.6.4, multiple --compare-dest
       directories may be provided, which will cause rsync to
       search the list in the order specified for an exact match.
       If a match is found that differs only in attributes, a
       local copy is made and the attributes updated.  If a match
       is not found, a basis file from one of the DIRs will be
       selected to try to speed up the transfer.

       If DIR is a relative path, it is relative to the
       destination directory.  See also --copy-dest and
       --link-dest.

       NOTE: beginning with version 3.1.0, rsync will remove a
       file from a non-empty destination hierarchy if an exact
       match is found in one of the compare-dest hierarchies
       (making the end result more closely match a fresh copy).

--copy-dest=DIR
       This option behaves like --compare-dest, but rsync will
       also copy unchanged files found in DIR to the destination
       directory using a local copy.  This is useful for doing
       transfers to a new destination while leaving existing files
       intact, and then doing a flash-cutover when all files have
       been successfully transferred.

       Multiple --copy-dest directories may be provided, which
       will cause rsync to search the list in the order specified
       for an unchanged file.  If a match is not found, a basis
       file from one of the DIRs will be selected to try to speed
       up the transfer.

       If DIR is a relative path, it is relative to the
       destination directory.  See also --compare-dest and
       --link-dest.

--link-dest=DIR
       This option behaves like --copy-dest, but unchanged files
       are hard linked from DIR to the destination directory.  The
       files must be identical in all preserved attributes (e.g.
       permissions, possibly ownership) in order for the files to
       be linked together.  An example:

           rsync -av --link-dest=$PWD/prior_dir host:src_dir/ new_dir/

       If files aren't linking, double-check their attributes.
       Also check if some attributes are getting forced outside of
       rsync's control, such a mount option that squishes root to
       a single user, or mounts a removable drive with generic
       ownership (such as OS X's "Ignore ownership on this volume"
       option).

       Beginning in version 2.6.4, multiple --link-dest
       directories may be provided, which will cause rsync to
       search the list in the order specified for an exact match
       (there is a limit of 20 such directories).  If a match is
       found that differs only in attributes, a local copy is made
       and the attributes updated.  If a match is not found, a
       basis file from one of the DIRs will be selected to try to
       speed up the transfer.

       This option works best when copying into an empty
       destination hierarchy, as existing files may get their
       attributes tweaked, and that can affect alternate
       destination files via hard-links.  Also, itemizing of
       changes can get a bit muddled.  Note that prior to version
       3.1.0, an alternate-directory exact match would never be
       found (nor linked into the destination) when a destination
       file already exists.

       Note that if you combine this option with --ignore-times,
       rsync will not link any files together because it only
       links identical files together as a substitute for
       transferring the file, never as an additional check after
       the file is updated.

       If DIR is a relative path, it is relative to the
       destination directory.  See also --compare-dest and
       --copy-dest.

       Note that rsync versions prior to 2.6.1 had a bug that
       could prevent --link-dest from working properly for a non-
       super-user when --owner (-o) was specified (or implied).
       You can work-around this bug by avoiding the -o option (or
       using --no-o) when sending to an old rsync.

--compress, -z
       With this option, rsync compresses the file data as it is
       sent to the destination machine, which reduces the amount
       of data being transmitted -- something that is useful over
       a slow connection.

       Rsync supports multiple compression methods and will choose
       one for you unless you force the choice using the
       --compress-choice (--zc) option.

       Run rsync --version to see the default compress list
       compiled into your version.

       When both sides of the transfer are at least 3.2.0, rsync
       chooses the first algorithm in the client's list of choices
       that is also in the server's list of choices.  If no common
       compress choice is found, rsync exits with an error.  If
       the remote rsync is too old to support checksum
       negotiation, its list is assumed to be "zlib".

       The default order can be customized by setting the
       environment variable RSYNC_COMPRESS_LIST to a space-
       separated list of acceptable compression names.  If the
       string contains a "&" character, it is separated into the
       "client string & server string", otherwise the same string
       applies to both.  If the string (or string portion)
       contains no non-whitespace characters, the default compress
       list is used.  Any unknown compression names are discarded
       from the list, but a list with only invalid names results
       in a failed negotiation.

       There are some older rsync versions that were configured to
       reject a -z option and require the use of -zz because their
       compression library was not compatible with the default
       zlib compression method.  You can usually ignore this
       weirdness unless the rsync server complains and tells you
       to specify -zz.

--compress-choice=STR, --zc=STR
       This option can be used to override the automatic
       negotiation of the compression algorithm that occurs when
       --compress is used.  The option implies --compress unless
       "none" was specified, which instead implies --no-compress.

       The compression options that you may be able to use are:

       o      zstd

       o      lz4

       o      zlibx

       o      zlib

       o      none

       Run rsync --version to see the default compress list
       compiled into your version (which may differ from the list
       above).

       Note that if you see an error about an option named
       --old-compress or --new-compress, this is rsync trying to
       send the --compress-choice=zlib or --compress-choice=zlibx
       option in a backward-compatible manner that more rsync
       versions understand.  This error indicates that the older
       rsync version on the server will not allow you to force the
       compression type.

       Note that the "zlibx" compression algorithm is just the
       "zlib" algorithm with matched data excluded from the
       compression stream (to try to make it more compatible with
       an external zlib implementation).

--compress-level=NUM, --zl=NUM
       Explicitly set the compression level to use (see
       --compress, -z) instead of letting it default.  The
       --compress option is implied as long as the level chosen is
       not a "don't compress" level for the compression algorithm
       that is in effect (e.g. zlib compression treats level 0 as
       "off").

       The level values vary depending on the checksum in effect.
       Because rsync will negotiate a checksum choice by default
       (when the remote rsync is new enough), it can be good to
       combine this option with a --compress-choice (--zc) option
       unless you're sure of the choice in effect.  For example:

           rsync -aiv --zc=zstd --zl=22 host:src/ dest/

       For zlib & zlibx compression the valid values are from 1 to
       9 with 6 being the default.  Specifying --zl=0 turns
       compression off, and specifying --zl=-1 chooses the default
       level of 6.

       For zstd compression the valid values are from -131072 to
       22 with 3 being the default. Specifying 0 chooses the
       default of 3.

       For lz4 compression there are no levels, so the value is
       always 0.

       If you specify a too-large or too-small value, the number
       is silently limited to a valid value.  This allows you to
       specify something like --zl=999999999 and be assured that
       you'll end up with the maximum compression level no matter
       what algorithm was chosen.

       If you want to know the compression level that is in
       effect, specify --debug=nstr to see the "negotiated string"
       results.  This will report something like
       "Client compress: zstd (level 3)" (along with the checksum
       choice in effect).

--compress-threads=NUM, --zt=NUM
       Set the number of threads to spawn when compressing data.
       Setting this option to 1 or more will instruct the
       compression library to spawn 1 or more threads for
       compression. Ideally, increasing the number of threads will
       increase transfer speed if the transfer is CPU bound on the
       sender.

       This option does not affect decompression.

       Compression algorithms that allow threading:

       o      zstd (only when libzstd is compiled with threading
              support)

       This option is ignored if one of the above alogithms is not
       selected as the --compression-choice or if compression not
       enabled.

--skip-compress=LIST
       NOTE: no compression method currently supports per-file
       compression changes, so this option has no effect.

       Override the list of file suffixes that will be compressed
       as little as possible.  Rsync sets the compression level on
       a per-file basis based on the file's suffix.  If the
       compression algorithm has an "off" level, then no
       compression occurs for those files.  Other algorithms that
       support changing the streaming level on-the-fly will have
       the level minimized to reduces the CPU usage as much as
       possible for a matching file.

       The LIST should be one or more file suffixes (without the
       dot) separated by slashes (/).  You may specify an empty
       string to indicate that no files should be skipped.

       Simple character-class matching is supported: each must
       consist of a list of letters inside the square brackets
       (e.g. no special classes, such as "[:alpha:]", are
       supported, and '-' has no special meaning).

       The characters asterisk (*) and question-mark (?) have no
       special meaning.

       Here's an example that specifies 6 suffixes to skip (since
       1 of the 5 rules matches 2 suffixes):

           --skip-compress=gz/jpg/mp[34]/7z/bz2

       The default file suffixes in the skip-compress list in this
       version of rsync are:

           3g2 3gp 7z aac ace apk avi bz2 deb dmg ear f4v flac flv
           gpg gz iso jar jpeg jpg lrz lz lz4 lzma lzo m1a m1v m2a
           m2ts m2v m4a m4b m4p m4r m4v mka mkv mov mp1 mp2 mp3
           mp4 mpa mpeg mpg mpv mts odb odf odg odi odm odp ods
           odt oga ogg ogm ogv ogx opus otg oth otp ots ott oxt
           png qt rar rpm rz rzip spx squashfs sxc sxd sxg sxm sxw
           sz tbz tbz2 tgz tlz ts txz tzo vob war webm webp xz z
           zip zst

       This list will be replaced by your --skip-compress list in
       all but one situation: a copy from a daemon rsync will add
       your skipped suffixes to its list of non-compressing files
       (and its list may be configured to a different default).

--numeric-ids
       With this option rsync will transfer numeric group and user
       IDs rather than using user and group names and mapping them
       at both ends.

       By default rsync will use the username and groupname to
       determine what ownership to give files.  The special uid 0
       and the special group 0 are never mapped via user/group
       names even if the --numeric-ids option is not specified.

       If a user or group has no name on the source system or it
       has no match on the destination system, then the numeric ID
       from the source system is used instead.  See also the
       use chroot setting in the rsyncd.conf manpage for some
       comments on how the chroot setting affects rsync's ability
       to look up the names of the users and groups and what you
       can do about it.

--usermap=STRING, --groupmap=STRING
       These options allow you to specify users and groups that
       should be mapped to other values by the receiving side.
       The STRING is one or more FROM:TO pairs of values separated
       by commas.  Any matching FROM value from the sender is
       replaced with a TO value from the receiver.  You may
       specify usernames or user IDs for the FROM and TO values,
       and the FROM value may also be a wild-card string, which
       will be matched against the sender's names (wild-cards do
       NOT match against ID numbers, though see below for why a
       '*' matches everything).  You may instead specify a range
       of ID numbers via an inclusive range: LOW-HIGH.  For
       example:

           --usermap=0-99:nobody,wayne:admin,*:normal --groupmap=usr:1,1:usr

       The first match in the list is the one that is used.  You
       should specify all your user mappings using a single
       --usermap option, and/or all your group mappings using a
       single --groupmap option.

       Note that the sender's name for the 0 user and group are
       not transmitted to the receiver, so you should either match
       these values using a 0, or use the names in effect on the
       receiving side (typically "root").  All other FROM names
       match those in use on the sending side.  All TO names match
       those in use on the receiving side.

       Any IDs that do not have a name on the sending side are
       treated as having an empty name for the purpose of
       matching.  This allows them to be matched via a "*" or
       using an empty name.  For instance:

           --usermap=:nobody --groupmap=*:nobody

       When the --numeric-ids option is used, the sender does not
       send any names, so all the IDs are treated as having an
       empty name.  This means that you will need to specify
       numeric FROM values if you want to map these nameless IDs
       to different values.

       For the --usermap option to work, the receiver will need to
       be running as a super-user (see also the --super and
       --fake-super options).  For the --groupmap option to work,
       the receiver will need to have permissions to set that
       group.

       Starting with rsync 3.2.4, the --usermap option implies the
       --owner (-o) option while the --groupmap option implies the
       --group (-g) option (since rsync needs to have those
       options enabled for the mapping options to work).

       An older rsync client may need to use -s to avoid a
       complaint about wildcard characters, but a modern rsync
       handles this automatically.

--chown=USER:GROUP
       This option forces all files to be owned by USER with group
       GROUP.  This is a simpler interface than using --usermap &
       --groupmap directly, but it is implemented using those
       options internally so they cannot be mixed.  If either the
       USER or GROUP is empty, no mapping for the omitted
       user/group will occur.  If GROUP is empty, the trailing
       colon may be omitted, but if USER is empty, a leading colon
       must be supplied.

       If you specify "--chown=foo:bar", this is exactly the same
       as specifying "--usermap=*:foo --groupmap=*:bar", only
       easier (and with the same implied --owner and/or --group
       options).

       An older rsync client may need to use -s to avoid a
       complaint about wildcard characters, but a modern rsync
       handles this automatically.

--timeout=SECONDS
       This option allows you to set a maximum I/O timeout in
       seconds.  If no data is transferred for the specified time
       then rsync will exit.  The default is 0, which means no
       timeout.

--contimeout=SECONDS
       This option allows you to set the amount of time that rsync
       will wait for its connection to an rsync daemon to succeed.
       If the timeout is reached, rsync exits with an error.

--address=ADDRESS
       By default rsync will bind to the wildcard address when
       connecting to an rsync daemon.  The --address option allows
       you to specify a specific IP address (or hostname) to bind
       to.

       See also the daemon version of the --address option.

--port=PORT
       This specifies an alternate TCP port number to use rather
       than the default of 873.  This is only needed if you are
       using the double-colon (::) syntax to connect with an rsync
       daemon (since the URL syntax has a way to specify the port
       as a part of the URL).

       See also the daemon version of the --port option.
