# python -m Algorithmns.Sorting.bubble_sort
from typing import List

def bubble_sort(list: List) -> List:
    """Sort the list with bubble sort algorithm"""
    # TC: O()
    # SC: O()

    sorted_list = list
    
    return sorted_list

def main():

    list_ = [1, 2, 3, 4]
    print(f"Original Array: {list_}")

    sorted_list_ = bubble_sort(list=list_)
    print(f"Sorted Array: {sorted_list_}")

if __name__ == "__main__":
    main()