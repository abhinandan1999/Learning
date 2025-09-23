# python -m Algorithmns.Sorting.05_quick_sort
from typing import List


def pivot_element(list_: List, start: int, end: int) -> int:
    """Function to Arrange the element around pivot"""
    pivot_element = list_[end-1]

    pivot_index = start # Keep track of Left most element from right of pivot element
    for i in range(start, end):
        if list_[i] < pivot_element:
            list_[i],list_[pivot_index] = list_[pivot_index] , list_[i]
            pivot_index += 1
    
    list_[pivot_index], list_[end-1] = list_[end-1], list_[pivot_index]

    return pivot_index


def quick_sort(list_: List, start: int, end: int) -> List:
    """Recursive Implementation of Quick Sort"""
    # TC: 
        # Worst case: O(N^2)
        # Avg Case: O(N*Log(N))
        # Best Case: O(N*Log(N))

    # SC: O(1) In Place Sorting hence it is preferred over Merge Sort

    # Step 0: Base Condition
    if end <= start:
        return

    # Step 1: Get the Pivot element
    pivot_index = pivot_element(list_, start=start, end=end)
    print(f"From the list: {list_[start:end]} pivot index is {pivot_index} with value {list_[pivot_index]}")

    # Step 2: Recursively Sort Left of Pivot 
    print(f"Calling Recursively on left of Pivot {list_[start:pivot_index]}\n")
    quick_sort(list_, start=start, end=pivot_index)

    # Step 3: Recursively Sort the right of Pivot
    print(f"Calling Recursively on right of Pivot {list_[pivot_index+1:]}\n")
    quick_sort(list_, start=pivot_index+1, end=end)

    print(f"After Both Calls list is: {list_}")

if __name__ == "__main__":

    list_ = [1, 3, 2, 4]
    print(f"Intial List: {list_}")

    quick_sort(list_, start=0, end=len(list_))
    print(f"Final sorted List using recursion: {list_}")

    # sorted_list = quick_sort_iterative(list_)
    # print(f"Final sorted List using Iteration: {sorted_list}")