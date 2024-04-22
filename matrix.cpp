#include <vector>
#include <stdexcept>
#include <random>
#include <iostream>

#include "matrix.h"

Matrix::Matrix(size_t rows, size_t cols) : rows(rows), cols(cols), data(rows * cols, 0.0f)
{
}

void Matrix::Set(size_t row, size_t col, float value)
{
  if (row >= 0 && row < rows && col >= 0 && col < cols)
  {
    data[row * cols + col] = value;
  }
}

float Matrix::Get(size_t row, size_t col) const
{
  if (row >= 0 && row < rows && col >= 0 && col < cols)
  {
    return data[row * cols + col];
  }
  throw std::out_of_range("Matrix indices out of range");
}

size_t Matrix::Rows() const
{
  return rows;
}

size_t Matrix::Cols() const
{
  return cols;
}