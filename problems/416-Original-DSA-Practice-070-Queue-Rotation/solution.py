from collections import deque

def solve(nums, k):
    dq = deque()
    out = []
    for i, n in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

if __name__ == "__main__":
    sample = [1,3,-1,-3,5,3,6,7]
    print(solve(sample, 3))
