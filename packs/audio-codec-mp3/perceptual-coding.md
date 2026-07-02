---
title: "Perceptual coding"
source: https://en.wikipedia.org/wiki/Perceptual_coding
domain: audio-codec-mp3
license: CC-BY-SA-4.0
tags: mp3 codec, mpeg audio layer, psychoacoustic model, audio bit rate
fetched: 2026-07-02
---

# Perceptual coding

**Perceptual coding** is a method of *lossy* *data compression* that exploits the limitations of human sensory system in order to reduce data size. It is widely applied in audio, image and video compression standards, where certain details are removed or simplified because they are unlikely to be noticed under regular listening or viewing conditions.

Perceptual coding is based on models of human hearing and vision, such as those studied in psychoacoustics and psychovisual research. By discarding or reducing components of a signal that fall below perceptual thresholds, it achieves significant reductions in bit rate while maintaining a subjectively acceptable quality.

## Applications

Perceptual coding is central to many everyday technologies, including:

- Audio compression: Formats such as MP3, AAC, and Opus apply psychoacoustic models to remove inaudible frequencies or sounds masked by louder ones.
- Image compression: Standards such as JPEG rely on psychovisual principles, such as chroma subsampling (reducing color resolution relative to brightness).
- Video compression: Standards such as MPEG-2, H.264/AVC, and HEVC use similar compression methods as image compression and add other principles, such as temporal masking (reducing detail during rapid motion).

## History

### Early analog applications

The principles of perceptual coding were applied in analog communication systems long before the advent of digital media.

- Telephony: Early telephone networks restricted audio transmission to a narrow band of roughly 300 Hz–3.4 kHz. Although much of the audible spectrum was discarded, this range was sufficient for intelligible speech, exploiting the fact that human listeners rely primarily on mid-range frequencies for communication.
- FM stereo broadcasting: Introduced in the 1960s, FM stereo used a sum-and-difference transmission system. The (L+R) signal carried the main content at full fidelity, while the (L−R) difference was modulated onto a subcarrier. This reduced bandwidth usage by assuming that much of the information in stereo channels is shared, while still providing an adequate sense of spatial separation.
- Color television: Beginning in the 1950s, color TV systems such as NTSC, PAL, and SECAM took advantage of the human eye’s greater sensitivity to brightness than to color. They encoded a high-resolution luminance channel alongside lower-resolution chrominance channels, allowing backward compatibility with black-and-white sets and conserving broadcast bandwidth.
- Fax transmission: Facsimile (fax) machines, particularly with the ITU-T Group 3 standard (1980), employed compression methods such as run-length encoding to reduce data. Standard fax resolutions (e.g., 200 × 100 dpi) were chosen to preserve legibility of text while omitting fine details like paper texture or ink gradients, relying on the psychovisual observation that readers perceive documents as intact even when such subtleties are lost.

These analog systems demonstrated the effectiveness of tailoring transmission to the characteristics of human perception, laying the groundwork for digital perceptual coding methods.

### Digital development

Research in the 1970s and 1980s on psychoacoustics and psychovisual modeling provided the basis for digital perceptual coding. In audio, this led to the late-1980s development of the MPEG audio formats (such as MP3), which achieved major reductions in bit rate by discarding inaudible sound components. At the same time, the MPEG standards applied similar principles to video, using techniques such as chroma subsampling and motion-adaptive coding.

During the 1990s and 2000s, perceptual coding was embedded in widely used formats including AAC, MPEG-2 video, and H.264/AVC, supporting the rise of digital media distribution on CDs, DVDs, and early internet platforms. More recent codecs, such as HEVC, AV1, and Opus, continue to refine perceptual models to balance compression efficiency with quality on modern networks and devices.

## Relation to other fields

Perceptual coding draws directly on psychoacoustics (the study of auditory perception) and psychovisual research (the study of visual perception). These disciplines provide the models that determine which parts of a signal can be safely removed without affecting perceived quality.
