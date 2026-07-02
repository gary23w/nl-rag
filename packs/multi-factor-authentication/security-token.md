---
title: "Security token"
source: https://en.wikipedia.org/wiki/Security_token
domain: multi-factor-authentication
license: CC-BY-SA-4.0
tags: multi factor authentication, time based one time password, hmac based one time password, hardware security token, smart card authentication
fetched: 2026-07-02
---

# Security token

A **security token** is a peripheral device used to gain access to an electronically restricted resource. The token is used in addition to, or in place of, a password. Examples of security tokens include wireless key cards used to open locked doors, a banking token used as a digital authenticator for signing in to online banking, or signing transactions such as wire transfers.

Security tokens can be used to store information such as passwords, cryptographic keys used to generate digital signatures, or biometric data (such as fingerprints). Some designs incorporate tamper resistant packaging, while others may include small keypads to allow entry of a PIN or a simple button to start a generation routine with some display capability to show a generated key number. Connected tokens utilize a variety of interfaces including USB, near-field communication (NFC), radio-frequency identification (RFID), or Bluetooth. Some tokens have audio capabilities designed for those who are vision-impaired.

## Password types

All tokens contain some secret information used to prove identity. There are four different ways in which this information can be used:

**Static password token**

The device contains a password that is physically hidden (not visible to the possessor), but is transmitted for each authentication. This type is vulnerable to

replay attacks

.

**Synchronous dynamic password token**

A timer is used to rotate through various combinations produced by a

cryptographic algorithm

. The token and the authentication server must have synchronized clocks.

**Asynchronous password token**

A

one-time password

is generated without the use of a clock, either from a

one-time pad

or cryptographic algorithm.

**Challenge–response token**

Using

public key cryptography

, it is possible to prove possession of a private key without revealing that key. The authentication server encrypts a challenge (typically a random number, or at least data with some random parts) with a public key; the device proves it possesses a copy of the matching private key by providing the decrypted challenge.

Time-synchronized, one-time passwords change constantly at a set time interval; e.g., once per minute. To do this, some sort of synchronization must exist between the client's token and the authentication server. For disconnected tokens, this time-synchronization is done before the token is distributed to the client. Other token types do the synchronization when the token is inserted into an input device. The main problem with time-synchronized tokens is that they can, over time, become unsynchronized. However, some such systems, such as RSA's SecurID, allow the user to re-synchronize the server with the token, sometimes by entering several consecutive passcodes. Most also cannot have replaceable batteries and only last up to 5 years before having to be replaced – so there is an additional cost. Another type of one-time password uses a complex mathematical algorithm, such as a hash chain, to generate a series of one-time passwords from a secret shared key. Each password is unique, even when previous passwords are known. The open-source OATH algorithm is standardized; other algorithms are covered by US patents. Each password is observably unpredictable and independent of previous ones, whereby an adversary would be unable to guess what the next password may be, even with knowledge of all previous passwords.

## Physical types

Tokens can contain chips with functions varying from very simple to very complex, including multiple authentication methods.

The simplest security tokens do not need any connection to a computer. The tokens have a physical display; the authenticating user simply enters the displayed number to log in. Other tokens connect to the computer using wireless techniques, such as Bluetooth. These tokens transfer a key sequence to the local client or to a nearby access point.

Alternatively, another form of token that has been widely available for many years is a mobile device which communicates using an out-of-band channel (like voice, SMS, or USSD).

Still other tokens plug into the computer and may require a PIN. Depending on the type of the token, the computer OS will then either read the key from the token and perform a cryptographic operation on it, or ask the token's firmware to perform this operation.

A related application is the hardware dongle required by some computer programs to prove ownership of the software. The dongle is placed in an input device and the software accesses the I/O device in question to authorize the use of the software in question.

Commercial solutions are provided by a variety of vendors, each with their own proprietary (and often patented) implementation of variously used security features. Token designs meeting certain security standards are certified in the United States as compliant with FIPS 140, a federal security standard. Tokens without any kind of certification are sometimes viewed as suspect, as they often do not meet accepted government or industry security standards, have not been put through rigorous testing, and likely cannot provide the same level of cryptographic security as token solutions which have had their designs independently audited by third-party agencies.

### Disconnected tokens

Disconnected tokens have neither a physical nor logical connection to the client computer. They typically do not require a special input device, and instead use a built-in screen to display the generated authentication data, which the user enters manually themselves via a keyboard or keypad. Disconnected tokens are the most common type of security token used (usually in combination with a password) in two-factor authentication for online identification.

### Connected tokens

Connected tokens are tokens that must be physically connected to the computer with which the user is authenticating. Tokens in this category automatically transmit the authentication information to the client computer once a physical connection is made, eliminating the need for the user to manually enter the authentication information. However, in order to use a connected token, the appropriate input device must be installed. The most common types of physical tokens are smart cards and USB tokens (also called *security keys*), which require a smart card reader and a USB port respectively. Increasingly, FIDO2 tokens, supported by the open specification group FIDO Alliance have become popular for consumers with mainstream browser support beginning in 2015 and supported by popular websites and social media sites.

Older PC card tokens are made to work primarily with laptops. Type II PC Cards are preferred as a token as they are half as thick as Type III.

The audio jack port is a relatively practical method to establish connection between mobile devices, such as iPhone, iPad and Android, and other accessories. The most well known device is called Square, a credit card reader for iOS and Android devices.

Some use a special purpose interface (e.g. the crypto ignition key deployed by the United States National Security Agency). Tokens can also be used as a photo ID card. Cell phones and PDAs can also serve as security tokens with proper programming.

#### Smart cards

Many connected tokens use smart card technology. Smart cards can be very cheap (around ten cents) and contain proven security mechanisms (as used by financial institutions, like cash cards). However, computational performance of smart cards is often rather limited because of extreme low power consumption and ultra-thin form-factor requirements.

Smart-card-based USB tokens which contain a smart card chip inside provide the functionality of both USB tokens and smart cards. They enable a broad range of security solutions and provide the abilities and security of a traditional smart card without requiring a unique input device. From the computer operating system's point of view such a token is a USB-connected smart card reader with one non-removable smart card present.

### Contactless tokens

Unlike connected tokens, contactless tokens form a logical connection to the client computer but do not require a physical connection. The absence of the need for physical contact makes them more convenient than both connected and disconnected tokens. As a result, contactless tokens are a popular choice for keyless entry systems and electronic payment solutions such as Mobil Speedpass, which uses RFID to transmit authentication info from a keychain token. However, there have been various security concerns raised about RFID tokens after researchers at Johns Hopkins University and RSA Laboratories discovered that RFID tags could be easily cracked and cloned.

Another downside is that contactless tokens have relatively short battery lives; usually only 5–6 years, which is low compared to USB tokens which may last more than 10 years. Some tokens however do allow the batteries to be changed, thus reducing costs.

#### Bluetooth tokens

The Bluetooth Low Energy protocols provide long lasting battery lifecycle of wireless transmission.

- The transmission of inherent Bluetooth identity data is the lowest quality for supporting authentication.
- A bidirectional connection for transactional data interchange serves for the most sophisticated authentication procedures.

Although, the automatic transmission power control attempts for radial distance estimates. The escape is available apart from the standardised Bluetooth power control algorithm to provide a calibration on minimally required transmission power.

Bluetooth tokens are often combined with a USB token, thus working in both a connected and a disconnected state. Bluetooth authentication works when closer than 32 feet (9.8 meters). When the Bluetooth link is not properly operable, the token may be inserted into a USB input device to function.

Another combination is with a smart card to store locally larger amounts of identity data and process information as well. Another is a contactless BLE token that combines secure storage and tokenized release of fingerprint credentials.

In the USB mode of operation sign-off requires care for the token while mechanically coupled to the USB plug. The advantage with the Bluetooth mode of operation is the option of combining sign-off with distance metrics. Respective products are in preparation, following the concepts of electronic leash.

#### NFC tokens

Near-field communication (NFC) tokens combined with a Bluetooth token may operate in several modes, thus working in both a connected and a disconnected state. NFC authentication works when closer than 1 foot (0.3 meters). The NFC protocol bridges short distances to the reader while the Bluetooth connection serves for data provision with the token to enable authentication. Also when the Bluetooth link is not connected, the token may serve the locally stored authentication information in coarse positioning to the NFC reader and relieves from exact positioning to a connector.

### Single sign-on software tokens

Some types of single sign-on (SSO) solutions, like enterprise single sign-on, use the token to store software that allows for seamless authentication and password filling. As the passwords are stored on the token, users need not remember their passwords and therefore can select more secure passwords, or have more secure passwords assigned. Usually most tokens store a cryptographic hash of the password so that if the token is compromised, the password is still protected.

### Programmable tokens

Programmable tokens are marketed as "drop-in" replacement of mobile applications such as Google Authenticator (miniOTP). They can be used as mobile app replacement, as well as in parallel as a backup.

## Vulnerabilities

### Loss and theft

The simplest vulnerability with any password container is theft or loss of the device. The chances of this happening, or happening unaware, can be reduced with physical security measures such as locks, electronic leash, or body sensor and alarm. Stolen tokens can be made useless by using two factor authentication. Commonly, in order to authenticate, a personal identification number (PIN) must be entered along with the information provided by the token the same time as the output of the token.

### Attacking

Any system which allows users to authenticate via an untrusted network (such as the Internet) is vulnerable to man-in-the-middle attacks. In this type of attack, an attacker acts as the "go-between" of the user and the legitimate system, soliciting the token output from the legitimate user and then supplying it to the authentication system themselves. Since the token value is mathematically correct, the authentication succeeds and the fraudster is granted access. In 2006, Citibank was the victim of an attack when its hardware-token-equipped business users became the victims of a large Ukrainian-based man-in-the-middle phishing operation.

### Breach of codes

In 2012, the Prosecco research team at INRIA Paris-Rocquencourt developed an efficient method of extracting the secret key from several PKCS #11 cryptographic devices. These findings were documented in INRIA Technical Report RR-7944, ID hal-00691958, and published at CRYPTO 2012.

## Digital signature

Trusted as a regular hand-written signature, the digital signature must be made with a private key known only to the person authorized to make the signature. Tokens that allow secure on-board generation and storage of private keys enable secure digital signatures, and can also be used for user authentication, as the private key also serves as a proof of the user's identity.

For tokens to identify the user, all tokens must have some kind of number that is unique. Not all approaches fully qualify as digital signatures according to some national laws. Tokens with no on-board keyboard or another user interface cannot be used in some signing scenarios, such as confirming a bank transaction based on the bank account number that the funds are to be transferred to.
