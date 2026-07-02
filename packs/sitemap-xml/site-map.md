---
title: "Site map"
source: https://en.wikipedia.org/wiki/Site_map
domain: sitemap-xml
license: CC-BY-SA-4.0
tags: xml sitemap, site map index, crawler discovery, structured url listing
fetched: 2026-07-02
---

# Site map

A **site map** or **sitemap** is a list of pages of a web site within a domain.

There are three primary kinds of sitemap:

- Sitemaps used during the planning of a website by its designers
- Human-visible listings, typically hierarchical, of the pages on a site
- Structured listings intended for web crawlers such as search engines

## Types

Sitemaps may be addressed to users or to software.

Many sites have user-visible sitemaps which present a systematic view, typically hierarchical, of the site. These are intended to help visitors find specific pages, and can also be used by crawlers. They also act as a navigation aid by providing an overview of a site's content at a single glance. Alphabetically organized sitemaps, sometimes called site indexes, are a different approach.

For use by search engines and other crawlers, there is a structured format, the XML Sitemap, which lists the pages in a site, their relative importance, and how often they are updated. This is pointed to from the robots.txt file and is typically called **sitemap.xml**. The structured format is particularly important for websites which include pages that are not accessible through links from other pages, but only through the site's search tools or by dynamic construction of URLs in JavaScript.

## XML sitemaps

Google introduced the Sitemap protocol, so web developers can publish lists of links from across their sites. The basic premise is that some sites have a large number of dynamic pages that are only available through the use of forms and user entries. The Sitemap files contain URLs to these pages so that web crawlers can find them. Bing, Google, Yahoo and Ask now jointly support the Sitemaps protocol.

Since the major search engines use the same protocol, having a Sitemap lets them have the updated page information. Sitemaps do not guarantee all links will be crawled, and being crawled does not guarantee indexing. Google Webmaster Tools allow a website owner to upload a sitemap that Google will crawl, or they can accomplish the same thing with the robots.txt file.

### Sample

Below is an example of a validated XML sitemap for a simple three-page website. Sitemaps are a useful tool for making sites searchable, particularly those written in non-HTML languages.

```mw
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>http://www.example.net/?id=who</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
  <url>
    <loc>http://www.example.net/?id=what</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
  <url>
    <loc>http://www.example.net/?id=how</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
</urlset>
```

**Notes:**

- As with all XML files, all tag values must be entity escaped.
- Google ignores the `<priority>` and `<changefreq>` values.
- Google may use the `<lastmod>` value if it is consistently and verifiably accurate (for example, matching the actual last modification date of the page).
