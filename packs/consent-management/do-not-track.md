---
title: "Do Not Track"
source: https://en.wikipedia.org/wiki/Do_Not_Track
domain: consent-management
license: CC-BY-SA-4.0
tags: consent management platform, informed consent record, cookie consent banner, privacy policy disclosure, do not track
fetched: 2026-07-02
---

# Do Not Track

**Do Not Track** (**DNT**) is a deprecated non-standard HTTP header field designed to allow internet users to opt out of tracking by websites, which includes the collection of data regarding a user's activity across multiple distinct contexts, and the retention, use, or sharing of data derived from that activity outside the context in which it occurred.

The Do Not Track header was originally proposed in 2009 and was adopted by most major browsers within a few years. However, the header failed to find widespread respect among publishers, due to the lack of legislation requiring companies to support the DNT header and confusion about the header's meaning. The DNT header was abandoned by standards bodies such as the W3C. As of 2025, some browsers had removed the header, including Apple Safari and Mozilla Firefox.

Following the failure of the DNT initiative, a coalition of US-based internet companies announced the creation of the Global Privacy Control header which is intended to have explicit legal force under privacy legislation.

The DNT header accepts three values: `1` in case the user does not want to be tracked *(opt-out)*, `00` in case the user consents to be tracked *(opt-in)*, or *null* (no header sent) if the user has not expressed a preference. The default behavior required by the document draft is not to send the header unless the user enables the setting via their browser or their choice is implied by the use of that specific browser.

## History

### Browser support

| Browser | Added | Removed | Comment |   |   |
|---|---|---|---|---|---|
| Version | Release date | Version | Release date |   |   |
| Firefox | 4.0 | March 22, 2011 | 135 | February 4, 2025 | Header disabled by default |
| Google Chrome | 23 | June 11, 2012 | N/A | N/A | Header disabled by default |
| Safari | 6 | July 25, 2012 | 12.1 | March 25, 2019 | Header disabled by default |
| Microsoft Edge | 12 | July 29, 2015 | N/A | N/A | Header disabled by default |
| Internet Explorer | 9 | March 14, 2011 |   |   | Different browser version |
| Pale Moon | 4.0 | March 27, 2011 | 31.0.0 | May 10, 2022 | Replaced by Sec-GPC |

## Implementation

The Do Not Track specification defines that if the user wishes to not be tracked, the client submits the following HTTP header:

`DNT: 1`

Alternative permitted values are `0` if the user prefers to permit tracking, and `null` if the user has not expressed a preference.

The user's DNT preference can also be read from the JavaScript `navigator.doNotTrack` property which returns one of the values `1`, `0` or `null`.

### Development

In 2007, several consumer advocacy groups asked the U.S. Federal Trade Commission (FTC) to create a Do Not Track list for online advertising. The proposal would have required that online advertisers submit their information to the FTC, which would compile a machine-readable list of the domain names used by those companies to place cookies or otherwise track consumers.

In July 2009, researchers Christopher Soghoian and Sid Stamm implemented support for the Do Not Track header in the Firefox web browser via a prototype add-on. Stamm was, at the time, a privacy engineer at Mozilla, while Soghoian soon afterward started working at the FTC. One year later, during a U.S. Senate privacy hearing, FTC Chairman Jon Leibowitz told the Senate Commerce Committee that the commission was exploring the idea of proposing a "do-not-track" list.

In December 2010, the FTC issued a privacy report that called for a "do-not-track" system that would enable people to avoid having their actions being monitored online.

One week later, Microsoft announced that its next browser would include support for Tracking Protection Lists that block tracking of consumers using blacklists supplied by third parties. In January 2011, Mozilla announced that its Firefox browser would soon provide a Do Not Track solution, via a browser header. Microsoft's Internet Explorer 9, Apple's Safari, Opera and Google Chrome all later added support for the header approach.

In August 2015, a coalition of privacy groups led by the Electronic Frontier Foundation using W3C's Tracking Preference Expression (DNT) standard proposed that "Do not track" be the goal for advocates to demand of businesses.

In January 2019, the W3C Tracking Protection Working Group was disbanded, citing "insufficient deployment of these extensions" and lack of "indications of planned support among user agents, third parties, and the ecosystem at large". Beginning the following month, Apple removed DNT support from Safari starting from version 12.1, citing that it could be used as a "fingerprinting variable" for tracking.

In December 2024, developer builds of Firefox lost support for the DNT header. Mozilla updated documentation about DNT to clarify that the browser no longer supports the header and recommended to use Global Privacy Control header instead. On February 4, 2025, Firefox 135.0 removed support for the DNT header for all users.

### Internet Explorer 10 default setting controversy

When using the "Express" settings upon installation, a Do Not Track option is enabled by default for Internet Explorer 10 and Windows 8. Microsoft faced criticism for its decision to enable Do Not Track by default from advertising companies, who say that use of the Do Not Track header should be a choice made by the user and must not be automatically enabled. The companies also said that this decision would violate the Digital Advertising Alliance's agreement with the U.S. government to honor a Do Not Track system, because the coalition said it would only honor such a system if it were not enabled by default by web browsers. A Microsoft spokesperson defended its decision however, stating that users would prefer a web browser that automatically respected their privacy.

On September 7, 2012, Roy Fielding, an author of the Do Not Track proposal, committed a patch to the source code of the Apache HTTP Server, which would make the server explicitly ignore any use of the Do Not Track header by users of Internet Explorer 10. Fielding wrote that Microsoft's decision "deliberately violates" the Do Not Track specification because it "does not protect anyone's privacy unless the recipients believe it was set by a real human being, with a real preference for privacy over personalization". The Do Not Track specification did not explicitly mandate that the use of Do Not Track actually be a choice until after the feature was implemented in Internet Explorer 10. According to Fielding, Microsoft knew its Do Not Track signals would be ignored, and that its goal was to effectively give an illusion of privacy while still catering to their own interests. On October 9, 2012, Fielding's patch was commented out, restoring the previous behavior.

On April 3, 2015, Microsoft announced that starting with Windows 10, it would comply with the specification and no longer automatically enable Do Not Track as part of the operating system's "Express" default settings, but that the company will "provide customers with clear information on how to turn this feature on in the browser settings should they wish to do so".

## Adoption

Very few advertising companies actually supported DNT, due to a lack of regulatory or voluntary requirements for its use and unclear standards over how websites should respond to the header. Websites that honor DNT requests include Medium and Pinterest. Despite offering the option in its Chrome web browser, Google did not implement support for DNT on its websites, and directed users to its online privacy settings and opt-outs for interest-based advertising instead. The Digital Advertising Alliance, Council of Better Business Bureaus and the Data & Marketing Association does not require its members to honor DNT signals.

Usage of ad blocking software to block web trackers and advertising has become increasingly common, with users citing both privacy concerns and performance impact as justification for its use. Apple and Mozilla have begun to add privacy enhancements, such as "tracking protection", to their browsers, designed to reduce undue cross-site tracking. In addition, laws such as the European Union's General Data Protection Regulation (GDPR) have imposed restrictions on how companies are to store and process personal information.

Princeton University associate professor of computer science Jonathan Mayer, who was a member of the W3C's working group for DNT, argued that the concept is a "failed experiment".

## Replacement by Global Privacy Control

In 2020, a coalition of US-based internet companies announced the Global Privacy Control header that intended to replace the DNT header. The creators hope that this new header will meet the definition of "user-enabled global privacy controls" defined by the California Consumer Privacy Act (CCPA) and the European General Data Protection Regulation (GDPR). In this case, the new header would be automatically strengthened by existing laws and companies would be required to honor it.
