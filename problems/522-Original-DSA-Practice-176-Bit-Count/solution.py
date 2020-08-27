def solve(s):
    bal = 0
    for ch in s:
        if ch == "(":
            bal += 1
        else:
            bal -= 1
            if bal < 0:
                return False
    return bal == 0

if __name__ == "__main__":
    sample = "(())()"
    print(solve(sample))
