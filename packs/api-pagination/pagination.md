---
title: "Pagination"
source: https://en.wikipedia.org/wiki/Pagination
domain: api-pagination
license: CC-BY-SA-4.0
tags: api pagination, cursor pagination, page navigation, result paging
fetched: 2026-07-02
---

# Pagination

**Pagination**, also known as **paging**, is the process of dividing a document into discrete pages, either electronic pages or printed pages.

In reference to books produced without a computer, pagination can mean the consecutive page numbering to indicate the proper order of the pages, which was rarely found in documents pre-dating 1500, and only became common practice c. 1550, when it replaced foliation, which numbered only the front sides of folios.

Word processing, desktop publishing, and digital typesetting are technologies built on the idea of print as the intended final output medium, although nowadays it is understood that plenty of the content produced through these pathways will be viewed onscreen as electronic pages by most users rather than being printed on paper.

All of these software tools are capable of flowing the content through algorithms to decide the pagination. For example, they all include automated word wrapping (to obviate hard-coded newline delimiters), machine-readable paragraphing (to make paragraph-ending decisions), and automated pagination (to make page-breaking decisions). All of those automated capabilities can be manually overridden by the human user, via soft hyphens (that is, inserting a hyphen which will only be used if the word is split over two lines, and thus not shown if not), manual line breaks (which force a new line within the same paragraph), hard returns (which force both a new line and a new paragraph), and manual page breaks.

Today printed pages are usually produced by outputting an electronic file to a printing device, such as a desktop printer or a modern printing press. These electronic files may for example be Microsoft Word, PDF or QXD files. They will usually already incorporate the instructions for pagination, among other formatting instructions. Pagination encompasses rules and algorithms for deciding where page breaks will fall, which depend partly on cultural considerations about which content belongs on the same page: for example one may try to avoid widows and orphans. Some systems are more sophisticated than others in this respect. Before the rise of information technology (IT), pagination was a manual process: all pagination was decided by a human. Today, most pagination is performed by machines, although humans often override particular decisions (e.g. by inserting a hard page break).

"Electronic page" is a term to encompass paginated content in presentations or documents that originate or remain as visual electronic documents. This is a software file and recording format term in contrast to electronic paper, a hardware display technology. Electronic pages may be a standard sized based on the document settings of a word processor file, desktop publishing application file, or presentation software file. Electronic pages may also be dynamic in size or content such as in the case of HTML pages. When end-user interactivity is part of the user experience design of an electronic page, it is better known as a graphical user interface (GUI). The number and size of electronic pages in a document are limited by the amount of computer data storage, not by the display devices or amount of paper.

Most electronic pages are for either display (screen output) on a computer monitor or handheld device, or output to a printing device. PDF and some e-book file format pages are designed to do both. Most applications will print electronic pages without the need for a screen capture. However, not all software supports WYSIWYG printing of pages. Pages exclusively for screen output are more commonly known as screens, windows, interfaces, scenes, or cards. In the case of presentation software, electronic pages are known as slides.

### In web browsers

Electronic pages displayed on a web browser are often called web pages, regardless of whether they are accessed online via a web server on the World Wide Web, or stored locally offline. More accurately, such documents are named by the markup language that makes them displayable via a web browser, e.g. "HTML page".

With dynamic web pages, pagination is used for such things as displaying a limited number of results on search engine results pages, or showing a limited number of posts when viewing a forum thread.

Pagination is used in some form in almost every web application to divide returned data and display it on multiple pages **within** one web page. Pagination also includes the logic of preparing and displaying the links to the various pages.

Pagination can be handled client-side or server-side.

For client-side pagination, the content of each page is included in the HTML source code pre-loaded within the page, while server-side pagination requests each page individually upon navigation.

Server-side pagination is more common. Client-side pagination can be used when there are very few records to be accessed, in which case all records can be returned, and the client can use JavaScript or CSS to view the separate pages.

By using AJAX, hybrid server/client-side pagination can be used, in which JavaScript is used to request the subsequent page from the server which is loaded and inserted into the Document Object Model via AJAX.

Server-side pagination is appropriate for large data sets providing faster initial page load, accessibility for those not running Javascript, and complex view business logic, while client-side pagination allows navigating between pages without delay from a server request.

Correctly implementing pagination can be difficult. There are many different usability questions such as should "previous" and "next" links be included, how many links to pages should be displayed, and should there be a link to the first and last pages. Also ability to define the number of records displayed in a single page is useful.

In comparison to bottomless or infinite scrolling, pagination allows skipping pages and can be implemented with permanent links (as done with the `offset` URL parameter in the MediaWiki wiki engine), whereas infinite scrolling continuously displays material dynamically.

### In Database

Pagination is an approach used to limit and display only a part of the total data of a query in the database. Instead of showing hundreds or thousands of rows at the same time, the server is requested only one page (a limited set of rows, per example only 10 rows), and the user starts navigating by requesting the next page, and then the next one, and so on. It is very useful, specially in web systems, where there is no dedicated connection between the client and the server, so the client does not have to wait to read and display all the rows of the server.

## Presentation vs. content

Today, all content, no matter which output medium is planned, predicted, or not predicted, can be produced with technologies that allow downstream transformations into any presentation desired, although such best-practice preparation is still far from universal. This usually involves a markup language (such as XML, HTML, or SGML) that tags the content semantically and machine-readably, which allows downstream technologies (such as XSLT, XSL, or CSS) to output them into whatever presentation is desired. This concept is known as the separation of presentation and content. This paradigm is now the conventional one in most commercial publishing, except to the extent that legacy and backward compatibility issues and budget constraints interfere, and to the extent that many of the people involved do not understand the topic enough to help build compliance. But the need to manually paginate has diminished as the technology for dynamic display and automatic pagination advances. Also, there is less need to make a hierarchical distinction between pagination in print and pagination in electronic display, because the same underlying content will most likely be used for the latter exclusively if not for both display methods.
