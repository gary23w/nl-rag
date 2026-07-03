---
title: "180th meridian"
source: https://en.wikipedia.org/wiki/180th_meridian
domain: afro-eurasia
license: CC-BY-SA-4.0
tags: afro-eurasia
fetched: 2026-07-03
---

# 180th meridian

The **180th meridian** or **antimeridian** is the meridian 180° both east and west of the prime meridian in a geographical coordinate system. The longitude at this line can be given as either east or west. On Earth, the prime and 180th meridians form a great ellipse that divides the planet into the Western and Eastern Hemispheres.

## Locations

The antimeridian passes mostly through the open waters of the Pacific Ocean but also runs across land in Russia, Fiji, and Antarctica. An important function of this meridian is its use as the basis for the International Date Line, which snakes around national borders to maintain date consistency within the territories of Russia, the United States, Kiribati, Fiji and New Zealand.

Starting at the North Pole of the Earth and heading south to the South Pole, the 180th meridian passes through:

| Coordinates (approximate) | Country, territory or sea | Notes |
|---|---|---|
| 90°0′N 180°0′E﻿ / ﻿90.000°N 180.000°E﻿ / 90.000; 180.000﻿ (Arctic Ocean) | Arctic Ocean | North Pole |
| 71°32′N 180°0′E﻿ / ﻿71.533°N 180.000°E﻿ / 71.533; 180.000﻿ (Russia) | Russia | Chukotka Autonomous Okrug — Wrangel Island |
| 70°58′N 180°0′E﻿ / ﻿70.967°N 180.000°E﻿ / 70.967; 180.000﻿ (Chukchi Sea) | Chukchi Sea |   |
| 68°59′N 180°0′E﻿ / ﻿68.983°N 180.000°E﻿ / 68.983; 180.000﻿ (Russia) | Russia | Chukotka Autonomous Okrug |
| 65°02′N 180°0′E﻿ / ﻿65.033°N 180.000°E﻿ / 65.033; 180.000﻿ (Bering Sea) | Bering Sea |   |
| 52°0′N 180°0′E﻿ / ﻿52.000°N 180.000°E﻿ / 52.000; 180.000﻿ (Amchitka Pass) | Amchitka Pass | Passing just east of Semisopochnoi Island, Alaska,  United States (at 51°57′N 179°47′E﻿ / ﻿51.950°N 179.783°E﻿ / 51.950; 179.783﻿ (Semisopochnoi Island)) |
| 9°24′S 180°0′W﻿ / ﻿9.400°S 180.000°W﻿ / -9.400; -180.000﻿ (Pacific Ocean) | Pacific Ocean | Passing just east of Nukulaelae atoll,  Tuvalu (at 9°25′S 179°52′E﻿ / ﻿9.417°S 179.867°E﻿ / -9.417; 179.867﻿ (Nukulaelae atoll)) Passing just west of the island of Cikobia-i-Lau,  Fiji (at 15°43′S 179°59′W﻿ / ﻿15.717°S 179.983°W﻿ / -15.717; -179.983﻿ (Cikobia)) |
| 16°9′S 180°0′W﻿ / ﻿16.150°S 180.000°W﻿ / -16.150; -180.000﻿ (Fiji) | Fiji | Islands of Vanua Levu, Rabi, Korolevu, and Taveuni |
| 16°59′S 180°0′W﻿ / ﻿16.983°S 180.000°W﻿ / -16.983; -180.000﻿ (Pacific Ocean) | Pacific Ocean | Passing just east of the island of Moala,  Fiji (at 18°33′S 179°57′E﻿ / ﻿18.550°S 179.950°E﻿ / -18.550; 179.950﻿ (Moala)) Passing just west of the island of Totoya,  Fiji (at 19°0′S 179°52′W﻿ / ﻿19.000°S 179.867°W﻿ / -19.000; -179.867﻿ (Totoya)) Passing just east of the island of Matuku,  Fiji (at 19°10′S 179°47′E﻿ / ﻿19.167°S 179.783°E﻿ / -19.167; 179.783﻿ (Matuku)) |
| 60°0′S 180°0′W﻿ / ﻿60.000°S 180.000°W﻿ / -60.000; -180.000﻿ (Southern Ocean) | Southern Ocean |   |
| 78°13′S 180°0′W﻿ / ﻿78.217°S 180.000°W﻿ / -78.217; -180.000﻿ (Antarctica) | Antarctica | Ross Dependency, claimed by  New Zealand |
| 90°0′S 180°0′W﻿ / ﻿90.000°S 180.000°W﻿ / -90.000; -180.000﻿ (Amundsen–Scott South Pole Station) | Antarctica | Amundsen–Scott South Pole Station, South Pole |

The meridian also passes between (but not particularly close to):

- through the Aleutian Island chain of US territory
- the Gilbert Islands and the Phoenix Islands of Kiribati
- North Island and the Kermadec Islands of New Zealand
- the Bounty Islands and the Chatham Islands, also of New Zealand

The only places where roads cross this meridian are in Fiji and Russia. Fiji has several such roads and some buildings very close to it. Russia has three roads in the Chukotka Autonomous Okrug.

## Software representation problems

Many geographic software libraries or data formats project the world to a rectangle; very often this rectangle is split exactly at the 180th meridian. This often makes it non-trivial to do simple tasks (like representing an area, or a line) over the 180th meridian. Some examples:

- The GeoJSON specification strongly suggests splitting geometries so that neither of their parts cross the antimeridian.
- In OpenStreetMap, areas (like the boundary of Russia) are split at the 180th meridian. Navigation is not possible across the 180th meridian with any directions engine, only on one side of it.
- QGIS may present lines and polygons in a wrapped way if they cross the 180th meridian.
- In Google Maps, navigation is not possible within the Taveuni island, Fiji, if crossing the 180th meridian, only if staying on one side of it.
