condition = True
while condition:
    number = input("enter a number or 'x' to quit: ")
    condition = number != 'x'
    if number.isdigit():
        print(number)
    else:
        print("'"+number+"' is not a number!")
else:
    print('goodbye!')

class EmptyClass:
    pass

def fib(n):
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib(2000))

# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
