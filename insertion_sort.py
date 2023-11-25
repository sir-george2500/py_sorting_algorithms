
# this is a implementation of the insertion sort algo
# Time complexity O(n^2) space complexity O(n)

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]

            # set j out of bound
            j -= 1
            arr[j+1] = key



my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)

