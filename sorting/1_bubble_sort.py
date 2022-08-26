def bubble_sort(listicle: list):
    # count = 0
    length = len(listicle)
    for i in range(length - 1):
        # (n - 1) pairs/passes
        for j in range(length - i - 1):
            # (n - i - 1) comparisons
            if listicle[j] > listicle[j + 1]:
                # swap elements as required
                listicle[j], listicle[j + 1] = listicle[j + 1], listicle[j]
        # count += 1
    return listicle #, count


# print(bubble_sort([3, 8, 6, 0, 7, 1, 9, 2]))
# print(bubble_sort([1, 2, 3, 5, 6, 7, 8, 9]))