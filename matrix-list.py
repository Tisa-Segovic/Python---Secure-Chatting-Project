
""" To do by Brandon - let me know when you have finished!
Fill out the following functions & Feel free to rename them! """

import random
import numpy as np

import random
import numpy as np

def numbers_into_matrix(msg):
    matrix = []
    message = []
    for i in msg:
        message.append(ord(i))

    if len(msg) % 4 == 0:
        len_row = (len(message) // 4)
    else:
        len_row = (len(message) // 4 + 1)

    [matrix.append([]) for i in range(len_row)]

    for i in range(len_row):
        for a in range(4):
            matrix[i].append(message.pop(0))

    matrix_checksum = matrix[:]
    for i in range(len_row):
        row_total = 0
        for e in matrix_checksum[i]:
            row_total += e
        matrix_checksum[i].append(row_total)

    matrix_checksum.append([])

    for i in range(5):
        colum_total = 0
        for a in range(len_row):
            colum_total += matrix_checksum[a][i]
        matrix_checksum[-1].append(colum_total)
    return matrix_checksum
  
def matrix_list2matrix_string(matrix):
    out = []
    for i in range(np.floor(len(matrix)/7)):
        s = i * 7
        # this is gross
        cs = matrix[s:s+7]
        cs = '0b' + ''.join([str(c) for c in cs])
        out.append(int(cs, 2))
    st = ''.join([chr(o) for o in out])
    return str(st)
  
def matrix_string2matrix_list(mat_string):
    r = list(mat_string)
        # convert to binary representation
    r = ['{:07b}'.format(ord(x)) for x in r]
        # split the binary into
    r = [[bit for bit in x] for x in r]
        # flatten it and convert to integers
        
    r = [int(bit) for sublist in r for bit in sublist]
    return r
  
def randomize_one_digit(matrix):
  
def error_correction(matrix):
    t = np.mat('0,1,1,1,1,0,0,0;\
               1,0,1,1,0,1,0,0;\
               1,1,0,1,0,0,1,0;\
               1,1,1,0,0,0,0,1')
    m = np.reshape(np.array(matrix), (-1, 8)).T
    r = np.dot(t, matrix)
    syndrome= np.mod(r, 2)
    for s in range(syndrome.shape[1]):
        if not np.any(syndrome[:,s]):
            # all zeros - no error!
            continue
        for c in range(t.shape[1]):
            if np.array_equal(t[:,c], syndrome[:,s]):
                cv = matrix[s,c]
                nv = (cv + 1) % 2
                matrix.itemset((s,c), nv)
    return matrix
  
def matrix2alnum(matrix):
    i = np.mat('1,0,0,0,0,0,0,0;\
                0,1,0,0,0,0,0,0;\
                0,0,1,0,0,0,0,0;\
                0,0,0,1,0,0,0,0')
    r = np.dot(i, matrix.T)
    ret = r.T.reshape((1,-1)).tolist()[0]
    return ret    
