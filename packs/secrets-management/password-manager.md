---
title: "Password manager"
source: https://en.wikipedia.org/wiki/Password_manager
domain: secrets-management
license: CC-BY-SA-4.0
tags: secrets management, key management, hardware security module, secret sharing, password manager
fetched: 2026-07-02
---

# Password manager

A **password manager** is a software program that prevents password fatigue by automatically generating, autofilling, and storing passwords. They are useful for local applications or web applications such as online shops or social media. Web browsers tend to have a built-in password manager. Password managers typically require a user to create and remember a single master password to unlock the database and access the stored passwords. Password managers can integrate multi-factor authentication and passkey authentication.

## History

The first password manager software designed to securely store passwords was Password Safe created by Bruce Schneier, which was released as a free utility on September 5, 1997. Designed for Microsoft Windows 95, Password Safe used Schneier's Blowfish algorithm to encrypt passwords and other sensitive data. Although Password Safe was released as a free utility, due to export restrictions on cryptography from the United States, only U.S. and Canadian citizens and permanent residents were initially allowed to download it.

Several other browser-based password managers were launched in the late 1990s including RoboForm (1999) developed by Siber Systems and Obongo (1999), a Sequoia Capital backed company, later acquired by America Online in 2001. The password management applications that emerged in the mid-2000s and that grew dramatically in the 2010s—represented by products such as 1Password (2006), LastPass (2008), Dashlane (2009), and Bitwarden (2016)—provide essentially the same core functionality that Obongo and RoboForm commercialized in 1999: a secure, cloud-based vault of login credentials accessible through a browser extension, protected by a single master password.

As of October 2024, the built-in Google Password Manager in Google Chrome has become the most used password manager.

## Types

### Browser-based

These are built directly into web browsers like Chrome, Safari, Firefox, and Edge. They offer convenient access for basic password management on the device where the browser is used. However, some may lack features like secure syncing across devices or

end-to-end encryption

.

### Local

These are standalone applications installed on a user's device. They offer strong security as passwords are stored locally, but access may be limited to that specific device. Popular open-source options include

KeepassXC

,

KeePass

and

Password Safe

.

### Cloud-based

These store passwords in encrypted form on remote servers, allowing access from supported internet-connected devices. They typically offer features like automatic syncing, secure sharing, and strong encryption. Examples include

1Password

,

Bitwarden

, and

Dashlane

.

### Enterprise

Designed for businesses, these cater to managing access credentials within an organization. They integrate with existing directory services and access control systems, often offering advanced features like role-based permissions and privileged access management.

### Hardware

These physical devices, often USB keys, provide an extra layer of security for password management. Some function as

secure tokens

for database access, such as

YubiKey

and OnlyKey. Others also offer offline storage for passwords, such as OnlyKey and Nitrokey.

## Vulnerabilities

### Weak vault storage

Some applications store passwords as an unencrypted file, leaving the passwords easily accessible to malware or people attempting to steal personal information.

### Master password as single point failure

Some password managers require a user-selected master password to derive the key used to encrypt passwords stored for the application to read. The security of this approach depends on the strength of the chosen master password (which may be brute-forced by an attacker), and also that the master password itself is never stored locally where a malicious program or individual could read it. A compromised master password may render all of the encrypted passwords vulnerable, meaning that a single point of entry can compromise the confidentiality of sensitive information. This is known as a single point of failure.

### Device security dependency

While password managers offer robust security for credentials, their effectiveness hinges on the user's device security. If a device is compromised by malware like Raccoon, which excels at stealing data, the password manager's protections can be nullified. Malware like keyloggers can steal the master password used to access the password manager, granting full access to all stored credentials. Clipboard sniffers can capture sensitive information copied from the manager, and some malware might even steal the encrypted password vault file itself. In essence, a compromised device with password-stealing malware can bypass the security measures of the password manager, leaving the stored credentials vulnerable.

As with password authentication techniques, key logging or acoustic cryptanalysis may be used to guess or copy the "master password". Some password managers attempt to use virtual keyboards to reduce this risk - though this is still vulnerable to key loggers that take the keystrokes and send what key was pressed to the person/people trying to access confidential information.

### Cloud-based storage

Cloud-based password managers offer a centralized location for storing login credentials. However, this approach raises security concerns. One potential vulnerability is a data breach at the password manager itself. If such an event were to occur, attackers could potentially gain access to a large number of user credentials. A 2022 security incident involving LastPass exemplifies this risk.

### Password generator security

Some password managers may include a password generator. Generated passwords may be guessable if the password manager uses a weak method of randomly generating a "seed" for all passwords generated by this program. There are documented cases, like the one with Kaspersky Password Manager in 2021, where a flaw in the password generation method resulted in predictable passwords.

### Others

A 2014 paper by researchers at Carnegie Mellon University found that while browsers refuse to autofill passwords if the login page protocol differs from when the password was saved (HTTP vs. HTTPS), some password managers insecurely filled passwords for the unencrypted (HTTP) version of saved passwords for encrypted (HTTPS) sites. Additionally, most managers lacked protection against iframe and redirection-based attacks, potentially exposing additional passwords when password synchronization was used across multiple devices.

A 2026 paper by researchers at ETH Zurich analyzed four popular commercial password managers and found 27 attacks in 4 attack categories. Some vulnerabilities were present because vulnerable cryptographic algorithms were still present due to backward compatibility. Others were possible because items were individually encrypted which allows field swapping, metadata leakage and downgrade attacks. Some attacks were possible because of unauthenticated public keys allowing a malicious server to replace keys. While most vulnerabilities have been fixed, vendors responded that public key authentication is out of scope.

## Blockage

Various high-profile websites and client-security products have attempted to block or discourage the use of password managers. Techniques have included disabling password autofill, preventing users from pasting into password fields, or setting `autocomplete="off"` on login forms. In 2015, British Gas blocked password managers before reversing the change following public criticism. Other reported examples included T-Mobile, Barclaycard, and Western Union restricting password pasting, often citing concerns such as malware, phishing, or automated attacks. The Trusteer client security software from IBM has included explicit options to block password managers.

Such blocking has been criticized by information security professionals as making users less secure, because it can discourage the use of strong, unique, machine-generated passwords. Research presented at the 2014 USENIX Security Symposium also described websites using form attributes and scripts to interfere with password managers. Modern browser behavior and security guidance have moved toward accommodating password managers. MDN Web Docs notes that many modern browsers do not support `autocomplete="off"` for login fields and may still offer to save and autofill credentials. *NIST Special Publication 800-63B* states that verifiers shall allow password managers and autofill functionality and should permit pasting passwords when autofill APIs are unavailable. The OWASP Authentication Cheat Sheet similarly recommends that web applications allow users to paste into username, password, and multi-factor authentication fields.
