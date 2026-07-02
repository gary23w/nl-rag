---
title: "Canonicalization"
source: https://en.wikipedia.org/wiki/Canonicalization
domain: path-traversal-defense
license: CC-BY-SA-4.0
tags: directory traversal, path traversal defense, canonical path resolution, file access control
fetched: 2026-07-02
---

# Canonicalization

In computer science, **canonicalization** (sometimes **standardization** or **normalization**) is a process for converting data that has more than one possible representation into a "standard", "normal", or canonical form. This can be done to compare different representations for equivalence, to count the number of distinct data structures, to improve the efficiency of various algorithms by eliminating repeated calculations, or to make it possible to impose a meaningful sorting order.

## Usage cases

### Filenames

Files in file systems may in most cases be accessed through multiple filenames. For instance in Unix-like systems, the string "`/./`" can be replaced by "`/`". In the C standard library, the function `realpath()` performs this task. Other operations performed by this function to canonicalize filenames are the handling of `/..` components referring to parent directories, simplification of sequences of multiple slashes, removal of trailing slashes, and the resolution of symbolic links.

Canonicalization of filenames is important for computer security. For example, a web server may have a restriction that only files under the cgi directory `C:\inetpub\wwwroot\cgi-bin` may be executed. This rule is enforced by checking that the path starts with `C:\inetpub\wwwroot\cgi-bin\` and only then executing it. While the file `C:\inetpub\wwwroot\cgi-bin\..\..\..\Windows\System32\cmd.exe` initially appears to be in the cgi directory, it exploits the `..` path specifier to traverse back up the directory hierarchy in an attempt to execute a file outside of `cgi-bin`. Permitting `cmd.exe` to execute would be an error caused by a failure to canonicalize the filename to the simplest representation, `C:\Windows\System32\cmd.exe`, and is called a directory traversal vulnerability. With the path canonicalized, it is clear the file should not be executed.

### Unicode

In Unicode, many accented letters can be represented in more than one way. For example, *é* can be represented in Unicode as the Unicode character U+0065 (LATIN SMALL LETTER E) followed by the character U+0301 (COMBINING ACUTE ACCENT), but it can also be represented as the precomposed character U+00E9 (LATIN SMALL LETTER E WITH ACUTE). This makes string comparison more complicated, since every possible representation of a string containing such glyphs must be considered. To deal with this, Unicode provides the mechanism of canonical equivalence. In this context, canonicalization is Unicode normalization.

Variable-width encodings in the Unicode standard, in particular UTF-8, may cause an additional need for canonicalization in some situations. Namely, by the standard, in UTF-8 there is only one valid byte sequence for any Unicode character, but some byte sequences are invalid, i.e., they cannot be obtained by encoding any string of Unicode characters into UTF-8. Some sloppy decoder implementations may accept invalid byte sequences as input and produce a valid Unicode character as output for such a sequence. If one uses such a decoder, some Unicode characters effectively have more than one corresponding byte sequence: the valid one and some invalid ones. This could lead to security issues similar to the one described in the previous section. Therefore, if one wants to apply some filter (e.g., a regular expression written in UTF-8) to UTF-8 strings that will later be passed to a decoder that allows invalid byte sequences, one should canonicalize the strings before passing them to the filter. In this context, canonicalization is the process of translating every string character to its single valid byte sequence. An alternative to canonicalization is to reject any strings containing invalid byte sequences.

### URL

A **canonical URL** is a URL for defining the single source of truth for duplicate content.

#### Use by Google

A canonical URL is the URL of the page that Google thinks is most representative from a set of duplicate pages on your site. For example, if you have URLs for the same page, such as `https://example.com/?dress=1234` and `https://example.com/dresses/1234`, Google chooses one as canonical. Note that the pages do not need to be absolutely identical; minor changes in sorting or filtering of list pages do not make the page unique (for example, sorting by price or filtering by item color).

The canonical can be in a different domain than a duplicate.

#### Internet

With the help of canonical URLs, a search engine knows which link should be provided in a query result.

A canonical link element can get used to define a canonical URL.

#### Intranet

In intranets, manual searching for information is predominant. In this case, canonical URLs can be defined in a non-machine-readable form, too. For example in a guideline.

#### Misc

Canonical URLs are usually the URLs that get used for the share action.

Since the Canonical URL gets used in the search result of search engines, they are in most cases a landing page.

In web search and search engine optimization (SEO), URL canonicalization deals with web content that has more than one possible URL. Having multiple URLs for the same web content can cause problems for search engines - specifically in determining which URL should be shown in search results. Most search engines support the Canonical link element as a hint to which URL should be treated as the true version. As indicated by John Mueller of Google, having other directives in a page, like the robots noindex element can give search engines conflicting signals about how to handle canonicalization

Example:

- `http://wikipedia.com`
- `http://www.wikipedia.com`
- `http://www.wikipedia.com/`
- `http://www.wikipedia.com/?source=asdf`

All of these URLs point to the homepage of Wikipedia, but a search engine will only consider one of them to be the canonical form of the URL.

### XML

A Canonical XML document is by definition an XML document that is in XML Canonical form, defined by The Canonical XML specification. Briefly, canonicalization removes whitespace within tags, uses particular character encodings, sorts namespace references and eliminates redundant ones, removes XML and DOCTYPE declarations, and transforms relative URIs into absolute URIs.

A simple example would be the following two snippets of XML:

1. `<node1 x='1' a="1" a="2">Data</node1    > <node2>Data</node2>`
2. `<node1 a="2" x="1">Data</node1> <node2>Data</node2>`

The first example contains extra spaces in the closing tag of the first node. The second example, which has been canonicalized, has had these spaces removed. Note that only the spaces within the tags are removed under W3C canonicalization, not those between tags.

A full summary of canonicalization changes is listed below:

- The document is encoded in UTF-8
- Line breaks normalized to #xA on input, before parsing
- Attribute values are normalized, as if by a validating processor
- Character and parsed entity references are replaced
- CDATA sections are replaced with their character content
- The XML declaration and document type declaration are removed
- Empty elements are converted to start-end tag pairs
- Whitespace outside of the document element and within start and end tags is normalized
- All whitespace in character content is retained (excluding characters removed during line feed normalization)
- Attribute value delimiters are set to quotation marks (double quotes)
- Special characters in attribute values and character content are replaced by character references
- Superfluous namespace declarations are removed from each element
- Default attributes are added to each element
- Fixup of `xml:base` attributes is performed
- Lexicographic order is imposed on the namespace declarations and attributes of each element

### Computational linguistics

In morphology and lexicography, a lemma is the *canonical form* of a set of words. In English, for example, *run*, *runs*, *ran*, and *running* are forms of the same lexeme, so we can select one of them; ex. *run*, to represent all the forms. Lexical databases such as Unitex use this kind of representation.

Lemmatisation is the process of converting a word to its *canonical form*.
