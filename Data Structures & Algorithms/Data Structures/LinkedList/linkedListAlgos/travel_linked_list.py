# python -m LinkedList.linkedListAlgos.travel_linked_list

from LinkedList import LinkedList, Node
from typing import List


def recursive_travel(head: Node) -> List[str]:
    """Algorithm to Travel Linked List Recursively"""

    # Base Condition
    if not head:
        return []
    
    # Get the Current Element
    collected_element = [head.data]

    # Call the function again
    res = recursive_travel(head.next)

    # Merge with Previous Result
    collected_element += res
    
    return collected_element

def main():

    # Create a Linked List
    llist = LinkedList(["1", "2", "3", "443432432432"])

    rec_travel_res = recursive_travel(llist.head)

    print(rec_travel_res)
    print(llist)
    
if __name__ == "__main__":
    main()
    