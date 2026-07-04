---
title: "Thermodynamic modelling"
source: https://en.wikipedia.org/wiki/Thermodynamic_modelling
domain: thermodynamic-modelling
license: CC-BY-SA-4.0
tags: thermodynamic modelling
fetched: 2026-07-04
---

# Thermodynamic modelling

**Thermodynamic modelling** is a set of different strategies that are used by engineers and scientists to develop models capable of evaluating different thermodynamic properties of a system. At each thermodynamic equilibrium state of a system, the thermodynamic properties of the system are specified. Generally, thermodynamic models are mathematical relations that relate different state properties to each other in order to eliminate the need of measuring all the properties of the system in different states.

The easiest thermodynamic models, also known as equations of state, can come from simple correlations that relate different thermodynamic properties using a linear or second-order polynomial function of temperature and pressures. They are generally fitted using experimental data available for that specific properties. This approach can result in limited predictability of the correlation and as a consequence it can be adopted only in a limited operating range.

By contrast, more advanced thermodynamic models are built in a way that can predict the thermodynamic behavior of the system, even if the functional form of the model is not based on the real thermodynamic behaviour of the material. These types of models contain different parameters that are gradually developed for each specific model in order to enhance the accuracy of the evaluating thermodynamic properties.

## Cubic model development

Cubic equations of state refer to the group of thermodynamic models that can evaluate the specific volume of gas and liquid systems as a function of pressure and temperature. To develop a cubic model, first, it is essential to select a cubic functional form. The most famous functional forms of this category are Redlich-Kwong, Soave-Redlich-Kwong and Peng-Robinson. Although their initial form is empirically suggested, they are categorised as semi-empirical models as their parameters can be adjusted to fit the real experimental measurement data of the target system.

### Pure component modelling

In case the development of a cubic model for a pure component is targeted, the purpose would be to replicate the specific volume behaviour of the fluid in terms of temperature and pressure. At a given temperature, any cubic functional form results in two separate roots which makes us capable of modelling the behaviour of both vapour and liquid phases within a single model. Finding the roots of the cubic function will be done by simulating the vapour-liquid equilibrium condition of the pure component where the fugacity coefficients of the two phases are equal to each other.

So, in this case, the main aim can be limited to deriving fugacity coefficients of vapour and liquid phases from the cubic model and refining the adjustable parameters of the model such that they will become equal to each other at different equilibrium pairs of temperature and pressure. As the equilibrium pressure and temperature are related together in the case of a pure component system, the functional form of cubic models are able to evaluate the specific volume of the system in the wide range of temperature and pressure domain.

### Multi-component modelling

Cubic model development for mixtures of more than one component is different as, according to the Gibbs phase rule, at each temperature level of a multi-component system, equilibrium states can exist at multiple pressure levels. Because of that, development of the thermodynamic model should be performed following different steps:

1. *Selection of the cubic model:* The initial step is the selection of a cubic functional form. Essentially, there exists no specific rule for this step. It can be done based on common practices of the cubic models already developed for the pure components existing in the mixture.
2. *Single phase:* Although a cubic model for a pure component is capable of predicting the specific volume of the system at both vapour and liquid phases, this is not the case for multi-component systems. Currently cubic models are used for the prediction of specific volume only in the vapour phase, while the liquid phase is modelled with more complex models based on the excess Gibbs energy, such as UNIFAC, UNIQUAQ, etc.
3. *Vapour and liquid phases:* Cubic models can be expanded to model multi-component systems at both vapour and liquid phases by integrating a proper mixing rule in their structural function.

### Mixing rules

Mixing rules refer to different approaches that can be used to modify the cubic model in the case of multi-component mixtures. The simplest mixing rule is proposed by van der Waals and is called the *van der Waals one fluid (vdW1f)* mixing rule. As it can be understood from its name, this mixing rule is only used in case of modelling of a single phase (vapor phase). As a first step, to combine the model parameters for each binary combination of the mixture, the following equations are suggested:

$a_{ij}={\sqrt {a_{ii}a_{jj}}}(1-k_{ij})$

$b_{ij}={\frac {b_{ii}+b_{jj}}{2}}(1-l_{ij})$

where $a_{ij}$ and $b_{ij}$ are the parameters of the main target cubic model that was previously chosen. Then, all the possible binary combinations together with the concentration of each constituent in the mixture are used to define the final parameters for the mixture model as below:

$a_{mix}=\sum _{i}\sum _{j}y_{i}y_{j}a_{ij}$

$b_{mix}=\sum _{i}y_{i}b_{i}$

In the case of using this mixing rule, except the two adjustable binary interaction parameters (BIPs) for each combination ( $k_{ij}$ and $l_{ij}$ ), other parameters are specified based on the pure component parameters and the concentration of different constituents in the mixture. So, the model developed in this case is limited to adjusting these two parameters such that the fugacity coefficients at different phases will be equal to each other at a certain temperature and pressure level. To overcome the limitation of the sole single-phase behaviour prediction in the case of using this mixing rule, other advanced mixing rules are developed. To predict the thermodynamic behaviour of the multi-component system in different phases, it is essential to build the energy function as a fundamental property of the system. Although this is mainly the case for the fundamental models, advanced mixing rules such as Huran-Vidal mixing rule and Wong-Sandler mixing rule are developed to adjust the parameters of the cubic models to contain these fundamental properties. This is usually done by building a mathematical structure capable of calculating the excess Gibbs energy of the system. It is generally built by two widely used approaches, namely UNIFAC and Non Random Two Liquid (NRTL) method. The choice of the proper mixing rule to be implemented in the target system can be done based on the inherent properties of the target system such as the polarity of different components, the reactivity of system's constituents with respect to each other, etc.

## Fundamental model development

Fundamental models refer to a family of thermodynamic models that propose a mathematical form for one of the fundamental thermodynamic properties of the system, such as Gibbs free energy or Helmholtz free energy. The core idea behind this type of thermodynamic models is that, by constructing the fundamental property, it is possible to take advantage of thermodynamic relations that express different thermodynamic properties as the first or second-order derivatives of fundamental properties, with respect to pressure, temperature or density.

### Helmholtz free energy models

For the development of Helmholtz free energy models, the idea is to associate different parameters that resemble different inter-molecular forces between system species. As a result, these models are referred to as multi-parameter models. Steps to develop a Helmholtz free energy model can be summarized as:

1. *Helmholtz free energy of pure components:* Like all the thermodynamic models, the first step is to build the Helmholtz free energy of pure constituents of a system. For well-known components, such as carbon dioxide and nitrogen, such functions are already established and reported in the literature. These can be used as the starting point to establish such models for multi-component systems.
2. *Helmholtz free energy of binary mixtures:* Helmholtz free energy of a multi-component system can be obtained from the weighted sum of the Helmholtz free energy of each binary combination of the system constituents. The binary Helmholtz free energy contains different terms that are taking into account various intermolecular forces that can exist based on the inherent of the two target components. Such models are developed for natural gas components through GERG-2008 thermodynamic model and EOS-CGfor the humid and combustion gas-like mixtures. The main advantages of these models are their generality, which makes them applicable to a wide range of pressure, temperature, and the whole concentration range of involved constituents.

## Thermodynamic models criterions

A thermodynamic model predicts different properties with a certain level of accuracy. In fact, based on the functional form of the thermodynamic model and the real behaviour of the system some properties can be predicted with high accuracy level, while the other ones could not be predicted accurately enough to comply with different industrial needs. In this regard several criterions should be taken into account for the proper choice of thermodynamic model to be practical based on the targeted application.

### Applicability

Although thermodynamic models are generally developed to predict thermodynamic properties in a wide range of temperatures and pressures, due to the lack of experimental data for different compounds in the full operational range, model accuracy varies by moving towards wider temperature and pressure ranges. When a model is targeted to be used in a specific application, the initial step is to identify the temperature and pressure at what the model is intended to be implemented. If the model is able to perform in the target operating window, the second step is to investigate whether the model can cover all the system constituents within the concentration ranges of interest or not. Fundamental models answered this ambiguity by covering the whole concentration range of the compounds that they involved. However, this is not the case for ad-hoc cubic model developments which may be considered in the specific range of concentration based on the application.

### Robustness

Thermodynamic models should be robust and reliable, providing consistent results across different conditions and applications. They should be able to handle non-ideal behaviour, phase transitions, and complex interactions without significant loss of accuracy. Although some models are capable of taking into account the possible reactions between the system constituents, this is not the case for other simpler models that can only predict the behaviour of the system only in a specific phase. So, it is essential to identify the typical behaviour of the fluid in the target application to select and develop a proper model. However, in most engineering applications, developing a model that would be able to predict the thermodynamic properties of the system in different phases, critical regions and taking into account the possible reaction between systems is a necessity.

### Accuracy

Based on the foundation that each thermodynamic model is built, the accuracy could vary not only for a specific property evaluation from different models but also for predicting different properties within a specific model itself. Cubic models are developed based on the phase equilibrium and as a result, they can predict the phase equilibrium of pure and multi-component systems within an acceptable accuracy level in case the model is fine-tuned to the experimental data of interest. However, this family of models is not accurate enough in predicting density and specific heat capacity as the two main thermodynamic properties that are of importance in most industrial applications. In the recent case, some corrections are suggested to enhance the accuracy of the cubic models for different properties, such as Peneloux translation for density prediction.

On the other hand, models that are developed based on fundamental properties such as Gibbs free energy or Helmholtz free energy, are generally capable of predicting a wider range of properties. As these models have a multiple number of adjustable parameters that fitted to different of experimental properties data, it makes them a pioneer when it comes to accuracy.

### Computational speed

The model should be computationally efficient, especially for complex systems and large-scale simulations. The model's equations and algorithms should be designed to minimize computational time. This is especially important in cases where transient processes are targeted that thermodynamic properties change significantly over the transient time domain and computationally demanding models cannot satisfy industrial needs.

### Availability

In certain applications, it may be important to consider the acceptance and implementation of a specific thermodynamic model within the industry. Industrial standards and guidelines can provide insights into the preferred models for specific processes. However, not all thermodynamic models are widely available in commercial software packages. This is especially the case for more complex fundamental models that despite their robustness, they are not still well-accepted by industry to their limited availability.
