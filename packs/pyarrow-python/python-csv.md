---
title: "Reading and Writing CSV files"
source: https://arrow.apache.org/docs/python/csv.html
domain: pyarrow-python
license: CC-BY-SA-4.0
tags: python pyarrow, apache arrow python, columnar data python
fetched: 2026-07-02
---

# Reading and Writing CSV files

Arrow supports reading and writing columnar data from/to CSV files. The features currently offered are the following:

- multi-threaded or single-threaded reading
- automatic decompression of input files (based on the filename extension, such as `my_data.csv.gz`)
- fetching column names from the first row in the CSV file
- column-wise type inference and conversion to one of `null`, `int64`, `float64`, `date32`, `time32[s]`, `timestamp[s]`, `timestamp[ns]`, `duration` (from numeric strings), `string` or `binary` data
- opportunistic dictionary encoding of `string` and `binary` columns (disabled by default)
- detecting various spellings of null values such as `NaN` or `#N/A`
- writing CSV files with options to configure the exact output format

## Usage

CSV reading and writing functionality is available through the `pyarrow.csv` module. In many cases, you will simply call the `read_csv()` function with the file path you want to read from:

```python
>>> from pyarrow import csv
>>> import pyarrow as pa
>>> import pandas as pd
>>> fn = 'tips.csv.gz'
>>> table = csv.read_csv(fn)
>>> table
pyarrow.Table
total_bill: double
tip: double
sex: string
smoker: string
day: string
time: string
size: int64
>>> len(table)
244
>>> df = table.to_pandas()
>>> df.head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

To write CSV files, just call `write_csv()` with a `pyarrow.RecordBatch` or `pyarrow.Table` and a path or file-like object:

```python
>>> table = pa.table({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
>>> csv.write_csv(table, "tips.csv")
>>> with pa.CompressedOutputStream("tips.csv.gz", "gzip") as out:
...     csv.write_csv(table, out)
```

Note

The writer does not yet support all Arrow types.

## Customized parsing

To alter the default parsing settings in case of reading CSV files with an unusual structure, you should create a `ParseOptions` instance and pass it to `read_csv()`:

```python
>>> def skip_handler(row):
...     pass
>>> table = csv.read_csv('tips.csv.gz', parse_options=csv.ParseOptions(
...    delimiter=";",
...    invalid_row_handler=skip_handler
... ))
>>> table
pyarrow.Table
col1,"col2": string
----
col1,"col2": [["1,"a"","2,"b"","3,"c""]]
```

Available parsing options are:

| `delimiter` | The character delimiting individual cells in the CSV data. |
|---|---|
| `quote_char` | The character used optionally for quoting CSV values (False if quoting is not allowed). |
| `double_quote` | Whether two quotes in a quoted CSV value denote a single quote in the data. |
| `escape_char` | The character used optionally for escaping special characters (False if escaping is not allowed). |
| `newlines_in_values` | Whether newline characters are allowed in CSV values. |
| `ignore_empty_lines` | Whether empty lines are ignored in CSV input. |
| `invalid_row_handler` | Optional handler for invalid rows. |

See also

For more examples see `ParseOptions`.

## Customized conversion

To alter how CSV data is converted to Arrow types and data, you should create a `ConvertOptions` instance and pass it to `read_csv()`:

```python
>>> table = csv.read_csv('tips.csv.gz', convert_options=csv.ConvertOptions(
...     column_types={
...         'total_bill': pa.decimal128(precision=10, scale=2),
...         'tip': pa.decimal128(precision=10, scale=2),
...     }
... ))
>>> table
pyarrow.Table
col1: int64
col2: string
----
col1: [[1,2,3]]
col2: [["a","b","c"]]
```

Note

To assign a column as `duration`, the CSV values must be numeric strings that match the expected unit (e.g. `60000` for 60 seconds when using `duration[ms]`).

Available convert options are:

| `check_utf8` | Whether to check UTF8 validity of string columns. |
|---|---|
| `column_types` | Explicitly map column names to column types. |
| `null_values` | A sequence of strings that denote nulls in the data. |
| `true_values` | A sequence of strings that denote true booleans in the data. |
| `false_values` | A sequence of strings that denote false booleans in the data. |
| `decimal_point` | The character used as decimal point in floating-point and decimal data. |
| `timestamp_parsers` | A sequence of strptime()-compatible format strings, tried in order when attempting to infer or convert timestamp values (the special value ISO8601() can also be given). |
| `strings_can_be_null` | Whether string / binary columns can have null values. |
| `quoted_strings_can_be_null` | Whether quoted values can be null. |
| `auto_dict_encode` | Whether to try to automatically dict-encode string / binary data. |
| `auto_dict_max_cardinality` | The maximum dictionary cardinality for *auto_dict_encode*. |
| `include_columns` | The names of columns to include in the Table. |
| `include_missing_columns` | If false, columns in *include_columns* but not in the CSV file will error out. |

See also

For more examples see `ConvertOptions`.

## Incremental reading

For memory-constrained environments, it is also possible to read a CSV file one batch at a time, using `open_csv()`.

There are a few caveats:

1. For now, the incremental reader is always single-threaded (regardless of `ReadOptions.use_threads`)
2. Type inference is done on the first block and types are frozen afterwards; to make sure the right data types are inferred, either set `ReadOptions.block_size` to a large enough value, or use `ConvertOptions.column_types` to set the desired data types explicitly.

## Character encoding

By default, CSV files are expected to be encoded in UTF8. Non-UTF8 data is accepted for `binary` columns. The encoding can be changed using the `ReadOptions` class:

```python
>>> table = csv.read_csv('tips.csv.gz', read_options=csv.ReadOptions(
...    column_names=["n_legs", "entry"],
...    skip_rows=1
... ))
>>> table
pyarrow.Table
n_legs: int64
entry: string
----
n_legs: [[1,2,3]]
entry: [["a","b","c"]]
```

Available read options are:

| `use_threads` | Whether to use multiple threads to accelerate reading. |
|---|---|
| `block_size` | How much bytes to process at a time from the input stream. |
| `skip_rows` | The number of rows to skip before the column names (if any) and the CSV data. |
| `skip_rows_after_names` | The number of rows to skip after the column names. |
| `column_names` | The column names of the target table. |
| `autogenerate_column_names` | Whether to autogenerate column names if *column_names* is empty. |
| `encoding` | encoding: object |

See also

For more examples see `ReadOptions`.

## Customized writing

To alter the default write settings in case of writing CSV files with different conventions, you can create a `WriteOptions` instance and pass it to `write_csv()`:

```python
>>> # Omit the header row (include_header=True is the default)
>>> options = csv.WriteOptions(include_header=False)
>>> csv.write_csv(table, "data.csv", options)
```

## Incremental writing

To write CSV files one batch at a time, create a `CSVWriter`. This requires the output (a path or file-like object), the schema of the data to be written, and optionally write options as described above:

```python
>>> with csv.CSVWriter("data.csv", table.schema) as writer:
...     writer.write_table(table)
```

## Performance

Due to the structure of CSV files, one cannot expect the same levels of performance as when reading dedicated binary formats like Parquet. Nevertheless, Arrow strives to reduce the overhead of reading CSV files. A reasonable expectation is at least 100 MB/s per core on a performant desktop or laptop computer (measured in source CSV bytes, not target Arrow data bytes).

Performance options can be controlled through the `ReadOptions` class. Multi-threaded reading is the default for highest performance, distributing the workload efficiently over all available cores.

Note

The number of concurrent threads is automatically inferred by Arrow. You can inspect and change it using the `cpu_count()` and `set_cpu_count()` functions, respectively.
