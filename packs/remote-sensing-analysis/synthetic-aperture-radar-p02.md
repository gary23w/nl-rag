---
title: "Synthetic-aperture radar (part 2/2)"
source: https://en.wikipedia.org/wiki/Synthetic-aperture_radar
domain: remote-sensing-analysis
license: CC-BY-SA-4.0
tags: remote sensing analysis, multispectral imaging, vegetation index, synthetic-aperture radar
fetched: 2026-07-02
part: 2/2
---

## Typical operation

### Data collection

In a typical SAR application, a single radar antenna is attached to an aircraft or spacecraft such that a substantial component of the antenna's radiated beam has a wave-propagation direction perpendicular to the flight-path direction. The beam is allowed to be broad in the vertical direction so it will illuminate the terrain from nearly beneath the aircraft out toward the horizon.

#### Image resolution and bandwidth

Resolution in the range dimension of the image is accomplished by creating pulses which define very short time intervals, either by emitting short pulses consisting of a carrier frequency and the necessary sidebands, all within a certain bandwidth, or by using longer "chirp pulses" in which frequency varies (often linearly) with time within that bandwidth. The differing times at which echoes return allow points at different distances to be distinguished.

Image resolution of SAR in its range coordinate (expressed in image pixels per distance unit) is mainly proportional to the radio bandwidth of whatever type of pulse is used. In the cross-range coordinate, the similar resolution is mainly proportional to the bandwidth of the Doppler shift of the signal returns within the beamwidth. Since Doppler frequency depends on the angle of the scattering point's direction from the broadside direction, the Doppler bandwidth available within the beamwidth is the same at all ranges. Hence the theoretical spatial resolution limits in both image dimensions remain constant with variation of range. However, in practice, both the errors that accumulate with data-collection time and the particular techniques used in post-processing further limit cross-range resolution at long ranges.

#### Image resolution and beamwidth

The total signal is that from a beamwidth-sized patch of the ground. To produce a beam that is narrow in the cross-range direction, diffraction effects require that the antenna be wide in that dimension. Therefore, the distinguishing, from each other, of co-range points simply by strengths of returns that persist for as long as they are within the beam width is difficult with aircraft-carryable antennas, because their beams can have linear widths only about two orders of magnitude (hundreds of times) smaller than the range. (Spacecraft-carryable ones can do 10 or more times better.) However, if both the amplitude and the phase of returns are recorded, then the portion of that multi-target return that was scattered radially from any smaller scene element can be extracted by phase-vector correlation of the total return with the form of the return expected from each such element.

The process can be thought of as combining the series of spatially distributed observations as if all had been made simultaneously with an antenna as long as the beamwidth and focused on that particular point. The "synthetic aperture" simulated at maximum system range by this process not only is longer than the real antenna, but, in practical applications, it is much longer than the radar aircraft, and tremendously longer than the radar spacecraft.

Although some references to SARs have characterized them as "radar telescopes", their actual optical analogy is the microscope, the detail in their images being smaller than the length of the synthetic aperture. In radar-engineering terms, while the target area is in the "far field" of the illuminating antenna, it is in the "near field" of the simulated one. Careful design and operation can accomplish resolution of items smaller than a millionth of the range, for example, 30 centimetres (12 in) at 300 kilometres (190 mi).

#### Pulse transmission and reception

The conversion of return delay time to geometric range can be very accurate because of the natural constancy of the speed and direction of propagation of electromagnetic waves. However, for an aircraft flying through the never-uniform and never-quiescent atmosphere, the relating of pulse transmission and reception times to successive geometric positions of the antenna must be accompanied by constant adjusting of the return phases to account for sensed irregularities in the flight path. SAR's in spacecraft avoid that atmosphere problem, but still must make corrections for known antenna movements due to rotations of the spacecraft, even those that are reactions to movements of onboard machinery. Locating a SAR in a crewed space vehicle may require that the humans carefully remain motionless relative to the vehicle during data collection periods.

Returns from scatterers within the range extent of any image are spread over a matching time interval. The inter-pulse period must be long enough to allow farthest-range returns from any pulse to finish arriving before the nearest-range ones from the next pulse begin to appear, so that those do not overlap each other in time. On the other hand, the interpulse rate must be fast enough to provide sufficient samples for the desired across-range (or across-beam) resolution. When the radar is to be carried by a high-speed vehicle and is to image a large area at fine resolution, those conditions may clash, leading to what has been called SAR's ambiguity problem. The same considerations apply to "conventional" radars also, but this problem occurs significantly only when resolution is so fine as to be available only through SAR processes. Since the basis of the problem is the information-carrying capacity of the single signal-input channel provided by one antenna, the only solution is to use additional channels fed by additional antennas. The system then becomes a hybrid of a SAR and a phased array, sometimes being called a Vernier array.

### Data processing

Combining the series of observations requires significant computational resources, usually using Fourier transform techniques. The high digital computing speed now available allows such processing to be done in near-real time on board a SAR aircraft. (There is necessarily a minimum time delay until all parts of the signal have been received.) The result is a map of radar reflectivity, including both amplitude and phase.

#### Amplitude data

The amplitude information, when shown in a map-like display, gives information about ground cover in much the same way that a black-and-white photo does. Variations in processing may also be done in either vehicle-borne stations or ground stations for various purposes, so as to accentuate certain image features for detailed target-area analysis.

#### Phase data

Although the phase information in an image is generally not made available to a human observer of an image display device, it can be preserved numerically, and sometimes allows certain additional features of targets to be recognized.

#### Coherence speckle

Unfortunately, the phase differences between adjacent image picture elements ("pixels") also produce random interference effects called "coherence speckle", which is a sort of graininess with dimensions on the order of the resolution, causing the concept of resolution to take on a subtly different meaning. This effect is the same as is apparent both visually and photographically in laser-illuminated optical scenes. The scale of that random speckle structure is governed by the size of the synthetic aperture in wavelengths, and cannot be finer than the system's resolution. Speckle structure can be subdued at the expense of resolution.

#### Optical holography

Before rapid digital computers were available, the data processing was done using an optical holography technique. The analog radar data were recorded as a holographic interference pattern on photographic film at a scale permitting the film to preserve the signal bandwidths (for example, 1:1,000,000 for a radar using a 0.6-meter wavelength). Then light using, for example, 0.6-micrometer waves (as from a helium–neon laser) passing through the hologram could project a terrain image at a scale recordable on another film at reasonable processor focal distances of around a meter. This worked because both SAR and phased arrays are fundamentally similar to optical holography, but using microwaves instead of light waves. The "optical data-processors" developed for this radar purpose were the first effective analog optical computer systems, and were, in fact, devised before the holographic technique was fully adapted to optical imaging. Because of the different sources of range and across-range signal structures in the radar signals, optical data-processors for SAR included not only both spherical and cylindrical lenses, but sometimes conical ones.


## Image appearance

The following considerations apply also to real-aperture terrain-imaging radars, but are more consequential when resolution in range is matched to a cross-beam resolution that is available only from a SAR.

### Range, cross-range, and angles

The two dimensions of a radar image are range and cross-range. Radar images of limited patches of terrain can resemble oblique photographs, but not ones taken from the location of the radar. This is because the range coordinate in a radar image is perpendicular to the vertical-angle coordinate of an oblique photo. The apparent entrance-pupil position (or camera center) for viewing such an image is therefore not as if at the radar, but as if at a point from which the viewer's line of sight is perpendicular to the slant-range direction connecting radar and target, with slant-range increasing from top to bottom of the image.

Because slant ranges to level terrain vary in vertical angle, each elevation of such terrain appears as a curved surface, specifically a hyperbolic cosine one. Verticals at various ranges are perpendiculars to those curves. The viewer's apparent looking directions are parallel to the curve's "hypcos" axis. Items directly beneath the radar appear as if optically viewed horizontally (i.e., from the side) and those at far ranges as if optically viewed from directly above. These curvatures are not evident unless large extents of near-range terrain, including steep slant ranges, are being viewed.

### Visibility

When viewed as specified above, fine-resolution radar images of small areas can appear most nearly like familiar optical ones, for two reasons. The first reason is easily understood by imagining a flagpole in the scene. The slant-range to its upper end is less than that to its base. Therefore, the pole can appear correctly top-end up only when viewed in the above orientation. Secondly, the radar illumination then being downward, shadows are seen in their most-familiar "overhead-lighting" direction.

The image of the pole's top will overlay that of some terrain point which is on the same slant range arc but at a shorter horizontal range ("ground-range"). Images of scene surfaces which faced both the illumination and the apparent eyepoint will have geometries that resemble those of an optical scene viewed from that eyepoint. However, slopes facing the radar will be foreshortened and ones facing away from it will be lengthened from their horizontal (map) dimensions. The former will therefore be brightened and the latter dimmed.

Returns from slopes steeper than perpendicular to slant range will be overlaid on those of lower-elevation terrain at a nearer ground-range, both being visible but intermingled. This is especially the case for vertical surfaces like the walls of buildings. Another viewing inconvenience that arises when a surface is steeper than perpendicular to the slant range is that it is then illuminated on one face but "viewed" from the reverse face. Then one "sees", for example, the radar-facing wall of a building as if from the inside, while the building's interior and the rear wall (that nearest to, hence expected to be optically visible to, the viewer) have vanished, since they lack illumination, being in the shadow of the front wall and the roof. Some return from the roof may overlay that from the front wall, and both of those may overlay return from terrain in front of the building. The visible building shadow will include those of all illuminated items. Long shadows may exhibit blurred edges due to the illuminating antenna's movement during the "time exposure" needed to create the image.

### Mirroring artefacts and shadows

Surfaces that we usually consider rough will, if that roughness consists of relief less than the radar wavelength, behave as smooth mirrors, showing, beyond such a surface, additional images of items in front of it. Those mirror images will appear within the shadow of the mirroring surface, sometimes filling the entire shadow, thus preventing recognition of the shadow.

The direction of overlay of any scene point is not directly toward the radar, but toward that point of the SAR's current path direction that is nearest to the target point. If the SAR is "squinting" forward or aft away from the exactly broadside direction, then the illumination direction, and hence the shadow direction, will not be opposite to the overlay direction, but slanted to right or left from it. An image will appear with the correct projection geometry when viewed so that the overlay direction is vertical, the SAR's flight-path is above the image, and range increases somewhat downward.

### Objects in motion

Objects in motion within a SAR scene alter the Doppler frequencies of the returns. Such objects therefore appear in the image at locations offset in the across-range direction by amounts proportional to the range-direction component of their velocity. Road vehicles may be depicted off the roadway and therefore not recognized as road traffic items. Trains appearing away from their tracks are more easily properly recognized by their length parallel to known trackage as well as by the absence of an equal length of railbed signature and of some adjacent terrain, both having been shadowed by the train. While images of moving vessels can be offset from the line of the earlier parts of their wakes, the more recent parts of the wake, which still partake of some of the vessel's motion, appear as curves connecting the vessel image to the relatively quiescent far-aft wake. In such identifiable cases, speed and direction of the moving items can be determined from the amounts of their offsets. The along-track component of a target's motion causes some defocus. Random motions such as that of wind-driven tree foliage, vehicles driven over rough terrain, or humans or other animals walking or running generally render those items not focusable, resulting in blurring or even effective invisibility.

These considerations, along with the speckle structure due to coherence, take some getting used to in order to correctly interpret SAR images. To assist in that, large collections of significant target signatures have been accumulated by performing many test flights over known terrains and cultural objects.


## Commercial industry

In recent years, the commercialization of synthetic aperture radar (SAR) technology has expanded, with private companies launching SAR satellites to provide high-resolution imaging capabilities for various applications. These include environmental monitoring, disaster response, defense and intelligence, infrastructure monitoring, and maritime surveillance.

Capella Space, an American Earth observation company, operates a constellation of SAR satellites designed to provide all-weather, high-resolution imagery. Capella was the first U.S. company to deploy a commercial SAR satellite and continues to expand its fleet with advanced SAR capabilities, including higher resolution, faster revisit times, and automated tasking. SAR data is often used by government agencies, defense organizations, and commercial customers to monitor changes on Earth in near real-time.

Other commercial SAR providers include ICEYE, a Finnish company specializing in small SAR satellites, and Airbus, which operates the TerraSAR-X and PAZ missions. The commercial SAR industry has grown significantly as advancements in satellite miniaturization, cloud-based data processing, and artificial intelligence enhance accessibility and utility for a broad range of users.


## History

The history of synthetic-aperture radar begins in 1951, with the invention of the technology by mathematician Carl A. Wiley, and its development in the following decade. Initially developed for military use, the technology has since been applied in the field of planetary science.


## Relationship to phased arrays

A technique closely related to SAR uses an array (referred to as a "phased array") of real antenna elements spatially distributed over either one or two dimensions perpendicular to the radar-range dimension. These physical arrays are truly synthetic ones, indeed being created by synthesis of a collection of subsidiary physical antennas. Their operation need not involve motion relative to targets. All elements of these arrays receive simultaneously in real time, and the signals passing through them can be individually subjected to controlled shifts of the phases of those signals. One result can be to respond most strongly to radiation received from a specific small scene area, focusing on that area to determine its contribution to the total signal received. The coherently detected set of signals received over the entire array aperture can be replicated in several data-processing channels and processed differently in each. The set of responses thus traced to different small scene areas can be displayed together as an image of the scene.

In comparison, a SAR's (commonly) single physical antenna element gathers signals at different positions at different times. When the radar is carried by an aircraft or an orbiting vehicle, those positions are functions of a single variable, distance along the vehicle's path, which is a single mathematical dimension (not necessarily the same as a linear geometric dimension). The signals are stored, thus becoming functions, no longer of time, but of recording locations along that dimension. When the stored signals are read out later and combined with specific phase shifts, the result is the same as if the recorded data had been gathered by an equally long and shaped phased array. What is thus synthesized is a set of signals equivalent to what could have been received simultaneously by such an actual large-aperture (in one dimension) phased array. The SAR simulates (rather than synthesizes) that long one-dimensional phased array. Although the term in the title of this article has thus been incorrectly derived, it is now firmly established by half a century of usage.

While operation of a phased array is readily understood as a completely geometric technique, the fact that a synthetic aperture system gathers its data as it (or its target) moves at some speed means that phases which varied with the distance traveled originally varied with time, hence constituted temporal frequencies. Temporal frequencies being the variables commonly used by radar engineers, their analyses of SAR systems are usually (and very productively) couched in such terms. In particular, the variation of phase during flight over the length of the synthetic aperture is seen as a sequence of Doppler shifts of the received frequency from that of the transmitted frequency. Once the received data have been recorded and thus have become timeless, the SAR data-processing situation is also understandable as a special type of phased array, treatable as a completely geometric process.

The core of both the SAR and the phased array techniques is that the distances that radar waves travel to and back from each scene element consist of some integer number of wavelengths plus some fraction of a "final" wavelength. Those fractions cause differences between the phases of the re-radiation received at various SAR or array positions. Coherent detection is needed to capture the signal phase information in addition to the signal amplitude information. That type of detection requires finding the differences between the phases of the received signals and the simultaneous phase of a well-preserved sample of the transmitted illumination.
