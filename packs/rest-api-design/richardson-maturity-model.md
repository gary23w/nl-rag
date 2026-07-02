---
title: "Richardson Maturity Model"
source: https://en.wikipedia.org/wiki/Richardson_Maturity_Model
domain: rest-api-design
license: CC-BY-SA-4.0
tags: api design, restful, http api, api guideline, hateoas
fetched: 2026-07-02
---

# Richardson Maturity Model

The **Richardson Maturity Model** (**RMM**) is a maturity model suggested in 2008 by Leonard Richardson which classifies Web APIs based on their adherence and conformity to each of the model's four levels. The aim of the research of the model as stated by the author was to find out the relationship between the constraints of REST and other forms of web services.

It divides the principal parts of RESTful design into three steps: resource identification (URI), HTTP verbs, and hypermedia controls (e.g. hyperlinks).

The RMM has been cited useful in evaluating the quality of particularly RESTful Web API design (even though it is not restricted to REST alone) and criticized for not addressing how a system could achieve the highest maturity levels of the model as well as for considering a limited number of quality attributes.

## Overview

The RMM can be employed to determine how well a Web service architecture adheres to REST principles. It categorizes a Web API into four levels (from 0 to 3) with each higher level corresponding to a more complete adherence to REST design. The next level also contains all the characteristics of the previous one.

Other classification systems for Web API services design also exist, such as CoHA and WS3.

## Levels

### Level 0: The Swamp of POX

The lowest level of the model describes a Web API with a single URI (typically POST over HTTP) accepting all the range of operations supported by the service. Resources in this form cannot be well-defined. Messaging is done in XML, JSON, or other text formats. These are typical RPC POX and many SOAP services.

Level zero systems don't classify as RESTful.

| URI | HTTP verb | Operations |
|---|---|---|
| `/bookingService` | `POST` | retrieve destinations/hotels/rooms; add/cancel a reservation; etc. |
| `/newsFeedService` | `POST` | get all news; get all news in category specified; get all news of an outlet specified; etc. |

### Level 1: Resources

Introduces resources and allows requests for individual URIs (still all typically POST) for separate actions instead of exposing one universal endpoint (API). The API resources are still generalized but it is possible to identify the scope of each one.

Level One design is not RESTful, yet it is organizing the API in the direction of becoming one.

| URI | HTTP verb | Operation |
|---|---|---|
| `/bookingDestinations` | `POST` | retrieve destinations |
| `/bookingReservations` | `POST` | add/cancel reservations |
| `/bookingRooms` | `POST` | add/cancel special requests to a reservation |
| `/bookingFeedback` | `POST` | leave feedback |

### Level 2: HTTP verbs

The system starts making use of HTTP Verbs. This allows for further specialization of the resource and thus narrows down the functionality of each individual operation within the service. The principal separation at this level consists in splitting a given resource into two – one request for obtaining data only (GET), the other for modifying the data (POST). Further granularization is also possible. GET requests only fetch data, POST/PUT calls introduce new and update existing data, and DELETE requests remove or otherwise invalidate previous actions. One drawback of providing a distributed service with more than GET and POST verbs per resource might be growing complexity of using such a system.

| URI | HTTP verb | Operation |
|---|---|---|
| `/destinations` | `GET` | retrieve destinations |
| `/reservations` | `GET` | get reservations according to certain criteria |
| `/reservations` | `POST` | add/cancel reservations |
| `/rooms` | `POST` | request room extras |
| `/rooms` | `DELETE` | remove room extras |

### Level 3: Hypermedia controls

The last level introduces the hypermedia representation. Also called HATEOAS (Hypermedia As The Engine of Application State), these are elements embedded in the response messages of resources which can establish a relation between individual data entities returned from and passed to the APIs. For instance, a GET request to a hotel reservation system might return a number of available rooms along with hypermedia links (these would be html hyperlink controls in the early days of the model) allowing the client to book specific rooms.

This is the last level of the Richardson Maturity Model.

Request:

```mw
 GET /room/?customerId=1&date=10-11-2020&hotelCode=ASTORIA HTTP/1.1
```

Response:

```mw
 {
    "customerId": "1",
    "reservations": [{"room": "102", "checkin": "10-11-2020", "checkout": "11-14-2020", "price": "100", "href": "https://localhost:8080/room/102"}]
 }
```
