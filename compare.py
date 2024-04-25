import time
import numpy as np
from build import toy_matrix
from pymatrix import PyMatrix

Matrix = toy_matrix.Matrix


def NPArrayFromMatrix(A):
    N = A.Rows()
    M = A.Cols()
    return np.array([[A.Get(i, j) for j in range(M)] for i in range(N)])


def PyMatrixFromMatrix(A):
    N = A.Rows()
    M = A.Cols()
    result = PyMatrix(N, M, random_fill=False)
    for i in range(N):
        for j in range(M):
            result.Set(i, j, A.Get(i, j))
    return result


def CompareResult(A, B):
    # 转换为Numpy
    A_NP = NPArrayFromMatrix(A)
    B_NP = NPArrayFromMatrix(B)

    # 转换为Python矩阵
    A_Py = PyMatrixFromMatrix(A)
    B_Py = PyMatrixFromMatrix(B)

    # Numpy矩阵点乘
    np_start = time.time()
    C_NP = A_NP.dot(B_NP)
    np_end = time.time()

    # Python调用C++实现
    C = Matrix(A.Rows(), B.Cols())
    cpp_start = time.time()
    Matrix.Dot(A, B, C)

    C.PrintSummary()

    cpp_end = time.time()
    C_CPP = NPArrayFromMatrix(C)

    # Python原生
    C_Py = PyMatrix(A.Rows(), B.Cols(), random_fill=False)
    py_start = time.time()
    PyMatrix.Dot(A_Py, B_Py, C_Py)
    py_end = time.time()
    C_Py_NP = np.array([[C_Py.Get(i, j) for j in range(C_Py.cols)] for i in range(C_Py.rows)])

    if not np.allclose(C_NP, C_CPP, atol=1e-6):
        print("C++ Result do not match")

        ERR = C_NP - C_CPP
        print("Error: ", np.max(np.abs(ERR)))
    elif not np.allclose(C_NP, C_Py_NP, atol=1e-6):
        print("Python Result do not match")

        ERR = C_NP - C_Py_NP
        print("Error: ", np.max(np.abs(ERR)))
    else:
        print("Result match")

    np_report = (f"Numpy matrix multiplication: size: {A.Rows()}, time: {(np_end - np_start)}")
    cpp_report = (f"C++ matrix multiplication: size: {A.Rows()}, time: {(cpp_end - cpp_start)}")
    py_report = (f"Python matrix multiplication: size: {A.Rows()}, time: {(py_end - py_start)}")

    print(np_report)
    print(cpp_report)
    print(py_report)


def Compare(N=1000):
    A = Matrix(N, N)
    B = Matrix(N, N)
    A.FillRandom()
    B.FillRandom()
    
    A.PrintSummary()
    B.PrintSummary()

    CompareResult(A, B)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Matrix multiplication performance comparison')
    parser.add_argument('--size', type=int, default=100, metavar='N', help='input size of the matrix')
    args = parser.parse_args()
    Compare(args.size)
