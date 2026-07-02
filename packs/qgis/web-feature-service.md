---
title: "Web Feature Service"
source: https://en.wikipedia.org/wiki/Web_Feature_Service
domain: qgis
license: CC-BY-SA-4.0
tags: qgis desktop, open source gis, geospatial software, grass gis
fetched: 2026-07-02
---

# Web Feature Service

In computing, the Open Geospatial Consortium **Web Feature Service** (**WFS**) Interface Standard provides an interface allowing requests for geographical features across the web using platform-independent calls. One can think of geographical features as the "source code" behind a map, whereas the WMS interface or online tiled mapping portals like Google Maps return only an image, which end-users cannot edit or spatially analyze. The XML-based Geography Markup Language (GML) furnishes the default payload-encoding for transporting geographic features, but other formats like shapefiles can also serve for transport. In early 2006 the OGC members approved the OpenGIS GML Simple Features Profile. This profile is designed both to increase interoperability between WFS servers and to improve the ease of implementation of the WFS standard.

The OGC membership defined and maintains the WFS specification. Numerous commercial and open-source implementations of the WFS interface standard exist, including the open-source reference implementations GeoServer and deegree. The OGC Implementing Products page provides a comprehensive list of WFS implementations.

## Overview

The WFS specification defines interfaces for describing data manipulation operations of geographic features. Data manipulation operations include the ability to:

- get or query features based on spatial and non-spatial constraints
- create a new feature instance
- delete a feature instance
- update a feature instance

The basic Web Feature Service allows querying and retrieval of features. A transactional Web Feature Service (WFS-T) allows creation, deletion, and updating of features.

A WFS describes discovery, query, or data transformation operations. The client generates the request and posts it to a web feature server using HTTP. The web feature server then executes the request. The WFS specification uses HTTP as the distributed computing platform, although this is not a hard requirement.

There are two encodings defined for WFS operations:

- XML (amenable to HTTP POST, or SOAP)
- Key/value pairs (encoded in HTTP GET query strings, to perform remote procedure calls)

In the taxonomy of Web Services, WFS is best categorized as a non-RESTful RPC type service.

### Communication models

The WFS Web Feature Services or Web Feature Server specification supports two communication models:

- Stateless Request Reply
- Pub/Sub

A messaging system in which clients address messages to a specific node in a content hierarchy, called a topic. Publishers and subscribers are generally anonymous and can dynamically publish or subscribe to the content hierarchy. The system takes care of distributing the messages arriving from a node's multiple publishers to its multiple subscribers. Messages are generally not persistent and will only be received by subscribers who are listening at the time the message is sent. A special case known as a “durable subscription” allows subscribers to receive messages sent while the subscribers are not active. (Source:

Oracle Technology Network for Java Developers | Oracle Technology Network | Oracle

)

The Web Notification Service (WNS) is one of the implementation specifications for the Pub/Sub model. Regardless of the model, URL format is used and specified in the WFS specification. At this time there are no open-standard implementations of WNSs. Vendors plan to release implementations once the standard has been ratified.

### Data

Data passed between a Web Feature Server and a client is encoded with Geography Markup Language (GML), an XML dialect which can be used to model geographic features.

The 1.0.0 version of the WFS specification requires the use of GML version 2.1.2, while the 1.1.0 version of the WFS specification requires the use of GML version 3.1.1. For both versions of the WFS specification, an arbitrary number of other encodings can also be defined, in addition to the required GML 2.1.2 or 3.1.1 format (for 1.0.0 and 1.1.0 respectively).

GML 2.1.2 contains encoding support for basic geometric 'primitives': points, lines, polygons, etc.

GML 3.1.1 contains encoding support for more advanced geometric representations: curves, surfaces, multi-dimensions (time, elevation, multi-band imagery). In addition, GML 3.1.1 includes encoding support for topologically integrated datasets.

## Public Interfaces

### Static Interfaces

The static interface model for the OGC Web Service model appears in the figure below. The Transaction and LockFeature operations are also optional.

When writing a WFS, you must implement the following operations:

- GetCapabilities - this queries the WFS service to determine available options.
- DescribeFeatureType - this retrieves the XML schema to allow the WFS client to parse the resultsets.
- GetFeature - this performs the actual query - parameters such as bounding box and any other filters should be passed in, as appropriate, and the WFS service then returns a GML resultset containing full geometry and feature attributes.

### Dynamic interface updates

The client gets updates by one of two mechanisms:

- Notification: Recommended but not mandatory. Depends on the availability of a WNS implementation.
- Polling: Use this method if a WNS implementation is not available.

**WFS dynamic interface web notification model**

This model uses the OGC Web Notification Service to send update notifications to registered clients.
