---
title: "Synthetic-aperture radar (part 1/2)"
source: https://en.wikipedia.org/wiki/Synthetic-aperture_radar
domain: remote-sensing-analysis
license: CC-BY-SA-4.0
tags: remote sensing analysis, multispectral imaging, vegetation index, synthetic-aperture radar
fetched: 2026-07-02
part: 1/2
---

# Synthetic-aperture radar

**Synthetic-aperture radar** (**SAR**) is a form of radar that is used to create two-dimensional images or three-dimensional reconstructions of objects, such as landscapes. SAR uses the motion of the radar antenna over a target region to provide finer spatial resolution than conventional stationary beam-scanning radars. SAR is typically mounted on a moving platform, such as an aircraft or spacecraft, and has its origins in an advanced form of side looking airborne radar (SLAR). The distance the SAR device travels over a target during the period when the target scene is illuminated creates the large *synthetic* antenna aperture (the *size* of the antenna). Typically, the larger the aperture, the higher the image resolution will be, regardless of whether the aperture is physical (a large antenna) or synthetic (a moving antenna) – this allows SAR to create high-resolution images with comparatively small physical antennas. For a fixed antenna size and orientation, objects which are further away remain illuminated longer – therefore SAR has the property of creating larger synthetic apertures for more distant objects, which results in a consistent spatial resolution over a range of viewing distances.

To create a SAR image, successive pulses of radio waves are transmitted to "illuminate" a target scene, and the echo of each pulse is received and recorded. The pulses are transmitted and the echoes received using a single beam-forming antenna, with wavelengths of a meter down to several millimeters. As the SAR device on board the aircraft or spacecraft moves, the antenna location relative to the target changes with time. Signal processing of the successive recorded radar echoes allows the combining of the recordings from these multiple antenna positions. This process forms the *synthetic antenna aperture* and allows the creation of higher-resolution images than would otherwise be possible with a given physical antenna.


## Motivation and applications

SAR is capable of high-resolution remote sensing, independent of flight altitude, and independent of weather, as SAR can select frequencies to avoid weather-caused signal attenuation. SAR has day and night imaging capability as illumination is provided by the SAR.

SAR images have wide applications in remote sensing and mapping of surfaces of the Earth and other planets. Applications of SAR are numerous. Examples include topography, oceanography, glaciology, geology (for example, terrain discrimination and subsurface imaging). SAR can also be used in forestry to determine forest height, biomass, and deforestation. Volcano and earthquake monitoring use differential interferometry. SAR can also be applied for monitoring civil infrastructure stability such as bridges. SAR is useful in environment monitoring such as oil spills, flooding, urban growth, and military surveillance: including strategic policy and tactical assessment. SAR can be implemented as inverse SAR by observing a moving target over a substantial time with a stationary antenna.


## Basic principle

A *synthetic-aperture radar* is an imaging radar mounted on a moving platform. SAR is a Doppler technique. It is based on the fact that "radar reflections from discrete objects in a passing radar beam field each [have] a minute Doppler, or speed, shift relative to the antenna".

> Carl Wiley, working at Goodyear, Arizona, (which later became Goodyear Aerospace, and eventually Lockheed Martin Corporation) in 1951, suggested the principle that — because each object in the radar beam has a slightly different speed relative to the antenna — each object will have its own doppler shift. A precise frequency analysis of the radar reflections will thus allow the construction of a detailed image.

In order to realise this concept, electromagnetic waves are transmitted sequentially, the echoes are collected and the system electronics digitizes and stores the data for subsequent processing. As transmission and reception occur at different times, they map to different small positions. The well ordered combination of the received signals builds a virtual aperture that is much longer than the physical antenna width. That is the source of the term "synthetic aperture," giving it the property of an imaging radar. The range direction is perpendicular to the flight track and perpendicular to the azimuth direction, which is also known as the *along-track* direction because it is in line with the position of the object within the antenna's field of view.

The 3D processing is done in two stages. The azimuth and range direction are focused for the generation of 2D (azimuth-range) high-resolution images, after which a digital elevation model (DEM) is used to measure the phase differences between complex images, which is determined from different look angles to recover the height information. This height information, along with the azimuth-range coordinates provided by 2-D SAR focusing, gives the third dimension, which is the elevation. The first step requires only standard processing algorithms, for the second step, additional pre-processing such as image co-registration and phase calibration is used.

In addition, multiple baselines can be used to extend 3D imaging to the *time dimension*. 4D and multi-D SAR imaging allows imaging of complex scenarios, such as urban areas, and has improved performance with respect to classical interferometric techniques such as persistent scatterer interferometry (PSI).


## Algorithm

SAR algorithms model the scene as a set of point targets that do not interact with each other (the Born approximation).

While the details of various SAR algorithms differ, SAR processing in each case is the application of a matched filter to the raw data, for each pixel in the output image, where the matched filter coefficients are the response from a single isolated point target. In the early days of SAR processing, the raw data was recorded on film and the postprocessing by matched filter was implemented optically using lenses of conical, cylindrical and spherical shape. The Range-Doppler algorithm is an example of a more recent approach.


## Existing spectral estimation approaches

Synthetic-aperture radar determines the 3D reflectivity from measured SAR data. It is basically a spectrum estimation, because for a specific cell of an image, the complex-value SAR measurements of the SAR image stack are a sampled version of the Fourier transform of reflectivity in elevation direction, but the Fourier transform is irregular. Thus the spectral estimation techniques are used to improve the resolution and reduce speckle compared to the results of conventional Fourier transform SAR imaging techniques.

### Non-parametric methods

#### FFT

FFT (Fast Fourier Transform i.e., periodogram or matched filter) is one such method, which is used in the majority of the spectral estimation algorithms, and there are many fast algorithms for computing the multidimensional discrete Fourier transform. Computational *Kronecker-core array algebra* is a popular algorithm used as new variant of FFT algorithms for the processing in multidimensional synthetic-aperture radar (SAR) systems. This algorithm uses a study of theoretical properties of input/output data indexing sets and groups of permutations.

A branch of finite multi-dimensional linear algebra is used to identify similarities and differences among various FFT algorithm variants and to create new variants. Each multidimensional DFT computation is expressed in matrix form. The multidimensional DFT matrix, in turn, is disintegrated into a set of factors, called functional primitives, which are individually identified with an underlying software/hardware computational design.

The FFT implementation is essentially a realization of the mapping of the mathematical framework through generation of the variants and executing matrix operations. The performance of this implementation may vary from machine to machine, and the objective is to identify on which machine it performs best.

##### Advantages

- Additive group-theoretic properties of multidimensional input/output indexing sets are used for the mathematical formulations, therefore, it is easier to identify mapping between computing structures and mathematical expressions, thus, better than conventional methods.
- The language of CKA algebra helps the application developer in understanding which are the more computational efficient FFT variants thus reducing the computational effort and improve their implementation time.

##### Disadvantages

- FFT cannot separate sinusoids close in frequency. If the periodicity of the data does not match FFT, edge effects are seen.

#### Capon method

The Capon spectral method, also called the minimum-variance method, is a multidimensional array-processing technique. It is a nonparametric covariance-based method, which uses an adaptive matched-filterbank approach and follows two main steps:

1. Passing the data through a 2D bandpass filter with varying center frequencies ( $\omega _{1},\omega _{2}$ ).
2. Estimating the power at ( $\omega _{1},\omega _{2}$ ) for all $\omega _{1}\in [0,2\pi ),\omega _{2}\in [0,2\pi )$ of interest from the filtered data.

The adaptive Capon bandpass filter is designed to minimize the power of the filter output, as well as pass the frequencies ( $\omega _{1},\omega _{2}$ ) without any attenuation, i.e., to satisfy, for each ( $\omega _{1},\omega _{2}$ ),

$\min _{h}h_{\omega _{1},\omega _{2}}^{*}Rh_{\omega _{1},\omega _{2}}$

subject to

$h_{\omega _{1},\omega _{2}}^{*}a_{\omega _{1},\omega _{2}}=1,$

where *R* is the covariance matrix, $h_{\omega _{1},\omega _{2}}^{*}$ is the complex conjugate transpose of the impulse response of the FIR filter, $a_{\omega _{1},\omega _{2}}$ is the 2D Fourier vector, defined as $a_{\omega _{1},\omega _{2}}\triangleq a_{\omega _{1}}\otimes a_{\omega _{2}}$ , $\otimes$ denotes Kronecker product.

Therefore, it passes a 2D sinusoid at a given frequency without distortion while minimizing the variance of the noise of the resulting image. The purpose is to compute the spectral estimate efficiently.

*Spectral estimate* is given as

$S_{\omega _{1},\omega _{2}}={\frac {1}{a_{\omega _{1},\omega _{2}}^{*}R^{-1}a_{\omega _{1},\omega _{2}}}},$

where *R* is the covariance matrix, and $a_{\omega _{1},\omega _{2}}^{*}$ is the 2D complex-conjugate transpose of the Fourier vector. The computation of this equation over all frequencies is time-consuming. It is seen that the forward–backward Capon estimator yields better estimation than the forward-only classical Capon approach. The main reason behind this is that while the forward–backward Capon uses both the forward and backward data vectors to obtain the estimate of the covariance matrix, the forward-only Capon uses only the forward data vectors to estimate the covariance matrix.

##### Advantages

- Capon can yield more accurate spectral estimates with much lower sidelobes and narrower spectral peaks than the fast Fourier transform (FFT) method.
- Capon method can provide much better resolution.

##### Disadvantages

- Implementation requires computation of two intensive tasks: inversion of the covariance matrix *R* and multiplication by the $a_{\omega _{1},\omega _{2}}$ matrix, which has to be done for each point $\left(\omega _{1},\omega _{2}\right)$ .

#### APES method

The APES (amplitude and phase estimation) method is also a matched-filter-bank method, which assumes that the phase history data is a sum of 2D sinusoids in noise.

APES spectral estimator has 2-step filtering interpretation:

1. Passing data through a bank of FIR bandpass filters with varying center frequency $\omega$ .
2. Obtaining the spectrum estimate for $\omega \in [0,2\pi )$ from the filtered data.

Empirically, the APES method results in wider spectral peaks than the Capon method, but more accurate spectral estimates for amplitude in SAR. In the Capon method, although the spectral peaks are narrower than the APES, the sidelobes are higher than that for the APES. As a result, the estimate for the amplitude is expected to be less accurate for the Capon method than for the APES method. The APES method requires about 1.5 times more computation than the Capon method.

##### Advantages

- Filtering reduces the number of available samples, but when it is designed tactically, the increase in signal-to-noise ratio (SNR) in the filtered data will compensate this reduction, and the amplitude of a sinusoidal component with frequency $\omega$ can be estimated more accurately from the filtered data than from the original signal.

##### Disadvantages

- The autocovariance matrix is much larger in 2D than in 1D, therefore it is limited by memory available.

### SAMV method

SAMV method is a parameter-free sparse signal reconstruction based algorithm. It achieves super-resolution and is robust to highly correlated signals. The name emphasizes its basis on the asymptotically minimum variance (AMV) criterion. It is a powerful tool for the recovery of both the amplitude and frequency characteristics of multiple highly correlated sources in challenging environment (e.g., limited number of snapshots, low signal-to-noise ratio). Applications include synthetic-aperture radar imaging and various source localization.

#### Advantages

SAMV method is capable of achieving resolution higher than some established parametric methods, e.g., MUSIC, especially with highly correlated signals.

#### Disadvantages

Computational complexity of the SAMV method is higher due to its iterative procedure.

### Parametric subspace decomposition methods

#### Eigenvector method

This subspace decomposition method separates the eigenvectors of the autocovariance matrix into those corresponding to signals and to clutter. The amplitude of the image at a point ( $\omega _{x},\omega _{y}$ ) is given by:

${\hat {\phi }}_{EV}\left(\omega _{x},\omega _{y}\right)={\frac {1}{W^{\mathsf {H}}\left(\omega _{x},\omega _{y}\right)\left(\sum _{\text{clutter}}{\frac {1}{\lambda _{i}}}{\underline {v_{i}}}\,{\underline {v_{i}}}^{\mathsf {H}}\right)W\left(\omega _{x},\omega _{y}\right)}}$

where ${\hat {\phi }}_{EV}$ is the amplitude of the image at a point $\left(\omega _{x},\omega _{y}\right)$ , ${\underline {v_{i}}}$ is the coherency matrix and ${\underline {v_{i}}}^{\mathsf {H}}$ is the Hermitian of the coherency matrix, ${\frac {1}{\lambda _{i}}}$ is the inverse of the eigenvalues of the clutter subspace, $W\left(\omega _{x},\omega _{y}\right)$ are vectors defined as

$W\left(\omega _{x},\omega _{y}\right)=\left[1\exp \left(-j\omega _{x}\right)\ldots \exp \left(-j(M-1)\omega _{x}\right)\right]\otimes \left[1\exp \left(-j\omega _{y}\right)\ldots \exp \left(-j(M-1)\omega _{y}\right)\right]$

where ⊗ denotes the Kronecker product of the two vectors.

##### Advantages

- Shows features of image more accurately.

##### Disadvantages

- High computational complexity.

#### MUSIC method

MUSIC detects frequencies in a signal by performing an eigen decomposition on the covariance matrix of a data vector of the samples obtained from the samples of the received signal. When all of the eigenvectors are included in the clutter subspace (model order = 0) the EV method becomes identical to the Capon method. Thus the determination of model order is critical to operation of the EV method. The eigenvalue of the R matrix decides whether its corresponding eigenvector corresponds to the clutter or to the signal subspace.

The MUSIC method is considered to be a poor performer in SAR applications. This method uses a constant instead of the clutter subspace.

In this method, the denominator is equated to zero when a sinusoidal signal corresponding to a point in the SAR image is in alignment to one of the signal subspace eigenvectors which is the peak in image estimate. Thus this method does not accurately represent the scattering intensity at each point, but show the particular points of the image.

##### Advantages

- MUSIC whitens or equalizes, the clutter eigenvalues.

##### Disadvantages

- Resolution loss due to the averaging operation.

### Backprojection algorithm

Backprojection Algorithm has two methods: *Time-domain Backprojection* and *Frequency-domain Backprojection*. The time-domain Backprojection has more advantages over frequency-domain and thus, is more preferred. The time-domain Backprojection forms images or spectrums by matching the data acquired from the radar and as per what it expects to receive. It can be considered as an ideal matched-filter for synthetic-aperture radar. There is no need of having a different motion compensation step due to its quality of handling non-ideal motion/sampling. It can also be used for various imaging geometries.

#### Advantages

- *It is invariant to the imaging mode*: which means, that it uses the same algorithm irrespective of the imaging mode present, whereas, frequency domain methods require changes depending on the mode and geometry.
- Ambiguous azimuth aliasing usually occurs when the Nyquist spatial sampling requirements are exceeded by frequencies. Unambiguous aliasing occurs in squinted geometries where the signal bandwidth does not exceed the sampling limits, but has undergone "spectral wrapping." Backprojection Algorithm does not get affected by any such kind of aliasing effects.
- *It matches the space/time filter:* uses the information about the imaging geometry, to produce a pixel-by-pixel varying matched filter to approximate the expected return signal. This usually yields antenna gain compensation.
- With reference to the previous advantage, the back projection algorithm compensates for the motion. This becomes an advantage at areas having low altitudes.

#### Disadvantages

- The computational expense is more for Backprojection algorithm as compared to other frequency domain methods.
- It requires very precise knowledge of imaging geometry.

#### Application: geosynchronous orbit synthetic-aperture radar (GEO-SAR)

In GEO-SAR, to focus specially on the relative moving track, the backprojection algorithm works very well. It uses the concept of Azimuth Processing in the time domain. For the satellite-ground geometry, GEO-SAR plays a significant role.

The procedure of this concept is elaborated as follows.

1. The raw data acquired is segmented or drawn into sub-apertures for simplification of speedy conduction of procedure.
2. The range of the data is then compressed, using the concept of "Matched Filtering" for every segment/sub-aperture created. It is given by- ${\textstyle s(t,\tau )=\exp \left(-j\cdot {\frac {4\pi }{\lambda }}\cdot R(t)\right)\cdot \operatorname {sinc} \left(\tau -{\frac {2}{c}}\cdot R(t)\right)}$ where *τ* is the range time, *t* is the azimuthal time, *λ* is the wavelength, *c* is the speed of light.
3. Accuracy in the "Range Migration Curve" is achieved by range interpolation.
4. The pixel locations of the ground in the image is dependent on the satellite–ground geometry model. Grid-division is now done as per the azimuth time.
5. Calculations for the "slant range" (range between the antenna's phase center and the point on the ground) are done for every azimuth time using coordinate transformations.
6. Azimuth Compression is done after the previous step.
7. Step 5 and 6 are repeated for every pixel, to cover every pixel, and conduct the procedure on every sub-aperture.
8. Lastly, all the sub-apertures of the image created throughout, are superimposed onto each other and the ultimate HD image is generated.

### Comparison between the algorithms

Capon and APES can yield more accurate spectral estimates with much lower sidelobes and more narrow spectral peaks than the fast Fourier transform (FFT) method, which is also a special case of the FIR filtering approaches. It is seen that although the APES algorithm gives slightly wider spectral peaks than the Capon method, the former yields more accurate overall spectral estimates than the latter and the FFT method.

FFT method is fast and simple but have larger sidelobes. Capon has high resolution but high computational complexity. EV also has high resolution and high computational complexity. APES has higher resolution, faster than capon and EV but high computational complexity.

MUSIC method is not generally suitable for SAR imaging, as whitening the clutter eigenvalues destroys the spatial inhomogeneities associated with terrain clutter or other diffuse scattering in SAR imagery. But it offers higher frequency resolution in the resulting power spectral density (PSD) than the fast Fourier transform (FFT)-based methods.

The backprojection algorithm is computationally expensive. It is specifically attractive for sensors that are wideband, wide-angle, and/or have long coherent apertures with substantial off-track motion.


## Multistatic operation

SAR requires that echo captures be taken at multiple antenna positions. The more captures taken (at different antenna locations) the more reliable the target characterization.

Multiple captures can be obtained by moving a single antenna to different locations, by placing multiple stationary antennas at different locations, or combinations thereof.

The advantage of a single moving antenna is that it can be easily placed in any number of positions to provide any number of monostatic waveforms. For example, an antenna mounted on an airplane takes many captures per second as the plane travels.

The principal advantages of multiple static antennas are that a moving target can be characterized (assuming the capture electronics are fast enough), that no vehicle or motion machinery is necessary, and that antenna positions need not be derived from other, sometimes unreliable, information. (One problem with SAR aboard an airplane is knowing precise antenna positions as the plane travels).

For multiple static antennas, all combinations of monostatic and multistatic radar waveform captures are possible. Note, however, that it is not advantageous to capture a waveform for each of both transmission directions for a given pair of antennas, because those waveforms will be identical. When multiple static antennas are used, the total number of unique echo waveforms that can be captured is

${\frac {N^{2}+N}{2}}$

where *N* is the number of unique antenna positions.


## Scanning modes

### Stripmap mode airborne SAR

The antenna stays in a fixed position. It may be orthogonal to the flight path, or it may be squinted slightly forward or backward.

When the antenna aperture travels along the flight path, a signal is transmitted at a rate equal to the pulse repetition frequency (PRF). The lower boundary of the PRF is determined by the Doppler bandwidth of the radar. The backscatter of each of these signals is commutatively added on a pixel-by-pixel basis to attain the fine azimuth resolution desired in radar imagery.

### Spotlight mode SAR

The spotlight synthetic aperture is given by

$Lsa=r_{0}\Delta \theta _{a}$

where $\Delta \theta _{a}$ is the angle formed between the beginning and end of the imaging, as shown in the diagram of spotlight imaging and $r_{0}$ is the range distance.

The spotlight mode gives better resolution albeit for a smaller ground patch. In this mode, the illuminating radar beam is steered continually as the aircraft moves, so that it illuminates the same patch over a longer period of time. This mode is not a traditional continuous-strip imaging mode; however, it has high azimuth resolution. A technical explanation of spotlight SAR from first principles is offered in.

### Scan mode SAR

While operating as a scan mode SAR, the antenna beam sweeps periodically and thus cover much larger area than the spotlight and stripmap modes. However, the azimuth resolution become much lower than the stripmap mode due to the decreased azimuth bandwidth. Clearly there is a balance achieved between the azimuth resolution and the scan area of SAR. Here, the synthetic aperture is shared between the sub swaths, and it is not in direct contact within one subswath. Mosaic operation is required in azimuth and range directions to join the azimuth bursts and the range sub-swaths.

- ScanSAR makes the swath beam huge.
- The azimuth signal has many bursts.
- The azimuth resolution is limited due to the burst duration.
- Each target contains varied frequencies which completely depends on where the azimuth is present.


## Special techniques

### Polarimetry

Radar waves have a polarization. Different materials reflect radar waves with different intensities, but anisotropic materials such as grass often reflect different polarizations with different intensities. Some materials will also convert one polarization into another. By emitting a mixture of polarizations and using receiving antennas with a specific polarization, several images can be collected from the same series of pulses. Frequently three such RX-TX polarizations (HH-pol, VV-pol, VH-pol) are used as the three color channels in a synthesized image. This is what has been done in the picture at right. Interpretation of the resulting colors requires significant testing of known materials.

New developments in polarimetry include using the changes in the random polarization returns of some surfaces (such as grass or sand) and between two images of the same location at different times to determine where changes not visible to optical systems occurred. Examples include subterranean tunneling or paths of vehicles driving through the area being imaged. Enhanced SAR sea oil slick observation has been developed by appropriate physical modelling and use of fully polarimetric and dual-polarimetric measurements.

#### SAR polarimetry

SAR polarimetry is a technique used for deriving qualitative and quantitative physical information for land, snow and ice, ocean and urban applications based on the measurement and exploration of the polarimetric properties of man-made and natural scatterers. *Terrain* and *land use* classification is one of the most important applications of polarimetric synthetic-aperture radar (PolSAR).

SAR polarimetry uses a scattering matrix (S) to identify the scattering behavior of objects after an interaction with electromagnetic wave. The matrix is represented by a combination of horizontal and vertical polarization states of transmitted and received signals.

$S={\begin{bmatrix}S_{HH}&S_{HV}\\S_{VH}&S_{VV}\end{bmatrix}}$

where, HH is for horizontal transmit and horizontal receive, VV is for vertical transmit and vertical receive, HV is for horizontal transmit and vertical receive, and VH for vertical transmit and horizontal receive.

The first two of these polarization combinations are referred to as like-polarized (or co-polarized), because the transmit and receive polarizations are the same. The last two combinations are referred to as cross-polarized because the transmit and receive polarizations are orthogonal to one another.

#### Three-component scattering power model

The three-component scattering power model by Freeman and Durden is successfully used for the decomposition of a PolSAR image, applying the reflection symmetry condition using covariance matrix. The method is based on simple physical scattering mechanisms (surface scattering, double-bounce scattering, and volume scattering). The advantage of this scattering model is that it is simple and easy to implement for image processing. There are 2 major approaches for a 3 $\times$ 3 polarimetric matrix decomposition. One is the lexicographic covariance matrix approach based on physically measurable parameters, and the other is the Pauli decomposition which is a coherent decomposition matrix. It represents all the polarimetric information in a single SAR image. The polarimetric information of [S] could be represented by the combination of the intensities $|S_{HH}|^{2},|S_{VV}|^{2},2|S_{HV}|^{2}$ in a single RGB image where all the previous intensities will be coded as a color channel.

#### Four-component scattering power model

For PolSAR image analysis, there can be cases where reflection symmetry condition does not hold. In those cases a *four-component scattering model* can be used to decompose polarimetric synthetic-aperture radar (SAR) images. This approach deals with the non-reflection symmetric scattering case. It includes and extends the three-component decomposition method introduced by Freeman and Durden to a fourth component by adding the helix scattering power. This helix power term generally appears in complex urban area but disappears for a natural distributed scatterer.

There is also an improved method using the four-component decomposition algorithm, which was introduced for the general polSAR data image analyses. The SAR data is first filtered which is known as speckle reduction, then each pixel is decomposed by four-component model to determine the surface scattering power ( $P_{s}$ ), double-bounce scattering power ( $P_{d}$ ), volume scattering power ( $P_{v}$ ), and helix scattering power ( $P_{c}$ ). The pixels are then divided into 5 classes (surface, double-bounce, volume, helix, and mixed pixels) classified with respect to maximum powers. A mixed category is added for the pixels having two or three equal dominant scattering powers after computation. The process continues as the pixels in all these categories are divided in 20 small clutter approximately of same number of pixels and merged as desirable, this is called cluster merging. They are iteratively classified and then automatically color is delivered to each class. The summarization of this algorithm leads to an understanding that, brown colors denotes the surface scattering classes, red colors for double-bounce scattering classes, green colors for volume scattering classes, and blue colors for helix scattering classes.

Although this method is aimed for non-reflection case, it automatically includes the reflection symmetry condition, therefore in can be used as a general case. It also preserves the scattering characteristics by taking the mixed scattering category into account therefore proving to be a better algorithm.

### Interferometry

Rather than discarding the phase data, information can be extracted from it. If two observations of the same terrain from very similar positions are available, aperture synthesis can be performed to provide the resolution performance which would be given by a radar system with dimensions equal to the separation of the two measurements. This technique is called interferometric SAR or InSAR.

If the two samples are obtained simultaneously (perhaps by placing two antennas on the same aircraft, some distance apart), then any phase difference will contain information about the angle from which the radar echo returned. Combining this with the distance information, one can determine the position in three dimensions of the image pixel. In other words, one can extract terrain altitude as well as radar reflectivity, producing a digital elevation model (DEM) with a single airplane pass. One aircraft application at the Canada Centre for Remote Sensing produced digital elevation maps with a resolution of 5 m and altitude errors also about 5 m. Interferometry was used to map many regions of the Earth's surface with unprecedented accuracy using data from the Shuttle Radar Topography Mission.

If the two samples are separated in time, perhaps from two flights over the same terrain, then there are two possible sources of phase shift. The first is terrain altitude, as discussed above. The second is terrain motion: if the terrain has shifted between observations, it will return a different phase. The amount of shift required to cause a significant phase difference is on the order of the wavelength used. This means that if the terrain shifts by centimeters, it can be seen in the resulting image (a digital elevation map must be available to separate the two kinds of phase difference; a third pass may be necessary to produce one).

This second method offers a powerful tool in geology and geography. Glacier flow can be mapped with two passes. Maps showing the land deformation after a minor earthquake or after a volcanic eruption (showing the shrinkage of the whole volcano by several centimeters) have been published.

#### Differential interferometry

Differential interferometry (D-InSAR) requires taking at least two images with addition of a DEM. The DEM can be either produced by GPS measurements or could be generated by interferometry as long as the time between acquisition of the image pairs is short, which guarantees minimal distortion of the image of the target surface. In principle, 3 images of the ground area with similar image acquisition geometry is often adequate for D-InSar. The principle for detecting ground movement is quite simple. One interferogram is created from the first two images; this is also called the reference interferogram or topographical interferogram. A second interferogram is created that captures topography + distortion. Subtracting the latter from the reference interferogram can reveal differential fringes, indicating movement. The described 3 image D-InSAR generation technique is called 3-pass or double-difference method.

Differential fringes which remain as fringes in the differential interferogram are a result of SAR range changes of any displaced point on the ground from one interferogram to the next. In the differential interferogram, each fringe is directly proportional to the SAR wavelength, which is about 5.6 cm for ERS and RADARSAT single phase cycle. Surface displacement away from the satellite look direction causes an increase in path (translating to phase) difference. Since the signal travels from the SAR antenna to the target and back again, the measured displacement is twice the unit of wavelength. This means in differential interferometry one fringe cycle −π to +π or one wavelength corresponds to a displacement relative to SAR antenna of only half wavelength (2.8 cm). There are various publications on measuring subsidence movement, slope stability analysis, landslide, glacier movement, etc. tooling D-InSAR. Further advancement to this technique whereby differential interferometry from satellite SAR ascending pass and descending pass can be used to estimate 3-D ground movement. Research in this area has shown accurate measurements of 3-D ground movement with accuracies comparable to GPS based measurements can be achieved.

#### Tomo-SAR

SAR Tomography is a subfield of a concept named as multi-baseline interferometry. It has been developed to give a 3D exposure to the imaging, which uses the beam formation concept. It can be used when the use demands a focused phase concern between the magnitude and the phase components of the SAR data, during information retrieval. One of the major advantages of Tomo-SAR is that it can separate out the parameters which get scattered, irrespective of how different their motions are. On using Tomo-SAR with differential interferometry, a new combination named "differential tomography" (Diff-Tomo) is developed.

Tomo-SAR has an application based on radar imaging, which is the depiction of Ice Volume and Forest Temporal Coherence (**Temporal coherence** describes the correlation between waves observed at different moments in time).

### Ultra-wideband SAR

Conventional radar systems emit bursts of radio energy with a fairly narrow range of frequencies. A narrow-band channel, by definition, does not allow rapid changes in modulation. Since it is the change in a received signal that reveals the time of arrival of the signal (obviously an unchanging signal would reveal nothing about "when" it reflected from the target), a signal with only a slow change in modulation cannot reveal the distance to the target as well as a signal with a quick change in modulation.

Ultra-wideband (UWB) refers to any radio transmission that uses a very large bandwidth – which is the same as saying it uses very rapid changes in modulation. Although there is no set bandwidth value that qualifies a signal as "UWB", systems using bandwidths greater than a sizable portion of the center frequency (typically about ten percent, or so) are most often called "UWB" systems. A typical UWB system might use a bandwidth of one-third to one-half of its center frequency. For example, some systems use a bandwidth of about 1 GHz centered around 3 GHz.

The two most common methods to increase signal bandwidth used in UWB radar, including SAR, are very short pulses and high-bandwidth chirping. A general description of chirping appears elsewhere in this article. The bandwidth of a chirped system can be as narrow or as wide as the designers desire. Pulse-based UWB systems, being the more common method associated with the term "UWB radar", are described here.

A pulse-based radar system transmits very short pulses of electromagnetic energy, typically only a few waves or less. A very short pulse is, of course, a very rapidly changing signal, and thus occupies a very wide bandwidth. This allows far more accurate measurement of distance, and thus resolution.

The main disadvantage of pulse-based UWB SAR is that the transmitting and receiving front-end electronics are difficult to design for high-power applications. Specifically, the transmit duty cycle is so exceptionally low and pulse time so exceptionally short, that the electronics must be capable of extremely high instantaneous power to rival the average power of conventional radars. (Although it is true that UWB provides a notable gain in channel capacity over a narrow band signal because of the relationship of bandwidth in the Shannon–Hartley theorem and because the low receive duty cycle receives less noise, increasing the signal-to-noise ratio, there is still a notable disparity in link budget because conventional radar might be several orders of magnitude more powerful than a typical pulse-based radar.) So pulse-based UWB SAR is typically used in applications requiring average power levels in the microwatt or milliwatt range, and thus is used for scanning smaller, nearer target areas (several tens of meters), or in cases where lengthy integration (over a span of minutes) of the received signal is possible. However, this limitation is solved in chirped UWB radar systems.

The principal advantages of UWB radar are better resolution (a few millimeters using commercial off-the-shelf electronics) and more spectral information of target reflectivity.

### Doppler-beam sharpening

Doppler Beam Sharpening commonly refers to the method of processing unfocused real-beam phase history to achieve better resolution than could be achieved by processing the real beam without it. Because the real aperture of the radar antenna is so small (compared to the wavelength in use), the radar energy spreads over a wide area (usually many degrees wide in a direction orthogonal (at right angles) to the direction of the platform (aircraft)). Doppler-beam sharpening takes advantage of the motion of the platform in that targets ahead of the platform return a Doppler upshifted signal (slightly higher in frequency) and targets behind the platform return a Doppler downshifted signal (slightly lower in frequency).

The amount of shift varies with the angle forward or backward from the ortho-normal direction. By knowing the speed of the platform, target signal return is placed in a specific angle "bin" that changes over time. Signals are integrated over time and thus the radar "beam" is synthetically reduced to a much smaller aperture – or more accurately (and based on the ability to distinguish smaller Doppler shifts) the system can have hundreds of very "tight" beams concurrently. This technique dramatically improves angular resolution; however, it is far more difficult to take advantage of this technique for range resolution. (See pulse-doppler radar).

### Chirped (pulse-compressed) radars

A common technique for many radar systems (usually also found in SAR systems) is to "chirp" the signal. In a "chirped" radar, the pulse is allowed to be much longer. A longer pulse allows more energy to be emitted, and hence received, but usually hinders range resolution. But in a chirped radar, this longer pulse also has a frequency shift during the pulse (hence the chirp or frequency shift). When the "chirped" signal is returned, it must be correlated with the sent pulse. Classically, in analog systems, it is passed to a dispersive delay line (often a surface acoustic wave device) that has the property of varying velocity of propagation based on frequency. This technique "compresses" the pulse in time – thus having the effect of a much shorter pulse (improved range resolution) while having the benefit of longer pulse length (much more signal energy returned). Newer systems use digital pulse correlation to find the pulse return in the signal.
