---
title: "Sender Policy Framework"
source: https://en.wikipedia.org/wiki/Sender_Policy_Framework
domain: dmarc-email-security
license: CC-BY-SA-4.0
tags: dmarc email authentication, email spoofing defense, sender policy alignment, domain based message authentication, phishing email prevention
fetched: 2026-07-02
---

# Sender Policy Framework

**Sender Policy Framework** (**SPF**) is an email authentication method that allows checking whether the sending mail server is authorized to originate mail from the email sender's domain. This authentication only applies to the email sender listed in the "envelope from" field during the initial SMTP connection. If the email is bounced, a message is sent to this address, and for downstream transmission it typically appears in the "Return-Path" header. To authenticate the email address which is actually visible to recipients on the "From:" line, other technologies, such as DMARC, must be used. Forgery of this address is known as email spoofing, and is often used in phishing and email spam.

The list of authorized sending hosts and IP addresses for a domain is published in the DNS records for that domain. Sender Policy Framework is defined in RFC 7208 dated April 2014 as a "proposed standard".

## History

The first public mention of the concept was in 2000 but went mostly unnoticed. No mention was made of the concept again until a first attempt at an SPF-like specification was published in 2002 on the IETF "namedroppers" mailing list by Dana Valerie Reese, who was unaware of the 2000 mention of the idea. The very next day, Paul Vixie posted his own SPF-like specification on the same list. These posts ignited a lot of interest, led to the forming of the IETF Anti-Spam Research Group (ASRG) and their mailing list, where the SPF idea was further developed. Among the proposals submitted to the ASRG were "Reverse MX" (RMX) by Hadmut Danisch, and "Designated Mailer Protocol" (DMP) by Gordon Fecyk.

In June 2003, Meng Weng Wong merged the RMX and DMP specifications and solicited suggestions from others. Over the next six months, a large number of changes were made and a large community had started working on SPF. Originally SPF stood for *Sender Permitted From* and was sometimes also called *SMTP+SPF*; but its name was changed to *Sender Policy Framework* in February 2004.

In early 2004, the IETF created the MARID working group and tried to use SPF and Microsoft's CallerID proposal as the basis for what is now known as Sender ID; but this collapsed due to technical and licensing conflicts.

The SPF community returned to the original "classic" version of SPF. In July 2005, this version of the specification was approved by the IESG as an IETF *experiment*, inviting the community to observe SPF during the two years following publication. On April 28, 2006, the SPF RFC was published as experimental RFC 4408.

On April 25, 2014 IETF published SPF in RFC 7208 as a "proposed standard" which "obsoleted" RFC 4408 and, as of May 2026, RFC 7208 had not been obsoleted.

## Principles of operation

The Simple Mail Transfer Protocol permits any computer to send email claiming to be from any source address. This is exploited by spammers and scammers who often use forged email addresses, making it more difficult to trace a message back to its source, and easy for spammers to hide their identity in order to avoid responsibility. It is also used in phishing techniques, where users can be duped into disclosing private information in response to an email purportedly sent by an organization such as a bank.

SPF allows the owner of an Internet domain to specify which computers are authorized to send mail with envelope-from addresses in that domain, using Domain Name System (DNS) records. Receivers verifying the SPF information in TXT records may reject messages from unauthorized sources before receiving the body of the message. Thus, the principles of operation are similar to those of DNS-based blackhole lists (DNSBL), except that SPF uses the authority delegation scheme of the Domain Name System. Current practice requires the use of TXT records, just as early implementations did. For a while a new record type (SPF, type 99) was registered and made available in common DNS software. Use of TXT records for SPF was intended as a transitional mechanism at the time. The experimental RFC, RFC 4408, section 3.1.1, suggested "an SPF-compliant domain name SHOULD have SPF records of both RR types". The proposed standard, RFC 7208, says "use of alternative DNS RR types was supported in SPF's experimental phase but has been discontinued".

The envelope-from address is transmitted at the beginning of the SMTP dialog. If the server rejects the domain, the unauthorized client should receive a rejection message, and if that client was a relaying message transfer agent (MTA), a bounce message to the original envelope-from address may be generated. If the server accepts the domain, and subsequently also accepts the recipients and the body of the message, it should insert a Return-Path field in the message header in order to save the envelope-from address. While the address in the Return-Path often matches other originator addresses in the mail header such as the *header-from*, this is not necessarily the case, and SPF does not prevent forgery of these other addresses such as *sender* header.

Spammers can send email with an SPF PASS result if they have an account in a domain with a sender policy, or abuse a compromised system in this domain. However, doing so makes the spammer easier to trace.

SPF benefits owners of email addresses that are forged in the Return-Path. They receive large numbers of unsolicited error messages and other auto-replies. If such receivers use SPF to specify their legitimate source IP addresses and indicate FAIL result for all other addresses, receivers checking SPF can reject forgeries, thus reducing or eliminating the amount of backscatter.

SPF has potential advantages beyond helping identify unwanted mail. In particular, if a sender provides SPF information, then receivers can use SPF PASS results in combination with an allow list to identify known reliable senders. Scenarios like compromised systems and shared sending mailers limit this use.

### Reasons to implement

If a domain publishes an SPF record, spammers and phishers are less likely to forge emails pretending to be from that domain, because the forged emails are more likely to be caught in spam filters which check the SPF record. Therefore, an SPF-protected domain is less attractive to spammers and phishers. Because an SPF-protected domain is less attractive as a spoofed address, it is less likely to be denylisted by spam filters and so ultimately the legitimate email from the domain is more likely to get through.

### FAIL and forwarding

SPF breaks plain message forwarding. When a domain publishes an SPF FAIL policy, legitimate messages sent to receivers forwarding their mail to third parties may be rejected and/or bounced if all of the following occur:

1. The forwarder does not rewrite the Return-Path, unlike mailing lists.
2. The next hop does not allowlist the forwarder.
3. This hop checks SPF.

This is a necessary and obvious feature of SPF – checks *behind* the "border" MTA (MX) of the receiver cannot work directly.

Publishers of SPF FAIL policies must accept the risk of their legitimate emails being rejected or bounced. They should test (e.g., with a SOFTFAIL policy) until they are satisfied with the results. See below for a list of alternatives to plain message forwarding.

### HELO tests

For an empty Return-Path as used in error messages and other auto-replies, an SPF check of the HELO identity is mandatory.

With a bogus HELO identity the result NONE would not help, but for valid host names SPF also protects the HELO identity. This SPF feature was always supported as an option for receivers, and later SPF drafts including the final specification recommend to check the HELO always.

This allows receivers to allowlist sending mailers based on a HELO PASS, or to reject all mails after a HELO FAIL. It can also be used in reputation systems (any allow or deny list is a simple case of a reputation system).

## Implementation

Compliance with SPF consists of three loosely related tasks:

- **Publishing a policy**: Domains and hosts identify the machines authorized to send email on their behalf. They do this by adding additional records to their existing DNS information: every domain name or host that has an A record or MX record should have an SPF record specifying the policy if it is used either in an email address or as HELO/EHLO argument. Hosts which do not send mail should have an SPF record published which indicate such ("v=spf1 -all").
- **Checking and using SPF information**: Receivers use ordinary DNS queries, which are typically cached to enhance performance. Receivers then interpret the SPF information as specified and act upon the result.
- **Revising mail forwarding**: Plain mail forwarding is not allowed by SPF. The alternatives are:
  - Remailing (i.e., replacing the original sender with one belonging to the local domain)
  - Refusing (e.g., answering `551 User not local; please try <user@example.com>`)
  - Allowlisting on the target server, so that it will not refuse a forwarded message
  - Sender Rewriting Scheme, a more complicated mechanism that handles routing non-delivery notifications to the original sender

Thus, the key issue in SPF is the specification for the new DNS information that domains set and receivers use. The records laid out below are in typical DNS syntax, for example:

```
"v=spf1 ip4:192.0.2.0/24 ip4:198.51.100.123 a -all"
```

"v=" defines the version of SPF used. The following words provide *mechanisms* to use to determine if a domain is eligible to send mail. The "ip4" and "a" specify the systems permitted to send messages for the given domain. The "-all" at the end specifies that, if the previous *mechanisms* did not match, the message should be rejected.

### Mechanisms

Eight *mechanisms* are defined:

| ALL | Matches always; used for a default result like `-all` for all IPs not matched by prior mechanisms. |
|---|---|
| A | If the domain name has an address record (A or AAAA) that can be resolved to the sender's address, it will match. |
| IP4 | If the sender is in a given IPv4 address range, match. |
| IP6 | If the sender is in a given IPv6 address range, match. |
| MX | If the domain name has an MX record resolving to the sender's address, it will match (i.e. the mail comes from one of the domain's incoming mail servers). |
| PTR | If the domain name (PTR record) for the client's address is in the given domain and that domain name resolves to the client's address (forward-confirmed reverse DNS), match. This mechanism is discouraged and should be avoided, if possible. |
| EXISTS | If the given domain name resolves to any address, match (no matter the address it resolves to). This is rarely used. Along with the SPF macro language it offers more complex matches like DNSBL-queries. |
| INCLUDE | References the policy of another domain. If that domain's policy passes, this mechanism passes. However, if the included policy fails, processing continues. To fully delegate to another domain's policy, the *redirect* extension must be used. |

### Qualifiers

Each *mechanism* can be combined with one of four *qualifiers*:

- **`+`** for a PASS result. This can be omitted; e.g., `+mx` is the same as `mx`.
- **`?`** for a NEUTRAL result interpreted like NONE (no policy).
- **`~`** (tilde) for SOFTFAIL, a debugging aid between NEUTRAL and FAIL. Typically, messages that return a SOFTFAIL are accepted but tagged.
- **`-`** (minus) for FAIL, the mail should be rejected (see below).

### Modifiers

The *modifiers* allow for future extensions to the framework. To date only the two *modifiers* defined in the RFC 4408 have been widely deployed:

- `exp=some.example.com` gives the name of a domain with a DNS TXT record (interpreted using SPF's macro language) to get an explanation for FAIL results—typically a URL which is added to the SMTP error code. This feature is rarely used.
- `redirect=some.example.com` can be used instead of the ALL-*mechanism* to link to the policy record of another domain. This *modifier* is easier to understand than the somewhat similar INCLUDE-*mechanism*.

### Error handling

As soon as SPF implementations detect syntax errors in a sender policy they **must** abort the evaluation with result PERMERROR. Skipping erroneous *mechanisms* cannot work as expected, therefore `include:bad.example` and `redirect=bad.example` also cause a PERMERROR.

Another safeguard is the maximum of ten mechanisms querying DNS, i.e. any mechanism except from IP4, IP6, and ALL. Implementations can abort the evaluation with result TEMPERROR when it takes too long or a DNS query times out or they can continue pretending that the query returned no data —which is called a "void lookup". However, they **must** return PERMERROR if the policy directly or indirectly needs more than ten queries for *mechanisms*. In addition, they **should** return PERMERROR as soon as more than two "void lookups" have been encountered. Any `redirect=` also counts towards this *processing limits*.

A typical SPF HELO policy `v=spf1 a mx ip4:192.0.2.0 -all` may execute four or more DNS queries: (1) TXT record (SPF type was obsoleted by RFC 7208), (2) A or AAAA for mechanism `a`, (3) MX record and (4+) A or AAAA for each MX name, for mechanism `mx`. Except the first one, all those queries count towards the limit of 10. In addition if, for example, the sender has an IPv6 address, while its name and its two MX names have only IPv4 addresses, then the evaluation of the first two mechanisms already results in more than two void lookups and hence PERMERROR. Mechanisms `ip4`, `ip6` and `all` need no DNS lookup.

## Issues

### DNS SPF Records

To enable rapid testing and deployment, initial versions of SPF checked for its setting in the DNS TXT record of the sending domain - even though this record was traditionally supposed to be free-form text with no semantics attached. Although in July 2005, IANA assigned a specific Resource Record type 99 to SPF the uptake of was never high, and having two mechanisms was confusing for users. In 2014 the use of this record was discontinued after the SPFbis working group concluded that *" ...significant migration to the SPF RR type in the foreseeable future was very unlikely and that the best solution for resolving this interoperability issue was to drop support for the SPF RR type."*

### Header limitations

As SPF increasingly prevents spammers from spoofing the envelope-from address, many have moved to only spoof the address in the From field of the mail header, which is actually displayed to the recipient rather than only processed by the recipient's message transfer agent (MTA). SPF (or DKIM) can be used together with DMARC though, to also check the From field of the mail header. This is called 'identifier alignment'.

Custom proprietary implementations are required to protect against such display name spoofing and cannot utilize SPF.

## Deployment

Anti-spam software such as SpamAssassin version 3.0.0 and ASSP implement SPF. Many mail transfer agents (MTAs) support SPF directly such as Courier, CommuniGate Pro, Wildcat, MDaemon, and Microsoft Exchange, or have patches or plug-ins available that support SPF, including Postfix, Sendmail, Exim, qmail, and Qpsmtpd. As of 2017, more than eight million domains publish SPF FAIL `-all` policies. In a survey published in 2007, 5% of the `.com` and `.net` domains had some kind of SPF policy. In 2009, a continuous survey run at Nokia Research reports that 51% of the tested domains specify an SPF policy. These results can include trivial policies like `v=spf1 ?all`.

In April 2007, BITS, a division of the Financial Services Roundtable, published email security recommendations for its members including SPF deployment. In 2008, the Messaging Anti-Abuse Working Group (MAAWG) published a paper about email authentication covering SPF, Sender ID, and DomainKeys Identified Mail (DKIM). In their "Sender Best Communication Practices" the MAAWG stated: "At the very least, senders should incorporate SPF records for their mailing domains". In 2015, the Messaging Anti-Abuse Working Group (MAAWG) revised a paper about email authentication covering SPF, DomainKeys Identified Mail (DKIM), and DMARC (DMARC). In their revised "Sender Best Communication Practices" the MAAWG stated: "Authentication supports transparency by further identifying the sender(s) of a message, while also contributing to the reduction or elimination of spoofed and forged addresses".

From February 1, 2024, Google requires SPF or DKIM for all domains sending emails to Gmail accounts. Bulk senders (5000+ emails per day) are required to have SPF, DKIM, and DMARC setup for their domains.
