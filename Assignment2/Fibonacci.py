def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = 5
print(f"The {n}th position of the fibonacci series is {fibonacci(n)}.")

# The 5th position of the fibonacci series is 3.