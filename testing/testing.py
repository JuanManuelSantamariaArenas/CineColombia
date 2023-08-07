def fill_array(rows, columns):
    matrix_hidden = []
    for i in range(0, rows):
        matrix_hidden.append([0]*columns)
    for i in range(0, rows):
        for j in range(0, columns):
            matrix_hidden[i][j] = " "
    for i in matrix_hidden:
        print(i)
    rows_and_columns = [rows, columns]
    print(rows_and_columns)
fill_array(2,2)