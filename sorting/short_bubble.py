# optimized bubble sort that ends when list recognized as sorted
# count variable used to increment number of passes to verify

def bubble_sort_short(listicle: list):
    length = len(listicle)
    # count = 0
    for i in range(length - 1):
        # (n - 1) pairs/passes
        swaps = False
        for j in range(length - i - 1):
            # (n - i - 1) comparisons
            if listicle[j] > listicle[j + 1]:
                swaps = True
                # swap elements as required
                listicle[j], listicle[j + 1] = listicle[j + 1], listicle[j]
        if not swaps:
            break
        # count += 1
    return listicle #, count

print(bubble_sort_short([1, 2, 3, 5, 6, 4, 7, 8, 9]))