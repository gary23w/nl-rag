---
title: "Ehrenfest equations"
source: https://en.wikipedia.org/wiki/Ehrenfest_equations
domain: phase-transitions
license: CC-BY-SA-4.0
tags: phase transition, state of matter, latent heat, phase diagram
fetched: 2026-07-02
---

# Ehrenfest equations

**Ehrenfest equations** (named after Paul Ehrenfest) are equations which describe changes in specific heat capacity and derivatives of specific volume in second-order phase transitions. The Clausius–Clapeyron relation does not make sense for second-order phase transitions, as both specific entropy and specific volume do not change in second-order phase transitions.

## Quantitative consideration

Ehrenfest equations are the consequence of continuity of specific entropy s and specific volume v , which are first derivatives of specific Gibbs free energy – in second-order phase transitions. If one considers specific entropy s as a function of temperature and pressure, then its differential is: $ds=\left({{\partial s} \over {\partial T}}\right)_{P}dT+\left({{\partial s} \over {\partial P}}\right)_{T}dP.$ As $\left({{\partial s} \over {\partial T}}\right)_{P}={{c_{P}} \over T}$ , $\left({{\partial s} \over {\partial P}}\right)_{T}=-\left({{\partial v} \over {\partial T}}\right)_{P}$ , then the differential of specific entropy also is:

$d{s_{i}}={{c_{iP}} \over T}dT-\left({{\partial v_{i}} \over {\partial T}}\right)_{P}dP,$

where $i=1$ and $i=2$ are the two phases which transit one into other. Due to continuity of specific entropy, the following holds in second-order phase transitions: ${ds_{1}}={ds_{2}}$ . So,

$\left({c_{2P}-c_{1P}}\right){{dT} \over T}=\left[{\left({{\partial v_{2}} \over {\partial T}}\right)_{P}-\left({{\partial v_{1}} \over {\partial T}}\right)_{P}}\right]dP$

Therefore, the first Ehrenfest equation is:

${\Delta c_{P}=T\cdot \Delta \left({\left({{\partial v} \over {\partial T}}\right)_{P}}\right)\cdot {{dP} \over {dT}}}.$

The second Ehrenfest equation is got in a like manner, but specific entropy is considered as a function of temperature and specific volume:

${\Delta c_{V}=-T\cdot \Delta \left({\left({{\partial P} \over {\partial T}}\right)_{v}}\right)\cdot {{dv} \over {dT}}}$

The third Ehrenfest equation is got in a like manner, but specific entropy is considered as a function of v and P :

${\Delta \left({{\partial v} \over {\partial T}}\right)_{P}=\Delta \left({\left({{\partial P} \over {\partial T}}\right)_{v}}\right)\cdot {{dv} \over {dP}}}.$

Continuity of specific volume as a function of T and P gives the fourth Ehrenfest equation:

${\Delta \left({{\partial v} \over {\partial T}}\right)_{P}=-\Delta \left({\left({{\partial v} \over {\partial P}}\right)_{T}}\right)\cdot {{dP} \over {dT}}}.$

## Limitations

Derivatives of Gibbs free energy are not always finite. Transitions between different magnetic states of metals can't be described by Ehrenfest equations.
