# python -m Algorithmns.Sorting.04_Merge_sort
from typing import List

def merge_sorted_list(list1: List, list2: List) -> List:
    """Utility Function to merge two sorted List"""
    # TC: O(m + n)
    # SC: O(m + n)  

    print(f"Merging the list: {list1} and {list2}")
    final_list = []
    m, n = len(list1), len(list2)
    i = j = 0

    while (i <= m-1) and (j <= n-1):

        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        
        else:
            final_list.append(list2[j])
            j += 1
    
    if i <= m-1:
        while (i != m):
            final_list.append(list1[i])
            i += 1

    if j <= n-1:
        while (j != n):
            final_list.append(list2[j])
            j += 1

    return final_list


def merge_sort(list_: List) -> List:
    """
    Sort the List using merge sort
    """
    # TC: O(n*log(n))
    # SC: 
    # Stability: Stable

    print(f"Sorting the List: {list_}")

    # Base Condition
    if len(list_) <= 1:
        return list_

    # Find the Mid Point
    mid = len(list_) // 2

    # Sort the Left of List
    left_sort = merge_sort(list_[0:mid])

    # Sort the right of List
    right_sort = merge_sort(list_[mid:])

    # Merge the Sorted List
    sorted_list = merge_sorted_list(left_sort, right_sort)

    return sorted_list


def merge_sort_iterative(list_: List) -> List:
    """Implement Iterative version of Merge Sort"""
    # TC: O(N*log*N)
    # SC: O(1)


    # Length of List
    n = len(list_)
    
    # Bottom Up Approach - Start by Merging one element, then two and so on
    """
    Suppose we have:
    [38, 27, 43, 3, 9, 82, 10]
    Pass 1 (size=1): merge [38] & [27], [43] & [3], [9] & [82], leftover [10]
    Pass 2 (size=2): merge [27, 38] & [3, 43], [9, 82] & [10]
    Pass 3 (size=4): merge [27, 38, 3, 43] & [9, 10, 82]
    Final sorted array achieved.
    """

    size = 1
    while size < n:
        for left in range(0, n, 2*size):
            right = min(left + 2*size - 1, n-1)
            mid = min(left + size, n-1) #left + (right + 1 - left) // 2
            sort_arr = merge_sorted_list(list1=list_[left:mid], list2=list_[mid:right+1])
            list_[left:right+1] = sort_arr

        size *= 2


    return list_




if __name__ == "__main__":

    list_ = [1, 2, 4]
    print(f"Intial List: {list_}")

    # sorted_list = merge_sort(list_)
    # print(f"Final sorted List using recursion: {sorted_list}")

    sorted_list = merge_sort_iterative(list_)
    print(f"Final sorted List using Iteration: {sorted_list}")
