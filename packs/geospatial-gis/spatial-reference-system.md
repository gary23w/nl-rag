---
title: "Spatial reference system"
source: https://en.wikipedia.org/wiki/Spatial_reference_system
domain: geospatial-gis
license: CC-BY-SA-4.0
tags: geospatial gis, spatial analysis, geographic information, digital cartography
fetched: 2026-07-02
---

# Spatial reference system

A **spatial reference system** (**SRS**) or **coordinate reference system** (**CRS**) is a framework used to precisely measure locations on, or relative to, the surface of Earth as coordinates. It is thus the application of the abstract mathematics of coordinate systems and analytic geometry to geographic space. A particular SRS specification (for example, "Universal Transverse Mercator WGS 84 Zone 16N") comprises a choice of Earth ellipsoid, horizontal datum, map projection (except in the geographic coordinate system), origin point, and unit of measure. Thousands of coordinate systems have been specified for use around the world or in specific regions and for various purposes, necessitating transformations between different SRS.

Although they date to the Hellenistic period, spatial reference systems are now a crucial basis for the sciences and technologies of Geoinformatics, including cartography, geographic information systems, surveying, remote sensing, and civil engineering. This has led to their standardization in international specifications such as the EPSG codes and *ISO 19111:2019 Geographic information—Spatial referencing by coordinates*, prepared by ISO/TC 211, also published by the Open Geospatial Consortium as *Abstract Specification, Topic 2: Spatial referencing by coordinate*.

The above refers to locations directly on the surface of the earth. Information on elevation may also be specified, via a vertical reference frame, so-called vertical CRS, or an integrated 3D CRS. Terminology in this area is evolving in line with increasing technical sophistication in measurement.

## Types of systems

The thousands of spatial reference systems used today are based on a few general strategies, which have been defined in the EPSG, ISO, and OGC standards:

**Geographic coordinate system (or geodetic)**

A

spherical coordinate system

measuring locations directly on the Earth (modeled as a

sphere

or

ellipsoid

) using

latitude

(degrees north or south of the

equator

) and

longitude

(degrees west or east of a

prime meridian

).

**Geocentric coordinate system (or Earth-centered Earth-fixed)**

A three-dimensional

cartesian coordinate system

that models the Earth as a three-dimensional object, measuring locations from a center point, usually the

center of mass

of the Earth, along x, y, and z axes aligned with the

equator

and the

prime meridian

. This system is commonly used to track the orbits of

satellites

, because they are based on the center of mass. Thus, this is the internal coordinate system used by

Satellite navigation

systems such as

GPS

to compute locations using

multilateration

.

**Projected coordinate system (or planar, grid)**

A standardized

cartesian coordinate system

that models the surface of Earth (or more commonly, a large region thereof) as a plane, measuring locations from an arbitrary origin point along x and y axes more or less aligned with the cardinal directions. Each of these systems is based on a particular

map projection

to create a planar surface from the curved Earth surface. Such SRSs are generally defined and used strategically in their target regions to minimize the distortions inherent to projections for specific use cases. Common examples include the

Universal transverse mercator

(UTM) and national systems such as the

British National Grid

, and

State Plane Coordinate System

(SPCS).

**Engineering coordinate system (or local, custom)**

A

cartesian coordinate system

(2-D or 3-D) that is created bespoke for a small area, often a single engineering project, over which the curvature of the Earth can be safely approximated as flat without significant distortion. Locations are typically measured directly from an arbitrary origin point using

surveying

techniques. These may or may not be aligned with a standard projected coordinate system.

Local tangent plane coordinates

are a type of local coordinate system used in aviation and marine vehicles.

**Vertical reference frame**

A standard reference system for measuring

elevation

using

vertical datums

, based on

levelling

, a

geoid

model, or a

chart datum

(considering

tides

). This does not carry information about localization of a point on the surface of the earth, but elevation relative to the surface of the earth, importantly including specification of what zero elevation is.

**3D (compound) coordinate system**

Combines a geographic or projected coordinate system with a vertical reference frame to provide a full parametrization of locations on or near the surface of the earth relative to a chosen zero elevation level.

These standards acknowledge that standard reference systems also exist for time (e.g. ISO 8601). These may be combined with a spatial reference system to form a *compound coordinate system* for representing three-dimensional and/or spatio-temporal locations. There are also internal systems for measuring location within the context of an object, such as the rows and columns of pixels in a raster image, Linear referencing measurements along linear features (e.g., highway mileposts), and systems for specifying location within moving objects such as ships. The latter two are often classified as subcategories of engineering coordinate systems.

## Components

The goal of any spatial reference system is to create a common reference frame in which locations can be measured precisely and consistently as coordinates, which can then be shared unambiguously, so that any recipient can identify the same location that was originally intended by the originator. To accomplish this, any coordinate reference system definition needs to be composed of several specifications:

- A coordinate system, an abstract framework for measuring locations. Like any mathematical coordinate system, its definition consists of a measurable space (whether a plane, a three-dimension void, or the surface of an object such as the Earth), an origin point, a set of axis vectors emanating from the origin, and a unit of measure.
- A geodetic datum (horizontal, vertical, or three-dimensional) which binds the abstract coordinate system to the real space of the Earth. A horizontal datum can be defined as a precise reference framework for measuring geographic coordinates (latitude and longitude). Examples include the World Geodetic System and the 1927 and 1983 North American Datum. A datum generally consists of an estimate of the shape of the Earth (usually an ellipsoid), and one or more *anchor points* or *control points*, established locations (often marked by physical monuments) for which the measurement is documented.
- A definition for a projected CRS must also include a choice of map projection to convert the spherical coordinates specified by the datum into cartesian coordinates on a planar surface.

Thus, a CRS definition will typically consist of a "stack" of dependent specifications, as exemplified in the following table:

EPSG code

Name

Ellipsoid

Horizontal datum

CS type

Projection

Origin

Axes

Unit of measure

4326

GCS

WGS 84

GRS 80

WGS 84

ellipsoidal (lat, lon)

—

N/a

equator/prime meridian

equator, prime meridian

degree of arc

26717

UTM

Zone 17N NAD 27

Clarke 1866

NAD 27

cartesian (x,y)

Transverse Mercator: central meridian 81°W, scaled 0.9996

500

km west of (81°W, 0°N)

equator, 81°W meridian

metre

6576

SPCS

Tennessee Zone NAD 83 (2011) ftUS

GRS 80

NAD 83

(2011 epoch)

cartesian (x,y)

Lambert Conformal Conic: center 86°W, 34°20'N, standard parallels 35°15'N, 36°25'N

600

km grid west of center point

grid east at center point, 86°W meridian

US survey foot

## Examples by continent

Examples of systems around the world are:

### Asia

- Chinese Global Navigation Grid Code, China
- Israeli Cassini Soldner, Israel
- Israeli Transverse Mercator, Israel
- Jordan Transverse Mercator, Jordan

### Europe

- British national grid reference system, Britain
- Lambert-93 (fr), the official projection in Metropolitan France
- Hellenic Geodetic Reference System 1987, Greece
- Irish grid reference system, Ireland
- Irish Transverse Mercator, Ireland
- SWEREF 99 (sv), Sweden

### North America

- United States National Grid and State Plane Coordinate System (SPCS), US
- Modified transverse Mercator coordinate system, Canada

### Worldwide

- Universal Transverse Mercator coordinate system
- Lambert conformal conic projection
- International mapcode system
- Military Grid Reference System

## Identifiers

A **Spatial Reference System Identifier** (**SRID**) is a unique value used to unambiguously identify projected, unprojected, and local spatial coordinate system definitions. These coordinate systems form the heart of all GIS applications.

Virtually all major spatial vendors have created their own SRID implementation or refer to those of an authority, such as the EPSG Geodetic Parameter Dataset.

SRIDs are the primary key for the Open Geospatial Consortium (OGC) **spatial_ref_sys** metadata table for the Simple Features for SQL Specification, Versions 1.1 and 1.2, which is defined as follows:

```mw
CREATE TABLE SPATIAL_REF_SYS
(
    SRID      INTEGER   NOT NULL PRIMARY KEY,
    AUTH_NAME CHARACTER VARYING(256),
    AUTH_SRID INTEGER,
    SRTEXT    CHARACTER VARYING(2048)
)
```

In spatially enabled databases (such as IBM Db2, IBM Informix, Ingres, Microsoft SQL Server, MonetDB, MySQL, Oracle RDBMS, Teradata, PostGIS, SQL Anywhere and Vertica), SRIDs are used to uniquely identify the coordinate systems used to define columns of spatial data or individual spatial objects in a spatial column (depending on the spatial implementation). SRIDs are typically associated with a well-known text (WKT) string definition of the coordinate system (SRTEXT, above). Here are two common coordinate systems with their EPSG SRID value followed by their WKT:

UTM, Zone 17N, NAD27 — SRID 2029:

```mw
PROJCS["NAD27(76) / UTM zone 17N",
    GEOGCS["NAD27(76)",
        DATUM["North_American_Datum_1927_1976",
            SPHEROID["Clarke 1866",6378206.4,294.9786982138982,
                AUTHORITY["EPSG","7008"]],
            AUTHORITY["EPSG","6608"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.01745329251994328,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4608"]],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-81],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    AUTHORITY["EPSG","2029"],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH]]
```

WGS84 — SRID 4326

```mw
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.01745329251994328,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]
```

SRID values associated with spatial data can be used to constrain spatial operations — for instance, spatial operations cannot be performed between spatial objects with differing SRIDs in some systems, or trigger coordinate system transformations between spatial objects in others.
