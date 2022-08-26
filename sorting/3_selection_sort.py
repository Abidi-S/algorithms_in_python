def selection_sort(listicle: list):
    n = len(listicle)
    i = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if listicle[j] < listicle[min_index]:
                min_index = j
                j += 1
        listicle[i], listicle[min_index] = listicle[min_index], listicle[i]
        i += 1

    return listicle

# print(selection_sort([6, 7, 8, 1, 9, 0, 2, 4]))