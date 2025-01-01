def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
bubble_sort(arr)
print("Sorted array:", arr)

## Without using Swapped variable
        
def bubbleSort(arr1):
    n=len(arr1)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j], arr1[j+1]=arr1[j+1], arr1[j]
                
    print("Sorted array:", arr1)
    
arr1=[64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr1)
                


