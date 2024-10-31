def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
target = int(input("Enter the target element to search: "))

result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
