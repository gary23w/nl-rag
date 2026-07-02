---
title: "rsync(1) (part 5/5)"
source: https://man7.org/linux/man-pages/man1/rsync.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 5/5
---

## FILTER RULES

The filter rules allow for custom control of several aspects of
how files are handled:

o      Control which files the sending side puts into the file
       list that describes the transfer hierarchy

o      Control which files the receiving side protects from
       deletion when the file is not in the sender's file list

o      Control which extended attribute names are skipped when
       copying xattrs

The rules are either directly specified via option arguments or
they can be read in from one or more files.  The filter-rule files
can even be a part of the hierarchy of files being copied,
affecting different parts of the tree in different ways.

### SIMPLE INCLUDE/EXCLUDE RULES

We will first cover the basics of how include & exclude rules
affect what files are transferred, ignoring any deletion side-
effects.  Filter rules mainly affect the contents of directories
that rsync is "recursing" into, but they can also affect a top-
level item in the transfer that was specified as a argument.

The default for any unmatched file/dir is for it to be included in
the transfer, which puts the file/dir into the sender's file list.
The use of an exclude rule causes one or more matching files/dirs
to be left out of the sender's file list.  An include rule can be
used to limit the effect of an exclude rule that is matching too
many files.

The order of the rules is important because the first rule that
matches is the one that takes effect.  Thus, if an early rule
excludes a file, no include rule that comes after it can have any
effect. This means that you must place any include overrides
somewhere prior to the exclude that it is intended to limit.

When a directory is excluded, all its contents and sub-contents
are also excluded.  The sender doesn't scan through any of it at
all, which can save a lot of time when skipping large unneeded
sub-trees.

It is also important to understand that the include/exclude rules
are applied to every file and directory that the sender is
recursing into. Thus, if you want a particular deep file to be
included, you have to make sure that none of the directories that
must be traversed on the way down to that file are excluded or
else the file will never be discovered to be included. As an
example, if the directory "a/path" was given as a transfer
argument and you want to ensure that the file
"a/path/down/deep/wanted.txt" is a part of the transfer, then the
sender must not exclude the directories "a/path", "a/path/down",
or "a/path/down/deep" as it makes it way scanning through the file
tree.

When you are working on the rules, it can be helpful to ask rsync
to tell you what is being excluded/included and why.  Specifying
--debug=FILTER or (when pulling files) -M--debug=FILTER turns on
level 1 of the FILTER debug information that will output a message
any time that a file or directory is included or excluded and
which rule it matched.  Beginning in 3.2.4 it will also warn if a
filter rule has trailing whitespace, since an exclude of "foo "
(with a trailing space) will not exclude a file named "foo".

Exclude and include rules can specify wildcard PATTERN MATCHING
RULES (similar to shell wildcards) that allow you to match things
like a file suffix or a portion of a filename.

A rule can be limited to only affecting a directory by putting a
trailing slash onto the filename.

### SIMPLE INCLUDE/EXCLUDE EXAMPLE

With the following file tree created on the sending side:

    mkdir x/
    touch x/file.txt
    mkdir x/y/
    touch x/y/file.txt
    touch x/y/zzz.txt
    mkdir x/z/
    touch x/z/file.txt

Then the following rsync command will transfer the file
"x/y/file.txt" and the directories needed to hold it, resulting in
the path "/tmp/x/y/file.txt" existing on the remote host:

    rsync -ai -f'+ x/' -f'+ x/y/' -f'+ x/y/file.txt' -f'- *' x host:/tmp/

Aside: this copy could also have been accomplished using the -R
option (though the 2 commands behave differently if deletions are
enabled):

    rsync -aiR x/y/file.txt host:/tmp/

The following command does not need an include of the "x"
directory because it is not a part of the transfer (note the
trailing slash).  Running this command would copy just
"/tmp/x/file.txt" because the "y" and "z" dirs get excluded:

    rsync -ai -f'+ file.txt' -f'- *' x/ host:/tmp/x/

This command would omit the zzz.txt file while copying "x" and
everything else it contains:

    rsync -ai -f'- zzz.txt' x host:/tmp/

### FILTER RULES WHEN DELETING

By default the include & exclude filter rules affect both the
sender (as it creates its file list) and the receiver (as it
creates its file lists for calculating deletions).  If no delete
option is in effect, the receiver skips creating the delete-
related file lists.  This two-sided default can be manually
overridden so that you are only specifying sender rules or
receiver rules, as described in the FILTER RULES IN DEPTH section.

When deleting, an exclude protects a file from being removed on
the receiving side while an include overrides that protection
(putting the file at risk of deletion). The default is for a file
to be at risk -- its safety depends on it matching a corresponding
file from the sender.

An example of the two-sided exclude effect can be illustrated by
the copying of a C development directory between 2 systems.  When
doing a touch-up copy, you might want to skip copying the built
executable and the .o files (sender hide) so that the receiving
side can build their own and not lose any object files that are
already correct (receiver protect).  For instance:

    rsync -ai --del -f'- *.o' -f'- cmd' src host:/dest/

Note that using -f'-p *.o' is even better than -f'- *.o' if there
is a chance that the directory structure may have changed.  The
"p" modifier is discussed in FILTER RULE MODIFIERS.

One final note, if your shell doesn't mind unexpanded wildcards,
you could simplify the typing of the filter options by using an
underscore in place of the space and leaving off the quotes.  For
instance, -f -_*.o -f -_cmd (and similar) could be used instead of
the filter options above.

### FILTER RULES IN DEPTH

Rsync supports old-style include/exclude rules and new-style
filter rules.  The older rules are specified using --include and
--exclude as well as the --include-from and --exclude-from. These
are limited in behavior but they don't require a "-" or "+"
prefix.  An old-style exclude rule is turned into a "- name"
filter rule (with no modifiers) and an old-style include rule is
turned into a "+ name" filter rule (with no modifiers).

Rsync builds an ordered list of filter rules as specified on the
command-line and/or read-in from files.  New style filter rules
have the following syntax:

    RULE [PATTERN_OR_FILENAME]
    RULE,MODIFIERS [PATTERN_OR_FILENAME]

You have your choice of using either short or long RULE names, as
described below.  If you use a short-named rule, the ','
separating the RULE from the MODIFIERS is optional.  The PATTERN
or FILENAME that follows (when present) must come after either a
single space or an underscore (_). Any additional spaces and/or
underscores are considered to be a part of the pattern name.  Here
are the available rule prefixes:

exclude, '-'
       specifies an exclude pattern that (by default) is both a
       hide and a protect.

include, '+'
       specifies an include pattern that (by default) is both a
       show and a risk.

merge, '.'
       specifies a merge-file on the client side to read for more
       rules.

dir-merge, ':'
       specifies a per-directory merge-file.  Using this kind of
       filter rule requires that you trust the sending side's
       filter checking, so it has the side-effect mentioned under
       the --trust-sender option.

hide, 'H'
       specifies a pattern for hiding files from the transfer.
       Equivalent to a sender-only exclude, so -f'H foo' could
       also be specified as -f'-s foo'.

show, 'S'
       files that match the pattern are not hidden. Equivalent to
       a sender-only include, so -f'S foo' could also be specified
       as -f'+s foo'.

protect, 'P'
       specifies a pattern for protecting files from deletion.
       Equivalent to a receiver-only exclude, so -f'P foo' could
       also be specified as -f'-r foo'.

risk, 'R'
       files that match the pattern are not protected. Equivalent
       to a receiver-only include, so -f'R foo' could also be
       specified as -f'+r foo'.

clear, '!'
       clears the current include/exclude list (takes no arg)

When rules are being read from a file (using merge or dir-merge),
empty lines are ignored, as are whole-line comments that start
with a '#' (filename rules that contain a hash character are
unaffected).

Note also that the --filter, --include, and --exclude options take
one rule/pattern each.  To add multiple ones, you can repeat the
options on the command-line, use the merge-file syntax of the
--filter option, or the --include-from / --exclude-from options.

### PATTERN MATCHING RULES

Most of the rules mentioned above take an argument that specifies
what the rule should match.  If rsync is recursing through a
directory hierarchy, keep in mind that each pattern is matched
against the name of every directory in the descent path as rsync
finds the filenames to send.

The matching rules for the pattern argument take several forms:

o      If a pattern contains a / (not counting a trailing slash)
       or a "**" (which can match a slash), then the pattern is
       matched against the full pathname, including any leading
       directories within the transfer.  If the pattern doesn't
       contain a (non-trailing) / or a "**", then it is matched
       only against the final component of the filename or
       pathname. For example, foo means that the final path
       component must be "foo" while foo/bar would match the last
       2 elements of the path (as long as both elements are within
       the transfer).

o      A pattern that ends with a / only matches a directory, not
       a regular file, symlink, or device.

o      A pattern that starts with a / is anchored to the start of
       the transfer path instead of the end.  For example, /foo/**
       or /foo/bar/** match only leading elements in the path.  If
       the rule is read from a per-directory filter file, the
       transfer path being matched will begin at the level of the
       filter file instead of the top of the transfer.  See the
       section on ANCHORING INCLUDE/EXCLUDE PATTERNS for a full
       discussion of how to specify a pattern that matches at the
       root of the transfer.

Rsync chooses between doing a simple string match and wildcard
matching by checking if the pattern contains one of these three
wildcard characters: '*', '?', and '[' :

o      a '?' matches any single character except a slash (/).

o      a '*' matches zero or more non-slash characters.

o      a '**' matches zero or more characters, including slashes.

o      a '[' introduces a character class, such as [a-z] or
       [[:alpha:]], that must match one character.

o      a trailing *** in the pattern is a shorthand that allows
       you to match a directory and all its contents using a
       single rule.  For example, specifying "dir_name/***" will
       match both the "dir_name" directory (as if "dir_name/" had
       been specified) and everything in the directory (as if
       "dir_name/**" had been specified).

o      a backslash can be used to escape a wildcard character, but
       it is only interpreted as an escape character if at least
       one wildcard character is present in the match pattern. For
       instance, the pattern "foo\bar" matches that single
       backslash literally, while the pattern "foo\bar*" would
       need to be changed to "foo\\bar*" to avoid the "\b"
       becoming just "b".

Here are some examples of exclude/include matching:

o      Option -f'- *.o' would exclude all filenames ending with .o

o      Option -f'- /foo' would exclude a file (or directory) named
       foo in the transfer-root directory

o      Option -f'- foo/' would exclude any directory named foo

o      Option -f'- foo/*/bar' would exclude any file/dir named bar
       which is at two levels below a directory named foo (if foo
       is in the transfer)

o      Option -f'- /foo/**/bar' would exclude any file/dir named
       bar that was two or more levels below a top-level directory
       named foo (note that /foo/bar is not excluded by this)

o      Options -f'+ */' -f'+ *.c' -f'- *' would include all
       directories and .c source files but nothing else

o      Options -f'+ foo/' -f'+ foo/bar.c' -f'- *' would include
       only the foo directory and foo/bar.c (the foo directory
       must be explicitly included or it would be excluded by the
       "- *")

### FILTER RULE MODIFIERS

The following modifiers are accepted after an include (+) or
exclude (-) rule:

o      A / specifies that the include/exclude rule should be
       matched against the absolute pathname of the current item.
       For example, -f'-/ /etc/passwd' would exclude the passwd
       file any time the transfer was sending files from the
       "/etc" directory, and "-/ subdir/foo" would always exclude
       "foo" when it is in a dir named "subdir", even if "foo" is
       at the root of the current transfer.

o      A ! specifies that the include/exclude should take effect
       if the pattern fails to match.  For instance, -f'-! */'
       would exclude all non-directories.

o      A C is used to indicate that all the global CVS-exclude
       rules should be inserted as excludes in place of the "-C".
       No arg should follow.

o      An s is used to indicate that the rule applies to the
       sending side.  When a rule affects the sending side, it
       affects what files are put into the sender's file list.
       The default is for a rule to affect both sides unless
       --delete-excluded was specified, in which case default
       rules become sender-side only.  See also the hide (H) and
       show (S) rules, which are an alternate way to specify
       sending-side includes/excludes.

o      An r is used to indicate that the rule applies to the
       receiving side.  When a rule affects the receiving side, it
       prevents files from being deleted.  See the s modifier for
       more info.  See also the protect (P) and risk (R) rules,
       which are an alternate way to specify receiver-side
       includes/excludes.

o      A p indicates that a rule is perishable, meaning that it is
       ignored in directories that are being deleted.  For
       instance, the --cvs-exclude (-C) option's default rules
       that exclude things like "CVS" and "*.o" are marked as
       perishable, and will not prevent a directory that was
       removed on the source from being deleted on the
       destination.

o      An x indicates that a rule affects xattr names in xattr
       copy/delete operations (and is thus ignored when matching
       file/dir names).  If no xattr-matching rules are specified,
       a default xattr filtering rule is used (see the --xattrs
       option).

### MERGE-FILE FILTER RULES

You can merge whole files into your filter rules by specifying
either a merge (.) or a dir-merge (:) filter rule (as introduced
in the FILTER RULES section above).

There are two kinds of merged files -- single-instance ('.') and
per-directory (':').  A single-instance merge file is read one
time, and its rules are incorporated into the filter list in the
place of the "." rule.  For per-directory merge files, rsync will
scan every directory that it traverses for the named file, merging
its contents when the file exists into the current list of
inherited rules.  These per-directory rule files must be created
on the sending side because it is the sending side that is being
scanned for the available files to transfer.  These rule files may
also need to be transferred to the receiving side if you want them
to affect what files don't get deleted (see PER-DIRECTORY RULES
AND DELETE below).

Some examples:

    merge /etc/rsync/default.rules
    . /etc/rsync/default.rules
    dir-merge .per-dir-filter
    dir-merge,n- .non-inherited-per-dir-excludes
    :n- .non-inherited-per-dir-excludes

The following modifiers are accepted after a merge or dir-merge
rule:

o      A - specifies that the file should consist of only exclude
       patterns, with no other rule-parsing except for in-file
       comments.

o      A + specifies that the file should consist of only include
       patterns, with no other rule-parsing except for in-file
       comments.

o      A C is a way to specify that the file should be read in a
       CVS-compatible manner.  This turns on 'n', 'w', and '-',
       but also allows the list-clearing token (!) to be
       specified.  If no filename is provided, ".cvsignore" is
       assumed.

o      A e will exclude the merge-file name from the transfer;
       e.g.  "dir-merge,e .rules" is like "dir-merge .rules" and
       "- .rules".

o      An n specifies that the rules are not inherited by
       subdirectories.

o      A w specifies that the rules are word-split on whitespace
       instead of the normal line-splitting.  This also turns off
       comments.  Note: the space that separates the prefix from
       the rule is treated specially, so "- foo + bar" is parsed
       as two rules (assuming that prefix-parsing wasn't also
       disabled).

o      You may also specify any of the modifiers for the "+" or
       "-" rules (above) in order to have the rules that are read
       in from the file default to having that modifier set
       (except for the ! modifier, which would not be useful).
       For instance, "merge,-/ .excl" would treat the contents of
       .excl as absolute-path excludes, while "dir-merge,s .filt"
       and ":sC" would each make all their per-directory rules
       apply only on the sending side.  If the merge rule
       specifies sides to affect (via the s or r modifier or
       both), then the rules in the file must not specify sides
       (via a modifier or a rule prefix such as hide).

Per-directory rules are inherited in all subdirectories of the
directory where the merge-file was found unless the 'n' modifier
was used.  Each subdirectory's rules are prefixed to the inherited
per-directory rules from its parents, which gives the newest rules
a higher priority than the inherited rules.  The entire set of
dir-merge rules are grouped together in the spot where the merge-
file was specified, so it is possible to override dir-merge rules
via a rule that got specified earlier in the list of global rules.
When the list-clearing rule ("!") is read from a per-directory
file, it only clears the inherited rules for the current merge
file.

Another way to prevent a single rule from a dir-merge file from
being inherited is to anchor it with a leading slash.  Anchored
rules in a per-directory merge-file are relative to the merge-
file's directory, so a pattern "/foo" would only match the file
"foo" in the directory where the dir-merge filter file was found.

Here's an example filter file which you'd specify via
--filter=". file":

    merge /home/user/.global-filter
    - *.gz
    dir-merge .rules
    + *.[ch]
    - *.o
    - foo*

This will merge the contents of the /home/user/.global-filter file
at the start of the list and also turns the ".rules" filename into
a per-directory filter file.  All rules read in prior to the start
of the directory scan follow the global anchoring rules (i.e. a
leading slash matches at the root of the transfer).

If a per-directory merge-file is specified with a path that is a
parent directory of the first transfer directory, rsync will scan
all the parent dirs from that starting point to the transfer
directory for the indicated per-directory file.  For instance,
here is a common filter (see -F):

    --filter=': /.rsync-filter'

That rule tells rsync to scan for the file .rsync-filter in all
directories from the root down through the parent directory of the
transfer prior to the start of the normal directory scan of the
file in the directories that are sent as a part of the transfer.
(Note: for an rsync daemon, the root is always the same as the
module's "path".)

Some examples of this pre-scanning for per-directory files:

    rsync -avF /src/path/ /dest/dir
    rsync -av --filter=': ../../.rsync-filter' /src/path/ /dest/dir
    rsync -av --filter=': .rsync-filter' /src/path/ /dest/dir

The first two commands above will look for ".rsync-filter" in "/"
and "/src" before the normal scan begins looking for the file in
"/src/path" and its subdirectories.  The last command avoids the
parent-dir scan and only looks for the ".rsync-filter" files in
each directory that is a part of the transfer.

If you want to include the contents of a ".cvsignore" in your
patterns, you should use the rule ":C", which creates a dir-merge
of the .cvsignore file, but parsed in a CVS-compatible manner.
You can use this to affect where the --cvs-exclude (-C) option's
inclusion of the per-directory .cvsignore file gets placed into
your rules by putting the ":C" wherever you like in your filter
rules.  Without this, rsync would add the dir-merge rule for the
.cvsignore file at the end of all your other rules (giving it a
lower priority than your command-line rules).  For example:

    cat <<EOT | rsync -avC --filter='. -' a/ b
    + foo.o
    :C
    - *.old
    EOT
    rsync -avC --include=foo.o -f :C --exclude='*.old' a/ b

Both of the above rsync commands are identical.  Each one will
merge all the per-directory .cvsignore rules in the middle of the
list rather than at the end.  This allows their dir-specific rules
to supersede the rules that follow the :C instead of being
subservient to all your rules.  To affect the other CVS exclude
rules (i.e. the default list of exclusions, the contents of
$HOME/.cvsignore, and the value of $CVSIGNORE) you should omit the
-C command-line option and instead insert a "-C" rule into your
filter rules; e.g.  "--filter=-C".

### LIST-CLEARING FILTER RULE

You can clear the current include/exclude list by using the "!"
filter rule (as introduced in the FILTER RULES section above).
The "current" list is either the global list of rules (if the rule
is encountered while parsing the filter options) or a set of per-
directory rules (which are inherited in their own sub-list, so a
subdirectory can use this to clear out the parent's rules).

### ANCHORING INCLUDE/EXCLUDE PATTERNS

As mentioned earlier, global include/exclude patterns are anchored
at the "root of the transfer" (as opposed to per-directory
patterns, which are anchored at the merge-file's directory).  If
you think of the transfer as a subtree of names that are being
sent from sender to receiver, the transfer-root is where the tree
starts to be duplicated in the destination directory.  This root
governs where patterns that start with a / match.

Because the matching is relative to the transfer-root, changing
the trailing slash on a source path or changing your use of the
--relative option affects the path you need to use in your
matching (in addition to changing how much of the file tree is
duplicated on the destination host).  The following examples
demonstrate this.

Let's say that we want to match two source files, one with an
absolute path of "/home/me/foo/bar", and one with a path of
"/home/you/bar/baz".  Here is how the various command choices
differ for a 2-source transfer:

    Example cmd: rsync -a /home/me /home/you /dest
    +/- pattern: /me/foo/bar
    +/- pattern: /you/bar/baz
    Target file: /dest/me/foo/bar
    Target file: /dest/you/bar/baz

    Example cmd: rsync -a /home/me/ /home/you/ /dest
    +/- pattern: /foo/bar               (note missing "me")
    +/- pattern: /bar/baz               (note missing "you")
    Target file: /dest/foo/bar
    Target file: /dest/bar/baz

    Example cmd: rsync -a --relative /home/me/ /home/you /dest
    +/- pattern: /home/me/foo/bar       (note full path)
    +/- pattern: /home/you/bar/baz      (ditto)
    Target file: /dest/home/me/foo/bar
    Target file: /dest/home/you/bar/baz

    Example cmd: cd /home; rsync -a --relative me/foo you/ /dest
    +/- pattern: /me/foo/bar      (starts at specified path)
    +/- pattern: /you/bar/baz     (ditto)
    Target file: /dest/me/foo/bar
    Target file: /dest/you/bar/baz

The easiest way to see what name you should filter is to just look
at the output when using --verbose and put a / in front of the
name (use the --dry-run option if you're not yet ready to copy any
files).

### PER-DIRECTORY RULES AND DELETE

Without a delete option, per-directory rules are only relevant on
the sending side, so you can feel free to exclude the merge files
themselves without affecting the transfer.  To make this easy, the
'e' modifier adds this exclude for you, as seen in these two
equivalent commands:

    rsync -av --filter=': .excl' --exclude=.excl host:src/dir /dest
    rsync -av --filter=':e .excl' host:src/dir /dest

However, if you want to do a delete on the receiving side AND you
want some files to be excluded from being deleted, you'll need to
be sure that the receiving side knows what files to exclude.  The
easiest way is to include the per-directory merge files in the
transfer and use --delete-after, because this ensures that the
receiving side gets all the same exclude rules as the sending side
before it tries to delete anything:

    rsync -avF --delete-after host:src/dir /dest

However, if the merge files are not a part of the transfer, you'll
need to either specify some global exclude rules (i.e. specified
on the command line), or you'll need to maintain your own per-
directory merge files on the receiving side.  An example of the
first is this (assume that the remote .rules files exclude
themselves):

    rsync -av --filter=': .rules' --filter='. /my/extra.rules'
       --delete host:src/dir /dest

In the above example the extra.rules file can affect both sides of
the transfer, but (on the sending side) the rules are subservient
to the rules merged from the .rules files because they were
specified after the per-directory merge rule.

In one final example, the remote side is excluding the .rsync-
filter files from the transfer, but we want to use our own .rsync-
filter files to control what gets deleted on the receiving side.
To do this we must specifically exclude the per-directory merge
files (so that they don't get deleted) and then put rules into the
local files to control what else should not get deleted.  Like one
of these commands:

    rsync -av --filter=':e /.rsync-filter' --delete \
        host:src/dir /dest
    rsync -avFF --delete host:src/dir /dest


## TRANSFER RULES

In addition to the FILTER RULES that affect the recursive file
scans that generate the file list on the sending and (when
deleting) receiving sides, there are transfer rules. These rules
affect which files the generator decides need to be transferred
without the side effects of an exclude filter rule.  Transfer
rules affect only files and never directories.

Because a transfer rule does not affect what goes into the
sender's (and receiver's) file list, it cannot have any effect on
which files get deleted on the receiving side.  For example, if
the file "foo" is present in the sender's list but its size is
such that it is omitted due to a transfer rule, the receiving side
does not request the file.  However, its presence in the file list
means that a delete pass will not remove a matching file named
"foo" on the receiving side.  On the other hand, a server-side
exclude (hide) of the file "foo" leaves the file out of the
server's file list, and absent a receiver-side exclude (protect)
the receiver will remove a matching file named "foo" if deletions
are requested.

Given that the files are still in the sender's file list, the
--prune-empty-dirs option will not judge a directory as being
empty even if it contains only files that the transfer rules
omitted.

Similarly, a transfer rule does not have any extra effect on which
files are deleted on the receiving side, so setting a maximum file
size for the transfer does not prevent big files from being
deleted.

Examples of transfer rules include the default "quick check"
algorithm (which compares size & modify time), the --update
option, the --max-size option, the --ignore-non-existing option,
and a few others.


## BATCH MODE

Batch mode can be used to apply the same set of updates to many
identical systems.  Suppose one has a tree which is replicated on
a number of hosts.  Now suppose some changes have been made to
this source tree and those changes need to be propagated to the
other hosts.  In order to do this using batch mode, rsync is run
with the write-batch option to apply the changes made to the
source tree to one of the destination trees.  The write-batch
option causes the rsync client to store in a "batch file" all the
information needed to repeat this operation against other,
identical destination trees.

Generating the batch file once saves having to perform the file
status, checksum, and data block generation more than once when
updating multiple destination trees.  Multicast transport
protocols can be used to transfer the batch update files in
parallel to many hosts at once, instead of sending the same data
to every host individually.

To apply the recorded changes to another destination tree, run
rsync with the read-batch option, specifying the name of the same
batch file, and the destination tree.  Rsync updates the
destination tree using the information stored in the batch file.

For your convenience, a script file is also created when the
write-batch option is used: it will be named the same as the batch
file with ".sh" appended.  This script file contains a command-
line suitable for updating a destination tree using the associated
batch file.  It can be executed using a Bourne (or Bourne-like)
shell, optionally passing in an alternate destination tree
pathname which is then used instead of the original destination
path.  This is useful when the destination tree path on the
current host differs from the one used to create the batch file.

Examples:

    $ rsync --write-batch=foo -a host:/source/dir/ /adest/dir/
    $ scp foo* remote:
    $ ssh remote ./foo.sh /bdest/dir/

    $ rsync --write-batch=foo -a /source/dir/ /adest/dir/
    $ ssh remote rsync --read-batch=- -a /bdest/dir/ <foo

In these examples, rsync is used to update /adest/dir/ from
/source/dir/ and the information to repeat this operation is
stored in "foo" and "foo.sh".  The host "remote" is then updated
with the batched data going into the directory /bdest/dir.  The
differences between the two examples reveals some of the
flexibility you have in how you deal with batches:

o      The first example shows that the initial copy doesn't have
       to be local -- you can push or pull data to/from a remote
       host using either the remote-shell syntax or rsync daemon
       syntax, as desired.

o      The first example uses the created "foo.sh" file to get the
       right rsync options when running the read-batch command on
       the remote host.

o      The second example reads the batch data via standard input
       so that the batch file doesn't need to be copied to the
       remote machine first.  This example avoids the foo.sh
       script because it needed to use a modified --read-batch
       option, but you could edit the script file if you wished to
       make use of it (just be sure that no other option is trying
       to use standard input, such as the --exclude-from=-
       option).

Caveats:

The read-batch option expects the destination tree that it is
updating to be identical to the destination tree that was used to
create the batch update fileset.  When a difference between the
destination trees is encountered the update might be discarded
with a warning (if the file appears to be up-to-date already) or
the file-update may be attempted and then, if the file fails to
verify, the update discarded with an error.  This means that it
should be safe to re-run a read-batch operation if the command got
interrupted.  If you wish to force the batched-update to always be
attempted regardless of the file's size and date, use the -I
option (when reading the batch).  If an error occurs, the
destination tree will probably be in a partially updated state.
In that case, rsync can be used in its regular (non-batch) mode of
operation to fix up the destination tree.

The rsync version used on all destinations must be at least as new
as the one used to generate the batch file.  Rsync will die with
an error if the protocol version in the batch file is too new for
the batch-reading rsync to handle.  See also the --protocol option
for a way to have the creating rsync generate a batch file that an
older rsync can understand.  (Note that batch files changed format
in version 2.6.3, so mixing versions older than that with newer
versions will not work.)

When reading a batch file, rsync will force the value of certain
options to match the data in the batch file if you didn't set them
to the same as the batch-writing command.  Other options can (and
should) be changed.  For instance --write-batch changes to
--read-batch, --files-from is dropped, and the --filter /
--include / --exclude options are not needed unless one of the
--delete options is specified.

The code that creates the BATCH.sh file transforms any
filter/include/exclude options into a single list that is appended
as a "here" document to the shell script file.  An advanced user
can use this to modify the exclude list if a change in what gets
deleted by --delete is desired.  A normal user can ignore this
detail and just use the shell script as an easy way to run the
appropriate --read-batch command for the batched data.

The original batch mode in rsync was based on "rsync+", but the
latest version uses a new implementation.


## SYMBOLIC LINKS

Three basic behaviors are possible when rsync encounters a
symbolic link in the source directory.

By default, symbolic links are not transferred at all.  A message
"skipping non-regular" file is emitted for any symlinks that
exist.

If --links is specified, then symlinks are added to the transfer
(instead of being noisily ignored), and the default handling is to
recreate them with the same target on the destination.  Note that
--archive implies --links.

If --copy-links is specified, then symlinks are "collapsed" by
copying their referent, rather than the symlink.

Rsync can also distinguish "safe" and "unsafe" symbolic links.  An
example where this might be used is a web site mirror that wishes
to ensure that the rsync module that is copied does not include
symbolic links to /etc/passwd in the public section of the site.
Using --copy-unsafe-links will cause any links to be copied as the
file they point to on the destination.  Using --safe-links will
cause unsafe links to be omitted by the receiver.  (Note that you
must specify or imply --links for --safe-links to have any
effect.)

Symbolic links are considered unsafe if they are absolute symlinks
(start with /), empty, or if they contain enough ".." components
to ascend from the top of the transfer.

Here's a summary of how the symlink options are interpreted.  The
list is in order of precedence, so if your combination of options
isn't mentioned, use the first line that is a complete subset of
your options:

--copy-links
       Turn all symlinks into normal files and directories
       (leaving no symlinks in the transfer for any other options
       to affect).

--copy-dirlinks
       Turn just symlinks to directories into real directories,
       leaving all other symlinks to be handled as described
       below.

--links --copy-unsafe-links
       Turn all unsafe symlinks into files and create all safe
       symlinks.

--copy-unsafe-links
       Turn all unsafe symlinks into files, noisily skip all safe
       symlinks.

--links --safe-links
       The receiver skips creating unsafe symlinks found in the
       transfer and creates the safe ones.

--links
       Create all symlinks.

For the effect of --munge-links, see the discussion in that
option's section.

Note that the --keep-dirlinks option does not effect symlinks in
the transfer but instead affects how rsync treats a symlink to a
directory that already exists on the receiving side.  See that
option's section for a warning.


## DIAGNOSTICS

Rsync occasionally produces error messages that may seem a little
cryptic.  The one that seems to cause the most confusion is
"protocol version mismatch -- is your shell clean?".

This message is usually caused by your startup scripts or remote
shell facility producing unwanted garbage on the stream that rsync
is using for its transport.  The way to diagnose this problem is
to run your remote shell like this:

    ssh remotehost /bin/true > out.dat

then look at out.dat.  If everything is working correctly then
out.dat should be a zero length file.  If you are getting the
above error from rsync then you will probably find that out.dat
contains some text or data.  Look at the contents and try to work
out what is producing it.  The most common cause is incorrectly
configured shell startup scripts (such as .cshrc or .profile) that
contain output statements for non-interactive logins.

If you are having trouble debugging filter patterns, then try
specifying the -vv option.  At this level of verbosity rsync will
show why each individual file is included or excluded.


## EXIT VALUES

o      0 - Success

o      1 - Syntax or usage error

o      2 - Protocol incompatibility

o      3 - Errors selecting input/output files, dirs

o

       o      4 - Requested action not supported. Either:

              an attempt was made to manipulate 64-bit files on a
              platform that cannot support them

       o      an option was specified that is supported by the
              client and not by the server

o      5 - Error starting client-server protocol

o      6 - Daemon unable to append to log-file

o      10 - Error in socket I/O

o      11 - Error in file I/O

o      12 - Error in rsync protocol data stream

o      13 - Errors with program diagnostics

o      14 - Error in IPC code

o      20 - Received SIGUSR1 or SIGINT

o      21 - Some error returned by waitpid()

o      22 - Error allocating core memory buffers

o      23 - Partial transfer due to error

o      24 - Partial transfer due to vanished source files

o      25 - The --max-delete limit stopped deletions

o      30 - Timeout in data send/receive

o      35 - Timeout waiting for daemon connection


## ENVIRONMENT VARIABLES

CVSIGNORE
       The CVSIGNORE environment variable supplements any ignore
       patterns in .cvsignore files.  See the --cvs-exclude option
       for more details.

RSYNC_ICONV
       Specify a default --iconv setting using this environment
       variable. First supported in 3.0.0.

RSYNC_OLD_ARGS
       Specify a "1" if you want the --old-args option to be
       enabled by default, a "2" (or more) if you want it to be
       enabled in the repeated-option state, or a "0" to make sure
       that it is disabled by default. When this environment
       variable is set to a non-zero value, it supersedes the
       RSYNC_PROTECT_ARGS variable.

       This variable is ignored if --old-args, --no-old-args, or
       --secluded-args is specified on the command line.

       First supported in 3.2.4.

RSYNC_PROTECT_ARGS
       Specify a non-zero numeric value if you want the
       --secluded-args option to be enabled by default, or a zero
       value to make sure that it is disabled by default.

       This variable is ignored if --secluded-args,
       --no-secluded-args, or --old-args is specified on the
       command line.

       First supported in 3.1.0.  Starting in 3.2.4, this variable
       is ignored if RSYNC_OLD_ARGS is set to a non-zero value.

RSYNC_RSH
       This environment variable allows you to override the
       default shell used as the transport for rsync.  Command
       line options are permitted after the command name, just as
       in the --rsh (-e) option.

RSYNC_PROXY
       This environment variable allows you to redirect your rsync
       client to use a web proxy when connecting to an rsync
       daemon.  You should set RSYNC_PROXY to a hostname:port
       pair.

RSYNC_PASSWORD
       This environment variable allows you to set the password
       for an rsync daemon connection, which avoids the password
       prompt.  Note that this does not supply a password to a
       remote shell transport such as ssh (consult its
       documentation for how to do that).

USER or LOGNAME
       The USER or LOGNAME environment variables are used to
       determine the default username sent to an rsync daemon.  If
       neither is set, the username defaults to "nobody".  If both
       are set, USER takes precedence.

RSYNC_PARTIAL_DIR
       This environment variable specifies the directory to use
       for a --partial transfer without implying that partial
       transfers be enabled.  See the --partial-dir option for
       full details.

RSYNC_COMPRESS_LIST
       This environment variable allows you to customize the
       negotiation of the compression algorithm by specifying an
       alternate order or a reduced list of names.  Use the
       command rsync --version to see the available compression
       names.  See the --compress option for full details.

RSYNC_CHECKSUM_LIST
       This environment variable allows you to customize the
       negotiation of the checksum algorithm by specifying an
       alternate order or a reduced list of names.  Use the
       command rsync --version to see the available checksum
       names.  See the --checksum-choice option for full details.

RSYNC_MAX_ALLOC
       This environment variable sets an allocation maximum as if
       you had used the --max-alloc option.

RSYNC_PORT
       This environment variable is not read by rsync, but is
       instead set in its sub-environment when rsync is running
       the remote shell in combination with a daemon connection.
       This allows a script such as rsync-ssl to be able to know
       the port number that the user specified on the command
       line.

HOME   This environment variable is used to find the user's
       default .cvsignore file.

RSYNC_CONNECT_PROG
       This environment variable is mainly used in debug setups to
       set the program to use when making a daemon connection.
       See CONNECTING TO AN RSYNC DAEMON for full details.

RSYNC_SHELL
       This environment variable is mainly used in debug setups to
       set the program to use to run the program specified by
       RSYNC_CONNECT_PROG.  See CONNECTING TO AN RSYNC DAEMON for
       full details.


## FILES

/etc/rsyncd.conf or rsyncd.conf


## SEE ALSO

rsync-ssl(1), rsyncd.conf(5), rrsync(1)


## BUGS

o      Times are transferred as *nix time_t values.

o      When transferring to FAT filesystems rsync may re-sync
       unmodified files.  See the comments on the --modify-window
       option.

o      File permissions, devices, etc. are transferred as native
       numerical values.

o      See also the comments on the --delete option.

Please report bugs! See the web site at 
⟨https://rsync.samba.org/⟩.


## VERSION

This manpage is current for version 3.4.3 of rsync.


## INTERNAL OPTIONS

The options --server and --sender are used internally by rsync,
and should never be typed by a user under normal circumstances.
Some awareness of these options may be needed in certain
scenarios, such as when setting up a login that can only run an
rsync command.  For instance, the support directory of the rsync
distribution has an example script named rrsync (for restricted
rsync) that can be used with a restricted ssh login.


## CREDITS

Rsync is distributed under the GNU General Public License.  See
the file COPYING for details.

An rsync web site is available at ⟨https://rsync.samba.org/⟩.  The
site includes an FAQ-O-Matic which may cover questions unanswered
by this manual page.

The rsync github project is 
⟨https://github.com/RsyncProject/rsync⟩.

We would be delighted to hear from you if you like this program.
Please contact the mailing-list at rsync@lists.samba.org
⟨mailto:rsync@lists.samba.org⟩.

This program uses the excellent zlib compression library written
by Jean-loup Gailly and Mark Adler.


## THANKS

Special thanks go out to: John Van Essen, Matt McCutchen, Wesley
W. Terpstra, David Dykstra, Jos Backus, Sebastian Krahmer, Martin
Pool, and our gone-but-not-forgotten compadre, J.W. Schultz.

Thanks also to Richard Brent, Brendan Mackay, Bill Waite, Stephen
Rothwell and David Bell.  I've probably missed some people, my
apologies if I have.


## AUTHOR

Rsync was originally written by Andrew Tridgell and Paul
Mackerras.  Many people from around the world have helped to
maintain and improve it.

Mailing lists for support and development are available at 
⟨https://lists.samba.org/⟩.
