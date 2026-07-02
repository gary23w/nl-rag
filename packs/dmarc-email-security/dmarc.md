---
title: "DMARC"
source: https://en.wikipedia.org/wiki/DMARC
domain: dmarc-email-security
license: CC-BY-SA-4.0
tags: dmarc email authentication, email spoofing defense, sender policy alignment, domain based message authentication, phishing email prevention
fetched: 2026-07-02
---

# DMARC

**Domain-based Message Authentication, Reporting and Conformance** (**DMARC**) is an email authentication protocol. It is designed to give email domain owners the ability to protect their domain from unauthorized use, commonly known as email spoofing. The purpose and primary outcome of implementing DMARC is to protect a domain from being used in business email compromise attacks, phishing email and email scams.

Once the DMARC DNS entry is published, any receiving email server can authenticate the incoming email based on the instructions published by the domain owner within the DNS entry. If the email passes the authentication, it will be delivered and can be trusted. If the email fails the check, depending on the instructions held within the DMARC record the email could be delivered, quarantined or rejected.

DMARC extends two existing email authentication mechanisms, Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM). It allows the administrative owner of a domain to publish a policy in their DNS records to specify how to check the `From:` field presented to end users and how the receiver should deal with failures, and it provides a reporting mechanism for actions performed under those policies.

DMARC is defined in the Internet Engineering Task Force's published document RFC 9989, dated May 2026, as "Standards Track".

## Overview

A DMARC policy allows a sender's domain to indicate that their email messages are protected by SPF and/or DKIM, and tells a receiver what to do if neither of those authentication methods passes – such as to reject the message or quarantine it. The policy can also specify how an email receiver can report back to the sender's domain about messages that pass and/or fail.

These policies are published in the public Domain Name System (DNS) as text TXT records.

DMARC does not directly address whether or not an email is spam or otherwise fraudulent. Instead, DMARC can require that a message not only pass DKIM or SPF validation, but that it also pass § Alignment. Under DMARC a message can fail even if it passes SPF or DKIM but fails alignment.

Setting up DMARC may improve the deliverability of messages from legitimate senders.

## Alignment

DMARC operates by checking that the domain in the message's `From:` field (also called "RFC5322.From") is "aligned" with other authenticated domain names. If either SPF (specified using the `aspf` field) or DKIM (specified using the `adkim` field) alignment checks pass, then the DMARC alignment test passes.

Alignment may be specified as strict or relaxed. For strict alignment, the domain names must be identical. For relaxed alignment, the top-level "Organizational Domain" must match. The Organizational Domain used to be found by checking a list of public DNS suffixes. The upcoming spec instead specifies a Tree Walk through the parent domains. So, for example, "a.b.c.d.example.com.au" and "example.com.au" have the same Organizational Domain, because _dmarc.example.com.au is the only defined DMARC record among all the subdomains involved, including _dmarc.au. As this allows domain owners to define domain roles, it is deemed to be more accurate than the Public Suffix List.

Like SPF and DKIM, DMARC uses the concept of a domain owner, the entity or entities authorized to make changes to a given DNS domain.

SPF checks that the IP address of the sending server is authorized by the owner of the domain that appears in the SMTP `MAIL FROM` command. (The email address in MAIL FROM is also called the bounce address, envelope-from or RFC5321.MailFrom.) In addition to requiring that the SPF check passes, DMARC checks that RFC5321.MailFrom aligns with 5322.From.

DKIM allows parts of an email message to be cryptographically signed, and the signature must cover the From field. Within the DKIM-Signature mail header, the `d=` (domain) and `s=` (selector) tags specify where in DNS to retrieve the public key for the signature. A valid signature proves that the signer is a domain owner, and that the From field hasn't been modified since the signature was applied. There may be several DKIM signatures on an email message; DMARC requires one valid signature where the domain in the `d=` tag aligns with the sender's domain stated in the `From:` header field.

## DNS record

DMARC records are published in DNS with a subdomain label `_dmarc`, for example `_dmarc.example.com`. Compare this to SPF at `example.com`, and DKIM at `selector._domainkey.example.com`.

The content of the TXT resource record consists of `name=value` tags, separated by semicolons, similar to SPF and DKIM.

The available tags are:

- **adkim**, DKIM alignment mode (default `r` for relaxed, alternatively `s` for strict)
- **aspf**, SPF alignment mode (default `r` for relaxed, alternatively `s` for strict)
- **fo**, failure reporting options (default `0`, alternatively `1`, `d`, or `s`)
- **p**, policy (see below),
- **pct**, percent of "bad" email on which to apply the policy (default `100`)
- **rf**, format for message-specific failure reports
- **ri**, requested interval between aggregate reports
- **rua**, URI to send aggregate reports to
- **ruf**, URI to send failure/forensic reports to
- **sp**, subdomain policy (default same as `p`),
- **v**, version,

For example:

```
"v=DMARC1;p=none;sp=quarantine;pct=100;rua=mailto:dmarcreports@example.com;"
```

In this example, the entity controlling the example.com DNS domain intends to monitor SPF and/or DKIM failure rates and doesn't expect email to be sent from subdomains of example.com. Note that a subdomain can publish its own DMARC record; receivers must check it out before falling back to the organizational domain record.

### Step by step adoption

The protocol provides for various ratchets, or transitional states, to allow mail admins to gradually transition from not implementing DMARC at all, all the way through to an unyielding setup. The concept of stepwise adoption assumes that the goal of DMARC is the strongest setting, which is not the case for all domains. Regardless of intent, these mechanisms allow for greater flexibility.

#### Policy

First and foremost, there are three policies:

- **none** is the entry level policy. No special treatment is required by receivers, but enables a domain to receive feedback reports.
- **quarantine** asks receivers to treat messages that fail DMARC check with suspicion. Different receivers have different means to implement that, for example flag messages or deliver them in the spam folder.
- **reject** asks receivers to outright reject messages that fail DMARC check.

The policy published can be mitigated by applying it to only a percentage of the messages that fail DMARC check. Receivers are asked to select the given percentage of messages by a simple Bernoulli sampling algorithm. The rest of the messages should undergo the lower policy; that is, none if `p=quarantine`, quarantine if `p=reject`. If not specified, pct defaults to 100% of messages. The case `p=quarantine; pct=0;` is being used to force mailing list managers to rewrite the From: field, as some don't do so when `p=none`.

Finally, the subdomain policy, `sp=` and the newly added no-domain policy, `np=` allow tweaking the policy for specific subdomains.

## Reports

DMARC is capable of producing two separate types of reports. Aggregate reports are sent to the address specified following the `rua`. Forensic reports are emailed to the address following the `ruf` tag. These mail addresses must be specified in URI mailto format (e.g. mailto:worker@example.net ). Multiple reporting addresses are valid and must each be in full URI format, separated by a comma.

Target email addresses can belong to external domains. In that case, the target domain has to set up a DMARC record to say it agrees to receive them, otherwise it would be possible to exploit reporting for spam amplification. For example, say `receiver.example` receives a mail message `From: someone@sender.example` and wishes to report it. If it finds `ruf=mailto:some-id@thirdparty.example`, it looks for a confirming DNS record in the namespace administered by the target, like this:

```mw
sender.example._report._dmarc.thirdparty.example IN TXT "v=DMARC1;"
```

### Aggregate reports

Aggregate Reports are sent as XML files, typically once per day. The subject mentions the "Report Domain", which indicates the DNS domain name about which the report was generated, and the "Submitter", which is the entity issuing the report. The payload is in an attachment with a long filename consisting of bang-separated elements such as the report-issuing receiver, the begin and end epochs of the reported period as Unix-style time stamps, an optional unique identifier and an extension which depends on the possible compression (used to be `.zip`).

For example: `example.com!example.org!1475712000!1475798400.xml.gz`.

The XML content consists of a header, containing the policy on which the report is based and report metadata, followed by a number of records. Records can be put in a database as a relation and viewed in a tabular form. The XML schema is defined in Appendix C of specifications and a raw record is exemplified in dmarc.org. Here we stick with a relational example, which better conveys the nature of the data. DMARC records can also be directly transformed in HTML by applying an XSL stylesheet.

DMARC rows of an aggregate record shown in tabular form

Source IP

Count

Disposition

SPF

DKIM

Header from

SPF domain (result)

DKIM domain (result)

192.0.2.1

12

none

Pass

Pass

example.org

example.org (

Pass

)

example.org (

Pass

)

192.0.2.1

1

none

Pass

✗

Fail

example.org

example.org (

Pass

)

example.org (

✗

Fail

)

192.0.2.28

42

none

✗

Fail

Pass

example.org

example.org (

✗

Fail

)

example.org (

Pass

)

forwarder.example (

Pass

)

192.0.2.82

21

none

✗

Fail

✗

Fail

example.org

discusslist.example (

Pass

)

example.org (

✗

Fail

)

discusslist.example (

Pass

)

...

Rows are grouped by source IP and authentication results, passing just the count of each group. The leftmost result columns, labelled **SPF** and **DKIM** show DMARC-wise results, either pass or fail, taking alignment into account. The rightmost ones, with similar labels, show the name of the domain which claims to participate in the sending of the message and (in parentheses) the authentication status of that claim according to the original protocol, SPF or DKIM, regardless of Identifier Alignment. On the right side, SPF can appear at most twice, once for the `Return-Path:` test and once for the `HELO` test; DKIM can appear once for each signature present in the message. In the example, the first row represents the main mail flow from example.org, and the second row is a DKIM glitch, such as signature breakage due to a minor alteration in transit. The third and fourth rows show typical failures modes of a forwarder and a mailing list, respectively. DMARC authentication failed for the last row only; it could have affected the message disposition if example.org had specified a strict policy.

The **disposition** reflects the policy published actually applied to the messages, *none*, *quarantine*, or *reject*. Along with it, not shown in the table, DMARC provides for a policy override. Some reasons why a receiver can apply a policy different from the one requested are already provided for by the specification:

***forwarded***

while keeping the same bounce address, usually doesn't break DKIM,

***sampled out***

because a sender can choose to apply the policy to a percentage of messages only,

***trusted forwarder***

the message arrived from a locally known source

***mailing list***

the receiver heuristically determined that the message arrived from a mailing list,

***local policy***

receivers are obviously free to apply the policy they like, it is just cool to let senders know,

***other***

if none of the above applies, a comment field allows to say more.

### Failure Reports

Failure Reports, also known as Forensic Reports, are generated in real time and consist of possibly redacted copies of individual messages that failed SPF, DKIM or both based upon what value is specified in the `fo` tag. Their format, an extension of Abuse Reporting Format, resembles that of regular bounces in that they contain either a "message/rfc822" or a "text/rfc822-headers".

Forensic Reports also contain the following:

- Source IP Address (message sender)
- Source Port (after RFC 6692)
- From email address
- Recipient email address
- Email subject line
- SPF and DKIM authentication results
- Received time
- Email message headers which include the sending host, email message ID, DKIM signature, and any other custom header information.

## Compatibility

### Forwarders

There are several different types of email forwarding, some of which may break SPF. This is one of the reasons why email forwarding can affect DMARC authentication results.

### Mailing lists

Mailing lists are a frequent cause of legitimate breakage of the original author's domain DKIM signature, for example by adding a prefix to the subject header. A number of workarounds are possible, and mailing list software packages are working on solutions.

#### Turn off all message modifications

This workaround keeps the standard mailing list workflow, and is adopted by several large mailing list operators, but precludes the list adding footers and subject prefixes. This requires careful configuration of mailing software to make sure signed headers are not reordered or modified. A misconfigured email server may put List-id in its DKIM of messages sent to a mailing list, and then the list operator is forced to reject it or do From: rewriting.

#### `From:` rewriting

One of the most popular and least intrusive workarounds consists of rewriting the `From:` header field. The original author's address can then be added to the `Reply-To:` field. Rewriting can range from just appending `.INVALID` to the domain name, to allocating a temporary user ID where a modified version of the user's address is used, or an opaque ID is used, which keeps the user's "real" email address private from the list. In addition, the display name can be changed so as to show both the author and the list (or list operator). Those examples would result, respectively, in one of the following:

```mw
From: John Doe <user@example.com.INVALID>
From: John Doe <user@example.com.dmarc.fail>
From: John Doe <243576@mailinglist.example.org>
From: John Doe via MailingList <list@mailinglist.example.org>
Reply-To: John Doe <user@example.com>
```

The last line, `Reply-To:`, has to be designed in order to accommodate reply-to-author functionality, in which case reply-to-list functionality is covered by the preceding change in the `From:` header field. That way, the original meaning of those fields is reversed.

Altering the author is not fair in general, and can break the expected relationship between meaning and appearance of that datum. It also breaks automated use of it. There are communities which use mailing lists to coordinate their work, and deploy tools which use the `From:` field to attribute authorship to attachments.

#### Other workarounds

Wrapping the message works nicely, for those who use an email client which understands wrapped messages. Not doing any change is perhaps the most obvious solution, except that they seem to be legally required in some countries, and that routinely losing SPF authentication may render overall authentication more fragile.

### Sender field

Making changes to the `From:` header field to pass DKIM alignment may bring the message out of compliance with RFC 5322 section 3.6.2: "The 'From:' field specifies the author(s) of the message, that is, the mailbox(es) of the person(s) or system(s) responsible for the writing of the message." Mailbox refers to the author's email address. The `Sender:` header is available to indicate that an email was sent on behalf of another party, but DMARC only checks policy for the From domain and ignores the Sender domain.

Both ADSP and DMARC reject using the Sender field on the non-technical basis that many user agents do not display this to the recipient.

## History

A draft DMARC specification has been maintained since 30 January 2012.

In October 2013, GNU Mailman 2.1.16 was released with options to handle posters from a domain with the DMARC policy of `p=reject`. The change tried to anticipate the interoperability issues expected in case restrictive policies were applied to domains with human users (as opposed to purely transactional mail domains).

In April 2014, Yahoo changed its DMARC policy to `p=reject`, thereby causing misbehavior in several mailing lists. A few days later, AOL also changed its DMARC policy to `p=reject`. Those moves resulted in a significant amount of disruption, and those mailbox providers have been accused of forcing the costs of their own security failures onto third parties. As of 2020, the FAQ in the official DMARC wiki contains several suggestions for mailing lists to handle messages from a domain with a strict DMARC policy, of which the most widely implemented is the mailing list changing the “From” header to an address in its own domain.

An IETF working group was formed in August 2014 in order to address DMARC issues, starting from interoperability concerns and possibly continuing with a revised standard specification and documentation. Meanwhile, the existing DMARC specification had reached an editorial state agreed upon and implemented by many. It was published in March 2015 on the Independent Submission stream in the "Informational" (non-standard) category as RFC 7489.

In March 2017, the Federal Trade Commission published a study on DMARC usage by businesses. Out of 569 businesses, the study found about a third implemented any DMARC configuration, fewer than 10% used DMARC to instruct servers to reject unauthenticated messages, and a majority had implemented SPF.

An updated RFC 9989 was published in May 2026.

### Contributors

The contributors of the DMARC specification include:

- Receivers: AOL, Comcast, Google (Gmail), Mail.Ru, Microsoft (Outlook.com, Hotmail), Netease (163.com, 126.com, 188.com, yeah.net), XS4ALL, Yahoo, Yandex
- Senders: American Greetings, Bank of America, Facebook, Fidelity Investments, JPMorganChase, LinkedIn, PayPal, Twitter
- Intermediaries & Vendors: Agari (Founder/CEO Patrick R. Peterson), Cloudmark, Red Sift, ReturnPath, Trusted Domain Project, ProDMARC,

## Commercial services

Popular services that perform DMARC analysis and/or record validation include Red Sift, Valimail, dmarcian, DMARC Advisor and EasyDmarc and Cloudflare.
