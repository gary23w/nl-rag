---
title: "Camera resectioning"
source: https://en.wikipedia.org/wiki/Camera_resectioning
domain: photogrammetry-3d
license: CC-BY-SA-4.0
tags: photogrammetry 3d, structure from motion, bundle adjustment reconstruction, epipolar geometry photogrammetry
fetched: 2026-07-02
---

# Camera resectioning

**Camera resectioning** is the process of estimating the parameters of a pinhole camera model approximating the camera that produced a given photograph or video; it determines which incoming light ray is associated with each pixel on the resulting image. Basically, the process determines the pose of the pinhole camera.

Usually, the camera parameters are represented in a 3 × 4 projection matrix called the *camera matrix*. The **extrinsic parameters** define the camera *pose* (position and orientation) while the **intrinsic parameters** specify the camera image format (focal length, pixel size, and image origin).

This process is often called **geometric camera calibration** or simply **camera calibration**, although that term may also refer to photometric camera calibration or be restricted for the estimation of the intrinsic parameters only. **Exterior orientation** and **interior orientation** refer to the determination of only the extrinsic and intrinsic parameters, respectively.

The classic camera calibration requires special objects in the scene, which is not required in *camera auto-calibration*. Camera resectioning is often used in the application of stereo vision where the camera projection matrices of two cameras are used to calculate the 3D world coordinates of a point viewed by both cameras.

## Formulation

The camera projection matrix is derived from the intrinsic and extrinsic parameters of the camera, and is often represented by the series of transformations; e.g., a matrix of camera intrinsic parameters, a 3 × 3 rotation matrix, and a translation vector. The camera projection matrix can be used to associate points in a camera's image space with locations in 3D world space.

### Homogeneous coordinates

In this context, we use $[u\ v\ 1]^{T}$ to represent a 2D point position in *pixel* coordinates and $[x_{w}\ y_{w}\ z_{w}\ 1]^{T}$ is used to represent a 3D point position in *world* coordinates. In both cases, they are represented in homogeneous coordinates (i.e. they have an additional last component, which is initially, by convention, a 1), which is the most common notation in robotics and rigid body transforms.

### Projection

Referring to the pinhole camera model, a camera matrix M is used to denote a projective mapping from *world* coordinates to *pixel* coordinates.

${\begin{bmatrix}wu\\wv\\w\end{bmatrix}}=K\,{\begin{bmatrix}R&T\end{bmatrix}}{\begin{bmatrix}x_{w}\\y_{w}\\z_{w}\\1\end{bmatrix}}=M{\begin{bmatrix}x_{w}\\y_{w}\\z_{w}\\1\end{bmatrix}}$

where $M=K\,{\begin{bmatrix}R&T\end{bmatrix}}$ . $u,v$ by convention are the x and y coordinates of the pixel in the camera, K is the intrinsic matrix as described below, and $R\,T$ form the extrinsic matrix as described below. $x_{w},y_{w},z_{w}$ are the coordinates of the source of the light ray which hits the camera sensor in world coordinates, relative to the origin of the world. By dividing the matrix product by w , the theoretical value for the pixel coordinates can be found.

### Intrinsic parameters

$K={\begin{bmatrix}\alpha _{x}&\gamma &u_{0}\\0&\alpha _{y}&v_{0}\\0&0&1\end{bmatrix}}$

The K contains 5 intrinsic parameters of the specific camera model. These parameters encompass focal length, image sensor format, and camera principal point. The parameters $\alpha _{x}=f\cdot m_{x}$ and $\alpha _{y}=f\cdot m_{y}$ represent focal length in terms of pixels, where $m_{x}$ and $m_{y}$ are the inverses of the width and height of a pixel on the projection plane and f is the focal length in terms of distance. $\gamma$ represents the skew coefficient between the x and the y axis, and is often 0. $u_{0}$ and $v_{0}$ represent the principal point, which would be ideally in the center of the image.

Nonlinear intrinsic parameters such as lens distortion are also important although they cannot be included in the linear camera model described by the intrinsic parameter matrix. Many modern camera calibration algorithms estimate these intrinsic parameters as well in the form of non-linear optimisation techniques. This is done in the form of optimising the camera and distortion parameters in the form of what is generally known as bundle adjustment.

### Extrinsic parameters

${}{\begin{bmatrix}R_{3\times 3}&T_{3\times 1}\\0_{1\times 3}&1\end{bmatrix}}_{4\times 4}$

$R,T$ are the **extrinsic parameters** which denote the coordinate system transformations from 3D world coordinates to 3D camera coordinates. Equivalently, the extrinsic parameters define the position of the camera center and the camera's heading in world coordinates. T is the position of the origin of the world coordinate system expressed in coordinates of the camera-centered coordinate system. T is often mistakenly considered the position of the camera. The position, C , of the camera expressed in world coordinates is $C=-R^{-1}T=-R^{T}T$ (since R is a rotation matrix). This can be verified by checking that the point $[-R^{-1}T,1]$ is transformed to $[0,0,0,1]^{T}$ , which is what is expected (since the camera's location is, in the camera's coordinates, the origin).

Camera calibration is often used as an early stage in computer vision.

When a camera is used, light from the environment is focused on an image plane and captured. This process reduces the dimensions of the data taken in by the camera from three to two (light from a 3D scene is stored on a 2D image). Each pixel on the image plane therefore corresponds to a shaft of light from the original scene.

## Algorithms

There are many different approaches to calculate the intrinsic and extrinsic parameters for a specific camera setup. The most common ones are:

1. Direct linear transformation (DLT) method
2. Zhang's method
3. Tsai's method
4. Selby's method (for X-ray cameras)

### Zhang's method

Zhang's method is a camera calibration method that uses traditional calibration techniques (known calibration points) and self-calibration techniques (correspondence between the calibration points when they are in different positions). To perform a full calibration by the Zhang method, at least three different images of the calibration target/gauge are required, either by moving the gauge or the camera itself. If some of the intrinsic parameters are given as data (orthogonality of the image or optical center coordinates), the number of images required can be reduced to two.

In a first step, an approximation of the estimated projection matrix H between the calibration target and the image plane is determined using DLT method. Subsequently, self-calibration techniques are applied to obtain the image of the absolute conic matrix. The main contribution of Zhang's method is how to, given n poses of the calibration target, extract a constrained intrinsic matrix K , along with n instances of R and T calibration parameters.

#### Derivation

Assume we have a homography ${\textbf {H}}$ that maps points $x_{\pi }$ on a "probe plane" $\pi$ to points x on the image.

The circular points $I,J={\begin{bmatrix}1&\pm j&0\end{bmatrix}}^{\mathrm {T} }$ lie on both our probe plane $\pi$ and on the absolute conic $\Omega _{\infty }$ . Lying on $\Omega _{\infty }$ of course means they are also projected onto the *image* of the absolute conic (IAC) $\omega$ , thus $x_{1}^{T}\omega x_{1}=0$ and $x_{2}^{T}\omega x_{2}=0$ . The circular points project as

${\begin{aligned}x_{1}&={\textbf {H}}I={\begin{bmatrix}h_{1}&h_{2}&h_{3}\end{bmatrix}}{\begin{bmatrix}1\\j\\0\end{bmatrix}}=h_{1}+jh_{2}\\x_{2}&={\textbf {H}}J={\begin{bmatrix}h_{1}&h_{2}&h_{3}\end{bmatrix}}{\begin{bmatrix}1\\-j\\0\end{bmatrix}}=h_{1}-jh_{2}\end{aligned}}$

.

We can actually ignore $x_{2}$ while substituting our new expression for $x_{1}$ as follows:

${\begin{aligned}x_{1}^{T}\omega x_{1}&=\left(h_{1}+jh_{2}\right)^{T}\omega \left(h_{1}+jh_{2}\right)\\&=\left(h_{1}^{T}+jh_{2}^{T}\right)\omega \left(h_{1}+jh_{2}\right)\\&=h_{1}^{T}\omega h_{1}+j\left(h_{2}^{T}\omega h_{2}\right)\\&=0\end{aligned}}$

### Tsai's algorithm

Tsai's algorithm, a significant method in camera calibration, involves several detailed steps for accurately determining a camera's orientation and position in 3D space. The procedure, while technical, can be generally broken down into three main stages:

#### Initial Calibration

The process begins with the **initial calibration** stage, where a series of images are captured by the camera. These images, often featuring a known calibration pattern like a checkerboard, are used to estimate intrinsic camera parameters such as focal length and optical center. In some applications, variants of the chessboard target are used which are robust to partial occlusions. Such targets like the ChArUco and PuzzleBoard targets simplify the measurement of distortions in the corners of the camera sensor.

#### Pose Estimation

Following initial calibration, the algorithm undertakes **pose estimation**. This involves calculating the camera's position and orientation relative to a known object in the scene. The process typically requires identifying specific points in the calibration pattern and solving for the camera's rotation and translation vectors.

#### Refinement of Parameters

The final phase is the **refinement of parameters**. In this stage, the algorithm refines the lens distortion coefficients, addressing radial and tangential distortions. Further optimization of internal and external camera parameters is performed to enhance the calibration accuracy.

This structured approach has positioned Tsai's Algorithm as a pivotal technique in both academic research and practical applications within robotics and industrial metrology.

### Selby's method (for X-ray cameras)

Selby's camera calibration method addresses the auto-calibration of X-ray camera systems. X-ray camera systems, consisting of the X-ray generating tube and a solid state detector can be modelled as pinhole camera systems, comprising 9 intrinsic and extrinsic camera parameters. Intensity based registration based on an arbitrary X-ray image and a reference model (as a tomographic dataset) can then be used to determine the relative camera parameters without the need of a special calibration body or any ground-truth data.
