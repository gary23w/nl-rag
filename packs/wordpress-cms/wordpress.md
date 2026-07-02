---
title: "WordPress"
source: https://en.wikipedia.org/wiki/WordPress
domain: wordpress-cms
license: CC-BY-SA-4.0
tags: wordpress cms, content management system, wordpress plugin, wordpress theme
fetched: 2026-07-02
---

# WordPress

Checked

## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

24 May 2026

.

**WordPress** (**WP**, or **WordPress.org**) is a web content management system. It was originally created as a tool to publish blogs but has evolved to support publishing other web content, including more traditional websites, mailing lists, Internet forums, media galleries, membership sites, learning management systems, and online stores. Available as free and open-source software, WordPress is among the most popular content management systems – it was used by 22.52% of the top one million websites as of December 2024.

WordPress is written in the PHP programming language and paired with a MySQL or MariaDB database. Features include a plugin architecture and a template system, known as “themes”. Since 2018, WordPress has included a block-based editor (“Gutenberg”).

To function, WordPress has to be installed on a web server, either as part of an Internet hosting service or on a personal computer.

WordPress was first released on May 27, 2003, by its founders, American developer Matt Mullenweg and English developer Mike Little. The WordPress Foundation owns WordPress, WordPress projects, and other related trademarks.

## Overview

"WordPress is a factory that makes webpages" is a core analogy designed to clarify the functions of WordPress: it stores content and enables a user to create and publish webpages, requiring nothing beyond a domain and a hosting service.

WordPress has a web template system using a template processor. Its architecture is a front controller, routing all requests for non-static URIs to a single PHP file that parses the URI and identifies the target page. This allows support for more human-readable permalinks.

### Themes

WordPress users may install and switch among many different themes. Themes allow users to change the look and functionality of a WordPress website without altering the core code or site content. Custom code can be added to the website by using a child theme or through a code editor. Every WordPress website requires at least one theme to be present. Themes may be directly installed using the WordPress "Appearance" administration tool in the dashboard, or theme folders may be copied directly into the themes directory. WordPress themes are generally classified into two categories: free and premium. Many free themes are listed in the WordPress theme directory (also known as the repository), and premium themes are available for purchase from marketplaces and individual WordPress developers. WordPress users may also create and develop their own custom themes and upload them in the WordPress directory or repository.

### Plugins

WordPress' plugin architecture allows users to extend or depreciate the features and functionality of a website or blog. As of December 2021, WordPress.org has 59,756 plugins available, each of which offers custom functions and features enabling users to tailor their sites to their specific needs. However, this does not include the available premium plugins (approximately 1,500+), which may not be listed in the WordPress.org repository. These customizations range from search engine optimization (SEO) to client portals used to display private information to logged-in users, to content management systems, to content displaying features, such as the addition of widgets and navigation bars. Not all available plugins are always abreast with the upgrades, and as a result, they may not function properly or may not function at all. If the plugin developer has not tested the plugin with the last two major versions of WordPress, a warning message will be displayed on the plugin directory, informing users that the plugin may not work properly with the latest WordPress version. Most plugins are available through WordPress themselves, either via downloading them and installing the files manually via FTP or through the WordPress dashboard. However, many third parties offer plugins through their websites, many of which are paid packages.

Web developers who wish to develop plugins need to learn WordPress' hook system, which consists of over 2,000 hooks (as of Version 5.7 in 2021) divided into two categories: action hooks and filter hooks.

Plugins also represent a development strategy that can transform WordPress into all sorts of software systems and applications, limited only by the imagination and creativity of programmers. These are implemented using custom plugins to create non-website systems, such as headless WordPress applications and Software as a Service (SaaS) products.

Plugins could also be used by hackers targeting sites that use WordPress, as hackers could exploit bugs in WordPress plugins instead of bugs in WordPress itself.

### Mobile applications

Phone apps for WordPress exist for Android, iOS. These applications, designed by Automattic, have options such as adding new blog posts and pages, commenting, moderating comments, replying to comments in addition to the ability to view the stats.

### Accessibility

The WordPress Accessibility Coding Standards state that "All new or updated code released in WordPress must conform with the Web Content Accessibility Guidelines 2.0 at level AA."

### Other features

WordPress also features integrated link management, a search engine–friendly, clean permalink structure; the ability to assign multiple categories to posts; and support for tagging of posts. Automatic filters are also included, providing standardized formatting and styling of text in posts (for example, converting regular quotes to smart quotes). WordPress also supports the trackback and pingback standards for displaying links to other sites that have themselves linked to a post or an article. WordPress posts can be edited in HTML, using the visual editor, or using one of several plugins that allow for a variety of customized editing features.

## Multi-user and multi-blogging

Before version 3, WordPress supported one blog per installation, although multiple concurrent copies may be run from different directories if configured to use separate database tables. WordPress Multisites (previously referred to as WordPress Multi-User, WordPress MU, or WPMU) was a fork of WordPress created to allow multiple blogs to exist within one installation but can be administered by a centralized maintainer. WordPress MU makes it possible for those with websites to host their own blogging communities, as well as control and moderate all the blogs from a single dashboard. WordPress MU adds eight new data tables for each blog.

As of the release of WordPress 3, WordPress MU has merged with WordPress.

## History

*b2/cafelog*, more commonly known as *b2* or *catalog*, was the precursor to WordPress. b2/cafelog was estimated to have been installed on approximately 2,000 blogs as of May 2003. It was written in PHP for use with MySQL by Michel Valdrighi, who was a contributing developer to WordPress until 2005. Although WordPress is the official successor, another project, b2evolution, is also in active development.

As the development of b2/cafelog slowed down, Matt Mullenweg began pondering the idea of forking b2/cafelog and new features that he would want in a new CMS, in a blog post written on January 24, 2003. Mike Little, a professional developer, became the first to comment on the blog post expressing interest to contribute. The two worked together to create the first version of WordPress, version 0.70, which was released on May 27, 2003. Christine Selleck Tremoulet, a friend of Mullenweg, suggested the name *WordPress*.

In 2004, the licensing terms for the competing Movable Type package were changed by Six Apart, resulting in many of its most influential users migrating to WordPress. By October 2009, the Open Source CMS MarketShare Report concluded that WordPress enjoyed the greatest brand strength of any open-source content management system.

As of December 2024, WordPress was used by 62.0% of all the websites whose content management system is known, and 22.52% of the top one million websites.

Starting September 2024, Mullenweg engaged WordPress, WordPress.com, and Automattic in a dispute leading to a lawsuit with hosting company WP Engine, causing widespread community concern.

### Awards and recognition

- Winner of InfoWorld's "Best of open source software awards: Collaboration", awarded in 2008.
- Winner of Open Source CMS Awards' "Overall Best Open Source CMS", awarded in 2009.
- Winner of digital synergy's "Hall of Fame CMS category in the 2010 Open Source", awarded in 2010.
- Winner of InfoWorld's "Bossie award for Best Open Source Software", awarded in 2011.

### Release history

Main releases of WordPress are codenamed after well-known jazz musicians, starting from version 1.0.

Although only the current release is officially supported, security updates are backported "as a courtesy" to all versions as far back as 4.0.

| Version | Codename | Release date | Notes |
|---|---|---|---|
| Unsupported: 0.7 | —N/a | May 27, 2003 | Used the same file structure as its predecessor, *b2/cafelog*, and continued the numbering from its last release, 0.6. Only 0.71-gold is available for download in the official WordPress Release Archive page. |
| Unsupported: 1.0 | *Davis* | January 3, 2004 | Added search engine-friendly permalinks, multiple categories, dead-simple installation, and upgrade, comment moderation, XFN support, and Atom support. |
| Unsupported: 1.2 | *Mingus* | May 22, 2004 | Added support of Plugins; in which the same identification headers are used unchanged in WordPress releases as of 2011. |
| Unsupported: 1.5 | *Strayhorn* | February 17, 2005 | Added a range of vital features, such as the ability to manage static pages and a template/Theme system. It was also equipped with a new default template (codenamed *Kubrick*). designed by Michael Heilemann. |
|   |   |   |   |
| Unsupported: 2.0 | *Duke* | December 31, 2005 | Added rich editing, better administration tools, image uploading, faster posting, improved import system, fully overhauled the back end, and various improvements to Plugin developers. |
| Unsupported: 2.1 | *Ella* | January 22, 2007 | Corrected security issues, a redesigned interface, enhanced editing tools (including integrated spell check and auto save), and improved content management options. |
| Unsupported: 2.2 | *Getz* | May 16, 2007 | Added widget support for templates, updated Atom feed support, and speed optimizations. |
| Unsupported: 2.3 | *Dexter* | September 24, 2007 | Added native tagging support, new taxonomy system for categories, and easy notification of updates, fully supports Atom 1.0, with the publishing protocol, and some much-needed security fixes. |
| Unsupported: 2.5 | *Brecker* | March 29, 2008 | Major revamp to the dashboard, dashboard widgets, multi-file upload, extended search, improved editor, an improved plugin system, and more. |
| Unsupported: 2.6 | *Tyner* | July 15, 2008 | Added new features that made WordPress a more powerful CMS: it can now track changes to every post and page and allow easy posting from anywhere on the web. |
| Unsupported: 2.7 | *Coltrane* | December 11, 2008 | Administration interface was redesigned fully, added automatic upgrades, and installed plugins, from within the administration interface. |
| Unsupported: 2.8 | *Baker* | June 10, 2009 | Added speed improvements, automatically installing themes from within the administration interface, introducing the CodePress editor for syntax highlighting, and a redesigned widget interface. |
| Unsupported: 2.9 | *Carmen* | December 19, 2009 | Added global undo, built-in image editor, batch plugin updating, and many less visible tweaks. |
|   |   |   |   |
| Unsupported: 3.0 | *Thelonious* | June 17, 2010 | Added new theme APIs, merged WordPress and WordPress MU, creating the new multi-site functionality, new default theme "Twenty Ten" and a refreshed, lighter admin UI. |
| Unsupported: 3.1 | *Reinhardt* | February 23, 2011 | Added the Admin Bar, which is displayed on all blog pages when an admin is logged in, and Post Format, best explained as a Tumblr-like micro-blogging feature. It provides easy access to many critical functions, such as comments and updates. Includes internal linking abilities, a newly streamlined writing interface, and many other changes. |
| Unsupported: 3.2 | *Gershwin* | July 4, 2011 | Focused on making WordPress faster and lighter. Released only four months after version 3.1, reflecting the growing speed of development in the WordPress community. |
| Unsupported: 3.3 | *Sonny* | December 12, 2011 | Focused on making WordPress friendlier for beginners and tablet computer users. |
| Unsupported: 3.4 | *Green* | June 13, 2012 | Focused on improvements to theme customization, Twitter integration and several minor changes. |
| Unsupported: 3.5 | *Elvin* | December 11, 2012 | Support for the Retina Display, color picker, a new default theme "Twenty Twelve", improved image workflow. |
| Unsupported: 3.6 | *Oscar* | August 1, 2013 | New default theme "Twenty Thirteen", admin enhancements, post formats UI update, menus UI improvements, new revision system, autosave, and post locking. |
| Unsupported: 3.7 | *Basie* | October 24, 2013 | Automatically apply maintenance and security updates in the background, stronger password recommendations, and support for automatically installing the right language files and keeping them up to date. |
| Unsupported: 3.8 | *Parker* | December 12, 2013 | Improved admin interface, responsive design for mobile devices, new typography using Open Sans, admin color schemes, redesigned theme management interface, simplified main dashboard, "Twenty Fourteen" magazine-style default theme, second release using "Plugin-first development process". |
| Unsupported: 3.9 | *Smith* | April 16, 2014 | Improvements to the editor for media, live widget and header previews, and new theme browser. |
|   |   |   |   |
| Unsupported: 4.0 | *Benny* | September 4, 2014 | Improved media management, embeds, writing interface, easy language change, theme customizer, plugin discovery, and compatibility with PHP 5.5 and MySQL 5.6. |
| Unsupported: 4.1 | *Dinah* | December 18, 2014 | Twenty Fifteen as the new default theme, distraction-free writing, easy language switch, Vine embeds, and plugin recommendations. |
| Unsupported: 4.2 | *Powell* | April 23, 2015 | New "Press This" features, improved characters support, emoji support, improved customizer, new embeds, and updated plugin system. |
| Unsupported: 4.3 | *Billie* | August 18, 2015 | Focus on the mobile experience, better passwords, and improved customizer. |
| Unsupported: 4.4 | *Clifford* | December 8, 2015 | Introduction of "Twenty Sixteen" theme, and improved responsive images and embeds. |
| Unsupported: 4.5 | *Coleman* | April 12, 2016 | Added inline linking, formatting shortcuts, live responsive previews, and other updates under the hood. |
| Unsupported: 4.6 | *Pepper* | August 16, 2016 | Added streamlined updates, native fonts, editor improvements with inline link checker and content recovery, and other updates under the hood. |
| Supported: 4.7 | *Vaughan* | December 6, 2016 | Comes with new default theme "Twenty Seventeen", Video Header Support, PDF preview, custom CSS in the live preview, editor Improvements, and other updates under the hood. |
| Supported: 4.8 | *Evans* | June 8, 2017 | The next-generation editor. Additional specific goals include the TinyMCE inline element/link boundaries, new media widgets, and WYSIWYG in the text widget. End Support for Internet Explorer Versions 8, 9, and 10. |
| Supported: 4.9 | *Tipton* | November 16, 2017 | Improved theme customizer experience, including scheduling, frontend preview links, autosave revisions, theme browsing, improved menu functions, and syntax highlighting. Added a new gallery widget and updated text and video widgets. Theme editor gives warnings and rollbacks when saving files that produce fatal errors. |
|   |   |   |   |
| Supported: 5.0 | *Bebo* | December 6, 2018 | New block-based editor *Gutenberg* with new default theme "Twenty Nineteen". |
| Supported: 5.1 | *Betty* | February 21, 2019 | PHP version upgrade notices and block editor improvements. |
| Supported: 5.2 | *Jaco* | May 7, 2019 | Include Site Health Check, PHP error protection, the all-new block directory, and update package signing. |
| Supported: 5.3 | *Kirk* | November 12, 2019 | Polish current user interactions and make user interfaces more user-friendly. New default theme "Twenty Twenty", was designed by Anders Norén. |
| Supported: 5.4 | *Adderley* | March 31, 2020 | Social Icons and Buttons blocks added, blocks customization and user interface improved, added features for personal data exports, custom fields for menu items, blocks improvements for developers. |
| Supported: 5.5 | *Eckstine* | August 11, 2020 | Added lazy-loading images, XML sitemaps by default, auto-updates to plugins and themes, and improvements to the block editor. |
| Supported: 5.6 | *Simone* | December 8, 2020 | New default theme "Twenty Twenty-One," Gutenberg enhancements, automatic updates for core releases, increased support for PHP 8, application passwords for REST API authentication, improved accessibility. |
| Supported: 5.7 | *Esperanza* | March 9, 2021 | New editor is easier to use, do more without writing custom code, simpler default color palette, from HTTP to HTTPS in a single click, new Robots API, lazy-load your iframes and ongoing cleanup after update to jQuery 3.5.1. |
| Supported: 5.8 | *Tatum* | July 20, 2021 | Block widgets, query loop blocks, block themes, List View, Pattern Transformations, Duotone, new theme.json file, dropped IE11 support, WebP image support, new block support flags. |
| Supported: 5.9 | *Joséphine* | January 25, 2022 | New default theme "Twenty Twenty-Two", new WordPress Admin feature Site Editor, Block Themes manageable through Site Editor, new Navigation block, improved block controls, Pattern Directory, List View, refactored Gallery block, Theme.json child theme support, block-level locking, multiple stylesheets per block. |
|   |   |   |   |
| Supported: 6.0 | *Arturo* | May 24, 2022 | Gutenberg writing improvements, multiple style variations and expanded template options for block themes, integrated patterns, additional design tools, multiple block selections from the list view, block locking, and various performance, and accessibility improvements. |
| Supported: 6.1 | *Misha* | November 1, 2022 | Gutenberg writing improvements, design tools for more consistency and control, cleaner layouts and document settings visualization, menu management, fluid typography, improved block placeholders, and spacing presets. |
| Supported: 6.2 | *Dolphy* | March 29, 2023 | Reimagined Site Editor interface, improved Navigation block, Block Inserter, and organized block settings sidebar with tabs for Settings and Styles. A collection of header and footer patterns for block themes is also available, as well as Openverse media integration and Distraction Free mode for writing. The new Style Book provides a complete overview of how each block in the site's library looks, and users can now copy and paste styles and add custom CSS for more control over their site's appearance. Other features include sticky positioning for top-level group blocks, options to import favorite widgets from Classic themes, and local fonts in default WordPress themes for better privacy with Google Fonts included. |
| Supported: 6.3 | *Lionel* | August 8, 2023 | Full content management through Site Editor, Block Theme preview, new My Patterns section for saved block arrangements, template and editor preference management via Command Palette, improved design tools and workflow, new Footnotes and Details block, performance and accessibility improvements. Image aspect ratio settings, distraction-free editing for Site Editor, updated Top Toolbar, improved List View, pattern template building. |
| Supported: 6.4 | *Shirley* | November 7, 2023 | New default theme "Twenty Twenty-Four," writing enhancements, improved Command Palette, advanced Pattern filtering, expanded Block design tools, image lightbox functions, Group block renaming, image previews in List View, export custom patterns as JSON files, new Block Hooks feature, and various performance and accessibility improvements. |
| Supported: 6.5 | *Regina* | April 2, 2024 | Google Fonts management via Font Library, view timestamps, quick summaries, and revision history via Style Book, enhanced background tools, aspect ratios, and box shadows for Block layouts and groups, Data views, enhanced drag-and-drop, improved link controls, new Interactivity and Block Bindings API's, new appearance tools for Classic themes without using *theme.json*, Plugin Dependencies, and various performance and accessibility improvements. |
| Supported: 6.6 | *Dorsey* | July 16, 2024 | Additional color palette and font set choices, quick previews for pages, rollbacks for automatic plugin updates, Block style overrides, and various performance and accessibility improvements. |
| Supported: 6.7 | *Rollins* | November 12, 2024 | New default theme "Twenty Twenty-Five," Zoom Out preview, custom fields for Blocks, font size presets for Styles, HEIC image support, and various performance and accessibility improvements. |
| Supported: 6.8 | *Cecil* | April 15, 2025 | Style Book update, editor improvements, speculative loading, stronger password security with bcrypt. |
| Supported: 6.9 | *Gene* | December 2, 2025 | Notes (for feedback attached to blocks), visual drag and drop for layouts with live preview, enhanced command palette access, automatic text resize to container. |
|   |   |   |   |
| Latest version: 7.0 | *Armstrong* | May 20, 2026 | AI integration, revised admin UI, new blocks and design features. |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |   |

#### WordPress 5.0 "Bebo"

The December 2018 release of WordPress 5.0, "Bebo", is named in homage to the pioneering Cuban jazz musician Bebo Valdés.

It included a new default editor "Gutenberg" – a block-based editor; that allows users to modify their displayed content in a much more user-friendly way than prior iterations. Blocks are abstract units of markup that, composed together, form the content or layout of a web page. Past content that was created on WordPress pages is listed under what is referred to as a Classic Block. Before Gutenberg, there were several block-based editors available as WordPress plugins, e.g. Elementor. Following the release of Gutenberg, comparisons were made between it and those existing plugins.

##### Classic Editor plugin

The Classic Editor plugin was created as a result of User preferences and helped website developers maintain past plugins only compatible with WordPress 4.9, giving plugin developers time to get their plugins updated & compatible with the 5.0 release. Having the Classic Editor plugin installed restores the "classic" editing experience that WordPress has had up until the WordPress 5.0 release. The Classic Editor plugin will be supported at least until 2024.

As of August 2023, the Classic Editor plugin is active on over 5 million installations of WordPress.

## Vulnerabilities

Many security issues have been uncovered and patched in the software, particularly in 2007, 2008, and 2015. A cumulative list of WordPress security vulnerabilities, not all of which have been corrected in the version current at any time, is maintained by SecurityScorecard.

In January 2007, many high-profile search engine optimization (SEO) blogs, as well as many low-profile commercial blogs featuring AdSense, were targeted and attacked with a WordPress exploit. A separate vulnerability on one of the project site's web servers allowed an attacker to introduce exploitable code in the form of a back door to some downloads of WordPress 2.1.1. The 2.1.2 release addressed this issue; an advisory released at the time advised all users to upgrade immediately.

In May 2007, a study revealed that 98% of WordPress blogs being run were exploitable because they were running outdated and unsupported versions of the software. To help mitigate this problem, WordPress made updating the software a much easier, "one-click" automated process in version 2.7 (released in December 2008). However, the filesystem security settings required to enable the update process can be an additional risk.

In a June 2007 interview, Stefan Esser, the founder of the PHP Security Response Team, spoke critically of WordPress' security track record, citing problems with the application's architecture that made it unnecessarily difficult to write code that is secure from SQL injection vulnerabilities, as well as some other problems.

In June 2013, it was found that some of the 50 most downloaded WordPress plugins were vulnerable to common Web attacks such as SQL injection and XSS. A separate inspection of the top 10 e-commerce plugins showed that seven of them were vulnerable.

To promote better security and to streamline the update experience overall, automatic background updates were introduced in WordPress 3.7.

Individual installations of WordPress can be protected with security plugins that prevent user enumeration, hide resources, and thwart probes. Users can also protect their WordPress installations by taking steps such as keeping all WordPress installations, themes, and plugins updated, using only trusted themes and plugins, and editing the site's .htaccess configuration file if supported by the webserver to prevent many types of SQL injection attacks and block unauthorized access to sensitive files. It is especially important to keep WordPress plugins updated because would-be hackers can easily list all the plugins a site uses and then run scans searching for any vulnerabilities against those plugins. If vulnerabilities are found, they may be exploited to allow hackers to, for example, upload their files (such as a web shell) that collect sensitive information.

Developers can also use tools to analyze potential vulnerabilities, including Jetpack Protect, WPScan, WordPress Auditor, and WordPress Sploit Framework developed by 0pc0deFR. These types of tools research known vulnerabilities, such as CSRF, LFI, RFI, XSS, SQL injection, and user enumeration. However, not all vulnerabilities can be detected by tools, so it is advisable to check the code of plugins, themes, and other add-ins from other developers.

In March 2015, it was reported that the Yoast SEO plugin was vulnerable to SQL injection, allowing attackers to potentially execute arbitrary SQL commands. The issue was fixed in version 1.7.4 of the plugin.

In January 2017, security auditors at Sucuri identified a vulnerability in the WordPress REST API that would allow any unauthenticated user to modify any post or page within a site running WordPress 4.7 or greater. The auditors quietly notified WordPress developers, and within six days WordPress released a high-priority patch to version 4.7.2, which addressed the problem.

As of WordPress 6.0, the minimum PHP version requirement is PHP 5.6, which was released on August 28, 2014, and which has been unsupported by the PHP Group and not received any security patches since December 31, 2018. Thus, WordPress recommends using PHP version 7.4 or greater.

In the absence of specific alterations to their default formatting code, WordPress-based websites use the canvas element to detect whether the browser can correctly render emoji. Because Tor Browser does not currently discriminate between this legitimate use of the Canvas API and an effort to perform canvas fingerprinting, it warns that the website is attempting to 'extract HTML5 canvas image data. Ongoing efforts seek workarounds to reassure privacy advocates while retaining the ability to check for proper emoji rendering capability.

## Development and support

### Key developers

Matt Mullenweg and Mike Little were co-founders of the project. Current key people are listed on WordPress's Web site.

WordPress is also developed by its community, including *WP tester*, a group of volunteers who test each release. They have early access to nightly builds, beta versions, and release candidates. Errors are documented via a mailing list and the project's Trac tool.

Though largely developed by the community surrounding it, WordPress is closely associated with Automattic, the company founded by Matt Mullenweg.

### WordPress Foundation

WordPress Foundation is a non-profit organization that was set up to support the WordPress project. The purpose of the organization is to guarantee open access to WordPress's software projects forever. As part of this, the organization owns and manages WordPress, WordCamp, and related trademarks. In January 2010, Matt Mullenweg formed the organization to own and manage the trademarks of WordPress project. Previously – from 2006 onwards – Automattic acted as a short-term owner of the WordPress trademarks. From the beginning, he intended later to place the WordPress trademarks with the WordPress Foundation, which did not yet exist in 2006 and which eventually took longer to set up than expected.

### WordPress Photo Directory

On December 14, 2021, Matt Mullenweg announced the WordPress Photo Directory at the State of the Word 2021 event. It is an open-source image directory for open images maintained by the WordPress project. The image directory aims to provide an open alternative to closed image banks, such as Unsplash, Pixbaby, and Adobe Stock, whose licensing terms have become restrictive in recent years. Use in WordPress themes, for example, is restricted. In January 2022, the project began to gather volunteers, and in February, its own developer website was launched, where team representatives were next selected.

### WordCamp developer and user conferences

WordCamps are casual, locally organized conferences covering everything related to WordPress. The first such event was WordCamp 2006 in August 2006 in San Francisco, which lasted one day and had over 500 attendees. The first WordCamp outside San Francisco was held in Beijing in September 2007. Since then, there have been over 1,022 WordCamps in over 75 cities in 65 countries around the world. WordCamp San Francisco 2014 was the last official annual conference of WordPress developers and users taking place in San Francisco, having now been replaced with WordCamp US. First ran in 2013 as WordCamp Europe, regional WordCamps in other geographical regions are held to connect people who are not already active in their local communities and inspire attendees to start user communities in their hometowns. In 2019, the Nordic region had its own WordCamp Nordic. The first WordCamp Asia was to be held in 2020, but cancelled due to the COVID-19 pandemic.

### Support

WordPress' primary support website is WordPress.org. This support website hosts both WordPress Codex, the online manual for WordPress and a living repository for WordPress information and documentation, and WordPress Forums, an active online community of WordPress users.

### Hosting

WordPress hosting services typically offer one-click WordPress installations, automated updates and backups, and security features to safeguard against common threats. Many also provide support and are configured for optimal performance with the CMS.

There are two primary types of WordPress hosting: shared WordPress hosting and managed WordPress hosting. Shared WordPress hosting is a budget-friendly option where multiple websites reside on a single server, sharing resources. Managed WordPress hosting includes comprehensive management of a WordPress site, including technical support, security, performance optimization, and often higher server resources, but comes at a higher price.
