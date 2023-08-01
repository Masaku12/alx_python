def no_c(my_string):
    outcome = ""
    
for char in my_string:
    if char != 'c' and char != 'C':
        outcome += char
        
return outcome