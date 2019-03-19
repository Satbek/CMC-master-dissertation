import pytest
import numpy
import sys
import variational_method.matrices as matrices

test_data = dict()
test_data['Lambda-3'] = [[2, -1, -1],
                         [-1, 2, -1],
                         [-1, -1, 2]]

test_data['Beta-3'] = [[2/3, 1/6, 1/6],
                       [1/6, 2/3, 1/6],
                       [1/6, 1/6, 2/3]]

test_data['G_1-3'] = [[0., -0.5, 0.5],
                      [0.5, 0., -0.5],
                      [-0.5, 0.5, 0.]]

test_data['G_2-3'] = [[0., 0.5, -0.5],
                      [-0.5,  0.,  0.5],
                      [0.5, -0.5,  0.]]


def to_list(arr):
    return numpy.ndarray.tolist(arr)


def compare_real_matrices(mat1, mat2):
    return numpy.allclose(mat1, mat2)


def test_lambda():
    assert to_list(matrices.create_l(3, 1)) == test_data['Lambda-3']


def test_beta():
    assert compare_real_matrices(matrices.create_b(3, 1), test_data['Beta-3'])


def test_g1():
    assert to_list(matrices.create_g1(3, 1)) == test_data['G_1-3']


def test_g2():
    assert to_list(matrices.create_g2(3, 1)) == test_data['G_2-3']
