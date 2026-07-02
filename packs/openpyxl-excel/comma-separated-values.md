---
title: "Comma-separated values"
source: https://en.wikipedia.org/wiki/Comma-separated_values
domain: openpyxl-excel
license: CC-BY-SA-4.0
tags: python openpyxl, openpyxl excel, xlsx spreadsheet python
fetched: 2026-07-02
---

# Comma-separated values

**Comma-separated values** (**CSV**) is a plain text data format for storing tabular data where the fields (values) of a record are separated by a comma and each record is a line (i.e. newline separated). CSV is commonly-used in software that generally deals with tabular data such as a database or a spreadsheet. Benefits cited for using CSV include simplicity of use and human readability. CSV is a form of delimiter-separated values. A **CSV file** is a file that contains CSV-formatted data.

CSV is not limited to a particular character encoding but should be and is commonly used with UTF-8, particularly because it does not provide a way to indicate the character encoding.

## History

The CSV format predates personal computers by more than a decade. The IBM Fortran (level H extended) compiler under OS/360 supported list-directed ("free-form") input/output, with commas between values, in 1972. List-directed input/output was defined in FORTRAN 77, approved in 1978. List-directed input used commas or spaces for delimiters, so unquoted character strings could not contain commas or spaces.

The term "comma-separated value" and the "CSV" abbreviation were in use by 1983. The manual for the Osborne Executive computer, which bundled the SuperCalc spreadsheet, documents the CSV quoting convention that allows strings to contain embedded commas.

Comma-separated value lists are easier to type (for example into punched cards) than fixed-column-aligned data, and they were less prone to producing incorrect results if a value was punched one column off from its intended location.

Comma separated files are used for the interchange of database information between machines of two different architectures. The plain-text character of CSV files largely avoids incompatibilities such as byte-order and word size. The files are largely human-readable, so it is easier to deal with them in the absence of perfect documentation or communication.

The main standardization initiative—transforming "*de facto* fuzzy definition" into a more precise and *de jure* one—was in 2005, with RFC 4180, defining CSV as a MIME Content Type. Later, in 2013, some of RFC 4180's deficiencies were tackled by a W3C recommendation.

In 2014 IETF published RFC 7111 describing the application of URI fragments to CSV documents. RFC 7111 specifies how row, column, and cell ranges can be selected from a CSV document using position indexes.

In 2015 W3C, in an attempt to enhance CSV with formal semantics, publicized the first *drafts of recommendations* for CSV metadata standards, which began as *recommendations* in December of the same year.

## Specification

CSV can be informally described as plain text data consisting of one record per line, where each line has the same sequence of fields separated by a comma. For a simple example:

```
id,name,email
1,John,john.doe@example.com
2,Jane,janey72@test.org
```

The format is more formally described in the 2005 technical standard RFC 4180 which codifies the CSV format and defines the MIME type `text/csv` for the handling of text-based fields. Among its requirements:

- A line is terminated per MS-DOS-style: carriage return and line feed (CR/LF) sequence
- A line terminator is optional for the last line
- The data can start with a header record but with no way to test whether the first line is, in fact, a header, care is required when importing
- Each record should contain the same number of fields
- A field containing a comma, double quote or line terminator character should be enclosed in double quotes
- Any field may be enclosed in double quotes
- If a field is enclosed in double quotes, then a double quote embedded in the field must be represented by a sequence of two double quotes

A more complex example, with some of the fields enclosed in double quotes, and fields containing special characters (double quotes, line terminators, commas):

```
Year,Make,Model,Description,Price
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00
1999,Chevy,"Venture ""Extended Edition, Very Large""","",5000.00
1996,Jeep,Grand Cherokee,"MUST SELL!
air, moon roof, loaded",4799.00
```

This example illustrates that a CSV cannot be parsed by naïvely splitting the data by line terminators into lines, and then each line by commas. The above data, when correctly parsed, can be represented as this table:

| Year | Make | Model | Description | Price |
|---|---|---|---|---|
| 1997 | Ford | E350 | ac, abs, moon | 3000.00 |
| 1999 | Chevy | Venture "Extended Edition" |   | 4900.00 |
| 1999 | Chevy | Venture "Extended Edition, Very Large" |   | 5000.00 |
| 1996 | Jeep | Grand Cherokee | MUST SELL! air, moon roof, loaded | 4799.00 |

Common challenges with CSV include:

- Programs may not support line terminator characters within a field even when properly quoted
- Programs may confuse a header line with data or interpret the first data line as a header
- Double quotes in a field may not be parsed correctly

In 2011, Open Knowledge Foundation (OKF) and various partners created a data protocols working group, which later evolved into the Frictionless Data initiative. One of the main formats they released was the Tabular Data Package. Tabular Data package was heavily based on CSV, using it as the main data transport format and adding basic type and schema metadata. (CSV lacks any type information to distinguish the string `1` from the number 1.) The Frictionless Data Initiative has also provided a standard CSV Dialect Description Format for describing different dialects of CSV, for example specifying the field separator or quoting rules.

In 2013, the W3C "CSV on the Web" working group began to specify technologies providing higher interoperability for web applications using CSV or similar formats. The working group completed its work in February 2016 and is officially closed in March 2016 with the release of a set of documents and W3C recommendations for modeling "Tabular Data", and enhancing CSV with metadata and semantics. While the well-formedness of CSV data can readily be checked, testing validity and canonical form is less well developed, relative to more precise data formats, such as XML and SQL, which offer richer types and rules-based validation.

## Applications

CSV is commonly used for data exchange and is widely supported by data-oriented applications. It is often used to move tabular data between programs that natively operate on incompatible data – often in formats that are proprietary or undocumented. A common scenario is moving data from a database to a spreadsheet which, in general, use completely different formats. Most database systems can export as CSV and most spreadsheet programs can import CSV-formatted data, leveraging CSV as an intermediate format. Every major ecommerce platform provides support for exporting data as a CSV file.

CSV is also used for storing data. Common data science tools such as Pandas include the option to export data to CSV for long-term storage. Benefits of CSV for data storage include the simplicity of CSV makes parsing and creating CSV files easy to implement and fast compared to other data formats, human readability making editing or fixing data simpler, and high compressibility leading to smaller data files. Alternatively, CSV does not support more complex data relations and makes no distinction between null and empty values, and in applications where these features are needed other formats are preferred.

More than 200 local, regional, and national data portals, such as those of the UK government and the European Commission, use CSV files with standardized data catalogs.

Some applications use CSV as a data interchange format to enhance its interoperability, exporting and importing CSV. Others use CSV as an internal format. CSV is supported by almost all spreadsheets and database management systems.

Spreadsheets including Apple Numbers, LibreOffice Calc, and Apache OpenOffice Calc. support reading CSV files. Microsoft Excel also supports a dialect of CSV with restrictions in comparison to other spreadsheet software (e.g., as of 2019 Excel still cannot export CSV files in the commonly used UTF-8 character encoding, and separator is not enforced to be the comma). LibreOffice Calc CSV importer is actually a more generic delimited text importer, supporting multiple separators at the same time as well as field trimming.

Various relational databases support saving query results to a CSV file. PostgreSQL provides the `COPY` command, which allows for both saving and loading data to and from a file. `COPY (SELECT * FROM articles) TO '/home/wikipedia/file.csv' (FORMAT csv)` saves the content of a table `articles` to a file called `/home/wikipedia/file.csv`. Some relational databases, when using standard SQL, offer *foreign-data wrapper* (FDW). For example, PostgreSQL offers the `CREATE FOREIGN TABLE` and `CREATE EXTENSION file_fdw` commands to configure any variant of CSV. Databases like Apache Hive offer the option to express CSV or .csv.gz as an internal table format.

Programs that work with CSV may have limits on the maximum number of rows CSV files can have. Examples include Microsoft Excel (1,048,576 rows), Apple Numbers (1,000,000 rows), Google Sheets (10,000,000 cells), and OpenOffice and LibreOffice (1,048,576 rows).
