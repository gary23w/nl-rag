---
title: "Solder mask"
source: https://en.wikipedia.org/wiki/Solder_mask
domain: pcb-layout-embedded
license: CC-BY-SA-4.0
tags: printed circuit board, surface-mount technology, board via, solder mask
fetched: 2026-07-02
---

# Solder mask

**Solder mask**, **solder stop mask** or **solder resist** is a thin lacquer-like layer of polymer that is usually applied to the copper traces of a printed circuit board (PCB) for protection against oxidation and to prevent solder bridges from forming between closely spaced solder pads. A solder bridge is an unintended electrical connection between two conductors by means of a small blob of solder. PCBs use solder masks to prevent this from happening. Solder mask is not always used for hand soldered assemblies, but is essential for mass-produced boards that are soldered automatically using reflow or wave soldering techniques. Once applied, openings must be made in the solder mask wherever components are soldered, which is accomplished using photolithography. Solder mask is traditionally green, but is also available in many other colors.

Solder mask comes in different media depending upon the demands of the application. The lowest-cost solder mask is epoxy liquid that is silkscreened through the pattern onto the PCB. Other types are the liquid photoimageable solder mask (LPSM or LPI) inks and dry-film photoimageable solder mask (DFSM). LPSM can be silkscreened or sprayed on the PCB, exposed to the pattern and developed to provide openings in the pattern for parts to be soldered to the copper pads. DFSM is vacuum-laminated on the PCB then exposed and developed. All three processes typically go through a thermal cure of some type after the pattern is defined although LPI solder masks are also available in ultraviolet (UV) cure.

The solder stop layer on a flexible board is also called *coverlay* or *coverfilm*.

In electronic design automation, the solder mask is treated as part of the layer stack of the printed circuit board, and is described in individual Gerber files for the top and bottom side of the PCB like any other layer (such as the copper and silk-screen layers). Typical names for these layers include `tStop`/`bStop` aka `STC`/`STS` or `TSM`/`BSM` (EAGLE), `F.Mask`/`B.Mask` (KiCad), `StopTop`/`StopBot` (TARGET), `maskTop`/`maskBottom` (Fritzing), `SMT`/`SMB` (OrCAD), `MT.PHO`/`MB.PHO` (PADS), `LSMVS`/`LSMRS` (WEdirekt) or `GTS`/`GBS` (Gerber and many others).
