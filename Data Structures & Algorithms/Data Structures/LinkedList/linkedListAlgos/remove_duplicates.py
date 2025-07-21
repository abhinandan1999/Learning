# python -m LinkedList.linkedListAlgos.remove_duplicates

from LinkedList import LinkedList, Node

def remove_duplicates(Llist_head: Node) -> Node:
    """Remove Duplicates from Linked List Iteratively"""
    # TC: O()
    # SC: O()

    return Llist_head

def remove_duplicates_recursive(Llist_head: Node) -> Node:
    """Remove Duplicates from Linked List Recursively"""
    # TC: O(N)
    # SC: O(N)

    # Base Condition
    if not Llist_head.next:
        return Llist_head
    
    # Recursively Dedupe Sub List
    deduped_llist = remove_duplicates_recursive(Llist_head=Llist_head.next)

    if Llist_head.data == deduped_llist.data:
        Llist_head.next = deduped_llist.next

    return Llist_head

def main():

    # Initialise a sorted Linked List
    Llist = LinkedList(["1", "1", "2", "2", "3"])
    print(f"Sorted Linked List: {Llist}")

    deduped_llist_head = remove_duplicates_recursive(Llist_head=Llist.head)
    deduped_llist_data = []
    while deduped_llist_head:
        deduped_llist_data.append(deduped_llist_head.data)
        deduped_llist_head = deduped_llist_head.next

    deduped_llist = LinkedList(deduped_llist_data)
    print(f"Deduped Sorted Linked List: {deduped_llist}")

if __name__ == "__main__":
    main()
    