---
title: "Resource Interchange File Format"
source: https://en.wikipedia.org/wiki/Resource_Interchange_File_Format
domain: waveform-audio
license: CC-BY-SA-4.0
tags: wav audio, pulse-code modulation, audio sampling, riff container
fetched: 2026-07-02
---

# Resource Interchange File Format

**Resource Interchange File Format** (**RIFF**) is a generic file container format for storing data in tagged chunks. It is primarily used for audio and video, though it can be used for arbitrary data.

The Microsoft implementation is mostly known through the container formats AVI, ANI and WAV, which use RIFF as their basis.

## History

RIFF was introduced in 1991 by Microsoft and IBM and used as the default format for Windows 3.1 multimedia files. It is based on Interchange File Format introduced by Electronic Arts in 1985 on the Amiga. IFF uses the big-endian convention of the Amiga's Motorola 68000 CPU, but in RIFF multi-byte integers are stored in the little-endian order of the x86 processors used in IBM PC compatibles. A RIFX format, which is big-endian, was also introduced.

In 2010 Google introduced the WebP picture format, which uses RIFF as a container.

## Explanation

RIFF files consist entirely of "chunks". The overall format is identical to IFF, except for the endianness as previously stated, and the different meaning of the chunk names.

All chunks have the following format:

- 4 bytes: an ASCII identifier for this chunk (examples are "fmt " and "data"; note the space in "fmt ").
- 4 bytes: an unsigned, little-endian 32-bit integer with the length of this chunk (except this field itself and the chunk identifier).
- variable-sized field: the chunk data itself, of the size given in the previous field.
- a pad byte, if the chunk's length is not even.

Two chunk identifiers, "RIFF" and "LIST", introduce a chunk that can contain subchunks. The RIFF and LIST chunk data (appearing after the identifier and length) have the following format:

- 4 bytes: an ASCII identifier for this particular RIFF or LIST chunk (for RIFF in the typical case, these 4 bytes describe the content of the entire file, such as "AVI " or "WAVE").
- rest of data: subchunks.

The file itself consists of one RIFF chunk, which then can contain further subchunks: hence, the first four bytes of a correctly formatted RIFF file will spell out "RIFF".

More information about the RIFF format can be found in the Interchange File Format article.

RF64 is a multichannel file format based on RIFF specification, developed by the European Broadcasting Union. It is BWF-compatible and allows file sizes to exceed 4 gigabytes. It does so by providing a "ds64" chunk with a 64-bit (8-byte) size.

## Use of the INFO chunk

The optional INFO chunk allows RIFF files to be "tagged" with information falling into a number of predefined categories, such as copyright ("ICOP"), comments ("ICMT"), artist ("IART"), in a standardised way. These details can be read from a RIFF file even if the rest of the file format is unrecognized. The standard also allows the use of user-defined fields. Programmers intending to use non-standard fields should bear in mind that the same non-standard subchunk ID may be used by different applications in different (and potentially incompatible) ways.

## Compatibility issues

### Initial difficulties with MIDI files

In line with their policy of using .RIFF for all Windows 3.1 "multimedia" files, Microsoft introduced a new variant on the existing MIDI file format used for storing song information to be played on electronic musical instruments. Microsoft's MIDI file format consisted of a standard MIDI file enclosed in a RIFF wrapper, and had the file extension .RMI. Since the existing MIDI file format already supported embedded "tagging" information, this caused the disadvantage of having to deal with two file formats for the same type of information.

The MIDI Manufacturers Association have since embraced the RIFF-based MIDI file format, and used it as the basis of an "extended midifile" that also includes instrument data in "DLS" format, embedded within the same .RMI file.

### INFO chunk placement problems

For cataloguing purposes, the optimal position for the INFO chunk is near the beginning of the file. However, since the INFO chunk is optional, it is often omitted from the detailed specifications of individual file formats, leading to some confusion over the correct position for this chunk within a file.

When dealing with large media files, the expansion or contraction of the INFO chunk during tag-editing can result in the following "data" section of the file having to be read and rewritten back to disk to accommodate the new header size. Since media files can be gigabytes in size, this is a potentially disk-intensive process. One workaround is to "pad out" the leading INFO chunk using dummy data (using a "dummy chunk" or "pad chunk") when the file is created. Later editing can then expand or contract the "dummy" field to keep the total size of the file header constant: an intelligently written piece of software can then overwrite just the file header when tagging data is changed, without modifying or moving the main body of the file.

Some programs have tried to address the problem by placing the INFO chunk at the end of a media file, after the main body of the file. This has resulted in two different conventions for chunk placement, with the attendant risk that some combinations of software can cause a file's INFO data to be ignored or permanently overwritten during editing. More sophisticated programs will take into account the possibility of "unexpected" chunk placement in files and respond accordingly. For instance, when the audio-editing program Audacity encounters a .WAV file with end-placed INFO data, it will correctly identify and read the data, but on saving, will relocate the INFO chunk back to the file header.

Although CorelDRAW 10 nominally uses a RIFF file structure, the program's initial release placed the INFO chunk at the end, so that any embedded preview bitmap would not be displayed under Windows' file manager by default. A "patch" utility supplied with the program fixes this problem.

## RIFF info tags

RIFF information tags are found in WAV audio and AVI video files.

| Tag ID | Tag name | Writable | Values / notes |
|---|---|---|---|
| DTIM | DateTimeOriginal | N | ICC Profile "dtim" format values |
| TAPE | TapeName | N |   |

### Converting DTIM time to normal time

The field consists of two values (v[0] and v[1]) separated with a space (0x20). Sample code:

```mw
// time in seconds - "concatenate" date & time elements with a decimal point delimiter
TimeInSeconds = (v[0] * (2^32) + v[1]) * 10^(-7);

// shift basis from Jan 1, 1601 to Unix epoch Jan 1, 1970 (369 years & leap days)
UnixTimeStamp = TimeInSeconds - 134774 * 24 * 3600;
```

## Some common RIFF file types

- WAV (Windows audio)
- AVI (Windows audiovisual)
- RMI (Windows "RIFF MIDIfile")
- CDR (CorelDRAW vector graphics file)
- ANI (Animated Windows cursors)
- PAL (Palette)
- DLS (Downloadable Sounds)
- WebP (An image format developed by Google)
- XMA (Microsoft Xbox 360 console audio format based on WMA Pro)
- SF(1/2/3) (SoundFont versions 1, 2, and 3 made to store instrument samples)
