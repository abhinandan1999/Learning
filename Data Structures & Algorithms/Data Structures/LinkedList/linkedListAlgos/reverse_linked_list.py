# python -m LinkedList.linkedListAlgos.reverse_linked_list

from LinkedList import LinkedList

def reverse_linked_list_iterative(llist: LinkedList) -> LinkedList:
    """Iteratively reverse a Linked List"""
    # TC: O(N)
    # SC: O(1)

    # Step 1: Intialize prevNode, curNode and nextNode
    prevNode = None
    curNode = llist.head

    # Step 2: Iterate till your current Node is None
    while curNode:
        # Define a next Node
        nextNode = curNode.next

        # Point Current Node Next to prev Node
        curNode.next = prevNode

        # Move the Prev Node to Current Node
        prevNode = curNode

        # Move the Current Node to Next Node
        curNode = nextNode

    # Set the Head of LinkedList
    llist.head = prevNode


    return llist

def reverse_linked_list_recursively(head: LinkedList):
    """Reverse a Linked List Recursively"""
    # TC: O(N)
    # SC: O(N)

    # Base Condition
    if head is None or head.next is None:
        return head

    # Reverse the remaining Linked List
    rest = reverse_linked_list_recursively(head=head.next)

    # Adjust the Pointer
    head.next.next = head
    head.next = None

    return rest


def main():

    # Initialize a linked List
    llist = LinkedList(["1", "2", "3", "4"])
    print(f"Original Linked List: {llist}")

    # Reverse the Linked List Iteratively
    reverse_llist = reverse_linked_list_iterative(llist=llist)
    print(f"Reversed Linked List: {reverse_llist}")

    # Initialize a linked List
    llist = LinkedList(["1", "2", "3", "4"])
    print(f"Original Linked List: {llist}")

    # Reverse the Linked List Recursively
    reverse_head = reverse_linked_list_recursively(head=llist.head)
    llist.head = reverse_head
    print(f"Reversed Linked List: {reverse_llist}")
    
    return

if __name__ == "__main__":

    main()