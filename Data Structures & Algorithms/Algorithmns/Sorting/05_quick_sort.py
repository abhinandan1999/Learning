# python -m Algorithmns.Sorting.05_quick_sort
from typing import List


def quick_sort(list_: List) -> List:
    """Recursive Implementation of Quick Sort"""

    return list_

if __name__ == "__main__":

    list_ = [1, 2, 4]
    print(f"Intial List: {list_}")

    sorted_list = quick_sort(list_)
    print(f"Final sorted List using recursion: {sorted_list}")

    # sorted_list = quick_sort_iterative(list_)
    # print(f"Final sorted List using Iteration: {sorted_list}")