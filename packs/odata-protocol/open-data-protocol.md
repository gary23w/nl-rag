---
title: "Open Data Protocol"
source: https://en.wikipedia.org/wiki/Open_Data_Protocol
domain: odata-protocol
license: CC-BY-SA-4.0
tags: odata protocol, open data protocol, restful query protocol, queryable rest api
fetched: 2026-07-02
---

# Open Data Protocol

In computing, **Open Data Protocol** (**OData**) is an open protocol that allows the creation and consumption of queryable and interoperable Web service APIs in a standard way. Microsoft initiated OData in 2007. Versions 1.0, 2.0, and 3.0 are released under the Microsoft Open Specification Promise. Version 4.0 was standardized at OASIS, with a release in March 2014. In April 2015 OASIS submitted OData v4 and OData JSON Format v4 to ISO/IEC JTC 1 for approval as an international standard. In December 2016, ISO/IEC published OData 4.0 Core as ISO/IEC 20802-1:2016 and the OData JSON Format as ISO/IEC 20802-2:2016.

The protocol enables the creation and consumption of HTTP-based Web APIs, which allow Web clients to publish and edit resources, identified using URLs and defined in a data model, using simple HTTP messages. OData shares some similarities with JDBC and with ODBC; like ODBC, OData is not limited to relational databases.

## Standardization

After initial development by Microsoft, OData became a standardized protocol of the OASIS OData Technical Committee (TC).

### OASIS OData Technical Committee

> "The OASIS OData TC works to simplify the querying and sharing of data across disparate applications and multiple stakeholders for re-use in the enterprise, Cloud, and mobile devices. A REST-based protocol, OData builds on HTTP, AtomPub, and JSON using URIs to address and access data feed resources. It enables information to be accessed from a variety of sources including (but not limited to) relational databases, file systems, content management systems, and traditional Web sites. OData provides a way to break down data silos and increase the shared value of data by creating an ecosystem in which data consumers can interoperate with data producers in a way that is far more powerful than currently possible, enabling more applications to make sense of a broader set of data. Every producer and consumer of data that participates in this ecosystem increases its overall value."

TC participants include CA Technologies, Citrix Systems, IBM, Microsoft, Progress Software, Red Hat, SAP SE and SDL.

## Architecture

OData is a protocol for the creation and consumption of Web APIs. OData thus builds on HTTP, AtomPub, and JSON using URIs to address and access data feed resources.

### Resource identification

OData uses URIs to identify resources. For every OData service whose service root is abbreviated as *http://host/service/*, the following **fixed** resources can be found:

#### The service document

The service document lists entity sets, functions, and singletons that can be retrieved. Clients can use the service document to navigate the model in a hypermedia-driven fashion.

The service document is available at *http://host/service/*

The metadata document describes the types, sets, functions and actions understood by the OData service. Clients can use the metadata document to understand how to query and interact with entities in the service.

The metadata document is available at *http://host/service/$metadata*.

#### Dynamic resources

The URIs for the dynamic resources may be computed from the hypermedia information in the service document and metadata document

### Resource operation

OData uses the HTTP verbs to indicate the operations on the resources.

- GET: Get the resource (a collection of entities, a single entity, a structural property, a navigation property, a stream, etc.).
- POST: Create a new resource.
- PUT: Update an existing resource by replacing it with a complete instance.
- PATCH: Update an existing resource by replacing part of its properties with a partial instance.
- DELETE: Remove the resource.

### Querying

URLs requested from an OData endpoint may include query options. The OData protocol specifies various 'system query options' endpoints should accept, these can be used to filter, order, map or paginate data.

Query options can be appended to a URL after a `?` character and are separated by `&` characters; each option consists of a `$`-sign prefixed name and its value, separated by a `=` sign, for example: `OData/Products?$top=2&$orderby=Name`. A number of logical operators and functions are defined for use when filtering data, for example: `OData/Products?$filter=Price lt 10.00 and startswith(Name,'M')` requests products with a price smaller than 10 and a name starting with the letter 'M'.

### Resource representation

OData uses different formats for representing data and the data model. In OData protocol version 4.0, JSON format is the standard for representing data, with the Atom format still being in committee specification stage. For representing the data model, the Common Schema Definition Language (CSDL) is used, which defines an XML representation of the entity data model exposed by OData services.

#### A sample OData JSON data payload

A collection of products:

```mw
{
  "@odata.context": "http://services.odata.org/V4/OData/OData.svc/$metadata#Products",
  "value": [
    {
      "ID": 0,
      "Name": "Meat",
      "Description": "Red Meat",
      "ReleaseDate": "1992-01-01T00:00:00Z",
      "DiscontinuedDate": null,
      "Rating": 14,
      "Price": 2.5
    },
    {
      "ID": 1,
      "Name": "Milk",
      "Description": "Low fat milk",
      "ReleaseDate": "1995-10-01T00:00:00Z",
      "DiscontinuedDate": null,
      "Rating": 3,
      "Price": 3.5
    },
    ...
  ]
}
```

#### A sample OData Atom data payload

A collection of products:

```mw
<feed xml:base="http://services.odata.org/V4/OData/OData.svc/" m:context="http://services.odata.org/V4/OData/OData.svc/$metadata#Products" xmlns="http://www.w3.org/2005/Atom" xmlns:d="http://docs.oasis-open.org/odata/ns/data" xmlns:m="http://docs.oasis-open.org/odata/ns/metadata" xmlns:georss="http://www.georss.org/georss" xmlns:gml="http://www.opengis.net/gml">
  <id>http://services.odata.org/v4/odata/odata.svc/Products</id>
  <title type="text">Products</title>
  <updated>2015-05-19T03:38:50Z</updated>
  <link rel="self" title="Products" href="Products"/>
  <entry>
    <id>http://services.odata.org/V4/OData/OData.svc/Products(0)</id>
    <category term="#ODataDemo.Product" scheme="http://docs.oasis-open.org/odata/ns/scheme"/>
    <link rel="edit" title="Product" href="Products(0)"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/Categories" type="application/xml" title="Categories" href="Products(0)/Categories/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/Categories" type="application/atom+xml;type=feed" title="Categories" href="Products(0)/Categories"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/Supplier" type="application/xml" title="Supplier" href="Products(0)/Supplier/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/Supplier" type="application/atom+xml;type=entry" title="Supplier" href="Products(0)/Supplier"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/ProductDetail" type="application/xml" title="ProductDetail" href="Products(0)/ProductDetail/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/ProductDetail" type="application/atom+xml;type=entry" title="ProductDetail" href="Products(0)/ProductDetail"/>
    <title/>
    <updated>2015-05-19T03:38:50Z</updated>
    <author>
      <name/>
    </author>
    <content type="application/xml">
      <m:properties>
        <d:ID m:type="Int32">0</d:ID>
        <d:Name>Bread</d:Name>
        <d:Description>Whole grain bread</d:Description>
        <d:ReleaseDate m:type="DateTimeOffset">1992-01-01T00:00:00Z</d:ReleaseDate>
        <d:DiscontinuedDate m:null="true"/>
        <d:Rating m:type="Int16">4</d:Rating>
        <d:Price m:type="Double">2.5</d:Price>
      </m:properties>
    </content>
  </entry>
  <entry>
    <id>http://services.odata.org/V4/OData/OData.svc/Products(1)</id>
    <category term="#ODataDemo.Product" scheme="http://docs.oasis-open.org/odata/ns/scheme"/>
    <link rel="edit" title="Product" href="Products(1)"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/Categories" type="application/xml" title="Categories" href="Products(1)/Categories/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/Categories" type="application/atom+xml;type=feed" title="Categories" href="Products(1)/Categories"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/Supplier" type="application/xml" title="Supplier" href="Products(1)/Supplier/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/Supplier" type="application/atom+xml;type=entry" title="Supplier" href="Products(1)/Supplier"/>
    <link rel="http://docs.oasis-open.org/odata/ns/relatedlinks/ProductDetail" type="application/xml" title="ProductDetail" href="Products(1)/ProductDetail/$ref"/>
    <link rel="http://docs.oasis-open.org/odata/ns/related/ProductDetail" type="application/atom+xml;type=entry" title="ProductDetail" href="Products(1)/ProductDetail"/>
    <title/>
    <updated>2015-05-19T03:38:50Z</updated>
    <author>
      <name/>
    </author>
    <content type="application/xml">
      <m:properties>
        <d:ID m:type="Int32">1</d:ID>
        <d:Name>Milk</d:Name>
        <d:Description>Low fat milk</d:Description>
        <d:ReleaseDate m:type="DateTimeOffset">1995-10-01T00:00:00Z</d:ReleaseDate>
        <d:DiscontinuedDate m:null="true"/>
        <d:Rating m:type="Int16">3</d:Rating>
        <d:Price m:type="Double">3.5</d:Price>
      </m:properties>
    </content>
  </entry>
  ...
</feed>
```

```mw
<edmx:Edmx Version="4.0" xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx">
  <edmx:DataServices>
    <Schema Namespace="ODataDemo" xmlns="http://docs.oasis-open.org/odata/ns/edm">
      <EntityType Name="Product">
        <Key>
          <PropertyRef Name="ID"/>
        </Key>
        <Property Name="ID" Type="Edm.Int32" Nullable="false"/>
        <Property Name="Name" Type="Edm.String"/>
        <Property Name="Description" Type="Edm.String"/>
        <Property Name="ReleaseDate" Type="Edm.DateTimeOffset" Nullable="false"/>
        <Property Name="DiscontinuedDate" Type="Edm.DateTimeOffset"/>
        <Property Name="Rating" Type="Edm.Int16" Nullable="false"/>
        <Property Name="Price" Type="Edm.Double" Nullable="false"/>
      </EntityType>

      <ComplexType Name="Address">
        <Property Name="Street" Type="Edm.String"/>
        <Property Name="City" Type="Edm.String"/>
        <Property Name="State" Type="Edm.String"/>
        <Property Name="ZipCode" Type="Edm.String"/>
        <Property Name="Country" Type="Edm.String"/>
      </ComplexType>
      
      <EntityContainer Name="DemoService">
        <EntitySet Name="Products" EntityType="ODataDemo.Product"></EntitySet>
      </EntityContainer>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>
```

### Applications

Applications include:

- Progress DataDirect Hybrid Data Pipeline can expose any cloud, big data or relational data sources as OData end points
- Socrata exposes an OData API.
- Microsoft Azure exposes an OData API.
- Oracle Analytics Cloud Archived 2022-08-19 at the Wayback Machine can connect to an OData API
- SAP NetWeaver Gateway provides OData access to SAP Business Suite and SAP Business Warehouse.
- IBM WebSphere eXtreme Scale REST data service can be accessed by any HTTP client using OData.
- Microsoft SharePoint 2010 and up can expose its data as OData endpoint
- Office 365 exposes OData V4.0 APIs.
- Salesforce Connect consumes OData APIs.
- Skyvia Connect exposes cloud and database data via OData
- Tableau can connect to OData APIs.
- TIBCO Spotfire can connect to OData APIs.
- Mulesoft helps integrate with OData APIs.
- SuccessFactors uses OData APIs
- Ceridian HCM's Dayforce uses Odata
- Redfish uses Odata

## Tools

- Nucleon Database Master
