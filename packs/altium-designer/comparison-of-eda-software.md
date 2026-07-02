---
title: "Comparison of EDA software"
source: https://en.wikipedia.org/wiki/Comparison_of_EDA_software
domain: altium-designer
license: CC-BY-SA-4.0
tags: altium designer, schematic capture, pcb layout tool, eda software comparison
fetched: 2026-07-02
---

# Comparison of EDA software

This page is a comparison of electronic design automation (EDA) software which is used today to design the near totality of electronic devices. Modern electronic devices are too complex to be designed without the help of a computer. Electronic devices may consist of integrated circuits (ICs), integrated circuit substrates, printed circuit boards (PCBs), field-programmable gate arrays (FPGAs) or a combination of them. Integrated circuits may consist of a combination of digital and analog circuits. These circuits can contain a combination of transistors, resistors, capacitors or specialized components such as analog neural networks, antennas or fuses.

The design of each of these electronic devices generally proceeds from a high- to a low-level of abstraction. For FPGAs the low-level description consists of a binary file to be flashed into the gate array, while for an integrated circuit or printed circuit board the low-level description consists of a layout file which describes the masks to be used for lithography inside a foundry.

Each design step requires specialized tools, and many of these tools can be used for designing multiple types of electronic circuits. For example, a program for high-level digital synthesis can usually be used both for IC digital design as well as for programming an FPGA. Similarly, a tool for schematic-capture and analog simulation can generally be used both for analog IC design and for PCB design.

In the case of integrated circuits (ICs) for example, a single chip may contain today more than 20 billion transistors and, as a general rule, every single transistor in a chip must work as intended. Since a single VLSI mask set can cost up to 10-100 millions, trial and error approaches are not economically viable. To minimize the risk of any design mistakes, the design flow is heavily automated. EDA software assists the designer in every step of the design process and every design step is accompanied by heavy test phases. Errors may be present in the high-level code already, such as for the Pentium FDIV floating-point unit bug, or it can be inserted all the way down to physical synthesis, such as a missing wire, or a timing violation.

## Comparison of proprietary EDA software

### Mainstream EDA software bundles for ICs design

The world of electronic design automation (EDA) software for integrated circuit (IC) design is dominated by the three vendors Synopsys, Cadence Design Systems and Siemens EDA (Formerly Mentor Graphics, acquired in 2017 by Siemens) which have a revenue respectively of 4,2 billion US$, 3 billion US$ and 1,3 billion US$.

These vendors offer software bundles which allow to cover the full spectrum of IC design, from HDL synthesis to physical synthesis and verification.

The development of EDA software for IC design is tightly connected with the development of technology nodes. The properties of a specific semiconductor foundry, such as the transistor models, the physical characteristics and the design rules, are usually encoded in file formats which are proprietary to one or more EDA vendors. This set of files constitutes the process design kit (PDK) and it is usually developed as a joint effort between the foundry and an EDA vendor. Foundries therefore usually release PDKs which are compatible only for one specific EDA bundle. The information contained inside PDKs is usually considered confidential. PDKs are therefore usually protected by non disclosure agreements (NDAs) and may be shipped in an incomplete or in an encrypted form to the designers.

### Proprietary software for electrical simulation (analog/mixed-signal/electromagnetic)

Application and developer

Platform

Latest release

Schematic

?

Simulation

?

PCB

editing?

User Interface Language(s)

Imports

Exports

Scripting support

Version

Date

Advanced Design System

by Keysight

EEsof

EDA

POSIX

2019

2018-11-15

No

Yes,

full-wave electromagnetic simulation

and netlist simulation

Yes

en

HSPICE, SPICE, Spectre netlists;

Gerber

,

Excellon

,

ODB++

, artwork; more

HSPICE, SPICE, Spectre netlists; Gerber, Excellon, ODB++, artwork; more

Python, Application Extension Language (proprietary; "AEL")

Windows

SuSE

RHEL

CircuitLogix

by Logic Design

Windows

10

2019-01

No

Yes, netlist simulation (analog and digital)

Yes

en

SPICE netlist and model formats

SPICE, PDF, Gerber, DXF

LTspice

by

Analog Devices

(free)

Windows, macOS, Wine

26.0.1

2026-01-14

Yes

Yes, netlist simulation (analog)

No

en

netlist

netlist

Micro-Cap

(free, end-of-life)

Windows

12.2.0.5

2021-06-17

(end-of-life)

Yes

Yes, netlist simulation (analog and digital)

No

en

,

jp

HSPICE, PSPICE, SPICE3, netlists, Images, IBIS, Touchstone

SPICE text file, netlist, BOM, Protel, Accel, OrCad, PADS netlists, Schematic and Analysis Plots Images, Numeric Output Text, Excel

Wine

TINA-TI

(free)

Windows, Linux, Mac OS, Android

12.0

2019-12

Yes

Yes

No

23 languages (

en

,

de

,

fr

,

es

, and 19 other languages)

XML, PSpice netlist, (.CIR)

XML, PSpice netlist, (.CIR)

Of these, LTSpice, TINA-TI, Micro-cap are free proprietary applications based on SPICE. Micro-Cap was released as freeware in July 2019, when its parent company Spectrum Software closed down while LTSpice has been free for a long time.

### Comparison of proprietary software for PCB design

Application and developer

Platform

Latest release

Schematic

?

Simulation

?

PCB

editing?

User Interface Language(s)

Imports

Exports

Scripting support

Version

Date

Altium Designer

(former Protel) by

Altium

(included in Altium Develop and Altium Agile)

Windows

24.10.1

2024-10-10

Yes

Yes

Yes

Multilingual

OrCAD, Allegro, PADS Logic, PADS PCB, Expedition, DxDesigner, EAGLE, P-CAD, Gerber, STEP, Solidworks, IDF, Zuken, more

3D PDF, Gerber, Gerber X2, pick-and-place CSV, Excellon, ODB++, IPC-2581, D356, DXF, STEP, Parasolid, EDB, more

Delphi, JS, VB

Wine

CADSTAR

, Board Designer, and Visula by

Zuken

Windows

2022.0

2022-08-31

Yes

Yes, SI & PI

Yes

en

PADS, OrCAD, P-CAD, Protel, DXF, IDF

PDF, Gerber, Excellon, ODB++, DXF, IDF more

COM, macros

CircuitMaker

by

Altium

Windows

2

2021-07

Yes

No

Yes

en

Importer Removed since Last Version (1.3)

Gerber, Excellon, DXF, STEP, PDF

None

Wine

CR-5000

by

Zuken

POSIX

13

2011-05-17

Yes

Yes, SI & PI

Yes

en

,

jp

EDIF, DXF, IGES, IDF, BSDL, STEP, ACIS, Gerber, Excellon, more

PDF, Gerber, Excellon, ODB++ (must request

), DXF, STEP, IPC D-356, IPC-2581, EPS, ACIS

Windows

Unix

Linux

CR-8000

by

Zuken

POSIX

2020

2020-06-30

Yes

Yes, SI & PI, IBIS-AMI/SERDES

Yes

en

,

jp

EDIF, DXF, IGES, IDF, BSDL, STEP, ACIS, Gerber, Excellon, more

PDF, Gerber, Excellon, ODB++ (must request

), DXF, STEP, IPC D-356, IPC-2581, EPS, ACIS

Windows

Unix

Linux

DesignSpark PCB

by

RS Components

Windows

9.0.3

2020-07-08

Yes

Yes, Spice

Yes

en

EAGLE, DXF, EDIF

Gerber, Excellon, ODB++, DXF, IDF, PDF, LPKF

DipTrace

by

Novarm

POSIX

5.2.0.4

2025-12-02

Yes

External

(Spice netlist export)

Yes

21 languages

Altium, Eagle, KiCad, OrCAD, P-CAD, PADS, Gerber, N/C Drill, DXF, BSDL Pinlist, Netlists

Gerber, Gerber X2, Excellon, ODB++, DXF, Eagle, P-CAD, PADS, OrCAD, IPC-D-356, STEP, VRML, Pick and Place, CSV, BOM

Windows

Mac

Wine

EAGLE

by

Autodesk

/

CadSoft Computer

(discontinued)

POSIX

9.6.2

2020-05-27

Yes

Ngspice

Yes

de

,

en

,

zh

,

hu

,

ru

EAGLE (XML), ACCEL (P-CAD, Altium, Protel), ULTIBOARD, Netlists, BMP, Custom

EAGLE (XML), Protel, Netlists, Images, Gerber, Gerber X2, Excellon,

Sieb & Meyer

, HPGL, PostScript/EPS, PDF, Images, HyperLynx, IDF, Custom

Proprietary User Language Programming (ULP)

Windows

Linux

Mac

EasyEDA

POSIX

6.4.5

2020-08-19

Yes

Ngspice

Yes

en

,

fr

,

de

,

pl

,

jp

,

ru

,

es

,

se

,

ua

,

zh

...

Altium, EAGLE, KiCad libraries, DipTrace, LTspice .asc/.asy files, JSON, Spice

PDF, PNG, SVG, JSON, Gerber, Excellon, Pick and Place CSV file, CSV-formatted drill chart, Bill of Materials CSV file, Altium netlist, FreePCB netlist, PADS Layout Netlist, Spice netlist.

JSON

Windows

Linux

Mac

ChromeOS

as a

Web application

Flux.ai

ChromeOS

as a

Web application

N/A

2025

Yes

Ngspice

Yes

en

EAGLE/KiCad libraries, Altium/Allegro Schematics, DXF, SVG, STEP, etc.

Gerber, IPC-2581C, ODB++, EDIF netlists, D356 netlists, JEP30, Pick and Place CSV file, CSV-formatted drill chart, Bill of Materials CSV file.

TypeScript

NI Ultiboard

and

Multisim

by

National Instruments

Windows

14.2

2019-05-19

Yes

Yes

Yes

en

MS*, MP*, EWB, Spice, OrCAD, UltiCap, Protel, Gerber, DXF, Ultiboard 4&5, Calay

BOM, Gerber, Excellon, IGES (3D), DXF (2D & 3D), SVG

Web application

OrCAD

Windows

17.4 - 22.1

2022-10-20

Yes

Yes

Yes

en

EAGLE, PADS, Altium, STEP, DXF, IDF, IDX, OrCAD SDT, OrCAD Layout,OrCAD

PDF, Gerber, Gerber X2, Excellon drill/route, netlist, ODB++, DXF, IDF, IDX, STEP,3D PDF, IPC2581

Tcl/TK, SKILL (Lisp)

Proteus

by Labcenter Electronics Ltd

Windows

8.17

2023-12-11

Yes

Yes

Yes

en

Gerber, BMP, DXF

PDF, Gerber, GerberX2, Excellon, ODB++, DXF, IDF, PKP, testpoint file, metafile, BMP.

internal script

Pulsonix

by WestDev Ltd

Windows

12.5

2023

Yes

Yes

Yes

en

Allegro, Altium, CadStar, EAGLE, OrCAD, PADS, P-CAD, Protel, Gerber, STEP, DXF, IDF, more

Gerber, Gerber X2, Excellon, ODB++, IPC-2581, PDF, DXF, STEP, IDF, BOM, more

Proprietary language, ActiveX

Wine

TARGET 3001!

Windows

33.4

2025-04-09

Yes

Yes

Yes

en

,

de

,

fr

EAGLE, DXF, Gerber, Gerber, Excellon, BMP, CXF, STEP 3D

ODB++, Gerber, Gerber X2, Excellon, EAGLE, HPGL, G-Code (Milling), CXF,

STEP 3D

, Excel BOMs, Pick&Place, GenCAD, FABmaster, IPC D-356,

Test points

, Netlists,

OBJ

,

POV-Ray

, PDF

Package generator scripts, BOM scripts, printing and PDF generator scripts, 3D scripts

Wine

TINA

Windows

12.0

2019-12

Yes

Yes

Yes

23 languages (

en

,

de

,

fr

,

es

and 19 other languages)

VHDL

,

Verilog

,

Verilog-A

, and

Verilog-AMS

VHDL

,

Verilog

,

Verilog-A

, and

Verilog-AMS

Linux

MacOS

Android

Upverter

POSIX

N/A

2019-05-10

Yes

No

Yes

en

Altium, PDF, OpenJSON, EAGLE

PDF, Gerber, Excellon, netlist, PADS Layout Netlist, Pick and Place CSV, High-Res PNG, CSV-formatted drill chart, CSV-formatted list of all parts

Windows

Web application

123D Circuits

by

Autodesk

POSIX

N/A

Yes, + breadboard

Yes

Yes

en

EAGLE

Gerber

Windows

Web application

Application and developer

Platform

Latest release

Schematic

?

Simulation

?

PCB

editing?

User Interface Language(s)

Imports

Exports

Scripting support

Version

Date

## Comparison of free and open source software EDA tools

### Free and open source software EDA bundles for IC design

Free and open-source (FOSS) EDA software bundles are currently under fast development mainly thanks to the DARPA and Google's openROAD project. The OpenROAD project offers a complete stack of tools from high-level synthesis down to layout generation The flow includes Yosys for logic synthesis, OpenLane for physical synthesis and targets the SkyWater 130 nm PDK. The flow is currently utilized to submit design for free fabrication at Google.

### Free and open source software for high-level synthesis

High-level synthesis software can generally be used for the design of both application-specific integrated circuits (ASICs) and field-programmable gate arrays (FPGAs). Most high-level synthesis software is used to edit and verify code written in one of the mainstream hardware description languages (HDL) like VHDL or Verilog. Other tools instead operate at a higher level of abstraction and allow to synthesize HDL code starting from languages like Chisel or SpinalHDL. The higher abstraction of such languages enables formal verification of HDL code.

| Name | Architecture | License | Comment |
|---|---|---|---|
| GHDL | Linux, Mac | GPL-2.0-or-later | VHDL analyzer, compiler, and simulator. |
| Icarus Verilog | *BSD, Linux, Mac | GPL-2.0-or-later | Verilog simulator |
| Verilator | Posix | LGPL-3.0-only or Artistic-2.0 | Verilator is the fastest free Verilog HDL simulator. It compiles synthesizable Verilog into cycle accurate C++ or SystemC code following 2-state synthesis (zero delay) semantics. Benchmarks reported on its website suggest it is several times faster than commercial event driven simulators such as ModelSim, NC-Verilog and VCS, while not quite as fast as commercial cycle accurate modeling tools such as Carbon ModelStudio and ARC VTOC. |

## List by developer

| List of electrical engineering software |   |   |
|---|---|---|
| Software | Developer | Operating System/License |
| Advanced Design System (ADS) | Keysight Technologies | Windows, Linux |
| Altium Designer (included in Altium Develop and Altium Agile) | Altium Limited | Windows |
| ANSYS Electronics | ANSYS | Windows, Linux |
| ANSYS HFSS | ANSYS | Windows |
| ANSYS Maxwell | ANSYS | Windows, Linux |
| AutoCAD – Electrical | Autodesk | Windows |
| CST Studio Suite | Simulia | Windows, Linux |
| Eagle | Autodesk | Windows, macOS, Linux |
| EMTP-RV | ATPDraw | Windows |
| EMTPWorks | EMTPWorks | Windows |
| Electrical Transient Analyzer Program | ETAP/Operation Technology Inc. | Windows |
| FreeCAD | FreeCAD Community | Windows, macOS, Linux |
| FreePCB | FreePCB community | Windows |
| gEDA | gEDA Project | Windows, macOS, Linux |
| KTechLab | KTechLab Developers | Windows, macOS, Linux |
| LibrePCB | LibrePCB Team | Windows, macOS, Linux |
| Quite Universal Circuit Simulator (QUCS) | Qucs Developers | Windows, macOS, Linux |
| KiCad | KiCad Developers | Windows, macOS, Linux |
| LabVIEW | National Instruments | Windows, macOS, Linux |
| LTspice | Linear Technology | Windows |
| NI Multisim | National Instruments Electronics Workbench Group | Windows |
| NL5 circuit simulator | New Wave Instruments | Windows |
| OrCAD | Cadence Design Systems | Windows |
| PowerEsim | Power Integrations | Web application |
| PSIM | Powersim Inc. | Windows |
| PSpice | Cadence Design Systems | Windows |
| Power system simulator for engineering | Siemens Energy | Windows |
| SaberRD | Synopsys | Windows |
| Simulink | MathWorks | Windows, macOS, Linux |
| SynchroTrace | Rosh Engineering LLC | Windows |
| TINA | DesignSoft | Windows |
| XCircuit | Tim Edwards | Windows, macOS, Linux |

- Proprietary
- Open source
- Freeware/Trialware

## Open source software for IC physical synthesis and layout

This list does not include schematic editors or simulators since these can generally be used both for Integrated Circuits (ICs) and for Printed Circuit Board (PCB) as long as device models are available.

| Name | Architecture | License | Autorouter | Comment |
|---|---|---|---|---|
| Electric | *BSD, Java | GPL-3.0-or-later | Yes | VLSI circuit design tool with connectivity at all levels. Can also be used for schematic entry and PCB design. In maintenance mode since 2017. |
| Magic | Linux | BSD license | No | A very-large-scale integration layout tool |

## Open source software for schematic editing and analog/mixed-signal simulation

| Name | Architecture | License | Comment |
|---|---|---|---|
| Gnucap | any (C++11) | GPL-3.0-or-later | Mixed-signal circuit simulator |
| KTechLab | Linux | GPL | KTechLab is a schematic capture and simulator. It is specifically geared toward mixed signal simulation of analog components and small digital processors. |
| Ngspice | Linux, Solaris, Mac, NetBSD, FreeBSD, Windows | BSD-3-Clause | SPICE + XSPICE + Cider |
| Oregano |   | GPL-2.0-or-later | Schematic capture + spice simulation |
| Quite Universal Circuit Simulator (QUCS) | Linux, Solaris, Mac, NetBSD, FreeBSD, Windows | GPL-2.0-or-later | Schematic capture + Verilog + VHDL + simulation. Qucs-S fork supports SPICE backends Ngspice, Xyce, & SpiceOpus. |
| XCircuit | Unix | GPL | Used to produce netlists and publish high-quality drawings. |

### Open source software for PCB design

| Name | Architecture | License | Autorouter | Imports | Exports | Scripting support | Comment |
|---|---|---|---|---|---|---|---|
| atopile | Linux, Mac, Windows | MIT License | No | - | Gerber, BOM | Python | Code-based EDA tool that allows hardware engineers to design electronic circuits and PCBs using a programming-like environment. It integrates hardware design specifications directly into code, enabling intelligent design capture, version control, and continuous integration practices. |
| FreePCB | Windows | GPL | Yes | - | Gerber | No | A printed circuit board design program for Microsoft Windows. FreePCB allows for up to 16 copper layers, both metric and US customary units, and export of designs in Gerber format. Boards can be partially or fully autorouted with the FreeRouting autorouter by using the FpcROUTE Specctra DSN design file translator. |
| Fritzing | Windows, Mac, Linux | GPL-3.0-or-later | Yes | gEDA symbols, KiCad symbols, SVG | Gerber, DIY etching, BOM, SVG, PDF, EPS | No | Protoboard view, schematic view, PCB view, Code (firmware) view. Includes customizable design rule checker. Includes common shaped boards like Arduino and Raspberry Pi shields. Allows spline curve traces. Only two layers (top and bottom). Outputs gerbers. |
| gEDA | *BSD, Linux, Mac | GPL-2.0-or-later | Yes | gschem netlists, image as background | Gerber, Excellon, SVG, PDF, EPS, PNG, GIF, JPEG, Specctra, XYRS | Guile (Scheme) | Schematic, simulation, PCB editor, gerber view |
| KiCad | Linux, Mac, Windows | GPL-3.0-or-later | FreeRouting | Altium, CadStar, EAGLE (XML), P-CAD, Fabmaster, TinyCAD net lists, OrCAD EDIF | PDF, Gerber, Gerber X2, Excellon, netlist, VRML2, STEP, IDFv3 | Python | Full package for schematic and board design, etc. Design rule checking. User-defined symbols and footprints. Gerber/drill file creation. Graphic interface. Active user community. |
| pcb-rnd | *BSD, Linux, Mac, Windows | GPL-2.0-or-later | Yes | gschem netlists, Protel Autotrax, KiCad (legacy & s-expr layouts), EAGLE (XML & v3,4,5 binary layouts), eeschema netlists, mentor netlists, TinyCad netlists, Calay netlist, FreePCB/easyEDA netlist, LT-Spice, MUCS, Mentor Graphics Hyperlynx, image (BMP, JPG, GIF, PNG), HPGL, BXL, Specctra (DSN), PADS | Gerber/drill, SVG, PDF, EPS, PNG, GIF, JPEG, Specctra (DSN), PADS, Protel Autotrax, KiCad (legacy & s-expr), DXF, FidocadJ, Mentor Graphics Hyperlynx, template configurable XYRS/BOM | Python, Lua, Perl, Tcl, AWK (multiple dialects), Lisp & Scheme (multiple dialects), JavaScript, Ruby, Pascal, BASIC | Circuit layout program with extended file format support, DRC, parametric footprints, query language, and GUI and command line operation for batch processing and automation |
| tscircuit | *BSD, Linux, Mac, Windows, Web Application | MIT License | Yes | KiCad | SVG, Gerber, KiCad, BOM | Javascript | Typescript-based framework for creating printed circuit boards with TSX code and a built-in autorouter |
