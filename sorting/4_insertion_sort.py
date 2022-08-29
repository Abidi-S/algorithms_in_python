def insertion_sort(arr: list):

    # i takes values 1 through n (len(arr))
    for i in range(1, len(arr)):
        # key is the i-th element with every loop iteration
        curr_value = arr[i]
        curr_position = i

        # executes if i-th element is smaller than j-th element
        while curr_position > 0 and curr_value < arr[curr_position - 1]:
            # i-th element is moved one position to the left
            arr[curr_position] = arr[curr_position - 1]

            # curr_postion is decremented
            curr_position -= 1
            # and the loop conditional is checked again prior to execution

        # note that curr_postion has been decremented by however many
        # times the while loop executed therefore arr[curr_position] != arr[i]
        # like it did at the start of the for loop
        arr[curr_position] = curr_value

    # sorts in place so don't need a return statement

arr = [12, 11, 5, 6, 2]
insertion_sort(arr)
print(arr)