---
title: "Beautiful Soup (HTML parser)"
source: https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)
domain: beautifulsoup-parsing
license: CC-BY-SA-4.0
tags: python beautifulsoup, beautiful soup html, html parsing python
fetched: 2026-07-02
---

# Beautiful Soup (HTML parser)

**Beautiful Soup** is a Python package for parsing HTML and XML documents, including those with malformed markup. It creates a parse tree for documents that can be used to extract data from HTML, which is useful for web scraping.

## History

Beautiful Soup was started in 2004 by Leonard Richardson. It takes its name from the poem *Beautiful Soup* from Alice's Adventures in Wonderland and is a reference to the term "tag soup" meaning poorly-structured HTML code. Richardson continues to contribute to the project, which is additionally supported by paid open-source maintainers from the company Tidelift.

### Versions

Beautiful Soup 3 was the official release line of Beautiful Soup from May 2006 to March 2012. The current release is Beautiful Soup 4.x.

In 2021, Python 2.7 support was retired and the release 4.9.3 was the last to support Python 2.7.

## Usage

Beautiful Soup represents parsed data as a tree which can be searched and iterated over with ordinary Python loops.

### Code example

The example below uses the Python standard library's urllib to load Wikipedia's main page, then uses Beautiful Soup to parse the document and search for all links within.

```mw
#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen("https://en.wikipedia.org/wiki/Main_Page") as response:
    soup = BeautifulSoup(response, "html.parser")
    for anchor in soup.find_all("a"):
        print(anchor.get("href", "/"))
```

Another example is using the Python requests library to get divs on a URL.

```mw
import requests
from bs4 import BeautifulSoup

url = "https://wikipedia.org"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headings = soup.find_all("div")

for heading in headings:
    print(heading.text.strip())
```
