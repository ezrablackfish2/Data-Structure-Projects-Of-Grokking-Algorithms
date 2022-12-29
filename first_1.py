def srch(arry, itm):
    low = 0
    high = len(arry) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arry[mid]
        if itm == guess:
            return mid
        elif itm < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(srch([1, 2, 3, 4, 5, 10], 10))
