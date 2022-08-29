def shell_sort(arr: list):
    # splits original array into sublists
    # initializes the gap
    sublist_count = len(arr)//2

    # loops thru list and increasingly many sublists:
    #  sublist_count = 0 would just be the og list
    while sublist_count > 0:

        # i is the first element of different sublists
        for i in range(sublist_count):
            # thus i, and the gap along with the list,
            # are used to sort using insertion sort
            # for each distinct sublist
            gap_insertion_sort(arr, i, sublist_count)

        # halves the gap size
        sublist_count = sublist_count // 2


def gap_insertion_sort(arr: list, start: int, gap: int):
    for i in range(start + gap, len(arr)):
        curr_value = arr[i]
        curr_position = i

        while curr_position > 0 and curr_value < arr[curr_position - gap]:
            arr[curr_position] = arr[curr_position - gap]
            curr_position -= gap

        arr[curr_position] = curr_value

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(a_list)
# print(a_list)