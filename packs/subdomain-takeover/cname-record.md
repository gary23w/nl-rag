---
title: "CNAME record"
source: https://en.wikipedia.org/wiki/CNAME_record
domain: subdomain-takeover
license: CC-BY-SA-4.0
tags: subdomain takeover, dangling dns record, orphaned cname defense, domain hijacking prevention
fetched: 2026-07-02
---

# CNAME record

A **Canonical Name** (**CNAME**) **record** is a type of resource record in the Domain Name System (DNS) that maps one domain name (an alias) to another (the **canonical name**).

This can prove convenient when running multiple services (like an FTP server *and* a web server, each running on different ports) from a single IP address. One can, for example, use CNAME records to point *ftp.example.com* and *www.example.com* to the DNS entry for *example.com*, which in turn has an A record which points to the IP address. Then, if the IP address ever changes, one only has to record the change in one place within the network: in the DNS A record for *example.com*.

CNAME records must always point to another domain name, never directly to an IP address.

## Details

DNS CNAME records are specified in RFC 1034 and clarified in Section 10 of RFC 2181.

CNAME records are handled specially in the domain name system and have several restrictions on their use. When a DNS resolver encounters a CNAME record while looking for a regular resource record, it will restart the query using the canonical name instead of the original name. However, if the resolver is specifically told to look for CNAME records, the canonical name (right-hand side) is returned, rather than restarting the query. The canonical name that a CNAME record points to can be anywhere in the DNS, whether local or on a remote server in a different DNS zone.

For example, consider a DNS zone as follows:

```mw
NAME                    TYPE   VALUE
--------------------------------------------------
bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23
```

When an A record lookup for *bar.example.com* is carried out, the resolver will see a CNAME record and restart the lookup for *foo.example.com* and will then return 192.0.2.23.

### Possible confusion

With a CNAME record, one can point a name such as "*bar.example.com*" to "*foo.example.com*". Because of this, during casual discussion, the "*bar.example.com.*" (left-hand) side of a DNS entry can be incorrectly identified as "the CNAME" or "a CNAME". However, this is inaccurate. The canonical (true) name of "*bar.example.com*" is "*foo.example.com*". Because CNAME stands for Canonical Name, the right-hand side is the *actual* "CNAME"; on the same side as the address "A".

This confusion is specifically mentioned in RFC 2181, "Clarifications to the DNS Specification". The left-hand label is an alias for the right-hand side (the RDATA portion), which *is* (or should be) a canonical name. In other words, consider the following CNAME record:

```mw
bar.example.com.        CNAME  foo.example.com.
```

This may be read as saying that "*bar.example.com*" is an alias for the canonical name (CNAME) "*foo.example.com*". A client will request "*bar.example.com*" and the answer will be "*foo.example.com*".

### Restrictions

- CNAME records must always be pointed to another domain name, never to an IP address.
- If a CNAME record is present at a node, no other data should be present; this ensures that the data for a canonical name and its aliases cannot be different. (RFC 1034 section 3.6.2, RFC 1912 section 2.4) The exception is when DNSSEC is being used, in which case there can be DNSSEC related records such as RRSIG, NSEC, etc. (RFC 2181 section 10.1)
- CNAME records that point to other CNAME records should be avoided due to their lack of efficiency, but are not an error. It is possible, then, to create unresolvable loops with CNAME records, as in: foo.example.com. CNAME bar.example.com. bar.example.com. CNAME foo.example.com.
- A CNAME record cannot be present at the zone apex. RFC 1034 section 4.2.1 demands a SOA record at the zone apex and RFC 1034 section 3.6.2 demands that are no other records be present if a CNAME record is present. Therefore a CNAME record cannot appear at the zone apex.
- CNAME records that are served by DNAME records may cause recursive loops in older resolvers.
- MX and NS records must never point to a CNAME alias (RFC 2181 section 10.3). So, for example, a zone must **not** contain constructs such as: example.com. MX 0 foo.example.com. foo.example.com. CNAME host.example.com. host.example.com. A 192.0.2.1
- Domains that are used in the SMTP MAIL and RCPT commands may not have a CNAME record. In practice this may work, but can have different behavior with different mail servers, and can have undesired effects.

## DNAME record

A **DNAME record** or **Delegation Name record** is defined by RFC 6672 (original RFC 2672 is now obsolete). The DNAME record provides redirection (alias) for a subtree of the domain name tree in the DNS. That is, all names that end with a particular suffix are redirected to another part of the DNS. In contrast, the CNAME record creates an alias for a single name and not its subdomains. Like the CNAME record, the DNS lookup will continue by retrying the lookup with the new name. The name server synthesizes a CNAME record to actually apply the DNAME record to the requested name—CNAMEs for every node on a subtree have the same effect as a DNAME for the entire subtree.

For example, if there is a DNS zone as follows:

```mw
foo.example.com.        DNAME  bar.example.com.
bar.example.com.        A      192.0.2.23
xyzzy.bar.example.com.  A      192.0.2.24
*.bar.example.com.      A      192.0.2.25
```

An **A** record lookup for *foo.example.com* will return no data because a DNAME is not a CNAME and there is no A record directly at *foo*.

However, a lookup for *xyzzy.**foo**.example.com* will be DNAME mapped and return the **A** record for *xyzzy.**bar**.example.com*, which is 192.0.2.24; if the DNAME record had been a CNAME record, this request would have returned name not found.

Lastly, a request for *foobar.foo.example.com* would be DNAME mapped and return 192.0.2.25.

## ANAME record

Several managed DNS platforms implement a non-standard ALIAS or ANAME record type. These pseudo records are managed by DNS administrators like CNAME records, but are published and resolved by (some) DNS clients like A records. ANAME records are typically configured to point to another domain, but when queried by a client, answer with an IP address. While ANAME record types were submitted for standardization, there are other non-conforming implementations, so they can do whatever the owner of the DNS platform chooses, including existing at the apex of a zone and existing for domains that receive mail.

The main advantage of ANAME records over CNAME records is that they can be used on a zone apex, while a standards-following resolver will not treat domain names with CNAME records as a zone apex. Also, while a DNS client requires at least two queries to resolve a CNAME to an A record to an IP address, an ANAME will shift the second and subsequent query to the server. If the DNS server can resolve the A record and cache the requested IP address more efficiently and with less latency than its DNS clients can, then the DNS client can resolve the query faster.

The ANAME record type was submitted as a draft standard to IETF. However, the latest draft document expired in January 2020 and has been superseded by a series of proposals, the most recent of which is the one for the SVCB and HTTPS record types.
