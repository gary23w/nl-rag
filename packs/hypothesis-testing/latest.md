---
title: "Hypothesis 6.156.0 documentation"
source: https://hypothesis.readthedocs.io/en/latest/
domain: hypothesis-testing
license: CC-BY-SA-4.0
tags: hypothesis python, property-based testing, test strategies, python testing
fetched: 2026-07-02
---

# Welcome to Hypothesis!

Hypothesis is the property-based testing library for Python. With Hypothesis, you write tests which should pass for all inputs in whatever range you describe, and let Hypothesis randomly choose which of those inputs to check - including edge cases you might not have thought about. For example:

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers() | st.floats()))
def test_sort_correctness_using_properties(lst):
    result = my_sort(lst)
    assert set(lst) == set(result)
    assert all(a <= b for a, b in zip(result, result[1:]))
```

You should start with the tutorial, or alternatively the more condensed quickstart.

## Tutorial

An introduction to Hypothesis.

New users should start here, or with the more condensed quickstart.

## How-to guides

Practical guides for applying Hypothesis in specific scenarios.

## Explanations

Commentary oriented towards deepening your understanding of Hypothesis.

## API Reference

Technical API reference.
