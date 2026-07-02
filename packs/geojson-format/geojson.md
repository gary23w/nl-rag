---
title: "GeoJSON"
source: https://en.wikipedia.org/wiki/GeoJSON
domain: geojson-format
license: CC-BY-SA-4.0
tags: geojson format, well known binary, spatial data format, simple features
fetched: 2026-07-02
---

# GeoJSON

**GeoJSON** is an open standard format designed for representing simple geographical features, along with their non-spatial attributes. It is based on the JSON format.

The features include points (therefore addresses and locations), line strings (therefore streets, highways and boundaries), polygons (countries, provinces, tracts of land), and multi-part collections of these types. GeoJSON features are not limited to representing entities of the physical world only; mobile routing and navigation apps, for example, might describe their service coverage using GeoJSON.

The GeoJSON format differs from other geographic information system standards in that it was written and is maintained not by a formal standards organization, but by an Internet working group of developers.

A notable offspring of GeoJSON is TopoJSON, an extension of GeoJSON that encodes geospatial topology and that typically provides smaller file sizes.

## History

The GeoJSON format working group and discussion were begun in March 2007 and the format specification was finalized in June 2008.

In April 2015 the Internet Engineering Task Force founded the *Geographic JSON working group* which released GeoJSON as RFC 7946 in August 2016.

## Example

```mw
{
   "type": "FeatureCollection",
   "features": [{
	   "type": "Feature",
	   "geometry": {
		   "type": "Point",
		   "coordinates": [102.0, 0.5]
	   },
	   "properties": {
		   "prop0": "value0"
	   }
   }, {
	   "type": "Feature",
	   "geometry": {
		   "type": "LineString",
		   "coordinates": [
			   [102.0, 0.0],
			   [103.0, 1.0],
			   [104.0, 0.0],
			   [105.0, 1.0]
		   ]
	   },
	   "properties": {
		   "prop0": "value0",
		   "prop1": 0.0
	   }
   }, {
	   "type": "Feature",
	   "geometry": {
		   "type": "Polygon",
		   "coordinates": [
			   [
				   [100.0, 0.0],
				   [101.0, 0.0],
				   [101.0, 1.0],
				   [100.0, 1.0],
				   [100.0, 0.0]
			   ]
		   ]
	   },
	   "properties": {
		   "prop0": "value0",
		   "prop1": {
			   "this": "that"
		   }
	   }
   }]
}
```

GeoJSON example (

map data

)

### Geometries

Points are [x, y] or [x, y, z]. They may be [longitude, latitude] or [eastings, northings]. Elevation, in meters, is an optional third number. They are decimal numbers.

For example, London (51.5074° North, 0.1278° West) is [-0.1278, 51.5074]

The coordinate reference system for all GeoJSON coordinates is a geographic coordinate reference system, using the World Geodetic System 1984 (WGS 84) [WGS84] datum, with longitude and latitude units of decimal degrees.

| Type | Examples |   |
|---|---|---|
| Point |   | { "type": "Point", "coordinates": [30.0, 10.0] } |
| LineString |   | { "type": "LineString", "coordinates": [ [30.0, 10.0], [10.0, 30.0], [40.0, 40.0] ] } |
| Polygon |   | { "type": "Polygon", "coordinates": [ [ [30.0, 10.0], [40.0, 40.0], [20.0, 40.0], [10.0, 20.0], [30.0, 10.0] ] ] } |
|   | { "type": "Polygon", "coordinates": [ [ [35.0, 10.0], [45.0, 45.0], [15.0, 40.0], [10.0, 20.0], [35.0, 10.0] ], [ [20.0, 30.0], [35.0, 35.0], [30.0, 20.0], [20.0, 30.0] ] ] } |   |

| Type | Examples |   |
|---|---|---|
| MultiPoint |   | { "type": "MultiPoint", "coordinates": [ [10.0, 40.0], [40.0, 30.0], [20.0, 20.0], [30.0, 10.0] ] } |
| MultiLineString |   | { "type": "MultiLineString", "coordinates": [ [ [10.0, 10.0], [20.0, 20.0], [10.0, 40.0] ], [ [40.0, 40.0], [30.0, 30.0], [40.0, 20.0], [30.0, 10.0] ] ] } |
| MultiPolygon |   | { "type": "MultiPolygon", "coordinates": [ [ [ [30.0, 20.0], [45.0, 40.0], [10.0, 40.0], [30.0, 20.0] ] ], [ [ [15.0, 5.0], [40.0, 10.0], [10.0, 20.0], [5.0, 10.0], [15.0, 5.0] ] ] ] } |
|   | { "type": "MultiPolygon", "coordinates": [ [ [ [40.0, 40.0], [20.0, 45.0], [45.0, 30.0], [40.0, 40.0] ] ], [ [ [20.0, 35.0], [10.0, 30.0], [10.0, 10.0], [30.0, 5.0], [45.0, 20.0], [20.0, 35.0] ], [ [30.0, 20.0], [20.0, 15.0], [20.0, 25.0], [30.0, 20.0] ] ] ] } |   |
| GeometryCollection |   | { "type": "GeometryCollection", "geometries": [ { "type": "Point", "coordinates": [40.0, 10.0] }, { "type": "LineString", "coordinates": [ [10.0, 10.0], [20.0, 20.0], [10.0, 40.0] ] }, { "type": "Polygon", "coordinates": [ [ [40.0, 40.0], [20.0, 45.0], [45.0, 30.0], [40.0, 40.0] ] ] } ] } |

## Newline-delimited GeoJSON

An alternative to GeoJSON is to encode one geographic feature per line, with line breaks (or record-separator characters) designating the separation between records.

This format can be much faster and more efficient to parse than normal GeoJSON, as tooling can read individual records in parallel. This format is similar to newline-delimited JSON.

Variants of newline-delimited GeoJSON include:

- GeoJSONSeq (short for GeoJSON Text Sequences) - with record-separator (RS) characters separating features
- GeoJSONL (short for GeoJSON Lines) - with newline characters separating features

## TopoJSON

**TopoJSON** is an extension of GeoJSON that encodes topology. Rather than representing geometries discretely, geometries in TopoJSON files are stitched together from shared line segments called *arcs*. *Arcs* are sequences of points, while line strings and polygons are defined as sequences of arcs. Each arc is defined only once, but can be referenced several times by different shapes, thus reducing redundancy and decreasing the file size. In addition, TopoJSON facilitates applications that use topology, such as topology-preserving shape simplification, automatic map coloring, and cartograms.

A reference implementation of the TopoJSON specification is available as a command-line tool to encode TopoJSON from GeoJSON (or ESRI Shapefiles) and a client side JavaScript library to decode TopoJSON back to GeoJSON again. TopoJSON is also supported by the popular OGR tool as of version 1.11 and PostGIS as of version 2.1.0.

### TopoJSON Schema

Given a GIS shape near coordinates latitude 0° and longitude 0°, a simple but valid and complete topojson file containing all metadata, *Polygon*, *LineString*, *Point* elements, *arcs* and *properties* is defined as follows:

```mw
{
  "type":"Topology",
  "transform":{
    "scale": [1,1],
    "translate": [0,0]
  },
  "objects":{ 
    "two-squares":{
      "type": "GeometryCollection",
      "geometries":[
        {"type": "Polygon", "arcs":[[0,1]],"properties": {"name": "Left_Polygon" }},
        {"type": "Polygon", "arcs":[[2,-1]],"properties": {"name": "Right_Polygon" }}
      ]
    },
    "one-line": {
      "type":"GeometryCollection",
      "geometries":[
        {"type": "LineString", "arcs": [3],"properties":{"name":"Under_LineString"}}
      ]
    },
    "two-places":{
      "type":"GeometryCollection",
      "geometries":[
        {"type":"Point","coordinates":[0,0],"properties":{"name":"Origin_Point"}},
        {"type":"Point","coordinates":[0,-1],"properties":{"name":"Under_Point"}}
      ]
    }
  },
  "arcs": [
    [[1,2],[0,-2]],
    [[1,0],[-1,0],[0,2],[1,0]],
    [[1,2],[1,0],[0,-2],[-1,0]],
    [[0,-1],[2,0]]
  ]
}
```
