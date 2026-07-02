---
title: "Ambisonic reproduction systems"
source: https://en.wikipedia.org/wiki/Ambisonic_reproduction_systems
domain: ambisonics
license: CC-BY-SA-4.0
tags: ambisonics audio, ambisonic sound field, surround sound ambisonics, spherical harmonic audio
fetched: 2026-07-02
---

# Ambisonic reproduction systems

The design of **speaker systems for Ambisonic playback** is governed by several constraints:

- the desired spatial operating range (horizontal-only, hemispherical, full-sphere),
- the predominant resolution (= Ambisonic order) of the expected program material,
- the desired localisation performance and size of listening area versus the available number of speakers and amplification channels, and
- the theoretically optimal distribution of speakers versus the actually available placement and/or rigging options.

This page attempts to discuss the interaction of these constraints and their various trade-offs in theory and practice, as well as perceptional advantages or drawbacks of specific speaker layouts which have been observed in actual deployments.

## General considerations

### Near-field effect

In its original formulation, Ambisonics assumed **plane-wave sources** for reproduction, which implies speakers that are infinitely far away. This assumption will lead to a pronounced bass boost for speaker rigs of small diameter, which increases with Ambisonic order. The cause is the very same proximity effect that occurs with directional microphones. Therefore, appropriate near-field compensation (bass equalisation) is beneficial.

### Speaker distance vs. angles

This same plane-wave assumption makes it possible to vary the distance of speakers within reasonable limits without upsetting the correct function of the decoder, provided that the difference is compensated with delay, the power is adjusted for uniform loudness at the center, and that per-speaker near-field compensation is used. Distance does not affect the decoder matrix.

Variable **speaker distance** is therefore the most important degree of freedom when deploying idealized layouts in actual rooms. It is constrained by the reverberation of the room which leads to uneven direct-to-reverb ratios between speakers at different distances, and the power handling capability of the most distant speaker. If speakers have to be moved very close, care must be taken to ensure they still cover the entire listening area with reasonably flat frequency response.

**Speaker angles** on the other hand should be adhered to as precisely as possible, unless an optimised irregular decoder can be generated in-the-field.

### Horizontal vs. full-sphere accuracy

For horizontal-only content, horizontal systems provide more stable localisation at high frequencies than full-sphere ones, as shown by a simulation of the energy vector ${\vec {r_{E}}}$ . Therefore, if occasional horizontal-only reproduction at the highest precision is desired, full-sphere layouts with a dense horizontal ring are preferable.

### Phasing

Since multiple speakers will inevitably radiate very highly correlated content, a moving listener may experience a **phasing effect** that affects the perceived timbre and can upset localisation. Phasing artefacts are most prominent in dry rooms on very precisely calibrated systems. They can be reduced by adding height speakers, which tend to smoothen the effect, or tuned to a subjective minimum by introducing staggered delays to the speakers, with the understanding that this may adversely affect low-frequency localisation if overdone.

Phasing problems usually become evident in walk-around environments, and are of less concern for a seated audience, unless the interference pattern is so dense that it is perceived by small head movements.

### Loudspeaker occlusion

For multi-listener environments and auditoria, the **occlusion of speakers** by other listeners must not be under-estimated. Generally, the higher the order and the more physically accurate the reproduction, the more robust it is, up to the point where occlusion produces realistic effects that are consistent with the affected listener's visual perception. For low order systems however, reconstruction can easily fail entirely when line-of-sight to speakers is blocked, which has led to odd seating arrangements in listening tests.

With-height systems usually provide more unhindered lines-of-sight per direction for a given audience, which might increase their robustness.

### Number of loudspeakers vs. source material resolution

Solvang and others have shown that using much more than the minimally required number of speakers can be detrimental. The reason is simple: more speakers with constant angular resolution means higher crosstalk and thus higher correlation between speakers. If not managed, this leads to stronger comb-filtering effect and phasing artefacts when the listener moves.

Therefore, with some decoding techniques, it may be advisable to consider if and how a reasonably regular lower-order decoder that omits some speakers can be fitted into any higher-order system design. For example, the third-order octagon allows for a perfectly regular first-order square using only every other speaker.

## Horizontal-only systems

**Horizontal-only playback rigs** are the most commonly deployed and most extensively researched Ambisonic speaker systems, because they constitute an economic next step after conventional stereo. They can reproduce full-sphere content, but elevated sources will be projected onto the horizontal plane, and sources at zenith and nadir will be reproduced in mono by all available speakers.

The literature is rife with horizontal decoders based on the simpler cylindrical harmonics, which do not depend on the elevation angle $\phi$ . Their use is discouraged, because they wrongly assume cylindrical waves which would require perfect line sources for reproduction. Actual speakers are point sources and will inevitably leak energy along the vertical axis, which has consequences for near-field compensation and the tuning of dual-band decoders. Hence, cylindrical decoders do not usually fulfill the Ambisonic criteria.

### Triangle

The theoretical minimum of speakers for horizontal playback is $2\ell +1$ , or the number of Ambisonic components. However, the triangle demonstrates that at least one more speaker is necessary for proper soundfield reconstruction, since it exhibits extreme *speaker detention*: when panned around, sounds will stick to speaker locations and then jump across to the next speaker, rather than showing uniform motion. As a consequence, the directions of ${\vec {r_{V}}}$ and ${\vec {r_{E}}}$ do not match between speakers, which causes localisation errors.

Hence, the triangle is a suitable setup for Ambisonic reproduction only at low frequencies.

### Square or rectangular setups

Four-speaker setups are the most economical way of reproducing first-order horizontal material, and a rectangular layout is most easily fit into a living room, which makes these setups the most common in domestic environments. With rectangles, there is a localisation performance trade-off: the short sides will localise more stably than the square, the long sides worse. Consequently, for predominantly frontal sound stages, Benjamin, Lee, and Heller (2008) have observed a preference for rectangular layouts over squares.

All legacy domestic hardware decoders supported rectangular layouts, usually with variable aspect ratios.

### ITU 5.1

It is tempting to consider 5.1 systems for Ambisonic playback due to their wide availability, but the ITU-R BS775 layout is quite hostile to Ambisonics due to its extreme irregularity. The three front speakers are so close together (-30°, 0°, +30°) that they will exhibit significant crosstalk in first-order, which causes irritating phasing artefacts without any benefit. Therefore, it is advisable to omit the center speaker and decode only for L, R, Ls and Rs, as has been done in all pre-decoded *G-format* releases for 5.1. These G-format disks also assume a rectangular layout. If first-order playback is desired, the rear speakers should be moved accordingly, otherwise the Ambisonic imaging will be very unstable due to the wide angle between the surround speakers.

Decoding approaches to 5.1 were first suggested by Gerzon and Barton in 1992 and subsequently patented. Adriansen provides a free second-order decoder obtained by genetic search, and Wiggins (2007) has shown that source material as high as fourth order can be beneficial in order to 'steer' the decoding functions, even though the system is unable to reproduce the full spatial resolution.

Second and third-order material can be played satisfactorily over the ITU 5.1 layout, but due to the problems with first-order reproduction, it should not be considered for Ambisonics except as a compromise when 5.1 content predominates.

### Hexagon

If six speakers and sufficient space are available, the hexagon is a very good option that has outperformed four-channel setups for first-order reproduction in listening tests and is capable of second-order reproduction. It can be driven by an inexpensive 5.1 sound card and domestic 5.1 amplifier, provided the LFE output is full-range.

When used with one speaker in front, the hexagon can be abused for native 5.1 playback at the expense of a significantly wider and more blurry stereo stage (120° as opposed to 60° between L and R as per ITU-R BS775). Alternatively, reasonably sharp virtual speakers at the canonical ITU locations can be created with second-order panners - this is an interesting option if a phantom center is tolerable, and it will also work with a two-in-front orientation, which leaves more room for a TV or projection screen.

### Octagon

The Octagon is a flexible choice for up to third-order playback. When oriented one-in-front, it can be used for reasonably accurate native 5.1 playback (L and R at +/- 45° vs. 30°, and surrounds within the standardized sector at +/- 112.5°). For first order, phasing artefacts might become obvious under non-reverberant listening conditions due to the use of significantly more speakers than required, and Solvang's results (2008) suggest slightly increased timbral defects outside the sweet spot.

With eight channels, an octagon can be driven by affordable 7.1 consumer equipment, again as long as the LFE output is full-range. Driven in third order, it is a reasonable lower bound for concert sound reinforcement over an extended listening area, either for native Ambisonic content or to produce virtual speakers, which has been found to scale to several hundred listeners under favourable conditions.

## Systems with limited height reproduction

### Stacked rings

Stacked rings have been a popular way of obtaining limited with-height reproduction. Spatial resolution will be weak close to the zenith and nadir, but these are somewhat rare positions for sound sources. Rings are generally easier to rig than (hemi-)spherical setups because they do not require overhead trussing, speaker stands can be shared unless the rings are twisted, and entrances, fire escape routes etc. can be more easily accommodated for.

Double hexagons and octagons are the most common variations.

Since the introduction of #H#V mixed-order schemes by Travis (2009), stacked rings can be operated at their full horizontal resolution even for elevated sources. #H#V decoding matrices for common layouts are available from Adriaensen (2012).

Triple rings are rare, but have been used to good effect.

### Upper hemisphere systems

Since stacked rings are somewhat wasteful at higher elevations and necessarily have a hole at the zenith, they have been largely surpassed by hemispherical layouts since mature methods for decoder generation have become available. As they are difficult to rig and require overhead points, hemispheres are usually found either in permanent installations or experimental studios, where expensive and visually intrusive trussing is not an issue.

## Full-sphere systems: Platonic solids

The regular Platonic solids are the only full-sphere layouts for which closed-form solutions for decoding matrices exist. Before the development and adoption of modern mathematical tools for the optimisation of irregular layouts and the generation of T-designs and Lebedev grids with higher numbers of speakers, the regular polyhedra were the only tractable options.

### Tetrahedron

Tetrahedral speaker setups were used in the 1970s for first trials of full-sphere sound reproduction. One such experiment conducted by the Oxford University Tape Recording Society was documented by Michael Gerzon in 1971. In this setup, the tetrahedron was inscribed into a cuboid, using every other corner.

Despite Gerzon's somewhat over-enthusiastic description (which pre-dates the introduction of Ambisonics and the proper formulation of its psychoacoustic criteria), the tetrahedron exhibits the same stability problems in 3D that plague the triangle for horizontal-only reproduction. It is a viable option for adequate full-sphere reproduction only at low frequencies.

### Octahedron

The octahedron is difficult to set up in "upright" orientation, since the listener would occlude the floor speaker. Hence, a "slanted" setup is usually preferred. It provides basic full-sphere first-order reproduction for a single listener.

Goodwin (2009) has suggested a slanted octahedron with separate front center (which he calls 3D7.1) as an alternative way of using 7.1 systems to achieve with-height Ambisonic reproduction in games, and to allow reasonably accurate native 5.1 playback. An OpenAL game audio backend and decoder for this setup is commercially available.

### Cube

The most commonly encountered full-sphere systems are cubes or rectangular cuboids. The same localisation trade-offs apply as for square vs. rectangle (see above). Cuboids are easily fit into standard rooms and provide precise localisation in first order for a single listener plus enjoyable envelopment for one or two more, and they can be built using off-the shelf 7.1 components. If all speakers are placed in room corners, their acoustic loading and resulting bass boost will be uniform, which means they can all be equalised in the same way.

### Icosahedron

For the sake of consistency, we consider the vertices of the regular polyhedra as speaker positions, which makes the twelve-vertex icosahedron the next in the list. If suitable rigging options are available, it is capable of second-order full-sphere reproduction. A good and slightly more practical alternative is a horizontal hexagon complemented by two twisted triangles on floor and ceiling.

### Dodecahedron

With twenty vertices, the dodecahedron is capable of third-order full-sphere playback. Budget dodecahedra can be built by combining four domestic 5.1 sets as demonstrated at IRCAM's Studio 4, which would also allow for a square horizontal subwoofer decode,

## Irregular speaker layouts

It is possible to decode Ambisonics and Higher-Order Ambisonics onto fairly arbitrary speaker arrays, and this is a subject of ongoing research. A number of free decoding toolkits as well as a commercial implementation are available.

## Binaural stereo

Higher-Order Ambisonics can be decoded to produce 3D stereo headphone output similar to that produced using binaural recording. This can be done in a number of ways, including the use of virtual loudspeakers in combination with HRTF data. Other methods are possible.
