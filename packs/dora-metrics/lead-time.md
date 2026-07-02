---
title: "Lead time"
source: https://en.wikipedia.org/wiki/Lead_time
domain: dora-metrics
license: CC-BY-SA-4.0
tags: dora metrics, deployment frequency lead time, change failure rate, delivery performance measure
fetched: 2026-07-02
---

# Lead time

A **lead time** is the latency between the initiation and completion of a process. For example, the lead time between the placement of an order and delivery of new cars by a given manufacturer might be between two weeks and six months, depending on various particularities. One business dictionary defines "manufacturing lead time" as the total time required to manufacture an item, including order preparation time, queue time, setup time, run time, move time, inspection time, and put-away time. For make-to-order products, it is the time between release of an order and the production and shipment that fulfill that order. For make-to-stock products, it is the time taken from the release of an order to production and receipt into finished goods inventory.

## Supply chain management

A conventional definition of lead time in a supply chain management context is the time from the moment the customer places an order (the moment the supplier learns of the requirement) to the moment it is ready for delivery. In the absence of finished goods or intermediate (work in progress) inventory, it is the time it takes to actually manufacture the order without any inventory other than raw materials. The Chartered Institute of Procurement & Supply identifies "total lead time" as a combination of "internal lead time" (the time required for the buying organization's internal processes to progress from identification of a need to the issue of a purchase order) and "external lead time" (the time required for the supplying organization's processes, including any development required, manufacture, dispatch and delivery). The lead time applicable to material flows within a supply chain may be paralleled by the concept of "information lead time". Mason-Jones and Towill report that reductions in both material flow lead time and information lead time are necessary to secure supply chain performance improvements. Several writers have referred to the importance of "information enriched supply chains" in this context.

## Manufacturing

In the manufacturing environment, lead time has the same definition as that used in supply chain management, but it includes the time required to ship the parts from the supplier. Shipping time is included because the manufacturing company needs to know when the parts will be available for material requirements planning purposes. It is also possible to include within lead time the time it takes for a company to process and have the part ready for manufacturing once it has been received. The time it takes a company to unload a product from a truck, inspect it, and move it into storage ("put-away time") is not trivial. With tight manufacturing constraints or when a company is using Just In Time manufacturing, it is important for supply chain to know how long their own internal processes take.

Lead time consists of:

- Preprocessing Lead Time (also known as "planning time" or "paperwork"): the time required to release a purchase order (if you buy an item) or create a job (if you manufacture an item), from the time you learn of the requirement.
- Processing Lead Time: the time required to procure or manufacture an item.
- Postprocessing Lead Time: the time to make a purchased item available in inventory from the time you receive it (including quarantine, inspection, etc.)

For example, Company A needs a part that can be manufactured in two days once Company B has received an order. It takes three days for company A to receive the part once shipped, and one additional day before the part is ready to go into manufacturing.

- If Company A's Supply Chain calls Company B they will be quoted a lead time of two days for the part.
- If Company A's Manufacturing division asks the Supply Chain division what the lead time is, they will be quoted five days since shipping will be included.
- If a line worker asks the Manufacturing Division boss what the lead time is before the part is ready to be used, it will be six days because setup time will be included.

### Possible ways of shortening lead time

To best meet the customer needs, a company should work towards the shortest possible lead time in manufacturing, production, and delivery. It can be helped by:

- Improving each processing step's efficiency through minimizing waste, quickly resolving any bottlenecks.
- Applying production leveling (Heijunka) to both supply chain management and production process steps.
- Automating all possible actions along the process.
- Reducing the length of the idle (waiting) process stages, as these are often the most wasteful and can be the easiest ones to tackle for a start.

## Order lead time

When talking about Order Lead Time (OLT) it is important to differentiate between the definitions that may exist around this concept. Although they look similar, there are differences between them that help the industry to model the order behavior of their customers. The four definitions are :

- The Actual Order Lead Time (OLTActual) refers to the time which elapses between the receipt of the customer's order (Order Entry Date) and the delivery of the goods."
- The Requested Order Lead Time (OLTRequested) represents the time between the Order Entry Date and the customer requested delivery date; this measurement could help the company to understand the order behavior of the customers and help to design profitable models to fulfill customer needs.
- The Quote Order Lead Time (OLTQuote) is the agreed time between the Order Entry Date and the supplier's committed deliver date of goods as stipulated in a supply chain contract.
- The Confirmed Order Lead Time (OLTConfirmed) represents the time between the Order Entry Date and the by the supplier confirmed delivery date of goods.

### OLT formulas

- OLTRequested = Wish Date – Order Entry Date

The OLTRequested will be determined by the difference between the date the customer wants the material in his facilities (wish date) and the date when they provided its order to the supplier.

- OLTQuote = Quote Date – Order Entry Date

The OLTQuote will be determined by the difference between the date the customer agree to receive the material in their facilities (Quote date) and the date when the order is provided to the supplier.

- OLTActual = Delivery Date – Order Entry Date

The OLTActual will be determined by the difference between the day the provider deliver the material (Delivery date) and the date when they enter the order in the system.

- OLTConfirmed = Confirmed Date – Order Entry Date

The OLTConfirmed will be determined by the difference between the date the confirmed date by the provider to deliver the material in the customer facilities (Confirmed date) and the date when they provide the order to the supplier.

### Average OLT based on volume

The Average OLT based on Volume (OLTV) is the addition of all the multiplications between the volume of product we deliver (quantity) and the OLT divided by the total quantity delivered in the period of time we are studying for that specific facility. $OLTV={\frac {\sum _{j}{Quantity_{j}\cdot OLT_{j}}}{_{TotalQuantityDeliver}}}\,$ By doing this the company will be able to find a relation of volume weighted between the quantities of material required for an order and the time requested to accomplish it. The volume metric could be applied to the 4 types of OLT. The figure obtained from this calculation will be the average time (e.g. in days) between order placing and the requested delivery date of a specific customer under consideration of the average quantities ordered during that particular time.

### Potential application areas for order lead time measurement

The correct analysis of OLT will give the company:

- Better understanding of the market behavior making it able to develop more profitable schemas that fit better with customer needs (Revenue Management).
- Increases company ability to detect and correct any behavior that is not within terms agreed in the contract (by penalization or different contract schema).
- The OLT measurement creates an opportunity area to improve the customer relations by increasing the level of communication with them.

## Project management

In project management, lead time is the time it takes to complete a task or a set of interdependent tasks. The lead of the entire project would be the overall duration of the critical path for the project.

According to the PMBOK (7th edition) by the Project Management Institute (PMI), lead time is the "time between a customer request and the actual delivery." The lead time is a deliverable metric and a customary measure. The lead time shows the amount of elapsed time from a chunk of work or story entering the backlog, to the end of the iteration or release. A smaller lead time means that the process is more effective and the project team is more productive.

Lead time is also the saved time by starting an activity before its predecessor is completed.

According to the PMBOK (7th edition) by PMI, lead is "The amount of time whereby a successor activity can be advanced with respect to a predecessor activity". An example would be scheduling the start of a two-week activity dependent with the finish of the successor activity with a lead of two weeks so they will finish at the same time.

## Other uses

### Journalism

Lead time in publishing describes the amount of time that a journalist has between receiving a writing assignment and submitting the completed piece. This is the production period of a particular publication before releasing it to the public as the issue date. Depending on the publication, lead times can be anything from a couple of hours to many months/years.

### Medicine

Lead time (when referring to a disease) is the length of time between detection of a disease through screening and the moment in time where it would have normally presented with symptoms and led to a diagnosis. An example of this is seen with breast cancer population screening, where women who are asymptomatic have a positive test result with mammography, whereas the underlying disease would have taken many more years to manifest.

### Video games

Lead time in video games can refer to the amount of time certain special, important actions in high-twitch action games, such as using health-recovering items, may need to take in order to be completed successfully. Lead time can be used to prevent players from abusing helpful abilities or items by making them a little more difficult to use safely, requiring some strategy, risk or caution.
