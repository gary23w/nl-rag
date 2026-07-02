---
title: "Pivot table"
source: https://en.wikipedia.org/wiki/Pivot_table
domain: pandas-dataframe
license: CC-BY-SA-4.0
tags: python pandas, pandas dataframe, data analysis python
fetched: 2026-07-02
---

# Pivot table

A **pivot table** is a table of values which are aggregations of groups of individual values from a more extensive table (such as from a database, spreadsheet, or business intelligence program) within one or more discrete categories. The aggregations or summaries of the groups of the individual terms might include sums, averages, counts, or other statistics. A pivot table is the outcome of the statistical processing of tabularized raw data and can be used for decision-making.

Although *pivot table* is a generic term, Microsoft held a trademark on the term in the United States from 1994 to 2020.

## History

In their book *Pivot Table Data Crunching*, Bill Jelen and Mike Alexander refer to Pito Salas as the "father of pivot tables". While working on a concept for a new program that would eventually become Lotus Improv, Salas noted that spreadsheets have patterns of data. A tool that could help the user recognize these patterns would help to build advanced data models quickly. With Improv, users could define and store sets of categories, then change views by dragging category names with the mouse. This core functionality would provide the model for pivot tables.

Lotus Development released Improv in 1991 on the NeXT platform. A few months after the release of Improv, Brio Technology published a standalone Macintosh implementation, called DataPivot (with technology eventually patented in 1999). Borland purchased the DataPivot technology in 1992 and implemented it in their own spreadsheet application, Quattro Pro.

In 1993 the Microsoft Windows version of Improv appeared. Early in 1994 Microsoft Excel 5 brought a new functionality called a "PivotTable" to market. Microsoft further improved this feature in later versions of Excel:

- Excel 97 included a new and improved PivotTable Wizard, the ability to create calculated fields, and new pivot cache objects that allow developers to write Visual Basic for Applications macros to create and modify pivot tables
- Excel 2000 introduced "Pivot Charts" to represent pivot-table data graphically
- Office 365 added the PIVOTBY function to Excel allowing users to create summary of data via a function versus building a Pivot Table.

In 2007 Oracle Corporation made `PIVOT` and `UNPIVOT` operators available in Oracle Database 11g.

## Mechanics

For typical data entry and storage, data usually appear in *flat* tables, meaning that they consist of only columns and rows, as in the following portion of a sample spreadsheet showing data on shirt types:

|   | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Region** | **Gender** | **Style** | **Ship date** | **Units** | **Price** | **Cost** |
| 2 | East | Boy | Tee | 2005-01-31 | 12 | 11.04 | 10.42 |
| 3 | East | Boy | Golf | 2005-01-31 | 12 | 13.00 | 12.60 |
| 4 | East | Boy | Fancy | 2005-01-31 | 12 | 11.96 | 11.74 |
| 5 | East | Girl | Tee | 2005-01-31 | 10 | 11.27 | 10.56 |
| 6 | East | Girl | Golf | 2005-01-31 | 10 | 12.12 | 11.95 |
| 7 | East | Girl | Fancy | 2005-01-31 | 10 | 13.74 | 13.33 |
| 8 | West | Boy | Tee | 2005-01-31 | 11 | 11.44 | 10.94 |
| 9 | West | Boy | Golf | 2005-01-31 | 11 | 12.63 | 11.73 |
| 10 | West | Boy | Fancy | 2005-01-31 | 11 | 12.06 | 11.51 |
| 11 | West | Girl | Tee | 2005-01-31 | 15 | 13.42 | 13.29 |
| 12 | West | Girl | Golf | 2005-01-31 | 15 | 11.48 | 10.67 |
| ⋮ | ... | ... | ... | ... | ... | ... | ... |

While tables such as these can contain many data items, it can be difficult to get summarized information from them. A pivot table can help quickly summarize the data and highlight the desired information. The usage of a pivot table is extremely broad and depends on the situation. The first question to ask is, "What am I seeking?" In the example here, let us ask, "How many *Units* did we sell in each *Region* for every *Ship Date?*":

| Sum of units | Ship date ▼ |   |   |   |   |   |
|---|---|---|---|---|---|---|
| Region ▼ | 2005-01-31 | 2005-02-28 | 2005-03-31 | 2005-04-30 | 2005-05-31 | 2005-06-30 |
| East | 66 | 80 | 102 | 116 | 127 | 125 |
| North | 96 | 117 | 138 | 151 | 154 | 156 |
| South | 123 | 141 | 157 | 178 | 191 | 202 |
| West | 78 | 97 | 117 | 136 | 150 | 157 |
| (blank) |   |   |   |   |   |   |
| **Grand total** | **363** | **435** | **514** | **581** | **622** | **640** |

A pivot table usually consists of *row*, *column* and *data* (or *fact*) fields. In this case, the column is *ship date*, the row is *region* and the data we would like to see is (sum of) *units*. These fields allow several kinds of aggregations, including: sum, average, standard deviation, count, etc. In this case, the total number of units shipped is displayed here using a *sum* aggregation.

## Implementation

Using the example above, the software will find all distinct values for *Region*. In this case, they are: *North*, *South*, *East*, *West*. Furthermore, it will find all distinct values for *Ship date*. Based on the aggregation type, *sum*, it will summarize the fact, the quantities of *Unit*, and display them in a multidimensional chart. In the example above, the first datum is 66. This number was obtained by finding all records where both *Region* was *East* and *Ship Date* was *2005-01-31*, and adding the *Units* of that collection of records (*i.e.*, cells E2 to E7) together to get a final result.

Pivot tables are not created automatically. For example, in Microsoft Excel one must first select all of the data in the original table and then go to the Insert tab and select "Pivot Table" (or "Pivot Chart"). The user then has the option of either inserting the pivot table into an existing sheet or creating a new sheet to house the pivot table. A pivot table field list is provided to the user which lists all the column headers present in the data. For instance, if a table represents sales data of a company, it might include Date of sale, Sales person, Item sold, Color of item, Units sold, Per unit price, and Total price. This makes the data more readily accessible.

| Date of sale | Sales person | Item sold | Color of item | Units sold | Per unit price | Total price |
|---|---|---|---|---|---|---|
| 2013-10-01 | Jones | Notebook | Black | 8 | 25000 | 200000 |
| 2013-10-02 | Prince | Laptop | Red | 4 | 35000 | 140000 |
| 2013-10-03 | George | Mouse | Red | 6 | 850 | 5100 |
| 2013-10-04 | Larry | Notebook | White | 10 | 27000 | 270000 |
| 2013-10-05 | Jones | Mouse | Black | 4 | 700 | 2800 |

The fields that would be created will be visible on the right hand side of the worksheet. By default, the pivot table layout design will appear below this list.

Pivot Table fields are the building blocks of pivot tables. Each of the fields from the list can be dragged on to this layout, which has four options:

1. Filters
2. Columns
3. Rows
4. Values

Some uses of pivot tables are related to the analysis of questionnaires with optional responses but some implementations of pivot tables do not allow these use cases. For example the implementation in LibreOffice Calc since 2012 is not able to process empty cells.

### Filters

Report filter is used to apply a filter to an entire table. For example, if the "Color of Item" field is dragged to this area, then the table constructed will have a report filter inserted above the table. This report filter will have drop-down options (Black, Red, and White in the example above). When an option is chosen from this drop-down list ("Black" in this example), then the table that would be visible will contain only the data from those rows that have the "Color of Item= Black".

### Columns

Column labels are used to apply a filter to one or more columns that have to be shown in the pivot table. For instance if the "Salesperson" field is dragged to this area, then the table constructed will have values from the column "Sales Person", *i.e.*, one will have a number of columns equal to the number of "Salesperson". There will also be one added column of Total. In the example above, this instruction will create five columns in the table — one for each salesperson, and Grand Total. There will be a filter above the data — column labels — from which one can select or deselect a particular salesperson for the pivot table.

This table will not have any numerical values as no numerical field is selected but when it is selected, the values will automatically get updated in the column of "Grand total".

### Rows

Row labels are used to apply a filter to one or more rows that have to be shown in the pivot table. For instance, if the "Salesperson" field is dragged on this area then the other output table constructed will have values from the column "Salesperson", *i.e.*, one will have a number of rows equal to the number of "Sales Person". There will also be one added row of "Grand Total". In the example above, this instruction will create five rows in the table — one for each salesperson, and Grand Total. There will be a filter above the data — row labels — from which one can select or deselect a particular salesperson for the Pivot table.

This table will not have any numerical values, as no numerical field is selected, but when it is selected, the values will automatically get updated in the Row of "Grand Total".

### Values

This usually takes a field that has numerical values that can be used for different types of calculations. However, using text values would also not be wrong; instead of Sum, it will give a count. So, in the example above, if the "Units sold" field is dragged to this area along with the row label of "Salesperson", then the instruction will add a new column, "Sum of units sold", which will have values against each salesperson.

| Row labels | Sum of units sold |
|---|---|
| Jones | 12 |
| Prince | 4 |
| George | 6 |
| Larry | 10 |
| Grand total | 32 |

## Application support

Pivot tables or pivot functionality are an integral part of many spreadsheet applications and some database software, as well as being found in other data visualization tools and business intelligence packages.

### Spreadsheets

- Microsoft Excel supports PivotTables, which can be visualized through PivotCharts.
- Apache POI
- LibreOffice Calc and Openoffice Calc support pivot tables. Prior to version 3.4, this feature was named "DataPilot".
- Calligra Sheets supports pivot tables.
- Google Sheets natively supports pivot tables.
- Numbers, from Apple Inc., gained pivot table support in version 11.2.

### Database support

- PostgreSQL, an object–relational database management system, allows the creation of pivot tables using the *tablefunc* module.
- MariaDB, a MySQL fork, allows pivot tables using the CONNECT storage engine.
- Microsoft Access supports pivot queries under the name "crosstab" query.
- Microsoft SQL Server supports pivot as of SQL Server 2016 with the FROM...PIVOT keywords
- Oracle Database supports the PIVOT operation.
- Some popular databases that do not directly support pivot functionality, such as SQLite, can usually simulate pivot functionality using embedded functions, dynamic SQL or subqueries. The issue with pivoting in such cases is usually that the number of output columns must be known at the time the query starts to execute; for pivoting this is not possible as the number of columns is based on the data itself. Therefore, the names must be hard coded or the query to be executed must itself be created dynamically (meaning, prior to each use) based upon the data.

### Web applications

Several JavaScript UI frameworks and web application libraries provide components for embedding pivot tables in web applications.

- ZK, an Ajax framework, allows embedding pivot tables in web applications.[citation needed]
- Webix, a JavaScript UI library, includes a Pivot component for embedding interactive pivot table functionality in web applications.

### Programming languages and libraries

Programming languages and libraries suited to work with tabular data contain functions that allow the creation and manipulation of pivot tables.

- Python data analysis toolkit pandas has the function `pivot_table` and the `xs` method useful to obtain sections of pivot tables.
- R has the Tidyverse metapackage, which contains a collection of tools providing pivot table functionality, as well as the pivottabler package. The example specific to this article can be implemented in tidyr (in the Tidyverse metapackage) directly via the `pivot_wider` function.

## Online analytical processing

Excel pivot tables include the feature to directly query an online analytical processing (OLAP) server for retrieving data instead of getting the data from an Excel spreadsheet. On this configuration, a pivot table is a simple client of an OLAP server. Excel's PivotTable not only allows for connecting to Microsoft's Analysis Service, but to any XML for Analysis (XMLA) OLAP standard-compliant server.
