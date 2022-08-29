def merge_sort(arr: list):
    # function only does something if array length is greater than 1
    # since an array of length 1 is already sorted
    if len(arr) > 1:

        # find the midpoint of the array
        mid = len(arr) // 2

        # create two temp sub-arrays using midpoint of og array
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recursively split up each array respectively
        # [recurses till len(sub_array) == 1]
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge

        i = 0       # left_arr index
        j = 0       # right_arr index
        k = 0       # final merged array index

        # loop iterates while there are elements in BOTH arrays
        while i < len(left_arr) and j < len(right_arr):

            # compare element in left array to element at
            # corresponding index at right array
            if left_arr[i] < right_arr[j]:
                # assign the smaller of the two to the kth index in merged array
                arr[k] = left_arr[i]
                # increment corresponding array's index
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1

            # increment k so next loop iteration places next element
            # at k + 1 index position
            k += 1

        # check if elements left in left_arr
        while i < len(left_arr):
            # just yeet remaining elements to merged array
            # and increment the indices accordingly
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # check if elements left in right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    # no return statement

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# merge_sort(a_list)
# print(a_list)