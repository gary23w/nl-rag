---
title: "Chapter 4. Branching and Merging"
source: https://svnbook.red-bean.com/en/1.7/svn.branchmerge.html
domain: subversion
license: CC-BY-SA-4.0
tags: subversion svn, centralized version control, apache subversion, revision repository
fetched: 2026-07-02
---

# Chapter 4. Branching and Merging

This documentation was written to describe the 1.7.x series of Apache™ Subversion®. If you are running a different version of Subversion, you are strongly encouraged to visit http://www.svnbook.com/ and instead consult the version of this documentation appropriate for your version of Subversion.

| Chapter 4. Branching and Merging |   |   |
|---|---|---|
| Prev |   | Next |

# Chapter 4. Branching and Merging

**Table of Contents**

**What's a Branch?**

**Using Branches**

**Creating a Branch**

**Working with Your Branch**

**The Key Concepts Behind Branching**

**Basic Merging**

**Changesets**

**Keeping a Branch in Sync**

**Subtree Merges and Subtree Mergeinfo**

**Reintegrating a Branch**

**Mergeinfo and Previews**

**Undoing Changes**

**Resurrecting Deleted Items**

**Advanced Merging**

**Cherrypicking**

**Merge Syntax: Full Disclosure**

**Merges Without Mergeinfo**

**More on Merge Conflicts**

**Blocking Changes**

**Keeping a Reintegrated Branch Alive**

**Merge-Sensitive Logs and Annotations**

**Noticing or Ignoring Ancestry**

**Merges and Moves**

**Preventing Naïve Clients from Committing Merges**

**The Final Word on Merge Tracking**

**Traversing Branches**

**Tags**

**Creating a Simple Tag**

**Creating a Complex Tag**

**Branch Maintenance**

**Repository Layout**

**Data Lifetimes**

**Common Branching Patterns**

**Release Branches**

**Feature Branches**

**Vendor Branches**

**General Vendor Branch Management Procedure**

**svn_load_dirs.pl**

**To Branch or Not to Branch?**

**Summary**

|   | “君子务本 (It is upon the Trunk that a gentleman works.)” |   |
|---|---|---|
|   | --Confucius |   |

Branching and merging are fundamental aspects of version control, simple enough to explain conceptually but offering just enough complexity and nuance to merit their own chapter in this book. Herein, we'll introduce you to the general ideas behind these operations as well as Subversion's somewhat unique approach to them. If you've not familiarized yourself with Subversion's basic concepts (found in Chapter 1, *Fundamental Concepts*), we recommmend that you do so before reading this chapter.

| Prev |   | Next |
|---|---|---|
| Summary | Home | What's a Branch? |
