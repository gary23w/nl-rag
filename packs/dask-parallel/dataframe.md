---
title: "Dask DataFrame"
source: https://docs.dask.org/en/stable/dataframe.html
domain: dask-parallel
license: CC-BY-SA-4.0
tags: python dask, dask parallel computing, parallel dataframe python
fetched: 2026-07-02
---

# Dask DataFrame

# Dask DataFrame

Dask DataFrame helps you process large tabular data by parallelizing pandas, either on your laptop for larger-than-memory computing, or on a distributed cluster of computers.

- **Just pandas:** Dask DataFrames are a collection of many pandas DataFrames. The API is the same. The execution is the same.
- **Large scale:** Works on 100 GiB on a laptop, or 100 TiB on a cluster.
- **Easy to use:** Pure Python, easy to set up and debug.

Dask DataFrames coordinate many pandas DataFrames/Series arranged along the index. A Dask DataFrame is partitioned *row-wise*, grouping rows by index value for efficiency. These pandas objects may live on disk or on other machines.

## From pandas to Dask

Dask DataFrame copies pandas, and so should be familiar to most users

Pandas and Dask have the same API, and so switching from one to the other is straightforward.

```python
>>> import pandas as pd

>>> df = pd.read_parquet('s3://mybucket/myfile.parquet')
>>> df.head()
0  1  a
1  2  b
2  3  c
```

```python
>>> import dask.dataframe as dd

>>> df = dd.read_parquet('s3://mybucket/myfile.*.parquet')
>>> df.head()
0  1  a
1  2  b
2  3  c
```

Dask does pandas in parallel. Dask is lazy; when you want an in-memory result add `.compute()`.

```python
>>> import pandas as pd

>>> df = df[df.value >= 0]
>>> joined = df.merge(other, on="account")
>>> result = joined.groupby("account").value.mean()

>>> result
alice 123
bob   456
```

```python
>>> import dask.dataframe as dd

>>> df = df[df.value >= 0]
>>> joined = df.merge(other, on="account")
>>> result = joined.groupby("account").value.mean()

>>> result.compute()
alice 123
bob   456
```

Machine learning libraries often have Dask submodules that expect Dask DataFrames and operate in parallel.

```python
>>> import pandas as pd
>>> import xgboost
>>> from sklearn.cross_validation import train_test_split

>>> X_train, X_test, y_train, y_test = train_test_split(
...    X, y, test_size=0.2,
)
>>> dtrain = xgboost.DMatrix(X_train, label=y_train)

>>> xgboost.train(params, dtrain, 100)
<xgboost.Booster ...>
```

```python
>>> import dask.dataframe as dd
>>> import xgboost.dask
>>> from dask_ml.model_selection import train_test_split

>>> X_train, X_test, y_train, y_test = train_test_split(
...    X, y, test_size=0.2,
)
>>> dtrain = xgboost.dask.DaskDMatrix(client, X, y)

>>> xgboost.dask.train(params, dtrain, 100)
<xgboost.Booster ...>
```

As with all Dask collections, you trigger computation by calling the `.compute()` method or persist data in distributed memory with the `.persist()` method.

## When not to use Dask DataFrames

Dask DataFrames are often used either when …

1. Your data is too big
2. Your computation is too slow and other techniques don’t work

You should probably stick to just using pandas if …

1. Your data is small
2. Your computation is fast (subsecond)
3. There are simpler ways to accelerate your computation, like avoiding `.apply` or Python for loops and using a built-in pandas method instead.

## Examples

Dask DataFrame is used across a wide variety of applications — anywhere where working with large tabular dataset. Here are a few large-scale examples:

- Parquet ETL with Dask DataFrame
- XGBoost model training with Dask DataFrame
- Visualize 1,000,000,000 points

These examples all process larger-than-memory datasets on Dask clusters deployed with Coiled, but there are many options for managing and deploying Dask. See our Deploy Dask Clusters documentation for more information on deployment options.

You can also visit https://examples.dask.org/dataframe.html for a collection of additional examples.
