---
title: "Pansharpening"
source: https://en.wikipedia.org/wiki/Pansharpening
domain: remote-sensing-analysis
license: CC-BY-SA-4.0
tags: remote sensing analysis, multispectral imaging, vegetation index, synthetic-aperture radar
fetched: 2026-07-02
---

# Pansharpening

**Pansharpening** is a process of merging high-resolution panchromatic and lower resolution multispectral imagery to create a single high-resolution color image. Google Maps and nearly every map creating company use this technique to increase image quality. Pansharpening produces a high-resolution color image from three, four or more low-resolution multispectral satellite bands plus a corresponding high-resolution panchromatic band:

> Low-res color bands + High-res grayscale band = High-res color image

Such band combinations are commonly bundled in satellite data sets, for example Landsat 7, which includes six 30 m resolution multispectral bands, a 60 m thermal infrared band plus a 15 m resolution panchromatic band. SPOT, GeoEye and Maxar commercial data packages also commonly include both lower-resolution multispectral bands and a single panchromatic band. One of the principal reasons for configuring satellite sensors this way is to keep satellite weight, cost, bandwidth and complexity down. Pan sharpening uses spatial information in the high-resolution grayscale band and color information in the multispectral bands to create a high-resolution color image, essentially increasing the resolution of the color information in the data set to match that of the panchromatic band.

One common class of algorithms for pansharpening is called “component substitution,” which usually involves the following steps:

- Up-sampling: the color bands are up-sampled to the same resolution as the panchromatic band;
- Alignment: the up-sampled color bands and the panchromatic band are aligned to reduce artifacts due to mis-registration (generally, when the data comes from the same sensor, this step is usually not necessary);
- Forward transform: the up-sampled color bands are transformed to an alternate color space (where intensity is orthogonal to the color information);
- Intensity matching: the intensity of the color bands is matched to the pan band intensity in the transformed space;
- Component substitution: the pan band is then directly substituted for the transformed intensity component;
- Reverse transform: the reverse transformation is performed using the substituted intensity component to transform back to the original color space.

Common color-space transformation used for pan sharpening are HSI (hue-saturation-intensity), and YCbCr. The same steps can also be performed using wavelet decomposition or PCA and replacing the first component with the pan band.

Pan-sharpening techniques can result in spectral distortions when pan sharpening satellite images as a result of the nature of the panchromatic band. The Landsat panchromatic band for example is not sensitive to blue light. As a result, the spectral characteristics of the raw pansharpened color image may not exactly match those of the corresponding low-resolution RGB image, resulting in altered color tones. This has resulted in the development of many algorithms that attempt to reduce this spectral distortion and to produce visually pleasing images.
