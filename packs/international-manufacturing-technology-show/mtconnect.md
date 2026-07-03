---
title: "MTConnect"
source: https://en.wikipedia.org/wiki/MTConnect
domain: international-manufacturing-technology-show
license: CC-BY-SA-4.0
tags: international manufacturing technology show
fetched: 2026-07-03
---

# MTConnect

**MTConnect** is a manufacturing technical standard to retrieve process information from numerically controlled machine tools. As explained by a member of the team that developed it, "This standard specifies the open-source, royalty-free communications protocol based on XML and HTTP Internet technology for real-time data sharing between shopfloor equipment such as machine tools and computer systems. MTConnect provides a common vocabulary with standardized definitions for the meaning of data that machine tools generate, making the data interpretable by software applications." A simple, real-world example of how this tool is used to improve shop management is given by the same author.

## History

The initiative began as a result of lectures given by David Edstrom of Sun Microsystems and David Patterson, professor of Computer Science at the University of California, Berkeley (UCB) at the 2006 annual meeting of the Association for Manufacturing Technology (AMT). The two lectures promoted an open communication standard to enable Internet connectivity to manufacturing equipment. Initial development was carried out by a joint effort between the UCB Electrical Engineering and Computer Sciences (EECS) department, the UCB Mechanical Engineering (ME) department (both in the College of Engineering) and the Georgia Institute of Technology, using input from industry representatives. The resulting standard is available under royalty-free licensing terms.

## Description

MTConnect is a protocol designed for the exchange of data between shop floor equipment and software applications used for monitoring and data analysis. MTConnect is referred to as a read-only standard, meaning that it only defines the extraction (reading) of data from control devices, not the writing of data to a control device. Freely available, open standards are used for all aspects of MTConnect. Data from shop floor devices is presented in XML format, and is retrieved from information providers, called Agents, using Hypertext Transfer Protocol (HTTP) as the underlying transport protocol. MTConnect provides a RESTful interface, which means the interface is stateless. No session must be established to retrieve data from an MTConnect Agent, and no logon or logoff sequence is required (unless overlying security protocols are added which do). Lightweight Directory Access Protocol (LDAP) is recommended for discovery services.

Version 1.0 was released in December 2008.

The first public demonstration of MTConnect occurred at the International Manufacturing Technology Show (IMTS) held in Chicago, Illinois September 2008. There, 25 industrial equipment manufacturers networked their machinery control systems, providing process information that could be retrieved from any web-enabled client connected to the network.

Subsequent demonstrations occurred at EMO (the European machine tool show) in Milan, Italy in October 2009, and the 2010 IMTS in Chicago.

## Standard

The MTConnect standard has three sections. The first section provides information on the protocol and structure of the XML documents via XML schemas. The second section specifies the machine tool components and the description of the available data. The third and last section specifies the organization of the data streams that can be provided from a manufacturing device. The MTConnect Institute is considering adding a fourth section to support mobile assets that include tools and work-holdings.

MTConnect took an incremental approach to defining the requirements for manufacturing device communications. It did not exhaustively define every possible piece of data an application can collect from a manufacturing device, but it works forward from business and research objectives to define the required elements to meet those needs. The standard catalogued important components and data items for metal cutting devices. MTConnect provides an extensible XML schema to allow implementors to add custom data to meet their specific needs, while providing as much commonality as possible.

On September 16, 2010, The MTConnect Institute and the OPC Foundation announced cooperation between the respective organizations.

## Applications

The maintenance cost and losses in productivity with unplanned downtime for machine tool components such as spindle bearings and ball screws could be reduced if one could proactively take action prior to failure. In addition, cutting tools and inserts are expensive to replace when they are still in good condition, but replacing the tools too late can be costly due to scrap and re-work. The proposed health monitoring application will use MTConnect to extract controller data and pattern recognition algorithms to assess the health condition of the spindle and machine tool axes. The health assessment approach is based on running a routine program each shift in which the most recent data patterns are compared to the baseline data patterns. An online tool condition monitoring module is also proposed and uses controller data such as the spindle motor current, with other add on sensors (vibration, acoustic emission) to accurately estimate and predict tool wear. With the added transparency of the machine tool health information, one can take proactive actions before significant downtime or productivity losses occur.
