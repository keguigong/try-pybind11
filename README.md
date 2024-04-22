# try-pybind11

Watch the tutorial from:

- Try `pybind11`: https://www.bilibili.com/video/BV1jr421W71p
- Performance comparison by matrix `Dot` calculation: https://www.bilibili.com/video/BV19w4m117yq

```bash
➜  mkdir build
➜  cd build
➜  build git:(main) ✗ cmake ..
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- pybind11 v2.12.0
-- Configuring done (0.1s)
-- Generating done (0.0s)
-- Build files have been written to: /Users/jiahong.he/Repos/try-pybind11/build
➜  build git:(main) ✗ make
[ 50%] Building CXX object CMakeFiles/example.dir/example.cpp.o
[100%] Linking CXX shared module example.cpython-311-darwin.so
[100%] Built target example
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

In [3]:
```
