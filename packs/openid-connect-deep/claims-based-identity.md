---
title: "Claims-based identity"
source: https://en.wikipedia.org/wiki/Claims-based_identity
domain: openid-connect-deep
license: CC-BY-SA-4.0
tags: openid connect, id token claims, userinfo endpoint, oidc authentication flow, claims based identity
fetched: 2026-07-02
---

# Claims-based identity

**Claims-based identity** is a common way for applications to acquire the identity information they need about users inside their organization, in other organizations, and on the Internet. It also provides a consistent approach for applications running on-premises or in the cloud. Claims-based identity abstracts the individual elements of identity and access control into two parts: a notion of claims, and the concept of an issuer or an authority.

## Identity and claims

A claim is a statement that one subject, such as a person or organization, makes about itself or another subject. For example, the statement can be about a name, group, buying preference, ethnicity, privilege, association or capability. The subject making the claim or claims is the provider. Claims are packaged into one or more tokens that are then issued by an issuer (provider), commonly known as a security token service (STS).

The name "claims-based identity" can be confusing at first because it seems like a misnomer, attaching the concept of claims to the concept of identity appears to be combining authentication (determination of identity) with authorization (what the identified subject may and may not do). However a closer examination reveals that this is not the case. Claims are not what the subject can and cannot do. They are what the subject is or is not. It is up to the application receiving the incoming claim to map the is/is not claims to the may/may not rules of the application. In traditional systems there is often confusion about the differences and similarities between what a user is/is not and what the user may/may not do. Claims-based identity makes that distinction clear.

## Security token service

Once the distinction between what the user is/is not and what the user may/may not do is clarified, it is possible that the authentication of what the user is/is not (the claims) can be handled by a third party. This third party is called the security token service. To better understand the concept of security token service, consider the analogy of a night club with a doorman. The doorman wants to prevent under-age patrons from entry. To facilitate this he requests a patron to present a driver's license, health insurance card or other identification (the token) that has been issued by a trusted third party (the security token service) such as the provincial or state vehicle license department, health department or insurance company. The nightclub is thus relieved of the responsibility of determining the patron's age. It only has to trust the issuing authority (and of course make its own judgment of the authenticity of the token presented). With these two steps completed the nightclub has successfully authenticated the patron with regard to the claim that he or she is of legal drinking age.

Continuing the analogy, the nightclub may have a membership system, and certain members may be regular or VIP. The doorman might ask for another token, the membership card, which might make another claim; that the member is a VIP. In this case the trusted issuing authority of the token would probably be the club itself. If the membership card makes the claim that the patron is a VIP, then the club can react accordingly, translating the authenticated VIP membership claim to a permission such as the patron being permitted to sit in the exclusive lounge area and be served free drinks. Note that not all uses of the term "authentication" include claims acquisition. The only difference is that authentication is limited to the binding of the user to the information contained about the user in the target site as no attribute data (claim) is required to complete an authentication. As privacy concerns become more important, the ability of digital entities to authenticate users without access to personal attributes becomes increasingly important.

## Benefits

Claims-based identity has the potential to simplify authentication logic for individual software applications, because those applications don't have to provide mechanisms for account creation, password creation, reset, and so on. Furthermore, claims-based identity enables applications to know certain things about the user, without having to interrogate the user to determine those facts. The facts, or claims, are transported in an "envelope" called a secure token.

Claims-based identity can greatly simplify the authentication process because the user doesn't have to sign in multiple times to multiple applications. A single sign in creates the token which is then used to authenticate against multiple applications, or web sites. In addition, because certain facts (claims) are packaged with the token, the user does not have to tell each individual application those facts repeatedly, for instance by answering similar questions or completing similar forms.
