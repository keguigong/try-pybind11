cmake_minimum_required(VERSION 3.5)
project(example)
project(toy_matrix)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# set(PYTHON_EXECUTABLE "/opt/homebrew/anaconda3/bin/python")
# set(PYTHON_INCLUDE_DIRECTORY "/opt/homebrew/anaconda3/bin/python3.11")

add_subdirectory(extern/pybind11-2.12.0)

pybind11_add_module(example example.cpp)
# add_executable(TestMatrix matrix.cpp)
pybind11_add_module(toy_matrix bind.cpp matrix.cpp)