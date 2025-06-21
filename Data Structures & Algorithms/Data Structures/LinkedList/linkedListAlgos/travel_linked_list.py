from LinkedList import LinkedList

def recursive_travel(llist: LinkedList) -> None:
    """Algorithm to Travel Linked List Recursively"""

    # Base Condition
    if not llist.head:
        return
    
    print(llist.head.data)
    llist.head = llist.head.next
    recursive_travel(llist=llist)

    return

def main():

    # Create a Linked List
    llist = LinkedList(["1", "2", "3", "443432432432"])

    recursive_travel(llist)

    print(llist)
    
if __name__ == "__main__":
    main()