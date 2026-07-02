---
title: "Keyhole Markup Language"
source: https://en.wikipedia.org/wiki/Keyhole_Markup_Language
domain: geojson-format
license: CC-BY-SA-4.0
tags: geojson format, well known binary, spatial data format, simple features
fetched: 2026-07-02
---

# Keyhole Markup Language

**Keyhole Markup Language** (**KML**) is an XML notation for expressing geographic annotation and visualization within two-dimensional maps and three-dimensional Earth browsers. KML was developed for use with Google Earth, which was originally named Keyhole Earth Viewer. It was created by Keyhole, Inc, which was acquired by Google in 2004. KML became an international standard of the Open Geospatial Consortium in 2008. Google Earth was the first program able to view and graphically edit KML files, but KML support is now available in many GIS software applications, such as Marble, QGIS, and ArcGIS.

## Structure

The KML file specifies a set of features (place marks, images, polygons, 3D models, textual descriptions, etc.) that can be displayed on maps in geospatial software implementing the KML encoding. Every place has a longitude and a latitude. Other data can make a view more specific, such as tilt, heading, or altitude, which together define a "camera view" along with a timestamp or timespan. KML shares some of the same structural grammar as Geography Markup Language (GML). Some KML information cannot be viewed in Google Maps or Mobile.

KML files are very often distributed as **KMZ** files, which are zipped KML files with a .kmz extension. The contents of a KMZ file are a single root KML document and optionally any overlays, images, icons, and COLLADA 3D models referenced in the KML including network-linked KML files. The root KML document by convention is a file named "doc.kml" at the root directory level, which is the file loaded upon opening. By convention the root KML document is at root level and referenced files are in subdirectories (e.g. images for overlay).

An example KML document is:

```mw
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
<Placemark>
  <name>New York City</name>
  <description>New York City</description>
  <Point>
    <coordinates>-74.006393,40.714172,0</coordinates>
  </Point>
</Placemark>
</Document>
</kml>
```

The MIME type associated with KML is *application/vnd.google-earth.kml+xml*; the MIME type associated with KMZ is *application/vnd.google-earth.kmz*.

## Geodetic reference systems in KML

For its reference system, KML uses 3D geographic coordinates: longitude, latitude, and altitude, in that order, with negative values for west, south, and below mean sea level. The longitude/latitude components (decimal degrees) are as defined by the World Geodetic System of 1984 (WGS84). Altitude, the vertical component, is measured in meters from the WGS84 EGM96 Geoid vertical datum. If altitude is omitted from a coordinate string, e.g. (-77.03647, 38.89763) then the default value of 0 (approximately sea level) is assumed for the altitude component, i.e. (-77.03647, 38.89763, 0).

A formal definition of the coordinate reference system (encoded as GML) used by KML is contained in the OGC KML 2.2 Specification. This definition references well-known EPSG CRS components.

## OGC standard process

The KML 2.2 specification was submitted to the Open Geospatial Consortium to assure its status as an open standard for all geobrowsers. In November 2007 a new KML 2.2 Standards Working Group was established within OGC to formalize KML 2.2 as an OGC standard. Comments were sought on the proposed standard until January 4, 2008, and it became an official OGC standard on April 14, 2008.

The OGC KML Standards Working Group finished working on change requests to KML 2.2 and incorporated accepted changes into the KML 2.3 standard. The official OGC KML 2.3 standard was published on August 4, 2015.
