---
title: "Passwordless authentication"
source: https://en.wikipedia.org/wiki/Passwordless_authentication
domain: passkeys
license: CC-BY-SA-4.0
tags: passkey authentication, passwordless authentication, webauthn credential, fido alliance, public key credential
fetched: 2026-07-02
---

# Passwordless authentication

**Passwordless authentication** is an authentication method in which a user can log in to a computer system without entering (and having to remember) a password or any other knowledge-based secret. In most common implementations, users are asked to enter their public identifier (username, phone number, email address, etc.) and then complete the authentication process by providing a secure proof of identity through a registered device or token.

Passwordless authentication methods typically rely on public-key cryptography infrastructure, where the public key is provided during registration to the authenticating service (remote server, application, or website). In contrast, the private key is kept on a user’s device (PC, smartphone or an external security token) and can be accessed only by providing a biometric signature or another authentication factor which is not knowledge-based.

These factors classically fall into two categories:

- Ownership factors (“Something the user has”) such as a cellular phone, OTP token, smart card, or a hardware token.
- Inherence factors (“Something the user is”) like fingerprints, retinal scans, face or voice recognition and other biometric identifiers.

Some designs might also accept a combination of other factors such as geo-location, network address, behavioral patterns, and gestures, as long as no memorized passwords are involved.

Passwordless authentication is sometimes confused with multi-factor authentication (MFA), since both use a wide variety of authentication factors. Still, while MFA is often used as an added layer of security on top of password-based authentication, passwordless authentication does not require a memorized secret. Usually, it uses just one highly secure factor to authenticate identity (i.e., an external security token), making it faster and simpler for users.

When both approaches are employed, “Passwordless MFA” is the term used. The authentication flow is passwordless and uses multiple factors, providing the highest security level when implemented correctly.

## History

The notion that passwords should become obsolete has been circling in computer science since at least 2004. Bill Gates, speaking at the 2004 RSA Conference, predicted the demise of passwords, saying "they just don't meet the challenge for anything you really want to secure." Matt Honan, a journalist at *Wired*, who was the victim of a hacking incident, in 2012 wrote "The age of the password has come to an end." Heather Adkins, manager of Information Security at Google, in 2013 said that "passwords are done at Google." Eric Grosse, VP of security engineering at Google, states that "passwords and simple bearer tokens, such as cookies, are no longer sufficient to keep users safe." Christopher Mims, writing in *The Wall Street Journal* said the password "is finally dying" and predicted their replacement by device-based authentication, however, purposefully revealing his Twitter password resulted in being forced to change his cellphone number. Avivah Litan of Gartner said in 2014, "Passwords were dead a few years ago. Now they are more than dead." The reasons given often include reference to the usability as well as security problems of passwords.

Bonneau et al. systematically compared web passwords to 35 competing authentication schemes regarding their usability, deployability, and security. (The technical report is an extended version of the peer-reviewed paper by the same name.) Their analysis shows that most schemes do better than passwords on security, some schemes do better and some worse regarding usability, while *every* scheme does worse than passwords on deployability. The authors conclude with the following observation: “Marginal gains are often not sufficient to reach the activation energy necessary to overcome significant transition costs, which may provide the best explanation of why we are likely to live considerably longer before seeing the funeral procession for passwords arrive at the cemetery.”

Recent technological advancements (e.g., the proliferation of biometric devices and smartphones) and changing business culture (acceptance of biometrics and decentralized workforce, for example) continuously promote the adoption of passwordless authentication. Leading tech companies (Microsoft, Google) and industry wide initiatives are developing better architectures and practices to bring it to wider use, with many taking a cautious approach, keeping passwords behind the scenes in some use cases. The development of open standards such as FIDO2 and WebAuthn has further generated adoption of passwordless technologies such as Windows Hello. On June 24, 2020, Apple Safari announced that Face ID or Touch ID would be available as a WebAuthn platform authenticator for passwordless login.

## Mechanism

A user must first register with a system before their identity can be verified. A passwordless registration flow may include the following steps:

- **Registration request**: When a user attempts to register with a website, the server sends a registration request to the user's device.
- **Authentication factor selection**: When the user's device receives the registration request, it sets up a method for authenticating the user. For example, the device may use biometrics like a fingerprint scanner or facial recognition for user identification.
- **Key generation**: The user's device generates a public/private key pair and sends the public key to the server for future verification.

Once they have registered, a user can log in to the system via the following process:

- **Authentication challenge**: The server sends an authentication challenge to the user's device when the user attempts to log into the site.
- **User authentication**: The user proves their identity to their device using the biometric scanner, unlocking their private key.
- **Challenge response**: The user's device digitally signs a response to the authentication challenge with the user's private key.
- **Response validation**: The server uses the user's public key to verify the digital signature and provides access to the user's account.

## Benefits and drawbacks

Proponents point out several unique benefits over other authentication methods:

- **Greater security** – passwords are known to be a weak point in computer systems (due to reuse, sharing, cracking, spraying etc.) and are regarded a top attack vector responsible for a huge percentage of security breaches.
- **Better user experience** – Not only users aren’t required to remember complicated password and comply with different security policies, they are also not required to periodically renew passwords.
- **Reduced IT costs** – since no password storage and management is needed IT teams are no longer burdened by setting password policies, detecting leaks, resetting forgotten passwords, and complying with password storage regulation.
- **Better visibility of credential use** – since credentials are tied to a specific device or inherent user attribute, they can't be massively used and access management becomes more tight.
- **Scalability** – managing multiple logins without additional password fatigue or complicated registration.

While others point out operational and cost-related disadvantages:

- **Implementation costs** – Although it is accepted that passwordless authentication leads to savings in the long term, deployment costs are currently a hindering factor for many potential users. Cost is associated with the need to deploy an authentication mechanism on an existing user directory and sometimes the additional hardware deployed to users (e.g. OTPs or security keys).
- **Training and expertise needed** – while most password management systems are built similarly and have been used for many years, passwordless authentication requires adaptation from both IT teams and end users.
- **Single point of failure** – particularly implementations using OTP or push notifications to cellular device applications can create a challenge for the end user if a device is broken, lost, stolen or simply upgraded.
