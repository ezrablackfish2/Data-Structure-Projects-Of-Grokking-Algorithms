def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess > item:
            low = mid + 1
        else:
            return mid


my_list = [1, 3, 5, 7, 9, 11]
print(binary_search(my_list, 1))
print(binary_search(my_list, 9))
print(f"ezra is {5 // 2} the best")
