def ezra(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


def aman(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = ezra(arr)
        newArr.append(arr[smallest])
        arr.pop(smallest)
    return newArr


print(aman([5, 3, 6, 2, 10, 12, 54, 87, 9]))
