---
title: "Sitemaps"
source: https://en.wikipedia.org/wiki/Sitemaps
domain: sitemap-xml
license: CC-BY-SA-4.0
tags: xml sitemap, site map index, crawler discovery, structured url listing
fetched: 2026-07-02
---

# Sitemaps

Checked

## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

27 June 2026

.

**Sitemaps** is a protocol in XML format meant for a webmaster to inform search engines about URLs on a website that are available for web crawling. It allows webmasters to include additional information about each URL: when it was last updated, how often it changes, and how important it is in relation to other URLs of the site. This allows search engines to crawl the site more efficiently and to find URLs that may be isolated from the rest of the site's content. The Sitemaps protocol is a URL inclusion protocol and complements `**robots.txt**`, a URL exclusion protocol.

## History

Google first introduced Sitemaps 0.84 in June 2005 so web developers could publish lists of links from across their sites. Google, Yahoo! and Microsoft announced joint support for the Sitemaps protocol in November 2006. The schema version was changed to "Sitemap 0.90", but no other changes were made.

In April 2007, Ask.com and IBM announced support for Sitemaps. Also, Google, Yahoo, MSN announced auto-discovery for sitemaps through `robots.txt`. In May 2007, the state governments of Arizona, California, Utah and Virginia announced they would use Sitemaps on their web sites.

The Sitemaps protocol is based on ideas from "Crawler-friendly Web Servers," with improvements including auto-discovery through `robots.txt` and the ability to specify the priority and change frequency of pages.

## Purpose

Sitemaps are particularly beneficial on websites where:

- Some areas of the website are not available through the browsable interface
- Webmasters use rich Ajax, Silverlight, or Flash content that is not normally processed by search engines.
- The site is very large and there is a chance for the web crawlers to overlook some of the new or recently updated content
- When websites have a huge number of pages that are isolated or not well linked together, or
- When a website has few external links
- The website contains a large amount of rich media content (such as video or images) or is included in Google News.

## File format

The Sitemap Protocol format consists of XML tags. The file itself must be UTF-8 encoded. Sitemaps can also be just a plain text list of URLs. They can also be compressed in .gz format.

A sample Sitemap that contains just one URL and uses all optional tags is shown below.

```mw
<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://example.com/</loc>
        <lastmod>2006-11-18</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```

### Element definitions

The definitions for the elements are shown below:

| Element | Required? | Description |
|---|---|---|
| `<urlset>` | Yes | The document-level element for the Sitemap. The rest of the document after the '<?xml version>' element must be contained in this. |
| `<url>` | Yes | Parent element for each entry. |
| `<sitemapindex>` | Yes | The document-level element for the Sitemap index. The rest of the document after the '<?xml version>' element must be contained in this. |
| `<sitemap>` | Yes | Parent element for each entry in the index. |
| `<loc>` | Yes | Provides the full URL of the page or sitemap, including the protocol (e.g. http, https) and a trailing slash, if required by the site's hosting server. This value must be shorter than 2,048 characters. Note that ampersands in the URL need to be escaped as `&amp;`. |
| `<lastmod>` | No | The date that the file was last modified, in ISO 8601 format. This can display the full date and time or, if desired, may simply be the date in the format YYYY-MM-DD. |
| `<changefreq>` | No | How frequently the page may change: always hourly daily weekly monthly yearly never "Always" is used to denote documents that change each time that they are accessed. "Never" is used to denote archived URLs (i.e. files that will not be changed again). This is used only as a guide for crawlers, and is not used to determine how frequently pages are indexed. Does not apply to `<sitemap>` elements. |
| `<priority>` | No | The priority of that URL relative to other URLs on the site. This allows webmasters to suggest to crawlers which pages are considered more important. The valid range is from 0.0 to 1.0, with 1.0 being the most important. The default value is 0.5. Rating all pages on a site with a high priority does not affect search listings, as it is only used to suggest to the crawlers how important pages of the site are to one another. Does not apply to `<sitemap>` elements. |

Support for the elements that are not required can vary from one search engine to another.

Google ignores `<priority>`and `<changefreq>` values.

## Other formats

### Text file

The Sitemaps protocol allows the Sitemap to be a simple list of URLs in a text file. The file specifications of XML Sitemaps apply to text Sitemaps as well; the file must be UTF-8 encoded, and cannot be more than 50MiB (uncompressed) or contain more than 50,000 URLs. Sitemaps that exceed these limits should be broken up into multiple sitemaps with a sitemap index file (a file that points to multiple sitemaps).

### Syndication feed

A syndication feed is a permitted method of submitting URLs to crawlers; this is advised mainly for sites that already have syndication feeds. One stated drawback is this method might only provide crawlers with more recently created URLs, but other URLs can still be discovered during normal crawling.

It can be beneficial to have a syndication feed as a delta update (containing only the newest content) to supplement a complete sitemap.

If Sitemaps are submitted directly to a search engine (pinged), it will return status information and any processing errors. The details involved with submission will vary with the different search engines. The location of the sitemap can also be included in the `robots.txt` file by adding the following line:

Sitemap: <sitemap_location>

The `<sitemap_location>` should be the complete URL to the sitemap, such as:

https://www.example.org/sitemap.xml

This directive is independent of the user-agent line, so it doesn't matter where it is placed in the file. If the website has several sitemaps, multiple "Sitemap:" records may be included in `robots.txt`, or the URL can simply point to the main sitemap index file.

The following table lists the sitemap submission URLs for a few major search engines:

| Search engine | Submission URL | Help page | Market |
|---|---|---|---|
| Baidu | **https://zhanzhang.baidu.com/dashboard/index** | Baidu Webmaster Dashboard | China, Singapore |
| Bing (and Yahoo!) | **https://www.bing.com/webmaster/ping.aspx?siteMap=** | Bing Webmaster Tools | Global |
| Yandex | **https://webmaster.yandex.com/site/map.xml** | Sitemaps files | Russia, Belarus, Kazakhstan, Turkey |

Sitemap URLs submitted using the sitemap submission URLs need to be URL-encoded, for example: replace `:` (colon) with `%3A`, replace `/` (slash) with `%2F`.

Google retired sitemap submissions using URLs in late 2023.

Sitemaps supplement and do not replace the existing crawl-based mechanisms that search engines already use to discover URLs. Using this protocol does not guarantee that web pages will be included in search indexes, nor does it influence the way that pages are ranked in search results. Specific examples are provided below.

- Google - Webmaster Support on Sitemaps: "Using a sitemap doesn't guarantee that all the items in your sitemap will be crawled and indexed, as Google processes rely on complex algorithms to schedule crawling. However, in most cases, your site will benefit from having a sitemap, and you'll never be penalized for having one."
- Bing - Bing uses the standard sitemaps.org protocol and is very similar to the one mentioned below.
- Yahoo - After the search deal commenced between Yahoo! Inc. and Microsoft, Yahoo! Site Explorer has merged with Bing Webmaster Tools.

## Limits and indexes

The Sitemap XML protocol is also extended to provide a way of listing multiple Sitemaps in a **sitemap index** file. The maximum sitemap size of 50 MiB (uncompressed) or 50,000 URLs means this is necessary for large sites. An example of sitemap index referencing one separate sitemap follows.

```mw
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd"
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <sitemap>
      <loc>https://www.example.com/sitemap1.xml.gz</loc>
      <lastmod>2014-10-01T18:23:17+00:00</lastmod>
   </sitemap>
</sitemapindex>
```

Sitemaps can be compressed using gzip, reducing bandwidth consumption. Multiple sitemap files are supported, with a Sitemap index file serving as an entry point. Sitemap index files may not list more than 50,000 Sitemaps and must be no larger than 50MiB and can be compressed. You can have more than one Sitemap index file.

According to Google, a single property in Google Search Console can include up to 500 sitemap index files. Additionally, sitemaps that are referenced in a sitemap index file must be located in the same directory as the sitemap index file, or in a subdirectory lower in the site hierarchy.

Best practice for optimising a sitemap index for search engine crawlability is to ensure the index refers only to sitemaps as opposed to other sitemap indexes; nesting a sitemap index within a sitemap index is invalid according to Google.

## Additional sitemap types

A number of additional XML sitemap types outside of the scope of the Sitemaps protocol are supported by Google to allow webmasters to provide additional data on the content of their websites. Video and image sitemaps are intended to improve the capability of websites to rank in image and video searches.

### Video sitemaps

Video sitemaps indicate data related to embedding and autoplaying, preferred thumbnails to show in search results, publication date, video duration, and other metadata. Video sitemaps are also used to allow search engines to index videos that are embedded on a website, but that are hosted externally, such as on Vimeo or YouTube.

### Image sitemaps

Image sitemaps are used to indicate image metadata, such as licensing information, geographic location, and an image's caption.

### Google News Sitemaps

Google supports a Google News sitemap type for facilitating quick indexing of time-sensitive news subjects.

## Multilingual and multinational sitemaps

In December 2011, Google announced the annotations for sites that want to target users in many languages and, optionally, countries. A few months later Google announced, on their official blog, that they are adding support for specifying the rel="alternate" and hreflang annotations in Sitemaps. Instead of the (until then only option) HTML link elements the Sitemaps option offered many advantages which included a smaller page size and easier deployment for some websites.

One example of the multilingual sitemap would be as follows:

If for example we have a site that targets English language users through `https://www.example.com/en` and Greek language users through `https://www.example.com/gr`, up until then the only option was to add the hreflang annotation either in the HTTP header or as HTML elements on both URLs like this

```mw
<link rel="alternate" hreflang="en" href="https://www.example.com/en" />
<link rel="alternate" hreflang="gr" href="https://www.example.com/gr" />
```

But now, one can alternatively use the following equivalent markup in Sitemaps:

```mw
 <url>
   <loc>https://www.example.com/en</loc>
    <xhtml:link
      rel="alternate"
      hreflang="gr"
      href="https://www.example.com/gr" />
    <xhtml:link
      rel="alternate"
      hreflang="en"
      href="https://www.example.com/en" />
 </url>
 <url>
   <loc>https://www.example.com/gr</loc>
    <xhtml:link
      rel="alternate"
      hreflang="gr"
      href="https://www.example.com/gr" />
    <xhtml:link
      rel="alternate"
      hreflang="en"
      href="https://www.example.com/en" />
 </url>
```
