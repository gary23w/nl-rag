---
title: "Pop-up notification"
source: https://en.wikipedia.org/wiki/Pop-up_notification
domain: notifications-api
license: CC-BY-SA-4.0
tags: notifications api, desktop notification permission, notification event handling, system notification banner
fetched: 2026-07-02
---

# Pop-up notification

A **pop-up notification** (or **toast**, **passive pop-up**, **snackbar**, **desktop notification**, **notification bubble**, or simply **notification**) is a graphical control element that communicates certain events to the user without forcing them to react to this notification immediately, unlike conventional pop-up windows. Desktop notifications usually disappear automatically after a short amount of time. Often their content is then stored in some widget that allows the users to access past notifications at a more convenient time.

On mobile devices, a push notification system is typically used.

## Support on different systems

In Windows 2000, Microsoft introduced balloon help-like passive pop-up notifications, tied to the notification area of the taskbar. Notifications get queued when user is away or screensaver is running, and get shown when the user resumes activity. They remain on screen for nine seconds while fading out if the user appears to ignore them. Microsoft also adopted similar notifications for its other software such as Windows Phone using the Microsoft Push Notification Service, Internet Explorer 7 and later, Microsoft Outlook, Microsoft Security Essentials, as well as Windows 8 and Windows 10 using the Windows Notification Service.

Desktop notifications are a proposed standard for freedesktop.org, but all the major desktop environments running on the X Window System already support this standard, making them typically available on Linux and other Unix-like systems. Google adopted the concepts of notification drawer and toast popup messages for user notifications as basic components of its Android operating system.

macOS (since OS X Mountain Lion) provides desktop notifications via Notification Center. Previous versions of OS X have no built-in desktop notification feature; however, Growl is a popular application that provides similar functionality and enjoys broad support from third-party software. iOS also includes Notification Center as of iOS 5.

## JavaScript

Browsers that support JavaScript typically implement the Notification API. This API asks for user confirmation to allow popups and give the programmer the opportunity to display notifications with a text (body) along with a descriptive icon and header.

## Capabilities

While passive pop-ups do not require any user interaction, some implementations still provide a way for the user to optionally interact with the pop-up. This is called *actions*. For the Freedesktop specification, this is an optional feature that clients cannot rely on, and its use is discouraged by some design guidelines.

Android adds the ability to provide actions with Jelly Bean.

## In the Material Design language

Google's Material Design introduced the term *snackbar* to refer to a user-interface element displaying a temporary, closable notification:

*Snackbars inform users of a process that an app has performed or will perform. They appear temporarily, towards the bottom of the screen. They shouldn’t interrupt the user experience, and they don’t require user input to disappear.*
