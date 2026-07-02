---
title: "Markup language"
source: https://en.wikipedia.org/wiki/Markup_language
domain: xslt-stylesheet
license: CC-BY-SA-4.0
tags: xslt stylesheet, xsl transformations, xml stylesheet language, xpath expressions
fetched: 2026-07-02
---

# Markup language

A **markup language** is a text-encoding system which specifies the structure and formatting of a document and potentially the relationships among its parts. Markup can control the display of a document or enrich its content to facilitate automated processing.

A markup language is a set of rules governing what markup information may be included in a document and how it is combined with the content of the document in a way to facilitate use by humans and computer programs. The idea and terminology evolved from the marking up of paper manuscripts (e.g., with revision instructions by editors), traditionally written with a red pen or blue pencil on authors' manuscripts.

Older markup languages, which typically focus on typesetting and presentation, include troff, TeX, and LaTeX. Scribe and most modern markup languages, such as XML, identify document components (for example headings, paragraphs, and tables), with the expectation that technology, such as stylesheets, will be used to apply formatting or other processing.

Some markup languages, such as the widely used HTML, have pre-defined presentation semantics, meaning that their specifications prescribe some aspects of how to present the structured data on particular media. HTML, like DocBook, Open eBook, JATS, and many others, are based on the markup metalanguages XML and SGML. That is, SGML and XML allow designers to specify particular schemas, which determine which elements, attributes, and other features are permitted, and where.

A key characteristic of most markup languages is that they allow combining markup with content such as text and pictures. For example, if a few words in a sentence need to be emphasized, or identified as a proper name, defined term, or another special item, the markup may be inserted between the characters of the sentence.

## Etymology

The word *markup* is derived from the traditional publishing practice of *marking up* a manuscript, which involves adding handwritten annotations in the form of conventional symbolic printer's instructions—in the margins and text of a paper or printed manuscript.

For centuries, this task was done primarily by skilled typographers known as *markup men* or *markers* who marked up text to indicate what typeface, style, and size should be applied to each part, and then passed the manuscript to others for typesetting by hand or machine.

The markup was also commonly applied by editors, proofreaders, publishers, and graphic designers, and by authors themselves, all of whom might also mark things such as corrections and changes.

## Types

There are three general categories of electronic markup, articulated by James Coombs, Allen Renear, and Steven DeRose in 1987, and Tim Bray in 2003.

### Presentational markup

Presentational markup is used by traditional word-processing systems. Binary codes embedded within document text produce the WYSIWYG ('what you see is what you get') effect. Such markup is usually hidden from human users, even authors and editors. Such systems use procedural and descriptive markup internally but convert them to present the user with formatted arrangements of type.

### Procedural markup

Markup is embedded in text which provides instructions for programs to process the text. Well-known examples include troff, TeX, and Markdown. Generally, software processes the text sequentially from beginning to end, following the instructions as encountered. Such text is often edited with the markup visible and directly manipulated by the author. Popular procedural markup systems usually include programming constructs, especially macros, allowing complex sets of instructions to be invoked by a simple name (and perhaps a few parameters). This is much faster, less error-prone, and more maintenance-friendly than re-stating the same or similar instructions in many places.

### Descriptive markup

Descriptive markup is specifically used to describe parts of the document for what they are, rather than how they should be processed. Well-known systems that provide many such labels include LaTeX, HTML, and XML. The objective is to decouple the structure of the document from any particular treatment or rendition of it. Such markup is often described as *semantic*. An example of a descriptive markup is HTML's `<cite>` tag, which is used to label a citation. Descriptive markup—sometimes called *logical markup* or *conceptual markup*—encourages authors to write in a way that describes the material conceptually, rather than visually.

There is considerable overlap and concurrent use of markup types. In modern word-processing systems, presentational markup is often saved in descriptive-markup-oriented systems such as XML, and then processed procedurally by implementations. The programming in procedural-markup systems, such as TeX, may be used to create higher-level markup systems that are more descriptive in nature, such as LaTeX.

In recent years, several markup languages have been developed with ease of use as a key goal, and without input from standards organizations, aimed at allowing authors to create formatted text via web browsers, for example in wikis and web forums. These are sometimes called lightweight markup languages. Markdown, BBCode, and the markup language used by Wikipedia are examples of such languages.

## History

### GenCode

The first well-known public presentation of markup languages in computer text processing was made by William W. Tunnicliffe at a conference in 1967, although he preferred to call it *generic coding.* It can be seen as a response to the emergence of processing programs such as RUNOFF that each used their own control notation, often specific to the target typesetting device. In the 1970s, Tunnicliffe led the development of a standard called GenCode for the publishing industry. Book designer Stanley Rice published speculation along similar lines in 1970.

Brian Reid, in his 1980 dissertation at Carnegie Mellon University, developed a theory and working implementation of descriptive markup in actual use. However, IBM researcher Charles Goldfarb is more commonly considered the inventor of markup languages. Goldfarb developed the basic idea while working on a primitive document management system intended for law firms in 1969, and helped invent IBM's Generalized Markup Language (GML) later that same year. GML was first publicly disclosed in 1973.

In 1975, Goldfarb moved from Cambridge, Massachusetts to Silicon Valley and became a product planner at the IBM Almaden Research Center. There, he convinced IBM's executives to deploy GML commercially in 1978 as part of IBM's Document Composition Facility product, and it was widely used in business within a few years.

Standard Generalized Markup Language (SGML), the first standard descriptive markup language, was based on both GML and GenCode. It was the result of an International Organization for Standardization (ISO) committee that was first chaired by Tunnicliffe, and which Goldfarb also worked on beginning in 1974. Goldfarb eventually became chair of the committee. SGML was first released by ISO as the ISO 8879 standard in October 1986.

### troff and nroff

Some early examples of computer markup languages available outside the publishing industry can be found in typesetting tools on Unix systems such as troff and nroff. In these systems, formatting commands were inserted into the document text so that typesetting software could format the text according to the editor's specifications. It was a trial and error iterative process to correctly print a document. The availability of WYSIWYG publishing software supplanted much use of these languages among casual users, though professional publishing work still uses markup to specify the non-visual structure of texts, and WYSIWYG editors now usually save documents in a markup-language-based format.

### TeX

Another major publishing standard is TeX, created and refined by Donald Knuth in the 1970s and 1980s. TeX concentrated on the detailed layout of text and font descriptions to typeset mathematical books. This required Knuth to spend considerable time investigating the art of typesetting. TeX is mainly used in academia, where it is a *de facto* standard in many scientific disciplines. A TeX macro package known as LaTeX provides a descriptive markup system on top of TeX, and is widely used both among the scientific community and the publishing industry.

### Scribe, GML, and SGML

The first language to make a clear distinction between structure and presentation was Scribe, developed by Brian Reid and described in his doctoral thesis in 1980. Scribe was revolutionary in a number of ways, introducing the idea of styles separated from the marked-up document, and a grammar that controlled the usage of descriptive elements. Scribe influenced the development of GML and later SGML, and is a direct ancestor to HTML and LaTeX.

In the early 1980s, the idea that markup should focus on the structural aspects of a document and leave the visual presentation of that structure to the interpreter led to the creation of SGML. The language was developed by a committee chaired by Goldfarb. It incorporated ideas from many different sources, including Tunnicliffe's project, GenCode. Sharon Adler, Anders Berglund, and James A. Marke were also key members of the SGML committee.

SGML specifies a syntax for including the markup in documents, as well as one for separately describing what tags are allowed, and where (the document type definition (DTD), later known as a schema). This allows authors to create and use any markup they want, selecting tags that make the most sense to them and are named in their own natural languages, while also allowing automated verification. Thus, SGML is properly a metalanguage, and many markup languages are derived from it. From the late 1980s onward, most substantial new markup languages have been based on SGML, including the Text Encoding Initiative (TEI) guidelines and DocBook. SGML was promulgated as the ISO 8879 standard in 1986.

SGML found wide acceptance and use in fields with very large-scale documentation requirements. However, many found it cumbersome and difficult to learn—a side effect of its design attempting to do too much and being too flexible. For example, SGML made end tags (or start tags, or both) optional in certain contexts, because its developers thought markup would be done manually by overworked support staff who would appreciate saving keystrokes.

#### HTML

In 1989, computer scientist Tim Berners-Lee wrote a memo proposing an Internet-based hypertext system, then specified HTML and wrote the browser and server software in late 1990. The first publicly available description of HTML was a document called "HTML Tags", first mentioned on the Internet by Berners-Lee in late 1991. It describes 18 elements comprising the initial, relatively simple design of HTML. Except for the hyperlink tag, these were strongly influenced by SGMLguid, an in-house SGML-based documentation format at CERN, and very similar to the sample schema in the SGML standard. Eleven of these elements still exist in HTML 4.

Berners-Lee considered HTML an SGML application. The Internet Engineering Task Force (IETF) formally defined it as such with the mid-1993 publication of the first proposal for an HTML specification: "Hypertext Markup Language (HTML)" by Berners-Lee and Dan Connolly, which included an SGML DTD to define the grammar. Many of the HTML text elements are found in the 1988 ISO technical report *TR 9537 Techniques for using SGML*, which in turn covers the features of early text formatting languages, such as that used by the RUNOFF command developed in the early 1960s for the Compatible Time-Sharing System operating system. These formatting commands were derived from those used by typesetters to manually format documents. Steven DeRose argues that HTML's use of descriptive markup (and the influence of SGML in particular) was a major factor in the success of the Web, because of the flexibility and extensibility that it enabled. HTML became the main markup language for creating web pages and other information that can be displayed in a web browser and is likely the most used markup language in the world in the 21st century.

### XML

XML (Extensible Markup Language) is a widely used meta markup language. It was developed by the World Wide Web Consortium (W3C) in a committee created and chaired by Jon Bosak. The main purpose of XML was to simplify SGML by focusing on a particular use case—documents on the Internet. XML remains a metalanguage like SGML, allowing users to create any tags needed (hence *extensible*) and then describing those tags and their permitted uses.

XML adoption was hastened by the fact that every XML document can be written so that it is also an SGML document, allowing existing SGML users and software to switch to XML fairly easily. At the same time, XML eliminates many complex features of SGML to simplify implementation environments such as documents and publications. It appears to balance simplicity and flexibility, as well as support very robust schema definitions and validation tools, and was rapidly adopted for many uses. XML is now widely used for communicating data between applications, serializing program data, for hardware communication protocols, vector graphics, and other uses besides documents.

#### XHTML

From January 2000 until HTML 5 was released, all W3C recommendations for HTML were based on XML, using XHTML (Extensible HyperText Markup Language). The language specification requires that XHTML documents be *well-formed* XML documents. This allows for more rigorous and robust documents, by avoiding many syntax errors which historically led to unwanted browser behavior, while still using document components familiar to HTML users.

One of the most noticeable differences between HTML and XHTML is the latter's rule that *all tags must be closed*: empty HTML tags such as `<br>` must either be *closed* with a regular end-tag, or replaced by a special form: `<br />` (the space before the slash on the end tag is optional but frequently used, because it enables some pre-XML web browsers and SGML parsers to accept the tag). Another difference is that all attribute values in tags must be quoted. Both these differences are commonly criticized as verbose but also praised because they make it far easier to detect, localize, and repair errors. Finally, all tag and attribute names within the XHTML namespace must be lowercase to be valid. HTML, on the other hand, was case-insensitive.

#### Other XML-based applications

Many XML-based applications exist, including the Resource Description Framework as RDF/XML, XForms, DocBook, SOAP, and the Web Ontology Language (OWL). For a partial list of these, see list of XML markup languages.

## Features

A common feature of many markup languages is that they intermix the text of a document with markup instructions in the same data stream or file. This is not necessary; it is possible to isolate markup from text content, using pointers, offsets, IDs, or other methods to coordinate the two. Such *standoff* markup is typical for the internal representations that programs use to work with marked-up documents. However, *embedded* or *inline* markup is much more common elsewhere. For example, the following is a small section of text marked up in HTML:

```mw
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <h1>Mozilla is cool</h1>
    <img src="images/firefox-icon.png" alt="The Firefox logo: a flaming fox surrounding the Earth.">

    <p>At Mozilla, we’re a global community of</p>

    <ul> <!-- changed to list in the tutorial -->
      <li>technologists</li>
      <li>thinkers</li>
      <li>builders</li>
    </ul>

    <p>working together to keep the Internet alive and accessible, so people worldwide can be informed contributors and creators of the Web. We believe this act of human collaboration across an open platform is essential to individual growth and our collective future.</p>

    <p>Read the <a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a> to learn even more about the values and principles that guide the pursuit of our mission.</p>
  </body>
</html>
```

The codes enclosed in angle-brackets `<like this>` are markup instructions (known as *tags*), while the text between these instructions is the actual text of the document. The codes `h1`, `p`, and `em` are examples of *semantic* markup, in that they describe the intended purpose or the meaning of the text they include. Specifically, `h1` means the enclosed text is a *first-level heading*, `p` means a *paragraph*, and `em` means an *emphasized* word or phrase. A program interpreting such structural markup may apply its own rules or styles for presenting the various pieces of text, using different typefaces, boldness, font size, indentation, color, or other styles, as desired. For example, a tag such as `h1` might be presented in a large bold sans-serif typeface in an article, or it might be underscored in a monospaced (fixed-width font) document, or it might not change the presentation at all.

In contrast, the `i` tag in HTML 4 is an example of *presentational* markup, which is generally used to specify a characteristic of the text without specifying the reason for that appearance. In this case, the `i` element dictates the use of an italic typeface. However, in HTML 5, this element has been repurposed with a more semantic usage: to denote "a span of text in an alternate voice or mood, or otherwise offset from the normal prose in a manner indicating a different quality of text". For example, it is appropriate to use the `i` element to indicate a taxonomic designation or a phrase in another language. The change was made to ease the transition from HTML 4 to 5 as smoothly as possible so that deprecated uses of presentational elements would preserve the most likely intended meaning.

TEI has published extensive guidelines for how to encode texts of interest in the humanities and social sciences, developed through years of international cooperative work. These guidelines are used for encoding historical documents, and the works of particular scholars, periods, and genres.

## Broader use

While the idea of markup language originated with text documents, they are increasingly used in the presentation of other types of information, including playlists, vector graphics, web services, content syndication, and user interfaces. Most of these are XML applications because XML is a well-defined and extensible language.

The use of XML has also led to the possibility of combining multiple markup languages into a single profile, like XHTML+SMIL and XHTML+MathML+SVG.
