---
title: "Name server"
source: https://en.wikipedia.org/wiki/Name_server
domain: aws-route53
license: CC-BY-SA-4.0
tags: aws route53, cloud dns, managed dns, dns resolution
fetched: 2026-07-02
---

# Name server

A **name server** is a computer application that implements a network service for providing responses to queries against a directory service. It translates an often humanly meaningful, text-based identifier to a system-internal, often numeric identification or addressing component. This service is performed by the server in response to a service protocol request.

An example of a name server is the server component of the Domain Name System (DNS), the core namespaces of the Internet. The most important function of DNS servers is the translation (resolution) of human-memorable domain names and hostnames into the corresponding numeric Internet Protocol (IP) addresses, which can be routed in the Internet.

## Domain name server

The Internet maintains two principal namespaces: the domain name hierarchy and the IP address system. The Domain Name System maintains the domain namespace and provides translation services between these two namespaces. Internet name servers implement the Domain Name System. The top hierarchy of the Domain Name System is served by the root name servers maintained by delegation by the Internet Corporation for Assigned Names and Numbers (ICANN). DNS servers, which are located all over the world, translate domain names into IP addresses, giving them control over which server a user may access via a given domain. Below the root, Internet resources are organized into a hierarchy of domains, administered by the respective registrars and domain name holders. A DNS name server is a server that stores the DNS records, such as address (A, AAAA) records, name server (NS) records, and mail exchanger (MX) records for a domain name (see also List of DNS record types) and responds with answers to queries against its database.

### Types of name servers

Name servers are usually either *authoritative* or *recursive*, as described below.

Although not the usual practice today, name servers can be both authoritative *and* recursive, if they are configured to give authoritative answers to queries in some zones, while acting as a caching name server for all other zones.

### Authoritative name server

An authoritative name server is a name server that is responsible for giving answers in response to questions asked about names in a zone. An authoritative-only name server returns answers only to queries about domain names for which it is responsible (as specifically configured by its administrator).

An authoritative name server can either be a *primary* server or a *secondary* server. A primary server for a zone is the server that stores the definitive versions of all records in that zone. It is identified in the start-of-authority (SOA) resource record. A secondary server for a zone uses an automatic updating mechanism to maintain an identical copy of the primary server's database for a zone. Examples of such mechanisms include DNS zone transfers and file transfer protocols. DNS provides a mechanism whereby the primary for a zone can notify all the known secondaries for that zone when the contents of the zone have changed. The contents of a zone are either manually configured by an administrator, or managed using Dynamic DNS.

Every domain name appears in a zone served by one or more authoritative name servers. The fully qualified domain names of the authoritative name servers of a zone are listed in the NS records of that zone. If the server for a zone is not also authoritative for its parent zone, the server for the parent zone must be configured with a delegation for the zone.

When a domain is registered with a domain name registrar, the zone administrator provides the list of name servers (typically at least two, for redundancy) that are authoritative for the zone that contains the domain. The registrar provides the names of these servers to the domain registry for the top-level domain containing the zone. The domain registry in turn configures the authoritative name servers for that top-level domain with delegations for each server for the zone. If the fully qualified domain name of any name server for a zone appears within that zone, the zone administrator additionally provides IP addresses for that name server, which are installed in the parent zone as glue records; otherwise, the delegation only consists of the list of NS records for that zone.

#### Authoritative answer

A name server indicates that its response is authoritative by setting the *Authoritative Answer* (*AA*) bit in the response to a query on a name for which it is authoritative. Name servers providing answers for which they are not authoritative (for example, name servers for parent zones or recursive resolvers) do not set the *AA* bit.

### Recursive Resolver

A *Recursive Resolver* (sometimes called a Recursive Name Server) is a DNS name server that accepts recursive queries (defined below) from clients (who are using a stub resolver), and then resolves those queries, either from a cache of prior results, or by asking one or more authoritative servers.

#### Recursive query

If a name server cannot answer a query because it does not contain an entry for the host in its DNS cache, it may recursively query name servers higher up in the hierarchy. This is known as a *recursive query* or *recursive lookup*. A server providing recursive queries is known as a *recursive name server*.

In principle, authoritative name servers suffice for the operation of the Internet. However, with only authoritative name-servers operating, every DNS query must start with recursive queries at the root zone of the Domain Name System and each user system must implement resolver software capable of recursive operation.

### Caching name server

A **caching name server** or **DNS cache** is usually a recursive resolver that stores DNS query results for a period of time determined in the configuration (time-to-live) of each domain-name record. DNS caches improve the efficiency of the DNS by reducing DNS traffic across the Internet, and by reducing load on authoritative name-servers, particularly root name-servers. Because they can answer questions more quickly, they also increase the performance of end-user applications that use the DNS.

Caching name servers are often also recursive name servers—they perform every step necessary to answer any DNS query they receive. To do this, the name server queries each authoritative name server in turn, starting from the DNS root zone. It continues until it reaches the authoritative server for the zone that contains the queried domain name. That server provides the answer to the question, or definitively says it can't be answered, and the *caching resolver* then returns this response to the client that asked the question. The authority, resolving and caching functions can all be present in a DNS server implementation, but this is not required: a DNS server can implement any one of these functions alone, without implementing the others.

Internet service providers typically provide caching resolvers for their customers. In addition, many home-networking routers implement caching resolvers to improve efficiency in the local network.

In some systems, `nscd` (name service caching daemon) provides a comprehensive name caching mechanism.
