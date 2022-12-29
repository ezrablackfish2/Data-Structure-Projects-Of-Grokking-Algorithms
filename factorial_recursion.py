def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        f = x * factorial(x - 1)
        print(f)
        return f


factorial(4)
