---
title: "Moxie Marlinspike"
source: https://en.wikipedia.org/wiki/Moxie_Marlinspike
domain: hsts-preload
license: CC-BY-SA-4.0
tags: http strict transport security, hsts preload list, ssl stripping defense, https enforcement policy
fetched: 2026-07-02
---

# Moxie Marlinspike

**Moxie Marlinspike** is an American entrepreneur, cryptographer, and computer security researcher. Marlinspike is the creator of Signal, co-founder of the Signal Technology Foundation, and served as the first CEO of Signal Messenger LLC. He is also a co-author of the Signal Protocol encryption used by Signal, WhatsApp, Google Messages, Facebook Messenger, and Skype.

Marlinspike is a former head of the security team at Twitter and the author of a proposed SSL authentication system replacement called Convergence. He previously maintained a cloud-based WPA cracking service and a targeted anonymity service called GoogleSharing.

## Career

Marlinspike began his career working for several technology companies, including enterprise infrastructure software maker BEA Systems Inc.

In 2010, Marlinspike was the chief technology officer and co-founder of Whisper Systems, an enterprise mobile security startup company. In May 2010, Whisper Systems launched TextSecure and RedPhone. These were applications that provided end-to-end encrypted SMS messaging and voice calling, respectively. Twitter acquired the company for an undisclosed amount in late 2011. The acquisition was done "primarily so that Mr. Marlinspike could help the then-startup improve its security". During his time as Twitter's head of cybersecurity, the firm made Whisper Systems' apps open source.

Marlinspike left Twitter in early 2013 and founded Open Whisper Systems as a collaborative open source project for the continued development of TextSecure and RedPhone. At the time, Marlinspike and Trevor Perrin started developing the Signal Protocol, an early version of which was first introduced in the TextSecure app in February 2014. In November 2015, Open Whisper Systems unified the TextSecure and RedPhone applications as Signal. Between 2014 and 2016, Marlinspike worked with WhatsApp, Facebook, and Google to integrate the Signal Protocol into their messaging services.

In 2017, Marlinspike assisted the cryptocurrency company MobileCoin as an early technical advisors alongside fellow former DARPA researcher Todd Huffman. MobileCoin was designed to be the in-app payments for Signal and Mixin Messenger.

On February 21, 2018, Marlinspike and WhatsApp co-founder Brian Acton announced the formation of the Signal Technology Foundation and its subsidiary, Signal Messenger LLC. Marlinspike served as Signal Messenger's first CEO until stepping down on January 10, 2022. In the wake of the United States government group chat leak Marlinspike posted in March 2025: "There are so many great reasons to be on Signal. Now including the opportunity for the vice president of the United States of America to randomly add you to a group chat for coordinating sensitive military operations. Don't sleep on this opportunity..."

## Research

### SSL stripping

In a 2009 paper, Marlinspike introduced the concept of SSL stripping, a man-in-the-middle attack in which a network attacker could prevent a web browser from upgrading to an SSL connection in a way that would likely go unnoticed by a user. He also announced the release of a tool, `sslstrip`, that would automatically perform these types of man-in-the-middle attacks. The HTTP Strict Transport Security (HSTS) specification was subsequently developed to combat these attacks.

### SSL implementation attacks

Marlinspike has discovered a number of different vulnerabilities in popular SSL implementations. Notably, he published a 2002 paper on exploiting SSL/TLS implementations that did not correctly verify the X.509 v3 "BasicConstraints" extension in public key certificate chains. This allowed anyone with a valid CA-signed certificate for any domain name to create what appeared to be valid CA-signed certificates for any other domain. The vulnerable SSL/TLS implementations included the Microsoft CryptoAPI, making Internet Explorer and all other Windows software that relied on SSL/TLS connections vulnerable to a man-in-the-middle attack. In 2011, the same vulnerability was discovered to have remained in the SSL/TLS implementation on Apple Inc.'s iOS. Also notably, Marlinspike presented a 2009 paper in which he introduced the concept of a null-prefix attack on SSL certificates. He revealed that all major SSL implementations failed to properly verify the Common Name value of a certificate, so that they could be tricked into accepting forged certificates by embedding null characters into the CN field.

### Solutions to the CA problem

In 2011, Marlinspike presented a talk, "SSL And The Future Of Authenticity", at the Black Hat security conference in Las Vegas. He outlined many of the problems with certificate authorities and announced the release of a software project called Convergence to replace them. In 2012, Marlinspike and Perrin submitted an Internet Draft for TACK, which is designed to provide SSL certificate pinning and help solve the CA problem, to the Internet Engineering Task Force.

### Cracking MS-CHAPv2

In 2012, Marlinspike and David Hulton presented research that makes it possible to reduce the security of MS-CHAPv2 handshakes to a single DES encryption. Hulton built hardware capable of cracking the remaining DES encryption in less than 24 hours, and the two made the hardware available for anyone to use as an Internet service.

### Mobily surveillance controversy

In 2013, Marlinspike published emails on his blog that he claimed were from Saudi Arabian telecom service Mobily soliciting his help in surveilling their customers, including intercepting communications running through various applications. Marlinspike refused to help, making the emails public instead. Mobily denied the allegations. "We never communicate with hackers", the company said.

## Traveling

Marlinspike says that when flying within the United States he is unable to print his own boarding pass, is required to have airline ticketing agents make a phone call in order to issue one, and is subjected to secondary screening at TSA security checkpoints.

While entering the U.S. on a flight from the Dominican Republic in 2010, Marlinspike was detained by federal agents for nearly five hours, all his electronic devices were confiscated, and at first agents claimed he would only get them back if he provided his passwords so they could decrypt the data. Marlinspike refused to do this, and the devices were eventually returned, though he noted that he could no longer trust them, saying, "They could have modified the hardware or installed new keyboard firmware."

## Recognition

- In 2016, *Fortune* magazine named Marlinspike among its 40 under 40 for being the founder of Open Whisper Systems and "[encrypting] the communications of more than a billion people worldwide". *Wired* also named him to its "Next List 2016," as one of "25 Geniuses Who Are Creating the Future of Business."
- In 2017, Marlinspike and Perrin were awarded the Levchin Prize for Real World Cryptography "for the development and wide deployment of the Signal protocol".

## Personal life

Originally from the state of Georgia, Marlinspike moved to San Francisco in the late 1990s at age 18. The name *Moxie Marlinspike* is an assumed name partly derived from a childhood nickname.

Marlinspike is a sailing enthusiast and master mariner. In 2004, he bought a derelict sailboat and, with three friends, refurbished it and sailed around the Bahamas while making a "video zine" about their journey called *Hold Fast*. He is also an anarchist, and several of his essays and speeches are published on the website *The Anarchist Library*, including "An Anarchist Critique of Democracy" and "The Promise of Defeat."
