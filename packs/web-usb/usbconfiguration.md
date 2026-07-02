---
title: "USBConfiguration - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/USBConfiguration
domain: web-usb
license: CC-BY-SA-4.0
tags: web usb api, usb device access, usb interface endpoint, usb transfer control
fetched: 2026-07-02
---

# USBConfiguration

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- Learn more
- See full compatibility

**Experimental:** **This is an experimental technology** Check the Browser compatibility table carefully before using this in production.

**Secure context:** This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

**Note:** This feature is available in Web Workers.

The `USBConfiguration` interface of the WebUSB API provides information about a particular configuration of a USB device and the interfaces that it supports.

## Constructor

**`USBConfiguration()`**

Creates a new `USBConfiguration` object which contains information about the configuration on the provided `USBDevice` with the given configuration value.

## Instance properties

**`USBConfiguration.configurationValue` Read only**

Returns the configuration value of this configuration. This is equal to the `bConfigurationValue` field of the configuration descriptor provided by the device defining this configuration.

**`USBConfiguration.configurationName` Read only**

Returns the name provided by the device to describe this configuration. This is equal to the value of the string descriptor with the index provided in the `iConfiguration` field of the configuration descriptor defining this configuration.

**`USBConfiguration.interfaces` Read only**

Returns an array containing instances of the `USBInterface` describing each interface supported by this configuration.

## Specifications

| Specification |
|---|
| WebUSB API # usbconfiguration-interface |

## Browser compatibility
