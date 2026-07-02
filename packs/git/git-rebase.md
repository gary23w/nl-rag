---
title: "Git - git-rebase Documentation"
source: https://git-scm.com/docs/git-rebase
domain: git
license: GPL-2.0
tags: git, merge conflict, version control
fetched: 2026-07-02
---

# Git - git-rebase Documentation

English ▾

Localized versions of

git-rebase

manual

1. English
2. Français
3. Português (Brasil)
4. Русский
5. Svenska
6. українська мова
7. 简体中文

Topics ▾

### Setup and Config

- git
- config
- help
- bugreport
- Credential helpers

### Getting and Creating Projects

- init
- clone

### Basic Snapshotting

- add
- status
- diff
- commit
- notes
- restore
- reset
- rm
- mv

### Branching and Merging

- branch
- checkout
- switch
- merge
- mergetool
- log
- stash
- tag
- worktree

### Sharing and Updating Projects

- fetch
- pull
- push
- remote
- submodule

### Inspection and Comparison

- show
- log
- diff
- difftool
- range-diff
- shortlog
- describe

### Patching

- apply
- cherry-pick
- diff
- rebase
- revert

### Debugging

- bisect
- blame
- grep

### Email

- am
- apply
- imap-send
- format-patch
- send-email
- request-pull

### External Systems

- svn
- fast-import

### Server Admin

- daemon
- update-server-info

### Guides

- gitattributes
- Command-line interface conventions
- Everyday Git
- Frequently Asked Questions (FAQ)
- Glossary
- Hooks
- gitignore
- gitmodules
- Revisions
- Submodules
- Tutorial
- Workflows
- All guides...

### Administration

- clean
- gc
- fsck
- reflog
- filter-branch
- instaweb
- archive
- bundle

### Plumbing Commands

- cat-file
- check-ignore
- checkout-index
- commit-tree
- count-objects
- diff-index
- for-each-ref
- hash-object
- ls-files
- ls-tree
- merge-base
- read-tree
- rev-list
- rev-parse
- show-ref
- symbolic-ref
- update-index
- update-ref
- verify-pack
- write-tree

Latest version ▾

git-rebase last updated in 2.54.0

Changes in the

git-rebase

manual

1. 2.55.0 no changes
2. 2.54.0 *2026-04-20*
3. 2.53.0 *2026-02-02*
4. 2.52.0 *2025-11-17*
5. 2.50.1 → 2.51.2 no changes
6. 2.50.0 *2025-06-16*
7. 2.49.1 no changes
8. 2.49.0 *2025-03-14*
9. 2.46.2 → 2.48.2 no changes
10. 2.46.1 *2024-09-13*
11. 2.45.1 → 2.46.0 no changes
12. 2.45.0 *2024-04-29*
13. 2.44.1 → 2.44.4 no changes
14. 2.44.0 *2024-02-23*
15. 2.43.3 → 2.43.7 no changes
16. 2.43.2 *2024-02-13*
17. 2.43.1 *2024-02-09*
18. 2.43.0 *2023-11-20*
19. 2.42.2 → 2.42.4 no changes
20. 2.42.1 *2023-11-02*
21. 2.41.1 → 2.42.0 no changes
22. 2.41.0 *2023-06-01*
23. 2.40.1 → 2.40.4 no changes
24. 2.40.0 *2023-03-12*
25. 2.39.4 → 2.39.5 no changes
26. 2.39.3 *2023-04-17*
27. 2.39.1 → 2.39.2 no changes
28. 2.39.0 *2022-12-12*
29. 2.38.1 → 2.38.5 no changes
30. 2.38.0 *2022-10-02*
31. 2.37.3 → 2.37.7 no changes
32. 2.37.2 *2022-08-11*
33. 2.36.3 → 2.37.1 no changes
34. 2.36.2 *2022-06-23*
35. 2.35.1 → 2.36.1 no changes
36. 2.35.0 *2022-01-24*
37. 2.34.1 → 2.34.8 no changes
38. 2.34.0 *2021-11-15*
39. 2.33.2 → 2.33.8 no changes
40. 2.33.1 *2021-10-12*
41. 2.32.1 → 2.33.0 no changes
42. 2.32.0 *2021-06-06*
43. 2.31.1 → 2.31.8 no changes
44. 2.31.0 *2021-03-15*
45. 2.30.1 → 2.30.9 no changes
46. 2.30.0 *2020-12-27*
47. 2.29.1 → 2.29.3 no changes
48. 2.29.0 *2020-10-19*
49. 2.28.1 no changes
50. 2.28.0 *2020-07-27*
51. 2.27.1 no changes
52. 2.27.0 *2020-06-01*
53. 2.26.1 → 2.26.3 no changes
54. 2.26.0 *2020-03-22*
55. 2.25.1 → 2.25.5 no changes
56. 2.25.0 *2020-01-13*
57. 2.24.1 → 2.24.4 no changes
58. 2.24.0 *2019-11-04*
59. 2.23.1 → 2.23.4 no changes
60. 2.23.0 *2019-08-16*
61. 2.22.1 → 2.22.5 no changes
62. 2.22.0 *2019-06-07*
63. 2.21.1 → 2.21.4 no changes
64. 2.21.0 *2019-02-24*
65. 2.20.1 → 2.20.5 no changes
66. 2.20.0 *2018-12-09*
67. 2.19.3 → 2.19.6 no changes
68. 2.19.2 *2018-11-21*
69. 2.19.1 no changes
70. 2.19.0 *2018-09-10*
71. 2.18.1 → 2.18.5 no changes
72. 2.18.0 *2018-06-21*
73. 2.17.1 → 2.17.6 no changes
74. 2.17.0 *2018-04-02*
75. 2.16.6 *2019-12-06*
76. 2.15.4 *2019-12-06*
77. 2.14.6 *2019-12-06*
78. 2.13.7 *2018-05-22*
79. 2.12.5 *2017-09-22*
80. 2.10.5 → 2.11.4 no changes
81. 2.9.5 *2017-07-30*
82. 2.8.6 *2017-07-30*
83. 2.7.6 no changes
84. 2.6.7 *2017-05-05*
85. 2.5.6 no changes
86. 2.4.12 *2017-05-05*
87. 2.3.10 *2015-09-28*
88. 2.2.3 *2015-09-04*
89. 2.1.4 *2014-12-17*
90. 2.0.5 *2014-12-17*

## NAME

git-rebase - Reapply commits on top of another base tip

## SYNOPSIS

git rebase [-i | --interactive] [<options>] [--exec <cmd>]
	[--onto <newbase> | --keep-base] [<upstream> [<branch>]]
git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase>]
	--root [<branch>]
git rebase (--continue|--skip|--abort|--quit|--edit-todo|--show-current-patch)

## DESCRIPTION

Transplant a series of commits onto a different starting point. You can also use `git` `rebase` to reorder or combine commits: see INTERACTIVE MODE below for how to do that.

For example, imagine that you have been working on the `topic` branch in this history, and you want to "catch up" to the work done on the `master` branch.

   A---B---C topic
  /

### D---E---F---G master

You want to transplant the commits you made on `topic` since it diverged from `master` (i.e. A, B, and C), on top of the current `master`. You can do this by running `git` `rebase` `master` while the `topic` branch is checked out. If you want to rebase `topic` while on another branch, `git` `rebase` `master` `topic` is a shortcut for *git checkout topic && git rebase master*.

           A'--B'--C' topic
          /

### D---E---F---G master

If there is a merge conflict during this process, `git` `rebase` will stop at the first problematic commit and leave conflict markers. If this happens, you can do one of these things:

1. Resolve the conflict. You can use `git` `diff` to find the markers (<<<<<<) and make edits to resolve the conflict. For each file you edit, you need to tell Git that the conflict has been resolved. You can mark the conflict as resolved with `git` `add` *<filename>*. After resolving all of the conflicts, you can continue the rebasing process with git rebase --continue
2. Stop the `git` `rebase` and return your branch to its original state with git rebase --abort
3. Skip the commit that caused the merge conflict with git rebase --skip

If you don’t specify an *<upstream>* to rebase onto, the upstream configured in `branch.`*<name>*`.remote` and `branch.`*<name>*`.merge` options will be used (see git-config[1] for details) and the `--fork-point` option is assumed. If you are currently not on any branch or if the current branch does not have a configured upstream, the rebase will abort.

Here is a simplified description of what `git` `rebase` *<upstream>* does:

1. Make a list of all commits on your current branch since it branched off from *<upstream>* that do not have an equivalent commit in *<upstream>*.
2. Check out *<upstream>* with the equivalent of `git` `checkout` `--detach` *<upstream>*.
3. Replay the commits, one by one, in order. This is similar to running `git` `cherry-pick` *<commit>* for each commit. See REBASING MERGES for how merges are handled.
4. Update your branch to point to the final commit with the equivalent of `git` `checkout` `-B` *<branch>*.

| Note | When starting the rebase, `ORIG_HEAD` is set to point to the commit at the tip of the to-be-rebased branch. However, `ORIG_HEAD` is not guaranteed to still point to that commit at the end of the rebase if other commands that change `ORIG_HEAD` (like `git` `reset`) are used during the rebase. The previous branch tip, however, is accessible using the reflog of the current branch (i.e. `@{1}`, see gitrevisions[7]). |
|---|---|

## TRANSPLANTING A TOPIC BRANCH WITH --ONTO

Here is how you would transplant a topic branch based on one branch to another, to pretend that you forked the topic branch from the latter branch, using `rebase` `--onto`.

First let’s assume your *topic* is based on branch *next*. For example, a feature developed in *topic* depends on some functionality which is found in *next*.

    o---o---o---o---o  master
  \
   o---o---o---o---o  next
                    \
                     o---o---o  topic

We want to make *topic* forked from branch *master*; for example, because the functionality on which *topic* depends was merged into the more stable *master* branch. We want our tree to look like this:

    o---o---o---o---o  master
 |            \
 |             o'--o'--o'  topic
  \
   o---o---o---o---o  next

We can get this using the following command:

git rebase --onto master next topic

Another example of --onto option is to rebase part of a branch. If we have the following situation:

                     H---I---J topicB
                    /
           E---F---G  topicA
          /

### A---B---C---D  master

then the command

git rebase --onto master topicA topicB

would result in:

          H'--I'--J'  topicB
         /
         | E---F---G  topicA
         |/

### A---B---C---D  master

This is useful when topicB does not depend on topicA.

A range of commits could also be removed with rebase. If we have the following situation:

### E---F---G---H---I---J  topicA

then the command

git rebase --onto topicA~5 topicA~3 topicA

would result in the removal of commits F and G:

### E---H'---I'---J'  topicA

This is useful if F and G were flawed in some way, or should not be part of topicA. Note that the argument to `--onto` and the *<upstream>* parameter can be any valid commit-ish.

## MODE OPTIONS

The options in this section cannot be used with any other option, including not with each other:

**--continue**

Restart the rebasing process after having resolved a merge conflict.

Restart the rebasing process by skipping the current patch.

**--abort**

Abort the rebase operation and reset HEAD to the original branch. If *<branch>* was provided when the rebase operation was started, then `HEAD` will be reset to *<branch>*. Otherwise `HEAD` will be reset to where it was when the rebase operation was started.

**--quit**

Abort the rebase operation but `HEAD` is not reset back to the original branch. The index and working tree are also left unchanged as a result. If a temporary stash entry was created using `--autostash`, it will be saved to the stash list.

Edit the todo list during an interactive rebase.

**--show-current-patch**

Show the current patch in an interactive rebase or when rebase is stopped because of conflicts. This is the equivalent of `git` `show` `REBASE_HEAD`.

## OPTIONS

**--onto <newbase>**

Starting point at which to create the new commits. If the `--onto` option is not specified, the starting point is *<upstream>*. May be any valid commit, and not just an existing branch name.

As a special case, you may use "A...B" as a shortcut for the merge base of A and B if there is exactly one merge base. You can leave out at most one of A and B, in which case it defaults to HEAD.

See TRANSPLANTING A TOPIC BRANCH WITH --ONTO above for examples.

**--keep-base**

Set the starting point at which to create the new commits to the merge base of *<upstream>* and *<branch>*. Running `git` `rebase` `--keep-base` *<upstream>* *<branch>* is equivalent to running `git` `rebase` `--reapply-cherry-picks` `--no-fork-point` `--onto` *<upstream>*`...`*<branch>* *<upstream>* *<branch>*.

This option is useful in the case where one is developing a feature on top of an upstream branch. While the feature is being worked on, the upstream branch may advance and it may not be the best idea to keep rebasing on top of the upstream but to keep the base commit as-is. As the base commit is unchanged this option implies `--reapply-cherry-picks` to avoid losing commits.

Although both this option and `--fork-point` find the merge base between *<upstream>* and *<branch>*, this option uses the merge base as the *starting point* on which new commits will be created, whereas `--fork-point` uses the merge base to determine the *set of commits* which will be rebased.

See also INCOMPATIBLE OPTIONS below.

**<upstream>**

Upstream branch to compare against. May be any valid commit, not just an existing branch name. Defaults to the configured upstream for the current branch.

**<branch>**

Working branch; defaults to `HEAD`.

**--apply**

Use applying strategies to rebase (calling `git-am` internally). This option may become a no-op in the future once the merge backend handles everything the apply one does.

See also INCOMPATIBLE OPTIONS below.

**--empty=(drop|keep|stop)**

How to handle commits that are not empty to start and are not clean cherry-picks of any upstream commit, but which become empty after rebasing (because they contain a subset of already upstream changes):

**`drop`**

The commit will be dropped. This is the default behavior.

**`keep`**

The commit will be kept. This option is implied when `--exec` is specified unless `-i`/`--interactive` is also specified.

**`stop`**

**`ask`**

The rebase will halt when the commit is applied, allowing you to choose whether to drop it, edit files more, or just commit the empty changes. This option is implied when `-i`/`--interactive` is specified. `ask` is a deprecated synonym of `stop`.

Note that commits which start empty are kept (unless `--no-keep-empty` is specified), and commits which are clean cherry-picks (as determined by `git` `log` `--cherry-mark` ...) are detected and dropped as a preliminary step (unless `--reapply-cherry-picks` or `--keep-base` is passed).

See also INCOMPATIBLE OPTIONS below.

**--no-keep-empty**

**--keep-empty**

Do not keep commits that start empty before the rebase (i.e. that do not change anything from its parent) in the result. The default is to keep commits which start empty, since creating such commits requires passing the `--allow-empty` override flag to `git` `commit`, signifying that a user is very intentionally creating such a commit and thus wants to keep it.

Usage of this flag will probably be rare, since you can get rid of commits that start empty by just firing up an interactive rebase and removing the lines corresponding to the commits you don’t want. This flag exists as a convenient shortcut, such as for cases where external tools generate many empty commits and you want them all removed.

For commits which do not start empty but become empty after rebasing, see the `--empty` flag.

See also INCOMPATIBLE OPTIONS below.

**--reapply-cherry-picks**

**--no-reapply-cherry-picks**

Reapply all clean cherry-picks of any upstream commit instead of preemptively dropping them. (If these commits then become empty after rebasing, because they contain a subset of already upstream changes, the behavior towards them is controlled by the `--empty` flag.)

In the absence of `--keep-base` (or if `--no-reapply-cherry-picks` is given), these commits will be automatically dropped. Because this necessitates reading all upstream commits, this can be expensive in repositories with a large number of upstream commits that need to be read. When using the *merge* backend, warnings will be issued for each dropped commit (unless `--quiet` is given). Advice will also be issued unless `advice.skippedCherryPicks` is set to false (see git-config[1]).

`--reapply-cherry-picks` allows rebase to forgo reading all upstream commits, potentially improving performance.

See also INCOMPATIBLE OPTIONS below.

**--allow-empty-message**

No-op. Rebasing commits with an empty message used to fail and this option would override that behavior, allowing commits with empty messages to be rebased. Now commits with an empty message do not cause rebasing to halt.

See also INCOMPATIBLE OPTIONS below.

**-m**

**--merge**

Using merging strategies to rebase (default).

Note that a rebase merge works by replaying each commit from the working branch on top of the *<upstream>* branch. Because of this, when a merge conflict happens, the side reported as *ours* is the so-far rebased series, starting with *<upstream>*, and *theirs* is the working branch. In other words, the sides are swapped.

See also INCOMPATIBLE OPTIONS below.

**-s <strategy>**

**--strategy=<strategy>**

Use the given merge strategy, instead of the default `ort`. This implies `--merge`.

Because `git` `rebase` replays each commit from the working branch on top of the *<upstream>* branch using the given strategy, using the `ours` strategy simply empties all patches from the *<branch>*, which makes little sense.

See also INCOMPATIBLE OPTIONS below.

**-X <strategy-option>**

**--strategy-option=<strategy-option>**

Pass the <strategy-option> through to the merge strategy. This implies `--merge` and, if no strategy has been specified, `-s` `ort`. Note the reversal of *ours* and *theirs* as noted above for the `-m` option.

See also INCOMPATIBLE OPTIONS below.

**`--rerere-autoupdate`**

**`--no-rerere-autoupdate`**

After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what git-rerere[1] did and catch potential mismerges, before committing the result to the index with a separate git-add[1].

**-S[<keyid>]**

**--gpg-sign[=<keyid>]**

**--no-gpg-sign**

GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`.

**-q**

**--quiet**

Be quiet. Implies `--no-stat`.

**-v**

**--verbose**

Be verbose. Implies `--stat`.

**--stat**

Show a diffstat of what changed upstream since the last rebase. The diffstat is also controlled by the configuration option rebase.stat.

**-n**

**--no-stat**

Do not show a diffstat as part of the rebase process.

**--no-verify**

This option bypasses the pre-rebase hook. See also githooks[5].

**--verify**

Allows the pre-rebase hook to run, which is the default. This option can be used to override `--no-verify`. See also githooks[5].

**-C<n>**

Ensure at least *<n>* lines of surrounding context match before and after each change. When fewer lines of surrounding context exist they all must match. By default no context is ever ignored. Implies `--apply`.

See also INCOMPATIBLE OPTIONS below.

**--no-ff**

**--force-rebase**

**-f**

Individually replay all rebased commits instead of fast-forwarding over the unchanged ones. This ensures that the entire history of the rebased branch is composed of new commits.

You may find this helpful after reverting a topic branch merge, as this option recreates the topic branch with fresh commits so it can be remerged successfully without needing to "revert the reversion" (see the revert-a-faulty-merge How-To for details).

**--fork-point**

**--no-fork-point**

Use reflog to find a better common ancestor between *<upstream>* and *<branch>* when calculating which commits have been introduced by *<branch>*.

When `--fork-point` is active, *fork_point* will be used instead of *<upstream>* to calculate the set of commits to rebase, where *fork_point* is the result of `git` `merge-base` `--fork-point` *<upstream>* *<branch>* command (see git-merge-base[1]). If *fork_point* ends up being empty, the *<upstream>* will be used as a fallback.

If *<upstream>* or `--keep-base` is given on the command line, then the default is `--no-fork-point`, otherwise the default is `--fork-point`. See also `rebase.forkpoint` in git-config[1].

If your branch was based on *<upstream>* but *<upstream>* was rewound and your branch contains commits which were dropped, this option can be used with `--keep-base` in order to drop those commits from your branch.

See also INCOMPATIBLE OPTIONS below.

**--ignore-whitespace**

Ignore whitespace differences when trying to reconcile differences. Currently, each backend implements an approximation of this behavior:

**apply backend**

When applying a patch, ignore changes in whitespace in context lines. Unfortunately, this means that if the "old" lines being replaced by the patch differ only in whitespace from the existing file, you will get a merge conflict instead of a successful patch application.

**merge backend**

Treat lines with only whitespace changes as unchanged when merging. Unfortunately, this means that any patch hunks that were intended to modify whitespace and nothing else will be dropped, even if the other side had no changes that conflicted.

**--whitespace=<option>**

This flag is passed to the `git` `apply` program (see git-apply[1]) that applies the patch. Implies `--apply`.

See also INCOMPATIBLE OPTIONS below.

**--committer-date-is-author-date**

Instead of using the current time as the committer date, use the author date of the commit being rebased as the committer date. This option implies `--force-rebase`.

| Warning | The history walking machinery assumes that commits have non-decreasing commit timestamps. You should consider if you really need to use this option. Then you should only use this option to override the committer date when rebasing commits on top of a base which commit is older (in terms of the commit date) than the oldest commit you are applying (in terms of the author date). |
|---|---|

**--ignore-date**

**--reset-author-date**

Instead of using the author date of the original commit, use the current time as the author date of the rebased commit. This option implies `--force-rebase`.

See also INCOMPATIBLE OPTIONS below.

**--signoff**

Add a `Signed-off-by` trailer to all the rebased commits. Note that if `--interactive` is given then only commits marked to be picked, edited or reworded will have the trailer added.

See also INCOMPATIBLE OPTIONS below.

**--trailer=<trailer>**

Append the given trailer to every rebased commit message, processed via git-interpret-trailers[1]. This option implies `--force-rebase`.

See also INCOMPATIBLE OPTIONS below.

**-i**

**--interactive**

Make a list of the commits which are about to be rebased. Let the user edit that list before rebasing. This mode can also be used to split commits (see SPLITTING COMMITS below).

The commit list format can be changed by setting the configuration option rebase.instructionFormat. A customized instruction format will automatically have the commit hash prepended to the format.

See also INCOMPATIBLE OPTIONS below.

**-r**

**--rebase-merges[=(rebase-cousins|no-rebase-cousins)]**

**--no-rebase-merges**

By default, a rebase will simply drop merge commits from the todo list, and put the rebased commits into a single, linear branch. With `--rebase-merges`, the rebase will instead try to preserve the branching structure within the commits that are to be rebased, by recreating the merge commits. Any resolved merge conflicts or manual amendments in these merge commits will have to be resolved/re-applied manually. `--no-rebase-merges` can be used to countermand both the `rebase.rebaseMerges` config option and a previous `--rebase-merges`.

When rebasing merges, there are two modes: `rebase-cousins` and `no-rebase-cousins`. If the mode is not specified, it defaults to `no-rebase-cousins`. In `no-rebase-cousins` mode, commits which do not have *<upstream>* as direct ancestor will keep their original branch point, i.e. commits that would be excluded by git-log[1]'s `--ancestry-path` option will keep their original ancestry by default. In `rebase-cousins` mode, such commits are instead rebased onto *<upstream>* (or *<onto>*, if specified).

It is currently only possible to recreate the merge commits using the `ort` merge strategy; different merge strategies can be used only via explicit `exec` `git` `merge` `-s` *<strategy>* [...] commands.

See also REBASING MERGES and INCOMPATIBLE OPTIONS below.

**-x <cmd>**

**--exec <cmd>**

Append "exec <cmd>" after each line creating a commit in the final history. *<cmd>* will be interpreted as one or more shell commands. Any command that fails will interrupt the rebase, with exit code 1.

You may execute several commands by either using one instance of `--exec` with several commands:

git rebase -i --exec "cmd1 && cmd2 && ..."

or by giving more than one `--exec`:

git rebase -i --exec "cmd1" --exec "cmd2" --exec ...

If `--autosquash` is used, `exec` lines will not be appended for the intermediate commits, and will only appear at the end of each squash/fixup series.

This uses the `--interactive` machinery internally, but it can be run without an explicit `--interactive`.

See also INCOMPATIBLE OPTIONS below.

**--root**

Rebase all commits reachable from *<branch>*, instead of limiting them with an *<upstream>*. This allows you to rebase the root commit(s) on a branch.

See also INCOMPATIBLE OPTIONS below.

**--autosquash**

**--no-autosquash**

Automatically squash commits with specially formatted messages into previous commits being rebased. If a commit message starts with "squash! ", "fixup! " or "amend! ", the remainder of the title is taken as a commit specifier, which matches a previous commit if it matches the title or the hash of that commit. If no commit matches fully, matches of the specifier with the start of commit titles are considered.

In the rebase todo list, the actions of squash, fixup and amend commits are changed from `pick` to `squash`, `fixup` or `fixup` `-C`, respectively, and they are moved right after the commit they modify. The `--interactive` option can be used to review and edit the todo list before proceeding.

The recommended way to create commits with squash markers is by using the `--squash`, `--fixup`, `--fixup=amend:` or `--fixup=reword:` options of git-commit[1], which take the target commit as an argument and automatically fill in the title of the new commit from that.

Setting configuration variable `rebase.autoSquash` to true enables auto-squashing by default for interactive rebase. The `--no-autosquash` option can be used to override that setting.

See also INCOMPATIBLE OPTIONS below.

**--autostash**

**--no-autostash**

Automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts.

**--reschedule-failed-exec**

**--no-reschedule-failed-exec**

Automatically reschedule `exec` commands that failed. This only makes sense in interactive mode (or when an `--exec` option was provided).

This option applies once a rebase is started. It is preserved for the whole rebase based on, in order, the command line option provided to the initial `git` `rebase`, the `rebase.rescheduleFailedExec` configuration (see git-config[1] or "CONFIGURATION" below), or it defaults to false.

Recording this option for the whole rebase is a convenience feature. Otherwise an explicit `--no-reschedule-failed-exec` at the start would be overridden by the presence of a `rebase.rescheduleFailedExec=true` configuration when `git` `rebase` `--continue` is invoked. Currently, you cannot pass `--`[`no-`]`reschedule-failed-exec` to `git` `rebase` `--continue`.

**--update-refs**

**--no-update-refs**

Automatically force-update any branches that point to commits that are being rebased. Any branches that are checked out in a worktree are not updated in this way.

If the configuration variable `rebase.updateRefs` is set, then this option can be used to override and disable this setting.

See also INCOMPATIBLE OPTIONS below.

## INCOMPATIBLE OPTIONS

The following options:

- --apply
- --whitespace
- -C

are incompatible with the following options:

- --merge
- --strategy
- --strategy-option
- --autosquash
- --rebase-merges
- --interactive
- --exec
- --no-keep-empty
- --empty=
- --[no-]reapply-cherry-picks when used without --keep-base
- --update-refs
- --root when used without --onto
- --trailer

In addition, the following pairs of options are incompatible:

- --keep-base and --onto
- --keep-base and --root
- --fork-point and --root

## BEHAVIORAL DIFFERENCES

`git` `rebase` has two primary backends: *apply* and *merge*. (The *apply* backend used to be known as the *am* backend, but the name led to confusion as it looks like a verb instead of a noun. Also, the *merge* backend used to be known as the interactive backend, but it is now used for non-interactive cases as well. Both were renamed based on lower-level functionality that underpinned each.) There are some subtle differences in how these two backends behave:

### Empty commits

The *apply* backend unfortunately drops intentionally empty commits, i.e. commits that started empty, though these are rare in practice. It also drops commits that become empty and has no option for controlling this behavior.

The *merge* backend keeps intentionally empty commits by default (though with `-i` they are marked as empty in the todo list editor, or they can be dropped automatically with `--no-keep-empty`).

Similar to the apply backend, by default the merge backend drops commits that become empty unless `-i`/`--interactive` is specified (in which case it stops and asks the user what to do). The merge backend also has an `--empty=`(`drop`|`keep`|`stop`) option for changing the behavior of handling commits that become empty.

### Directory rename detection

Due to the lack of accurate tree information (arising from constructing fake ancestors with the limited information available in patches), directory rename detection is disabled in the *apply* backend. Disabled directory rename detection means that if one side of history renames a directory and the other adds new files to the old directory, then the new files will be left behind in the old directory without any warning at the time of rebasing that you may want to move these files into the new directory.

Directory rename detection works with the *merge* backend to provide you warnings in such cases.

### Context

The *apply* backend works by creating a sequence of patches (by calling `format-patch` internally), and then applying the patches in sequence (calling `am` internally). Patches are composed of multiple hunks, each with line numbers, a context region, and the actual changes. The line numbers have to be taken with some offset, since the other side will likely have inserted or deleted lines earlier in the file. The context region is meant to help find how to adjust the line numbers in order to apply the changes to the right lines. However, if multiple areas of the code have the same surrounding lines of context, the wrong one can be picked. There are real-world cases where this has caused commits to be reapplied incorrectly with no conflicts reported. Setting `diff.context` to a larger value may prevent such types of problems, but increases the chance of spurious conflicts (since it will require more lines of matching context to apply).

The *merge* backend works with a full copy of each relevant file, insulating it from these types of problems.

### Labelling of conflicts markers

When there are content conflicts, the merge machinery tries to annotate each side’s conflict markers with the commits where the content came from. Since the *apply* backend drops the original information about the rebased commits and their parents (and instead generates new fake commits based off limited information in the generated patches), those commits cannot be identified; instead it has to fall back to a commit summary. Also, when `merge.conflictStyle` is set to `diff3` or `zdiff3`, the *apply* backend will use "constructed merge base" to label the content from the merge base, and thus provide no information about the merge base commit whatsoever.

The *merge* backend works with the full commits on both sides of history and thus has no such limitations.

### Hooks

The *apply* backend has not traditionally called the post-commit hook, while the *merge* backend has. Both have called the post-checkout hook, though the *merge* backend has squelched its output. Further, both backends only call the post-checkout hook with the starting point commit of the rebase, not the intermediate commits nor the final commit. In each case, the calling of these hooks was by accident of implementation rather than by design (both backends were originally implemented as shell scripts and happened to invoke other commands like `git` `checkout` or `git` `commit` that would call the hooks). Both backends should have the same behavior, though it is not entirely clear which, if any, is correct. We will likely make rebase stop calling either of these hooks in the future.

### Interruptability

The *apply* backend has safety problems with an ill-timed interrupt; if the user presses Ctrl-C at the wrong time to try to abort the rebase, the rebase can enter a state where it cannot be aborted with a subsequent `git` `rebase` `--abort`. The *merge* backend does not appear to suffer from the same shortcoming. (See https://lore.kernel.org/git/20200207132152.GC2868@szeder.dev/ for details.)

### Commit Rewording

When a conflict occurs while rebasing, rebase stops and asks the user to resolve. Since the user may need to make notable changes while resolving conflicts, after conflicts are resolved and the user has run `git` `rebase` `--continue`, the rebase should open an editor and ask the user to update the commit message. The *merge* backend does this, while the *apply* backend blindly applies the original commit message.

### Miscellaneous differences

There are a few more behavioral differences that most folks would probably consider inconsequential but which are mentioned for completeness:

- Reflog: The two backends will use different wording when describing the changes made in the reflog, though both will make use of the word "rebase".
- Progress, informational, and error messages: The two backends provide slightly different progress and informational messages. Also, the apply backend writes error messages (such as "Your files would be overwritten…") to stdout, while the merge backend writes them to stderr.
- State directories: The two backends keep their state in different directories under `.git/`

## MERGE STRATEGIES

The merge mechanism (`git` `merge` and `git` `pull` commands) allows the backend *merge strategies* to be chosen with `-s` option. Some strategies can also take their own options, which can be passed by giving `-X`*<option>* arguments to `git` `merge` and/or `git` `pull`.

**`ort`**

This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym ("Ostensibly Recursive’s Twin") and came from the fact that it was written as a replacement for the previous default algorithm, `recursive`.

In the case where the path is a submodule, if the submodule commit used on one side of the merge is a descendant of the submodule commit used on the other side of the merge, Git attempts to fast-forward to the descendant. Otherwise, Git will treat this case as a conflict, suggesting as a resolution a submodule commit that is descendant of the conflicting ones, if one exists.

The `ort` strategy can take the following options:

**`ours`**

This option forces conflicting hunks to be auto-resolved cleanly by favoring *our* version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side.

This should not be confused with the `ours` merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring *our* history contains all that happened in it.

**`theirs`**

This is the opposite of `ours`; note that, unlike `ours`, there is no `theirs` merge strategy to confuse this merge option with.

**`ignore-space-change`**

**`ignore-all-space`**

**`ignore-space-at-eol`**

**`ignore-cr-at-eol`**

Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also git-diff[1] `-b`, `-w`, `--ignore-space-at-eol`, and `--ignore-cr-at-eol`.

- If *their* version only introduces whitespace changes to a line, *our* version is used;
- If *our* version introduces whitespace changes but *their* version includes a substantial change, *their* version is used;
- Otherwise, the merge proceeds in the usual way.

**`renormalize`**

This runs a virtual check-out and check-in of all three stages of any file which needs a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See "Merging branches with differing checkin/checkout attributes" in gitattributes[5] for details.

**`no-renormalize`**

Disables the `renormalize` option. This overrides the `merge.renormalize` configuration variable.

**`find-renames`[`=`*<n>*]**

Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the `merge.renames` configuration variable. See also git-diff[1] `--find-renames`.

**`rename-threshold=`*<n>***

Deprecated synonym for `find-renames=`*<n>*.

**`no-renames`**

Turn off rename detection. This overrides the `merge.renames` configuration variable. See also git-diff[1] `--no-renames`.

**`histogram`**

Deprecated synonym for `diff-algorithm=histogram`.

**`patience`**

Deprecated synonym for `diff-algorithm=patience`.

**`diff-algorithm=`(`histogram`|`minimal`|`myers`|`patience`)**

Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also git-diff[1] `--diff-algorithm`. Note that `ort` defaults to `diff-algorithm=histogram`, while regular diffs currently default to the `diff.algorithm` config setting.

**`subtree`[`=`*<path>*]**

This option is a more advanced form of *subtree* strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match.

**`recursive`**

This is now a synonym for `ort`. It was an alternative implementation until v2.49.0, but was redirected to mean `ort` in v2.50.0. The previous recursive strategy was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0.

**`resolve`**

This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames.

**`octopus`**

This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch.

**`ours`**

This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the `-Xours` option to the `ort` merge strategy.

**`subtree`**

This is a modified `ort` strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.

With the strategies that use 3-way merge (including the default, `ort`), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.
