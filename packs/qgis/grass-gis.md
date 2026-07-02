---
title: "GRASS GIS"
source: https://en.wikipedia.org/wiki/GRASS_GIS
domain: qgis
license: CC-BY-SA-4.0
tags: qgis desktop, open source gis, geospatial software, grass gis
fetched: 2026-07-02
---

# GRASS GIS

**GRASS** (originally *Geographic Resources Analysis Support System*, formerly often referred to as **GRASS GIS**) is a software package used for geospatial data management and analysis, image processing, producing graphics and maps, spatial and temporal modeling, and visualizing. It can handle raster, topological vector, image processing, and graphic data, and it can be used as a geographic information system (GIS).

GRASS contains over 400 modules to render maps and images on monitor and paper; manipulate raster and vector data including vector networks; process multispectral image data; and create, manage, and store spatial data.

It is licensed and released as free and open-source software under the GNU General Public License (GPL). It runs on multiple operating systems, including OS X, Windows and Linux. Users can interface with the software features through a graphical user interface (GUI) or by *plugging into* GRASS via other software such as QGIS. They can also interface with the modules directly through a bespoke shell that the application launches or by calling individual modules directly from a standard shell.

The GRASS development team is a multinational group consisting of developers at many locations. GRASS is one of the eight initial software projects of the Open Source Geospatial Foundation and is fiscally sponsored by NumFOCUS.

## Architecture

GRASS supports raster and vector data in two and three dimensions. The vector data model is topological, meaning that areas are defined by boundaries and centroids; boundaries cannot overlap within one layer. In contrast, OpenGIS Simple Features, defines vectors more freely, much as a non-georeferenced vector illustration program does.

GRASS is designed as an environment in which tools that perform specific GIS computations are executed. Unlike GUI-based application software, the GRASS user is presented with a Unix shell containing a modified environment that supports execution of GRASS commands, termed modules. The environment has a state that includes parameters such as the geographic region covered and the map projection in use. All GRASS modules read this state and additionally are given specific parameters (such as input and output maps, or values to use in a computation) when executed. Most GRASS modules and abilities can be operated via a graphical user interface (provided by a GRASS module), as an alternative to manipulating geographic data in a shell.

The GRASS distribution includes over 400 core modules. Over 400 add-on modules created by users are offered on its website. The libraries and core modules are written in C. Other modules are written in C, C++, Python, Unix shell, or other scripting languages. The modules are designed under the Unix philosophy and hence can be combined using Python or shell scripting to build more complex or specialized modules, by users, without knowledge of C programming.

There is cooperation between the GRASS and QGIS projects. Recent versions of QGIS can be executed within the GRASS environment, allowing QGIS to be used as a user-friendly graphical interface to GRASS that more closely resembles other graphical GIS software than does the shell-based GRASS interface.

Another project, JGrass, implemented in Java, combines the user-interface of uDig and algorithms in GRASS to provide hydrological and geomorphological analyses.

## History

GRASS has been under continuous development since 1982 and has involved a large number of federal US agencies, universities, and private companies. The core components of GRASS and the management of integration of efforts into its releases was originally directed by the U.S. Army - Construction Engineering Research Laboratory (USA-CERL), a branch of the U.S. Army Corps of Engineers, in Champaign, Illinois. USA-CERL completed its last release of GRASS as version 4.1 in 1992, and provided five updates and patches to this release through 1995. USA-CERL also wrote the core components of the GRASS 5.0 floating point version.

The development of GRASS was started by the USA-CERL to meet the need of the United States military for software for land management and environmental planning. A key motive was the National Environmental Policy Act. The development platform was Unix running on VAX hardware. During 1982 through 1995, USA-CERL led the development of GRASS, with the involvement of many others, including universities and other federal agencies. USA-CERL officially ceased its involvement in GRASS after release 4.1 (1995), though development had been limited to minor patches since 1993. A group formed at Baylor University to take over the software, releasing GRASS 4.2. Around this time, a port of the software to Linux was made. In 1998, Markus Neteler, the current project leader, announced the release of GRASS 4.2.1, which offered major improvements including a new graphical user interface. In October 1999, the license of the originally public domain software GRASS software was changed to the GNU GPL in version 5.0.

Since then, GRASS has evolved into a powerful software suite with a wide range of applications in many different areas of scientific research and engineering. For example, it is used to estimate potential solar photovoltaic yield with r.sun. As of 2015, GRASS is used in academic and commercial settings around the world, and in many government agencies including NASA, NOAA, USDA, DLR, CSIRO, the National Park Service, the U.S. Census Bureau, USGS, and many environmental consulting companies.

As of 2015, the latest stable release version (LTS) was GRASS GIS 7. It was released in 2015, replacing the old stable branch (6.4) which was released in 2011. Version 7 added many new features, including large data support, a fast topological 2D/3D vector engine, powerful vector network analysis, a full temporal framework and many other features and improvements. As of 2025, the latest stable release version (LTS) is GRASS GIS 8.4.1.

As of 2015, GRASS development is split into two branches: stable and developmental. The stable branch is recommended for most users, while the development branch operates as a testbed for new features.
