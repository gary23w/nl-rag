---
title: "Data Types and In-Memory Data Model"
source: https://arrow.apache.org/docs/python/data.html
domain: pyarrow-python
license: CC-BY-SA-4.0
tags: python pyarrow, apache arrow python, columnar data python
fetched: 2026-07-02
---

# Data Types and In-Memory Data Model

Apache Arrow defines columnar array data structures by composing type metadata with memory buffers, like the ones explained in the documentation on Memory and IO. These data structures are exposed in Python through a series of interrelated classes:

- **Type Metadata**: Instances of `pyarrow.DataType`, which describe the type of an array and govern how its values are interpreted
- **Schemas**: Instances of `pyarrow.Schema`, which describe a named collection of types. These can be thought of as the column types in a table-like object.
- **Arrays**: Instances of `pyarrow.Array`, which are atomic, contiguous columnar data structures composed from Arrow Buffer objects
- **Record Batches**: Instances of `pyarrow.RecordBatch`, which are a collection of Array objects with a particular Schema
- **Tables**: Instances of `pyarrow.Table`, a logical table data structure in which each column consists of one or more `pyarrow.Array` objects of the same type.

We will examine these in the sections below in a series of examples.

## Schemas

The `Schema` type is similar to the `struct` array type; it defines the column names and types in a record batch or table data structure. The `pyarrow.schema()` factory function makes new Schema objects in Python:

```python
>>> my_schema = pa.schema([('field0', t1),
...                        ('field1', t2),
...                        ('field2', t4),
...                        ('field3', t6)])
>>> my_schema
field0: int32
field1: string
field2: fixed_size_binary[10]
field3: list<item: int32>
  child 0, item: int32
```

In some applications, you may not create schemas directly, only using the ones that are embedded in IPC messages.

Schemas are immutable, which means you can’t update an existing schema, but you can create a new one with updated values using `Schema.set()`.

```python
>>> updated_field = pa.field('field0_new', pa.int64())
>>> my_schema2 = my_schema.set(0, updated_field)
>>> my_schema2
field0_new: int64
field1: string
field2: fixed_size_binary[10]
field3: list<item: int32>
  child 0, item: int32
```

## Arrays

For each data type, there is an accompanying array data structure for holding memory buffers that define a single contiguous chunk of columnar array data. When you are using PyArrow, this data may come from IPC tools, though it can also be created from various types of Python sequences (lists, NumPy arrays, pandas data).

A simple way to create arrays is with `pyarrow.array`, which is similar to the `numpy.array` function. By default PyArrow will infer the data type for you:

```python
>>> arr = pa.array([1, 2, None, 3])
>>> arr
<pyarrow.lib.Int64Array object at ...>
[
  1,
  2,
  null,
  3
]
```

But you may also pass a specific data type to override type inference:

```python
>>> pa.array([1, 2], type=pa.uint16())
<pyarrow.lib.UInt16Array object at ...>
[
  1,
  2
]
```

The array’s `type` attribute is the corresponding piece of type metadata:

```python
>>> arr.type
DataType(int64)
```

Each in-memory array has a known length and null count (which will be 0 if there are no null values):

```python
>>> len(arr)
4
>>> arr.null_count
1
```

Scalar values can be selected with normal indexing. `pyarrow.array` converts `None` values to Arrow nulls; we return the special `pyarrow.NA` value for nulls:

```python
>>> arr[0]
<pyarrow.Int64Scalar: 1>
>>> arr[2]
<pyarrow.Int64Scalar: None>
```

Arrow data is immutable, so values can be selected but not assigned.

Arrays can be sliced without copying:

```python
>>> arr[1:3]
<pyarrow.lib.Int64Array object at ...>
[
  2,
  null
]
```

### None values and NAN handling

As mentioned in the above section, the Python object `None` is always converted to an Arrow null element on the conversion to `pyarrow.Array`. For the float NaN value which is either represented by the Python object `float('nan')` or `numpy.nan` we normally convert it to a *valid* float value during the conversion. If an integer input is supplied to `pyarrow.array` that contains `np.nan`, `ValueError` is raised.

To handle better compatibility with Pandas, we support interpreting NaN values as null elements. This is enabled automatically on all `from_pandas` function and can be enabled on the other conversion functions by passing `from_pandas=True` as a function parameter.

### List arrays

`pyarrow.array` is able to infer the type of simple nested data structures like lists:

```python
>>> nested_arr = pa.array([[], None, [1, 2], [None, 1]])
>>> print(nested_arr.type)
list<item: int64>
```

### ListView arrays

`pyarrow.array` can create an alternate list type called ListView:

```python
>>> nested_arr = pa.array([[], None, [1, 2], [None, 1]], type=pa.list_view(pa.int64()))
>>> print(nested_arr.type)
list_view<item: int64>
```

ListView arrays have a different set of buffers than List arrays. The ListView array has both an offsets and sizes buffer, while a List array only has an offsets buffer. This allows for ListView arrays to specify out-of-order offsets:

```python
>>> values = [1, 2, 3, 4, 5, 6]
>>> offsets = [4, 2, 0]
>>> sizes = [2, 2, 2]
>>> arr = pa.ListViewArray.from_arrays(offsets, sizes, values)
>>> arr
<pyarrow.lib.ListViewArray object at ...>
[
  [
    5,
    6
  ],
  [
    3,
    4
  ],
  [
    1,
    2
  ]
]
```

See the format specification for more details on ListView Layout.

### Struct arrays

`pyarrow.array` is able to infer the schema of a struct type from arrays of dictionaries:

```python
>>> pa.array([{'x': 1, 'y': True}, {'z': 3.4, 'x': 4}])
<pyarrow.lib.StructArray object at ...>
-- is_valid: all not null
-- child 0 type: int64
  [
    1,
    4
  ]
-- child 1 type: bool
  [
    true,
    null
  ]
-- child 2 type: double
  [
    null,
    3.4
  ]
```

Struct arrays can be initialized from a sequence of Python dicts or tuples. For tuples, you must explicitly pass the type:

```python
>>> ty = pa.struct([('x', pa.int8()),
...                 ('y', pa.bool_())])
>>> pa.array([{'x': 1, 'y': True}, {'x': 2, 'y': False}], type=ty)
<pyarrow.lib.StructArray object at ...>
-- is_valid: all not null
-- child 0 type: int8
  [
    1,
    2
  ]
-- child 1 type: bool
  [
    true,
    false
  ]
>>> pa.array([(3, True), (4, False)], type=ty)
<pyarrow.lib.StructArray object at ...>
-- is_valid: all not null
-- child 0 type: int8
  [
    3,
    4
  ]
-- child 1 type: bool
  [
    true,
    false
  ]
```

When initializing a struct array, nulls are allowed both at the struct level and at the individual field level. If initializing from a sequence of Python dicts, a missing dict key is handled as a null value:

```python
>>> pa.array([{'x': 1}, None, {'y': None}], type=ty)
<pyarrow.lib.StructArray object at ...>
-- is_valid:
  [
    true,
    false,
    true
  ]
-- child 0 type: int8
  [
    1,
    0,
    null
  ]
-- child 1 type: bool
  [
    null,
    false,
    null
  ]
```

You can also construct a struct array from existing arrays for each of the struct’s components. In this case, data storage will be shared with the individual arrays, and no copy is involved:

```python
>>> xs = pa.array([5, 6, 7], type=pa.int16())
>>> ys = pa.array([False, True, True])
>>> arr = pa.StructArray.from_arrays((xs, ys), names=('x', 'y'))
>>> arr.type
StructType(struct<x: int16, y: bool>)
>>> arr
<pyarrow.lib.StructArray object at ...>
-- is_valid: all not null
-- child 0 type: int16
  [
    5,
    6,
    7
  ]
-- child 1 type: bool
  [
    false,
    true,
    true
  ]
```

### Map arrays

Map arrays can be constructed from lists of lists of tuples (key-item pairs), but only if the type is explicitly passed into `array()`:

```python
>>> data = [[('x', 1), ('y', 0)], [('a', 2), ('b', 45)]]
>>> ty = pa.map_(pa.string(), pa.int64())
>>> pa.array(data, type=ty)
<pyarrow.lib.MapArray object at ...>
[
  keys:
  [
    "x",
    "y"
  ]
  values:
  [
    1,
    0
  ],
  keys:
  [
    "a",
    "b"
  ]
  values:
  [
    2,
    45
  ]
]
```

MapArrays can also be constructed from offset, key, and item arrays. Offsets represent the starting position of each map. Note that the `MapArray.keys` and `MapArray.items` properties give the *flattened* keys and items. To keep the keys and items associated to their row, use the `ListArray.from_arrays()` constructor with the `MapArray.offsets` property.

```python
>>> arr = pa.MapArray.from_arrays([0, 2, 3], ['x', 'y', 'z'], [4, 5, 6])
>>> arr.keys
<pyarrow.lib.StringArray object at ...>
[
  "x",
  "y",
  "z"
]
>>> arr.items
<pyarrow.lib.Int64Array object at ...>
[
  4,
  5,
  6
]
>>> pa.ListArray.from_arrays(arr.offsets, arr.keys)
<pyarrow.lib.ListArray object at ...>
[
  [
    "x",
    "y"
  ],
  [
    "z"
  ]
]
>>> pa.ListArray.from_arrays(arr.offsets, arr.items)
<pyarrow.lib.ListArray object at ...>
[
  [
    4,
    5
  ],
  [
    6
  ]
]
```

### Union arrays

The union type represents a nested array type where each value can be one (and only one) of a set of possible types. There are two possible storage types for union arrays: sparse and dense.

In a sparse union array, each of the child arrays has the same length as the resulting union array. They are adjuncted with a `int8` “types” array that tells, for each value, from which child array it must be selected:

```python
>>> xs = pa.array([5, 6, 7])
>>> ys = pa.array([False, False, True])
>>> types = pa.array([0, 1, 1], type=pa.int8())
>>> union_arr = pa.UnionArray.from_sparse(types, [xs, ys])
>>> union_arr.type
SparseUnionType(sparse_union<0: int64=0, 1: bool=1>)
>>> union_arr
<pyarrow.lib.UnionArray object at ...>
-- is_valid: all not null
-- type_ids:   [
    0,
    1,
    1
  ]
-- child 0 type: int64
  [
    5,
    6,
    7
  ]
-- child 1 type: bool
  [
    false,
    false,
    true
  ]
```

In a dense union array, you also pass, in addition to the `int8` “types” array, a `int32` “offsets” array that tells, for each value, at each offset in the selected child array it can be found:

```python
>>> xs = pa.array([5, 6, 7])
>>> ys = pa.array([False, True])
>>> types = pa.array([0, 1, 1, 0, 0], type=pa.int8())
>>> offsets = pa.array([0, 0, 1, 1, 2], type=pa.int32())
>>> union_arr = pa.UnionArray.from_dense(types, offsets, [xs, ys])
>>> union_arr.type
DenseUnionType(dense_union<0: int64=0, 1: bool=1>)
>>> union_arr
<pyarrow.lib.UnionArray object at ...>
-- is_valid: all not null
-- type_ids:   [
    0,
    1,
    1,
    0,
    0
  ]
-- value_offsets:   [
    0,
    0,
    1,
    1,
    2
  ]
-- child 0 type: int64
  [
    5,
    6,
    7
  ]
-- child 1 type: bool
  [
    false,
    true
  ]
```

### Dictionary Arrays

The **Dictionary** type in PyArrow is a special array type that is similar to a factor in R or a `pandas.Categorical`. It enables one or more record batches in a file or stream to transmit integer *indices* referencing a shared **dictionary** containing the distinct values in the logical array. This is particularly often used with strings to save memory and improve performance.

The way that dictionaries are handled in the Apache Arrow format and the way they appear in C++ and Python is slightly different. We define a special `DictionaryArray` type with a corresponding dictionary type. Let’s consider an example:

```python
>>> indices = pa.array([0, 1, 0, 1, 2, 0, None, 2])
>>> dictionary = pa.array(['foo', 'bar', 'baz'])
>>>
>>> dict_array = pa.DictionaryArray.from_arrays(indices, dictionary)
>>> dict_array
<pyarrow.lib.DictionaryArray object at ...>
...
-- dictionary:
  [
    "foo",
    "bar",
    "baz"
  ]
-- indices:
  [
    0,
    1,
    0,
    1,
    2,
    0,
    null,
    2
  ]
```

Here we have:

```python
>>> print(dict_array.type)
dictionary<values=string, indices=int64, ordered=0>
>>> dict_array.indices
<pyarrow.lib.Int64Array object at ...>
[
  0,
  1,
  0,
  1,
  2,
  0,
  null,
  2
]
>>> dict_array.dictionary
<pyarrow.lib.StringArray object at ...>
[
  "foo",
  "bar",
  "baz"
]
```

When using `DictionaryArray` with pandas, the analogue is `pandas.Categorical` (more on this later):

```python
>>> dict_array.to_pandas()
0    foo
1    bar
2    foo
3    bar
4    baz
5    foo
6    NaN
7    baz
dtype: category
Categories (3, str): ['foo', 'bar', 'baz']
```

## Record Batches

A **Record Batch** in Apache Arrow is a collection of equal-length array instances. Let’s consider a collection of arrays:

```python
>>> data = [
...     pa.array([1, 2, 3, 4]),
...     pa.array(['foo', 'bar', 'baz', None]),
...     pa.array([True, None, False, True])
... ]
```

A record batch can be created from this list of arrays using `RecordBatch.from_arrays`:

```python
>>> batch = pa.RecordBatch.from_arrays(data, ['f0', 'f1', 'f2'])
>>> batch.num_columns
3
>>> batch.num_rows
4
>>> batch.schema
f0: int64
f1: string
f2: bool
>>>
>>> batch[1]
<pyarrow.lib.StringArray object at ...>
[
  "foo",
  "bar",
  "baz",
  null
]
```

A record batch can be sliced without copying memory like an array:

```python
>>> batch2 = batch.slice(1, 3)
>>> batch2[1]
<pyarrow.lib.StringArray object at ...>
[
  "bar",
  "baz",
  null
]
```

## Tables

The PyArrow `Table` type is not part of the Apache Arrow specification, but is rather a tool to help with wrangling multiple record batches and array pieces as a single logical dataset. As a relevant example, we may receive multiple small record batches in a socket stream, then need to concatenate them into contiguous memory for use in NumPy or pandas. The Table object makes this efficient without requiring additional memory copying.

Considering the record batch we created above, we can create a Table containing one or more copies of the batch using `Table.from_batches`:

```python
>>> batches = [batch] * 5
>>> table = pa.Table.from_batches(batches)
>>> table
pyarrow.Table
f0: int64
f1: string
f2: bool
----
f0: [[1,2,3,4],[1,2,3,4],...,[1,2,3,4],[1,2,3,4]]
f1: [["foo","bar","baz",null],...,["foo","bar","baz",null]]
f2: [[true,null,false,true],...,[true,null,false,true]]
>>> table.num_rows
20
```

The table’s columns are instances of `ChunkedArray`, which is a container for one or more arrays of the same type.

```python
>>> c = table[0]
>>> c
<pyarrow.lib.ChunkedArray object at ...>
[
  [
    1,
    2,
    3,
    4
  ],
  ...
  [
    1,
    2,
    3,
    4
  ]
]
>>> c.num_chunks
5
>>> c.chunk(0)
<pyarrow.lib.Int64Array object at ...>
[
  1,
  2,
  3,
  4
]
```

As you’ll see in the pandas section, we can convert these objects to contiguous NumPy arrays for use in pandas:

```python
>>> c.to_pandas()
0     1
1     2
2     3
3     4
4     1
5     2
6     3
7     4
8     1
9     2
10    3
11    4
12    1
13    2
14    3
15    4
16    1
17    2
18    3
19    4
Name: f0, dtype: int64
```

Multiple tables can also be concatenated together to form a single table using `pyarrow.concat_tables`, if the schemas are equal:

```python
>>> tables = [table] * 2
>>> table_all = pa.concat_tables(tables)
>>> table_all.num_rows
40
>>> c = table_all[0]
>>> c.num_chunks
10
```

This is similar to `Table.from_batches`, but uses tables as input instead of record batches. Record batches can be made into tables, but not the other way around, so if your data is already in table form, then use `pyarrow.concat_tables`.

## Record Batch Readers

Many functions in PyArrow either return or take as an argument a `RecordBatchReader`. It can be used like any iterable of record batches, but also provides their common schema without having to get any of the batches.

```python
>>> schema = pa.schema([('x', pa.int64())])
>>>
>>> def iter_record_batches():
...    for i in range(2):
...       yield pa.RecordBatch.from_arrays([pa.array([1, 2, 3])], schema=schema)
>>>
>>> reader = pa.RecordBatchReader.from_batches(schema, iter_record_batches())
>>> print(reader.schema)
x: int64
>>> for batch in reader:
...    print(batch)
pyarrow.RecordBatch
x: int64
----
x: [1,2,3]
pyarrow.RecordBatch
x: int64
----
x: [1,2,3]
```

It can also be sent between languages using the C stream interface.

## Conversion of RecordBatch to Tensor

Each array of the `RecordBatch` has it’s own contiguous memory that is not necessarily adjacent to other arrays. A different memory structure that is used in machine learning libraries is a two dimensional array (also called a 2-dim tensor or a matrix) which takes only one contiguous block of memory.

For this reason there is a function `pyarrow.RecordBatch.to_tensor()` available to efficiently convert tabular columnar data into a tensor.

Data types supported in this conversion are unsigned, signed integer and float types. Currently only column-major conversion is supported.

```python
>>> arr1 = [1, 2, 3, 4, 5]
>>> arr2 = [10, 20, 30, 40, 50]
>>> batch = pa.RecordBatch.from_arrays(
...      [
...          pa.array(arr1, type=pa.uint16()),
...          pa.array(arr2, type=pa.int16()),
...      ], ["a", "b"]
...  )
>>> batch.to_tensor()
<pyarrow.Tensor>
type: int32
shape: (5, 2)
strides: (8, 4)
>>> batch.to_tensor().to_numpy()
array([[ 1, 10],
       [ 2, 20],
       [ 3, 30],
       [ 4, 40],
       [ 5, 50]], dtype=int32)
```

With `null_to_nan` set to `True` one can also convert data with nulls. They will be converted to `NaN`:

```python
>>> batch = pa.record_batch(
...     [
...         pa.array([1, 2, 3, 4, None], type=pa.int32()),
...         pa.array([10, 20, 30, 40, None], type=pa.float32()),
...     ], names = ["a", "b"]
... )
>>> batch.to_tensor(null_to_nan=True).to_numpy()
array([[ 1., 10.],
       [ 2., 20.],
       [ 3., 30.],
       [ 4., 40.],
       [nan, nan]])
```
