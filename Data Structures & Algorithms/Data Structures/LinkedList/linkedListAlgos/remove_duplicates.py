# python -m LinkedList.linkedListAlgos.remove_duplicates

from LinkedList import LinkedList, Node

def remove_duplicates_sorted(Llist_head: Node) -> Node:
    """Remove Duplicates from Linked List Iteratively"""
    # TC: O(N)
    # SC: O(1)

    # Define the first node and next node
    curr_node = Llist_head
    next_node = Llist_head.next

    # Iterate till next node is not null
    while next_node:
        # Keep Moving until next node is same as curr node
        while next_node and (curr_node.data == next_node.data):
            next_node = next_node.next

        # Adjust the pointer
        curr_node.next = next_node
        curr_node = curr_node.next

    return Llist_head

def remove_duplicates_recursive_sorted(Llist_head: Node) -> Node:
    """Remove Duplicates from Linked List Recursively"""
    # TC: O(N)
    # SC: O(N)

    # Base Condition
    if not Llist_head.next:
        return Llist_head
    
    # Recursively Dedupe Sub List
    deduped_llist = remove_duplicates_recursive_sorted(Llist_head=Llist_head.next)

    if Llist_head.data == deduped_llist.data:
        Llist_head.next = deduped_llist.next

    return Llist_head


def remove_duplicates(Llist_head: Node) -> Node:
    """Remove Duplicates from Linked List Iteratively"""
    # TC: O(N)
    # SC: O(N)

    # Nodes Track
    nodes_found = set()

    # Define the Current node
    curr_node = Llist_head
    prev_node = Llist_head

    # Iterate till the end
    while curr_node:

        # Check if current_node data lies in Dict
        if curr_node.data in nodes_found:
            # Adjust the pointer
            prev_node.next = curr_node.next

        else:
            # Add Current Node data to list
            nodes_found.add(curr_node.data)
            prev_node = curr_node
        
        curr_node = curr_node.next
        
    return Llist_head

def main():

    # # Initialise a sorted Linked List
    # Llist = LinkedList(["1", "1", "2", "2", "2"])
    # print(f"Sorted Linked List: {Llist}")

    # deduped_llist_head = remove_duplicates_recursive_sorted(Llist_head=Llist.head)
    # deduped_llist_data = []
    # while deduped_llist_head:
    #     deduped_llist_data.append(deduped_llist_head.data)
    #     deduped_llist_head = deduped_llist_head.next

    # deduped_llist = LinkedList(deduped_llist_data)
    # print(f"Deduped Sorted Linked List: {deduped_llist}")


    # # Dedupe Llinked List Iteratively
    # deduped_llist = remove_duplicates_sorted(Llist.head)
    # deduped_llist_iter_data = []
    # while deduped_llist:
    #     deduped_llist_iter_data.append(deduped_llist.data)
    #     deduped_llist = deduped_llist.next

    # deduped_llist_iter = LinkedList(deduped_llist_iter_data)
    # print(f"Deduped Sorted Linked List iteratively: {deduped_llist_iter}")

    # Dedupe any Linked List
    Llist = LinkedList(["1", "2", "1", "3", "2", "1"])
    print(f"Sorted Linked List: {Llist}")

    deduped_llist = remove_duplicates(Llist.head)
    deduped_llist_data = []
    while deduped_llist:
        deduped_llist_data.append(deduped_llist.data)
        deduped_llist = deduped_llist.next

    deduped_llist_any = LinkedList(deduped_llist_data)
    print(f"Deduped Sorted Linked List iteratively: {deduped_llist_any}")

if __name__ == "__main__":
    main()
    