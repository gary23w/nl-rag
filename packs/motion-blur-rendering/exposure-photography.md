---
title: "Exposure (photography)"
source: https://en.wikipedia.org/wiki/Exposure_(photography)
domain: motion-blur-rendering
license: CC-BY-SA-4.0
tags: motion blur rendering, per-object motion blur, shutter speed blur, velocity buffer blur
fetched: 2026-07-02
---

# Exposure (photography)

Photographic image taken using a variety of exposures

In photography, **exposure** is the amount of light per unit area reaching a frame of photographic film or the surface of an electronic image sensor. It is determined by exposure time, lens f-number, and scene luminance. Exposure is measured in units of lux-seconds (symbol lx⋅s), and can be computed from exposure value (EV) and scene luminance in a specified region.

An "exposure" is a single shutter cycle. For example, a long exposure refers to a single, long shutter cycle to gather enough dim light, whereas a multiple exposure involves a series of shutter cycles, effectively layering a series of photographs in one image. The accumulated *photometric exposure* (*H*v) is the same so long as the total exposure time is the same.

## Definitions

### Radiant exposure

**Radiant exposure** of a *surface*, denoted *H*e ("e" for "energetic", to avoid confusion with photometric quantities) and measured in J/m2, is given by $H_{\mathrm {e} }=E_{\mathrm {e} }t,$ where

- *E*e is the irradiance of the surface, measured in watts per square-meter, W/m2;
- t is the exposure duration, measured in seconds.

### Luminous exposure

**Luminous exposure** of a *surface*, denoted *H*v ('v' for 'visual', to avoid confusion with radiometric quantities) and measured in lux-seconds, is given by| $H_{\mathrm {v} }=E_{\mathrm {v} }t,$ where

- *E*v is the illuminance of the surface, measured in lux; and
- t is the exposure duration, measured in seconds.

If the measurement is adjusted to account only for light that reacts with the photo-sensitive surface, that is, weighted by the appropriate spectral sensitivity, the exposure is still measured in radiometric units (joules per square meter), rather than photometric units (weighted by the nominal sensitivity of the human eye). Only in this appropriately weighted case does the H measure the effective amount of light falling on the film, such that the characteristic curve will be correct independent of the spectrum of the light.

Many photographic materials are also sensitive to "invisible" light, which can be a nuisance , or a benefit . The use of radiometric units is appropriate to characterize such sensitivity to invisible light.

In sensitometric data, such as characteristic curves, the *log exposure* is conventionally expressed as log10(*H*). Photographers more familiar with base-2 logarithmic scales (such as exposure values) can convert using log2(*H*) ≈ 3.32 log10(*H*).

| Quantity | Unit | Dimension | Notes |   |   |
|---|---|---|---|---|---|
| Name | Symbol | Name | Symbol |   |   |
| Radiant energy | *Q*e | joule | J | **M**⋅**L**2⋅**T**−2 | Energy of electromagnetic radiation. |
| Radiant energy density | *w*e | joule per cubic metre | J/m3 | **M**⋅**L**−1⋅**T**−2 | Radiant energy per unit volume. |
| Radiant flux | Φe | watt | W = J/s | **M**⋅**L**2⋅**T**−3 | Radiant energy emitted, reflected, transmitted or received, per unit time. This is sometimes also called "radiant power", and called luminosity in astronomy. |
| Spectral flux | Φe,*ν* | watt per hertz | W/Hz | **M**⋅**L**2⋅**T** −2 | Radiant flux per unit frequency or wavelength. The latter is commonly measured in W⋅nm−1. |
| Φe,*λ* | watt per metre | W/m | **M**⋅**L**⋅**T**−3 |   |   |
| Radiant intensity | *I*e,Ω | watt per steradian | W/sr | **M**⋅**L**2⋅**T**−3 | Radiant flux emitted, reflected, transmitted or received, per unit solid angle. This is a *directional* quantity. |
| Spectral intensity | *I*e,Ω,*ν* | watt per steradian per hertz | W⋅sr−1⋅Hz−1 | **M**⋅**L**2⋅**T**−2 | Radiant intensity per unit frequency or wavelength. The latter is commonly measured in W⋅sr−1⋅nm−1. This is a *directional* quantity. |
| *I*e,Ω,*λ* | watt per steradian per metre | W⋅sr−1⋅m−1 | **M**⋅**L**⋅**T**−3 |   |   |
| Radiance | *L*e,Ω | watt per steradian per square metre | W⋅sr−1⋅m−2 | **M**⋅**T**−3 | Radiant flux emitted, reflected, transmitted or received by a *surface*, per unit solid angle per unit projected area. This is a *directional* quantity. This is sometimes also called "intensity". |
| Spectral radiance Specific intensity | *L*e,Ω,*ν* | watt per steradian per square metre per hertz | W⋅sr−1⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiance of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅sr−1⋅m−2⋅nm−1. This is a *directional* quantity. This is sometimes also called "spectral intensity". |
| *L*e,Ω,*λ* | watt per steradian per square metre, per metre | W⋅sr−1⋅m−3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Irradiance Flux density | *E*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *received* by a *surface* per unit area. This is sometimes also called "intensity". |
| Spectral irradiance Spectral flux density | *E*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Irradiance of a *surface* per unit frequency or wavelength. This is sometimes also called "spectral intensity". Non-SI units of spectral flux density include jansky (1 Jy = 10−26 W⋅m−2⋅Hz−1) and solar flux unit (1 sfu = 10−22 W⋅m−2⋅Hz−1 = 104 Jy). |
| *E*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiosity | *J*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *leaving* (emitted, reflected and transmitted by) a *surface* per unit area. This is sometimes also called "intensity". |
| Spectral radiosity | *J*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiosity of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅m−2⋅nm−1. This is sometimes also called "spectral intensity". |
| *J*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiant exitance | *M*e | watt per square metre | W/m2 | **M**⋅**T**−3 | Radiant flux *emitted* by a *surface* per unit area. This is the emitted component of radiosity. "Radiant emittance" is an old term for this quantity. This is sometimes also called "intensity". |
| Spectral exitance | *M*e,*ν* | watt per square metre per hertz | W⋅m−2⋅Hz−1 | **M**⋅**T**−2 | Radiant exitance of a *surface* per unit frequency or wavelength. The latter is commonly measured in W⋅m−2⋅nm−1. "Spectral emittance" is an old term for this quantity. This is sometimes also called "spectral intensity". |
| *M*e,*λ* | watt per square metre, per metre | W/m3 | **M**⋅**L**−1⋅**T**−3 |   |   |
| Radiant exposure | *H*e | joule per square metre | J/m2 | **M**⋅**T**−2 | Radiant energy received by a *surface* per unit area, or equivalently irradiance of a *surface* integrated over time of irradiation. This is sometimes also called "radiant fluence". |
| Spectral exposure | *H*e,*ν* | joule per square metre per hertz | J⋅m−2⋅Hz−1 | **M**⋅**T**−1 | Radiant exposure of a *surface* per unit frequency or wavelength. The latter is commonly measured in J⋅m−2⋅nm−1. This is sometimes also called "spectral fluence". |
| *H*e,*λ* | joule per square metre, per metre | J/m3 | **M**⋅**L**−1⋅**T**−2 |   |   |
| See also: SIRadiometryPhotometry\|(Compare) |   |   |   |   |   |

| Quantity | Unit | Dimension | Notes |   |   |
|---|---|---|---|---|---|
| Name | Symbol | Name | Symbol |   |   |
| Luminous energy | *Q*v | lumen second | lm⋅s | **T**⋅**J** | The lumen second is sometimes called the *talbot*. |
| Luminous flux, luminous power | Φv | lumen (= candela steradian) | lm (= cd⋅sr) | **J** | Luminous energy per unit time |
| Luminous intensity | *I*v | candela (= lumen per steradian) | cd (= lm/sr) | **J** | Luminous flux per unit solid angle |
| Luminance | *L*v | candela per square metre | cd/m2 (= lm/(sr⋅m2)) | **L**−2⋅**J** | Luminous flux per unit solid angle per unit *projected* source area. The candela per square metre is sometimes called the *nit*. |
| Illuminance | *E*v | lux (= lumen per square metre) | lx (= lm/m2) | **L**−2⋅**J** | Luminous flux *incident* on a surface |
| Luminous exitance, luminous emittance | *M*v | lumen per square metre | lm/m2 | **L**−2⋅**J** | Luminous flux *emitted* from a surface |
| Luminous exposure | *H*v | lux second | lx⋅s | **L**−2⋅**T**⋅**J** | Time-integrated illuminance |
| Luminous energy density | *ω*v | lumen second per cubic metre | lm⋅s/m3 | **L**−3⋅**T**⋅**J** |   |
| Luminous efficacy (of radiation) | *K* | lumen per watt | lm/W | **M**−1⋅**L**−2⋅**T**3⋅**J** | Ratio of luminous flux to radiant flux |
| Luminous efficacy (of a source) | η | lumen per watt | lm/W | **M**−1⋅**L**−2⋅**T**3⋅**J** | Ratio of luminous flux to power consumption |
| Luminous efficiency, luminous coefficient | V |   |   | **1** | Luminous efficacy normalized by the maximum possible efficacy |
| See also: SIPhotometryRadiometry\|(Compare) |   |   |   |   |   |

## Optimum exposure

So-called "correct" exposure may be defined as an exposure that achieves the effect the photographer intended.

A more technical approach recognises that a photographic film (or sensor) has a physically limited useful exposure range, sometimes called its dynamic range. If, for any part of the photograph, the actual exposure is outside this range, the film cannot record it accurately. In a very simple model, for example, out-of-range values would be recorded as "black" (underexposed) or "white" (overexposed) rather than the precisely graduated shades of colour and tone required to describe "detail". Therefore, the purpose of exposure adjustment (and/or lighting adjustment) is to control the physical amount of light from the subject that is allowed to fall on the film, so that 'significant' areas of shadow and highlight detail do not exceed the film's useful exposure range. This ensures that no 'significant' information is lost during capture.

The photographer may carefully overexpose or underexpose the photograph to *eliminate* what they judge as insignificant or unwanted detail; to make, for example, a white altar cloth appear immaculately clean, or to emulate the heavy, pitiless shadows of film noir. However, it is technically much easier to discard recorded information during post processing than to try to 're-create' unrecorded information.

In a scene with strong or harsh lighting, the *ratio* between highlight and shadow luminance values may well be larger than the ratio between the film's maximum and minimum useful exposure values. In this case, adjusting the camera's exposure settings (which only applies changes to the whole image, not selectively to parts of the image) only allows the photographer to choose between underexposed shadows or overexposed highlights; it cannot bring both into the useful exposure range at the same time. Methods for dealing with this situation include: using what is called fill lighting to increase the illumination in shadow areas; using a graduated neutral-density filter, flag, scrim, or gobo to reduce the illumination falling upon areas deemed too bright; or varying the exposure between multiple, otherwise identical, photographs (exposure bracketing) and then combining them afterwards in an HDRI process.

### Overexposure and underexposure

A photograph may be described as *overexposed* when it has a loss of highlight detail, that is, when important bright parts of an image are "washed out" or effectively all white, known as "blown-out highlights" or "clipped whites". A photograph may be described as *underexposed* when it has a loss of shadow detail, that is, when important dark areas are "muddy" or indistinguishable from black, known as "blocked-up shadows" (or sometimes "crushed shadows", "crushed blacks", or "clipped blacks", especially in video). As the adjacent image shows, these terms are technical ones rather than artistic judgments; an overexposed or underexposed image may be "correct" in the sense that it provides the effect that the photographer intended. Intentionally over- or underexposing (relative to a standard or the camera's automatic exposure) is casually referred to as "exposing to the right" or "exposing to the left" respectively, as these shift the histogram of the image to the right or left.

## Exposure settings

### Manual exposure

In manual mode, the photographer adjusts the lens aperture and/or shutter speed to achieve the desired exposure. Many photographers choose to control aperture and shutter independently because opening up the aperture increases exposure, but also decreases the depth of field, and a slower shutter increases exposure but also increases the opportunity for motion blur.

"Manual" exposure calculations may be based on some method of light metering with a working knowledge of exposure values, the APEX system and/or the Zone System.

### Automatic exposure

A camera in **automatic exposure** or **autoexposure** (usually initialized as **AE**) mode automatically calculates and adjusts exposure settings to match (as closely as possible) the subject's mid-tone to the mid-tone of the photograph. For most cameras, this means using an on-board TTL exposure meter.

Aperture priority (commonly abbreviated as *A*, or *Av* for "aperture value") mode gives the photographer manual control of the aperture, whilst the camera automatically adjusts the shutter speed to achieve the exposure specified by the TTL meter. Shutter priority (often abbreviated as *S*, or *Tv* for "time value") mode gives manual shutter control, with automatic aperture compensation. In each case, the actual exposure level is still determined by the camera's exposure meter.

### Exposure compensation

The purpose of an exposure meter is to estimate the subject's mid-tone luminance and indicate the camera exposure settings required to record this as a mid-tone. In order to do this it has to make a number of assumptions which, under certain circumstances, will be wrong. If the exposure setting indicated by an exposure meter is taken as the "reference" exposure, the photographer may wish to deliberately *overexpose* or *underexpose* in order to compensate for known or anticipated metering inaccuracies.

Cameras with any kind of internal exposure meter usually feature an exposure compensation setting which is intended to allow the photographer to simply offset the exposure level from the internal meter's estimate of appropriate exposure. Frequently calibrated in stops, also known as EV units, a "+1" exposure compensation setting indicates one stop more (twice as much) exposure and "−1" means one stop less (half as much) exposure.

Exposure compensation is particularly useful in combination with auto-exposure mode, as it allows the photographer to *bias* the exposure level without resorting to full manual exposure and losing the flexibility of auto exposure. On low-end video camcorders, exposure compensation may be the only manual exposure control available.

## Exposure control

An appropriate exposure for a photograph is determined by the sensitivity of the medium used. For photographic film, sensitivity is referred to as film speed and is measured on a scale published by the International Organization for Standardization (ISO). Faster film, that is, film with a higher ISO rating, requires less exposure to make a readable image. Digital cameras usually have variable ISO settings that provide additional flexibility. Exposure is a combination of the length of time and the illuminance at the photosensitive material. Exposure time is controlled in a camera by shutter speed, and the illuminance depends on the lens aperture and the scene luminance. Slower shutter speeds (exposing the medium for a longer period of time), greater lens apertures (admitting more light), and higher-luminance scenes produce greater exposures.

An approximately correct exposure will be obtained on a sunny day using ISO 100 film, an aperture of f/16 and a shutter speed of 1⁄100 of a second. This is called the sunny 16 rule: at an aperture of f/16 on a sunny day, a suitable shutter speed will be one over the film speed (or closest equivalent).

A scene can be exposed in many ways, depending on the desired effect a photographer wishes to convey.

## Reciprocity

An important principle of exposure is reciprocity. If one exposes the film or sensor for a longer period, a reciprocally smaller aperture is required to reduce the amount of light hitting the film to obtain the same exposure. For example, the photographer may prefer to make their sunny-16 shot at an aperture of f/5.6 (to obtain a shallow depth of field). As f/5.6 is 3 **stops** "faster" than f/16, with each stop meaning double the amount of light, a new shutter speed of (1⁄125)/(2·2·2) = 1⁄1000 s is needed. Once the photographer has determined the exposure, aperture stops can be traded for halvings or doublings of speed, within limits.

The true characteristic of most photographic emulsions is not actually linear (see sensitometry), but it is close enough over the exposure range of about 1 second to 1⁄1000 of a second. Outside of this range, it becomes necessary to increase the exposure from the calculated value to account for this characteristic of the emulsion. This characteristic is known as *reciprocity failure*. The film manufacturer's data sheets should be consulted to arrive at the correction required, as different emulsions have different characteristics.

Digital camera image sensors can also be subject to a form of reciprocity failure.

## Determining exposure

The Zone System is another method of determining exposure and development combinations to achieve a greater tonality range over conventional methods by varying the contrast of the film to fit the print contrast capability. Digital cameras can achieve similar results (high dynamic range) by combining several different exposures (varying shutter or diaphragm) made in quick succession.

Today, most cameras automatically determine the correct exposure at the time of taking a photograph by using a built-in light meter, or multiple point meters interpreted by a built-in computer, see metering mode.

Negative and print film tends to bias for exposing for the shadow areas (film dislikes being starved of light), with digital favouring exposure for highlights. See latitude below.

## Latitude

Latitude is the degree by which one can over, or under expose an image, and still recover an acceptable level of quality from an exposure. Typically negative film has a better ability to record a range of brightness than slide/transparency film or digital. Digital should be considered to be the reverse of print film, with a good latitude in the shadow range, and a narrow one in the highlight area; in contrast to film's large highlight latitude, and narrow shadow latitude. Slide/Transparency film has a narrow latitude in both highlight and shadow areas, requiring greater exposure accuracy.

Negative film's latitude increases somewhat with high ISO material, in contrast digital tends to narrow on latitude with high ISO settings.

### Highlights

Areas of a photo where information is lost due to extreme brightness are described as having "blown-out highlights" or "flared highlights".

In digital images this information loss is often irreversible, though small problems can be made less noticeable using photo manipulation software. Recording to raw image format can correct this problem to some degree, as can using a digital camera with a better sensor.

Film can often have areas of extreme overexposure but still record detail in those areas. This information is usually somewhat recoverable when printing or transferring to digital.

A loss of highlights in a photograph is usually undesirable, but in some cases can be considered to "enhance" appeal. Examples include black and white photography and portraits with an out-of-focus background.

### Blacks

Areas of a photo where information is lost due to extreme darkness are described as "crushed blacks". Digital capture tends to be more tolerant of underexposure, allowing better recovery of shadow detail, than same-ISO negative print film.

Crushed blacks cause loss of detail, but can be used for artistic effect.
