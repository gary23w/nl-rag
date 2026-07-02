---
title: "Short Message service center"
source: https://en.wikipedia.org/wiki/Short_message_service_center
domain: sms-gateways
license: CC-BY-SA-4.0
tags: sms gateway, short message service, smsc center, ss7 signalling
fetched: 2026-07-02
---

# Short Message service center

(Redirected from

Short message service center

)

A **Short Message Service Center** (**SMSC**) is a network element in the mobile telephone network. Its purpose is to store, forward, convert and deliver Short Message Service (SMS) messages.

The full designation of an SMSC according to 3GPP is *Short Message Service - Service Center (SMS-SC).*8522076203

## Basic trajectories

SMS can be directed in several ways:

1. From mobile to another mobile - referred to as MO-MT (Mobile Originated - Mobile Terminated)
2. From mobile to a content provider (also known as Large Account / ESME) - referred to as MO-AT (Mobile Originated - Application Terminated)
3. From application to a mobile - referred to as AO-MT (Application Originated - Mobile Terminated)

## Operation

The tasks of an SMSC can be described as

1. Reception of text messages (SMS) from wireless network users
2. Storage of text messages
3. Forwarding of text messages
4. Delivery of text messages (SMS) to wireless network users
5. Maintenance of unique time stamps in text messages

When a user *sends* a text message (SMS message) to another user, the message gets stored in the SMSC (Short Message Service Center), which delivers it to the destination user when they are available. This is a store and forward option.

An SMS center (SMSC) is responsible for handling the SMS operations of a wireless network.

1. When an SMS message is sent from a mobile phone, it will first reach an SMS center.
2. The SMS center then forwards the SMS message towards the destination.
3. The main duty of an SMSC is to route SMS messages and regulate the process. If the recipient is unavailable (for example, when the mobile phone is switched off), the SMSC will store the SMS CAR message.
4. It will forward the SMS message when the recipient is available and the message's expiry period is not exceeded.

SMSCs can be used to interface with other applications, for example a spreadsheet can interface with the SMSC allowing messages to be sent SMS from an Excel spreadsheet, or to send an SMS from Excel. Inbound messages to a long number or short code can also be passed through the SMSC allowing m2m communications or Telematics.

### Validity period of an SMS message

An SMS message is stored temporarily in the SMS center if the recipient mobile phone is unavailable. It is possible on most mobile handsets to specify an expiry period after which the SMS message will be deleted from the SMS center. Once deleted, the SMS message will no longer be available for dispatch to the recipient mobile phone (even if it comes on line). The validity period should be regarded by the handset user as a request, as the SMSC itself can be configured to ignore or otherwise handle message delivery schedules.

### Message status reports

The SMS sender needs to set a flag in the SMS message to notify the SMS center that they want the status report about the delivery of this SMS message. This is usually done by changing a setting on the mobile handset.
