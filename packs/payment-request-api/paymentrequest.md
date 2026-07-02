---
title: "PaymentRequest - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/PaymentRequest
domain: payment-request-api
license: CC-BY-SA-4.0
tags: payment request api, browser checkout flow, payment method data, merchant payment sheet
fetched: 2026-07-02
---

# PaymentRequest

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more support for this feature? Tell us why.

- Learn more
- See full compatibility

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

The Payment Request API's **`PaymentRequest`** interface is the primary access point into the API, and lets web content and apps accept payments from the end user on behalf of the operator of the site or the publisher of the app.

## Constructor

**`PaymentRequest()`**

Creates a new `PaymentRequest` object.

## Instance properties

**`PaymentRequest.id` Read only**

A unique identifier for a particular `PaymentRequest`, which can be set via `details.id`. When none is set, it defaults to a UUID.

**`PaymentRequest.shippingAddress` Read only**

If requested via payment options, returns the shipping address chosen by the user for the purposes of calculating shipping. This property is only populated if the constructor is called with the `requestShipping` flag set to true. Additionally, in some browsers, the parts of the address will be redacted for privacy until the user indicates they are ready to complete the transaction (i.e., they hit "Pay").

**`PaymentRequest.shippingOption` Read only**

Returns the identifier of the selected shipping option. This property is only populated if the constructor is called with the `requestShipping` flag set to true.

**`PaymentRequest.shippingType` Read only**

Returns the type of shipping used to fulfill the transaction. This will be one of `shipping`, `delivery`, `pickup`, or `null` if a value was not provided in the constructor.

## Static methods

**`PaymentRequest.securePaymentConfirmationAvailability()`**

Indicates whether the Secure payment confirmation feature is available.

## Instance methods

**`PaymentRequest.canMakePayment()`**

Indicates whether the `PaymentRequest` object can make a payment before calling `show()`.

**`PaymentRequest.show()`**

Causes the user agent to begin the user interaction for the payment request.

**`PaymentRequest.abort()`**

Causes the user agent to end the payment request and to remove any user interface that might be shown.

## Events

**`merchantvalidation`**

With some payment handlers (e.g., Apple Pay), this event handler is called to handle the `merchantvalidation` event, which is dispatched when the user agent requires that the merchant validate that the merchant or vendor requesting payment is legitimate.

**`paymentmethodchange`**

With some payment handlers (e.g., Apple Pay), dispatched whenever the user changes payment instrument, like switching from a credit card to a debit card.

**`shippingaddresschange`**

Dispatched whenever the user changes their shipping address.

**`shippingoptionchange`**

Dispatched whenever the user changes a shipping option.

## Specifications

| Specification |
|---|
| Payment Request API # paymentrequest-interface |

## Browser compatibility
