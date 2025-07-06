# python -m LinkedList.linkedListAlgos.detect_cycle_linked_list
from LinkedList import LinkedList, Node


def has_cycle_llist(llist: LinkedList) -> bool:
    """Detect Cycle in the Linked List"""
    # TC: O(n)
    # SC: O(1)

    # Check for the case where llist is None
    if not llist:
        return llist

    # Initialise SP and FP
    SP = FP = llist.head

    # Iterate Till you reach end or FP meets SP
    while FP and FP.next:

        # Move SP by 1
        SP = SP.next

        # Move FP by 2
        FP = FP.next.next

        # Check if FP and SP met
        if SP == FP:
            return SP

    return False

def get_start_of_cycle(llist: LinkedList):
    """ Get Start of the cycle"""
    # TC: O(1)
    # SCL O(1)

    # Handle the edge case
    if not llist:
        return llist
    
    # Get the detection node of cycle
    cycle_detection_node = has_cycle_llist(llist=llist)

    # Initialise a head pointer
    start = llist.head
    next_cycle_node = cycle_detection_node

    # Iterate till tead and cycle_detection_node matches
    while start != next_cycle_node:
        start = start.next
        next_cycle_node = next_cycle_node.next

    return start

def remove_cycle(llist: LinkedList):
    """ Get Start of the cycle"""
    # TC: O(1)
    # SCL O(1)

    # Handle the edge case
    if not llist:
        return llist
    
    # Get the detection node of cycle
    cycle_detection_node = has_cycle_llist(llist=llist)

    # Initialise a head pointer
    start = llist.head
    next_cycle_node = cycle_detection_node

    # Iterate till tead and cycle_detection_node matches
    while start.next != next_cycle_node.next:
        start = start.next
        next_cycle_node = next_cycle_node.next

    # Set the Last Node of cycle to None
    next_cycle_node.next = None

    return llist


def main():

    llist = LinkedList(["1", "2", "3", "4"])
    print(f"Linked List is: {llist}")
    
    # Create a new Node
    node = llist.head.next
    # Create a Cycle
    llist.head.next.next.next = node

    has_cycle = has_cycle_llist(llist=llist)
    print(f"Linked List {f'has cycle which is detected at {has_cycle}'  if has_cycle else 'does not have cycle'}")


    start_of_cycle = get_start_of_cycle(llist=llist)
    print(f"Linked List {f'has cycle starting at {start_of_cycle}'  if has_cycle else 'does not have cycle'}")

    llist = remove_cycle(llist=llist)
    print(f"Linked List after removing cycle {llist}")
    
if __name__ == "__main__":
    main()