---
title: "Optical flow"
source: https://en.wikipedia.org/wiki/Optical_flow
domain: mediapipe
license: CC-BY-SA-4.0
tags: mediapipe framework, pose estimation, gesture recognition, on device vision, real time perception
fetched: 2026-07-02
---

# Optical flow

**Optical flow** or **optic flow** is the pattern of apparent motion of objects, surfaces, and edges in a visual scene caused by the relative motion between an observer and a scene. Optical flow can also be defined as the distribution of apparent velocities of movement of brightness pattern in an image.

The concept of optic flow has roots as far back as Euclid's *Optics*, but its modern formulation arose from Second World War research into pilot vision during landing. Several researchers arrived at the idea independently; James J. Gibson gave it its most influential treatment, publishing his theory in 1947 and created the term "optic flow" in 1950.

The term optical flow is also used by roboticists, encompassing related techniques from image processing and control of navigation including motion detection, object segmentation, time-to-contact information, focus of expansion calculations, luminance, motion compensated encoding, and stereo disparity measurement.

## Estimation

Optical flow can be estimated in a number of ways. Broadly, optical flow estimation approaches can be divided into machine learning based models (sometimes called data-driven models), classical models (sometimes called knowledge-driven models) which do not use machine learning and hybrid models which use aspects of both learning based models and classical models.

### Classical models

Many classical models use the intuitive assumption of *brightness constancy*; that even if a point moves between frames, its brightness stays constant. To formalise this intuitive assumption, consider two consecutive frames from a video sequence, with intensity $I(x,y,t)$ , where $(x,y)$ refer to pixel coordinates and t refers to time. In this case, the brightness constancy constraint is

$I(x,y,t)-I(x+u,y+v,t+1)=0,$

where $\mathbf {w$ is the displacement vector between a point in the first frame and the corresponding point in the second frame. By itself, the brightness constancy constraint cannot be solved for u and v at each pixel, since there is only one equation and two unknowns. This is known as the *aperture problem*. Therefore, additional constraints must be imposed to estimate the flow field.

#### Regularized models

Perhaps the most natural approach to addressing the aperture problem is to apply a smoothness constraint or a *regularization constraint* to the flow field. One can combine both of these constraints to formulate estimating optical flow as an optimization problem, where the goal is to minimize the cost function of the form,

$E=\iint _{\Omega }\Psi (I(x+u,y+v,t+1)-I(x,y,t))+\alpha \Psi (|\nabla u|)+\alpha \Psi (|\nabla v|)dxdy,$

where $\Omega$ is the extent of the images $I(x,y)$ , $\nabla$ is the gradient operator, $\alpha$ is a constant, and $\Psi ()$ is a loss function.

This optimisation problem is difficult to solve owing to its non-linearity. To address this issue, one can use a *variational approach* and linearise the brightness constancy constraint using a first order Taylor series approximation. Specifically, the brightness constancy constraint is approximated as,

${\frac {\partial I}{\partial x}}u+{\frac {\partial I}{\partial y}}v+{\frac {\partial I}{\partial t}}=0.$

For convenience, the derivatives of the image, ${\tfrac {\partial I}{\partial x}}$ , ${\tfrac {\partial I}{\partial y}}$ and ${\tfrac {\partial I}{\partial t}}$ are often condensed to become $I_{x}$ , $I_{y}$ and $I_{t}$ . Doing so, allows one to rewrite the linearised brightness constancy constraint as,

$I_{x}u+I_{y}v+I_{t}=0.$

The optimization problem can now be rewritten as

$E=\iint _{\Omega }\Psi (I_{x}u+I_{y}v+I_{t})+\alpha \Psi (|\nabla u|)+\alpha \Psi (|\nabla v|)dxdy.$

For the choice of $\Psi (x)=x^{2}$ , this method is the same as the Horn-Schunck method. Of course, other choices of cost function have been used such as $\Psi (x)={\sqrt {x^{2}+\epsilon ^{2}}}$ , which is a differentiable variant of the $L^{1}$ norm.

To solve the aforementioned optimization problem, one can use the Euler-Lagrange equations to provide a system of partial differential equations for each point in $I(x,y,t)$ . In the simplest case of using $\Psi (x)=x^{2}$ , these equations are,

$I_{x}(I_{x}u+I_{y}v+I_{t})-\alpha \Delta u=0,$

$I_{y}(I_{x}u+I_{y}v+I_{t})-\alpha \Delta v=0,$

where $\Delta ={\frac {\partial ^{2}}{\partial x^{2}}}+{\frac {\partial ^{2}}{\partial y^{2}}}$ denotes the Laplace operator. Since the image data is made up of discrete pixels, these equations are discretised. Doing so yields a system of linear equations which can be solved for $(u,v)$ at each pixel, using an iterative scheme such as Gauss-Seidel.

Although, linearising the brightness constancy constraint simplifies the optimisation problem significantly, the linearisation is only valid for small displacements and/or smooth images. To avoid this problem, a multi-scale or coarse-to-fine approach is often used. In such a scheme, the images are initially downsampled and the linearised Euler-Lagrange equations are solved at the reduced resolution. The estimated flow field at this scale is then used to initialise the process at next scale. This initialisation process is often performed by warping one frame using the current estimate of flow field so that it is as similar to other as possible.

An alternate approach is to discretize the optimisation problem and then perform a search of the possible $(u,v)$ values without linearising it. This search is often performed using Max-flow min-cut theorem algorithms, linear programming or belief propagation methods.

These regularized methods typically require manual tuning of the Lagrange multiplier, the so-called regularization parameters. There has been some progress in the automatic determination of these parameters in the context of optical flow applied to particle image velocimetry (PIV) data.

#### Parametric models

Instead of applying the regularization constraint on a point by point basis as per a regularized model, one can group pixels into regions and estimate the motion of these regions. This is known as a *parametric model*, since the motion of these regions is parameterized. In formulating optical flow estimation in this way, one makes the assumption that the motion field in each region be fully characterised by a set of parameters. Therefore, the goal of a parametric model is to estimate the motion parameters that minimise a loss function which can be written as,

${\hat {\boldsymbol {\alpha }}}=\arg \min _{\boldsymbol {\alpha }}\sum _{(x,y)\in {\mathcal {R}}}g(x,y)\rho (x,y,I_{1},I_{2},u_{\boldsymbol {\alpha }},v_{\boldsymbol {\alpha }}),$

where ${\boldsymbol {\alpha }}$ is the set of parameters determining the motion in the region ${\mathcal {R}}$ , $\rho ()$ is data cost term, $g()$ is a weighting function that determines the influence of pixel $(x,y)$ on the total cost, and $I_{1}$ and $I_{2}$ are frames 1 and 2 from a pair of consecutive frames.

The simplest parametric model is the Lucas-Kanade method. This uses rectangular regions and parameterises the motion as purely translational. The Lucas-Kanade method uses the original brightness constancy constraint as the data cost term and selects $g(x,y)=1$ . This yields the local loss function,

${\hat {\boldsymbol {\alpha }}}=\arg \min _{\boldsymbol {\alpha }}\sum _{(x,y)\in {\mathcal {R}}}|I(x+u_{\boldsymbol {\alpha }},y+v_{\boldsymbol {\alpha }},t+1)-I(x,y,t)|.$

Other possible local loss functions include the negative normalized cross-correlation between the two frames.

### Learning-based models

Instead of seeking to model optical flow directly, one can train a machine learning system to estimate optical flow. Since 2015, when FlowNet was proposed, learning based models have been applied to optical flow and have gained prominence. Initially, these approaches were based on Convolutional Neural Networks arranged in a U-Net architecture, often utilizing encoder-decoder or feature pyramid structures, such as PWC-Net, which integrated cost volumes (a 4D tensor representing the matching costs between all pairs of pixels in two feature maps) and warping (the process of spatially transforming one image based on a predicted flow field) to refine flow estimates across multiple scales. However, with the advent of transformer architecture in 2017, transformer based models have gained prominence. A significant shift occurred with the introduction of RAFT (Recurrent All-Pairs Field Transforms), which replaced coarse-to-fine pyramids with a single GRU-based state that iteratively updates the flow field. By maintaining a constant feature resolution at 1/8 of the input, RAFT significantly improved the preservation of fine details and robustness to fast motion compared to previous bottleneck-heavy designs, influencing a wide range of subsequent models that adopt similar iterative update mechanisms.

However, the all-pairs correlation used in such models is computationally expensive; for high-resolution content like FullHD or 4K, global matching can require more than 32 GB of VRAM, making it impractical for consumer-grade GPUs. To address this, efficiency-focused methods such as Flow1D, MeFlow, and Memfof have been developed. While these approaches generally optimize memory usage by decomposing the 2D search space, the latter optimizes correlation volumes for high-resolution multi-frame sequences, providing a practical implementation for standard GPUs.

Most learning-based approaches to optical flow use supervised learning. In this case, many frame pairs of video data and their corresponding ground-truth flow fields are used to optimise the parameters of the learning-based model to accurately estimate optical flow. This process often relies on vast synthetic training datasets, such as FlyingChairs and FlyingThings3D, due to the number of parameters involved. The models are then evaluated on benchmarks like MPI Sintel, KITTI, and the high-resolution Spring dataset. However, models trained exclusively on synthetic data often struggle with the domain gap when applied to real-world footage.

To address this, some learning-based optical flow approaches use self-supervised learning (sometimes called unsupervised learning) to reduce the need for large datasets with ground-truth data and leverage real-world footage without labels during training. Instead of training models to minimise the differences between estimated and ground-truth flow fields, they are trained to achieve learning objectives such as brightness constancy and smoothness of the flow field. More recently, methods like CroCo have introduced cross-view completion pre-training. Forcing the network to predict the masked regions of one image using the full second image teaches the model a strong geometric understanding and better generalization than models trained solely on task-specific labels.

## Uses

Motion estimation and video compression have developed as a major aspect of optical flow research. While the optical flow field is superficially similar to a dense motion field derived from the techniques of motion estimation, optical flow is the study of not only the determination of the optical flow field itself, but also of its use in estimating the three-dimensional nature and structure of the scene, as well as the 3D motion of objects and the observer relative to the scene, most of them using the image Jacobian.

Optical flow was used by robotics researchers in many areas such as: object detection and tracking, image dominant plane extraction, movement detection, robot navigation and visual odometry. Optical flow information has been recognized as being useful for controlling micro air vehicles.

The application of optical flow includes the problem of inferring not only the motion of the observer and objects in the scene, but also the structure of objects and the environment. Since awareness of motion and the generation of mental maps of the structure of our environment are critical components of animal (and human) vision, the conversion of this innate ability to a computer capability is similarly crucial in the field of machine vision.

Consider a five-frame clip of a ball moving from the bottom left of a field of vision, to the top right. Motion estimation techniques can determine that on a two dimensional plane the ball is moving up and to the right and vectors describing this motion can be extracted from the sequence of frames. For the purposes of video compression (e.g., MPEG), the sequence is now described as well as it needs to be. However, in the field of machine vision, the question of whether the ball is moving to the right or if the observer is moving to the left is unknowable yet critical information. Not even if a static, patterned background were present in the five frames, could we confidently state that the ball was moving to the right, because the pattern might have an infinite distance to the observer.

Optical flow has also been applied to fluid mechanics as a method of estimating flow patterns in a non-invasive way if visible tracer particles are added. This approach is called particle image velocimetry (PIV). It has been shown that optical flow methods can provide higher accuracy than traditional cross-correlation in PIV processing .

## Optical flow sensor

Various configurations of optical flow sensors exist. One configuration is an image sensor chip connected to a processor programmed to run an optical flow algorithm. Another configuration uses a vision chip, which is an integrated circuit having both the image sensor and the processor on the same die, allowing for a compact implementation. An example of this is a generic optical mouse sensor used in an optical mouse. In some cases the processing circuitry may be implemented using analog or mixed-signal circuits to enable fast optical flow computation using minimal current consumption.

One area of contemporary research is the use of neuromorphic engineering techniques to implement circuits that respond to optical flow, and thus may be appropriate for use in an optical flow sensor. Such circuits may draw inspiration from biological neural circuitry that similarly responds to optical flow.

Optical flow sensors are used extensively in computer optical mice, as the main sensing component for measuring the motion of the mouse across a surface.

Optical flow sensors are also being used in robotics applications, primarily where there is a need to measure visual motion or relative motion between the robot and other objects in the vicinity of the robot. The use of optical flow sensors in unmanned aerial vehicles (UAVs), for stability and obstacle avoidance, is also an area of current research.

## History

As early as Euclid's *Optics* note was made of the geometry underlying optic flow. Helmholtz's nineteenth-century account of motion parallax also implicitly concerns it. However, its explicit identification arose during the Second World War due the need to understand how pilots judge height and direction during landing. John T. MacCurdy, in advise to the Royal Air Force in the late 1920s, had earlier observed that during a straight descent the point on the ground being approached stays fixed in the pilot's visual field while all other points appear to stream away from it. G. C. Grindley, in a classified 1942 report then mathematically analyzed how retinal velocity changed during self-motion to enable an individual to accurately estimate visual speed. He, however, considered only this as a cue to altitude and not information to determine travel.

James J. Gibson working for the U.S. Army Air Forces, first identified that retinal velocities radiate from a "focus of expansion" in the direction of travel. Moreover, that eye movements do not disturb this, and that it was the global pattern—not individual velocities—that provided this information. In 1947, he published the theory, and in 1950 gave the phenomenon the name "optic flow". In 1955, he together with Paul Olum and Frank Rosenblatt detailed its mathematics. Independently, the E. S. Calvert at the Royal Aircraft Establishment came to a similar ideas when researching on airport approach lighting. In 1949, he proposed them as the "parafoveal streamer theory" which described how pilots use the pattern and speed of visual streamers to control their descent.

Gibson stressed the importance of optic flow for affordance perception, the ability to discern possibilities for action within the environment. Followers of Gibson and his ecological approach to psychology have further demonstrated the role of the optical flow stimulus for the perception of movement by the observer in the world; perception of the shape, distance and movement of objects in the world; and the control of locomotion.
