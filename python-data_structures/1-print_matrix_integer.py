def print_matrix_integer(matrix=[[]]):    
    for row in matrix:
        if not row:
            print()
            continue
        count = 0
        
        for item in row:
            if count != len(row) - 1:
                print('{:d} '.format(item), end=" ")
            else:
                print("{:d}".format(item))
            count += 1
            
if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])