---
title: "Canonical link element"
source: https://en.wikipedia.org/wiki/URL_canonicalization
domain: search-engine-optimization
license: CC-BY-SA-4.0
tags: search engine optimization, meta description tag, canonical link relation, web crawler indexing
fetched: 2026-07-02
---

# Canonical link element

(Redirected from

URL canonicalization

)

A **canonical link element** is an HTML element that helps webmasters prevent duplicate content issues in search engine optimization by specifying the "canonical" or "preferred" version of a web page. It is described in RFC 6596, which went live in April 2012.

## Purpose

A major problem for search engines is to determine the original source for documents that are available on multiple URLs. Content duplication can happen in many ways, including:

- Duplication due to GET-parameters
- Duplication with multiple URLs due to CMS (i.e. www or non www urls)
- Duplication due to accessibility on different hosts/protocols. (i.e. https or http)
- Duplication due to print versions of websites

Duplicate content issues occur when the same content is accessible from multiple URLs. For example, http://www.example.com/page.html would be considered by search engines to be an entirely different page from http://www.example.com/page.html?parameter=1, even though both URLs may reference the same content.

In February 2009, Google, Yahoo and Microsoft announced support for the `canonical` link element, which can be inserted into the `<head>` section of a web page, to allow webmasters to prevent these issues. The canonical link element helps webmasters make clear to the search engines which page should be credited as the original.

The canonical link element allows search engines to consolidate indexing and ranking signals from duplicate or similar pages into a single preferred URL.

Search engines try to utilize canonical link definitions as an output filter for their search results. If multiple URLs contain the same content in the result set, the canonical link URL definitions will likely be incorporated to determine the original source of the content. "For example, when Google finds identical content instances, it decides to show one of them. Its choice of the resource to display in the search results will depend upon the search query."

According to Google, the `canonical` link element is not considered to be a directive, but rather a hint that the ranking algorithm will "honor strongly".

While the canonical link element has its benefits, Matt Cutts, then the head of Google's webspam team, has said that the search engine prefers the use of 301 redirects. Cutts said the preference for redirects is because Google's spiders can choose to ignore a canonical link element if they deem it more beneficial to do so.

## Factors Google considers when choosing a canonical for a page

There are multiple factors Google evaluates when determining the canonical version of a page, including:

- **The canonical tag you set up**: This is the most direct way to suggest the preferred URL to search engines.
- **Internal linking**: Pages with strong internal links pointing to them are more likely to be treated as canonical.
- **Sitemap.xml**: The URLs listed in the sitemap also influence Google's decision.
- **Redirects**: Google may choose a URL redirected to from others as the canonical version.

## Implementation

### Semantic tag

The canonical link element can be either used in the semantic HTML `<head>` or sent with the HTTP header of a document. For non HTML documents, the HTTP header is an alternate way to set a canonical URL.

By the HTML 5 standard, the `<link rel="canonical" href="http://example.com/">` HTML element must be within the `<head>` section of the document.

### Self-hyperlink

Some sites such as Stack Overflow have on-page hyperlinks which link to a clean URL of themselves. Usability benefits are facilitating copying the hyperlink target URL or title if the browser or a browser extension offers a "Copy link text" context menu option for hyperlinks, the ability for the original URL to be retrieved from a saved page if not stored by the browser into a comment inside the file, as well as the ability to duplicate the opened page into a new tab right next to the currently opened one if the browser lacks such a feature.

When the same or very similar content is accessible from multiple URLs, search engines like Google can get confused. For example, the following URLs might all show the exact same page:

- https://example.com/product
- https://example.com/product?ref=email
- https://www.example.com/product
- https://example.com/product/

Without a canonical tag, search engines don't know which version to index and rank. This can dilute your SEO strength and cause a negative impact on your search rankings.

## Examples

### HTTP

```mw
HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <https://www.newthink.life/page.php>; rel="canonical"
Content-Length: 4223
...
```
