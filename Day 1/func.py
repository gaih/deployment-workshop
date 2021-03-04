
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def power(x, y):
    return x ** y

def divide(x, y):
    if y == 0:
        raise ValueError("Trying to divide by zero!!!")
    return x / y

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def fibonacci(n):
    if n <= 1:
        return 1
    else: 
        return fibonacci(n - 2) + fibonacci(n - 1)



a = 1900

b = 41

if is_even(a) & is_even(b):
    c = add(a, b)
    d = power(b, 2)
    e = subtract(a, d)
    f = divide(e, b)
    print(f)
else:
    print("Conditions not satisfied!!!")