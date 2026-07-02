---
title: "Multi-project wafer service"
source: https://en.wikipedia.org/wiki/Multi-project_wafer_service
domain: tsmc-process-node
license: CC-BY-SA-4.0
tags: tsmc foundry, semiconductor process node, 5 nm process, pure-play foundry
fetched: 2026-07-02
---

# Multi-project wafer service

**Multi-project chip** (**MPC**), and **multi-project wafer** (**MPW**) semiconductor manufacturing arrangements allow customers to share tooling (like mask) and microelectronics wafer fabrication cost between several designs or projects.

With the MPC arrangement, one chip is a combination of several designs and this combined chip is then repeated all over the wafer during the manufacturing. The MPC arrangement typically produces a roughly equal number of chip designs per wafer.

With the MPW arrangement, different chip designs are aggregated on a wafer, with perhaps a different number of designs/projects per wafer. This is made possible by novel mask-making and exposure systems in photolithography during IC manufacturing. MPW builds upon the older MPC procedures and enables more effective support for different phases and needs of manufacturing volumes of different designs/projects. MPW arrangement support education, research of new circuit architectures and structures, prototyping, and even small-volume production.

Worldwide, several MPW services are available from companies, semiconductor foundries and from government-supported institutions. Originally both MPC and MPW arrangements were introduced for integrated circuit (IC) education and research; some MPC/MPW services/gateways are aimed for non-commercial use only. Currently MPC/MPW services are effectively used for system on a chip integration. Selecting the right service platform at the prototyping phase ensures gradual scaling up production via MPW services taking into account the rules of the selected service.

MPC/MPW arrangements have also been applied to microelectromechanical systems (MEMS), integrated photonics like photonics fabrication including also other materials than silicon like InP, flexible electronics, microfluidics and even chiplets.

A refinement of MPW is multi-layer mask (MLM) arrangement, where a limited number of masks (e.g. 4) are changed during manufacturing at exposure phase. The rest of the masks are the same from the chip to chip on the whole wafer. MLM approach is well suited for several specific cases:

- Large (even possibly part or whole wafer) designs like detectors, where by using few mask layers it is possible to form functional devices
- Making different versions of one design/project, like for different performance or standards of one design

Typically MLM approach is used for one wafer batch (consisting of several wafers depending on the fabrication line) and for one customer. By using MLM it is possible to get larger devices (even up to wafer size) or larger number of dies and wafers up to few batches typically. MLM is a smooth continuation from MPW production volumes upwards and therefore this may support also small/mid size volume production. Not all foundries support MLM arrangements.

Due to the complexity of the technologies available and the need to run MPC/MPWs smoothly, following the rules, timing of the designs and use of suggested design tools are critical for leveraging the benefits of MPC/MPW services. However every service provider has its own practicalities including design data, die sizes, design rules, device models, design tools used, ready IP blocks available and timing etc.

Turn around times and cost of MPC and MPW services depend on the manufacturing technology and designs/prototypes are typically available as bare dies or as packaged devices. Deliveries are typically untested, but in most of the cases the quality of the manufacturing process is guaranteed by the measurement results of process control monitor(s) (PCM) or similar.

MPC approach was one of the first hardware service platforms in semiconductor industry, and the MPW arrangement is continuing to be part of microelectronics manufacturing and foundry model not limited to silicon IC manufacturing but spreading into other semiconductor and microelectronic production areas for prototyping, development and research.

## Companies and services

Many MPC/MPW arrangements were first nationwide activities, but were expanded international, global co-operative activities based on emerging and later mature semiconductor foundry technologies available from research institutes or universities and commercial foundries:

### CMC Microsystems

CMC Microsystems is a not-for-profit organization in Canada accelerating research and innovation in advanced technologies. Founded in 1984, CMC lowers barriers to designing, manufacturing, and testing prototypes in microelectronics, photonics, quantum, MEMS, and packaging. CMC technology platforms such as the ESP (Electronic Sensor Platform) jumpstart R&D projects, enabling engineers and scientists to achieve results sooner and at a lower cost. Annually, more than 700 research teams from companies and 100 academic institutions around the world access CMC's services and turn more than 400 designs into prototypes through its global network of manufacturers. This support enables 400 industrial collaborations and 1,000 trained HQP to join industry each year, and these relationships assist in the translation of academic research into outcomes—publications, patents, and commercialization.

### Muse Semiconductor

Muse Semiconductor was founded in 2018 by former eSilicon employees. The company name "Muse" is an informal acronym for MPW University SErvice. Muse focuses on serving the MPW needs of microelectronics researchers. Muse supports all TSMC technologies and offers an MPW service with a minimum area of 1mm^2 for some technologies. Muse is a member of the TSMC University FinFET Program.

### MOSIS

The first well known MPC service was MOSIS (Metal Oxide Silicon Implementation Service), established by DARPA as a technical and human infrastructure for VLSI. MOSIS began in 1981 after Lynn Conway organized the first VLSI System Design Course at MIT in 1978 and the course produced 'multi-university, multi-project chip-design demonstration' delivering devices to the course participants in 1979. The designs for the MPC were gathered using ARPANET. The technical background additionally to education was to develop and research in a cost effective way new computer architectures without limitations of standard components. MOSIS primarily services commercial users with MPW arrangement. MOSIS has ended their University Support Program. With MOSIS, designs are submitted for fabrication using either open (i.e., non-proprietary) VLSI layout design rules or vendor proprietary rules. Designs are pooled into common lots and run through the fabrication process at foundries. The completed chips (packaged or bare dies) are returned to customers.

### NORCHIP

The first international silicon IC MPC service NORCHIP was established among four nordic countries (Denmark, Finland, Norway and Sweden) 1981 delivering first chips 1982. It was funded by Nordic Industrial Fund and R&D financing organisations from each participating country. Targets were training and to enhance cooperation between research and industry specifically in areas of analog and digital signal processing and power management Integration. Parallel with NORCHIP organised by same nordic countries there was Nordic GaAs program NOGAP 1986-1989, which produced modelling techniques for GaAs IC devices, and demonstrators of high speed digital and RF/analog MMICs. From 1989 to 1995 nordic universities, research institutes and small companies have been participating in european EUROCHIP and from 1995 on wards in EUROPRACTICE.

### CMP

CMP a French company working since 1981 started MPC operation with NMOS offering but expanding offering to CMOS and various other technologies. CMP was also the first official pan-continental MPC/MPW operation having link to MOSIS among other MPW arrangements globally. CMPs services have included variety of technologies including multi-chip modules (MCMs) suitable for the packaging of chiplets.

### AusMPC

Similar arrangements utilising silicon IC technology were also AusMPC in Australia starting 1981, E.I.S. project (started year 1983) in Germany and EUROEAST (1994-1997) covering Romania, Poland, Slovak Republic, Hungary, Czech Republic, Bulgaria, Estonia, Ukraine, Russia, Latvia, Lithuania and Slovenia. BERCHIP MPC activity starting in 1994 was organised in Latin America. Numerous MPW services have been launched since 1994 worldwide.

### Tiny Tapeout

Tiny Tapeout is a multi project chip service that lowers the barrier to entry to chip design by using open source tools and PDKs. To reduce the cost of tapeout, up to 512 analog and digital designs are connected via a power-gated multiplexer. As of 2026 supported PDKs are Skywater's SKY130, IHP's SG13G2 and Global Foundries' GF180mcu. Tiny Tapeout schedules multiple tapeout opportunities per year.
