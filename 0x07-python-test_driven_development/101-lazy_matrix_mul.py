#!/usr/bin/python3
"""define matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplay two matrix

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Returns:
        multiplication of the two matrix
    """

    return (np.matmul(m_a, m_b))
