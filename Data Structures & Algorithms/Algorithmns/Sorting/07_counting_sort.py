# python -m 07_counting_sort
from typing import List

def counting_sort(list_: List) -> List:
    """Implement a counting sort algorithm"""
    # TC: O(N)
    # SC: O(N)
    # Stability: Stable

    # Step 1: Find the Offset element
    # TC: O(N)
    # SC: O(1)
    offset_ele = min(list_)
    print(f"Offset element is {offset_ele}")

    # Step 2: If Min Element is < 0 then offset the element by the min_ele amount
    # TC: O(N)
    # SC: O(1)
    if offset_ele < 0:
        for i in range(len(list_)):
            list_[i] += (-offset_ele)

    
    # Step 3: Find the Minimum and Maximum Element
    # TC: O(N)
    # SC: O(1)
    min_ele, max_ele = min(list_), max(list_)
    print(f"Minimum and Maximum element after offset by {offset_ele} is {min(list_)} and {max(list_)}")

    # Step 4: Create a new array to count frequency of each element from 0 to max_ele
    # TC: O(N)
    # SC: O(N)
    count_list = [0] * (max_ele + 1)
    print(f"Count List of {len(count_list)} is initialised with 0")
    for ele in list_:
        count_list[ele] += 1

    print(f"Count List is {count_list}")

    # Step 5: Create Cumlative frequency count of count list
    # TC: O(N)
    # SC: O(1)
    for idx in range(1, len(count_list)):
        count_list[idx] += count_list[idx-1]

    print(f"Cumulative count of element is: {count_list}")

    # Step 6: Create the final Sorted list
    sorted_list_ = [0] * len(list_)
    for i in range(len(list_)-1, -1, -1): # Travel each element
        ele = list_[i]
        pos = count_list[ele] - 1 # Find the postition of the element
        sorted_list_[pos] = ele # Place the element in the sorted list

        # print(f"Sorted Position of {ele} is {pos}: {sorted_list_}")
        count_list[ele] -= 1 # Reduce the frequency of it by one

    print(f"Cumulative count of element after placing: {count_list}")

    # Step 7: Reset the List by offset index
    # TC: O(N)
    # SC: O(1)
    for i in range(len(sorted_list_)):
        sorted_list_[i] += offset_ele

    return sorted_list_


if __name__ == "__main__":

    list_ = [-2, -1, 0, 0, 4, 1, 2, 2]
    print(f"Original List before sorting: {list_}")

    sorted_list = counting_sort(list_)
    print(f"List after sorting: {sorted_list}")