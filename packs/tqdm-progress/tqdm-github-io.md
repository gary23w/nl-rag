---
title: "tqdm documentation"
source: https://tqdm.github.io/
domain: tqdm-progress
license: CC-BY-SA-4.0
tags: python tqdm, tqdm progress bar, progress meter python
fetched: 2026-07-02
---

# tqdm

(Py-Versions) (Versions) (Conda-Forge-Status) (Docker) (Snapcraft) (colab-demo) (binder-demo)

(Build-Status) (Coverage-Status) (Branch-Coverage-Status) (Codacy-Grade) (Libraries-Rank) (PyPI-Downloads) (Repology) (awesome-python) (README-Hits)

`tqdm` means "progress" in Arabic (*taqadum*, تقدّم) and is an abbreviation for "I love you so much" in Spanish (*te quiero demasiado*).

Instantly make your loops show a smart progress meter - just wrap any iterable with `tqdm(iterable)`, and you're done!

```
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
```

`76%|████████████████████████████         | 7568/10000 [00:33<00:10, 229.00it/s]`

`trange(N)` can be also used as a convenient shortcut for `tqdm(range(N))`.

(Screenshot)

(Video) (Slides) (Merch)

It can also be executed as a module with pipes:

```
$ seq 9999999 | tqdm --bytes | wc -l
75.2MB [00:00, 217MB/s]
9999999
$ 7z a -bd -r backup.7z docs/ | grep Compressing | \
    tqdm --total $(find docs/ -type f | wc -l) --unit files >> backup.log
100%|███████████████████████████████▉| 8014/8014 [01:37<00:00, 82.29files/s]
```

Overhead is low -- about 60ns per iteration (80ns with `tqdm_gui`), and is unit tested against performance regression. By comparison, the well-established ProgressBar has an 800ns/iter overhead.

In addition to its low overhead, `tqdm` uses smart algorithms to predict the remaining time and to skip unnecessary iteration displays, which allows for a negligible overhead in most cases.

`tqdm` works on any platform (Linux, Windows, Mac, FreeBSD, NetBSD, Solaris/SunOS), in any console or in a GUI, and is also friendly with IPython/Jupyter notebooks.

`tqdm` does not require any dependencies (not even `curses`!), just Python and an environment supporting `carriage return \r` and `line feed \n` control characters.

| (OpenAI) | Your Logo Here |
|---|---|
| OpenAI | Sponsoring `tqdm` |

(DOI) (LICENCE) (OpenHub-Status) (CII Best Practices)
