---
title: "Transport Layer Security (part 3/3)"
source: https://en.wikipedia.org/wiki/Transport_Layer_Security
domain: security
license: CC-BY-SA-4.0 (OWASP) / CC-BY-SA-4.0 (Wikipedia)
tags: security, authentication, password hashing, session token, tls, owasp
fetched: 2026-07-02
part: 3/3
---

## Protocol details

The TLS protocol exchanges *records*, which encapsulate the data to be exchanged in a specific format (see below). Each record can be compressed, padded, appended with a message authentication code (MAC), or encrypted, all depending on the state of the connection. Each record has a *content type* field that designates the type of data encapsulated, a length field and a TLS version field. The data encapsulated may be control or procedural messages of the TLS itself, or simply the application data needed to be transferred by TLS. The specifications (cipher suite, keys etc.) required to exchange application data by TLS, are agreed upon in the "TLS handshake" between the client requesting the data and the server responding to requests. The protocol therefore defines both the structure of payloads transferred in TLS and the procedure to establish and monitor the transfer.

### TLS handshake

When the connection starts, the record encapsulates a "control" protocol – the handshake messaging protocol (*content type* 22). This protocol is used to exchange all the information required by both sides for the exchange of the actual application data by TLS. It defines the format of messages and the order of their exchange. These may vary according to the demands of the client and server – i.e., there are several possible procedures to set up the connection. This initial exchange results in a successful TLS connection (both parties ready to transfer application data with TLS) or an alert message (as specified below).

#### Basic TLS handshake

A typical connection example follows, illustrating a handshake where the server (but not the client) is authenticated by its certificate:

1. Negotiation phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and suggested compression methods. If the client is attempting to perform a resumed handshake, it may send a *session ID*. If the client can use Application-Layer Protocol Negotiation, it may include a list of supported application protocols, such as HTTP/2.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. To confirm or allow resumed handshakes the server may send a *session ID*. The chosen protocol version should be the highest that both the client and server support. For example, if the client supports TLS version 1.1 and the server supports version 1.2, version 1.1 should be selected; version 1.2 should not be selected.
  - The server sends its **Certificate** message (depending on the selected cipher suite, this may be omitted by the server).
  - The server sends its **ServerKeyExchange** message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon cipher suites.
  - The server sends a **ServerHelloDone** message, indicating it is done with handshake negotiation.
  - The client responds with a **ClientKeyExchange** message, which may contain a *PreMasterSecret*, public key, or nothing. (Again, this depends on the selected cipher.) This *PreMasterSecret* is encrypted using the public key of the server certificate.
  - The client and server then use the random numbers and *PreMasterSecret* to compute a common secret, called the "master secret". All other key data (session keys such as IV, symmetric encryption key, MAC key) for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function.
2. The client now sends a **ChangeCipherSpec** record, essentially telling the server, "Everything I tell you from now on will be authenticated (and encrypted if encryption parameters were present in the server certificate)." The ChangeCipherSpec is itself a record-level protocol with content type of 20.
  - The client sends an authenticated and encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The server will attempt to decrypt the client's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be terminated.
3. Finally, the server sends a **ChangeCipherSpec**, telling the client, "Everything I tell you from now on will be authenticated (and encrypted, if encryption was negotiated)."
  - The server sends its authenticated and encrypted **Finished** message.
  - The client performs the same decryption and verification procedure as the server did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be authenticated and optionally encrypted exactly like in their *Finished* message. Otherwise, the content type will return 25 and the client will not authenticate.

#### Client-authenticated TLS handshake

The following *full* example shows a client being authenticated (in addition to the server as in the example above; see mutual authentication) via TLS using certificates exchanged between both peers.

1. Negotiation Phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. The server may also send a *session id* as part of the message to perform a resumed handshake.
  - The server sends its **Certificate** message (depending on the selected cipher suite, this may be omitted by the server).
  - The server sends its **ServerKeyExchange** message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon ciphersuites.[1]
  - The server sends a **CertificateRequest** message, to request a certificate from the client.
  - The server sends a **ServerHelloDone** message, indicating it is done with handshake negotiation.
  - The client responds with a **Certificate** message, which contains the client's certificate, but not its private key.
  - The client sends a **ClientKeyExchange** message, which may contain a *PreMasterSecret*, public key, or nothing. (Again, this depends on the selected cipher.) This *PreMasterSecret* is encrypted using the public key of the server certificate.
  - The client sends a **CertificateVerify** message, which is a signature over the previous handshake messages using the client's certificate's private key. This signature can be verified by using the client's certificate's public key. This lets the server know that the client has access to the private key of the certificate and thus owns the certificate.
  - The client and server then use the random numbers and *PreMasterSecret* to compute a common secret, called the "master secret". All other key data ("session keys") for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function.
2. The client now sends a **ChangeCipherSpec** record, essentially telling the server, "Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated). "The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22.
  - Finally, the client sends an encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The server will attempt to decrypt the client's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down.
3. Finally, the server sends a **ChangeCipherSpec**, telling the client, "Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated)."
  - The server sends its own encrypted **Finished** message.
  - The client performs the same decryption and verification procedure as the server did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their *Finished* message.

#### Resumed TLS handshake

Public key operations (e.g., RSA) are relatively expensive in terms of computational power. TLS provides a secure shortcut in the handshake mechanism to avoid these operations: resumed sessions. Resumed sessions are implemented using session IDs or session tickets.

Apart from the performance benefit, resumed sessions can also be used for single sign-on, as it guarantees that both the original session and any resumed session originate from the same client. This is of particular importance for the FTP over TLS/SSL protocol, which would otherwise suffer from a man-in-the-middle attack in which an attacker could intercept the contents of the secondary data connections.

#### TLS 1.3 handshake

The TLS 1.3 handshake was condensed to only one round trip compared to the two round trips required in previous versions of TLS/SSL.

To start the handshake, the client guesses which key exchange algorithm will be selected by the server and sends a **ClientHello** message to the server containing a list of supported ciphers (in order of the client's preference) and public keys for some or all of its key exchange guesses. If the client successfully guesses the key exchange algorithm, 1 round trip is eliminated from the handshake. After receiving the **ClientHello**, the server selects a cipher and sends back a **ServerHello** with its own public key, followed by server **Certificate** and **Finished** messages.

After the client receives the server's finished message, it now is coordinated with the server on which cipher suite to use.

##### Session IDs

In an ordinary *full* handshake, the server sends a *session id* as part of the **ServerHello** message. The client associates this *session id* with the server's IP address and TCP port, so that when the client connects again to that server, it can use the *session id* to shortcut the handshake. In the server, the *session id* maps to the cryptographic parameters previously negotiated, specifically the "master secret". Both sides must have the same "master secret" or the resumed handshake will fail (this prevents an eavesdropper from using a *session id*). The random data in the **ClientHello** and **ServerHello** messages virtually guarantee that the generated connection keys will be different from in the previous connection. In the RFCs, this type of handshake is called an *abbreviated* handshake. It is also described in the literature as a *restart* handshake.

1. Negotiation phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods. Included in the message is the *session id* from the previous TLS connection.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. If the server recognizes the *session id* sent by the client, it responds with the same *session id*. The client uses this to recognize that a resumed handshake is being performed. If the server does not recognize the *session id* sent by the client, it sends a different value for its *session id*. This tells the client that a resumed handshake will not be performed. At this point, both the client and server have the "master secret" and random data to generate the key data to be used for this connection.
2. The server now sends a **ChangeCipherSpec** record, essentially telling the client, "Everything I tell you from now on will be encrypted." The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22.
  - Finally, the server sends an encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The client will attempt to decrypt the server's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down.
3. Finally, the client sends a **ChangeCipherSpec**, telling the server, "Everything I tell you from now on will be encrypted."
  - The client sends its own encrypted **Finished** message.
  - The server performs the same decryption and verification procedure as the client did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their *Finished* message.

##### Session tickets

Instead of session IDs, TLS can also be extended via use of session tickets. It defines a way to resume a TLS session without requiring that session-specific state is stored at the TLS server.

When using session tickets, the TLS server stores its session-specific state in a session ticket and sends the session ticket to the TLS client for storing. The client resumes a TLS session by sending the session ticket to the server, and the server resumes the TLS session according to the session-specific state in the ticket. The session ticket is encrypted and authenticated by the server, and the server verifies its validity before using its contents.

One particular weakness of this method with OpenSSL is that it always limits encryption and authentication security of the transmitted TLS session ticket to `AES128-CBC-SHA256`, no matter what other TLS parameters were negotiated for the actual TLS session. This means that the state information (the TLS session ticket) is not as well protected as the TLS session itself. Of particular concern is OpenSSL's storage of the keys in an application-wide context (`SSL_CTX`), i.e. for the life of the application, and not allowing for re-keying of the `AES128-CBC-SHA256` TLS session tickets without resetting the application-wide OpenSSL context (which is uncommon, error-prone and often requires manual administrative intervention).

### TLS record

This is the general format of all TLS records.

General TLS record format

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Content Type

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

8

64

Protocol message(s)

12

96

⋮

⋮

⁠

5

+

m

{\displaystyle 5+m}

⁠

⁠

40

+

m

∗

8

{\displaystyle 40+m*8}

⁠

Message Authentication Code

(optional)

⋮

⋮

⋮

⋮

⁠

5

+

m

+

q

{\displaystyle 5+m+q}

⁠

⁠

40

+

(

m

+

q

)

∗

8

{\displaystyle 40+(m+q)*8}

⁠

Padding (block ciphers only)

**Content Type: 8 bits**

This field identifies the Record Layer Protocol Type contained in this record.

| Hex | Dec | Type |
|---|---|---|
| 0x14 | 20 | ChangeCipherSpec |
| 0x15 | 21 | Alert |
| 0x16 | 22 | Handshake |
| 0x17 | 23 | Application |
| 0x18 | 24 | Heartbeat |

**Legacy version: 16 bits**

This field identifies the major and minor version of TLS prior to TLS 1.3 for the contained message. For a

ClientHello

message, this need not be the

highest

version supported by the client. For TLS 1.3 and later, this must be set to

0x0303

and application must send supported versions in an extra message extension block.

| Major version | Minor version | Version type |
|---|---|---|
| 3 | 0 | SSL 3.0 |
| 3 | 1 | TLS 1.0 |
| 3 | 2 | TLS 1.1 |
| 3 | 3 | TLS 1.2 |
| 3 | 4 | TLS 1.3 |

**Length: 16 bits; Length < 214**

The length of

Protocol message(s)

,

MAC

and

Padding

fields combined. The length should not exceed 2

14

bytes (16 KiB).

**Protocol message(s): variable**

One or more messages identified by the Protocol field. Note that this field may be encrypted depending on the state of the connection. The length (in bytes) of all messages is indicated by the letter

m

.

**Message Authentication Code (MAC): 16, 20, or 32 bytes (optional)**

A

message authentication code

computed over the

Protocol message(s)

field, with additional key material included. 32 bytes for the

SHA-256

-based HMAC, 20 bytes for the

SHA-1

-based HMAC, 16 bytes for the

MD5

-based HMAC. Note that this field may be encrypted, or not included entirely, depending on the state of the connection. The length (in bytes) of the MAC is indicated by the letter

q

.

**Padding: variable (optional)**

Padding is only added when needed.

No *MAC* or *Padding* fields can be present at end of TLS records before all cipher algorithms and parameters have been negotiated and handshaked and then confirmed by sending a **CipherStateChange** record (see below) for signalling that these parameters will take effect in all further records sent by the same peer.

#### Handshake protocol

Most messages exchanged during the setup of the TLS session are based on this record, unless an error or warning occurs and needs to be signaled by an Alert protocol record (see below), or the encryption mode of the session is modified by another record (see **ChangeCipherSpec** protocol below).

Handshake TLS record format

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Content Type

(22)

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

Message Type

Handshake Message Data Length

↴

8

64

↪

Handshake Length (cont.)

12

96

Handshake Message

16

128

⋮

⋮

⋮

⋮

Handshake Message Data Length

⋮

⋮

Handshake Message

⋮

⋮

⋮

⋮

**Content Type: 8 bits; == 22**

This field indicates the

Handshake

Protocol Type.

**Message Type: 8 bits**

This field identifies the handshake message type.

| Code | Description |
|---|---|
| 0 | HelloRequest |
| 1 | ClientHello |
| 2 | ServerHello |
| 4 | NewSessionTicket |
| 8 | EncryptedExtensions (TLS 1.3 only) |
| 11 | Certificate |
| 12 | ServerKeyExchange |
| 13 | CertificateRequest |
| 14 | ServerHelloDone |
| 15 | CertificateVerify |
| 16 | ClientKeyExchange |
| 20 | Finished |

**Handshake Message Data Length: 24 bits**

This is a 3-byte field indicating the length of the handshake data, not including the header.

**Handshake Message: variable**

Data of the handshake message itself.

Note that multiple handshake messages may be combined within one record.

#### Alert protocol

This record should normally not be sent during normal handshaking or application exchanges. However, this message can be sent at any time during the handshake and up to the closure of the session. If this is used to signal a fatal error, the session will be closed immediately after sending this record, so this record is used to give a reason for this closure. If the alert level is flagged as a warning, the remote can decide to close the session if it decides that the session is not reliable enough for its needs (before doing so, the remote may also send its own signal).

Alert TLS record format

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Content Type

(21)

Legacy version (major/minor)

Length

(2)

↴

4

32

↪

Length (cont.)

Level

Description

8

64

MAC (optional)

12

96

⋮

⋮

⋮

⋮

Padding (block ciphers only)

**Content Type: 8 bits; == 21**

This field indicates the

Alert

Protocol Type.

**Length: 16 bits; == 2**

The length of the rest of fields, which is 2.

**Level: 8 bits**

This field identifies the level of alert. If the level is fatal, the sender should close the session immediately. Otherwise, the recipient may decide to terminate the session itself, by sending its own fatal alert and closing the session itself immediately after sending it. The use of Alert records is optional, however if it is missing before the session closure, the session may be resumed automatically (with its handshakes).

Normal closure of a session after termination of the transported application should preferably be alerted with at least the

Close notify

Alert type (with a simple warning level) to prevent such automatic resume of a new session. Signalling explicitly the normal closure of a secure session before effectively closing its transport layer is useful to prevent or detect attacks (like attempts to truncate the securely transported data, if it intrinsically does not have a predetermined length or duration that the recipient of the secured data may expect).

| Code | Level type | Connection state |
|---|---|---|
| 1 | **warning** | connection or security may be unstable. |
| 2 | **fatal** | connection or security may be compromised, or an unrecoverable error has occurred. |

**Description: 8 bits**

This field identifies which type of alert is being sent.

| Code | Description | Level types | Note |
|---|---|---|---|
| 0 | Close notify | **warning**/**fatal** |   |
| 10 | Unexpected message | **fatal** |   |
| 20 | Bad record MAC | **fatal** | Possibly a bad SSL implementation, or payload has been tampered with e.g. FTP firewall rule on FTPS server. |
| 21 | Decryption failed | **fatal** | TLS only, reserved |
| 22 | Record overflow | **fatal** | TLS only |
| 30 | Decompression failure | **fatal** |   |
| 40 | Handshake failure | **fatal** |   |
| 41 | No certificate | **warning**/**fatal** | SSL 3.0 only, reserved |
| 42 | Bad certificate | **warning**/**fatal** |   |
| 43 | Unsupported certificate | **warning**/**fatal** | e.g. certificate has only server authentication usage enabled and is presented as a client certificate |
| 44 | Certificate revoked | **warning**/**fatal** |   |
| 45 | Certificate expired | **warning**/**fatal** | Check server certificate expire also check no certificate in the chain presented has expired |
| 46 | Certificate unknown | **warning**/**fatal** |   |
| 47 | Illegal parameter | **fatal** |   |
| 48 | Unknown CA (Certificate authority) | **fatal** | TLS only |
| 49 | Access denied | **fatal** | TLS only – e.g. no client certificate has been presented (TLS: Blank certificate message or SSLv3: No Certificate alert), but server is configured to require one. |
| 50 | Decode error | **fatal** | TLS only |
| 51 | Decrypt error | **warning**/**fatal** | TLS only |
| 60 | Export restriction | **fatal** | TLS only, reserved |
| 70 | Protocol version | **fatal** | TLS only |
| 71 | Insufficient security | **fatal** | TLS only |
| 80 | Internal error | **fatal** | TLS only |
| 86 | Inappropriate fallback | **fatal** | TLS only |
| 90 | User canceled | **fatal** | TLS only |
| 100 | No renegotiation | **warning** | TLS only |
| 110 | Unsupported extension | **warning** | TLS only |
| 111 | Certificate unobtainable | **warning** | TLS only |
| 112 | Unrecognized name | **warning**/**fatal** | TLS only; client's Server Name Indicator specified a hostname not supported by the server |
| 113 | Bad certificate status response | **fatal** | TLS only |
| 114 | Bad certificate hash value | **fatal** | TLS only |
| 115 | Unknown PSK identity | **fatal** | TLS only. Used in TLS-PSK and TLS-SRP. |
| 116 | Certificate required | **fatal** | TLS version 1.3 only |
| 120 or 255 | No application protocol | **fatal** | TLS version 1.3 only |

#### ChangeCipherSpec protocol

ChangeCipherSpec TLS record format

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Content Type

(20)

Legacy version (major/minor)

Length

(1)

↴

4

32

↪

Length (cont.)

CCS Protocol Type

**Content Type: 8 bits; == 20**

This field indicates the

ChangeCipherSpec

Protocol Type.

**Length: 16 bits; == 1**

The length of the rest of fields, which is 1.

**CCS Protocol Type: 8 bits**

This field identifies the CCS Protocol type. There is currently only one.

#### Application protocol

Application TLS record format

Offset

Octet

0

1

2

3

Octet

Bit

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

0

Content Type

(23)

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

8

64

Application Data

12

96

⋮

⋮

⁠

5

+

m

{\displaystyle 5+m}

⁠

⁠

40

+

m

∗

8

{\displaystyle 40+m*8}

⁠

Message Authentication Code

(optional)

⋮

⋮

⋮

⋮

⁠

5

+

m

+

q

{\displaystyle 5+m+q}

⁠

⁠

40

+

(

m

+

q

)

∗

8

{\displaystyle 40+(m+q)*8}

⁠

Padding (block ciphers only)

**Content Type: 8 bits; == 23**

This field identifies the

Application

Protocol Type.

**Length: 16 bits; Length < 214**

The length of

Application Data

,

MAC

and

Padding

fields combined. The length should not exceed 2

14

bytes (16 KiB).

**Application Data: variable**

Data of the application. The length (in bytes) of the data is indicated by the letter

m

.

**Message Authentication Code (MAC): 16, 20, or 32 bytes (optional)**

A

message authentication code

computed over the

Application Data

field. 32 bytes for the

SHA-256

-based HMAC, 20 bytes for the

SHA-1

-based HMAC, 16 bytes for the

MD5

-based HMAC. The length (in bytes) of the MAC is indicated by the letter

q

.

**Padding: variable (optional)**

The last byte contains the padding length.


## Support for name-based virtual servers

From the application protocol point of view, TLS belongs to a lower layer, although the TCP/IP model is too coarse to show it. This means that the TLS handshake is usually (except in the STARTTLS case) performed before the application protocol can start. In the name-based virtual server feature being provided by the application layer, all co-hosted virtual servers share the same certificate because the server has to select and send a certificate immediately after the ClientHello message. This is a big problem in hosting environments because it means either sharing the same certificate among all customers or using a different IP address for each of them.

There are two known workarounds provided by X.509:

- If all virtual servers belong to the same domain, a wildcard certificate can be used. Besides the loose host name selection that might be a problem or not, there is no common agreement about how to match wildcard certificates. Different rules are applied depending on the application protocol or software used.
- Add every virtual host name in the subjectAltName extension. The major problem being that the certificate needs to be reissued whenever a new virtual server is added.

To provide the server name, Transport Layer Security (TLS) Extensions allow clients to include a Server Name Indication extension (SNI) in the extended ClientHello message. This extension hints to the server immediately which name the client wishes to connect to, so the server can select the appropriate certificate to send to the clients.

There is also a method to implement name-based virtual hosting by upgrading HTTP to TLS via an HTTP/1.1 Upgrade header. Normally this is to securely implement HTTP over TLS within the main "http" URI scheme instead of the commonly used "https" scheme. This would avoid forking the URI space and reduces the number of used ports, however, few implementations currently support this.
