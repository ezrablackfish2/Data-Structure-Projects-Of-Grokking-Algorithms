def counter(i):
    if i == 20:
        return i
    else:
        print(i)
        counter(i + 1)
    return i


counter(1)
