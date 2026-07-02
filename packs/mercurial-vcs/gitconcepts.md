---
title: "GitConcepts"
source: https://www.mercurial-scm.org/wiki/GitConcepts
domain: mercurial-vcs
license: CC-BY-SA-4.0
tags: mercurial vcs, distributed version control, hg repository, changeset history
fetched: 2026-07-02
---

# GitConcepts

Mercurial for Git users

Git is a very popular DistributedSCM that works very similarly to Mercurial. Both are built upon such similar concepts that most repositories can be converted to and from Mercurial and Git without any significant data loss! There are, however, significant design and conceptual differences that may cause trouble when coming from Git to Mercurial.

1. High-level Comparison

Mercurial and Git differ mainly in nomenclature, interface, and - of course - implementation details, including features.

Mercurial has always focused heavily on interface aspects. This makes Mercurial easier to learn - even for someone who has never used version control before. Git tends to expose lower-level implementation details to users, requiring knowledge of them in order to use Git effectively (e.g. refs). In comparison to Git, Mercurial requires a shallower understanding to operate in a useful manner.

Mercurial is also safer by default: functionality like history rewriting (which is considered an advanced topic for a version control newcomer) must be enabled. To Mercurial newcomers with Git experience, this often gives the false appearance that Mercurial is less powerful or featureful than it really is.

2. Logical architecture

This section tries to prove that the only logical architecture difference between the two systems, is nomenclature.

2.1. History model

One of the first Git lessons is the repository basic object types: blob, tree and commit. These are the building blocks for the history model. Mercurial also builds up history upon the same three concepts, respectively: file, manifest and changeset.

To identify these objects both systems use a SHA1 hash value, what Mercurial calls nodeid. Additionally, Mercurial also provides a **local** revision number, a simply incrementing integer, for each changeset, in addition to the reverse count notation provided by Git (like HEAD~4). (Mercurial also includes a powerful query language for specifying revisions called revsets.)

From that, Mercurial's view of history is, just like Git's, a DAG or Directed Acyclic Graph of changesets. For instance, the graphical representation of history is the same in the two.

2.2. Branch model

Also like in Git, Mercurial supports branching in different ways. First and foremost, each clone of a repository represents a branch, potentially identical to other clones of the same repositories. This way of branching is sometimes referred to as *heavy branches* and works almost the same in both systems.

Then Git has its famous *lightweight branches*, which allow switching between development lines within the same clone of a repository. Take the following history graph as an example:

In Git, branches X and Y are simply references to the e and g commits. If a new commit is appended to e then the reference X would point to such commit, like this:

In Mercurial, the X and Y branches are called *heads* and they can be referred by their changeset identifier: either local (number) or global (SHA1 hash). In brief, it is like using Git detached heads instead of branch names, but much easier and without the risk of garbage collection (see hg help heads). They can be referred also by a bookmark, which can be pushed and pulled with the -B/--bookmark option.

Finally, Mercurial has another branching functionality called NamedBranches, also known as long lived branches. This kind of branch does not have a Git equivalent. For more information about named branches: Branch NamedBranches MultipleHeads

2.3. Tag model

Like with branches both Git and Mercurial support two tag levels: *local* and *global*. Local tags are only visible where they were created and do not propagate, so they behave practically the same in both systems.

Global tags is one of the aspects that really differs from Git. Apparently they serve the same purpose, however they are treated differently. In Git, global tags have a dedicated repository object type; these tags are usually referred as *annotated tags*. In Mercurial, though, they are stored in a special text file called .hgtags residing in the root directory of a repository clone. Because the .hgtags file is versioned as a normal file, all the file modifications are stored as part of the repository history.

Two important things need to be remembered about how .hgtags is handled: The file only grows and should not be edited, except when it generates a merge conflict. Because it is revision controlled, there is a corresponding revlog. When looking for tags, only the latest revision of .hgtags is parsed; never mind the checked out copy revision.

Although it is questioned by many people new to Mercurial, this design allows to keep track of all global tagging operations. Nevertheless, it also confuses because it can lead to some puzzling scenarios. For example, consider the following history graph:

In the graph, T is a global tag pointing to changeset c. This tagging action generated changeset d because .hgtags had to be committed. Now, if you clone a new repository using hg clone --rev T, the history graph of the cloned repository would look like this:

Therefore, in the new repository tag T does not exist. The reason behind this is because in the original repository tag T points to changeset c; however, tag T is added by commit d which is a descendant of c. As the clone command limits the history up to changeset c, the addition of the tag is not included in the new repository. Things work similarly when tagging a particular revision using hg tag --rev ...

Regarding tag propagation across repositories, Mercurial has very simple semantics. From the history and WireProtocol point of view, the .hgtags file is treated like the rest of the tracked files, which means that any global tagging operation becomes visible to everyone just like any other commit. It also implies that merge conflicts can occur in .hgtags.

The rationale behind Mercurial's global tags is briefly justified in this thread (January 2009).

See also: Giving a persistent name to a revision.

3. Behavioral differences

In most design decisions, Mercurial tries to avoid exposing excessive complexity to the user. This can sometimes lead to the belief that both systems have nothing in common when in practice the difference is subtle, and vice versa. The main difference is that mercurial does not offer an "undo" to what you did without using commands that are referred to as "dangerous", "not what you want" etc in the help pages.

3.1. Communication between repositories

While the branching model is very similar, moving history between different repositories is slightly mismatched.

Git adds the notion of *tracking branch*, a branch that is used to follow changes from another repository. Tracking branches allow to selectively pull or push branches from or to a remote repository.

Mercurial keeps things simpler in this aspect: When you pull, you bring all remote heads into your local repository. Then you can decide whether to merge or not. Or else, pull and merge automatically using "-u". All pushes that would create new heads (i.e. lightweight branches) stop with a warning, except if the user explicitly forces them.

3.2. Git's staging area

Git is the only DistributedSCM that exposes the concept of *index* or *staging area*. The others may implement and hide it, but in no other case is the user aware or has to deal with it.

Mercurial's rough equivalent is the DirState, which controls working copy status information to determine the files to be included in the next commit. But in any case, this file is handled automatically. Additionally, it is possible to be more selective at commit time either by specifying the files you want to commit on the command line or by using hg commit --interactive.

If you felt uncomfortable dealing with Git's index, you are switching for the better. (;-))

If you need the index, you can gain its behavior (with many additional options) with mercurial queues (MQ). Simple addition of changes to the index can be imitated by just building up a commit with hg commit --amend (optionally with --secret, see phases).

3.3. Bare repositories

Although this is a minor issue, Mercurial can obviously handle a *bare* repository; that is, a repository **without** a working copy. In Git you need a configuration option for that, whereas in Hg you only need to check out the null revision, like this:

hg update null  As push and pull operations do not update the working copy by default, by not updating the working copy you get the same effect of a bare repository. In fact, it is the recommended option for some particular hgwebdir.cgi setups.

4. Command equivalence table

The table presented below is far from being complete due to the large amount of command and switch combinations that Git offers. Nevertheless, it tries to cover the most shocking changes when moving from Git to Hg: **Git command** **Hg command** **Notes** git pull hg fetch hg pull -u The fetch command is more similar but requires the FetchExtension to be enabled. git fetch hg pull git push hg push -r . By default, git only pushes the current branch. git checkout <commit> hg update -c <cset> git checks and reloads (accidentally) removed files git checkout [<rev>] -- <file(s)> hg revert [-r <rev>] <file(s)> git reset --hard hg revert -a --no-backup git reset --hard HEAD~1 hg strip -r . git revert <commit> hg backout <cset> git add <new_file> hg add <new_file> Only equivalent when <new_file> is not tracked. git add <file> git reset HEAD <file> — Not necessary in Mercurial (see shelve below for partial commit support). git add -i git add -p hg record hg commit -i Requires the RecordExtension to be enabled. Interactive mode has been added to commit in 3.4. git commit --amend hg commit --amend git rebase --interactive hg histedit <base cset> Requires the HisteditExtension. In core since version 2.3 git stash hg shelve Requires the ShelveExtension or the AtticExtension. git merge hg merge git merge is capable of octopus merges, while mercurial merge prefers multiple merges git cherry-pick <commit> hg transplant <cset> hg graft <csets> Transplant requires the TransplantExtension. Graft is available in 2.0 and higher. git rebase <upstream> hg rebase -d <cset> Requires the RebaseExtension. git format-patch <commits> and git send-mail hg email -r <csets> Requires the PatchbombExtension. git am <mbox> hg mimport -m <mbox> Requires the MboxExtension and the MqExtension. Imports patches to mq. git describe hg log -r . --template '{latesttag}-{latesttagdistance}-{node|short}\n' git describe rev hg log -r rev --template '{latesttag}-{latesttagdistance}-{node|short}\n' git log origin..HEAD git log origin/foobranch..HEAD hg outgoing git fetch && git log HEAD..origin hg incoming git fetch keeps the changesets while hg incoming (without --bundle foo) discards them. Use git pull (will fetch further changes) or git merge origin to update the working directory git show rev hg export rev hg log -pvr rev git rev-parse HEAD hg identify git ls-remote <url> HEAD hg identify <url> git show hash:file hg cat -r rev file git ls-files hg manifest git log hg log git log -n hg log --limit n git log --graph hg glog hg log --graph Requires the GraphlogExtension. log supports --graph without the extension since version 2.3 git ?? hg summary git status hg outgoing hg status git remote add -f remotename url — Edit .hg/hgrc and add the line 'remotename = url' under section '[paths]'; see below for getting changesets git remote update remotename hg pull remotename When remotename is omitted in Git, all remotes are updated. In Mercurial, the default remote is refreshed. git branch -a hg branches git config --global user.(name|email) ... — Edit ~/.hgrc section "[ui]", key "username", value "First Last < mail@example.org >" git clean or git status --porcelain|sed -r 's:\?\?\s(.*):\1:g'|xargs rm hg purge or hg status -un|xargs rm purge requires the PurgeExtension In Windows you might need to add sed 's:\\:/:g' before piping xargs rm, otherwise the inverted slash in Windows paths will be interpreted as an escape git merge-base rev1 rev2 hg log -r 'last(ancestors(rev1) and ancestors(rev2))' git merge-base --is-ancestor rev1 rev2 && echo yes hg log -r 'descendants(rev1) and rev2' -T yes git tag --contains rev hg log -r 'ancestors(rev) and tag()' -T "{join(tags, '\n')}\n"

While the output of git commands often gives hints as to which commands one could use next, hg does this only in rare cases.
