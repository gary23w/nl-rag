---
title: "noindex"
source: https://en.wikipedia.org/wiki/Noindex
domain: robots-txt
license: CC-BY-SA-4.0
tags: robots exclusion standard, robots txt file, crawler directives, noindex directive, nofollow link
fetched: 2026-07-02
---

# noindex

The **noindex** value of an HTML robots meta tag requests that automated Internet bots avoid indexing a web page. It is also a value of the HTTP response header X-Robots-Tag. Reasons why one might want to use this meta tag include advising robots not to index a very large database, web pages that are very transitory, web pages that are under development, web pages that one wishes to keep slightly more private, or the printer and mobile-friendly versions of pages. Since the burden of honoring a website's noindex tag lies with the author of the search robot, sometimes these tags are ignored. Also the interpretation of the noindex tag is sometimes slightly different from one search engine company to the next.

## Noindexing entire pages

```mw
<html>
<head>
  <meta name="robots" content="noindex">
  <title>Don't index this page</title>
</head>
```

Possible values for the meta tag content are: "none", "all", "index", "noindex", "nofollow", and "follow". A combination of the values is also possible, for example:

```mw
<meta name="robots" content="noindex, follow">
```

### Bot-specific directives

The noindex directive can be restricted only to certain bots by specifying a different "name" value in the meta tag. For example, to specifically block Google's bot, specify:

```mw
<meta name="googlebot" content="noindex">
```

Or, to block Bing's bot, specify:

```mw
<meta name="bingbot" content="noindex">
```

Or, to block Baidu's bot, specify:

```mw
<meta name="baiduspider" content="noindex">
```

### robots.txt file

A robots.txt file can be used to block crawling.

## Noindexing part of a page

It is also possible to exclude part of a Web page, for example navigation text, from being indexed rather than the whole page. There are various techniques for doing this; it is possible to use several in combination. Google's main indexing spider, Googlebot, is not known to recognize any of these techniques.

### <noindex> tag

The Russian search engine Yandex introduced a new `<noindex>...</noindex>` tag which prevents indexing of the content between the tags. To allow the source code to validate, `<!--noindex-->` alternatively can be used:

```mw
<p>
Do index this text.
<noindex>Don't index this text.</noindex>
<!--noindex-->Don't index this text.<!--/noindex-->
</p>
```

Other indexing spiders also recognize the `<noindex>...</noindex>` tag, including Atomz.

### microformat

There is a 2005 draft microformats specification with the same functionality. The Robot Exclusion Profile looks for the attribute and value *class="robots-noindex"* in HTML tags:

```mw
<p>Do index this text.</p>
<div class="robots-noindex">Don't index this text.</div>
<span class="robots-noindex">Don't index this text.</span>
<p class="robots-noindex">Don't index this text.</p>
```

A combination of values is also possible, for example:

```mw
<div class="robots-noindex robots-follow">Text.</div>
```

### Yahoo!

In 2007, Yahoo! introduced similar functionality to the microformat into its spider. However, Yahoo!'s spider is incompatible in that it looks for the value *class="robots-nocontent"* and only this value:

```mw
<p>Do index this text.</p>
<div class="robots-nocontent">Don't index this text.</div>
<span class="robots-nocontent">Don't index this text.</span>
<p class="robots-nocontent">Don't index this text.</p>
```

### SharePoint

SharePoint 2010’s iFilter excludes content inside of a `<div class="noindex">...</div>` tag. Inner `<div>...</div>`s were initially not excluded, but this may have changed. It is also unknown whether the attribute can be applied to tags other than `<div>...</div>`.

```mw
<p>Do index this text.</p>
<div class="noindex">Don't index this text.</div>
```

The Google Search Appliance uses structured comments:

```mw
<p>
Do index this text.
<!--googleoff: all-->
Don't index this text.
<!--googleon: all-->
</p>
```

Other indexing spiders also use their own structured comments.
