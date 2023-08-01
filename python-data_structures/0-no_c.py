def no_c(my_string):
    
    outcome = []
    
    for char in my_string:
        if char != 'c' and char != 'C':
            outcome.append(char)
        return ''.join(outcome)

if __name__ == "__main__":
    print(no_c("This string contains c's and C's"))