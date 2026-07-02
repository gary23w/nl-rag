---
title: "Card security code"
source: https://en.wikipedia.org/wiki/Card_security_code
domain: payment-card-processing
license: CC-BY-SA-4.0
tags: payment card processing, pci dss, emv chip, card tokenization
fetched: 2026-07-02
---

# Card security code

A **card security code** (**CSC**; also known as **CVC**, **CVV**, or several other names) is a series of numbers that, in addition to the bank card number, is printed (but not embossed) on a credit or debit card. The CSC is used as a security feature for card-not-present transactions, where a personal identification number (PIN) cannot be manually entered by the cardholder (as they would during point-of-sale or card present transactions). It was instituted to reduce the incidence of credit card fraud. Unlike the card number, the CSC is deliberately not embossed, so that it is not read when using a mechanical credit card imprinter which will only pick up embossed numbers.

These codes are in slightly different places for different card issuers. The CSC for Visa, Mastercard, and Discover credit cards is a three-digit number on the back of the card, to the right of the signature box. The CSC for American Express is a four-digit code on the front of the card above the account number. See the figures to the right for examples.

CSC was originally developed in the UK as an eleven-character alphanumeric code by Equifax employee Michael Stone in 1995. After testing with the Littlewoods Home Shopping group and NatWest bank, the concept was adopted by the UK Association for Payment Clearing Services (APACS) and streamlined to the three-digit code known today. Mastercard started issuing CVC2 numbers in 1997 and Visa in the United States issued them by 2001. American Express started to use the CSC in 1999, in response to growing Internet transactions and card member complaints of spending interruptions when the security of a card has been brought into question.

Contactless card and chip cards may electronically generate their own code, such as iCVV or a *dynamic* CVV.366

## Naming

The codes have different names:

- "CSC" or "card security code": debit cards, American Express (three digits on back of card, also referred to as 3CSC)
- "CVC" or "card validation code": Mastercard
- "CVV" or "card verification value": Visa
- "CAV" or "card authentication value": JCB
- "CID": "card ID", "card identification number", or "card identification code": Discover, American Express (four digits on front of card). American Express usually uses the four-digit code on the front of the card, referred to as the card identification code (CID), but also has a three-digit code on the back of the card, referred to as the card security code (CSC). American Express also sometimes refers to a "unique card code".
- "CVD" or "card verification data": Discover
- "CVE" or "Elo verification code": Elo in Brazil
- "CVN" or "card validation number", also "card verification number": China UnionPay, Google Ads
- "SPC" or "signature panel code"
- "CCV" or "card code verification": commonly used in Canada

## Types

There are several types of security codes and PVV (all generated from DES key in the bank in HSM modules using PAN, expiration date and service code):

- The first code, 3 numbers, called CVC1 or CVV1, is encoded on track one and two of the magnetic stripe of the card and used for card present transactions, with signature (second track also contains pin verification value, PVV, but now it is usually all zeroed out and service code). The purpose of the code is to verify that a payment card is actually in the hand of the merchant (thus it should be different from CVV2). This code is automatically retrieved when the magnetic stripe of a card is read (swiped) on a point-of-sale (card present) device and is verified by the issuer. A limitation is that if the entire card has been duplicated and the magnetic stripe copied, then the code is still valid, notwithstanding the fact that cardholder signature will still usually be required .
- The second code, and the most cited, is CVV2 or CVC2. This code is often used by merchants for card-not-present transactions including online purchases. In some countries in Western Europe, card issuers require a merchant to obtain the code when the cardholder is not present in person. Uses service code 000.
- Contactless and/or chip EMV cards supply their own electronically generated codes, called iCVV. Uses service code 999. It is described in public standards from EMVCo.
- Consumer Device Cardholder Verification Method (CDCVM for short) is a type of identity verification in which the user's mobile device (such as a smartphone) is used to verify the user's identity; for example, it can use the device's biometrics authentication features (e.g. Touch ID or Face ID), or the device's set passcode. It is supported by a number of payment systems, such as Apple Pay, Google Pay or Samsung Pay.

## Location

The card security code is typically the last three or four digits printed, not embossed like the card number, on the signature strip on the back of the card. On American Express cards, however, the card security code is the four digits printed (not embossed) on the front towards the right. The card security code is not encoded on the magnetic stripe but is printed flat.

- American Express cards have a four-digit code printed on the front side of the card above the number.
- Diners Club, Discover, JCB, Mastercard, and Visa credit and debit cards have a three-digit card security code. The code is the final group of numbers printed on the back signature panel of the card.
- New North American Mastercard and Visa cards feature the code in a separate panel to the right of the signature strip. This has been done to prevent overwriting of the numbers by signing the card.

## Generation

The CSC for each card (form 1 and 2) is generated by the card issuer when the card is issued. It is calculated by encrypting the bank card number and expiration date (two fields printed on the card) with encryption keys known only to the card issuer, and decimalising the result (in a similar manner to a hash function).

## Benefits and limitations

As a security measure, merchants who require the CVV2 for card-not-present transactions are required by the card issuer not to store the CVV2 once the individual transaction is authorized. This way, if a database of transactions is compromised, the CVV2 is not present and the stolen card numbers are less useful. Virtual terminals and payment gateways do not store the CVV2 code; therefore, employees and customer service representatives with access to these web-based payment interfaces, who otherwise have access to complete card numbers, expiration dates, and other information, still lack the CVV2 code.

The Payment Card Industry Data Security Standard (PCI DSS) also prohibits the storage of CSC (and other sensitive authorisation data) post transaction authorisation. This applies globally to anyone who stores, processes or transmits cardholder data. Since the CSC is not contained on the magnetic stripe of the card, it is not typically included in the transaction when the card is used face to face at a merchant. However, some merchants in North America, such as Sears and Staples, require the code. For American Express cards, this has been an invariable practice (for card-not-present transactions) in European Union (EU) countries like Ireland and the United Kingdom since the start of 2005. This provides a level of protection to the bank/cardholder, in that a fraudulent merchant or employee cannot simply capture the magnetic stripe details of a card and use them later for card-not-present transactions over the phone, mail order or Internet. To do this, a merchant or its employee would also have to note the CVV2 visually and record it, which is more likely to arouse the cardholder's suspicion.

Supplying the CSC code in a transaction is intended to verify that the customer has the card in their possession. Knowledge of the code proves that the customer has seen the card, or has seen a record made by somebody who saw the card.

Limitations include:

- The use of the CSC cannot protect against phishing scams, where the cardholder is tricked into entering the CSC among other card details via a fraudulent website. The growth in phishing has reduced the real-world effectiveness of the CSC as an anti-fraud device. There is now also a scam where a phisher has already obtained the card account number (perhaps by hacking a merchant database or from a poorly designed receipt) and gives this information *to* the victims (lulling them into a false sense of security) before asking for the CSC (which is all that the phisher needs and the purpose of the scam in the first place).
- Since the CSC may not be stored by the merchant for any length of time (after the original transaction in which the CSC was quoted and then authorized), a merchant who needs to regularly bill a card for a regular subscription would not be able to provide the code after the initial transaction. Payment gateways, however, have responded by adding "periodic bill" features as part of the authorization process.
- Some card issuers do not use the CSC. However, transactions without CSC are possibly subjected to higher card processing cost to the merchants, and fraudulent transactions without CSC are more likely to be resolved in favour of the cardholder.
- It is not mandatory for a merchant to require the security code for making a transaction, so the card may still be prone to fraud even if only its number is known to phishers. For example, Amazon requires only a card number and expiration date to complete a transaction.
- It is possible for a fraudster to guess the CSC by using a distributed attack.
