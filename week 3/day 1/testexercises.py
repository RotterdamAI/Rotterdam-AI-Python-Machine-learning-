from time import sleep
import sys
import numpy as np
OKGREEN = '\033[92m'
ENDC = '\033[0m'

#################################################
# helper functions
#################################################
def correct_assertion():
    print(f"\n{OKGREEN}All tests passed!!!"+ ENDC)

def loader():
    for i in range(10):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        sleep(0.1)

#################################################
# exercise tests
#################################################

def hint_matrixmul():
    print("you can use the @ operator to do the matmul")

def test_matrixmul(f):
    loader()
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7,8], [9,10], [11,12]])
    result = matrix1 @ matrix2
    assert(f(matrix1, matrix2) == result)
    correct_assertion()

def hint_matrix3x3():
    print("we can use arange and afterwards a reshape")

def test_matrix3x3(f):
    loader()
    matrix = np.arange(2,11).reshape(3,3)
    assert(f() == matrix)
    correct_assertion()

def hint_append_array():
    print("you can use np.append()")

def test_append_array():
    loader()
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    result = np.append(x, y)
    assert(f(x, y)== result)
    correct_assertion()

def hint_checkerboard_pattern():
    print("first we can initialize our board using board = np.zeros((y, x), dtype=int)")
    print("then we can use some smart index to assign 1 using:")
    print("board[1::2, ::2] = 1")
    print("board[::2, 1::2] = 1")

def test_checkerboard_pattern(f):
    loader()
    x = 5
    y = 5
    result = np.zeros((y, x), dtype=int)
    result[1::2, ::2] = 1
    result[::2, 1::2] = 1
    assert(f(5, 5) == result)
    correct_assertion()

def checkerboard_pattern(x, y):
    board = np.zeros((y, x),dtype=int)
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    return board

# checkerboard_pattern(4, 6)