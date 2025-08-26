# python -m Algorithmns.Sorting.bubble_sort
from typing import List

def bubble_sort(list_: List) -> List:
    """Sort the list with bubble sort algorithm"""
    # TC: O(N^2)
    # SC: O(1)
    # Stable Sorting

    # Get Length of the list
    n = len(list_)

    # Iterate over each element
    for i in range(0, n-1):
        
        # Flag to check if Swap was made, if no then the array is already sorted
        is_swap = False

        # Since after every iteration each element will be moved to end.
        # Subsequent iteration need not iterate till last element (n - i - 1)
        for j in range(0, n-i-1):
            # Compare the adjacent element
            if list_[j] > list_[j+1]:
                # Swap them
                list_[j], list_[j+1] = list_[j+1], list_[j]
                is_swap = True

        # Check if no swap was made
        if not is_swap:
            break

        # After end of each iteration the greatest element will be pushed to end
        print(f"List after Iteration {i+1}: {list_}")

    return list_

def main():

    list_ = [4, 3, 2, 1]
    print(f"Original Array: {list_}")

    sorted_list_ = bubble_sort(list_=list_)
    print(f"Sorted Array: {sorted_list_}")

if __name__ == "__main__":
    main()