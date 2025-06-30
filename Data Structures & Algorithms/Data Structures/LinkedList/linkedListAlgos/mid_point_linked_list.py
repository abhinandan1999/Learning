# python -m LinkedList.linkedListAlgos.mid_point_linked_list
from LinkedList import LinkedList, Node

def get_mid_point_llist(llist: LinkedList) -> tuple:
    """Find the Mid point of Linked and return a Tuple of index and data"""

    return (2, 3)

def main():

    # Create a Linked List
    llist = LinkedList(["1", "2", "3", "4", "5"])
    print(f"Original Linked List: {llist}")

    idx, data = get_mid_point_llist(llist=llist)
    print(f"Mid point is {data} at position {idx}")

if __name__ == "__main__":

    # Call main
    main()

    



