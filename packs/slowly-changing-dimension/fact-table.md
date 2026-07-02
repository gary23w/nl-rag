---
title: "Fact table"
source: https://en.wikipedia.org/wiki/Fact_table
domain: slowly-changing-dimension
license: CC-BY-SA-4.0
tags: slowly changing dimension, dimension data warehouse, historical tracking, type two dimension, dimensional modeling
fetched: 2026-07-02
---

# Fact table

In data warehousing, a **fact table** consists of the measurements, metrics or facts of a business process. It is located at the center of a star schema or a snowflake schema surrounded by dimension tables. Where multiple fact tables are used, these are arranged as a fact constellation schema. A fact table typically has two types of columns: those that contain facts and those that are a foreign key to dimension tables. The primary key of a fact table is usually a composite key that is made up of all of its foreign keys. Fact tables contain the content of the data warehouse and store different types of measures like additive, non-additive, and semi-additive measures.

Fact tables (usually) provide the additive values that act as independent variables by which dimensional attributes are analyzed. Fact tables are often defined by their grain. The grain of a fact table represents the most atomic level by which the facts may be defined. The grain of a sales fact table might be stated as "sales volume by day by product by store". Each record in this fact table is therefore uniquely defined by a day, product, and store. Other dimensions might be members of this fact table (such as location/region) but these add nothing to the uniqueness of the fact records. These "affiliate dimensions" allow for additional slices of the independent facts but generally provide insights at a higher level of aggregation (a region contains many stores).

## Example

If the business process is sales, then the corresponding fact table will typically contain columns representing both raw facts and aggregations in rows such as:

- *$12,000*, being "sales for New York store for 15-Jan-2005".
- *$34,000*, being "sales for Los Angeles store for 15-Jan-2005"
- *$22,000*, being "sales for New York store for 16-Jan-2005"
- *$21,000*, being "average daily sales for Los Angeles Store for Jan-2005"
- *$65,000*, being "average daily sales for Los Angeles Store for Feb-2005"
- *$33,000*, being "average daily sales for Los Angeles Store for year 2005"

*"Average daily sales"* is a measurement that is stored in the fact table. The fact table also contains foreign keys from the dimension tables, where time series (e.g. dates) and other dimensions (e.g. store location, salesperson, product) are stored.

All foreign keys between fact and dimension tables should be surrogate keys, not reused keys from operational data.

## Measure types

- Additive – measures that can be added across any dimension.
- Non-additive – measures that cannot be added across any dimension.
- Semi-additive – measures that can be added across some dimensions.

A fact table might contain either detail-level facts or facts that have been aggregated (fact tables that contain aggregated facts are often instead called summary tables).

Special care must be taken when handling ratios and percentages. One good design rule is to never store percentages or ratios in fact tables but only calculate these in the data access tool. Thus, only store the numerator and denominator in the fact table, which then can be aggregated, and the aggregated stored values can then be used for calculating the ratio or percentage in the data access tool.

In the real world, it is possible to have a fact table that contains no measures or facts. These tables are called "factless fact tables", or "junction tables".

The *factless fact tables* may be used for modeling many-to-many relationships or for capturing timestamps of events.

## Types of fact tables

There are four fundamental measurement events, which characterize all fact tables.

**Transactional**

A transactional table is the most basic and fundamental. The grain associated with a transactional fact table is usually specified as "one row per line in a transaction", e.g., every line on a receipt. Typically a transactional fact table holds data of the most detailed level, causing it to have a great number of

dimensions

associated with it.

**Periodic snapshots**

The periodic snapshot, as the name implies, takes a "picture of the moment", where the moment could be any defined period of time, e.g. a performance summary of a salesman over the previous month. A periodic snapshot table is dependent on the transactional table, as it needs the detailed data held in the transactional fact table in order to deliver the chosen performance output.

**Accumulating snapshots**

This type of fact table is used to show the activity of a process that has a well-defined beginning and end, e.g., the processing of an order. An order moves through specific steps until it is fully processed. As steps towards fulfilling the order are completed, the associated row in the fact table is updated. An accumulating snapshot table often has multiple date columns, each representing a milestone in the process. Therefore, it's important to have an entry in the associated date dimension that represents a placeholder for an unknown date, as many of the milestone dates are unknown at the time of the creation of the row.

**Temporal snapshots**

By applying

temporal database

theory and modeling techniques the

temporal snapshot fact table

allows to have the equivalent of daily snapshots without really having daily snapshots. It introduces the concept of time Intervals into a fact table, allowing saving a lot of space, optimizing performances while allowing the end user to have the logical equivalent of the "picture of the moment" they are interested in.

### Steps in designing a fact table

Kimball’s dimensional design follows four steps:

1. **Select the business process** to model (e.g., order entry, claims processing).
2. **Declare the grain** – define exactly what a single fact-table row represents; different grains must not be mixed in one table.
3. **Identify the dimensions** that apply to each fact-table row.
4. **Identify the facts (measures)** that are true to the declared grain.

After the grain is declared, choose an appropriate fact-table type (e.g., transaction, periodic snapshot, accumulating snapshot). Measures in a fact table are commonly classified as:

- **Additive** – can be summed across all dimensions (e.g., sales amount).
- **Semi-additive** – additive across some dimensions but not others (e.g., account balance not additive across time).
- **Non-additive** – not summable across any dimension (e.g., ratios); typically computed in queries rather than stored.

*Example (transaction grain, “one row per order line”):*

```mw
SELECT d.calendar_date, SUM(f.sales_amount) AS daily_sales
FROM fact_sales f
JOIN dim_date d    ON f.date_key = d.date_key
JOIN dim_product p ON f.product_key = p.product_key
WHERE p.category = 'Widgets'
GROUP BY d.calendar_date;
```

This aggregate remains valid because the measure is additive and the fact rows share a single declared grain.
