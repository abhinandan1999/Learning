# python -m Algorithmns.Sorting.insertion_sort
from typing import List

def insertion_sort(list_: List) -> List:
    """
    Sort the list using insertion sort algorithm.
    
    Insertion sort works by maintaining two sub array:
      Left Subarray: Always sorted (i.e. till index i)
      Right Subarray: Requires sorting (by moving element at i + 1) to right place in Left Subarray
    """
    # TC: O(N^2)
    # SC: O(1)

    # Get Number of elements of List
    n = len(list_)

    # Till list_[i] list is sorted
    for i in range(1, n):
        
        # Step 1: Assume List is sorted till index i
        # Step 2: Find appropriate place for element at index (i + 1)
        # Step 3: Keep swapping until appropriate index is found
        for j in range(i, 0, -1):
            # Check if list_[i+1] is smaller than the last element of sorted array i.e. list_[i]
            if list_[j] < list_[j-1]:
                list_[j-1], list_[j] = list_[j], list_[j-1]

        print(f"List after Iteration {i} is: {list_}")

    return list_


def main():

    list_ = [3, 2, 1, 4, 0, -1]
    print(f"Original Array: {list_}")

    sorted_list_ = insertion_sort(list_=list_)
    print(f"Sorted Array: {sorted_list_}")

if __name__ == "__main__":
    main()