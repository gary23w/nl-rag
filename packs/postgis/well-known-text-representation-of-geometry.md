---
title: "Well-known text representation of geometry"
source: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
domain: postgis
license: CC-BY-SA-4.0
tags: postgis spatial, spatial database, geometry storage, well known text
fetched: 2026-07-02
---

# Well-known text representation of geometry

**Well-known text** (**WKT**) is a text markup language for representing vector geometry objects. A binary equivalent, known as **well-known binary** (**WKB**), is used to transfer and store the same information in a more compact form convenient for computer processing but that is not human-readable. The formats were originally defined by the Open Geospatial Consortium (OGC) and described in their Simple Feature Access. The current standard definition is in the ISO/IEC 13249-3:2016 standard.

## Geometric objects

WKT can represent the following distinct geometric objects:

- Point, MultiPoint
- LineString, MultiLineString
- Polygon, MultiPolygon, Triangle
- PolyhedralSurface
- TIN (Triangulated irregular network)
- GeometryCollection

Coordinates for geometries may be 2D (*x*, *y*), 3D (*x*, *y*, *z*), 4D (*x*, *y*, *z*, *m*) with an *m* value that is part of a linear referencing system or 2D with an *m* value (*x*, *y*, *m*). Three-dimensional geometries are designated by a "Z" after the geometry type and geometries with a linear referencing system have an "M" after the geometry type. Empty geometries that contain no coordinates can be specified by using the symbol `EMPTY` after the type name.

WKT geometries are used throughout OGC specifications and are present in applications that implement these specifications. For example, PostGIS contains functions that can convert geometries to and from a WKT representation, making them human readable.

The OGC standard definition requires a polygon to be topologically closed. It also states that if the exterior linear ring of a polygon is defined in a counterclockwise direction, then it will be seen from the "top". Any interior linear rings should be defined in opposite fashion compared to the exterior ring, in this case, clockwise.

| Type | Examples |   |
|---|---|---|
| Point |   | `POINT (30 10)` |
| LineString |   | `LINESTRING (30 10, 10 30, 40 40)` |
| Polygon |   | `POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))` |
|   | `POLYGON ((35 10, 45 45, 15 40, 10 20, 35 10), (20 30, 35 35, 30 20, 20 30))` |   |

| Type | Examples |   |
|---|---|---|
| MultiPoint |   | `MULTIPOINT ((10 40), (40 30), (20 20), (30 10))` |
| `MULTIPOINT (10 40, 40 30, 20 20, 30 10)` |   |   |
| MultiLineString |   | `MULTILINESTRING ((10 10, 20 20, 10 40), (40 40, 30 30, 40 20, 30 10))` |
| MultiPolygon |   | `MULTIPOLYGON (((30 20, 45 40, 10 40, 30 20)), ((15 5, 40 10, 10 20, 5 10, 15 5)))` |
|   | `MULTIPOLYGON (((40 40, 20 45, 45 30, 40 40)), ((20 35, 10 30, 10 10, 30 5, 45 20, 20 35), (30 20, 20 15, 20 25, 30 20)))` |   |
| GeometryCollection |   | `GEOMETRYCOLLECTION (POINT (40 10), LINESTRING (10 10, 20 20, 10 40), POLYGON ((40 40, 20 45, 45 30, 40 40)))` |

The following are some other examples of geometric WKT strings: (Note: Each item below is an individual geometry.)

```mw
GEOMETRYCOLLECTION(POINT(4 6),LINESTRING(4 6,7 10))
POINT ZM (1 1 5 60)
POINT M (1 1 80)
POINT EMPTY
MULTIPOLYGON EMPTY
TRIANGLE((0 0 0,0 1 0,1 1 0,0 0 0))
TIN (((0 0 0, 0 0 1, 0 1 0, 0 0 0)), ((0 0 0, 0 1 0, 1 1 0, 0 0 0)))
POLYHEDRALSURFACE Z ( PATCHES
    ((0 0 0, 0 1 0, 1 1 0, 1 0 0, 0 0 0)),
    ((0 0 0, 0 1 0, 0 1 1, 0 0 1, 0 0 0)),
    ((0 0 0, 1 0 0, 1 0 1, 0 0 1, 0 0 0)),
    ((1 1 1, 1 0 1, 0 0 1, 0 1 1, 1 1 1)),
    ((1 1 1, 1 0 1, 1 0 0, 1 1 0, 1 1 1)),
    ((1 1 1, 1 1 0, 0 1 0, 0 1 1, 1 1 1))
  )
```

## Well-known binary

Well-known binary (WKB) representations are typically shown in hexadecimal strings.

The first byte indicates the byte order for the data:

- `0x00` : big endian
- `0x01` : little endian

The next 4 bytes are a 32-bit unsigned integer for the geometry type, as described below:

| Type | 2D | Z | M | ZM |
|---|---|---|---|---|
| Geometry | `0` | `1000` | `2000` | `3000` |
| Point | `1` | `1001` | `2001` | `3001` |
| LineString | `2` | `1002` | `2002` | `3002` |
| Polygon | `3` | `1003` | `2003` | `3003` |
| MultiPoint | `4` | `1004` | `2004` | `3004` |
| MultiLineString | `5` | `1005` | `2005` | `3005` |
| MultiPolygon | `6` | `1006` | `2006` | `3006` |
| GeometryCollection | `7` | `1007` | `2007` | `3007` |
| CircularString | `8` | `1008` | `2008` | `3008` |
| CompoundCurve | `9` | `1009` | `2009` | `3009` |
| CurvePolygon | `10` | `1010` | `2010` | `3010` |
| MultiCurve | `11` | `1011` | `2011` | `3011` |
| MultiSurface | `12` | `1012` | `2012` | `3012` |
| Curve | `13` | `1013` | `2013` | `3013` |
| Surface | `14` | `1014` | `2014` | `3014` |
| PolyhedralSurface | `15` | `1015` | `2015` | `3015` |
| TIN | `16` | `1016` | `2016` | `3016` |
| Triangle | `17` | `1017` | `2017` | `3017` |
| Circle | `18` | `1018` | `2018` | `3018` |
| GeodesicString | `19` | `1019` | `2019` | `3019` |
| EllipticalCurve | `20` | `1020` | `2020` | `3020` |
| NurbsCurve | `21` | `1021` | `2021` | `3021` |
| Clothoid | `22` | `1022` | `2022` | `3022` |
| SpiralCurve | `23` | `1023` | `2023` | `3023` |
| CompoundSurface | `24` | `1024` | `2024` | `3024` |
| BrepSolid |   | `1025` |   |   |
| AffinePlacement | `102` | `1102` |   |   |

Each data type has a unique data structure, such as the number of points or linear rings, followed by coordinates in 64-bit double numbers.

For example, the geometry `POINT(2.0 4.0)` is represented as: `000000000140000000000000004010000000000000`, where:

- 1-byte integer `00` or 0: big endian
- 4-byte integer `00000001` or 1: POINT (2D)
- 8-byte float `4000000000000000` or 2.0: *x*-coordinate
- 8-byte float `4010000000000000` or 4.0: *y*-coordinate

## Format variations

***EWKT* and *EWKB* – *Extended Well-Known Text/Binary***

A

PostGIS

-specific format that includes the

spatial reference system identifier

(SRID) and up to 4 ordinate values (XYZM).

For example:

SRID

=

4326

;

POINT

(

-

44.3

60.1

)

to locate a longitude/latitude coordinate using the

WGS 84

reference coordinate system. It also supports circular curves, following elements named (but not fully defined) within the original WKT: CircularString, CompoundCurve, CurvePolygon and CompoundSurface.

***AGF Text* – Autodesk Geometry Format**

An extension to

OGC

's Standard (at the time), to include curved elements; most notably used in

MapGuide

.
