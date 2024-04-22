cmake_minimum_required(VERSION 3.4)
project(example)

# Set(PYTHON_EXECUTABLE "/opt/homebrew/anaconda3/bin/python")
# Set(PYTHON_INCLUDE_DIRECTORY "/opt/homebrew/anaconda3/bin/python3.11")

add_subdirectory(extern/pybind11)
pybind11_add_module(example example.cpp)