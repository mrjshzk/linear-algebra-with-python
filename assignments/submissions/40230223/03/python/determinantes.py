# import matplotlib.pyplot as plt
import numpy as np


def det_2x2_sarrus(mat):
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


def det_3x3_sarrus(mat):
    d1 = mat[0][0] * mat[1][1] * mat[2][2]
    d2 = mat[0][1] * mat[1][2] * mat[2][1]
    d3 = mat[0][2] * mat[1][1] * mat[2][2]

    dr1 = mat[0][2] * mat[1][1] * mat[2][0]
    dr2 = mat[0][0] * mat[1][2] * mat[2][1]
    dr3 = mat[0][1] * mat[1][1] * mat[2][2]

    return (d1 + d2 + d3) - (dr1 + dr2 + dr3)


m1 = np.array([[1.0, 2.0], [3.0, 4.0]])
m2 = np.array([[2.0, 4.0], [1.0, 2.0]])

print("Invertible 2x2 Matrix")
print(m1)
print(f"Determinant by Sarrus method: {det_2x2_sarrus(m1)}")

print("Singular 2x2 Matrix")
print(m2)
print(f"Determinant by Sarrus method: {det_2x2_sarrus(m2)}")


m1 = np.array([[1.0, 2.0, 3.0], [0.0, 1.0, 4.0], [5.0, 6.0, 0.0]])
m2 = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [1.0, 1.0, 1.0]])

print("Invertible 3x3 Matrix")
print(m1)
print(f"Determinant by Sarrus method: {det_3x3_sarrus(m1)}")

print("Singular 3x3 Matrix")
print(m2)
print(f"Determinant by Sarrus method: {det_3x3_sarrus(m2)}")
