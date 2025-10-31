# Exercise 2.1-2, page 22
# Rewrite the Insertion-Sort procedure
# to sort into nonincreasing instead of
# nondecreasing order.


def insertion_sort_decreasing (arr):
    n = len(arr)
    print(f"\nInitial array is {arr}.")
    print(f"Length of array is {n}.\n")
    for i in range(n - 2, -1, -1):
        key = arr[i]
        print(f"Key nr {i} is {key}.")
        j = i + 1
        print(f"Start comparing with nr {j}.")
        while j < n and arr[j] > key:
            print(f"Skip nr {j}.")
            arr[j - 1] = arr[j]
            j = j + 1
        arr[j - 1] = key
        print(f"Now arr[{j - 1}] become {key}!")
        print(f"The array now: {arr}\n")
    return arr


arr = [31, 41, 59, 26, 41, 58]
newarr = insertion_sort_decreasing(arr)
print(f"\nRESULT: {newarr}\n")