---
title: "Apache HBase® Reference Guide (part 38/41)"
source: https://hbase.apache.org/book.html
domain: apache-hbase
license: CC-BY-SA-4.0
tags: apache hbase, bigtable clone, wide-column store, apache hadoop
fetched: 2026-07-02
part: 38/41
---

## Appendix A: Contributing to Documentation

The Apache HBase project welcomes contributions to all aspects of the project, including the documentation.

In HBase, documentation includes the following areas, and probably some others:

- The HBase Reference Guide (this book)
- The HBase website
- API documentation
- Command-line utility output and help text
- Web UI strings, explicit help text, context-sensitive strings, and others
- Log messages
- Comments in source files, configuration files, and others
- Localization of any of the above into target languages other than English

No matter which area you want to help out with, the first step is almost always to download (typically by cloning the Git repository) and familiarize yourself with the HBase source code. For information on downloading and building the source, see developer.

### A.1. Contributing to Documentation or Other Strings

If you spot an error in a string in a UI, utility, script, log message, or elsewhere, or you think something could be made more clear, or you think text needs to be added where it doesn’t currently exist, the first step is to file a JIRA. Be sure to set the component to `Documentation` in addition to any other involved components. Most components have one or more default owners, who monitor new issues which come into those queues. Regardless of whether you feel able to fix the bug, you should still file bugs where you see them.

If you want to try your hand at fixing your newly-filed bug, assign it to yourself. You will need to clone the HBase Git repository to your local system and work on the issue there. When you have developed a potential fix, submit it for review. If it addresses the issue and is seen as an improvement, one of the HBase committers will commit it to one or more branches, as appropriate.

Procedure: Suggested Work flow for Submitting Patches

This procedure goes into more detail than Git pros will need, but is included in this appendix so that people unfamiliar with Git can feel confident contributing to HBase while they learn.

1. If you have not already done so, clone the Git repository locally. You only need to do this once.
2. Fairly often, pull remote changes into your local repository by using the `git pull` command, while your tracking branch is checked out.
3. For each issue you work on, create a new branch. One convention that works well for naming the branches is to name a given branch the same as the JIRA it relates to: `$ git checkout -b HBASE-123456`
4. Make your suggested changes on your branch, committing your changes to your local repository often. If you need to switch to working on a different issue, remember to check out the appropriate branch.
5. When you are ready to submit your patch, first be sure that HBase builds cleanly and behaves as expected in your modified branch.
6. If you have made documentation changes, be sure the documentation and website builds by running `mvn clean site`.
7. If it takes you several days or weeks to implement your fix, or you know that the area of the code you are working in has had a lot of changes lately, make sure you rebase your branch against the remote master and take care of any conflicts before submitting your patch. `$ git checkout HBASE-123456 $ git rebase origin/master`
8. Generate your patch against the remote master. Run the following command from the top level of your git repository (usually called `hbase`): `$ git format-patch --stdout origin/master > HBASE-123456.patch` The name of the patch should contain the JIRA ID.
9. Look over the patch file to be sure that you did not change any additional files by accident and that there are no other surprises.
10. When you are satisfied, attach the patch to the JIRA and click the **Patch Available** button. A reviewer will review your patch.
11. If you need to submit a new version of the patch, leave the old one on the JIRA and add a version number to the name of the new patch.
12. After a change has been committed, there is no need to keep your local branch around.

### A.2. Editing the HBase Website

The source for the HBase website is in the HBase source, in the *src/site/* directory. Within this directory, source for the individual pages is in the *xdocs/* directory, and images referenced in those pages are in the *resources/images/* directory. This directory also stores images used in the HBase Reference Guide.

The website’s pages are written in an HTML-like XML dialect called xdoc, which has a reference guide at https://maven.apache.org/archives/maven-1.x/plugins/xdoc/reference/xdocs.html. You can edit these files in a plain-text editor, an IDE, or an XML editor such as XML Mind XML Editor (XXE) or Oxygen XML Author.

To preview your changes, build the website using the `mvn clean site -DskipTests` command. The HTML output resides in the *target/site/* directory. When you are satisfied with your changes, follow the procedure in submit doc patch procedure to submit your patch.

### A.3. Publishing the HBase Website and Documentation

HBase uses the ASF’s `gitpubsub` mechanism. A Jenkins job runs the `dev-support/jenkins-scripts/generate-hbase-website.sh` script, which runs the `mvn clean site site:stage` against the `master` branch of the `hbase` repository and commits the built artifacts to the `asf-site` branch of the `hbase-site` repository. When the commit is pushed, the website is redeployed automatically. If the script encounters an error, an email is sent to the developer mailing list. You can run the script manually or examine it to see the steps involved.

### A.4. Checking the HBase Website for Broken Links

A Jenkins job runs periodically to check HBase website for broken links, using the `dev-support/jenkins-scripts/check-website-links.sh` script. This script uses a tool called `linklint` to check for bad links and create a report. If broken links are found, an email is sent to the developer mailing list. You can run the script manually or examine it to see the steps involved.

### A.5. HBase Reference Guide Style Guide and Cheat Sheet

The HBase Reference Guide is written in Asciidoc and built using AsciiDoctor. The following cheat sheet is included for your reference. More nuanced and comprehensive documentation is available at http://asciidoctor.org/docs/user-manual/.

| Element Type | Desired Rendering | How to do it |
|---|---|---|
| A paragraph | a paragraph | Just type some text with a blank line at the top and bottom. |
| Add line breaks within a paragraph without adding blank lines | Manual line breaks | This will break + at the plus sign. Or prefix the whole paragraph with a line containing '[%hardbreaks]' |
| Give a title to anything | Colored italic bold differently-sized text |   |
| In-Line Code or commands | monospace | `text` |
| In-line literal content (things to be typed exactly as shown) | bold mono | *`typethis`* |
| In-line replaceable content (things to substitute with your own values) | bold italic mono | *_typesomething_* |
| Code blocks with highlighting | monospace, highlighted, preserve space | [source,java] ---- myAwesomeCode() { } ---- |
| Code block included from a separate file | included just as though it were part of the main file | [source,ruby] ---- include\::path/to/app.rb[] ---- |
| Include only part of a separate file | Similar to Javadoc | See http://asciidoctor.org/docs/user-manual/#by-tagged-regions |
| Filenames, directory names, new terms | italic | _hbase-default.xml_ |
| External naked URLs | A link with the URL as link text | `link:http:` |
| External URLs with text | A link with arbitrary link text | `link:http:` |
| Create an internal anchor to cross-reference | not rendered | `[[anchor_name]]` |
| Cross-reference an existing anchor using its default title | an internal hyperlink using the element title if available, otherwise using the anchor name | `<<anchor_name>>` |
| Cross-reference an existing anchor using custom text | an internal hyperlink using arbitrary text | `<<anchor_name,Anchor Text>>` |
| A block image | The image with alt text | `image::sunset.jpg[Alt Text]` (put the image in the src/site/resources/images directory) |
| An inline image | The image with alt text, as part of the text flow | `image:sunset.jpg [Alt Text]` (only one colon) |
| Link to a remote image | show an image hosted elsewhere | `image::http:` (or `image:`) |
| Add dimensions or a URL to the image | depends | inside the brackets after the alt text, specify width, height and/or link="http://my_link.com" |
| A footnote | subscript link which takes you to the footnote | `Some text.footnote:[The footnote text.]` |
| A note or warning with no title | The admonition image followed by the admonition | `NOTE:My note here` `WARNING:My warning here` |
| A complex note | The note has a title and/or multiple paragraphs and/or code blocks or lists, etc | .The Title [NOTE] ==== Here is the note text. Everything until the second set of four equals signs is part of the note. ---- some source code ---- ==== |
| Bullet lists | bullet lists | `* list item 1` (see http://asciidoctor.org/docs/user-manual/#unordered-lists) |
| Numbered lists | numbered list | `. list item 2` (see http://asciidoctor.org/docs/user-manual/#ordered-lists) |
| Checklists | Checked or unchecked boxes | Checked: `- [*]` Unchecked: `- [ ]` |
| Multiple levels of lists | bulleted or numbered or combo | `. Numbered (1), at top level * Bullet (2), nested under 1 * Bullet (3), nested under 1 . Numbered (4), at top level * Bullet (5), nested under 4 ** Bullet (6), nested under 5 - [x] Checked (7), at top level` |
| Labelled lists / variablelists | a list item title or summary followed by content | `Title:: content Title:: content` |
| Sidebars, quotes, or other blocks of text | a block of text, formatted differently from the default | Delimited using different delimiters, see http://asciidoctor.org/docs/user-manual/#built-in-blocks-summary. Some of the examples above use delimiters like ...., ----,====. [example] ==== This is an example block. ==== [source] ---- This is a source block. ---- [note] ==== This is a note block. ==== [quote] ____ This is a quote block. ____ If you want to insert literal Asciidoc content that keeps being interpreted, when in doubt, use eight dots as the delimiter at the top and bottom. |
| Nested Sections | chapter, section, sub-section, etc | `= Book (or chapter if the chapter can be built alone, see the leveloffset info below) == Chapter (or section if the chapter is standalone) === Section (or subsection, etc) ==== Subsection` and so on up to 6 levels (think carefully about going deeper than 4 levels, maybe you can just titled paragraphs or lists instead). Note that you can include a book inside another book by adding the `:leveloffset:+1` macro directive directly before your include, and resetting it to 0 directly after. See the *book.adoc* source for examples, as this is how this guide handles chapters. **Don’t do it for prefaces, glossaries, appendixes, or other special types of chapters.** |
| Include one file from another | Content is included as though it were inline | `include::[/path/to/file.adoc]` For plenty of examples. see *book.adoc*. |
| A table | a table | See http://asciidoctor.org/docs/user-manual/#tables. Generally rows are separated by newlines and columns by pipes |
| Comment out a single line | A line is skipped during rendering | `+//+ This line won’t show up` |
| Comment out a block | A section of the file is skipped during rendering | `Nothing between the slashes will show up.` |
| Highlight text for review | text shows up with yellow background | `Test between #hash marks# is highlighted yellow.` |

### A.6. Auto-Generated Content

Some parts of the HBase Reference Guide, most notably config.files, are generated automatically, so that this area of the documentation stays in sync with the code. This is done by means of an XSLT transform, which you can examine in the source at *src/main/xslt/configuration_to_asciidoc_chapter.xsl*. This transforms the *hbase-common/src/main/resources/hbase-default.xml* file into an Asciidoc output which can be included in the Reference Guide.

Sometimes, it is necessary to add configuration parameters or modify their descriptions. Make the modifications to the source file, and they will be included in the Reference Guide when it is rebuilt.

It is possible that other types of content can and will be automatically generated from HBase source files in the future.

### A.7. Images in the HBase Reference Guide

You can include images in the HBase Reference Guide. It is important to include an image title if possible, and alternate text always. This allows screen readers to navigate to the image and also provides alternative text for the image. The following is an example of an image with a title and alternate text. Notice the double colon.

```
.My Image Title
image::sunset.jpg[Alt Text]
```

Here is an example of an inline image with alternate text. Notice the single colon. Inline images cannot have titles. They are generally small images like GUI buttons.

```
image:sunset.jpg[Alt Text]
```

When doing a local build, save the image to the *src/site/resources/images/* directory. When you link to the image, do not include the directory portion of the path. The image will be copied to the appropriate target location during the build of the output.

When you submit a patch which includes adding an image to the HBase Reference Guide, attach the image to the JIRA. If the committer asks where the image should be committed, it should go into the above directory.

### A.8. Adding a New Chapter to the HBase Reference Guide

If you want to add a new chapter to the HBase Reference Guide, the easiest way is to copy an existing chapter file, rename it, and change the ID (in double brackets) and title. Chapters are located in the *src/main/asciidoc/_chapters/* directory.

Delete the existing content and create the new content. Then open the *src/main/asciidoc/book.adoc* file, which is the main file for the HBase Reference Guide, and copy an existing `include` element to include your new chapter in the appropriate location. Be sure to add your new file to your Git repository before creating your patch.

When in doubt, check to see how other files have been included.

### A.9. Common Documentation Issues

The following documentation issues come up often. Some of these are preferences, but others can create mysterious build errors or other problems.

1. *Isolate Changes for Easy Diff Review.* Be careful with pretty-printing or re-formatting an entire XML file, even if the formatting has degraded over time. If you need to reformat a file, do that in a separate JIRA where you do not change any content. Be careful because some XML editors do a bulk-reformat when you open a new file, especially if you use GUI mode in the editor.
2. *Syntax Highlighting* The HBase Reference Guide uses `coderay` for syntax highlighting. To enable syntax highlighting for a given code listing, use the following type of syntax: [source,xml] ---- <name>My Name</name> ---- Several syntax types are supported. The most interesting ones for the HBase Reference Guide are `java`, `xml`, `sql`, and `bash`.


## Appendix B: FAQ

### B.1. General

**When should I use HBase?**

See Overview in the Architecture chapter.

**Does HBase support SQL?**

Not really. SQL-ish support for HBase via Hive is in development, however Hive is based on MapReduce which is not generally suitable for low-latency requests. See the Data Model section for examples on the HBase client.

**How can I find examples of NoSQL/HBase?**

See the link to the BigTable paper in Other Information About HBase, as well as the other papers.

**What is the history of HBase?**

See hbase.history.

**Why are the cells above 10MB not recommended for HBase?**

Large cells don’t fit well into HBase’s approach to buffering data. First, the large cells bypass the MemStoreLAB when they are written. Then, they cannot be cached in the L2 block cache during read operations. Instead, HBase has to allocate on-heap memory for them each time. This can have a significant impact on the garbage collector within the RegionServer process.

### B.2. Upgrading

**How do I upgrade Maven-managed projects from HBase 0.94 to HBase 0.96+?**

In HBase 0.96, the project moved to a modular structure. Adjust your project’s dependencies to rely upon the `hbase-client` module or another module as appropriate, rather than a single JAR. You can model your Maven dependency after one of the following, depending on your targeted version of HBase. See Section 3.5, “Upgrading from 0.94.x to 0.96.x” or Section 3.3, “Upgrading from 0.96.x to 0.98.x” for more information.

Maven Dependency for HBase 0.98

```
<dependency>
  <groupId>org.apache.hbase</groupId>
  <artifactId>hbase-client</artifactId>
  <version>0.98.5-hadoop2</version>
</dependency>
```

Maven Dependency for HBase 0.96

```
<dependency>
  <groupId>org.apache.hbase</groupId>
  <artifactId>hbase-client</artifactId>
  <version>0.96.2-hadoop2</version>
</dependency>
```

Maven Dependency for HBase 0.94

```
<dependency>
  <groupId>org.apache.hbase</groupId>
  <artifactId>hbase</artifactId>
  <version>0.94.3</version>
</dependency>
```

### B.3. Architecture

**How does HBase handle Region-RegionServer assignment and locality?**

See Regions.

### B.4. Configuration

**How can I get started with my first cluster?**

See Quick Start - Standalone HBase.

**Where can I learn about the rest of the configuration options?**

See Apache HBase Configuration.

### B.5. Schema Design / Data Access

**How should I design my schema in HBase?**

See Data Model and HBase and Schema Design.

**How can I store (fill in the blank) in HBase?**

See Supported Datatypes.

**How can I handle secondary indexes in HBase?**

See Secondary Indexes and Alternate Query Paths.

**Can I change a table’s rowkeys?**

This is a very common question. You can’t. See Immutability of Rowkeys.

**What APIs does HBase support?**

See Data Model, Client, and Apache HBase External APIs.

### B.6. MapReduce

**How can I use MapReduce with HBase?**

See HBase and MapReduce.

### B.7. Performance and Troubleshooting

**How can I improve HBase cluster performance?**

See Apache HBase Performance Tuning.

**How can I troubleshoot my HBase cluster?**

See Troubleshooting and Debugging Apache HBase.

### B.8. Amazon EC2

**I am running HBase on Amazon EC2 and…**

EC2 issues are a special case. See Amazon EC2 and Amazon EC2.

### B.9. Operations

**How do I manage my HBase cluster?**

See Apache HBase Operational Management.

**How do I back up my HBase cluster?**

See HBase Backup.

### B.10. HBase in Action

**Where can I find interesting videos and presentations on HBase?**

See Other Information About HBase.


## Appendix C: Access Control Matrix

The following matrix shows the permission set required to perform operations in HBase. Before using the table, read through the information about how to interpret it.

Interpreting the ACL Matrix Table

The following conventions are used in the ACL Matrix table:

### C.1. Scopes

Permissions are evaluated starting at the widest scope and working to the narrowest scope.

A scope corresponds to a level of the data model. From broadest to narrowest, the scopes are as follows:

Scopes

- Global
- Namespace (NS)
- Table
- Column Family (CF)
- Column Qualifier (CQ)
- Cell

For instance, a permission granted at table level dominates any grants done at the Column Family, Column Qualifier, or cell level. The user can do what that grant implies at any location in the table. A permission granted at global scope dominates all: the user is always allowed to take that action everywhere.

### C.2. Permissions

Possible permissions include the following:

Permissions

- Superuser - a special user that belongs to group "supergroup" and has unlimited access
- Admin (A)
- Create (C)
- Write (W)
- Read (R)
- Execute (X)

For the most part, permissions work in an expected way, with the following caveats:

**Having Write permission does not imply Read permission.**

It is possible and sometimes desirable for a user to be able to write data that same user cannot read. One such example is a log-writing process.

**The hbase:meta table is readable by every user, regardless of the user’s other grants or restrictions.**

This is a requirement for HBase to function correctly.

**`CheckAndPut` and `CheckAndDelete` operations will fail if the user does not have both Write and Read permission.**

**`Increment` and `Append` operations do not require Read access.**

**The `superuser`, as the name suggests has permissions to perform all possible operations.**

**And for the operations marked with *, the checks are done in post hook and only subset of results satisfying access checks are returned back to the user.**

The following table is sorted by the interface that provides each operation. In case the table goes out of date, the unit tests which check for accuracy of permissions can be found in *hbase-server/src/test/java/org/apache/hadoop/hbase/security/access/TestAccessController.java*, and the access controls themselves can be examined in *hbase-server/src/main/java/org/apache/hadoop/hbase/security/access/AccessController.java*.

| Interface | Operation | Permissions |
|---|---|---|
| Master | createTable | superuser\|global(C)\|NS(C) |
|   | modifyTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | deleteTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | truncateTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | addColumn | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | modifyColumn | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C)\|column(A)\|column(C) |
|   | deleteColumn | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C)\|column(A)\|column(C) |
|   | enableTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | disableTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | disableAclTable | Not allowed |
|   | move | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | assign | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | unassign | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | regionOffline | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | balance | superuser\|global(A) |
|   | balanceSwitch | superuser\|global(A) |
|   | shutdown | superuser\|global(A) |
|   | stopMaster | superuser\|global(A) |
|   | snapshot | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | listSnapshot | superuser\|global(A)\|SnapshotOwner |
|   | cloneSnapshot | superuser\|global(A)\|(SnapshotOwner & TableName matches) |
|   | restoreSnapshot | superuser\|global(A)\|SnapshotOwner & (NS(A)\|TableOwner\|table(A)) |
|   | deleteSnapshot | superuser\|global(A)\|SnapshotOwner |
|   | createNamespace | superuser\|global(A) |
|   | deleteNamespace | superuser\|global(A) |
|   | modifyNamespace | superuser\|global(A) |
|   | getNamespaceDescriptor | superuser\|global(A)\|NS(A) |
|   | listNamespaceDescriptors* | superuser\|global(A)\|NS(A) |
|   | flushTable | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | getTableDescriptors* | superuser\|global(A)\|global(C)\|NS(A)\|NS(C)\|TableOwner\|table(A)\|table(C) |
|   | getTableNames* | superuser\|TableOwner\|Any global or table perm |
|   | setUserQuota(global level) | superuser\|global(A) |
|   | setUserQuota(namespace level) | superuser\|global(A) |
|   | setUserQuota(Table level) | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | setTableQuota | superuser\|global(A)\|NS(A)\|TableOwner\|table(A) |
|   | setNamespaceQuota | superuser\|global(A) |
|   | addReplicationPeer | superuser\|global(A) |
|   | removeReplicationPeer | superuser\|global(A) |
|   | enableReplicationPeer | superuser\|global(A) |
|   | disableReplicationPeer | superuser\|global(A) |
|   | getReplicationPeerConfig | superuser\|global(A) |
|   | updateReplicationPeerConfig | superuser\|global(A) |
|   | listReplicationPeers | superuser\|global(A) |
|   | getClusterStatus | any user |
| Region | openRegion | superuser\|global(A) |
|   | closeRegion | superuser\|global(A) |
|   | flush | superuser\|global(A)\|global(C)\|TableOwner\|table(A)\|table(C) |
|   | split | superuser\|global(A)\|TableOwner\|TableOwner\|table(A) |
|   | compact | superuser\|global(A)\|global(C)\|TableOwner\|table(A)\|table(C) |
|   | getClosestRowBefore | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | getOp | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | exists | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | put | superuser\|global(W)\|NS(W)\|table(W)\|TableOwner\|CF(W)\|CQ(W) |
|   | delete | superuser\|global(W)\|NS(W)\|table(W)\|TableOwner\|CF(W)\|CQ(W) |
|   | batchMutate | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | checkAndPut | superuser\|global(RW)\|NS(RW)\|TableOwner\|table(RW)\|CF(RW)\|CQ(RW) |
|   | checkAndPutAfterRowLock | superuser\|global(R)\|NS(R)\|TableOwner\|Table(R)\|CF(R)\|CQ(R) |
|   | checkAndDelete | superuser\|global(RW)\|NS(RW)\|TableOwner\|table(RW)\|CF(RW)\|CQ(RW) |
|   | checkAndDeleteAfterRowLock | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | incrementColumnValue | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | append | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | appendAfterRowLock | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | increment | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | incrementAfterRowLock | superuser\|global(W)\|NS(W)\|TableOwner\|table(W)\|CF(W)\|CQ(W) |
|   | scannerOpen | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | scannerNext | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | scannerClose | superuser\|global(R)\|NS(R)\|TableOwner\|table(R)\|CF(R)\|CQ(R) |
|   | bulkLoadHFile | superuser\|global(C)\|TableOwner\|table(C)\|CF(C) |
|   | prepareBulkLoad | superuser\|global(C)\|TableOwner\|table(C)\|CF(C) |
|   | cleanupBulkLoad | superuser\|global(C)\|TableOwner\|table(C)\|CF(C) |
| Endpoint | invoke | superuser\|global(X)\|NS(X)\|TableOwner\|table(X) |
| AccessController | grant(global level) | global(A) |
|   | grant(namespace level) | global(A)\|NS(A) |
|   | grant(table level) | global(A)\|NS(A)\|TableOwner\|table(A)\|CF(A)\|CQ(A) |
|   | revoke(global level) | global(A) |
|   | revoke(namespace level) | global(A)\|NS(A) |
|   | revoke(table level) | global(A)\|NS(A)\|TableOwner\|table(A)\|CF(A)\|CQ(A) |
|   | getUserPermissions(global level) | global(A) |
|   | getUserPermissions(namespace level) | global(A)\|NS(A) |
|   | getUserPermissions(table level) | global(A)\|NS(A)\|TableOwner\|table(A)\|CF(A)\|CQ(A) |
|   | hasPermission(table level) | global(A)\|SelfUserCheck |
| RegionServer | stopRegionServer | superuser\|global(A) |
|   | mergeRegions | superuser\|global(A) |
|   | rollWALWriterRequest | superuser\|global(A) |
|   | replicateLogEntries | superuser\|global(W) |
| RSGroup | addRSGroup | superuser\|global(A) |
|   | balanceRSGroup | superuser\|global(A) |
|   | getRSGroupInfo | superuser\|global(A) |
|   | getRSGroupInfoOfTable | superuser\|global(A) |
|   | getRSGroupOfServer | superuser\|global(A) |
|   | listRSGroups | superuser\|global(A) |
|   | moveServers | superuser\|global(A) |
|   | moveServersAndTables | superuser\|global(A) |
|   | moveTables | superuser\|global(A) |
|   | removeRSGroup | superuser\|global(A) |
|   | removeServers | superuser\|global(A) |
