---
title: "Satellite navigation solution"
source: https://en.wikipedia.org/wiki/GNSS_positioning
domain: gps-positioning
license: CC-BY-SA-4.0
tags: gps positioning, satellite navigation, gnss positioning, nmea sentence
fetched: 2026-07-02
---

# Satellite navigation solution

(Redirected from

GNSS positioning

)

Satellite navigation solution for the receiver's position (geopositioning) involves an algorithm. In essence, a GNSS receiver measures the transmitting time of GNSS signals emitted from four or more GNSS satellites (giving the pseudorange) and these measurements are used to obtain its position (i.e., spatial coordinates) and reception time.

The following are expressed in inertial-frame coordinates.

## The solution illustrated

- (Essentially, the solution shown in orange, ( r ^ rec , t ^ rec ) {\textstyle ({\hat {\boldsymbol {r}}}_{\text{rec}},\,{\hat {t}}_{\text{rec}})} , is the intersection of light cones.)Essentially, the solution shown in orange, ${\textstyle ({\hat {\boldsymbol {r}}}_{\text{rec}},\,{\hat {t}}_{\text{rec}})}$ , is the intersection of light cones.
- (The posterior distribution of the solution is derived from the product of the distribution of propagating spherical surfaces. (See animation.))The posterior distribution of the solution is derived from the product of the distribution of propagating spherical surfaces. (See animation.)

## Calculation steps

1. A global-navigation-satellite-system (GNSS) receiver measures the apparent transmitting time, ${\tilde {t}}_{i}$ , or "phase", of GNSS signals emitted from four or more GNSS satellites ( $i=1,\,2,\,3,\,4,\,..,\,n$ ), simultaneously.
2. GNSS satellites broadcast the messages of satellites' ephemeris, ${\boldsymbol {r}}_{i}(t)$ , and intrinsic clock bias (i.e., clock advance), $\delta t_{{\text{clock,sv}},i}(t)$ as the functions of (atomic) standard time, e.g., GPST.
3. The transmitting time of GNSS satellite signals, $t_{i}$ , is thus derived from the non-closed-form equations ${\tilde {t}}_{i}=t_{i}+\delta t_{{\text{clock}},i}(t_{i})$ and $\delta t_{{\text{clock}},i}(t_{i})=\delta t_{{\text{clock,sv}},i}(t_{i})+\delta t_{{\text{orbit-relativ}},\,i}({\boldsymbol {r}}_{i},\,{\dot {\boldsymbol {r}}}_{i})$ , where $\delta t_{{\text{orbit-relativ}},i}({\boldsymbol {r}}_{i},\,{\dot {\boldsymbol {r}}}_{i})$ is the relativistic clock bias, periodically risen from the satellite's orbital eccentricity and Earth's gravity field. The satellite's position and velocity are determined by $t_{i}$ as follows: ${\boldsymbol {r}}_{i}={\boldsymbol {r}}_{i}(t_{i})$ and ${\dot {\boldsymbol {r}}}_{i}={\dot {\boldsymbol {r}}}_{i}(t_{i})$ . The satellite's position is derived from ${\boldsymbol {r}}_{i}={\boldsymbol {r}}_{i}(t_{i})$ .
4. In the field of GNSS, "geometric range", $r({\boldsymbol {r}}_{A},\,{\boldsymbol {r}}_{B})$ , is defined as straight range, or 3-dimensional distance, from ${\boldsymbol {r}}_{A}$ to ${\boldsymbol {r}}_{B}$ in inertial frame (e.g., ECI one), not in rotating frame.
5. The receiver's position, ${\boldsymbol {r}}_{\text{rec}}$ , and reception time, $t_{\text{rec}}$ , satisfy the light-cone equation of $r({\boldsymbol {r}}_{i},\,{\boldsymbol {r}}_{\text{rec}})/c+(t_{i}-t_{\text{rec}})=0$ in inertial frame, where c is the speed of light. The signal time of flight from satellite to receiver is $-(t_{i}-t_{\text{rec}})$ .
6. The above is extended to the satellite-navigation positioning equation, $r({\boldsymbol {r}}_{i},\,{\boldsymbol {r}}_{\text{rec}})/c+(t_{i}-t_{\text{rec}})+\delta t_{{\text{atmos}},i}-\delta t_{{\text{meas-err}},i}=0$ , where $\delta t_{{\text{atmos}},i}$ is atmospheric delay (= ionospheric delay + tropospheric delay) along signal path and $\delta t_{{\text{meas-err}},i}$ is the measurement error.
7. The Gauss–Newton method can be used to solve the nonlinear least-squares problem for the solution: $({\hat {\boldsymbol {r}}}_{\text{rec}},\,{\hat {t}}_{\text{rec}})=\arg \min \phi ({\boldsymbol {r}}_{\text{rec}},\,t_{\text{rec}})$ , where $\phi ({\boldsymbol {r}}_{\text{rec}},\,t_{\text{rec}})=\sum _{i=1}^{n}(\delta t_{{\text{meas-err}},i}/\sigma _{\delta t_{{\text{meas-err}},i}})^{2}$ . Note that $\delta t_{{\text{meas-err}},i}$ should be regarded as a function of ${\boldsymbol {r}}_{\text{rec}}$ and $t_{\text{rec}}$ .
8. The posterior distribution of ${\boldsymbol {r}}_{\text{rec}}$ and $t_{\text{rec}}$ is proportional to $\exp(-{\frac {1}{2}}\phi ({\boldsymbol {r}}_{\text{rec}},\,t_{\text{rec}}))$ , whose mode is $({\hat {\boldsymbol {r}}}_{\text{rec}},\,{\hat {t}}_{\text{rec}})$ . Their inference is formalized as maximum a posteriori estimation.
9. The posterior distribution of ${\boldsymbol {r}}_{\text{rec}}$ is proportional to $\int _{-\infty }^{\infty }\exp(-{\frac {1}{2}}\phi ({\boldsymbol {r}}_{\text{rec}},\,t_{\text{rec}}))\,dt_{\text{rec}}$ .

### Notes for above

- In the field of GNSS, ${\textstyle {\tilde {r}}_{i}=-c({\tilde {t}}_{i}-{\tilde {t}}_{\text{rec}})}$ is called pseudorange, where ${\textstyle {\tilde {t}}_{\text{rec}}}$ is a provisional reception time of the receiver. ${\textstyle \delta t_{\text{clock,rec}}={\tilde {t}}_{\text{rec}}-t_{\text{rec}}}$ is called receiver's clock bias (i.e., clock advance).
- Standard GNSS receivers output ${\textstyle {\tilde {r}}_{i}}$ and ${\textstyle {\tilde {t}}_{\text{rec}}}$ per an observation epoch.
- The temporal variation in the relativistic clock bias of satellite is linear if its orbit is circular (and thus its velocity is uniform in inertial frame).
- The signal time of flight from satellite to receiver is expressed as ${\textstyle -(t_{i}-t_{\text{rec}})={\tilde {r}}_{i}/c+\delta t_{{\text{clock}},i}-\delta t_{\text{clock,rec}}}$ , whose right side is round-off-error resistive during calculation.
- The geometric range is calculated as ${\textstyle r({\boldsymbol {r}}_{i},\,{\boldsymbol {r}}_{\text{rec}})=|\Omega _{\text{E}}(t_{i}-t_{\text{rec}}){\boldsymbol {r}}_{i,{\text{ECEF}}}-{\boldsymbol {r}}_{\text{rec,ECEF}}|}$ , where the Earth-centred, Earth-fixed (ECEF) rotating frame (e.g., WGS84 or ITRF) is used in the right side and ${\textstyle \Omega _{\text{E}}}$ is the Earth rotating matrix with the argument of the signal transit time. The matrix can be factorized as ${\textstyle \Omega _{\text{E}}(t_{i}-t_{\text{rec}})=\Omega _{\text{E}}(\delta t_{\text{clock,rec}})\Omega _{\text{E}}(-{\tilde {r}}_{i}/c-\delta t_{{\text{clock}},i})}$ .
- The line-of-sight unit vector of satellite observed at ${\textstyle {\boldsymbol {r}}_{\text{rec,ECEF}}}$ is described as: ${\textstyle {\boldsymbol {e}}_{i,{\text{rec,ECEF}}}=-{\frac {\partial r({\boldsymbol {r}}_{i},\,{\boldsymbol {r}}_{\text{rec}})}{\partial {\boldsymbol {r}}_{\text{rec,ECEF}}}}}$ .
- The satellite-navigation positioning equation may be expressed by using the variables ${\textstyle {\boldsymbol {r}}_{\text{rec,ECEF}}}$ and ${\textstyle \delta t_{\text{clock,rec}}}$ .
- The nonlinearity of the vertical dependency of tropospheric delay degrades the convergence efficiency in the Gauss–Newton iterations in step 7.
- The above notation is different from that in the Wikipedia articles, 'Position calculation introduction' and 'Position calculation advanced', of Global Positioning System (GPS).

## The GPS case

- For Global Positioning System (GPS), the non-closed-form equations in step 3 result in ${\begin{cases}\Delta t_{i}(t_{i},\,E_{i})\triangleq t_{i}+\delta t_{{\text{clock}},i}(t_{i},\,E_{i})-{\tilde {t}}_{i}=0,\\\Delta M_{i}(t_{i},\,E_{i})\triangleq M_{i}(t_{i})-(E_{i}-e_{i}\sin E_{i})=0,\end{cases}}$ in which ${\textstyle E_{i}}$ is the orbital eccentric anomaly of satellite i , ${\textstyle M_{i}}$ is the mean anomaly, ${\textstyle e_{i}}$ is the eccentricity, and ${\textstyle \delta t_{{\text{clock}},i}(t_{i},\,E_{i})=\delta t_{{\text{clock,sv}},i}(t_{i})+\delta t_{{\text{orbit-relativ}},i}(E_{i})}$ .
- The above can be solved by using the bivariate Newton–Raphson method on ${\textstyle t_{i}}$ and ${\textstyle E_{i}}$ . Two times of iteration will be necessary and sufficient in most cases. Its iterative update will be described by using the approximated inverse of Jacobian matrix as follows: ${\begin{pmatrix}t_{i}\\E_{i}\\\end{pmatrix}}\leftarrow {\begin{pmatrix}t_{i}\\E_{i}\\\end{pmatrix}}-{\begin{pmatrix}1&0\\{\frac {{\dot {M}}_{i}(t_{i})}{1-e_{i}\cos E_{i}}}&-{\frac {1}{1-e_{i}\cos E_{i}}}\\\end{pmatrix}}{\begin{pmatrix}\Delta t_{i}\\\Delta M_{i}\\\end{pmatrix}}$
- Tropospheric delay should not be ignored, while the Global Positioning System (GPS) specification doesn't provide its detailed description.

## The GLONASS case

- The GLONASS ephemerides don't provide clock biases ${\textstyle \delta t_{{\text{clock,sv}},i}(t)}$ , but ${\textstyle \delta t_{{\text{clock}},i}(t)}$ .
