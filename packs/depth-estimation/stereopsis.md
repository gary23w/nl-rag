---
title: "Stereopsis"
source: https://en.wikipedia.org/wiki/Stereopsis
domain: depth-estimation
license: CC-BY-SA-4.0
tags: monocular depth estimation, depth map prediction, stereo depth reconstruction, scene geometry inference, dense depth prediction
fetched: 2026-07-02
---

# Stereopsis

In the science of visual perception, **stereopsis** is the sensation that objects in space extend into depth, and that objects have different distances from each other. This sensation is much stronger than the suggestion of depth that is created by two-dimensional perspective.

In humans, at least two mechanisms produce the sensation of stereopsis: binocular depth vision and (monocular) motion vision. In binocular depth vision, the sensation arises from processing differences in retinal images resulting from the two eyes looking from different, but similar, directions (binocular disparity). In motion vision, the sensation arises from processing motion information when the observer moves (e.g. optical flow, parallax). The sensation of stereopsis is similar in both cases.

In research on depth vision, the term *stereopsis* is primarily used for binocular depth vision and not for the sensation of depth resulting from motion vision. Sometimes the term "relative depth" is used. This term emphasizes that it refers not to the distance to the observer, but to the mutual depth relationships of the perceived objects. If the meaning is clear from the context, the single word "depth" is also used instead of "relative depth." The word *stereopsis* comes from Greek *stereós* 'solid' and *ópsis* 'appearance, sight'. Together, these indicate seeing the outside of three-dimensional, "solid" objects.

Binocular depth vision comes in two qualities: *coarse stereopsis* and *fine stereopsis*. Fine stereopsis plays a role in the recognition of shapes and objects, and coarse stereopsis in spatial localization.

## Summary of research

Research into binocular depth vision begins with Charles Wheatstone, who was the first to make a stereoscope. At the end of the 19th century, he was the first to demonstrate that horizontal disparity of vertical lines is sufficient to evoke a sensation of depth. Bela Julesz showed in the 20th century that the sensation also occurs with dots (random dot stereogram) and that depth vision precedes the perception of forms. Jodi Krol showed around the same time that a light transition (edge) is necessary, but that two corresponding edges of opposite contrast do not give a depth sensation. He also found that the depth of the surfaces between these edges is an interpretation. The left and right visual directions should be stimulated at approximately the same time, but this does not have to happen at exactly the same time. This is illustrated by the Puflrich illusion.

Kenneth Ogle (1950) found that the quality of depth perception differs for small and large disparities and on this basis distinguishes different types of stereopsis. It is generally accepted that in the absence of a sensation of stereopsis the perceived image is usually seen in the plane of the horopter. John Foley (1972) describes that in exceptional cases the image can also appear slightly behind or in front of the horopter. Jodi Krol (1982) shows that the latter happens when the eyes are unconsciously directed slightly in front of or behind the intended fixation point due to certain reflexes and the fixation point is therefore not on the horopter.

Finally, nerve cells have been found in the visual cortex that are tuned to a certain disparity. These cells form the basis for neural models for binocular depth vision and for the solution of the correspondence problem to be discussed. These cells are part of two neurophysiological mechanisms that are specialized in shape and object recognition and in spatial localization, respectively.

## Binocular disparity

When attention is directed to a point F in space, automatic eye movements are performed, causing the eye to rotate and point F is mapped onto the point of the eye with which it can see most sharply, the fovea. The direction in which the eye then looks is called the *principle ocular direction*. Every other point in space is seen by the eye in a certain direction that can be expressed as the angle that this direction makes with the principle direction. This is called *visual direction* or simply *direction*. The directions in which each eye sees the same object are sometimes the same, but usually not. The difference in directions is called **disparity**. The separate article on directional vision explains how the brain combines the directions that each eye sees into a combined image with single images, double images and fused images that are apparently seen from a point in the middle between both eyes (cyclopean eye).

### Horizontal disparity

The horizontal distance of approximately 6.5 cm between the two eyes ensures that points in space that are at different depths relative to the fixation point have a horizontal difference in direction. This difference is called **horizontal disparity** and is expressed as the difference between the angles α and β in the figure. In addition to horizontal disparity, there is also *vertical disparity.* This term indicates a vertical disalignment between the two eyes which can be caused by vertical eye movement or tilting the head. The latter is usually partially or completely corrected with automatically performed eye movements. Vertical disparities can also evoke a sense of depth in some cases.

The terms horizontal and vertical disparity only make sense when the observer is upright. Another term that is sometimes used and that better describes the load is *binocular disparity.* Binocular disparity has many similarities with motion parallax and is therefore sometimes also called *binocular parallax.* Motion parallax also evokes a depth sensation, but it requires the observer to move or the observed objects to move relative to each other. Under neurophysiological mechanisms it can be read that motion parallax is possibly processed in the same system as coarse stereopsis.

### Horopter

Points at the same depth as the fixation point lie on a circle through both eyes and the fixation point. This circle is called the horopter. Points on this circle project onto corresponding points in both eyes, i.e. onto points that look in the same direction in the left and right eye. We perceive the horopter as a kind of screen on which we see the world.

#### Crossed disparity

The directions in both eyes of a point C that is closer than the horopter are seen crossed on this screen: the direction in which the direction of the left eye is seen is to the right of the direction of the right eye. This is called crossed disparity or negative disparity.

#### Parallel disparity

The directions in both eyes of a point P that is further away than the horopter are seen side by side on this screen: the right direction is seen on the right. This is called parallel disparity or positive disparity.

### Wheatstone's proof

Charles Wheatstone showed in 1838 that two objects that differ only in horizontal disparity produce a sensation of relative depth. To ensure that this sensation could not be caused by two-dimensional perspective, he used a pair of flat plates with two vertical lines, a line stereogram, to represent the visual directions, and invented the stereoscope to view these plates.

## Depth as a function of disparity

Ogle (1950) investigated how the sensation of depth depends on the degree of disparity. Ogle asked an observer to fixate a point F and then moved a vertical rod Y in depth away from X. The magnitude of the perceived depth was found to increase linearly at small disparities, and to decrease again at larger disparities, and to be completely absent at even larger disparities. In the latter case, Y was seen at the distance of the horopter.

If Ogle asked the observer to look back and forth between X and Y (vergence), depth perception was found to be possible over a much larger range.

According to the research of Ogle and others, depth differences are perceived only in a narrow region of space, further away and closer than the horopter and this occurs with three qualities: *fine stereopsis*, *coarse stereopsis* and *no stereopsis*.

### Fine stereopsis

With **fine stereopsis** the observer can indicate the size of the depth: the greater the disparity, the greater the perceived depth. Ogle used the term *patent stereopsis* for this. Later researchers replaced this term with *fine stereopsis*.

### Coarse stereopsis

With **coarse stereopsis** the observer can indicate whether one object is further away than the other, but not how much. Ogle used the term *qualitative stereopsis* for this. Later researchers replaced this term with *coarse stereopsis*.

### No stereopsis

In the remaining area, objects are seen without depth sensation, at or around the distance of the horopter, and usually as a double image.

## Conditions for binocular depth vision

Horizontal disparity is a condition for seeing relative depth, but not a sufficient condition. The visual directions in the left and right eyes must also have a certain similarity, such as equal light transitions (edges) or spots, and must be stimulated more or less simultaneously. Eye movements ensure that objects in space fall on corresponding points in both eyes as much as possible and the disparity remains as small as possible.

### Equal edges

Hering suggested as early as 1864 that the visual directions must contain equal "edges" and that the surfaces between these edges are "filled in" during perception. This has been confirmed by Krol (1982, p. 38-39). Edges with an opposite contrast do not give a depth sensation. Seeing an opposite contrast triggers an eye movement reflex, which means that the opposite contrasts do not fall on corresponding points and the edges appear to lie slightly in front of or behind the fixation point.

### Color and brightness

The color and brightness do not have to be the same. Stereopsis even occurs with opposite colors, where the perceived color alternates between the two colors. There is no color mixing (Krol 1982, p. 38-39).

### Random dot stereogram

Julesz (1971) has shown with random dot stereograms that stereopsis also occurs when the visual directions consist of small, random white and black spots, where a certain group of spots in the left image has shifted in the right eye. Each eye alone sees only spots, but both eyes together see the group of shifted spots as a shape with depth.

**Figure.** *Random dot stereogram*

**Figure *Hidden shape***. *The image alternates between the left and right images of the random dot stereogram above. The movement that then becomes visible reveals which shape is hidden in the stereogram. In this case, a square. This square also becomes visible when the stereogram is viewed through a stereoscope, only then the square does not move.*

### Simultaneity

The visual direction in the left and right eyes must be stimulated simultaneously or in quick succession. An illustration of non-simultaneous stimulation is the Pulfrich illusion, in which (according to the explanation of the Pulfrich effect) a dark glass in front of one of the eyes delays the signals from that eye.

When viewing the back and forth movement of a car windshield wiper with a gray filter or sunglasses lens in front of one eye, the wiper appears to make an elliptical movement in depth. It even appears to move through the glass. This illusion was first described by Pulfrich in 1922.

### Eye movement

Eye movements are important to achieve and maintain the conditions necessary for stereopsis. Vertical eye movements and rotational movements ensure that the images in the left and right eyes are at the correct, equal height and remain at the same height when the head is not upright. Vergence movements (convergence and divergence) ensure that the horopter is positioned and held in space in such a way that objects of interest lie optimally within the area for stereopsis. A large part of these movements occurs reflexively.

#### Checking for correct fixation

To ensure that the eyes fixate the correct point (vergence) and that reflexes do not influence the result during research, various methods are used. One method consists of unexpectedly and briefly presenting the stimuli so that the eyes do not have time to perform an eye movement reflex. Another method consists of making visible with so-called vernier lines that the observer is fixating correctly. The left and right eyes both see a hairline, above and below the fixation point respectively, that the other eye does not see and that must be aligned. A final method consists of registering the eye movements during the experiment.

## Correspondence problem

If there is a visual direction in one eye that can be combined with multiple visual directions in the other eye to give a sensation of depth, then the brain is faced with a choice problem: which combination is the right one and is seen? Julesz calls this the correspondence problem and has investigated this problem with random dot stereograms. This research shows, among other things, that the visual system prefers to see surfaces (globality principle) and that shapes are only filled in after disparities have been established. Krol has also investigated the correspondence problem, but now with natural stimuli (double-nail illusion), whereby by feeling and looking from multiple positions it can be determined which "interpretation" is the correct one. It turns out that the interpretation with the least depth is always seen.

### Binocular ghost images

In the double-nail illusion, two nails or needles are placed at the shown positions A and B. Under the right observation conditions, these needles are invisible and instead of these real objects, two needles are seen at positions C and D. These needles are not really there and are therefore called ghost images by Krol.

## Neurophysiological mechanisms

In the 1960s, Horace Barlow, Colin Blakemore, and Jack Pettigrew found neurons in the cat visual cortex that had their receptive fields in different horizontal positions in the two eyes. This established the neural basis for stereopsis. Their findings were disputed by David Hubel and Torsten Wiesel, although they eventually conceded when they found similar neurons in the monkey visual cortex. In the 1980s, Gian Poggio and others found neurons in V2 of the monkey brain that responded to the depth of random-dot stereograms.

Fine stereopsis appears to be processed by a system of small cells that processes fine detail and color in an environment that changes relatively slowly. This system plays a major role in the recognition of shapes and objects and is concerned with "what" is seen. Coarse stereopsis (and associated double vision) is processed by a system of large cells that process large changes such as motion, contrast, and rapid changes in a relatively rapidly changing environment. This system is focused on localization and orientation in space. The nerve pathways of both systems run from the eyes to the visual cortex. The fine stereopsis system then extends to the inferior temporal cortex where "what" information is processed (parvo pathway). The coarse stereopsis system extends to the posterior parietal cortex where "where" and "how" information is processed (magno pathway). Both systems appear to operate partially in parallel but also work together. If one system fails, the other system can sometimes still function: people who do not have fine stereopsis can sometimes experience coarse stereopsis. For dynamic disparity processing, see

## Benefits

Stereopsis has a positive effect on practicing practical tasks such as threading a needle and catching balls (especially in fast ball games).), pouring liquids, and others. Occupational activities may include operating stereoscopic instruments such as a binocular microscope. Although some of these tasks may benefit from compensation of the visual system by means of other depth cues, there are some functions for which stereopsis is necessary. Occupations that require accurate distance judgment sometimes require some degree of stereopsis; aircraft pilots in particular have such a requirement (even if the first pilot to fly solo around the world, Wiley Post, accomplished his feat with only monocular vision.) Also surgeons normally show high stereoacuity. Regarding driving, one study found a positive effect of stereopsis in specific situations, only at intermediate distances. Furthermore, a study among elderly people found that glare, visual field loss and the useful visual field were predictors of crash involvement, whereas older adults' visual acuity, contrast sensitivity, and stereoacuity scores were not associated with crashes.

Binocular vision has other advantages besides stereopsis, in particular the improvement of the quality of vision by binocular summation; People with strabismus (even those without diplopia) score lower on binocular summation, and this appears to prompt people with strabismus to close one eye in visually demanding situations. Stereopsis is also important for object recognition and for seeing through camouflage.
