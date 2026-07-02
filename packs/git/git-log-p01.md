---
title: "Git - git-log Documentation (part 1/4)"
source: https://git-scm.com/docs/git-log
domain: git
license: GPL-2.0
tags: git, merge conflict, version control
fetched: 2026-07-02
part: 1/4
---

# Git - git-log Documentation

English ▾

Localized versions of

git-log

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

git-log last updated in 2.55.0

Changes in the

git-log

manual

1. 2.55.0 *2026-06-29*
2. 2.54.0 *2026-04-20*
3. 2.53.0 *2026-02-02*
4. 2.52.0 *2025-11-17*
5. 2.51.2 no changes
6. 2.51.1 *2025-10-15*
7. 2.51.0 *2025-08-18*
8. 2.50.1 no changes
9. 2.50.0 *2025-06-16*
10. 2.49.1 no changes
11. 2.49.0 *2025-03-14*
12. 2.48.1 → 2.48.2 no changes
13. 2.48.0 *2025-01-10*
14. 2.46.1 → 2.47.3 no changes
15. 2.46.0 *2024-07-29*
16. 2.45.4 no changes
17. 2.45.3 *2024-11-26*
18. 2.45.1 → 2.45.2 no changes
19. 2.45.0 *2024-04-29*
20. 2.44.1 → 2.44.4 no changes
21. 2.44.0 *2024-02-23*
22. 2.43.3 → 2.43.7 no changes
23. 2.43.2 *2024-02-13*
24. 2.43.1 no changes
25. 2.43.0 *2023-11-20*
26. 2.42.2 → 2.42.4 no changes
27. 2.42.1 *2023-11-02*
28. 2.42.0 *2023-08-21*
29. 2.41.1 → 2.41.3 no changes
30. 2.41.0 *2023-06-01*
31. 2.40.1 → 2.40.4 no changes
32. 2.40.0 *2023-03-12*
33. 2.39.1 → 2.39.5 no changes
34. 2.39.0 *2022-12-12*
35. 2.38.3 → 2.38.5 no changes
36. 2.38.2 *2022-12-11*
37. 2.38.1 no changes
38. 2.38.0 *2022-10-02*
39. 2.37.1 → 2.37.7 no changes
40. 2.37.0 *2022-06-27*
41. 2.36.1 → 2.36.6 no changes
42. 2.36.0 *2022-04-18*
43. 2.35.1 → 2.35.8 no changes
44. 2.35.0 *2022-01-24*
45. 2.33.3 → 2.34.8 no changes
46. 2.33.2 *2022-03-23*
47. 2.33.1 *2021-10-12*
48. 2.33.0 *2021-08-16*
49. 2.32.1 → 2.32.7 no changes
50. 2.32.0 *2021-06-06*
51. 2.31.1 → 2.31.8 no changes
52. 2.31.0 *2021-03-15*
53. 2.30.1 → 2.30.9 no changes
54. 2.30.0 *2020-12-27*
55. 2.29.1 → 2.29.3 no changes
56. 2.29.0 *2020-10-19*
57. 2.28.1 no changes
58. 2.28.0 *2020-07-27*
59. 2.27.1 no changes
60. 2.27.0 *2020-06-01*
61. 2.26.1 → 2.26.3 no changes
62. 2.26.0 *2020-03-22*
63. 2.25.2 → 2.25.5 no changes
64. 2.25.1 *2020-02-17*
65. 2.25.0 *2020-01-13*
66. 2.24.1 → 2.24.4 no changes
67. 2.24.0 *2019-11-04*
68. 2.23.1 → 2.23.4 no changes
69. 2.23.0 *2019-08-16*
70. 2.22.1 → 2.22.5 no changes
71. 2.22.0 *2019-06-07*
72. 2.21.1 → 2.21.4 no changes
73. 2.21.0 *2019-02-24*
74. 2.20.1 → 2.20.5 no changes
75. 2.20.0 *2018-12-09*
76. 2.19.3 → 2.19.6 no changes
77. 2.19.2 *2018-11-21*
78. 2.19.1 no changes
79. 2.19.0 *2018-09-10*
80. 2.18.1 → 2.18.5 no changes
81. 2.18.0 *2018-06-21*
82. 2.17.1 → 2.17.6 no changes
83. 2.17.0 *2018-04-02*
84. 2.16.6 *2019-12-06*
85. 2.15.4 *2019-12-06*
86. 2.14.6 *2019-12-06*
87. 2.13.7 *2018-05-22*
88. 2.12.5 *2017-09-22*
89. 2.11.4 *2017-09-22*
90. 2.10.5 *2017-09-22*
91. 2.9.5 *2017-07-30*
92. 2.8.6 *2017-07-30*
93. 2.7.6 *2017-07-30*
94. 2.6.7 *2017-05-05*
95. 2.5.6 *2017-05-05*
96. 2.4.12 *2017-05-05*
97. 2.3.10 *2015-09-28*
98. 2.2.3 *2015-09-04*
99. 2.1.4 *2014-12-17*
100. 2.0.5 *2014-12-17*


## NAME

git-log - Show commit logs


## SYNOPSIS

git log [<options>] [<revision-range>] [[--] <path>…]


## DESCRIPTION

Shows the commit logs.

List commits that are reachable by following the `parent` links from the given commit(s), but exclude commits that are reachable from the one(s) given with a *^* in front of them. The output is given in reverse chronological order by default.

You can think of this as a set operation. Commits reachable from any of the commits given on the command line form a set, and then commits reachable from any of the ones given with *^* in front are subtracted from that set. The remaining commits are what comes out in the command’s output. Various other options and paths parameters can be used to further limit the result.

Thus, the following command:

$ git log foo bar ^baz

means "list all the commits which are reachable from *foo* or *bar*, but not from *baz*".

A special notation "*<commit1>*`..`*<commit2>*" can be used as a short-hand for "`^`*<commit1>* *<commit2>*". For example, either of the following may be used interchangeably:

$ git log origin..HEAD
$ git log HEAD ^origin

Another special notation is "*<commit1>*`...`*<commit2>*" which is useful for merges. The resulting set of commits is the symmetric difference between the two operands. The following two commands are equivalent:

$ git log A B --not $(git merge-base --all A B)
$ git log A...B

The command takes options applicable to the git-rev-list[1] command to control what is shown and how, and options applicable to the git-diff[1] command to control how the changes each commit introduces are shown.
