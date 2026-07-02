---
title: "Billion laughs attack"
source: https://en.wikipedia.org/wiki/Billion_laughs_attack
domain: xxe-prevention
license: CC-BY-SA-4.0
tags: xml external entity, xxe prevention, xml parser hardening, document type definition
fetched: 2026-07-02
---

# Billion laughs attack

In computer security, a **billion laughs attack** is a type of denial-of-service attack (DoS attack) which is aimed at parsers of XML documents.

It is also referred to as an **XML bomb** or as an exponential entity expansion attack.

## Details

The example attack consists of defining 10 entities, each defined as consisting of 10 of the previous entity, with the document consisting of a single instance of the largest entity, which expands to one billion copies of the first entity. Versions with larger amount of entries also exist.

In the most frequently cited example, the first entity is the string "lol", hence the name "billion laughs". At the time this vulnerability was first reported, the computer memory used by a billion instances of the string "lol" would likely exceed that available to the process parsing the XML.

While the original form of the attack was aimed specifically at XML parsers, the term may be applicable to similar subjects as well.

The problem was first reported as early as 2002, but began to be widely addressed in 2008.

Defenses against this kind of attack include capping the memory allocated in an individual parser if loss of the document is acceptable, or treating entities symbolically and expanding them lazily only when (and to the extent) their content is to be used.

## Code example

```mw
<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "lollollollollollollollollollol">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
 <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
 <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
 <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
 <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
 <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
```

When an XML parser loads this document, it sees that it includes one root element, "lolz", that contains the text "&lol9;". However, "&lol9;" is a defined entity that expands to a string containing ten "&lol8;" strings. Each "&lol8;" string is a defined entity that expands to ten "&lol7;" strings, and so on. After all the entity expansions have been processed, this small (< 1 KB) block of XML will actually contain 109 = a billion "lol"s, taking up almost 3 gigabytes of memory.

## Variations

The billion laughs attack described above can take an exponential amount of space or time. The **quadratic blowup** variation causes quadratic growth in resource requirements by simply repeating a large entity over and over again, to avoid countermeasures that detect heavily nested entities. (See computational complexity theory for comparisons of different growth classes.)

A "billion laughs" attack could exist for any file format that can contain macro expansions, for example this YAML bomb:

```mw
a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
```

This crashed earlier versions of Go because the Go YAML processor (contrary to the YAML spec) expands references as if they were macros. The Go YAML processor was modified to fail parsing if the result object becomes too large.

Enterprise software like Kubernetes has been affected by this attack through its YAML parser. For this reason, either a parser with intentionally limited capabilities is preferred (like StrictYAML) or file formats that do not allow references are often preferred for data arriving from untrusted sources.
