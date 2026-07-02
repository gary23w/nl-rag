---
title: "SSH File Transfer Protocol"
source: https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol
domain: paramiko-ssh
license: CC-BY-SA-4.0
tags: python paramiko, paramiko ssh client, sftp python
fetched: 2026-07-02
---

# SSH File Transfer Protocol

In computing, the **SSH File Transfer Protocol**, also known as **Secure File Transfer Protocol** (**SFTP**), is a network protocol that provides file access, file transfer, and file management over any reliable data stream. It was designed by the Internet Engineering Task Force (IETF) as an extension of the Secure Shell protocol (SSH) version 2.0 to provide secure file transfer capabilities, and is seen as a replacement of File Transfer Protocol (FTP) due to superior security. The IETF Internet Draft states that, even though this protocol is described in the context of the SSH-2 protocol, it could be used in a number of different applications, such as secure file transfer over Transport Layer Security (TLS) and transfer of management information in VPN applications.

This protocol assumes that it is run over a secure channel, such as SSH, that the server has already authenticated the client, and that the identity of the client user is available to the protocol.

The official URI scheme is `sftp`.

## Capabilities

Compared to the SCP protocol, which only allows file transfers, the SFTP protocol allows for a range of operations on remote files which make it more like a remote file system protocol. An SFTP client's extra capabilities include resuming interrupted transfers, directory listings, and remote file removal. There is also support for all UNIX file types, including symbolic links.

SFTP attempts to be more platform-independent than SCP; with SCP, for instance, the expansion of wildcards specified by the client is up to the server, whereas SFTP's design avoids this problem. While SCP is most frequently implemented on Unix platforms, SFTP servers are commonly available on most platforms. In SFTP, the file transfer can be easily terminated without terminating a session like other mechanisms do.

SFTP is not FTP run over SSH, but rather a new protocol designed from the ground up by the IETF SECSH working group. It is sometimes confused with Simple File Transfer Protocol.

The protocol itself does not provide authentication and security; it expects the underlying protocol to secure this. SFTP is most often used as subsystem of SSH protocol version 2 implementations, having been designed by the same working group. It is possible, however, to run it over SSH-1 (and some implementations support this), or other data streams. However, running an SFTP server over SSH-1 is not platform-independent, as SSH-1 does not support the concept of subsystems. An SFTP client connecting to an SSH-1 server must be aware of the path to the SFTP server binary on the server side.

Uploaded files may be associated with their basic attributes, such as time stamps. This is an advantage over the common FTP protocol.

## History and development

The Internet Engineering Task Force (IETF) working group "Secsh" that was responsible for the development of the Secure Shell version 2 protocol (RFC 4251) also attempted to draft an extension of that standard for secure file transfer functionality. Internet Drafts were created that successively revised the protocol into new versions. The software industry began to implement various versions of the protocol before the drafts were standardized. As development work progressed, the scope of the Secsh File Transfer project expanded to include file access and file management. Eventually, development stalled as some committee members began to view SFTP as a file system protocol, not just a file access or file transfer protocol, which places it beyond the purview of the working group. After a seven-year hiatus, in 2013 an attempt was made to restart work on SFTP using the version 3 draft as the baseline.

### Versions 0–2

Prior to the IETF's involvement, SFTP was a proprietary protocol of SSH Communications Security, designed by Tatu Ylönen with assistance from Sami Lehtinen in 1997. Differences between versions 0–2 and version 3 are enumerated upon in section 10 of draft-ietf-secsh-filexfer-02.

### Version 3

At the outset of the IETF Secure Shell File Transfer project, the Secsh group stated that its objective of SSH File Transfer Protocol was to provide a secure file transfer functionality over any reliable data stream, and to be the standard file transfer protocol for use with the SSH-2 protocol.

Drafts 00–02 of the IETF Internet Draft define successive revisions of version 3 of the SFTP protocol.

- SSH File Transfer Protocol, Draft 00, January 2001
- SSH File Transfer Protocol, Draft 01, March 2001
- SSH File Transfer Protocol, Draft 02, October 2001

### Version 4

Drafts 03–04 of the IETF Internet Draft define version 4 of the protocol.

- SSH File Transfer Protocol, Draft 03, October 2002
- SSH File Transfer Protocol, Draft 04, December 2002

### Version 5

Draft 05 of the IETF Internet Draft defines version 5 of the protocol.

- SSH File Transfer Protocol, Draft 05, January 2004

### Version 6

Drafts 06–13 of the IETF Internet Draft define successive revisions of version 6 of the protocol.

- SSH File Transfer Protocol, Draft 06, October 2004
- SSH File Transfer Protocol, Draft 07, March 2005
- SSH File Transfer Protocol, Draft 08, April 2005
- SSH File Transfer Protocol, Draft 09, June 2005 – Added byte-range locks. ACL changes. Rearranged SSH_FXP_REALPATH request parameters.
- SSH File Transfer Protocol, Draft 10, June 2005 – Extensions "vendor-id", "md5-hash", "space-available", "home-directory" removed. ACL changes.
- SSH File Transfer Protocol, Draft 11, January 2006 – ACL transfer fully specified. Editorial changes.
- SSH File Transfer Protocol, Draft 12, January 2006 – Added "IANA considerations". A size parameter is now allowed for file creation as an advisory signal.
- SSH File Transfer Protocol, Draft 13, July 2006 – editorial changes

### Extensions

The SFTP protocol supports a generic way of indicating extended commands, along with a method of including them in version negotiation. An IANA registry is requested, but since the protocol never became an official standard, no such registry has been created.

- Draft 13 specifies text-seek, supported2, acl-supported, newline, versions, version-select, filename-charset, filename-translation-control.
- OpenSSH, the most widespread implementation, defines constants to convert ST_NOSUID and ST_RDONLY values across the protocol, using the statvfs@openssh.com version identifier. It only implements version 3 from draft 1.

## Software

### SFTP client

The term **SFTP** can also refer to Secure file transfer program, a command-line program that implements the client part of this protocol. As an example, the sftp program supplied with OpenSSH implements this.

Some implementations of the `scp` *program* support both the SFTP and SCP protocols to perform file transfers, depending on what the server supports. The scp program supplied with OpenSSH 9.0 and higher defaults to using SFTP.

### SFTP server

Some FTP server implementations implement the SFTP protocol; however, outside of dedicated file servers, SFTP protocol support is usually provided by an SSH server implementation, as it shares the default port of 22 with other SSH services. SFTP implementations may include an SSH protocol implementation to leverage integration of SSH connection details with preexisting FTP server access controls, where an alternative SSH server is tolerable or where alternative ports may be used. An SSH-2 server which supports subsystems may be leveraged to keep a uniform SSH implementation while enhancing access controls with third party software, at the cost of fine-grained integration with connection details, and SSH-1 compatibility.

### SFTP proxy

It is difficult to control SFTP transfers on security devices at the network perimeter. There are standard tools for logging FTP transactions, like TIS gdev or SUSE FTP proxy, but SFTP is encrypted, rendering traditional proxies ineffective for controlling SFTP traffic.

There are some tools that implement man-in-the-middle for SSH which also feature SFTP control. Examples of such a tool are Shell Control Box from Balabit and CryptoAuditor from SSH Communications Security (the original developer of the Secure Shell protocol) which provides functions such as SFTP transaction logging and logging of the actual data transmitted on the wire.
