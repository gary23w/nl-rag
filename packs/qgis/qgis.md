---
title: "QGIS"
source: https://en.wikipedia.org/wiki/QGIS
domain: qgis
license: CC-BY-SA-4.0
tags: qgis desktop, open source gis, geospatial software, grass gis
fetched: 2026-07-02
---

# QGIS

**QGIS** is a free and open-source geographic information system (GIS) software. QGIS supports Windows, macOS, and Linux. It supports viewing, editing, printing, and analysis of geospatial data in a range of data formats. Its name comes from an abbreviation of its previous name, Quantum GIS.

## Functionality

QGIS functions as geographic information system (GIS) software, allowing users to analyze and edit spatial information, in addition to composing and exporting graphical maps. QGIS supports raster, vector, mesh, and point cloud layers. Vector data is stored as either point, line, or polygon features. Multiple formats of raster images are supported, and the software can georeference images.

QGIS supports shapefiles, personal geodatabases, dxf, MapInfo, PostGIS, and other industry-standard formats. Web services, including Web Map Service and Web Feature Service, are also supported to allow use of data from external sources.

QGIS integrates with other open-source GIS packages, including PostGIS, GRASS GIS, Felt (GIS company), SAGA GIS, and MapServer. Plugins written in Python or C++ extend QGIS's capabilities. Plugins can geocode using the Google Geocoding API, perform geoprocessing functions similar to those of the standard tools found in ArcGIS, and interface with PostgreSQL/PostGIS, SpatiaLite and MySQL databases.

QGIS is built on top of, and standard installs include, broadly-used open-source GIS format and projection conversion libraries GDAL and proj.

## Development

Gary Sherman began the development of Quantum GIS in early 2002, and it became an incubator project of the Open Source Geospatial Foundation in 2007. Version 1.0 was released in January 2009.

In 2013, along with release of version 2.0 the name was officially changed from *Quantum GIS* to *QGIS* to avoid confusion as both names had been used in parallel.

Written mainly in C++, QGIS makes extensive use of the Qt library. In addition to Qt, required dependencies of QGIS include GEOS and SQLite. GDAL, GRASS GIS, PostGIS, and PostgreSQL are also recommended, as they provide access to additional data formats.

As of 2017, QGIS is available for multiple operating systems including Mac OS X, Linux, Unix, and Microsoft Windows. There are several third-party apps that allow use of QGIS on mobile devices such as QField (Android, iOS and Windows), Mergin Maps (Android, iOS and Windows) and IntraMaps Roam (Windows).

QGIS can also be used as a graphical user interface to GRASS. QGIS has a small install footprint on the host file system compared to commercial GISs and generally requires less RAM and processing power; hence it can be used on older hardware or running simultaneously with other applications where CPU power may be limited.

QGIS is maintained by volunteer developers who regularly release updates and bug fixes. As of 2012, developers have translated QGIS into 48 languages and the application is used internationally in academic and professional environments. Several companies offer support and feature development services.

## Function

QGIS enables users to visualize their data using maps, charts, and diagrams while customizing the presentation with a variety of symbology choices. The capabilities for geographical analysis provided by QGIS include buffer construction, spatial querying, and geoprocessing. For more complex geographical analysis, users can additionally make use of plugins and algorithms. QGIS also makes it simple to share and publish geospatial data as maps, online services, or print maps in a variety of file formats, such as shapefiles, GeoTIFFs, and KML files.

In order to prepare printed map with QGIS, Print Layout is used. It can be used for adding multiple map views, labels, legends, etc.

## Licensing

As a free software application under GNU GPLv2, QGIS can be freely modified to perform different or more specialized tasks. Two examples are the QGIS Browser and QGIS Server applications, which use the same code for data access and rendering, but present different front-end interfaces.

## Adoption

Many public and private organizations have adopted QGIS, including:

- National Security Agency
- National Geospatial-Intelligence Agency
- Austrian state of Vorarlberg
- The Economist
- Swiss cantons of Glarus and Solothurn
- New Zealand's Land Information public service department

## Release history

"LTR" indicates a Long Term Release. Detailed changelogs are available for releases 2.0 and later.

| Version | Codename | Release date | Notes |
|---|---|---|---|
| 0.0.1-alpha |   | 2002–07 | First public release |
| 1.0 | Kore | 2009-01-05 |   |
| 2.0 | Dufour | 2013-09-08 | New vector API, integration of SEXTANTE geoprocessing, symbology and labeling overhaul. Dropped "Quantum" from the name. |
| 3.0 | Girona | 2018-02-23 | Significant rewrite, upgrading to Qt5, PyQt5, and Python 3. |
| 3.2 | Bonn | 2018-06-22 |   |
| 3.4 LTR | Madeira | 2018-10-26 |   |
| 3.6 | Noosa | 2019-02-22 |   |
| 3.8 | Zanzibar | 2019-06-21 |   |
| 3.10 LTR | A Coruña | 2019-10-25 |   |
| 3.12 | Bucureşti | 2020-02-21 |   |
| 3.14 | Pi | 2020-06-19 | New temporal controller. |
| 3.16 LTR | Hannover | 2020-10-23 |   |
| 3.18 | Zürich | 2021-02-19 |   |
| 3.20 | Odense | 2021-06-18 |   |
| 3.22 LTR | Białowieża | 2021-10-22 |   |
| 3.24 | Tisler | 2022-02-18 |   |
| 3.26 | Buenos Aires | 2022-06-17 | Improved pointcloud and 3D support. New profile plotting framework. |
| 3.28 LTR | Firenze | 2022-10-21 |   |
| 3.30 | 's-Hertogenbosch | 2023-03-03 |   |
| 3.32 | Lima | 2023-06-23 |   |
| 3.34 LTR | Prizren | 2023-10-27 |   |
| 3.36 | Maidenhead | 2024-02-23 |   |
| 3.38 | Grenoble | 2024-06-21 |   |
| 3.40 LTR | Bratislava | 2024-10-25 |   |
| 3.42 | Münster | 2025-02-21 |   |
| 3.44 | Solothurn | 2025-06-20 |   |
| 4.0 | Norrköping | 2026-03-06 | major upgrade to Qt6 framework |
