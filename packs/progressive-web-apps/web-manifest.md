---
title: "Web application manifest - Progressive web apps"
source: https://developer.mozilla.org/en-US/docs/Web/Manifest
domain: progressive-web-apps
license: CC-BY-SA-2.5
tags: progressive web app, pwa, web app manifest, installable web app
fetched: 2026-07-02
---

# Web application manifest

A **web application manifest**, defined in the Web Application Manifest specification, is a JSON text file that provides information about a web application.

The most common use for a web application manifest is to provide information that the browser needs to install a progressive web app (PWA) on a device, such as the app's name and icon.

A web application manifest contains a single JSON object where the top-level keys are called *members*.

## Members

This section lists reference pages for manifest members that are documented on MDN. All members are optional in the specification, but some applications require some members to be present. For example, PWAs must provide certain manifest members.

- background_color
- categories
- description
- display
- display_override
- file_handlers
- icons
- id
- launch_handler
- name
- note_taking
- orientation
- prefer_related_applications
- protocol_handlers
- related_applications
- scope
- scope_extensions
- screenshots
- serviceworker
- share_target
- short_name
- shortcuts
- start_url
- theme_color

**Note:** The `dir`, `lang`, and `iarc_rating_id` members are not implemented.

## Example manifest

```json
{
  "short_name": "MDN",
  "name": "MDN Web Docs",
  "icons": [
    {
      "src": "/favicon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/favicon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "black",
  "background_color": "white"
}
```

## Deploying a manifest

Web app manifests are deployed in your HTML pages using a `<link>` element in the `<head>` of a document:

```html
<link rel="manifest" href="manifest.json" />
```

The `.webmanifest` extension is specified in the Media type registration section of the specification (the response of the manifest file should return `Content-Type: application/manifest+json`). Browsers generally support manifests with other appropriate extensions like `.json` (`Content-Type: application/json`).

If the manifest requires credentials to fetch, the `crossorigin` attribute must be set to `use-credentials`, even if the manifest file is in the same origin as the current page.

```html
<link rel="manifest" href="/app.webmanifest" crossorigin="use-credentials" />
```

## Splash screens

In some browsers and operating systems, a splash screen is displayed when an installed PWA is launched. This splash screen is automatically generated and its appearance is defined by members in the web app manifest, specifically:

- `name`
- `background_color`
- `icons`

## Browser compatibility
