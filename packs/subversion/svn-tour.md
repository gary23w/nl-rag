---
title: "Chapter 2. Basic Usage"
source: https://svnbook.red-bean.com/en/1.7/svn.tour.html
domain: subversion
license: CC-BY-SA-4.0
tags: subversion svn, centralized version control, apache subversion, revision repository
fetched: 2026-07-02
---

# Chapter 2. Basic Usage

This documentation was written to describe the 1.7.x series of Apache™ Subversion®. If you are running a different version of Subversion, you are strongly encouraged to visit http://www.svnbook.com/ and instead consult the version of this documentation appropriate for your version of Subversion.

| Chapter 2. Basic Usage |   |   |
|---|---|---|
| Prev |   | Next |

# Chapter 2. Basic Usage

**Table of Contents**

**Help!**

**Getting Data into Your Repository**

**Importing Files and Directories**

**Recommended Repository Layout**

**What's In a Name?**

**Creating a Working Copy**

**Basic Work Cycle**

**Update Your Working Copy**

**Make Your Changes**

**Review Your Changes**

**See an overview of your changes**

**Examine the details of your local modifications**

**Fix Your Mistakes**

**Resolve Any Conflicts**

**Viewing conflict differences interactively**

**Resolving conflict differences interactively**

**Postponing conflict resolution**

**Merging conflicts by hand**

**Discarding your changes in favor of a newly fetched revision**

**Punting: using svn revert**

**Commit Your Changes**

**Examining History**

**Examining the Details of Historical Changes**

**Examining local changes**

**Comparing working copy to repository**

**Comparing repository revisions**

**Generating a List of Historical Changes**

**Browsing the Repository**

**Displaying file contents**

**Displaying line-by-line change attribution**

**Listing versioned directories**

**Fetching Older Repository Snapshots**

**Sometimes You Just Need to Clean Up**

**Disposing of a Working Copy**

**Recovering from an Interruption**

**Dealing with Structural Conflicts**

**An Example Tree Conflict**

**Summary**

Theory is useful, but its application is just plain fun. Let's move now into the details of using Subversion. By the time you reach the end of this chapter, you will be able to perform all the tasks you need to use Subversion in a normal day's work. You'll start with getting your files into Subversion, followed by an initial checkout of your code. We'll then walk you through making changes and examining those changes. You'll also see how to bring changes made by others into your working copy, examine them, and work through any conflicts that might arise.

This chapter will not provide exhaustive coverage of all of Subversion's commands—rather, it's a conversational introduction to the most common Subversion tasks that you'll encounter. This chapter assumes that you've read and understood Chapter 1, *Fundamental Concepts* and are familiar with the general model of Subversion. For a complete reference of all commands, see Chapter 9, *Subversion Complete Reference*.

Also, this chapter assumes that the reader is seeking information about how to interact in a basic fashion with an existing Subversion repository. No repository means no working copy; no working copy means not much of interest in this chapter. There are many Internet sites which offer free or inexpensive Subversion repository hosting services. Or, if you'd prefer to set up and administer your own repositories, check out Chapter 5, *Repository Administration*. But don't expect the examples in this chapter to work without the user having access to a Subversion repository.

Finally, any Subversion operation that contacts the repository over a network may potentially require that the user authenticate. For the sake of simplicity, our examples throughout this chapter avoid demonstrating and discussing authentication. Be aware that if you hope to apply the knowledge herein to an existing, real-world Subversion instance, you'll probably be forced to provide at least a username and password to the server. See the section called “Client Credentials” for a detailed description of Subversion's handling of authentication and client credentials.

| Prev |   | Next |
|---|---|---|
| Summary | Home | Help! |
