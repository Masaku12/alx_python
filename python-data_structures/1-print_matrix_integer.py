def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0
    
    for row in matrix:
        for i in range(rows):
            print("{:d}".format(row[i], end=""))
            
            if i < columns - 1:
                print(" ", end="")
                
        print()
                