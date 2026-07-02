---
title: "pandas (software)"
source: https://en.wikipedia.org/wiki/Pandas_(software)
domain: pandas-dataframe
license: CC-BY-SA-4.0
tags: python pandas, pandas dataframe, data analysis python
fetched: 2026-07-02
---

# pandas (software)

**Pandas** (styled as **pandas**) is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license. The name is derived from the term "**pan**el **da**ta", an econometrics term for data sets that include observations over multiple time periods for the same individuals, as well as a play on the phrase "Python data analysis". Wes McKinney started building what would become Pandas at AQR Capital while he was a researcher there from 2007 to 2010.

The development of Pandas introduced into Python many comparable features of working with DataFrames that were established in the R programming language. The library is built upon another library, NumPy.

## History

Developer Wes McKinney started working on Pandas in 2008 while at AQR Capital Management out of the need for a high performance, flexible tool to perform quantitative analysis on financial data. Before leaving AQR, he was able to convince management to allow him to open source the library in 2009.

Another AQR employee, Chang She, joined the effort in 2012 as the second major contributor to the library.

In 2015, Pandas signed on as a fiscally sponsored project of NumFOCUS, a 501(c)(3) nonprofit charity in the United States.

## Data model

Pandas is built around data structures called *Series* and *DataFrames*. Data for these collections can be imported from various file formats such as comma-separated values, JSON, Parquet, SQL database tables or queries, and Microsoft Excel.

### Series

A *Series* is a one-dimensional array-like object that stores a sequence of values together with an associated set of labels, called an index. It is built on top of NumPy's array and affords many similar functionalities, but instead of using implicit integer positions, a Series allows explicit index labels of many data types.

A Series can be created from Python lists, dictionaries, or NumPy arrays. If no index is provided, pandas automatically assigns a default integer index ranging from 0 to n-1, where n is the number of items in the Series. A simple example with customized labels is:

```mw
import pandas as pd
ser = pd.Series(['a', 'b', 'c'], index=["x", "y", "z"])
```

To access a value or list of values from a Series, use its index or list of indices:

```mw
ser['x']
ser[['x', 'z']]
```

Series can be used arithmetically, as in the statement `series_3 = series_1 + series_2`. This will align data points with corresponding index values in `series_1` and `series_2` (similar to a join in relational algebra), then add them together to produce new values in `series_3`.

A Series has various attributes, such as `name` (Series name), `dtype` (data type of values), `shape` (number of rows), `values`, and `index`. They can be used in many of the same operations as NumPy arrays, with additional methods for reindexing, label-based selection, and handling missing data.

### DataFrame

A *DataFrame* is a two-dimensional, tabular data structure with labeled rows and columns. Each column is stored internally as a Series and may hold a different data type (numeric, string, boolean, etc.). DataFrames can be created by a variety of means, including dictionaries of lists, NumPy arrays, and external files such as CSV or Excel spreadsheets:

```mw
df1 = pd.Series(['A', 'B', 'C']).to_frame()
df2 = pd.DataFrame({"grade": ["A", "B", "C"], "score": [100, 80, 60]})
df3 = pd.read_csv('path/classgrades.csv')
```

To retrieve a DataFrame column as a Series, use either 1) the index (dict-like notation) or 2) the name of column if the name is a valid Python identifier (attribute-like access). DataFrames support operations such as column assignment, row and column deletion, label-based indexing with `loc`, position-based indexing with `iloc`, reshaping, grouping, and joining. Merge operations implement a subset of relational algebra and allow one-to-one, many-to-one, and many-to-many joins.

Some common attributes of a DataFrame include `dtypes` (data type of each column), `shape` (dimensions of the DataFrame returned as a tuple with form `(number of rows, number of columns)`), `index`/`columns` (labels of the DataFrame's rows/columns, respectively, returned as an Index object), `values` (data in the DataFrame returned as a 2D array), and `empty` (returns `True` if the DataFrame is empty).

### Index

*Index* objects hold metadata for Series and Dataframe objects, such as axis labels and names, and are automatically created from input data. By default, a pandas index is a series of integers ascending from 0, similar to the indices of Python arrays. However, indices can also use any NumPy data type, including floating point, timestamps, or strings. Indices are also immutable, which allows them to be safely shared across multiple objects.

pandas' syntax for mapping index values to relevant data is the same syntax Python uses to map dictionary keys to values. For example, if `s` is a Series, `s['a']` will return the data point at index `a`. Unlike dictionary keys, index values are not guaranteed to be unique. If a Series uses the index value `a` for multiple data points, then `s['a']` will instead return a new Series containing all matching values. A DataFrame's column names are stored and implemented identically to an index. As such, a DataFrame can be thought of as having two indices: one column-based and one row-based. Because column names are stored as an index, these are not required to be unique.

If `data` is a Series, then `data['a']` returns all values with the index value of `a`. However, if `data` is a DataFrame, then `data['a']` returns all values in the column(s) named `a`. To avoid this ambiguity, Pandas supports the syntax `data.loc['a']` as an alternative way to filter using the index. Pandas also supports the syntax `data.iloc[n]`, which always takes an integer *n* and returns the *nth* value, counting from 0. This allows a user to act as though the index is an array-like sequence of integers, regardless of how it is actually defined.

pandas also supports hierarchical indices with multiple values per data point through the "MultiIndex" class. MultiIndex objects allow a single DataFrame to represent multiple dimensions, similar to a pivot table in Microsoft Excel, where each level can optionally carry its own unique name. In practice, data with more than 2 dimensions is often represented using DataFrames with hierarchical indices, instead of the higher-dimension *Panel* and *Panel4D* data structures.

## Functionality

pandas supports a variety of indexing and subsetting techniques, allowing data to be selected by label, index, or Boolean conditions. For example, `df[df['col1'] > 5]` will return all rows in the DataFrame `df` for which the value of the column `col1` exceeds 5. The library also implements grouping operations based on the split-apply-combine approach, enabling users to aggregate, transform, or restructure data according to column values or functions applied to index labels. For example, `df['col1'].groupby(df['col2'])` groups the data in 'col1' by their values in 'col2', while `df.groupby(lambda i: i % 2)` groups all data in the whole DataFrame by whether their index is even.

The library also provides extensive tools for transforming, filtering and summarizing data. Users may apply arbitrary functions to Series and DataFrames, and because the library is built on top of Numpy, most NumPy functions can be applied directly to pandas objects as well. The library also includes built-in operations for arithmetic operations, string processing, and descriptive statistics such as mean, median, and standard deviation. These built-in functions are designed to handle missing data, usually represented by the floating-point value NaN.

In addition, pandas includes tools for reorganizing data into different structural formats, with methods that can reshape tabular data between "wide" and "long" formats and pivot values based on column labels. pandas also implements a flexible set of relational operations for combining datasets. For instance, `merge()` links row in DataFrames based on one or more shared keys or indices, supporting one-to-one, one-to-many, and many-to-many relationships in a manner analogous to join operations in relational databases like SQL. DataFrames can also be concatenated or stacked together along an axis through the `concat()` method, and overlapping data can be further spliced together using `combine_first()` to fill in missing values.

Furthermore, the library includes specialized support for working with time-series data. Features include the ability to interpolate values and filter using a range of timestamps, such as `data['1/1/2023':'2/2/2023']` , which will return all dates between January 1 and February 2. Missing values in time-series data are represented by a dedicated NaT (Not a Timestamp) object, instead of the NaN value it uses elsewhere.

## Criticisms

Pandas has been criticized for its inefficiency. The entire dataset must be loaded in RAM, and the library does not optimize query plans or support parallel computing across multiple cores. Wes McKinney, the creator of Pandas, has recommended Apache Arrow as an alternative to address these performance concerns and other limitations. Otherwise, he says, "my rule of thumb for pandas is that you should have 5 to 10 times as much RAM as the size of your dataset".

## Examples

Pandas is customarily imported as `pd`.

```mw
import numpy as np
import pandas as pd
```

### Example 1: Food & Nutrition

Here's a fake dataset on the nutritional value of various food items:

```mw
df = pd.DataFrame({
    "food": ["Apple", "Banana", "Almonds", "Broccoli", "Salmon", "Oatmeal"],
    "calories": [95, 105, 164, 55, 208, 158],
    "protein_g": [0.5, 1.3, 6.0, 3.7, 22.0, 6.0],
    "carb_g": [25.1, 27.0, 6.4, 11.2, 0.5, 29.3],
    "fat_g": [0.3, 0.4, 14.0, 0.6, 13.0, 3.2],
    "fiber_g": [4.4, 3.1, 3.5, 2.4, 0.0, 4.0],
    "category": ["Fruit", "Fruit", "Nuts", "Vegetable", "Meat", "Grain"]
})
df
```

```mw
        food  calories  protein_g  carb_g  fat_g  fiber_g   category
0      Apple        95        0.5    25.1    0.3      4.4      Fruit
1     Banana       105        1.3    27.0    0.4      3.1      Fruit
2    Almonds       164        6.0     6.4   14.0      3.5       Nuts
3   Broccoli        55        3.7    11.2    0.6      2.4  Vegetable
4     Salmon       208       22.0     0.5   13.0      0.0       Meat
5    Oatmeal       158        6.0    29.3    3.2      4.0      Grain
```

Some possible manipulations and analyses that can be performed:

1. Compute descriptive statistics:df.describe() This provides summaries across numeric columns, including count, mean, standard deviation, and min/max values.
2. Select specific columns:df[["food", "calories"]]
3. Sort foods by calories (descending order):df.sort_values("calories", ascending=False) Note: Any missing values are automatically sorted to the end of the Series.
4. Find nutrient-dense foods (> 3g protein + > 3g fat):df[(df["protein_g"] > 3) & (df["fat_g"] > 3)]
5. Group items by category and calculate average macros:df.groupby("category")[["carb_g", "fat_g", "protein_g"]].mean() This returns a GroupBy object that is analogous to a collection of DataFrames.
6. Find the highest-calorie food per category:df.loc[df.groupby("category")["protein_g"].idxmax()] `idxmax()` returns the index value of the maximum value. `idxmin()` performs an analogous function with the minimum value.
7. Create new columns (macronutrient ratio as a percentage of total calories):df["carb_pct"] = df["carb_g"] * 4 / df["calories"] * 100 df["fat_pct"] = df["fat_g"] * 9 / df["calories"] * 100 df["protein_pct"] = df["protein_g"] * 4 / df["calories"] * 100
8. Handle missing data:df.loc[2, "fiber_g"] = None # Simulate a missing value df["fiber_g"].fillna(df["fiber_g"].mean()) This replaces the `None` value with `NaN`. Alternatively, we can also drop rows containing missing values by calling `df.dropna()`.
9. Merge DataFrames (combine with grocery prices)prices = pd.DataFrame({ "food": ["Apple", "Banana", "Almonds", "Broccoli", "Salmon", "Oatmeal"], "price": [0.7, 0.5, 4.2, 2.0, 10.5, 3.4] }) merged = df.merge(prices, on="food") The `on` keyword specifies the name of the key column by which the two DataFrames will be merged. To merge datasets with different key column names, use the parameters `left_on` and `right_on` instead.
10. Categorize food by calories:df["calorie_level"] = pd.cut( df["calories"], bins=[0,100,200,300], labels=["Low", "Medium", "High"] ) This splits numeric data into separate "bins" or intervals, thereby allowing continuous measurements to be analyzed as discrete categories.

### Example 2: Resampling

Create example time series data, daily:

```mw
periods = 30
days = pd.date_range(start='1 June 2019', periods=periods)
np.random.seed(0)  # Seed the random number generator (RNG)
values = np.random.rand(periods)
s_daily = pd.Series(values, index=days)
print(s_daily)
```

```
2019-06-01    0.548814
2019-06-02    0.715189
2019-06-03    0.602763
                ...   
2019-06-28    0.944669
2019-06-29    0.521848
2019-06-30    0.414662
Freq: D, Length: 30, dtype: float64
```

Resample to weekly ending Monday:

```mw
s_weekly = s_daily.resample('W-Mon').sum()
print(s_weekly)
```

```
2019-06-03    1.866766
2019-06-10    4.290897
2019-06-17    2.992645
2019-06-24    5.500574
2019-07-01    2.782728
Freq: W-MON, dtype: float64
```
