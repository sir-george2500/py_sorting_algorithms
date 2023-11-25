

def quick_sort(arr):

    if len(arr) < 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quick_sort(lesser) + [pivot] + quick_sort(greater)



my_list = [12, 11, 13, 5, 6]
quick_sort(my_list)
print("Sorted array:", my_list)

