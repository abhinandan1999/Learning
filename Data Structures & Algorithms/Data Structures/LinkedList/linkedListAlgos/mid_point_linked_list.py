# python -m LinkedList.linkedListAlgos.mid_point_linked_list
from LinkedList import LinkedList, Node


def get_mid_point_llist_sp_fp(llist: LinkedList) -> tuple:
    """
    Find the Mid point of Linked and return a Tuple of index and data using slow pointer and fast pointer

    Reason: SP and FP is better algorithm to find the mid point of a linked list because it doesn't require to traverse the entire linked list.
    """
    # TC: O(n)
    # SC: O(1)

    # Check if the Linked List is empty
    if llist.head is None:
        return (-1, None)
    
    # Initialize the slow pointer and Fast pointer
    sp = llist.head
    fp = llist.head

    # Travel till FP is None
    idx = 0
    while fp and fp.next:

        # Increment the sp by one
        sp = sp.next
        idx += 1

        # Increment the fp by two
        fp = fp.next.next

    # When the loop will end sp will be at midpoint
    return (idx, sp.data)


def get_mid_point_llist(llist: LinkedList) -> tuple:
    """Find the Mid point of Linked and return a Tuple of index and data"""
    # TC: O(n)
    # SC: O(1)

    # Check if the linked list is empty
    if llist.head is None:
        return (-1, None)

    # Get the length of the linked list
    llist_len = llist.len
    mid_point = llist_len // 2
    print(f"Length of Linked List: {llist_len}")
    print(f"Mid point: {mid_point}")

    # Travel to the mid point
    start = 0
    node = llist.head
    while start < mid_point:
        node = node.next
        start += 1

    # Return the mid point
    return (mid_point, node.data)

def main():

    # Create a Linked List
    llist = LinkedList(["1", "2", "3", "4", "5", "6"])
    print(f"Original Linked List: {llist}")

    idx, data = get_mid_point_llist(llist=llist)
    print(f"Mid point is {data} at position {idx}\n")

    idx, data = get_mid_point_llist_sp_fp(llist=llist)
    print(f"Mid point is {data} at position {idx}")

if __name__ == "__main__":

    # Call main
    main()

    



