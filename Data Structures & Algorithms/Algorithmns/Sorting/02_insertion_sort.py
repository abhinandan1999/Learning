# python -m Algorithmns.Sorting.02_insertion_sort
from typing import List


def binary_search(arr: List, target: int, start: int, end: int) -> int:
    """
    Perform binary search to find the correct position for the target in the sorted subarray.
    """
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def insertion_sort(list_: List) -> List:
    """
    Sort the list using insertion sort algorithm.
    
    Insertion sort works by maintaining two sub array:
      Left Subarray: Always sorted (i.e. till index i)
      Right Subarray: Requires sorting (by moving element at i + 1) to right place in Left Subarray
    """
    # TC: O(N^2)
    # SC: O(1)
    # Stable Sorting

    # Get Number of elements of List
    n = len(list_)

    # Till list_[i] list is sorted
    for i in range(1, n):
        
        # Step 1: Assume List is sorted till index i
        # Step 2: Find appropriate place for element at index (i + 1)
        

        # Method 1:  Keep swapping until appropriate index is found
        # for j in range(i, 0, -1):
        #     # Check if list_[i+1] is smaller than the last element of sorted array i.e. list_[i]
        #     if list_[j] < list_[j-1]:
        #         list_[j-1], list_[j] = list_[j], list_[j-1]

        # Method 2: Keep Shifting element until appropriate index is found
        # j = i
        # ele_to_reindex = list_[j]
        # while (j > 0) and (ele_to_reindex < list_[j-1]):
        #     list_[j] = list_[j-1]
        #     j -= 1
        
        # list_[j] = ele_to_reindex

        # Method 3: Find the index to insert the element using binary search (As Left Subarray is sorted)
        ele_to_reindex = list_[i]
        k = binary_search(list_, ele_to_reindex, 0, i)
        list_[k+1:i+1] = list_[k:i]
        list_[k] = ele_to_reindex

        print(f"List after Iteration {i} is: {list_}")

    return list_


def main():

    list_ = [3, 4,22, 13, 0, -1, 44]
    print(f"Original Array: {list_}")

    sorted_list_ = insertion_sort(list_=list_)
    print(f"Sorted Array: {sorted_list_}")

if __name__ == "__main__":
    main()