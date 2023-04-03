#!usr/bin/python3
"""Solve the N-queens puzzle
Determine all posible soluton to place N

Attributes:
    board (list): A list of list represent the chase board
    solution (list): a list of list containg solutions
"""
import sys


def create_board(n):
    """initialize an n x n sized chaseboard with 0's """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return(board)
