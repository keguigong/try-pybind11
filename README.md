# try-pybind11

Watch the tutorial from:

- Try `pybind11`: https://www.bilibili.com/video/BV1jr421W71p
- Performance comparison by matrix `Dot` calculation: https://www.bilibili.com/video/BV19w4m117yq

```bash
mkdir build
cd build
cmake ..
make
```

Invoke `add` function from python.

```bash
➜  build git:(main) ✗ ipython
Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import example

In [2]: example.add(10, 15)
Out[2]: 25
```
