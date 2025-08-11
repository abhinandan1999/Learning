# python -m LinkedList.linkedListAlgos.misc_linked_list
from LinkedList import LinkedList, Node


def find_kth_node_from_end(Llist: Node, k: int) -> Node:
    """Find the Kth Node from the end"""
    # TC: O()
    # SC: O()

    firstP = Llist
    secondP= Llist

    # Move the first pointer by k
    for _ in range(k):
        if not firstP.next:
            return None
        
        firstP = firstP.next

    # Now move both firstP and secondP by one
    while firstP:
        firstP = firstP.next
        secondP = secondP.next

    return secondP

def check_if_llist_is_palindrome(llist: Node) -> bool:
    """Check if given Linked List is palindrome"""
    # TC: O(N)
    # SC: O(1)

    # Travel till mid of Linked List using slowP and fastP approach
    slowP = fastP = llist

    while (fastP) and (fastP.next):
        slowP = slowP.next
        fastP = fastP.next.next

    
    # Reverse the second Half of the Linked List
    prevP, currP = None, slowP
    while currP:
        nextP = currP.next
        currP.next = prevP
        prevP = currP
        currP = nextP
    
    slowP_rev = prevP

    # Iterate and check element by element if they match
    currP = llist
    while slowP_rev:
        if slowP_rev.data != currP.data:
            return False
        
        slowP_rev = slowP_rev.next
        currP = currP.next

    return True

def get_intersection_of_llist(llist_head1: Node, llist_head2: Node) -> Node:
    """Get Intersection of Two Node"""
    # TC: O(N)
    # SC: O(1)
    
    headA = llist_head1
    headB = llist_head2

    # Step 1: Travel Both the linked list one by one
    # Step 2: If reached end of one linked List set it to start of Other one
    # Step 3: If there is intersection, then they will meet else both of them would be none
    
    while headA is not headB:
        headA = headA.next if headA else llist_head1
        headB = headB.next if headB else llist_head2
    
    return headA


def rotate_linked_list(llist_head: Node, k: int) -> Node:
    """Rotate Linked Linked by K element"""
    # TC: 
    # SC: 

    # Step 1: Find the length and tail of Linked List
    length = 1
    tail = llist_head
    while tail.next:
        length += 1
        tail = tail.next

    # Step 2: Check if k is multiple of N
    if k % length == 0:
        return llist_head
    
    # Step 3: Adjust the pointer of tail to point to head (Creating a circular list)
    head = llist_head
    tail.next = head

    # Step 4: Travel the tail by (n - k)
    for _ in range(length - k):
        tail = tail.next

    # Step 5: Adjust the Pointers
    new_head = tail.next
    tail.next = None

    return new_head


def main():

    # # Find Kth Node from end
    # llist = LinkedList(["1", "2", "3", "4", "5"])
    # print(f"Original Linked List is: {llist}")
    # kNode = find_kth_node_from_end(Llist=llist.head, k=2)
    # print(kNode)

    # Check if Linked List is Palindrome
    # llist = LinkedList(["1", "2", "2", "1"])
    # print(f"Original Linked List: {llist}")
    # palindrome = "palindrome" if check_if_llist_is_palindrome(llist.head) else "not palindrome"
    # print(f"Given Linked List is {palindrome}")

    # # Find Intersection of Two Linked List
    # n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4); n5 = Node(5)
    # n8 = Node(8); n9 = Node(9)

    # n1.next = n2; n2.next = n8
    # n3.next = n4; n4.next = n5; n5.next = n8
    # n8.next = n9

    # intersection = get_intersection_of_llist(n1, n3)
    # print(intersection.data if intersection else None)

    # Rotate the Linked List by k elements
    llist = LinkedList(["1", "2", "2", "1", "5"])
    print(f"Original Linked List: {llist}")

    rotated_llist = rotate_linked_list(llist_head=llist.head, k=2)
    rotated_llist_data = []
    while rotated_llist:
        rotated_llist_data.append(rotated_llist.data)
        rotated_llist = rotated_llist.next
    print(f"Rotated Linked List: {LinkedList(rotated_llist_data)}")



if __name__ == "__main__":
    main()