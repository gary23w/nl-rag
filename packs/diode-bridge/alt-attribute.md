---
title: "alt attribute"
source: https://en.wikipedia.org/wiki/Alt_attribute
domain: diode-bridge
license: CC-BY-SA-4.0
tags: diode bridge
fetched: 2026-07-03
---

# alt attribute

The **alt attribute** is the HTML attribute used in HTML and XHTML documents to specify alternative text (**alt text**) that is to be displayed in place of an element that cannot be rendered. The alt attribute is used for short descriptions, with longer descriptions using the longdesc attribute. The standards organization for the World Wide Web, the World Wide Web Consortium (W3C), recommends that every image displayed through HTML have an alt attribute, though the alt attribute does not need to contain text. The lack of proper alt attributes on website images has led to several accessibility-related lawsuits.

The alt attribute is used to increase accessibility and user friendliness, including for blind internet users who rely on special software for web browsing. The use of the alt attribute for images displayed within HTML is part of W3C's Web Content Accessibility Guidelines (WCAG). Screen readers and text-based web browsers read the alt attribute in place of the image. The text within the alt attribute substitutes the image when copy-pasted as text and makes images more machine-readable, which improves search engine optimization (SEO).

## History

The attribute was first introduced in the HTML 1.2 draft in 1993 to provide support for text-based browsers. In HTML 4.01, which was released in 1999, the attribute was made to be a requirement for the img and area tags. It is optional for the input tag and the deprecated applet tag.

Internet Explorer 7 and earlier render text in alt attributes as tooltip text, which is not compliant with the World Wide Web Consortium (W3C)'s HTML standards. This behavior led many web developers to misuse the alt attribute when they wished to display tooltips containing additional information about images, instead of using the title attribute that was intended for that use. As of Internet Explorer 8, released in 2009, alt attributes no longer render as tooltips on Internet Explorer.

## Usage

The text in the alt attribute is used to replace the image when the image cannot be loaded, without changing the intended meaning of the page's contents. The W3C's web content accessibility guidelines state that the alt attribute is used to convey the meaning and intent of the image, rather than being a literal description of the image itself. For example, an alt attribute for an image of an institution's logo should convey that it is the institution's logo rather than describing details of what the logo looks like. The alt attribute is intended to be used for short and concise descriptions of the image. Longer descriptions can be given using the longdesc attribute, which provides more detailed information and complements but does not replace the alt attribute.

A screen reader such as Orca will read out the alt text in place of the image. A text-based web browser such as Lynx will display the alt text instead of the image (or will display the value attribute if the image is a clickable button). A graphical browser typically will display only the image, and will display the alt text only if the user views the image's properties, or has configured the browser not to display images, or if the browser was unable to retrieve or to decode the image.

The use of descriptions in the alt attribute improves search engine optimization and allows image-specific search engines, such as Google Images, to search for and display relevant images that are used on websites in search results. For non-image search results, the text within the alt attribute is read by search engines the same way that regular text on the page is read.

The W3C recommends that images that convey no information, but are purely decorative, be specified in CSS rather than in the HTML markup. If decorative images are rendered using HTML that do not add to the content and provide no additional information, then the W3C recommends that a blank alt attribute be included in the form of `alt=""`. This makes the page more navigable for users of screen readers or non-graphical browsers by skipping over images that do not convey any meaning. If no alt attribute has been supplied, then browsers that cannot display the image will not overlook the image but instead will read or display the URL or another identifying marker. This creates ambiguity since the user is generally unable to determine from a bare reading of a URL if the image is relevant to the text or if it is a purely decorative element of the webpage. A 2021 Google Lighthouse audit showed that 27% of alt text attributes audited were empty, despite the fact that the majority of those images were non-decorative informational images.

## Lawsuits

There have been many lawsuits over website accessibility and the lack of proper alt attributes on websites. *Maguire v Sydney Organising Committee for the Olympic Games* was a 2000 lawsuit in which a blind man in Australia sued the Sydney Organising Committee for the Olympic Games because their website www.olympics.com was not accessible to him because of the lack of alt attributes on images. The Australian Human Rights Commission ruled that the website had discriminated against him for failing to conform to accessibility standards that enable blind individuals to navigate websites. During the lawsuit, the Australian commonwealth, state and territory governments issued a joint statement through the Department of Broadband, Communications and the Digital Economy that they were adopting the W3C's accessibility guidelines for all .gov.au websites.

In the United States, there have been several high-profile lawsuits involving the lack of alt attributes on images that cite a violation of the Americans with Disabilities Act (ADA). The United States Department of Justice gives the lack of alt attributes as an example of a barrier to website accessibility. *National Federation of the Blind v. Target Corp.* was a 2006 class-action lawsuit that alleged that Target.com violated the ADA because the images did not use alt attributes. This lawsuit set a legal precedent in the United States for website accessibility and compliance with the ADA.
