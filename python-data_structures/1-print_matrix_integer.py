def print_matrix_integer(matrix=[[]]):
    
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()

if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
