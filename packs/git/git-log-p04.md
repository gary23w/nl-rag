---
title: "Git - git-log Documentation (part 4/4)"
source: https://git-scm.com/docs/git-log
domain: git
license: GPL-2.0
tags: git, merge conflict, version control
fetched: 2026-07-02
part: 4/4
---

## Generating patch text with -p

Running git-diff[1], git-log[1], git-show[1], git-diff-index[1], git-diff-tree[1], or git-diff-files[1] with the `-p` option produces patch text. You can customize the creation of patch text via the `GIT_EXTERNAL_DIFF` and the `GIT_DIFF_OPTS` environment variables (see git[1]), and the `diff` attribute (see gitattributes[5]).

What the `-p` option produces is slightly different from the traditional diff format:

1. It is preceded by a "git diff" header that looks like this: diff --git a/file1 b/file2 The `a/` and `b/` filenames are the same unless rename/copy is involved. Especially, even for a creation or a deletion, `/dev/null` is *not* used in place of the `a/` or `b/` filenames. When a rename/copy is involved, `file1` and `file2` show the name of the source file of the rename/copy and the name of the file that the rename/copy produces, respectively.
2. It is followed by one or more extended header lines: `old` `mode` *<mode>* `new` `mode` *<mode>* `deleted` `file` `mode` *<mode>* `new` `file` `mode` *<mode>* `copy` `from` *<path>* `copy` `to` *<path>* `rename` `from` *<path>* `rename` `to` *<path>* `similarity` `index` *<number>* `dissimilarity` `index` *<number>* `index` *<hash>*`..`*<hash>* *<mode>* File modes *<mode>* are printed as 6-digit octal numbers including the file type and file permission bits. Path names in extended headers do not include the `a/` and `b/` prefixes. The similarity index is the percentage of unchanged lines, and the dissimilarity index is the percentage of changed lines. It is a rounded down integer, followed by a percent sign. The similarity index value of 100% is thus reserved for two equal files, while 100% dissimilarity means that no line from the old file made it into the new one. The index line includes the blob object names before and after the change. The *<mode>* is included if the file mode does not change; otherwise, separate lines indicate the old and the new mode.
3. Pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see git-config[1]).
4. All the `file1` files in the output refer to files before the commit, and all the `file2` files refer to files after the commit. It is incorrect to apply each change to each file sequentially. For example, this patch will swap a and b: diff --git a/a b/b rename from a rename to b diff --git a/b b/a rename from b rename to a
5. Hunk headers mention the name of the function to which the hunk applies. See "Defining a custom hunk-header" in gitattributes[5] for details of how to tailor this to specific languages.


## Combined diff format

Any diff-generating command can take the `-c` or `--cc` option to produce a *combined diff* when showing a merge. This is the default format when showing merges with git-diff[1] or git-show[1]. Note also that you can give suitable `--diff-merges` option to any of these commands to force generation of diffs in a specific format.

A "combined diff" format looks like this:

diff --combined describe.c
index fabadb8,cc95eb0..4866510
--- a/describe.c
+++ b/describe.c
@@@ -98,20 -98,12 +98,20 @@@
	return (a_date > b_date) ? -1 : (a_date == b_date) ? 0 : 1;
  }

- static void describe(char *arg)
 -static void describe(struct commit *cmit, int last_one)
++static void describe(char *arg, int last_one)
  {
 +	unsigned char sha1[20];
 +	struct commit *cmit;
	struct commit_list *list;
	static int initialized = 0;
	struct commit_name *n;

 +	if (get_sha1(arg, sha1) < 0)
 +		usage(describe_usage);
 +	cmit = lookup_commit_reference(sha1);
 +	if (!cmit)
 +		usage(describe_usage);
 +
	if (!initialized) {
		initialized = 1;
		for_each_ref(get_name);

1. It is preceded by a "git diff" header, that looks like this (when the `-c` option is used): diff --combined file or like this (when the `--cc` option is used): diff --cc file
2. It is followed by one or more extended header lines (this example shows a merge with two parents): `index` *<hash>*`,`*<hash>*`..`*<hash>* `mode` *<mode>*`,`*<mode>*`..`*<mode>* `new` `file` `mode` *<mode>* `deleted` `file` `mode` *<mode>*`,`*<mode>* The `mode` *<mode>*`,`*<mode>*`..`*<mode>* line appears only if at least one of the <mode> is different from the rest. Extended headers with information about detected content movement (renames and copying detection) are designed to work with the diff of two *<tree-ish>* and are not used by combined diff format.
3. It is followed by a two-line from-file/to-file header: --- a/file +++ b/file Similar to the two-line header for the traditional *unified* diff format, `/dev/null` is used to signal created or deleted files. However, if the --combined-all-paths option is provided, instead of a two-line from-file/to-file, you get an N+1 line from-file/to-file header, where N is the number of parents in the merge commit: --- a/file --- a/file --- a/file +++ b/file This extended format can be useful if rename or copy detection is active, to allow you to see the original name of the file in different parents.
4. Chunk header format is modified to prevent people from accidentally feeding it to `patch` `-p1`. Combined diff format was created for review of merge commit changes, and was not meant to be applied. The change is similar to the change in the extended *index* header: @@@ <from-file-range> <from-file-range> <to-file-range> @@@ There are (number of parents + 1) `@` characters in the chunk header for combined diff format.

Unlike the traditional *unified* diff format, which shows two files A and B with a single column that has `-` (minus — appears in A but removed in B), `+` (plus — missing in A but added to B), or `"` `"` (space — unchanged) prefix, this format compares two or more files file1, file2,… with one file X, and shows how X differs from each of fileN. One column for each of fileN is prepended to the output line to note how X’s line is different from it.

A `-` character in the column N means that the line appears in fileN but it does not appear in the result. A `+` character in the column N means that the line appears in the result, and fileN does not have that line (in other words, the line was added, from the point of view of that parent).

In the above example output, the function signature was changed from both files (hence two `-` removals from both file1 and file2, plus `++` to mean one line that was added does not appear in either file1 or file2). Also, eight other lines are the same from file1 but do not appear in file2 (hence prefixed with `+`).

When shown by `git` `diff-tree` `-c`, it compares the parents of a merge commit with the merge result (i.e. file1..fileN are the parents). When shown by `git` `diff-files` `-c`, it compares the two unresolved merge parents with the working tree file (i.e. file1 is stage 2 aka "our version", file2 is stage 3 aka "their version").


## EXAMPLES

**`git` `log` `--no-merges`**

Show the whole commit history, but skip any merges

**`git` `log` `v2.6.12..` `include/scsi` `drivers/scsi`**

Show all commits since version *v2.6.12* that changed any file in the `include/scsi` or `drivers/scsi` subdirectories

**`git` `log` `--since="2` `weeks` `ago"` `--` `gitk`**

Show the changes during the last two weeks to the file `gitk`. The `--` is necessary to avoid confusion with the **branch** named `gitk`

**`git` `log` `--name-status` `release..test`**

Show the commits that are in the "`test`" branch but not yet in the "`release`" branch, along with the list of paths each commit modifies.

**`git` `log` `--follow` `builtin/rev-list.c`**

Shows the commits that changed `builtin/rev-list.c`, including those commits that occurred before the file was given its present name.

**`git` `log` `--branches` `--not` `--remotes=origin`**

Shows all commits that are in any of local branches but not in any of remote-tracking branches for `origin` (what you have that origin doesn’t).

**`git` `log` `master` `--not` `--remotes=*/master`**

Shows all commits that are in local master but not in any remote repository master branches.

**`git` `log` `-p` `-m` `--first-parent`**

Shows the history including change diffs, but only from the “main branch” perspective, skipping commits that come from merged branches, and showing full diffs of changes introduced by the merges. This makes sense only when following a strict policy of merging all topic branches when staying on a single integration branch.

**`git` `log` `-L` `/int` `main/',/^}/:main.c`**

Shows how the function `main`() in the file `main.c` evolved over time.

**`git` `log` `-3`**

Limits the number of commits to show to 3.


## DISCUSSION

Git is to some extent character encoding agnostic.

- The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.
- Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (`.git/config` (see git-config[1]), gitignore[5], gitattributes[5] and gitmodules[5]). Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.
- Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but *not* UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).

Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind.

1. `git` `commit` and `git` `commit-tree` issue a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have `i18n.commitEncoding` in `.git/config` file, like this: [i18n] commitEncoding = ISO-8859-1 Commit objects created with the above setting record the value of `i18n.commitEncoding` in their `encoding` header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.
2. `git` `log`, `git` `show`, `git` `blame` and friends look at the `encoding` header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with `i18n.logOutputEncoding` in `.git/config` file, like this: [i18n] logOutputEncoding = ISO-8859-1 If you do not have this configuration variable, the value of `i18n.commitEncoding` is used instead.

Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.


## CONFIGURATION

See git-config[1] for core variables and git-diff[1] for settings related to diff generation.

**`format.pretty`**

Default for the `--format` option. (See *Pretty Formats* above.) Defaults to `medium`.

**`i18n.logOutputEncoding`**

Encoding to use when displaying logs. (See *Discussion* above.) Defaults to the value of `i18n.commitEncoding` if set, and UTF-8 otherwise.

Everything above this line in this section isn’t included from the git-config[1] documentation. The content that follows is the same as what’s found there:

**`log.abbrevCommit`**

If `true`, make git-log[1], git-show[1], and git-whatchanged[1] assume `--abbrev-commit`. You may override this option with `--no-abbrev-commit`.

**`log.date`**

Set the default date-time mode for the `log` command. Setting a value for log.date is similar to using `git` `log`'s `--date` option. See git-log[1] for details.

If the format is set to "auto:foo" and the pager is in use, format "foo" will be used for the date format. Otherwise, "default" will be used.

**`log.decorate`**

Print out the ref names of any commits that are shown by the log command. Possible values are:

**`short`**

the ref name prefixes `refs/heads/`, `refs/tags/` and `refs/remotes/` are not printed.

**`full`**

the full ref name (including prefix) are printed.

**`auto`**

if the output is going to a terminal, the ref names are shown as if `short` were given, otherwise no ref names are shown.

This is the same as the `--decorate` option of the `git` `log`.

**`log.initialDecorationSet`**

By default, `git` `log` only shows decorations for certain known ref namespaces. If *all* is specified, then show all refs as decorations.

**`log.excludeDecoration`**

Exclude the specified patterns from the log decorations. This is similar to the `--decorate-refs-exclude` command-line option, but the config option can be overridden by the `--decorate-refs` option.

**`log.diffMerges`**

Set diff format to be used when `--diff-merges=on` is specified, see `--diff-merges` in git-log[1] for details. Defaults to `separate`.

**`log.follow`**

If `true`, `git` `log` will act as if the `--follow` option was used when a single <path> is given. This has the same limitations as `--follow`, i.e. it cannot be used to follow multiple files and does not work well on non-linear history.

**`log.graphColors`**

A list of colors, separated by commas, that can be used to draw history lines in `git` `log` `--graph`.

**`log.showRoot`**

If true, the initial commit will be shown as a big creation event. This is equivalent to a diff against an empty tree. Tools like git-log[1] or git-whatchanged[1], which normally hide the root commit will now show it. True by default.

**`log.showSignature`**

If true, makes git-log[1], git-show[1], and git-whatchanged[1] assume `--show-signature`.

**`log.mailmap`**

If true, makes git-log[1], git-show[1], and git-whatchanged[1] assume `--use-mailmap`, otherwise assume `--no-use-mailmap`. True by default.

**`notes.mergeStrategy`**

Which merge strategy to choose by default when resolving notes conflicts. Must be one of `manual`, `ours`, `theirs`, `union`, or `cat_sort_uniq`. Defaults to `manual`. See the "NOTES MERGE STRATEGIES" section of git-notes[1] for more information on each strategy.

This setting can be overridden by passing the `--strategy` option to git-notes[1].

**`notes.`*<name>*`.mergeStrategy`**

Which merge strategy to choose when doing a notes merge into `refs/notes/`*<name>*. This overrides the more general `notes.mergeStrategy`. See the "NOTES MERGE STRATEGIES" section in git-notes[1] for more information on the available strategies.

**`notes.displayRef`**

Which ref (or refs, if a glob or specified more than once), in addition to the default set by `core.notesRef` or `GIT_NOTES_REF`, to read notes from when showing commit messages with the `git` `log` family of commands.

This setting can be overridden with the `GIT_NOTES_DISPLAY_REF` environment variable, which must be a colon separated list of refs or globs.

A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored.

This setting can be disabled by the `--no-notes` option to the git-log[1] family of commands, or by the `--notes=`*<ref>* option accepted by those commands.

The effective value of `core.notesRef` (possibly overridden by `GIT_NOTES_REF`) is also implicitly added to the list of refs to be displayed.

**`notes.rewrite.`*<command>***

When rewriting commits with *<command>* (currently `amend` or `rebase`), if this variable is `false`, git will not copy notes from the original to the rewritten commit. Defaults to `true`. See also `notes.rewriteRef` below.

This setting can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable, which must be a colon separated list of refs or globs.

**`notes.rewriteMode`**

When copying notes during a rewrite (see the `notes.rewrite.`*<command>* option), determines what to do if the target commit already has a note. Must be one of `overwrite`, `concatenate`, `cat_sort_uniq`, or `ignore`. Defaults to `concatenate`.

This setting can be overridden with the `GIT_NOTES_REWRITE_MODE` environment variable.

**`notes.rewriteRef`**

When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. May be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times.

Does not have a default value; you must configure this variable to enable note rewriting. Set it to `refs/notes/commits` to enable rewriting for the default commit notes.

Can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable. See `notes.rewrite.`*<command>* above for a further description of its format.


## GIT

Part of the git[1] suite

### log
