---
title: "Application permissions"
source: https://en.wikipedia.org/wiki/Application_permissions
domain: android-app-hardening
license: CC-BY-SA-4.0
tags: android application hardening, android keystore system, android permission model, network security config
fetched: 2026-07-02
---

# Application permissions

**Permissions** are a means of controlling and regulating access to specific system- and device-level functions by software. Typically, types of permissions cover functions that may have privacy implications, such as the ability to access a device's hardware features (including the camera and microphone), and personal data (such as storage devices, contacts lists, and the user's present geographical location). Permissions are typically declared in an application's manifest, and certain permissions must be specifically granted at runtime by the user—who may revoke the permission at any time.

Permission systems are common on mobile operating systems, where permissions needed by specific apps must be disclosed via the platform's app store.

## Mobile devices

On mobile operating systems for smartphones and tablets, typical types of permissions regulate:

- Access to storage and personal information, such as contacts, calendar appointments, etc.
- Location tracking.
- Access to the device's internal camera and/or microphone.
- Access to biometric sensors, including fingerprint readers and other health sensors..
- Internet access.
- Access to communications interfaces (including their hardware identifiers and signal strength where applicable, and requests to enable them), such as Bluetooth, Wi-Fi, NFC, and others.
- Making and receiving phone calls.
- Sending and reading text messages
- The ability to perform in-app purchases.
- The ability to "overlay" themselves within other apps.
- Installing, deleting and otherwise managing applications.
- Authentication tokens (e.g., OAuth tokens) from web services stored in system storage for sharing between apps.

Prior to Android 6.0 "Marshmallow", permissions were automatically granted to apps at runtime, and they were presented upon installation in Google Play Store. Since Marshmallow, certain permissions now require the app to request permission at runtime by the user. These permissions may also be revoked at any time via Android's settings menu. Usage of permissions on Android are sometimes abused by app developers to gather personal information and deliver advertising; in particular, apps for using a phone's camera flash as a flashlight (which have grown largely redundant due to the integration of such functionality at the system level on later versions of Android) have been known to require a large array of unnecessary permissions beyond what is actually needed for the stated functionality.

iOS imposes a similar requirement for permissions to be granted at runtime, with particular controls offered for enabling of Bluetooth, Wi-Fi, and location tracking.

## WebPermissions

WebPermissions is a permission system for web browsers. When a web application needs some data behind permission, it must request it first. When it does it, a user sees a window asking him to make a choice. The choice is remembered, but can be cleared lately.

Currently the following resources are controlled:

- geolocation
- desktop notifications
- service workers
- sensors
  - audio capturing devices, like sound cards, and their model names and characteristics
  - video capturing devices, like cameras, and their identifiers and characteristics

## Analysis

The permission-based access control model assigns access privileges for certain data objects to application. This is a derivative of the discretionary access control model. The access permissions are usually granted in the context of a specific user on a specific device. Permissions are granted permanently with few automatic restrictions.

In some cases permissions are implemented in 'all-or-nothing' approach: a user either has to grant all the required permissions to access the application or the user can not access the application. There is still a lack of transparency when the permission is used by a program or application to access the data protected by the permission access control mechanism. Even if a user can revoke a permission, the app can blackmail a user by refusing to operate, for example by just crashing or asking user to grant the permission again in order to access the application.

The permission mechanism has been widely criticized by researchers for several reasons, including;

- Intransparency of personal data extraction and surveillance, including the creation of a false sense of security;
- End-user fatigue of micro-managing access permissions leading to a fatalistic acceptance of surveillance and intransparency;
- Massive data extraction and personal surveillance carried out once the permissions are granted.

Some apps, such as XPrivacy and Mockdroid spoof data in order to act as a measure for privacy. Further transparency methods include longitudinal behavioural profiling and multiple-source privacy analysis of app data access.
