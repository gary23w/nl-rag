---
title: "GitHub"
source: https://github.com/lovell/sharp
domain: sharp-imaging
license: CC-BY-SA-4.0
tags: sharp imaging, high performance image processing, image resize pipeline, libvips binding
fetched: 2026-07-02
---

# GitHub

lovell

/

sharp

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 1.4k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History2,484 Commits2,484 Commits |   |   |   |
| .github | .github |   |   |
| docs | docs |   |   |
| install | install |   |   |
| lib | lib |   |   |
| npm | npm |   |   |
| scripts | scripts |   |   |
| src | src |   |   |
| test | test |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitignore | .gitignore |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| biome.json | biome.json |   |   |
| package.json | package.json |   |   |
|   |   |   |   |

## Repository files navigation

# sharp

(sharp logo)

The typical use case for this high speed Node-API module is to convert large images in common formats to smaller, web-friendly JPEG, PNG, WebP, GIF and AVIF images of varying dimensions.

It can be used with all JavaScript runtimes that provide support for Node-API v9, including Node.js (>= 20.9.0), Deno and Bun.

Resizing an image is typically 4x-5x faster than using the quickest ImageMagick and GraphicsMagick settings due to its use of libvips.

Colour spaces, embedded ICC profiles and alpha transparency channels are all handled correctly. Lanczos resampling ensures quality is not sacrificed for speed.

As well as image resizing, operations such as rotation, extraction, compositing and gamma correction are available.

Most modern macOS, Windows and Linux systems do not require any additional install or runtime dependencies.

## Documentation

Visit sharp.pixelplumbing.com for complete installation instructions, API documentation, benchmark tests and changelog.

## Examples

```highlight
npm install sharp
```

```highlight
// ESM
import sharp from 'sharp';

// CJS
const sharp = require('sharp');
```

```highlight
await sharp(inputBuffer)
  .resize({ width: 320, height: 240 })
  .toFile('output.webp', (err, info) => { ... });
```

```highlight
const output = await sharp('input.jpg')
  .autoOrient()
  .resize({ width: 200 })
  .jpeg({ mozjpeg: true })
  .toBuffer();
```

```highlight
const semiTransparentRedPng = await sharp({
  create: {
    width: 48,
    height: 48,
    channels: 4,
    background: { r: 255, g: 0, b: 0, alpha: 0.5 }
  }
})
  .png()
  .toBuffer();
```

```highlight
const roundedCorners = Buffer.from(
  '<svg><rect x="0" y="0" width="200" height="200" rx="50" ry="50"/></svg>'
);

const roundedCornerResizer =
  sharp()
    .resize(200, 200)
    .composite([{
      input: roundedCorners,
      blend: 'dest-in'
    }])
    .png();

readableStream
  .pipe(roundedCornerResizer)
  .pipe(writableStream);
```

## Contributing

A guide for contributors covers reporting bugs, requesting features and submitting code changes.

## Licensing

Copyright 2013 Lovell Fuller and others.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
