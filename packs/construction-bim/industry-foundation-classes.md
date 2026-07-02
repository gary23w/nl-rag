---
title: "Industry Foundation Classes"
source: https://en.wikipedia.org/wiki/Industry_Foundation_Classes
domain: construction-bim
license: CC-BY-SA-4.0
tags: building information modeling, industry foundation classes, construction management, 4d bim
fetched: 2026-07-02
---

# Industry Foundation Classes

The **Industry Foundation Classes** (**IFC**) is a CAD data exchange data schema intended for description of architectural, building and construction industry data (ABCII). The IFC file format is based on ISO 10303-21 standard and definitions of ABCII are documented by using underlying EXPRESS.

It is a platform-neutral, open data schema specification that is not controlled by a single vendor or group of vendors. It is an object-based data schema with a data model developed by buildingSMART (formerly the International Alliance for Interoperability, IAI) to facilitate interoperability in the architecture, engineering and construction (AEC) industry, and is a commonly used collaboration format in Building information modeling (BIM) based projects. The IFC model specification is open and available. It is registered by ISO and is an official International Standard ISO 16739-1:2024.

Because of its focus on interoperability the Danish government in 2010 made the use of IFC format(s) compulsory for publicly aided building projects. In 2017 the Finnish state-owned facility management company Senate Properties started to demand use of IFC compatible software and BIM in all their projects. Also the Norwegian Government, Health and Defense client organisations require use of IFC BIM in all projects as well as many municipalities, private clients, contractors and designers have integrated IFC BIM in their business. The popularity of the IFC data schema in construction has continued to grow, primarily for the purpose of exchanging geometry.

## History

The IFC initiative began in 1994, when Autodesk formed an industry consortium to advise the company on the development of a set of C++ classes that could support integrated application development. Twelve US companies joined the consortium. These companies included AT&T, HOK Architects, Honeywell, Carrier, Tishman and Butler Manufacturing. Initially named the Industry Alliance for Interoperability, the Alliance opened membership to all interested parties in September, 1995 and changed its name in 1997 to the International Alliance for Interoperability. The new Alliance was reconstituted as a non-profit industry-led organization, with the goal of publishing the Industry Foundation Class (IFC) as a neutral AEC product model responding to the AEC building lifecycle. A further name change occurred in 2005, and the IFC specification is now developed and maintained by buildingSMART.

## IFC specifications

The following IFC specification versions are available:

- IFC4.3 Add2 (2024)
- IFC4.2 (2019-04): withdrawn
- IFC4.1 (2018-86): withdrawn
- IFC4 Add2 TC1 (2017)
- IFC4 Add2 (2016)
- IFC4 Add1 (2015)
- IFC4 (March 2013)
- ifcXML2x3 (June 2007)
- IFC2x3 (February 2006)
- ifcXML2 for IFC2x2 add1 (RC2)
- IFC2x2 Addendum 1 (July 2004)
- ifcXML2 for IFC2x2 (RC1)
- IFC 2x2
- IFC 2x Addendum 1
- ifcXML1 for IFC2x and IFC2x Addendum 1
- IFC 2x
- IFC 2.0 (March 1999)
- IFC 1.5.1 (September 1998)
- IFC 1.5 (November 1997)
- IFC 1.0 (June 1996)

## File formats

IFC defines multiple file formats that may be used, supporting various encodings of the same underlying data.

- IFC-SPF is a text format defined by ISO 10303-21 ("STEP-File"), where each line typically consists of a single object record, and having file extension ".ifc". This is the most widely used IFC format, having the advantage of compact size yet readable text.
- IFC-XML is an XML format defined by ISO 10303-28 ("STEP-XML"), having file extension ".ifcXML". This format is suitable for interoperability with XML tools and exchanging partial building models. Due to the large size of typical building models, this format is less common in practice.
- IFC-ZIP is a ZIP compressed format consisting of an embedded IFC-SPF file or IFC-XML file and having file extension ".ifcZIP".
- IFC-Turtle (Terse RDF Triple Language) is a textual semantic data format that uses RDF and is expressed in the ifcOWL ontology.
- IFC-RDF is a XML-based semantic data format that uses RDF and is expressed in the ifcOWL ontology.
- ifcJSON uses JSON, a modern format often used by web applications.
- ifcHDF uses HDF and is based on the ISO 10303-26 standard for STEP data representation in HDF.

IFC-SPF is in ASCII format which, while human-readable, suffers from common ASCII file issues, in that file-sizes are bloated, files must be read sequentially from start to finish, mid-file extraction is not possible, files are slow to parse, and definitions are non-hierarchical. In addition to ifcXML and ifcZIP, modern data formats include RDF/XML or Turtle (using the ifcOWL ontology), ifcJSON (JavaScript Object Notation, broadly available) and ifcHDF5 (Hierarchical Data Format v5, binary). In 2020, buildingSmart had two JSON projects underway: ifcJSON v4 (a direct mapping from EXPRESS-based IFC v4) and ifcJSON v5, plus a research project experimenting with turning IFC into a binary format.

## Architecture

IFC defines an EXPRESS based entity-relationship model consisting of several hundred entities organized into an object-based inheritance hierarchy. Examples of entities include building elements such as IfcWall, geometry such as IfcExtrudedAreaSolid, and basic constructs such as IfcCartesianPoint.

At the most abstract level, IFC divides all entities into rooted and non-rooted entities. Rooted entities derive from IfcRoot and have a concept of identity (having a GUID), along with attributes for name, description, and revision control. Non-rooted entities do not have identity and instances only exist if referenced from a rooted instance directly or indirectly. IfcRoot is subdivided into three abstract concepts: object definitions, relationships, and property sets:

- IfcObjectDefinition captures tangible object occurrences and types
- IfcRelationship captures relationships among objects
- IfcPropertyDefinition captures dynamically extensible properties about objects.

### IfcObjectDefinition

IfcObjectDefinition is split into object occurrences and object types. IfcObject captures object occurrences such as a product installation having serial number and physical placement. IfcTypeObject captures type definitions (or templates) such as a product type having a particular model number and common shape. Occurrences and types are further subdivided into six fundamental concepts: actors ("who"), controls ("why"), groups ("what"), products ("where"), processes ("when"), and resources ("how").

- IfcActor represents people or organizations.
- IfcControl represents rules controlling time, cost, or scope such as work orders.
- IfcGroup represents collections of objects for particular purpose such as electrical circuits.
- IfcProduct represents occurrences in space such as physical building elements and spatial locations.
- IfcProcess represents occurrences in time such as tasks, events, and procedures.
- IfcResource represents usage of something with limited availability such as materials, labor, and equipment.

### IfcRelationship

IfcRelationship captures relationships among objects. There are five fundamental relationship types: composition, assignment, connectivity, association, and definition.

- IfcRelDecomposes captures a whole-part relationship having exclusive containment such as subdividing a building into floors and rooms or a wall into studs and sheathing.
- IfcRelAssigns captures assignment relationships where one object consumes the services of another object, such as a labor resource assigned to a task, or a task assigned to a building element.
- IfcRelConnects indicates connectivity between objects such as a floor slab connected to a beam or a pipe connected to a sink.
- IfcRelAssociates indicates external references for an object such as an external IFC library file where an object is defined.
- IfcRelDefines indicates an instance-of relationship such as a pipe segment being of a particular type.

### IfcPropertyDefinition

IfcPropertyDefinition captures dynamically extensible property sets. A property set contains one or more properties which may be a single value (e.g. string, number, unit measurement), a bounded value (having minimum and maximum), an enumeration, a list of values, a table of values, or a data structure. While IFC defines several hundred property sets for specific types, custom property sets may be defined by application vendors or end users.

- IfcPropertySet represents a set of properties attached to an object occurrence or object type.
- IfcPropertySetTemplate [IFC2x4] captures definitions of properties and their data types.

### Products

IfcProduct is the base class for all physical objects and is subdivided into spatial elements, physical elements, structural analysis items, and other concepts. Products may have associated materials, shape representations, and placement in space. Spatial elements include IfcSite, IfcBuilding, IfcBuildingStorey, and IfcSpace. Physical building elements include IfcWall, IfcBeam, IfcDoor, IfcWindow, IfcStair, etc. Distribution elements (HVAC, electrical, plumbing) have a concept of ports where elements may have specific connections for various services, and connected together using cables, pipes, or ducts to form a system. Various connectivity relationships are used for building elements such as walls having openings filled by doors or windows.

Materials may be defined for products as a whole, or as layers, profiles, or constituents for specified parts.

- IfcMaterial indicates a specific material, with optional properties (e.g. mechanical, thermal) and styles (e.g. colors, textures).
- IfcMaterialLayerSet captures a list of layers, each indicating a material of a specified thickness.
- IfcMaterialProfileSet [IFC2x4] captures a set of profiles, each indicating a material of a specified cross-section.
- IfcMaterialConstituentSet [IFC2x4] captures a set of constituents, each indicating a material used at a named shape aspect.

Representations may be defined for explicit 3D shape, and optionally as parametric constraints. Each representation is identified by IfcShapeRepresentation with a well-known name.

- 'Body' indicates a 3D shape which may be represented by B-rep, NURBS, Constructive Solid Geometry (CSG), or swept profiles. It may be defined directly or derived by applying material definitions to other representations.
- 'Axis' indicates a path for linear elements (e.g. wall, beam, pipe) for which material profiles or layers are aligned.
- 'FootPrint' indicates a boundary for planar elements (e.g. slab, staircase) for which material layers are bounded.
- 'Profile' indicates a side profile for opening elements (e.g. door, window) for which material constituents are bounded.
- 'SurveyPoints' indicates a set of points for surface elements (e.g. site) for describing contours.

Placement may indicate position, vertical angle, and horizontal angle.

- IfcLocalPlacement indicates placement relative to an enclosing element hierarchy.
- IfcGridPlacement indicates placement relative to a grid with user-defined axes.

Quantities may be defined for take-off purposes such as Gross Area, Gross Volume, Gross Weight, Net Weight, etc. IFC defines various quantities specific to each element type and the method of calculation according to geometry and relationships.

### Processes

IfcProcess is the base class for processes and is subdivided into tasks, events, and procedures. Processes may have durations and be scheduled to occur at specific time periods. Processes may be sequenced such that a successor task may start after a predecessor task finishes, following the critical path method. Processes may be nested into sub-processes for summary roll-up. Processes may be assigned to products indicating the output produced by the work performed.

### Resources

IfcResource is the base class for resources and is subdivided into materials, labor, equipment, subcontracts, crews, and more. Resources may have various costs and calendars of availability. Resources may be nested into sub-resources for granular allocation. Resources may be assigned to processes indicating tasks performed on behalf of a resource.

### Contexts

IfcProject encapsulates an overall project and indicates the project name, description, default units, currency, coordinate system, and other contextual information. A valid IFC file must always include exactly one IfcProject instance, from which all other objects relate directly or indirectly. A project may include multiple buildings, multiple participants, and/or multiple phases according to the particular use.

In addition to project-specific information, an IfcProject may also reference external projects from which shared definitions may be imported such as product types. Each external project is encapsulated using IfcProjectLibrary [IFC2x4] along with IfcRelAssociatesLibrary and IfcLibraryInformation to identify the particular revision of the imported project library.

Projects support revision control where any IfcRoot-based entity has a unique identifier and may be marked as added, modified, deleted, or having no change. Such capability allows multiple IFC files to be merged deterministically, ensuring data integrity without human intervention.
