def fibonacci_sequence(n):
    # Check for invalid input
    if n <= 0:
        return []

    # Initialize a list to store the fibonacci
    fibonacci_numbers = []

    # Handle the first fibonacci numbers (0, 1)
    if n >= 1:
        fibonacci_numbers.append(0)

    if n >= 2:
        fibonacci_numbers.append(1)

    # Generate the rest of the fibonacci numbers
    while len(fibonacci_numbers) < n:
        # Calculate the next fibonacci number
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers
