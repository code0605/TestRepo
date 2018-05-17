def factorial(n):
    if n < 0:
        raise ValueError("Neg numbers do not have factorials")
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(10))

print(factorial(-10))

