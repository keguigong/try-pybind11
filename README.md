# try-pybind11

## Example to Use `pybind11`

Compile `cpp` file to `.so` using `pybind11`.

```txt
# CMakeLists.txt
cmake_minimum_required(VERSION 3.5)
project(example)

add_subdirectory(extern/pybind11-2.12.0)

pybind11_add_module(example example.cpp)
```

```bash
$ mkdir build && cd build
$ cmake ..
$ make
```

Then we can call C++ methods from python, e.g. `add` method we just defined in C++.

```bash
$ build git:(main) ✗ ipython
In [1]: import example

In [2]: example.add(10, 15)
Out[2]: 25
```

## Roughly Comparing the Performance of C++, Python and Numpy

Matrix multiplication is quite time consuming, and can be used for our testing. Implement our own matrix multiplication function with C++, and Python as well.

```cpp
// matrix.h
class Matrix {
  public:
    static void Dot(const Matrix &A, const Matrix &B, Matrix &C);
}

// matrix.cpp
void Matrix::Dot(const Matrix &A, const Matrix &B, Matrix &C) {
  for (size_t i = 0; i < A.Rows(); i++) {
    for (size_t j = 0; j < B.Cols(); j++) {

      float sum = 0.0f;
      for (size_t k = 0; k < A.Cols(); k++) {
        sum += A.Get(i, k) * B.Get(k, j);
      }
      C.Set(i, j, sum);
    }
  }
}
```

Then run the script with specifying matrix size. 100 means a 100x100 matrix.

```bash
$ python compare.py --size=100
Numpy matrix multiplication: size: 100, time: 0.0004189014434814453
C++ matrix multiplication: size: 100, time: 0.006092071533203125
Python matrix multiplication: size: 100, time: 0.13921570777893066
```

After simple testing, the results reveal that C++ is much faster compared to Python. However, numpy spends the least time, with some unique optimizations.

## References

关注了很久的 up HexUp 的视频：

- https://www.bilibili.com/video/BV1jr421W71p
- https://www.bilibili.com/video/BV19w4m117yq
