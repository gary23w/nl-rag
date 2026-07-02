---
title: "Tutorial"
source: https://www.mercurial-scm.org/wiki/Tutorial
domain: mercurial-vcs
license: CC-BY-SA-4.0
tags: mercurial vcs, distributed version control, hg repository, changeset history
fetched: 2026-07-02
---

# Tutorial

A Tutorial on Using Mercurial

This tutorial is an introduction to using Mercurial. We don't assume any particular background in using SCM software.

({i}) You might first want to read UnderstandingMercurial

1. Introduction

After you work through this tutorial, you should have a grasp of the following: The basic concepts and commands you'll need to use Mercurial How to use Mercurial in simple ways to contribute to a software project

It is also strongly recommended that you have a look at the Mercurial man pages hg(1) and hgrc(5), which are also available in the release tarballs as doc/hg.1.html and doc/hgrc.5.html. You can also use hg help <command> on the command line.

The tutorial is split into the following pages: TutorialInstall - installing Mercurial TutorialInit - Initialize a repository TutorialClone - making a copy of an existing repository TutorialHistory - navigating the history of a repository TutorialFirstChange - making your first change TutorialShareChange - sharing changes with another repository TutorialExport - sharing changes with another person TutorialMerge - handling multiple independent changes to a file TutorialConflict - handling merges that need manual resolution TutorialConclusion - the end

2. How to read this tutorial

The formatting convention is simple. Command names and parameters are displayed in fixed font.

A line of input that you should type into your shell or command prompt is displayed in a fixed font, and the line will start with a $ character.

A line of output that you should expect Mercurial or your shell to display is displayed in a fixed font, but with no special character at the start of the line.

$ this is a line of user input this is a line of program output

We use the bash shell in all examples. The concepts remain the same for other Unix shells and the Windows cmd.exe, but the syntax of some operations may change. For example, ls in a Unix shell is roughly equivalent to dir under Windows, and Unix vi is similar to Windows edit.

Now, let's begin with TutorialInstall.

3. See also Understanding Mercurial - a graphical explanation of some Mercurial basics Beginner's Guides http://mercurial.aragost.com/kick-start/ - A set of exercises for getting started with Mercurial by Martin Geisler http://hginit.com/ - A tutorial by Joel Spolsky

CategoryTutorial

Chinese, Czech, French, German, Italian, Japanese, Korean, Lithuanian, Português do Brasil, Spanish, Russian, Ukrainian, Thai
