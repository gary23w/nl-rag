---
title: "Journey planner"
source: https://en.wikipedia.org/wiki/Route_planning_software
domain: routing-osrm
license: CC-BY-SA-4.0
tags: osrm routing, route planning, shortest path routing, contraction hierarchies
fetched: 2026-07-02
---

# Journey planner

(Redirected from

Route planning software

)

A **journey planner**, **trip planner**, or **route planner** is a specialized search engine used to find an optimal means of travelling between two or more given locations, sometimes using more than one transport mode. Searches may be optimized on different criteria, for example *fastest*, *shortest*, *fewest changes*, *cheapest*. They may be constrained, for example, to leave or arrive at a certain time, to avoid certain waypoints, etc. A single journey may use a sequence of several modes of transport, meaning the system may know about public transport services as well as transport networks for private transportation.

Trip planning or journey planning is sometimes distinguished from *route planning*, which is typically thought of as using private modes of transportation such as cycling, driving, or walking, normally using a single mode at a time. Trip or journey planning, in contrast, would make use of at least one public transport mode which operates according to published schedules; given that public transport services only depart at specific times (unlike private transport which may leave at any time), an algorithm must therefore not only find a path to a destination, but seek to optimize it so as to minimize the waiting time incurred for each leg. In European Standards such as Transmodel, trip planning is used specifically to describe the planning of a route for a passenger, to avoid confusion with the completely separate process of planning the operational journeys to be made by public transport vehicles on which such trips are made.

Trip planners have been widely used in the travel industry since the 1970s, by booking agents. The growth of the internet, the proliferation of geospatial data, and the development of information technologies generally has led to the rapid development of many self-service app or browser-based, on-line intermodal trip planners.

A trip planner may be used in conjunction with ticketing and reservation systems. As an example, the largest single use of journey planning technology is used in Great Britain in railway booking systems, often referred to as RTJP (Real Time Journey Planner), which processes the data between two or multiple points. This can be viewed on National Rail's official website.

## History

### First-generation systems

In the late 1980s and early 1990s, some national railway operators and major metropolitan transit authorities developed their own specialized trip planners to support their customer enquiry services. These typically ran on mainframes and were accessed internally with terminals by their own staff in customer information centers, call centers, and at ticket counters in order to answer customer queries. The data came from the timetable databases used to publish printed timetables and to manage operations and some included simple route planning capabilities. The HAFAs timetable information system developed in 1989 by the German company Hacon, (now part of Siemens AG) is an example of such a system and was adopted by Swiss Federal Railways (SBB) and Deutsche Bahn in 1989. The "Routes" system of London Transport, now TfL, in use before the development of the on-line planner and covering all public transport services in London, was another example of a mainframe OLTP journey planner and included a large database of tourist attractions and popular destinations in London.

### Second-generation systems

In the 1990s with the advent of personal computers with sufficient memory and processor power to undertake trip planning (which is relatively expensive computationally in terms of memory and processor requirements), systems were developed that could be installed and run on minicomputers and personal computers. The first digital public transport trip planner systems for a microcomputer was developed by Eduard Tulp, an informatica student at the Amsterdam University on an Atari PC. He was hired by the Dutch Railways to build a digital trip planner for the train services. In 1990 the first digital trip planner for the Dutch Railways (on diskette) was sold to be installed on PC's and computers for off-line consultation. The principles of his software program was published in a Dutch university paper in 1991 This was soon expanded to include all public transport in the Netherlands.

Another pioneer was Hans-Jakob Tobler in Switzerland. His product *Finajour*, which ran for PC DOS and MS-DOS was the first electronic timetable for Switzerland . The first published version was sold for the timetable period 1989/1990. Other European countries soon followed with their own journey planners.

A further development of this trend was to deploy trip planners onto even smaller platforms such as mobile devices, a Windows CE version of Hafas was launched in 1998 compressing the application and the entire railway timetable of Deutsche Bahn into six megabytes and running as a stand-alone application.

### Early internet-based systems

The development of the internet allowed HTML based user interfaces to be added to allow direct querying of trip planning systems by the general public. A test web interface for HaFAs, was launched as Deutsche Bahn's official rail trip planner in 1995 and evolved over time into the main Deutsche Bahn website. In 2001 Transport for London launched the world's first large-scale multimodal trip planner for a world city covering all of London's transport modes as well as rail routes to London; this used a trip planning engine supplied by Mentz Gmbh] of Munich after earlier attempts in the late 1990s to add a web interface to TfL's own mainframe internal trip planner failed to scale. Internet trip planners for major transport networks such as national railways and major cities must sustain very high query rates and so require software architectures optimized to sustain such traffic. The world's first mobile trip planner for a large metropolitan area, a WAP based interface to the London using the Mentz engine, was launched in 2001 by London startup company Kizoom Ltd, who also launched the UK's first rail trip planner for the mobile internet in 2000, also as a WAP service, followed by an SMS service. Starting in 2000 the Traveline service provided all parts of the UK with regional multi-modal trip planning on bus, coach, and rail. A web-based trip planner for UK rail was launched by UK National Rail Enquiries in 2003.

Early public transport trip planners typically required a stop or station to be specified for the endpoints. Some also supported inputting the name of a tourist attraction or other popular destination places by keeping a table of the nearest stop to the destination. This was later extended with ability to add addresses or coordinates to offer true point to point planning.

Critical to the development of large-scale multi-modal trip planning in the late 1990s and early 2000s was the development in parallel of standards for encoding stop and schedule data from many different operators and the setting up of workflows to aggregate and distribute data on a regular basis. This is more challenging for modes such as bus and coach, where there tend to a large number of small operators, than for rail, which typically involves only a few large operators who have exchange formats and processes already in place in order to operate their networks. In Europe, which has a dense and sophisticated public transport network, the CEN Transmodel Reference Model for Public Transport was developed to support the process of creating and harmonizing standard formats both nationally and internationally.

### Distributed journey planners

In the 2000s, Several major projects developed distributed trip planning architectures to allow the federation of separate trip planners each covering a specific area to create a composite engine covering a very large area.

- The UK Transport Direct Portal launched in 2004 by the UK Department of Transport, used the JourneyWeb protocol to link eight separate regional engines covering data from 140 local transport authorities in England, Scotland and Wales as a unified engine. The portal integrated both road and public transport planners allowing a comparison between modes of travel times, CO2 footprint etc..
- The German Delfi project developed a distributed trip planning architecture used to federate the German regional planners, launched as a prototype in 2004. The Interface was further developed by the German TRIAS project and led to the development of a CEN Standard [[|Open API for distributed journey planning']] (CEN/TS 17118:2017) published in 2017 to provide a standard interface to trip planners, incorporating features from JourneyWeb and EU-Spirit and making use of the SIRI Protocol Framework and the Transmodel reference model.
- The European EU Spirit project developed a long-distance trip planner between a number of different European regions

### Second-generation internet systems

Public transport trip planners proved to be immensely popular (for example by 2005 Deutsche Bahn was already sustaining 2.8 million requests per day and journey planning sites constitute some of the highest trafficked information sites in every country that has them. The ability to purchase tickets for travel for the journeys found has further increased the utility and popularity of the sites; early implementations such as the UK's Trainline offered delivery of tickets by mail; this has been complemented in most European countries by self-service print and mobile fulfillment methods. Internet trip planners now constitute a primary sales channel for most rail and air transport operators.

Google started to add trip planning capabilities to its product set with a version of Google Transit in 2005, covering trips in the Portland region, as described by the TriMet agency manager Bibiana McHugh. This led to the development of the General Transit Feed Specification (GTFS), a format for collecting transit data for use in trip planners that has been highly influential in developing an ecosystem of PT data feeds covering many different countries. The successful uptake of GTFS as an available output format by large operators in many countries has allowed Google to extend its trip planner coverage to many more regions around the world. The Google Transit trip planning capabilities were integrated into the Google Map product in 2012.

Further evolution of trip planning engines has seen the integration of real time data so that trip plans for the immediate future take into account real time delays and disruptions. The UK National Rail Enquiries added real time to its rail trip planner in 2007. Also significant has been the integration of other types of data into the trip planning results such as disruption notices, crowding levels, CO2 costs, etc. The trip planners of some major metropolitan cities such as the Transport for London trip planner have the ability to dynamically suspend individual stations and whole lines so that modified trip plans are produced during major disruptions that omit the unavailable parts of the network. Another development has been the addition of accessibility data and the ability for algorithms to optimize plans to take into account the requirements of specific disabilities such as wheelchair access.

For the London 2012 Olympics, an enhanced London trip planner was created that allowed the proposed trip results to be biased to manage available capacity across different routes, spreading traffic to less congested routes. Another innovation was the detailed modelling of all the access paths into and out of every Olympic venue, (from PT stop to individual arena entrance) with predicted and actual queueing times to allow for security checks and other delays being factored into the recommended travel times.

An initiative to develop an open source trip planner, OpenTripPlanner, was seeded by Portland, Oregon's transit agency TriMet in 2009 and developed with the participation of agencies and operators in the US and Europe; a full version 1.0 released in September 2016, is making it possible for smaller transit agencies and operators to provide trip planning without paying proprietary license fees.

## Mode-specific considerations

### Public transport routing

A public transport route planner is an intermodal journey planner, typically accessed via the web that provides information about available public transport services. The application prompts a user to input an origin and a destination, and then uses algorithms to find a good route between the two on public transit services. Time of travel may be constrained to either time of departure or arrival and other routing preferences may be specified as well.

An intermodal journey planner supports intermodal journeys i.e. using more than one modes of transport, such as cycling, rapid transit, bus, ferry, etc. Many route planners support door-to-door planning while others only work between stops on the transport network, such as stations, airports or bus stops.

For public transport routing the trip planner is constrained by times of arrival or departure. It may also support different optimization criteria – for example, *fastest route, fewest changes, most accessible*. Optimization by price (*cheapest, most flexible fare*, etc.) is usually done by a separate algorithm or engine, though trip planners that can return fare prices for the trips they find may also offer sorting or filtering of results by price and product type. For long-distance rail and air trip planning, where price is a significant consideration in price optimizing trip planners may suggest the cheapest dates to travel for customers are flexible as to travel time.

### Car routing

The planning of road legs is sometimes done by a separate subsystem within a journey planner, but may consider both single mode trip calculations as well as intermodal scenarios (e.g. Park and Ride, kiss and ride, etc.). Typical optimizations for car routing are *shortest route*, *fastest route*, *cheapest route* and with constraints for specific *waypoints.* The rise of e-mobility poses new challenges to route planning, e.g. sparse charging infrastructure, limited range, and long charging have to be taken into account and offer room for optimization. Some advanced journey planners can take into account average journey times on road sections, or even real-time predicted average journey times on road sections.

### Pedestrian routing

A journey planner will ideally provide detailed routing for pedestrian access to stops, stations, points of interest etc. This will include options to take into account accessibility requirements for different types of users, for example; 'no steps', 'wheelchair access', 'no lifts', etc.

### Bicycle routing

Some journey planning systems can calculate bicycle routes, integrating all paths accessible by bicycle and often including additional information like topography, traffic, on-street cycling infrastructure, etc. These systems assume, or allow the user to specify, preferences for quiet or safe roads, minimal elevation change, bicycle lanes, etc.

## Data requirements

Trip planners depend on a number of different types of data and the quality and extent of this data limits their capability. Some trip planners integrate many different kinds of data from numerous sources. Others may work with one mode only, such as flight itineraries between airports, or using only addresses and the street network for driving directions.

### Contextual data

#### Point of interest data

Passengers don't travel because they want to go to a particular station or stop, but because they want to go some destination of interest, such as a sports arena, tourist attraction, shopping center, park, law court, etc., etc. Many trip planners allow users to look for such "Points of interest", either by name or by category (*museum, stadium, prison,* etc.). Data sets of systematically named, geocoded and categorized popular destinations can be obtained commercially, for example, The UK PointX data set, or derived from opensource data sets such as OpenStreetMap. Major operators such as Transport for London or National Rail have historically had well developed sets of such data for use in their Customer Call centers, along with information on the links to the nearest stops. For points of interest that cover a large area, such as parks, country houses or stadia, a precise geocoding of the entrances is important.

#### Gazetteer data

Trip planning user interfaces can be made more usable by integration of Gazetteer data. This can be associated with stops to assist with stop finding in particular, for example for disambiguation; there are 33 places named Newport in the US and 14 in the UK - a Gazetteer can be used to distinguish which is which and also in some cases to indicate the relationship of transport interchanges with towns and urban centers that passengers are trying to reach - for example only one of London's five or so Airports is actually in London. Data for this purpose typically comes from additional layers in a map data set such as that provided by Esri, Ordnance Survey, Navtech, or specific data sets such as the UK National Public Transport Gazetteer.

### Road data

#### Road network data

Road trip planners, sometimes referred to as route planners, use street and footpath network data to compute a route using simply the network connectivity (i.e. trips may run at any time and not constrained by a timetable). Such data can come from one or more public, commercial or crowdsourced datasets such as TIGER, Esri or OpenStreetMap. The data is fundamental both for computing access legs to reach public transport stops, and to compute road trips in their own right. The fundamental representation is a graph of nodes and edges (i.e. points and links). The data may be further annotated to assist trip planning for different modes;

- Road data may be characterized by road type (highway, major road, minor road, track, etc.), turn restrictions, speed restrictions etc., as well as average travel times at different times of day on different day types (*Weekday, Weekend, Public Holiday,* etc.), so that accurate travel time predictions can be offered
- Cycle road and path data may be annotated with characteristics such as cycle route number, traffic levels, surface, lighting, etc. that affect its usability by cyclists.
- Footpath data may be annotated with accessibility characteristics such as steps, lifts, wheelchair access, ramps, etc., etc., and also safety indicators (e.g., lighting, CCTV, help points, ) so that accessibility constrained trip plans can be computed.

#### Real-time data for roads

Advanced road trip planners take into account the real-time state of the network. They use two main types of feed to do this, obtained from road data services using interfaces such as Datex II or UTMC.

- Situation data, which described the incidents, events and planned roadworks in a structured form that can be related to the network; this is used to decorate trip plans and road maps to show current bottlenecks and incident locations.
- Link traffic flow data, which gives a quantitative measurement of the current flow on each link of the network that is monitored; this can be used to take actual current conditions into account when computing predicted journey times.

### Public transport data

For transit route planners to work, transit schedule data must always be kept up to date. To facilitate data exchange and interoperability between different trip planners, several standard data formats have emerged.

The General Transit Feed Specification, developed in 2006, is now used by hundreds of transit agencies around the world.

In the European Union all public passenger travel operators have the obligation to provide the information under the EU railway timetable data exchange format. In other parts of the world there similar exchange standards.

#### Stop data

The location and identity of public transport access points such as bus, tram and coach stops, stations, airports, ferry landing and ports are fundamental to trip planning and a stop data set is an essential layer of the transport data infrastructure. In order to integrate stops with spatial searches and road routing engines they are geocoded. In order to integrate them with the timetables and routes they are given a unique identifier within the transport network. In order to be recognizable to passengers they are given official names and may also have a public short code (for example the three letter IATA codes for airports) to use in interfaces. Historically, different operators quite often used a different identifier for the same stop and stop numbers were not unique within a country or even a region. Systems for managing stop data, such as the International Union of Railways (UIC) station location code set or the UK's NaPTAN (National Public Transport Access Point) system for stop numbers provide a means of ensuring numbers are unique and the stops are fully described, greatly facilitate the integration of data. Timetable exchange formats, such as GTFS, TransXChange or NeTEx include stop data in their formats and spatial data sets such as OpenStreetMap allow stop identifiers to be geocoded.

#### Public transport network topology data

For public transport networks with a very high frequency of service, such as urban metro cities and inner city bus services, the topology of the network can also be used for route planning, with an average interval being assumed rather than specific departure times. Data on the routes of trains and buses is also useful for providing visualization of results, for example, to plot the route of a train on a map. National mapping bodies, such as the UK's Ordnance Survey typically include a transport layer in their data sets and the European INSPIRE framework includes public transport infrastructure links in its set of strategic digital data. The CEN NeTEx format allows both the physical layer (e.g. road and railway track infrastructure links) and the logical layer (e.g. links between scheduled stopping points on a given line) of the transport infrastructure to be exchanged

In the UK the Online Journey Planner (OJP) is the engine used by National Rail to plan routes, calculate fares and establish ticket availability. OJP obtains its route information from SilverRail's planning engine known as IPTIS (Integrated Passenger Transport Information System). The National Rail website provides information on how businesses can access this data directly via online data feed xml files. However, OJP was switched off in 2023 in favour of a new journey planner which is currently integrated into nationalrail.co.uk.

### Public transport timetables

Data on public transport schedules is used by trip planners to determine the available journeys at specific times. Historically rail data has been widely available in national formats, and many countries also have bus and other mode data in national formats such as VDV 452 (Germany), TransXChange (UK) and Neptune (France). Schedule data is also increasingly becoming available in international formats such as GTFS and NeTEx. To allow a route to be projected onto a map, GTFS allows the specification of a simple shape plot; whilst Transmodel based standards such as CEN NeTEx, TransXChange additionally allow a more detailed representation which can recognize the constituent links and distinguish several different semantic layers.

### Real-time prediction information for public transport

Trip planners may be able to incorporate real-time information into their database and consider them in the selection of optimal routes for travel in the immediate future. Automatic vehicle location (AVL) systems monitor the position of vehicles using GPS systems and can pass on real-time and forecast information to the journey planning system. A trip planner may use a real time interface such as the CEN Service Interface for Real Time Information to obtain this data.

### Situation information

A situation is a software representation of an incident or event that is affecting or is likely to affect the transport network. A trip planner can integrate situation information and use it both to revise its trip planning computations and to annotate its responses so as to inform users through both text and map representations. A trip planner will typically use a standard interface such as SIRI, TPEG or Datex II to obtain situation information.

Incidents are captured through an incident capturing system (ICS) by different operators and stakeholders, for example in transport operator control rooms, by broadcasters or by the emergency services. Text and image information can be combined with the trip result. Recent incidents can be considered within the routing as well as visualized in an interactive map.

## Technology

Typically journey planners use an efficient in-memory representation of the network and timetable to allow the rapid searching of a large number of paths. Database queries may also be used where the number of nodes needed to compute a journey is small, and to access ancillary information relating to the journey. A single engine may contain the entire transport network, and its schedules, or may allow the distributed computation of journeys using a distributed journey planning protocol such as JourneyWeb or Delfi Protocol. A journey planning engine may be accessed by different front ends, using a software protocol or application program interface specialized for journey queries, to provide a user interface on different types of device.

The development of journey planning engines has gone hand in hand with the development of data standards for representing the stops, routes and timetables of the network, such as TransXChange, NaPTAN, Transmodel or GTFS that ensure that these fit together. Journey planning algorithms are a classic example of problems in the field of Computational complexity theory. Real-world implementations involve a tradeoff of computational resources between accuracy, completeness of the answer, and the time required for calculation.

The sub-problem of route planning is an easier problem to solve as it generally involves less data and fewer constraints. However, with the development of "road timetables", associating different journey times for road links at different times of day, time of travel is increasingly relevant for route planners as well.

### Algorithms

Journey planners use a routing algorithm to search a graph representing the transport network. In the simplest case where routing is independent of time, the graph uses (directed) edges to represent street/path segments and nodes to represent intersections. Routing on such a graph can be accomplished effectively using any of a number of routing algorithms such as Dijkstra's, A*, Floyd–Warshall, or Johnson's algorithm. Different weightings such as distance, cost or accessibility may be associated with each edge, and sometimes with nodes.

When time-dependent features such as public transit are included, there are several proposed ways of representing the transport network as a graph and different algorithms may be used such as RAPTOR

### Automated trip planner

Automated trip planners generate your itinerary automatically, based on the information you provide. One way is to submit the desired destination, dates of your trip and interests and the plan will be created in a while. Another way is to provide the necessary information by forwarding confirmation e-mails from airlines, hotels and car rental companies.

### Custom trip planner

With a custom trip planner the user creates one's own travel itinerary individually by picking the appropriate activities from a database. Some of these websites like Triphobo.com offer pre-built databases of points of interest, while others rely on user generated content. A number of community developed trip planners for mobile, such as CoMaps, created route plans from downloaded maps from OpenStreetMap, for use offline.

In 2017, Google released a mobile app called Google Trips. Custom trip planning startups are seeing renewed interest from investors with the advent of data science, AI and voice technologies in 2018. Lola.com, an AI based travel planning startup and Hopper.com have managed to raise significant funding for developing trip planning apps.

When bookings and payments are added to a mobile trip planner app, then the result is considered mobility as a service.

### Commercial software

Many distribution and logistics companies use route planning software as part of their fleet management systems to improve operational efficiency. These systems often integrate GPS tracking and telematics functionality, enabling dispatchers to monitor vehicles in real time, analyze performance through reporting tools, and adjust routes as needed. The goals typically include reducing mileage and idling, cutting fuel consumption, and improving delivery reliability.
