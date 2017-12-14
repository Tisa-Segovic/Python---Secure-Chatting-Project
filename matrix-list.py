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
  
def correct_error(matrix):
    len_row = len(matrix)
    len_column = 5
    error_row = None
    error_column = None
    error_row_sum = None  # For the actual matrix code

    for row in range(len_row - 1):  # For error row
        if np.sum(matrix[row][:4]) != matrix[row][4]:
            error_row = row
            error_row_sum = np.sum(matrix[row][:4])

    for col in range(len_column - 1):  # For error column
        col_sum = 0
        for i in range(len_row - 1):
            col_sum += matrix[i][col]
        if col_sum != matrix[-1][col]:
            error_column = col

    if error_row == None and error_column == None:  # No error
        matrix[len_row - 1][len_column - 1] = (
        int(matrix[len_row - 1][0]) + int(matrix[len_row - 1][1]) + int(matrix[len_row - 1][2]) + int(
            matrix[len_row - 1][3]))
    elif error_row == None and error_column != None:  # Matrix row error
        m = 0
        for row in range(len_row - 1):
            m += matrix[row][error_column]
        matrix[-1][error_column] = m
    elif error_column == None and error_row != None:  # Matrix column error
        n = 0
        for col in range(len_column - 1):
            n += matrix[error_row][col]
        matrix[error_row][-1] = n
    return matrix
  
def matrix2alnum(matrix):
    i = np.mat('1,0,0,0,0,0,0,0;\
                0,1,0,0,0,0,0,0;\
                0,0,1,0,0,0,0,0;\
                0,0,0,1,0,0,0,0')
    r = np.dot(i, matrix.T)
    ret = r.T.reshape((1,-1)).tolist()[0]
    return ret    
