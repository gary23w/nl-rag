---
title: "Polars (software)"
source: https://en.wikipedia.org/wiki/Polars_(software)
domain: polars
license: CC-BY-SA-4.0
tags: polars dataframe, rust dataframe library, lazy query engine, vectorized execution, lazy evaluation
fetched: 2026-07-02
---

# Polars (software)

**Polars** is an open-source software library for data manipulation. Polars is built with an OLAP query engine implemented in Rust using Apache Arrow Columnar Format as the memory model. Although built using Rust, there are Python, Node.js, R, and SQL API interfaces to use Polars.

As of September 2025, Polars has over 24 million monthly downloads and over 250 million downloads in total.

## History

The initial code commit was on June 23, 2020. Polars started as a "pet project" by Ritchie Vink, who was motivated by the limitations of the software tool pandas that is used to organize and work with data. Vink aimed to address those limitations with a data processing library written in the Rust programming language.

Ritchie Vink and Chiel Peters co-founded a company of the same name to develop Polars, after working together at the company Xomnia for five years. In 2023, Vink and Peters successfully closed a seed round of approximately $4 million, which was led by Bain Capital Ventures.

In September 2025, Vink and Peters raised €18,000,000 (about US$21,000,000) in a Series A round led by Accel, along with Bain Capital Partners and angel investors.

Vink and Peters have also developed other services like Polars Cloud and Polars Distributed that are built around Polars.

## Features

The core object in Polars is the DataFrame, similar to other data processing software libraries. Contexts and expressions are important concepts to Polars' syntax. A context is the specific environment in which an expression is evaluated. Meanwhile, an expression refers to computations or transformations that are performed on data columns.

Polars has three main contexts:

- **selection**: choosing columns from a DataFrame
- **filtering**: subset a DataFrame by keeping rows that meet specified conditions
- **group by/aggregation**: calculating summary statistics within subgroups of the data

Polars was also designed to be "intuitive and [have] concise syntax for data processing tasks".

## Compared with other data processing software

### Compared to pandas

#### Feature differences

Given that Polars was designed to work on a single machine, this prompts many comparisons with the similar data manipulation software, pandas. One big advantage that Polars has over pandas is performance, where Polars is 5 to 10 times faster than pandas on similar tasks. Additionally, pandas requires around 5 to 10 times as much RAM as the size of the dataset, which compares to the 2 to 4 times needed for Polars. These performance increases may be due to Polars being written in Rust and supporting parallel operations.

Polars is also designed to use lazy evaluation (where a query optimizer will use the most efficient evaluation after looking at all steps) compared with pandas using eager evaluation (where steps are performed immediately). Some research on comparing pandas and Polars completing data analysis tasks show that Polars is more memory-efficient than pandas, where "Polars consumes 63% of the energy needed by pandas on the TPC-H benchmark and uses eight times less energy than pandas on synthetic data".

Polars does not have an index for the DataFrame object, which contrasts pandas' use of an index.

#### Syntax differences

Polars and pandas have similar syntax for reading in data using a `read_csv()` method, but have different syntax for calculating a rolling mean.

Code using pandas:

```mw
import pandas as pd

# Read in data
df_temp = pd.read_csv(
    "temp_record.csv", index_col="date", parse_dates=True, dtype={"temp": int}
)

# Explore data
print(df_temp.dtypes)
print(df_temp.head())

# Calculate rolling mean
df_temp.rolling(2).mean()
```

Code using Polars:

```mw
import polars as pl

# Read in data
df_temp = pl.read_csv(
    "temp_record.csv", try_parse_dates=True, dtypes={"temp": int}
).set_sorted("date")

# Explore data
print(df_temp.dtypes)
print(df_temp.head())

# Calculate rolling average
df_temp.rolling("date", period="2d").agg(pl.mean("temp"))
```

### Compared to Dask

Dask is a Python package for applying parallel computation using NumPy, pandas, and scikit-learn, and is used for datasets that are larger than what can fit in memory. Polars is for single-machine use, while Dask is more for distributed computing.

### Compared to DuckDB

DuckDB is an in-process SQL OLAP database system for efficient analytical queries on structured data. Both DuckDB and Polars offer excellent analytical performance, but DuckDB is more SQL-centric for running queries, while Polars is Python-centric.

### Compared to Spark

Apache Spark has a Python API, PySpark, for distributed big data processing. Similar to Dask, Spark is focused on distributed computing, while Polars is for single-machine use. So Polars has an advantage when processing data on a single machine, while Spark may be preferred for larger datasets that don't fit on a single machine.
