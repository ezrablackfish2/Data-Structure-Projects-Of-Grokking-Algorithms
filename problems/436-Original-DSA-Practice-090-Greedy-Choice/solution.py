def solve(node):
    if node is None:
        return 0
    _, left, right = node
    return 1 + max(solve(left), solve(right))

if __name__ == "__main__":
    tree = (1, (2, None, None), (3, None, None))
    print(solve(tree))
