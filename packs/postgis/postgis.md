---
title: "PostGIS"
source: https://en.wikipedia.org/wiki/PostGIS
domain: postgis
license: CC-BY-SA-4.0
tags: postgis spatial, spatial database, geometry storage, well known text
fetched: 2026-07-02
---

# PostGIS

**PostGIS** (/ˈpoʊstdʒɪs/ *POST-jis*) is an open source software program that adds support for geographic objects to the PostgreSQL object-relational database. PostGIS follows the Simple Features for SQL specification from the Open Geospatial Consortium (OGC).

PostGIS is implemented as a *PostgreSQL external extension*.

## Features

- Geometry types for Points, LineStrings, Polygons, MultiPoints, MultiLineStrings, MultiPolygons, GeometryCollections, 3D types TINS and polyhedral surfaces, including solids.
- Spheroidal types under the geography datatype Points, LineStrings, Polygons, MultiPoints, MultiLineStrings, MultiPolygons and GeometryCollections.
- raster type - supports various pixel types and more than 1000 bands per raster. Since PostGIS 3, is a separate PostgreSQL extension called postgis_raster.
- SQL/MM Topology support - via PostgreSQL extension postgis_topology.
- Spatial predicates for determining the interactions of geometries using the 3x3 DE-9IM (provided by the GEOS software library).
- Spatial operators for determining geospatial measurements like area, distance, length and perimeter.
- Spatial operators for determining geospatial set operations, like union, difference, symmetric difference and buffers (provided by GEOS).
- R-tree-over-GiST (Generalized Search Tree) spatial indexes for high speed spatial querying.
- Index selectivity support, to provide high performance query plans for mixed spatial/non-spatial queries.

The PostGIS implementation is based on "light-weight" geometries and indexes optimized to reduce disk and memory footprint. Using light-weight geometries helps servers increase the amount of data migrated up from physical disk storage into RAM, improving query performance substantially.

PostGIS is registered as "implements the specified standard" for "Simple Features for SQL" by the OGC. PostGIS has not been certified as compliant by the OGC.

## History

> May of 2001, at that point I was running a small consulting company here in Victoria, working for the provincial government, mostly working in the geospatial field. Because all of our contracts came from the provincial government, we were very tied to the cycle of when they would release and sign contracts. And the government changed that year, so all the civil servants were very risk averse in terms of signing new contract contracts. They didn't know whether what their budget situation was going to be that year. So we ended up having like three months where we got almost no direct revenue. We, you know, didn't all go on vacation for three months. We were kind of young, excited about the field. So we thought, you know, let's see if we can build something to store the spatial data in a database. And we had used Postgres for one of our data processing projects the year previous, so we were kind of familiar with it. And that experimental work in the spring of 2001 ended up being released at the end of May 2001 as PostGIS version 0.1.

— Paul Ramsey (8 September 2023) "Why people care about PostGIS and Postgres" Path To Citus Con

Refractions Research released the first version of PostGIS in 2001 under the GNU General Public License. After six release candidates, a stable "1.0" version followed on 19 April 2005.

In 2006 the OGC registered PostGIS as "implement[ing] the specified standard" for "Simple Features for SQL".

| Release | First release | Latest minor version | Latest release |
|---|---|---|---|
| 1.0 | 2005-04-19 | Unsupported: 1.0.6 | 2005-12-06 |
| 1.1 | 2005-12-21 | Unsupported: 1.1.7 | 2007-01-31 |
| 1.2 | 2006-12-08 | Unsupported: 1.2.1 | 2007-01-11 |
| 1.3 | 2007-08-09 | Unsupported: 1.3.6 | 2009-05-06 |
| 1.4 | 2009-07-24 | Unsupported: 1.4.2 | 2010-03-11 |
| 1.5 | 2010-02-04 | Unsupported: 1.5.8 | 2012-11-15 |
| 2.0 | 2012-04-03 | Unsupported: 2.0.7 | 2015-04-06 |
| 2.1 | 2013-08-17 | Unsupported: 2.1.9 | 2017-09-19 |
| 2.2 | 2015-10-07 | Unsupported: 2.2.8 | 2018-11-22 |
| 2.3 | 2016-09-26 | Unsupported: 2.3.10 | 2019-08-11 |
| 2.4 | 2017-09-30 | Unsupported: 2.4.10 | 2022-04-24 |
| 2.5 | 2018-09-23 | Unsupported: 2.5.9 | 2022-11-12 |
| 3.0 | 2019-10-20 | Supported: 3.0.9 | 2023-05-29 |
| 3.1 | 2020-12-18 | Supported: 3.1.9 | 2023-05-29 |
| 3.2 | 2021-12-18 | Supported: 3.2.5 | 2023-05-29 |
| 3.3 | 2023-05-29 | Supported: 3.3.4 | 2023-07-28 |
| 3.4 | 2023-08-15 | Supported: 3.4.3 | 2024-09-04 |
| 3.5 | 2025-01-18 | Supported: 3.5.2 | 2025-01-18 |
| 3.6 | 2025-09-01 | Latest version: 3.6.0 | 2025-09-01 |

Legend:

Unsupported

Supported

Latest version

Preview version

Future version

## Users

Many software products can use PostGIS as a database backend, including:

- ArcGIS (via GISquirrel, ST-Links SpatialKit, ZigGIS, ArcSDE and other third-party connectors)
- Cadcorp SIS
- Carto
- CockroachDB
- GeoMedia (via third-party connectors)
- GeoServer (GPL)
- GeoNetwork (GPL)
- GRASS GIS (GPL)
- gvSIG (GPL)
- Kosmo (GPL)
- Manifold System
- MapInfo Professional
- Mapnik (LGPL)
- MapServer (BSD)
- Maptitude
- MapGuide (LGPL)
- OpenJUMP (GPL)
- OpenStreetMap
- QGIS (GPL)
- SAGA GIS (GPL)
- TerraLib (LGPL)
- TerraView (GPL)
- uDig (LGPL)
