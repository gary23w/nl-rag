---
title: "Repository (version control)"
source: https://en.wikipedia.org/wiki/Repository_(version_control)
domain: subversion
license: CC-BY-SA-4.0
tags: subversion svn, centralized version control, apache subversion, revision repository
fetched: 2026-07-02
---

# Repository (version control)

In version control systems, a **repository** is a data structure that stores metadata for a set of files or directory structure. Depending on whether the version control system in use is distributed, like Git or Mercurial, or centralized, like Subversion, CVS, or Perforce, the whole set of information in the repository may be duplicated on every user's system or may be maintained on a single server. Some of the metadata that a repository contains includes, among other things, a historical record of changes in the repository, a set of commit objects, and a set of references to commit objects, called *heads*.

The main purpose of a repository is to store a set of files, as well as the history of changes made to those files. Exactly how each version control system handles storing those changes, however, differs greatly. For instance, Subversion in the past relied on a database instance but has since moved to storing its changes directly on the filesystem. These differences in storage techniques have generally led to diverse uses of version control by different groups, depending on their needs.

## Overview

In software engineering, a version control system is used to keep track of versions of a set of files, usually to allow multiple developers to collaborate on a project. The repository keeps track of the files in the project, which is represented as a graph.

A distributed version control system is made up of central and branch repositories. A central repository exists on the server. To make changes to it, a developer first works on a branch repository, and proceeds to commit the change to the former.

## Forges

A code forge is a web interface to a version control system. A user can commonly browse repositories and their constituent files on the page itself.

### Static web hosting

While forges are mainly used to perform version control operations, some forges allow users to host static web pages by uploading its source code (such as HTML and JavaScript, but not PHP) to a repository. This is usually done in order to provide documentation or a landing page for a software project.

The use of repositories as a place to upload web documents allows version control to be integrated, and additionally allows quick iteration because changes are pushed through the Version Control System instead of having to upload the file through a protocol like FTP.

Examples of this kind of service include Codeberg Pages, GitHub Pages and GitLab Pages.
