def solve(r, c):
    dp = [1] * c
    for _ in range(1, r):
        for j in range(1, c):
            dp[j] += dp[j-1]
    return dp[-1]

if __name__ == "__main__":
    print(solve(2, 3))
