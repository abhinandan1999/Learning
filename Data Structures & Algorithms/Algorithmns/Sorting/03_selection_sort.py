# python -m Algorithmns.Sorting.03_selection_sort
from typing import List


def selection_sort(list_: List):
    """Implement a sorting algorithm using selection sort"""
    # TC: O(N^2)
    # SC: O(1) - No additonal space is required
    # Stability: Algorithm is not stable (Order can cange) Ex [(4, A), (4, B), (3, C), (5, D)] -> (First Swap) -> [(3, C), (4, B), (4 A), (5 D)]
    # Notice how the position of (4, A) and (4, B) is swapped
    n = len(list_)

    for i in range(n):

        # Get the minimum element from subarray[i : n-1]
        min_index_subarray = i
        for j in range(i+1, n):

            # Get the index of minimum element in sub array
            if list_[j] < list_[i]:
                min_index_subarray = j
        
        # Swap it
        if min_index_subarray != i:
            list_[i], list_[min_index_subarray] = list_[min_index_subarray], list_[i]
        
        print(f"List after {i + 1} is: {list_}")

    return list_

def main():
    
    list_ = [4, 3, 2, 2,  1]
    print(f"Original List: {list_}")

    sorted_list = selection_sort(list_=list_)
    print(f"Sorted List: {sorted_list}")

if __name__ == "__main__":
    main()