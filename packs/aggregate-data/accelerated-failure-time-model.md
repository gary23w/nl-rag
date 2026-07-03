---
title: "Accelerated failure time model"
source: https://en.wikipedia.org/wiki/Accelerated_failure_time_model
domain: aggregate-data
license: CC-BY-SA-4.0
tags: aggregate data
fetched: 2026-07-03
---

# Accelerated failure time model

In the statistical area of survival analysis, an **accelerated failure time model** (**AFT model**) is a parametric model that provides an alternative to the commonly used proportional hazards models. Whereas a proportional hazards model assumes that the effect of a covariate is to multiply the hazard by some constant, an AFT model assumes that the effect of a covariate is to accelerate or decelerate the life course of a disease by some constant. There is strong basic science evidence from *C. elegans* experiments by Stroustrup et al. indicating that AFT models are the correct model for biological survival processes.

## Model specification

In full generality, the accelerated failure time model can be specified as

$\lambda (t|\theta )=\theta \lambda _{0}(\theta t)$

where $\theta$ denotes the joint effect of covariates, typically $\theta =\exp(-[\beta _{1}X_{1}+\cdots +\beta _{p}X_{p}])$ . (Specifying the regression coefficients with a negative sign implies that high values of the covariates *increase* the survival time, but this is merely a sign convention; without a negative sign, they increase the hazard.)

This is satisfied if the probability density function of the event is taken to be $f(t|\theta )=\theta f_{0}(\theta t)$ ; it then follows for the survival function that $S(t|\theta )=S_{0}(\theta t)$ . From this it is easy to see that the moderated life time T is distributed such that $T\theta$ and the unmoderated life time $T_{0}$ have the same distribution. Consequently, $\log(T)$ can be written as

$\log(T)=-\log(\theta )+\log(T\theta ):=-\log(\theta )+\epsilon$

where the last term is distributed as $\log(T_{0})$ , i.e., independently of $\theta$ . This reduces the accelerated failure time model to regression analysis (typically a linear model) where $-\log(\theta )$ represents the fixed effects, and $\epsilon$ represents the noise. Different distributions of $\epsilon$ imply different distributions of $T_{0}$ , i.e., different baseline distributions of the survival time. Typically, in survival-analytic contexts, many of the observations are censored: we only know that $T_{i}>t_{i}$ , not $T_{i}=t_{i}$ . In fact, the former case represents survival, while the later case represents an event/death/censoring during the follow-up. These right-censored observations can pose technical challenges for estimating the model, if the distribution of $T_{0}$ is unusual.

The interpretation of $\theta$ in accelerated failure time models is straightforward: $\theta =2$ means that everything in the relevant life history of an individual happens twice as fast. For example, if the model concerns the development of a tumor, it means that all of the pre-stages progress twice as fast as for the unexposed individual, implying that the expected time until a clinical disease is 0.5 of the baseline time. However, this does not mean that the hazard function $\lambda (t|\theta )$ is always twice as high—that would be the proportional hazards model.

## Statistical issues

Unlike proportional hazards models, in which Cox's semi-parametric proportional hazards model is more widely used than parametric models, AFT models are predominantly fully parametric i.e. a probability distribution is specified for $\log(T_{0})$ . (Buckley and James proposed a semi-parametric AFT but its use is relatively uncommon in applied research; in a 1992 paper, Wei pointed out that the Buckley–James model has no theoretical justification and lacks robustness, and reviewed alternatives.) This can be a problem, if a degree of realistic detail is required for modelling the distribution of a baseline lifetime. Hence, technical developments in this direction would be highly desirable.

When a frailty term is incorporated in the survival model, the regression parameter estimates from AFT models are robust to omitted covariates, unlike proportional hazards models. They are also less affected by the choice of probability distribution for the frailty term.

The results of AFT models are easily interpreted. For example, the results of a clinical trial with mortality as the endpoint could be interpreted as a certain percentage increase in future life expectancy on the new treatment compared to the control. So a patient could be informed that he would be expected to live (say) 15% longer if he took the new treatment. Hazard ratios can prove harder to explain in layman's terms.

### Distributions used in AFT models

The log-logistic distribution provides the most commonly used AFT model. Unlike the Weibull distribution, it can exhibit a non-monotonic hazard function which increases at early times and decreases at later times. It is somewhat similar in shape to the log-normal distribution but it has heavier tails. The log-logistic cumulative distribution function has a simple closed form, which becomes important computationally when fitting data with censoring. For the censored observations one needs the survival function, which is the complement of the cumulative distribution function, i.e. one needs to be able to evaluate $S(t|\theta )=1-F(t|\theta )$ .

The Weibull distribution (including the exponential distribution as a special case) can be parameterised as either a proportional hazards model or an AFT model, and is the only family of distributions to have this property. The results of fitting a Weibull model can therefore be interpreted in either framework. However, the biological applicability of this model may be limited by the fact that the hazard function is monotonic, i.e. either decreasing or increasing.

Any distribution on a multiplicatively closed group, such as the positive real numbers, is suitable for an AFT model. Other distributions include the log-normal, gamma, hypertabastic, Gompertz distribution, and inverse Gaussian distributions, although they are less popular than the log-logistic, partly as their cumulative distribution functions do not have a closed form. Finally, the generalized gamma distribution is a three-parameter distribution that includes the Weibull, log-normal and gamma distributions as special cases.
