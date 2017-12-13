
""" To do by Brandon - let me know when you have finished!
Fill out the following functions & Feel free to rename them! """

import random
import numpy as np

def alnum2matrix(msg):
    #hamming (8,4)
    while len(msg) % 4 != 0:
        msg.append(0)
    m = np.reshape(np.array(msg), (-1, 4))
    t = np.mat('1,0,0,0,0,1,1,1;\
                0,1,0,0,1,0,1,1;\
                0,0,1,0,1,1,0,1;\
                0,0,0,1,1,1,1,0')
    r =  np.dot(m, t)
    return np.mod(r, 2)
  
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
