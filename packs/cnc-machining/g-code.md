---
title: "G-code"
source: https://en.wikipedia.org/wiki/G-code
domain: cnc-machining
license: CC-BY-SA-4.0
tags: numerical control, g-code, machining, computer-aided manufacturing
fetched: 2026-07-02
---

# G-code

**G-code** (abbreviation for **geometric code**; also called **RS-274**, standardized today in **ISO 6983-1**) is the most widely used computer numerical control (CNC) and 3D printing programming language. It is used mainly in computer-aided manufacturing to control automated machine tools, as well as for 3D-printer slicer applications. G-code has many variants.

G-code instructions are provided to a machine controller (industrial computer) that tells the motors where to move, how fast to move, and what path to follow. The two most common situations are that, within a machine tool such as a lathe or mill, a cutting tool is moved according to these instructions through a toolpath cutting away material to leave only the finished workpiece and/or an unfinished workpiece is precisely positioned in any of up to nine axes around the three dimensions relative to a toolpath and, either or both can move relative to each other. The same concept also extends to noncutting tools such as forming or burnishing tools, photoplotting, additive methods such as 3D printing, and measuring instruments.

## History

The first implementation of a numerical control programming language was developed at the MIT Servomechanisms Laboratory in the 1950s. In the decades that followed, many implementations were developed by numerous organizations, both commercial and noncommercial. Elements of G-code had often been used in these implementations. The first standardized version of G-code used in the United States, *RS-274*, was published in 1963 by the Electronic Industries Alliance (EIA; then known as Electronic Industries Association). In 1974, EIA approved *RS-274-C*, which merged *RS-273* (variable block for positioning and straight cut) and *RS-274-B* (variable block for contouring and contouring/positioning). A final revision of *RS-274* was approved in 1979, as *RS-274-D*. In other countries, the standard *ISO 6983* (finalized in 1982) is often used, but many European countries use other standards. For example, *DIN 66025* is used in Germany, and PN-73M-55256 and PN-93/M-55251 were formerly used in Poland.

From the 1970s to 1990s, many CNC machine tool builders attempted to overcome compatibility difficulties by standardizing on machine tool controllers built by Fanuc. Siemens was another market dominator in CNC controls, especially in Europe. In the 2010s, controller differences and incompatibility were mitigated with the widespread adoption of CAD/CAM applications that could output the appropriate G-code to operate a specific machine through a software tool called a post-processor (sometimes shortened to "post").

## Syntax

G-code began as a limited language that lacked constructs such as loops, conditional operators, and programmer-declared variables with natural-word-including names (or the expressions in which to use them). It was unable to encode logic but was just a way to "connect the dots" where the programmer figured out many of the dots' locations longhand. The latest implementations of G-code include macro language capabilities somewhat closer to a high-level programming language. Additionally, all primary manufacturers (e.g., Fanuc, Siemens Digital Industries Software, Heidenhain) provide access to programmable logic controller (PLC) data, such as axis positioning data and tool data, via variables used by NC programs. These constructs make it easier to develop automation applications.

## Extensions and variations

Extensions and variations have been added independently by control manufacturers and machine tool manufacturers, and operators of a specific controller must be aware of the differences between each manufacturer's product.

One standardized version of G-code, known as *BCL* (Binary Cutter Language), is used only on very few machines. Developed at MIT, BCL was developed to control CNC machines in terms of straight lines and arcs.

Some CNC machines use "conversational" programming, which is a wizard-like programming mode that either hides G-code or completely bypasses the use of G-code. Some popular examples are Okuma's Advanced One Touch (AOT), Southwestern Industries' ProtoTRAK, Mazak's Mazatrol, Hurco's Ultimax and Winmax, Haas' Intuitive Programming System (IPS), and Mori Seiki's CAPS conversational software.
