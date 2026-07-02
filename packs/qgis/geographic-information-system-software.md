---
title: "Geographic information system software"
source: https://en.wikipedia.org/wiki/Geographic_information_system_software
domain: qgis
license: CC-BY-SA-4.0
tags: qgis desktop, open source gis, geospatial software, grass gis
fetched: 2026-07-02
---

# Geographic information system software

A **GIS software program** is a computer program to support the use of a geographic information system, providing the ability to create, store, manage, query, analyze, and visualize geographic data, that is, data representing phenomena for which location is important. The GIS software industry encompasses a broad range of commercial and open-source products that provide some or all of these capabilities within various information technology architectures.

## History

The earliest geographic information systems, such as the Canadian Geographic Information System started in 1963, were bespoke programs developed specifically for a single installation (usually a government agency), based on custom-designed data models. During the 1950s and 1960s, academic researchers during the quantitative revolution of geography began writing computer programs to perform spatial analysis, especially at the University of Washington and the University of Michigan, but these were also custom programs that were rarely available to other potential users.

Perhaps the first general-purpose software that provided a range of GIS functionality was the Synagraphic Mapping Package (SYMAP), developed by Howard T. Fisher and others at the nascent Harvard Laboratory for Computer Graphics and Spatial Analysis starting in 1965. While not a true full-range GIS program, it included some basic mapping and analysis functions, and was freely available to other users. Through the 1970s, the Harvard Lab continued to develop and publish other packages focused on automating specific operations, such as SYMVU (3-D surface visualization), CALFORM (choropleth maps), POLYVRT (topological vector data management), WHIRLPOOL (vector overlay), GRID and IMGRID (raster data management), and others. During the late 1970s, several of these modules were brought together into Odyssey, one of the first commercial complete GIS programs, released in 1980.

During the late 1970s and early 1980s, GIS was emerging in many large government agencies that were responsible for managing land and facilities. Particularly, federal agencies of the United States government developed software that was by definition in the public domain because of the Freedom of Information Act, and was thus released to the public. Notable examples included the Map Overlay and Statistical System (MOSS) developed by the Fish & Wildlife Service and Bureau of Land Management (BLM) starting in 1976; the PROJ library developed at the United States Geological Survey (USGS), one of the first programming libraries available; and GRASS GIS originally developed by the Army Corps of Engineers starting in 1982. These formed the foundation of the open source GIS software community.

The 1980s also saw the beginnings of most commercial GIS software, including Esri ARC/INFO in 1982; Intergraph IGDS in 1985, and the Mapping Display and Analysis System (MIDAS), the first GIS product for MS-DOS personal computers, which later became MapInfo. These would proliferate in the 1990s with the advent of more powerful personal computers, Microsoft Windows, and the 1990 U.S. census, which raised awareness of the usefulness of geographic data to businesses and other new users.

Several trends emerged in the late 1990s that have significantly changed the GIS software ecosystem leading to the present, by moving in directions beyond the traditional full-featured desktop GIS application. The emergence of object-oriented programming languages facilitated the release of component libraries and application programming interfaces, both commercial and open-source, which encapsulated specific GIS functions, allowing programmers to build spatial capabilities into their own programs. Second, the development of spatial extensions to object-relational database management systems (also both open-source and commercial) created new opportunities for data storage for traditional GIS, but also enabled spatial capabilities to be integrated into enterprise information systems, including business processes such as human resources. Third, as the World Wide Web emerged, web mapping quickly became one of its most popular applications; this led to the development of Server-based GIS software that could perform the same functions as a traditional GIS, but at a location remote from a client who only needed a web browser installed. All of these have combined to enable emerging trends in GIS software, such as the use of cloud computing, software as a service (SAAS), and smartphones to broaden the availability of spatial data, processing, and visualization.

## Types of software

The software component of a traditional geographic information system is expected to provide a wide range of functions for handling spatial data:

- *Data management*, including the creation, editing, and storage of geographic data, as well as transformations such as changing coordinate systems and converting between raster and vector models.
- *Spatial analysis*, including a range of processing tools from basic queries to advanced algorithms such as network analysis and vector overlay
- *Output*, especially cartographic design.

The modern GIS software ecosystem includes a variety of products that may include more or less of these capabilities, collect them in a single program, or distribute them over the Internet. These products can be grouped into the following broad classes:

**Desktop GIS application**

The traditional form of GIS software, first developed for mainframes and minicomputers, then

Unix

workstations

, and now

personal computers

. A desktop GIS program provides a full suite of capabilities, although some programs are modularized with extensions that can be purchased separately.

**Server GIS application**

A program which runs on a remote

server

(usually in concert with an

HTTP server

), handling many or all of the above functions, taking in requests and delivering results via the

World Wide Web

. Thus, the client typically accesses server capabilities using a normal web browser. Early server software was focused specifically on

web mapping

, only including the output phase, but current server GIS provides the full suite of functions. This server software is at the core of modern

cloud-based

platforms such as

ArcGIS Online

.

**Geospatial library**

A

software component

that provides a focused set of documented functions, which software developers can incorporate into their own programs. In modern

object-oriented programming

languages such as

C#

,

JavaScript

and

Python

, these are typically encapsulated as

classes

with a documented

application programming interface

(API).

**Spatial database**

An extension to an existing database software program (most commonly, an

object-relational database

management system) that creates a geometry datatype, enabling spatial data to be stored in a column in a table, but also provides new functions to query languages such as

SQL

that include many of the management and analysis functions of GIS. This enables database managers and programmers to perform GIS functions without traditional GIS software.

The current software industry consists of many competing products of each of these types, in both open-source and commercial forms. Many of these are listed below; for a direct comparison of the characteristics of some of them, see Comparison of geographic information systems software.

## Open source software

The development of open source GIS software has—in terms of software history—a long tradition with the appearance of a first system in 1978. Numerous systems are available which cover all sectors of geospatial data handling.

### Desktop GIS

The following open-source desktop GIS projects are reviewed in Steiniger and Bocher (2008/9):

- GRASS GIS – Geospatial data management, vector and raster manipulation - developed by the U.S. Army Corps of Engineers
- gvSIG – Mapping and geoprocessing with a 3D rendering plugin
- ILWIS (Integrated Land and Water Information System) – Integrates image, vector and thematic data.
- JUMP GIS / OpenJUMP ((Open) Java Unified Mapping Platform) – The desktop GISs OpenJUMP, SkyJUMP, deeJUMP and Kosmo all emerged from JUMP.
- MapWindow GIS – Free desktop application with plugins and a programmer library
- QGIS (previously known as Quantum GIS) – Powerful cartographic and geospatial data processing tools with extensive plug-in support
- SAGA GIS (System for Automated Geoscientific Analysis) – Tools for environmental modeling, terrain analysis, and 3D mapping
- uDig – API and source code (Java) available.

Besides these, there are other open source GIS tools:

- Generic Mapping Tools – A collection of command-line tools for manipulating geographic and Cartesian data sets and producing PostScript illustrations.
- FalconView – A mapping system created by the Georgia Tech Research Institute for Windows. A free, open source version is available.
- Kalypso – Uses Java and GML3. Focuses mainly on numerical simulations in water management.
- TerraView – Handles vector and raster data stored in a relational or geo-relational database, i.e. a frontend for TerraLib.
- Whitebox GAT – Cross-platform, free and open-source GIS software.

### Other geospatial tools

Apart from desktop GIS, many other types of GIS software exist.

#### Web map servers

- GeoServer – Written in Java and relies on GeoTools. Allows users to share and edit geospatial data.
- MapGuide Open Source – Runs on Linux or Windows, supports Apache and IIS web servers, and has APIs (PHP, .NET, Java, and JavaScript) for application development.
- Mapnik – C++/Python library for rendering - used by OpenStreetMap.
- MapServer – Written in C. Developed by the University of Minnesota.

#### Spatial database management systems

- PostGIS – Spatial extensions for the open source PostgreSQL database, allowing geospatial queries.
- ArangoDB – Builtin features available for Spatial data management, allowing geospatial queries.
- SpatiaLite – Spatial extensions for the open source SQLite database, allowing geospatial queries.
- TerraLib – Provides advanced functions for GIS analysis.
- OrientDB – Builtin features available for Spatial data management, allowing geospatial queries.

#### Software development frameworks and libraries (for web applications)

- GeoBase (Telogis GIS software) – Geospatial mapping software available as a software development kit.
- OpenLayers – Open source AJAX library for accessing geographic data layers of all kinds, originally developed and sponsored by MetaCarta.
- Leafletjs – Open source JavaScript Library for Mobile-Friendly Interactive Maps
- xeokit – Open-source JavaScript SDK for high-performance 3D visualization of BIM and engineering models in web browsers with support for formats like IFC, CityJSON, and LAS/LAZ, with global coordinates and double-precision rendering suitable for GIS applications.

#### Software development frameworks and libraries (non-web)

- GeoTools – Open source GIS toolkit written in Java, using Open Geospatial Consortium specifications.
- GDAL / OGR
- Orfeo toolbox

#### Cataloging application for spatially referenced resources

- GeoNetwork opensource – A catalog application to manage spatially referenced resources
- pycsw – pycsw is an OGC CSW server implementation written in Python

#### Other tools

## Commercial or proprietary GIS software

### Desktop GIS

Note: Almost all of the companies below offer Desktop GIS and WebMap Server products. Some such as Manifold Systems and Esri offer Spatial DBMS products as well.

- Autodesk – Products that interface with its AutoCAD software package include Map 3D, Topobase, and MapGuide.
- Bentley Systems – Products that interface with its MicroStation software package include Bentley Map and Bentley Map View.
- ENVI – Utilized for image analysis, exploitation, and hyperspectral analysis.
- ERDAS IMAGINE – Products include Leica Photogrammetry Suite, ERDAS ER Mapper, ERDAS ECW/JP2 SDK (ECW (file format)) and ERDAS APOLLO.
- Esri – Products include ArcMap, ArcGIS, ArcSDE, ArcIMS, ArcWeb services and ArcGIS Server.
- Intergraph – Products include G/Technology, GeoMedia, GeoMedia Professional, GeoMedia WebMap, and add-on products for industry sectors, as well as photogrammetry.
- MapInfo – Desktop GIS MapInfo Professional.
- Smallworld

- Cadcorp – Products include Cadcorp SIS, GeognoSIS, mSIS and developer kits.
- Caliper – Products include Maptitude, TransModeler and TransCAD.
- Conform by GameSim – Software for fusing and visualizing elevation, imagery, vectors, and LiDAR. The fused environment can be exported into 3D formats for gaming, simulation, and urban planning.
- Dragon/ips – Remote sensing software with GIS capabilities.
- Geosoft – GIS and data processing software used in natural resource exploration.
- GeoTime – software for 3D visual analysis and reporting of location data over time; an ArcGIS extension is also available.
- Global Mapper – GIS software package currently developed by Blue Marble Geographics; originally based on USGS dlgv32 source code.
- Golden Software – GIS and scientific software. Products include *Surfer* for gridding and contouring, *MapViewer* for thematic mapping and spatial analysis, *Strater* for well or borehole logging and cross sections, *Voxler* for true 3D well and component mapping, *Didger* for digitizing and coordinate conversion, and *Grapher* for 2D and 3D graphing.
- Kongsberg Gallium Ltd. – Products include InterMAPhics and InterView.
- MapDotNet – Framework written in C#/.NET for building WPF, Silverlight, and HTML5 applications.
- Manifold System – GIS software package.
- RegioGraph by GfK GeoMarketing – GIS software for business planning and analyses; company also provides compatible maps and market data.
- RemoteView
- SuperMap Inc. – a GIS software provider that offers Desktop, Component, Web, and Mobile GIS.
- TerrSet (formerly IDRISI) – GIS and Image Processing product developed by Clark Labs at Clark University.
- TNTmips by MicroImages – a system integrating desktop GIS, advanced image processing, 2D-3D-stereo visualization, desktop cartography, geospatial database management, and webmap publishing.

### GIS as a service

Many suppliers are now starting to offer Internet based services as well as or instead of downloadable software and/or data. These can be free, funded by advertising or paid for on subscription; they split into three areas:

- SaaS – Software as a Service: Software available as a service on the Internet
  - ArcGIS Online – Esri's cloud based version of ArcGIS
  - CartoDB – Online mapping platform that offers an open source, cloud based SaaS model
  - Google Earth#Google_Earth_Engine; Provides algorithms and a large catalog of public data for global scale spatial computation.
  - Mapbox – Provider of custom online maps for websites
  - MapTiler – Provider of customizable maps for applications and websites.
  - Maptitude Online – Caliper's cloud based version of Maptitude
- PaaS – Platform as a Service: geocoding or analysis/processing services
  - ArcGIS Online
  - FME Cloud
  - Google Maps JavaScript API version 3
  - Here Maps JavaScript API version
  - Microsoft Bing Geocode Dataflow API
  - US Census Geocoder
- DaaS – Data as a Service: data or content services
  - ArcGIS Online
  - Apple Maps
  - Google Maps
  - Here Maps
  - OpenStreetMap
  - Microsoft Bing Maps

### Spatial DBMS

- Boeing's Spatial Query Server – Spatially enables Sybase ASE.
- IBM Db2 – Allows spatial querying and storing of most spatial data types.
- Informix – Allows spatial querying and storing of most spatial data types.
- MySQL – Allows spatial querying and storing of most spatial data types.
- Microsoft SQL Server (2008 and later) – GIS products such as MapInfo and Cadcorp SIS can read and edit this data while Esri and others are expected to be able to read and edit this data at some point in the future.
- Oracle Spatial – Product allows users to perform geographic operations and store spatial data types in an Oracle environment. Most commercial GIS packages can read and edit spatial data stored in this way.
- SAP HANA – Allows users to store common spatial data types, load spatial data files with well-known text (WKT) and well-known binary (WKB) formats and perform spatial processing using SQL. Open Geospatial Consortium (OGC) certification allows third party GIS software providers to store and process spatial data. GIS products such as ArcGIS from Esri work with HANA.
- Teradata – Teradata geospatial allows storage and spatial analysis on location-based data which is stored using native geospatial data-types within the Teradata database.
- VMDS – Version managed data store from Smallworld.

### Geospatial Internet of Things

- SensorUp – SensorUp provides the Cloud hosting and SDKs, based on the Open Geospatial Consortium SensorThings API standard.
