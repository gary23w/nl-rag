---
title: "Fully qualified domain name"
source: https://en.wikipedia.org/wiki/Fully_qualified_domain_name
domain: subdomain-takeover
license: CC-BY-SA-4.0
tags: subdomain takeover, dangling dns record, orphaned cname defense, domain hijacking prevention
fetched: 2026-07-02
---

# Fully qualified domain name

A **fully qualified domain name** (**FQDN**), sometimes also called an **absolute domain name**, is a domain name that specifies its exact location in the tree hierarchy of the Domain Name System (DNS). It specifies all domain levels, including the top-level domain and the root zone. A fully qualified domain name is distinguished by its unambiguous DNS zone location in the hierarchy of DNS labels: it can be interpreted in only one way.

## Definition

A fully qualified domain name is conventionally written as a list of domain labels separated using the full stop "`.`" character (*dot* or *period*). The top of the hierarchy in an FQDN begins with the rightmost label. For instance, in the FQDN `somehost.example.com`, `com` is a label directly under the root zone, `example` is nested under `com`, and finally `somehost` is nested under `example.com`.

The topmost layer of every domain name is the DNS root zone, which is expressed as an empty label and can be represented in an FQDN with a trailing dot, such as `somehost.example.com.`. A trailing dot is generally implied and often omitted by most applications. Trailing dots are required by the standard format for DNS zone files, as well as to disambiguate cases where an FQDN does not contain any other label separators, such as the FQDNs for the root zone itself and any top-level domain.

The length of each label must be between 1 and 63 octets, and the full domain name is limited to 255 octets, full stops included.

## Relative domain names

A **relative domain name** is a domain name which does not include all labels. It may also be referred to as a partially-qualified domain name, or PQDN. Hostnames can be used as relative domain names.

## Usage

Dot-separated fully qualified domain names are the primarily used form for human-readable representations of a domain name. Dot-separated domain names are not used in the internal representation of labels in a DNS message but are used to reference domains in some TXT records and can appear in resolver configurations, system hosts files, and URLs.

Web addresses typically use FQDNs to represent the host, as it ensures the address will be interpreted identically on any network. Relative hostnames are allowed by some protocols, including HTTP, but disallowed by others, such as the Simple Mail Transfer Protocol (SMTP).
