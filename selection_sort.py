
def selection_sort(arr):

    for i in range(len(arr)):
        mid_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[mid_index]:
                mid_index = j
        arr[i], arr[mid_index] = arr[mid_index], arr[i]



my_list = [12, 11, 13, 5, 6]
selection_sort(my_list)
print("Sorted array:", my_list)
