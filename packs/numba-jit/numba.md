---
title: "Numba"
source: https://en.wikipedia.org/wiki/Numba
domain: numba-jit
license: BSD-3-Clause
tags: numba compiler, just-in-time compilation, automatic vectorization, llvm backend
fetched: 2026-07-02
---

# Numba

**Numba** is an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes.

Numba was started by Travis Oliphant in 2012 and has since been under active development with frequent releases. The project is driven by developers at Anaconda, Inc., with support by DARPA, the Gordon and Betty Moore Foundation, Intel, Nvidia and AMD, and a community of contributors on GitHub.

## Example

Numba can be used by simply applying the `numba.jit` decorator to a Python function that does numerical computations:

```mw
import numba
import random

@numba.jit
def monte_carlo_pi(n_samples: int) -> float:
    """Monte Carlo"""
    acc = 0
    for i in range(n_samples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / n_samples
```

The just-in-time compilation happens transparently when the function is called:

```mw
>>> monte_carlo_pi(1000000)
3.14
```

## GPU support

Numba can compile Python functions to GPU code. Initially two backends are available:

- NVIDIA CUDA, see numba.readthedocs.io/en/stable/cuda/index.html
- AMD ROCm HSA, see numba.pydata.org/numba-doc/dev/roc

Since release 0.56.4, AMD ROCm HSA has been officially moved to unmaintained status and a separate repository stub has been created for it.

## Alternative approaches

Numba is one approach to make Python fast, by compiling specific functions that contain Python and NumPy code. Many alternative approaches for fast numeric computing with Python exist, such as Cython, Pythran, and PyPy.
