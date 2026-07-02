---
title: "Simple Features"
source: https://en.wikipedia.org/wiki/Simple_Features
domain: geojson-format
license: CC-BY-SA-4.0
tags: geojson format, well known binary, spatial data format, simple features
fetched: 2026-07-02
---

# Simple Features

**Simple Features** (officially **Simple Feature Access**) is a set of standards that specify a common storage and access model of geographic features made of mostly two-dimensional geometries (point, line, polygon, multi-point, multi-line, etc.) used by geographic databases and geographic information systems. It is formalized by both the Open Geospatial Consortium (OGC) and the International Organization for Standardization (ISO).

The ISO 19125 standard comes in two parts. Part 1, ISO 19125-1 (SFA-CA for "common architecture"), defines a model for two-dimensional simple features, with linear interpolation between vertices, defined in a hierarchy of classes; this part also defines representation of geometry in text and binary forms. Part 2 of the standard, ISO 19125-2 (SFA-SQL), defines a "SQL/MM" language binding API for SQL under the prefix "ST_". The open access OGC standards cover additionally APIs for CORBA and OLE/COM, although these have lagged behind the SQL one and are not standardized by ISO. There are also adaptations to other languages covered below.

The ISO/IEC 13249-3 SQL/MM Spatial extends the Simple Features data model, originally based on straight-line segments, adding circular interpolations (e.g. circular arcs) and other features like coordinate transformations and methods for validating geometries, as well as Geography Markup Language support.

## Details

### Part 1

The geometries are associated with spatial reference systems. The standard also specifies attributes, methods and assertions with the geometries, in the object-oriented style. In general, a 2D geometry is simple if it contains no self-intersection. The specification defines DE-9IM spatial predicates and several spatial operators that can be used to generate new geometries from existing geometries.

### Part 2

Part 2 is a SQL binding to Part 1, providing a translation of the interface to non-object-oriented environments. For example, instead of a `someGeometryObject.isEmpty()` as in Part 1, SQL/MM uses a `ST_IsEmpty(...)` function in SQL.

### Spatial

The spatial extension adds the datatypes "Circularstring", "CompoundCurve", "CurvePolygon", "PolyhedralSurface", the last of which is also included into the OGC standard. It also defines the SQL/MM versions of these types and operations on them.

## Implementations

Direct implementations of Part 2 (SQL/MM) include:

- MySQL Spatial Extensions. Up to MySQL 5.5, all of the functions that calculate relations between geometries are implemented using bounding boxes not the actual geometries. Starting from version 5.6, MySQL offers support for precise object shapes.
- MonetDB/GIS extension for MonetDB.
- PostGIS extension for PostgreSQL, also supporting some of the SQL/MM Spatial features.
- SpatiaLite extension for SQLite
- Oracle Spatial, which also implements some of the advanced features from SQL/MM Spatial.
- IBM Db2 Spatial Extender and IBM Informix Spatial DataBlade.
- Microsoft SQL Server since version 2008, with significant additions in the 2012 version.
- SAP Sybase IQ.
- SAP HANA as of 1.0 SPS6.

Adaptations include:

- Implementations of the CORBA and OLE/COM interfaces detailed above are mainly produced by commercial vendors maintaining legacy technology.
- R: The sf package implements Simple Features and contains functions that bind to GDAL for reading and writing data, to GEOS for geometrical operations, and to PROJ for projection conversions and datum transformations.
- The GDAL library implements the Simple Features data model in its OGR component.
- The Java-based deegree framework implements SFA (part 1) and various other OGC standards.
- The Rust library geo_types implements geometry primitives that adhere to the simple feature access standards.

GeoSPARQL is an OGC standard that is intended to allow geospatially-linked data representation and querying based on RDF and SPARQL by defining an ontology for geospatial reasoning supporting a small Simple Features (as well as DE-9IM and RCC8) RDFS/OWL vocabulary for GML and WKT literals.

As of 2012, various NoSQL databases had very limited support for "anything more complex than a bounding box or proximity search".
