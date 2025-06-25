# python -m LinkedList.linkedListAlgos.recursive_length

from LinkedList import LinkedList, Node

def len_llist(llist: Node) -> int:
    """Recursive function to get length of Linked List"""

    if not llist:
        return 0
    
    return 1 + len_llist(llist.next)

def main():

    # Initialize the Linked List
    llist = LinkedList(["1", "2", "3", "4"])

    llist_len = len_llist(llist.head)

    print(f"Length of Linked List is: {llist_len}")

if __name__ == "__main__":
    main()