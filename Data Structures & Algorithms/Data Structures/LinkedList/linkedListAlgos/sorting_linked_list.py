# python -m LinkedList.linkedListAlgos.sorting_linked_list

from LinkedList import LinkedList, Node


def merge_sorted_ll(Llist1: LinkedList, Llist2: LinkedList) -> LinkedList:
    """
    Merge two sorted linked List
    """
    # TC: O()
    # SC: O()

    # Check if Both are Null
    if not Llist1 and not Llist2:
        return Llist1
    
    # Check if any Llist 1 is Null
    if not Llist1:
        return Llist2
    
    # Check if Llist 2 is Null
    if not Llist2:
        return Llist1
    
    # Set the Current Position of both First and Second Linked List
    first_curr_p = Llist1.head
    second_curr_p = Llist2.head
    
    # If both are Not Null, get the final head and First LL Curr Pointer and Second LL current pointer
    final_head, first_curr_p, second_curr_p = (
        (Llist1, first_curr_p.next, second_curr_p) 
        if first_curr_p.data < second_curr_p.data 
        else (Llist2, first_curr_p, second_curr_p.next)
    )
    
    # Set the Min Pointer (Which always points to minimum value two Linked List)
    min_p = final_head.head

    

    # Iterate till first_curr_p is None or second_curr_p is None
    while (first_curr_p and second_curr_p):

        if first_curr_p.data < second_curr_p.data:
            # Set the Next Node of min_p
            min_p.next = first_curr_p
            
            # Set the new Min Pointer
            min_p = min_p.next

            # Move the first current pointer
            first_curr_p = first_curr_p.next

        else:
            # Set the Next Node of min_p
            min_p.next = second_curr_p

            # Set the new Min Pointer
            min_p = min_p.next

            # Move the first current pointer
            second_curr_p = second_curr_p.next

    # Set the Last Node
    if not first_curr_p:
        min_p.next = second_curr_p
    else:
         min_p.next = first_curr_p
        
    return final_head

def main():

    # Initialise Linked List 1
    llist1 = LinkedList(["1", "1", "4"])
    print(f"Linked List 1: {llist1}")

    # Initialise Linked List 2
    llist2 = LinkedList(["0", "0", "3"])
    print(f"Linked List 2: {llist2}")

    # Sorted Linked List
    sorted_llist = merge_sorted_ll(Llist1=llist1, Llist2=llist2)
    print(f"Sorted Merged Linked List: {sorted_llist}")

if __name__ == "__main__":

    main()

