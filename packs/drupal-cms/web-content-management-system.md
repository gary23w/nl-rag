---
title: "Web content management system"
source: https://en.wikipedia.org/wiki/Web_content_management_system
domain: drupal-cms
license: CC-BY-SA-4.0
tags: drupal cms, web content management, drupal module, content taxonomy
fetched: 2026-07-02
---

# Web content management system

A **web content management system** (**WCM** or **WCMS**) is a software content management system (CMS) specifically for web content. It provides website authoring, collaboration, and administration tools that help users with little knowledge of web programming languages or markup languages create and manage website content. A WCMS provides the foundation for collaboration, providing users the ability to manage documents and output for multiple author editing and participation. Most systems use a content repository or a database to store page content, metadata, and other information assets the system needs.

A presentation layer (template engine) displays the content to website visitors based on a set of templates, which are sometimes XSLT files.

Most systems use server side caching to improve performance. This works best when the WCMS is not changed often but visits happen frequently. Administration is also typically done through browser-based interfaces, but some systems require the use of a fat client.

## Capabilities

A web content management system controls a dynamic collection of web material, including HTML documents, images, and other forms of media. A WCMS facilitates document control, auditing, editing, and timeline management. A WCMS typically has the following features:

**Automated templates**

Create standard templates (usually HTML and

XML

) that users can apply to new and existing content, changing the appearance of all content from one central place.

**Access control**

Some WCMS systems support user groups, which control how registered users interact with the site. A page on the site can be restricted to one or more groups. This means an anonymous user (someone not logged-on), or a logged on user who is not a member of the group a page is restricted to, is denied access.

**Scalable expansion**

Available in

most modern WCMSs

.is the ability to expand a single implementation (one installation on one server) across multiple domains, depending on the server's settings. WCMS sites may be able to create

microsites

/

web portals

within a main site as well.

**Easily editable content**

Once content is separated from the visual presentation of a site, it usually becomes much easier and quicker to edit and manipulate. Most WCMS software includes

WYSIWYG

editing tools allowing non-technical users to create and edit content.

**Scalable feature sets**

Most WCMS software includes plug-ins or modules that can be easily installed to extend an existing site's functionality.

**Web standards upgrades**

Active WCMS software usually receives regular updates that include new feature sets and keep the system up to current web standards.

**Workflow management**

Workflow

management is the process of creating cycles of sequential and parallel tasks that must be accomplished in the WCMS. For example, one or many content creators can submit a story, but it is not published until the copy editor cleans it up and the editor-in-chief approves it.

**Collaboration**

WCMS software may act as a

collaboration platform

where many users retrieve and work on content. Changes can be tracked and authorized for publication or ignored reverting to old versions. Other advanced forms of collaboration allow multiple users to modify (or comment) a page at the same time in a collaboration session.

**Delegation**

Some WCMS software allows for various user groups to have limited privileges over specific content on the website, spreading out the responsibility of content management.

**Document management**

WCMS software may provide a means of collaboratively

managing the lifecycle of a document

from initial creation time, through revisions, publication, archive, and document destruction.

**Content virtualization**

WCMS software may provide a means of allowing each user to work within a virtual copy of the entire website, document set, and/or code base. This enables viewing changes to multiple interdependent resources in context before submission.

**Content syndication**

WCMS software often helps distribute content by generating

RSS

and

Atom

data feeds to other systems. They may also e-mail users when updates become available.

**Multilingual communication**

Many WCMSs can display content in multiple languages.

**Versioning**

Like

document management systems

, WCMS software may implement

version control

, by which users check pages in and out of the WCMS. Authorized editors can retrieve previous versions and work from a selected point.

Versioning

is useful for content that changes and requires updating, but it may be necessary to start from or reference a previous version.

## Types

A WCMS can use one of three approaches: *offline processing*, *online processing*, and *hybrid processing*. These terms describe the deployment pattern for the WCMS in terms of when it applies presentation templates to render web pages from structured content.

### Offline processing

These systems, sometimes referred to as "static site generators", pre-process all content, applying templates before publication to generate web pages. Since pre-processing systems do not require a server to apply the templates at request time, they may also exist purely as design-time tools.

### Online processing

These systems apply templates on-demand. They may generate HTML when a user visits the page, or the user might receive pre-generated HTML from a web cache. Most open source WCMSs support add-ons that extended the system's capabilities. These include features like forums, blogs, wikis, web stores, photo galleries, and contact management. These are variously called modules, nodes, widgets, add-ons, or extensions.

### Hybrid processing

Some systems combine the offline and online approaches. Some systems write out executable code (e.g., JSP, ASP, PHP, ColdFusion, or Perl pages) rather than just static HTML. That way, personnel don't have to deploy the WCMS itself on every web server. Other hybrids operate in either an online or offline mode.

## Advantages

**Low cost**

Some content management systems are free, such as

Drupal

,

eZ Publish

,

TYPO3

,

Joomla

,

Zesty.io

, and

WordPress

. Others may be affordable based on size subscriptions.

Although subscriptions can be expensive, overall the cost of not having to hire full-time developers can lower the total costs. Additionally

software

can be bought based on need for many WCMSs.

**Ease of customization**

A universal layout is created, making pages have a similar theme and design without much code. Many WCMS tools use a drag and drop

AJAX

system for their design modes. It makes it easy for beginner users to create custom front-ends.

**Ease of use**

WCMSs accommodate non-technical people. Simplicity in design of the admin

UI

lets website content managers and other users update content without much training in coding or system maintenance.

**Workflow management**

WCMSs provide the facility to control how content is published, when it is published, and who publishes it. Some WCMSs allow administrators to set up rules for

workflow

management, guiding content managers through a series of steps required for each of their tasks.

**Search engine optimization**

WCMS websites also accommodate

search engine optimization

(SEO). Content freshness helps, as some search engines prefer websites with newer content. Social media plugins help build a community around content. RSS feeds automatically generated by blogs, or WCMS websites can increase the number of subscribers and readers to a site. URL rewriting can be implemented easily—clean URLs without parameters further help in SEO.

Some plugins specifically help with website SEO.

## Disadvantages

**Cost of implementations**

Larger scale implementations may require training, planning, and certifications. Certain WCMSs may require hardware installation. Commitment to the software is required on bigger investments. Commitment to training, developing, and upkeep are costs incurred in any enterprise system.

**Cost of maintenance**

Maintaining WCMSs may require license updates, upgrades, and hardware maintenance.

**Latency issues**

Larger WCMSs can experience latency if hardware infrastructure is not up-to-date, databases are used incorrectly, or

web cache

files that reload every time data updates grow too large.

Load balancing

issues may also impair caching files.

**Tool mixing**

Because the URLs of many WCMSs are dynamically generated with internal parameters and reference information, they are often not stable enough for static pages and other web tools, particularly search engines, to rely on them.

**Security**

WCMS's are often forgotten about when hardware, software, and operating systems are patched for security threats. Due to lack of patching by the user, a hacker can use unpatched WCMS software to exploit vulnerabilities to enter an otherwise secure environment. WCMS's should be part of an overall, holistic security

patch management

program to maintain the highest possible security standards.
