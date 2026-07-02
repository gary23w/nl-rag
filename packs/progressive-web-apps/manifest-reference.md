---
title: "Web app manifest members reference - Web app manifest"
source: https://developer.mozilla.org/en-US/docs/Web/Manifest/Reference
domain: progressive-web-apps
license: CC-BY-SA-2.5
tags: progressive web app, pwa, web app manifest, installable web app
fetched: 2026-07-02
---

# Web app manifest members reference

This page lists references for Web app manifest members usage on the web.

**background_color**

The `background_color` manifest member is used to specify an initial background color for your web application. This color appears in the application window before your application's stylesheets have loaded.

**categories**

The `categories` manifest member lets you specify one or more classifications for your web application. These categories help users discover your app in app stores.

**description**

The `description` manifest member is used to explain the core features or functionality of your web application. This text helps users understand your app's purpose when viewing it in an app store.

**display**

The `display` manifest member is used to specify your preferred display mode for the web application. The display mode determines how much of the browser UI is shown to the user when the app is launched within the context of an operating system. You can choose to show the full browser interface or hide it to provide a more app-like experience.

**display_override**

The `display` member is used to determine the developer's preferred display mode for a website. It follows a process where the browser falls back to the next display mode if the requested one is not supported. In some advanced use cases, this fallback process might not be enough.

**file_handlers**

The `file_handlers` member specifies an array of objects representing the types of files an installed progressive web app (PWA) can handle.

**icons**

The `icons` manifest member is used to specify one or more image files that define the icons to represent your web application.

**id**

The `id` manifest member is used to specify a unique identifier for your web application.

**launch_handler**

The `launch_handler` member defines values that control the launch of a web application. Currently it can only contain a single value, `client_mode`, which specifies the context in which the app should be loaded when launched. For example, in an existing web app client containing an instance of the app, or in a new web app client. This leaves scope for more `launch_handler` values to be defined in the future.

**name**

The `name` manifest member is used to specify the full name of your web application as it's usually displayed to users, such as in application lists or as a label for your application's icon.

**note_taking**

The `note_taking` member identifies a web app as a note-taking app and defines related information, for example a URL pointing to functionality for taking a new note. This enables operating systems to integrate the app's note taking functionality, for example including a "New note" option in the app's context menu, or providing the app as an option for taking a note in other apps.

**orientation**

The `orientation` manifest member is used to specify the default orientation for your web application. It defines how the app should be displayed when launched and during use, in relation to the device's screen orientation, particularly on devices that support multiple orientations.

The `prefer_related_applications` manifest member is used to provide a hint to browsers whether to prefer installing native applications specified in the `related_applications` manifest member over your web application.

**protocol_handlers**

The `protocol_handlers` member specifies an array of objects that are protocols which this web app can register and handle. Protocol handlers register the application in an OS's application preferences; the registration associates a specific application with the given protocol scheme. For example, when using the protocol handler `mailto://` on a web page, registered email applications open.

The `related_applications` manifest member is used to specify one or more applications that are related to your web application. These may be platform-specific applications or Progressive Web Apps.

**scope**

The `scope` manifest member is used to specify the top-level URL path that contains your web application's pages and subdirectories. When users install and use your web app, pages *within scope* provide an app-like interface. When users navigate to pages outside the app's scope, they still experience the app-like interface, but browsers display UI elements like the URL bar to indicate the change in context.

**scope_extensions**

The `scope_extensions` manifest member is used to extend the scope of a web app to include other origins. This allows multiple domains to be presented as a single web app.

**screenshots**

The `screenshots` manifest member lets you specify one or more images that showcase your web application. These images help users preview your web app's interface and features in app stores.

**serviceworker**

The `serviceworker` member specifies a serviceworker that is Just-In-Time (JIT)-installed and registered to run a web-based payment app providing a payment mechanism for a specified payment method in a merchant website. See `Web-based Payment Handler API` for more details.

The `share_target` manifest member allows installed Progressive Web Apps (PWAs) to be registered as a share target in the system's share dialog.

**short_name**

The `short_name` manifest member is used to specify a short name for your web application, which may be used when the full `name` is too long for the available space.

**shortcuts**

The `shortcuts` manifest member is used to specify links to key tasks or pages within your web application. Browsers can use this information to create a context menu, which is typically displayed when a user interacts with the web app's icon.

**start_url**

The `start_url` manifest member is used to specify the URL that should be opened when a user launches your web application, such as when tapping the application's icon on their device's home screen or in an application list.

**theme_color**

The `theme_color` member is used to specify the default color for your web application's user interface. This color may be applied to various browser UI elements, such as the toolbar, address bar, and status bar. It can be particularly noticeable in contexts like the task switcher or when the app is added to the home screen.
