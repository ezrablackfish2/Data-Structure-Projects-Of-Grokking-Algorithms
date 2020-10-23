def solve(nums):
    out = []
    current = None
    for n in nums:
        current = n if current is None else max(current, n)
        out.append(current)
    return out

if __name__ == "__main__":
    sample = [2, 1, 5, 3]
    print(solve(sample))
