---
title: "Domain hijacking"
source: https://en.wikipedia.org/wiki/Domain_hijacking
domain: subdomain-takeover
license: CC-BY-SA-4.0
tags: subdomain takeover, dangling dns record, orphaned cname defense, domain hijacking prevention
fetched: 2026-07-02
---

# Domain hijacking

**Domain hijacking** or **domain theft** is the act of changing the registration of a domain name without the permission of its original registrant, or by abuse of privileges on domain hosting and registrar software systems.

This can be devastating to the original domain name holder, not only financially as they may have derived commercial income from a website hosted at the domain or conducted business through that domain's e-mail accounts, but also in terms of readership and/or audience for non-profit or artistic web addresses. After a successful hijacking, the hijacker can use the domain name to facilitate other illegal activity such as phishing, where a website is replaced by an identical website that records private information such as log-in passwords, spam, or may distribute malware from the perceived "trusted" domain.

## Description

Domain hijacking can be done in several ways, generally by unauthorized access to, or exploiting a vulnerability in the domain name registrar's system, through social engineering, or getting into the domain owner's email account that is associated with the domain name registration.

A frequent tactic used by domain hijackers is to use acquired personal information about the actual domain owner to impersonate them and persuade the domain registrar to modify the registration information and/or transfer the domain to another registrar, a form of identity theft. Once this has been done, the hijacker has full control of the domain and can use it or sell it to a third party.

Other methods include email vulnerability, vulnerability at the domain-registration level, keyloggers, and phishing sites.

Responses to discovered hijackings vary; sometimes the registration information can be returned to its original state by the current registrar, but this may be more difficult if the domain name was transferred to another registrar, particularly if that registrar resides in another country. If the stolen domain name has been transferred to another registrar, the losing registrar may invoke ICANN's Registrar Transfer Dispute Resolution Policy to seek the return of the domain.

In some cases, the losing registrar for the domain name is not able to regain control over the domain, and the domain name owner may need to pursue legal action to obtain the court ordered return of the domain. In some jurisdictions, police may arrest cybercriminals involved, or prosecutors may file indictments.

Although the legal status of domain hijacking was formerly thought to be unclear, certain U.S. federal courts in particular have begun to accept causes of action seeking the return of stolen domain names. Domain hijacking is analogous with theft, in that the original owner is deprived of the benefits of the domain, but theft traditionally relates to concrete goods such as jewelry and electronics, whereas domain name ownership is stored only in the digital state of the domain name registry, a network of computers. For this reason, court actions seeking the recovery of stolen domain names are most frequently filed in the location of the relevant domain registry. In some cases, victims have pursued recovery of stolen domain names through ICANN's Uniform Domain Name Dispute Resolution Policy (UDRP), but a number of UDRP panels have ruled that the policy is not appropriate for cases involving domain theft. Additionally, police may arrest cybercriminals involved.

## Notable cases

- During the dot com boom, there was extensive media coverage of the hijacking of "sex.com".
- Basketball player Mark Madsen unknowingly bought a "stolen" (or hijacked) domain in an eBay auction.
- In 2015 Lenovo's website and Google's main search page for Vietnam were briefly hijacked.
- In early 2021, the domain for programming language Perl was briefly hijacked, causing problems for the CPAN system.
- On August 19, 2024, Fur Affinity's domain was hijacked for over a day, redirecting users to a *Washington Post* article, then to Kiwi Farms.
- In early 2024, 8,000 domains and 13,000 subdomains of major brands including eBay, Lacoste, Marvel, McAfee, MSN, Pearson, PwC, and The Economist were taken over via a specific form of hijacking called SubdoMailing. This attack focused on spam proliferation and click monetization.

## Prevention

ICANN imposes a 60-day waiting period between a change in registration information and a transfer to another registrar. This is intended to make domain hijacking more difficult, since a transferred domain is much more difficult to reclaim, and it is more likely that the original registrant will discover the change in that period and alert the registrar. Extensible Provisioning Protocol is used for many TLD registries, and uses an authorization code issued exclusively to the domain registrant as a security measure to prevent unauthorized transfers.

## RFC’s

- RFC 3375 - Generic Registry-Registrar Protocol Requirements
- RFC 3735 - Guidelines for Extending EPP
- RFC 3915 - Domain Registry Grace Period Mapping (e.g. Add Grace Period, Redemption Grace Period)
- RFC 4114 - Using EPP for ENUM addresses
- RFC 5910 - Domain Name System (DNS) Security Extensions Mapping for the Extensible Provisioning Protocol (EPP) (obsoletes RFC 4310, DNSSEC)
- RFC 5730 - Extensible Provisioning Protocol (EPP) (obsoletes RFC 4930, which obsoleted RFC 3730)
- RFC 5731 - Extensible Provisioning Protocol (EPP) Domain Name Mapping (obsoletes RFC 4931)
- RFC 5732 - Extensible Provisioning Protocol (EPP) Host Mapping (obsoletes RFC 4932)
- RFC 5733 - Extensible Provisioning Protocol (EPP) Contact Mapping (obsoletes RFC 4933)
- RFC 5734 - Extensible Provisioning Protocol (EPP) Transport over TCP (obsoletes RFC 4934)
