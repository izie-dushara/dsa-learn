def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if target == list[midpoint]:
            return midpoint
        elif target > list[midpoint]:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index} with the value of {numbers[index]}")
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 2)
verify(result)

result = binary_search(numbers, 6)
verify(result)
