# python -m LinkedList.linkedListAlgos.sorting_linked_list

from LinkedList import LinkedList, Node


def merge_sorted_ll_recursive(Llist1_head: Node, Llist2_head: Node) -> Node:
    """Recursively merge two sorted Linked List"""
    # TC: O(1)
    # SC: O(M+N) Due to memory consumed by recursive stack

    # Write Base Condition
    # Check if any Llist 1 is Null
    if not Llist1_head:
        return Llist2_head
    
    # Check if Llist 2 is Null
    if not Llist2_head:
        return Llist1_head
    
    if Llist1_head.data < Llist2_head.data:
        sorted_llist = merge_sorted_ll_recursive(Llist1_head=Llist1_head.next, Llist2_head=Llist2_head)
        Llist1_head.next = sorted_llist
        return Llist1_head

    else:
        sorted_llist = merge_sorted_ll_recursive(Llist1_head=Llist1_head, Llist2_head=Llist2_head.next)
        Llist2_head.next = sorted_llist
        return Llist2_head

    


def merge_sorted_ll(Llist1_head: Node, Llist2_head: Node) -> Node:
    """
    Merge two sorted linked List
    """
    # TC: O(M + N) = O(N)
    # SC: O(1)

    # Check if any Llist 1 is Null
    if not Llist1_head:
        return Llist2_head
    
    # Check if Llist 2 is Null
    if not Llist2_head:
        return Llist1_head
    
    # Set the Current Position of both First and Second Linked List
    first_curr_p = Llist1_head
    second_curr_p = Llist2_head

    # Initialise min_p
    min_p = Node("dummy")
    final_llist = min_p

    # Iterate till first_curr_p is None or second_curr_p is None
    while (first_curr_p and second_curr_p):

        if first_curr_p.data < second_curr_p.data:
            # Set the Next Node of min_p
            min_p.next = first_curr_p

            # Move the first current pointer
            first_curr_p = first_curr_p.next
        else:
            # Set the Next Node of min_p
            min_p.next = second_curr_p

            # Move the first current pointer
            second_curr_p = second_curr_p.next

        # Set the new Min Pointer
        min_p = min_p.next

    # Set the Last Node
    if not first_curr_p:
        min_p.next = second_curr_p
    else:
         min_p.next = first_curr_p
    
    print(type(final_llist.next))
    return final_llist.next

def main():

    # Initialise Linked List 1
    llist1 = LinkedList(["1", "1", "4"])
    print(f"Linked List 1: {llist1}")

    # Initialise Linked List 2
    llist2 = LinkedList(["0", "0", "3"])
    print(f"Linked List 2: {llist2}")

    # Sorted Linked List
    sorted_llist_head = merge_sorted_ll(Llist1_head=llist1.head, Llist2_head=llist2.head)
    sorted_llist_data = []
    while sorted_llist_head:
        sorted_llist_data.append(sorted_llist_head.data)
        sorted_llist_head = sorted_llist_head.next

    sorted_llist = LinkedList(sorted_llist_data)
    print(f"Sorted Merged Linked List: {sorted_llist}")


    # Sorted Linked List Recursively

    # Initialise Linked List 1
    llist1_rec = LinkedList(["1", "1", "4"])
    print(f"Linked List 1: {llist1}")

    # Initialise Linked List 2
    llist2_rec = LinkedList(["0", "0", "3"])
    print(f"Linked List 2: {llist2}")


    sorted_llist_head_rec = merge_sorted_ll_recursive(Llist1_head=llist1_rec.head, Llist2_head=llist2_rec.head)
    sorted_llist_data_rec = []
    while sorted_llist_head_rec:
        sorted_llist_data_rec.append(sorted_llist_head_rec.data)
        sorted_llist_head_rec = sorted_llist_head_rec.next

    sorted_llist_rec = LinkedList(sorted_llist_data_rec)
    print(f"Sorted Merged Linked List Recursively: {sorted_llist_rec}")
    

if __name__ == "__main__":

    main()

