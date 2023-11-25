# This bubble sort algorithms using to sort a list of element
# The Time Complexity of this algorithms is O(n^2)

def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted array:", my_list)
