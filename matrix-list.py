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
  
def list_into_string(matrix):
    myString = str(matrix)
    return myString
  
def string_into_matrix(mat_string):
    mat_string = mat_string.lstrip('[[')
    mat_string = mat_string.rstrip(']]')
    matrix_list = []
    for i in mat_string.split('], ['):
        sublist = []
        for j in i.split(','):
            sublist.append(int(j))
        matrix_list.append(sublist)

    return matrix_list
  
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
  
def back_to_ASCII(matrix):
    matrix = np.array(matrix)
    msg = ""
    len_row = int(matrix.size / 5)
    len_column = 5
    for row in range(len_row - 1):
        for column in range(len_column - 1):
            if int(matrix[row][column]) != 0:
                msg += chr(matrix[row][column])
    msg = str(msg)
    return msg 
