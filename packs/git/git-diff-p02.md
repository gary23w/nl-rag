---
title: "Git - git-diff Documentation (part 2/2)"
source: https://git-scm.com/docs/git-diff
domain: git
license: GPL-2.0
tags: git, merge conflict, version control
fetched: 2026-07-02
part: 2/2
---

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


## other diff formats

The `--summary` option describes newly added, deleted, renamed and copied files. The `--stat` option adds `diffstat`(1) graph to the output. These options can be combined with other options, such as `-p`, and are meant for human consumption.

When showing a change that involves a rename or a copy, `--stat` output formats the pathnames compactly by combining common prefix and suffix of the pathnames. For example, a change that moves `arch/i386/Makefile` to `arch/x86/Makefile` while modifying 4 lines will be shown like this:

arch/{i386 => x86}/Makefile    |   4 +--

The `--numstat` option gives the diffstat(1) information but is designed for easier machine consumption. An entry in `--numstat` output looks like this:

1	2	README
3	1	arch/{i386 => x86}/Makefile

That is, from left to right:

1. the number of added lines;
2. a tab;
3. the number of deleted lines;
4. a tab;
5. pathname (possibly with rename/copy information);
6. a newline.

When `-z` output option is in effect, the output is formatted this way:

1	2	README NUL
3	1	NUL arch/i386/Makefile NUL arch/x86/Makefile NUL

That is:

1. the number of added lines;
2. a tab;
3. the number of deleted lines;
4. a tab;
5. a NUL (only exists if renamed/copied);
6. pathname in preimage;
7. a NUL (only exists if renamed/copied);
8. pathname in postimage (only exists if renamed/copied);
9. a NUL.

The extra `NUL` before the preimage path in renamed case is to allow scripts that read the output to tell if the current record being read is a single-path record or a rename/copy record without reading ahead. After reading added and deleted lines, reading up to `NUL` would yield the pathname, but if that is `NUL`, the record will show two paths.


## EXAMPLES

**Various ways to check your working tree**

$ git diff            (1)
$ git diff --cached   (2)
$ git diff HEAD       (3)
$ git diff AUTO_MERGE (4)

1. Changes in the working tree not yet staged for the next commit.
2. Changes between the index and your last commit; what you would be committing if you run `git` `commit` without `-a` option.
3. Changes in the working tree since your last commit; what you would be committing if you run `git` `commit` `-a`
4. Changes in the working tree you’ve made to resolve textual conflicts so far.

**Comparing with arbitrary commits**

$ git diff test            (1)
$ git diff HEAD -- ./test  (2)
$ git diff HEAD^ HEAD      (3)

1. Instead of using the tip of the current branch, compare with the tip of "test" branch.
2. Instead of comparing with the tip of "test" branch, compare with the tip of the current branch, but limit the comparison to the file "test".
3. Compare the version before the last commit and the last commit.

**Comparing branches**

$ git diff topic master    (1)
$ git diff topic..master   (2)
$ git diff topic...master  (3)

1. Changes between the tips of the topic and the master branches.
2. Same as above.
3. Changes that occurred on the master branch since when the topic branch was started off it.

**Limiting the diff output**

$ git diff --diff-filter=MRC            (1)
$ git diff --name-status                (2)
$ git diff arch/i386 include/asm-i386   (3)

1. Show only modification, rename, and copy, but not addition or deletion.
2. Show only names and the nature of change, but not actual diff output.
3. Limit diff output to named subtrees.

**Munging the diff output**

$ git diff --find-copies-harder -B -C  (1)
$ git diff -R                          (2)

1. Spend extra cycles to find renames, copies and complete rewrites (very expensive).
2. Output diff in reverse.


## CONFIGURATION

Everything below this line in this section is selectively included from the git-config[1] documentation. The content is the same as what’s found there:

**`diff.autoRefreshIndex`**

When using `git` `diff` to compare with work tree files, do not consider stat-only changes as changed. Instead, silently run `git` `update-index` `--refresh` to update the cached stat information for paths whose contents in the work tree match the contents in the index. This option defaults to `true`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`.

**`diff.dirstat`**

A comma separated list of `--dirstat` parameters specifying the default behavior of the `--dirstat` option to `git` `diff` and friends. The defaults can be overridden on the command line (using `--dirstat=`*<param>*`,...`). The fallback defaults (when not changed by `diff.dirstat`) are `changes,noncumulative,3`. The following parameters are available:

**`changes`**

Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given.

**`lines`**

Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options.

**`files`**

Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all.

**`cumulative`**

Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter.

***<limit>***

An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.

Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `files,10,cumulative`.

**`diff.statNameWidth`**

Limit the width of the filename part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

**`diff.statGraphWidth`**

Limit the width of the graph part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

**`diff.context`**

Generate diffs with *<n>* lines of context instead of the default of 3. This value is overridden by the `-U` option.

**`diff.interHunkContext`**

Show the context between diff hunks, up to the specified number of lines, thereby fusing the hunks that are close to each other. This value serves as the default for the `--inter-hunk-context` command line option.

**`diff.external`**

If this config variable is set, diff generation is not performed using the internal diff machinery, but using the given command. Can be overridden with the `GIT_EXTERNAL_DIFF` environment variable. The command is called with parameters as described under "git Diffs" in git[1]. Note: if you want to use an external diff program only on a subset of your files, you might want to use gitattributes[5] instead.

**`diff.trustExitCode`**

If this boolean value is set to `true` then the `diff.external` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code `0` regardless of equality. Any other exit code causes Git to report a fatal error.

**`diff.ignoreSubmodules`**

Sets the default value of `--ignore-submodules`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`. `git` `checkout` and `git` `switch` also honor this setting when reporting uncommitted changes. Setting it to `all` disables the submodule summary normally shown by `git` `commit` and `git` `status` when `status.submoduleSummary` is set unless it is overridden by using the `--ignore-submodules` command-line option. The `git` `submodule` commands are not affected by this setting. By default this is set to untracked so that any untracked submodules are ignored.

**`diff.mnemonicPrefix`**

If set, `git` `diff` uses a prefix pair that is different from the standard `a/` and `b/` depending on what is being compared. When this configuration is in effect, reverse diff output also swaps the order of the prefixes:

**`git` `diff`**

compares the (i)ndex and the (w)ork tree;

**`git` `diff` `HEAD`**

compares a (c)ommit and the (w)ork tree;

**`git` `diff` `--cached`**

compares a (c)ommit and the (i)ndex;

**`git` `diff` `HEAD:`*<file1>* *<file2>***

compares an (o)bject and a (w)ork tree entity;

**`git` `diff` `--no-index` *<a>* *<b>***

compares two non-git things *<a>* and *<b>*.

**`diff.noPrefix`**

If set, `git` `diff` does not show any source or destination prefix.

**`diff.srcPrefix`**

If set, `git` `diff` uses this source prefix. Defaults to `a/`.

**`diff.dstPrefix`**

If set, `git` `diff` uses this destination prefix. Defaults to `b/`.

**`diff.relative`**

If set to `true`, `git` `diff` does not show changes outside of the directory and show pathnames relative to the current directory.

**`diff.orderFile`**

File indicating how to order files within a diff. See the `-O` option for details. If `diff.orderFile` is a relative pathname, it is treated as relative to the top of the working tree.

**`diff.renameLimit`**

The number of files to consider in the exhaustive portion of copy/rename detection; equivalent to the `git` `diff` option `-l`. If not set, the default value is currently 1000. This setting has no effect if rename detection is turned off.

**`diff.renames`**

Whether and how Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. If set to `copies` or `copy`, Git will detect copies, as well. Defaults to `true`. Note that this affects only `git` `diff` Porcelain like git-diff[1] and git-log[1], and not lower level commands such as git-diff-files[1].

**`diff.suppressBlankEmpty`**

A boolean to inhibit the standard behavior of printing a space before each empty output line. Defaults to `false`.

**`diff.submodule`**

Specify the format in which differences in submodules are shown. The `short` format just shows the names of the commits at the beginning and end of the range. The `log` format lists the commits in the range like git-submodule[1] `summary` does. The `diff` format shows an inline diff of the changed contents of the submodule. Defaults to `short`.

**`diff.wordRegex`**

A POSIX Extended Regular Expression used to determine what is a "word" when performing word-by-word difference calculations. Character sequences that match the regular expression are "words", all other characters are **ignorable** whitespace.

**`diff.`*<driver>*`.command`**

The custom diff driver command. See gitattributes[5] for details.

**`diff.`*<driver>*`.trustExitCode`**

If this boolean value is set to `true` then the `diff.`*<driver>*`.command` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code 0 regardless of equality. Any other exit code causes Git to report a fatal error.

**`diff.`*<driver>*`.xfuncname`**

The regular expression that the diff driver should use to recognize the hunk header. A built-in pattern may also be used. See gitattributes[5] for details.

**`diff.`*<driver>*`.binary`**

Set this option to `true` to make the diff driver treat files as binary. See gitattributes[5] for details.

**`diff.`*<driver>*`.textconv`**

The command that the diff driver should call to generate the text-converted version of a file. The result of the conversion is used to generate a human-readable diff. See gitattributes[5] for details.

**`diff.`*<driver>*`.wordRegex`**

The regular expression that the diff driver should use to split words in a line. See gitattributes[5] for details.

**`diff.`*<driver>*`.cachetextconv`**

Set this option to `true` to make the diff driver cache the text conversion outputs. See gitattributes[5] for details.

**`diff.indentHeuristic`**

Set this option to `false` to disable the default heuristics that shift diff hunk boundaries to make patches easier to read.

**`diff.algorithm`**

Choose a diff algorithm. The variants are as follows:

**`default`**

**`myers`**

The basic greedy diff algorithm. Currently, this is the default.

**`minimal`**

Spend extra time to make sure the smallest possible diff is produced.

**`patience`**

Use "patience diff" algorithm when generating patches.

**`histogram`**

This algorithm extends the patience algorithm to "support low-occurrence common elements".

**`diff.wsErrorHighlight`**

Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. The whitespace errors are colored with `color.diff.whitespace`. The command line option `--ws-error-highlight=`*<kind>* overrides this setting.

**`diff.colorMoved`**

If set to either a valid *<mode>* or a `true` value, moved lines in a diff are colored differently. For details of valid modes see `--color-moved`. If simply set to `true` the default color mode will be used. When set to `false`, moved lines are not colored.

**`diff.colorMovedWS`**

When moved lines are colored using e.g. the `diff.colorMoved` setting, this option controls the mode how spaces are treated. For details of valid modes see `--color-moved-ws` in git-diff[1].
