---
title: "UnderstandingMercurial"
source: https://www.mercurial-scm.org/wiki/UnderstandingMercurial
domain: mercurial-vcs
license: CC-BY-SA-4.0
tags: mercurial vcs, distributed version control, hg repository, changeset history
fetched: 2026-07-02
---

# UnderstandingMercurial

Understanding Mercurial

Mercurial's decentralized development model can be confusing to new users. This page attempts to illustrate some of the basic concepts. See the Tutorial for step-by-step instructions.

1. What's in a repository

Mercurial repositories contain a working directory coupled with a store:

The store contains the **complete** history of the project. Unlike traditional SCMs, where there's only one central copy of this history, every working directory is paired with a private copy of the history. This allows development to go on in parallel.

The working directory contains a copy of the project's files at a given point in time (eg rev 2), ready for editing. Because tags and ignored files are revision-controlled, they are also included.

2. Committing changes

When you commit, the state of the working directory relative to its parents is recorded as a new changeset (also called a new "revision"):

Note here that revision 4 is a **branch** of revision 2, which was the revision in the working directory. Now revision 4 is the working directory's **parent**.

3. Revisions, changesets, heads, and tip

Mercurial groups related changes to multiple files into single atomic changesets, which are revisions of the whole project. These each get a sequential revision number. Because Mercurial allows distributed parallel development, these revision numbers may disagree between users. So Mercurial also assigns each revision a global changeset ID. Changeset IDs are 40-digit hexadecimal numbers, but they can be abbreviated to any unambiguous prefix, like "e38487".

Branches and merges in the revision history can occur at any point. Each unmerged branch creates a new head of the revision history. Here, revisions 5 and 6 are heads. Mercurial considers revision 6 to be the tip of the repository, the head with the highest revision number. Revision 4 is a merge changeset, as it has *two* parent changesets (revisions 2 and 3).

4. Cloning, making changes, merging, pulling and updating

Let's start with a user Alice, who has a repository that looks like:

Bob clones this repo, and ends up with a complete, independent, local copy of Alice's store and a clean checkout of the tipmost revision d in his working directory:

Bob can now work independently of Alice. He then commits two changes e and f:

Alice then makes her own change g in parallel, which causes her repository store to diverge from Bob's, thus creating a branch:

Bob then pulls Alice's repo to synchronize. This copies all of Alice's changes into Bob's repository store (here, it's just a single change g). Note that Bob's working directory is **not** changed by the pull:

Because Alice's **g** is the newest head in Bob's repository, it's now the **tip**.

Bob then does a merge, which combines the last change he was working on (f) with the tip in his repository. Now, his working directory has two parent revisions (f and g):

After examining the result of the merge in his working directory and making sure the merge is perfect, Bob commits the result and ends up with a new merge changeset h in his store:

Now if Alice **pulls** from Bob, she will get Bob's changes e, f, and h into her store:

Note that Alice's working directory was not changed by the pull. She has to do an update to synchronize her working directory to the merge changset h. This changes the parent changeset of her working directory to changeset h and updates the files in her working directory to revision h.

Now Alice and Bob are fully synchronized again.

5. A decentralized system

Mercurial is a completely decentralized system, and thus has no internal notion of a central repository. Thus users are free to define their own topologies for sharing changes (see CommunicatingChanges):

Unlike a centralized version control system in which experimentation can be disastrous, with a DVCS like Mercurial, you just clone and experiment. If you like the results, push them back, otherwise wipe the cloned repository and try something else.

6. What Mercurial can't do

Many SVN/CVS users expect to host related projects together in one repository. This is really not what Mercurial was made for, so you should try a different way of working. In particular, this means that you cannot check out only one directory of a repository.

If you absolutely need to host multiple projects in a kind of meta-repository though, you could try the Subrepositories feature that was introduced with Mercurial 1.3 or the older ForestExtension.

For a hands-on introduction to using Mercurial, see the Tutorial.

Brazilian Portuguese, Czech, Deutsch, Français, Italiano, Russian, Spanish, Thai, 中文, 日本語, 한국어
