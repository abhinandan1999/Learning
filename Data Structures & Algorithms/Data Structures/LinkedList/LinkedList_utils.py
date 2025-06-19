# TODO
# 1. Insert
#   - Start
#   - End
#   - Before a Node
#   - After a Node

# 2. Remove
#   - Star
#   - End
#   - Before a Node
#   - After a Node

# 3. Retrieve
#   - From a Index


# Create a Node Class
class Node:
    def __init__(self, value):
        """
        Initialize the Node
        TC: (1)
        SC: O(1)
        """
        self.data = value
        self.next = None

    def __repr__(self):
        """
        String Representation of Data
        TC: O(1) for Primitive Data Type like int, float
            O(n) for Collection like List, Tupe
        SC: O(1) for Primitive Data Type like int, float
            O(n) for Collection like List, Tupe
        """
        return str(self.data)


# Create a LinkedList Class
class LinkedList:
    """Linked List Implementation"""

    def __init__(self, nodes=None):
        """
        Initialize the Linked List usings Iterators

        Args:
            nodes: (Iterable) (List, Tuple)

        Complexity:
            TC: O(n)
            SC: O(n)
        """
        # The only information we need to store a Linked List is the head (Starting of Linked List)
        self.head = None
        self.len = 0

        # Add individual elemnets as a Node
        if nodes is not None:
            node = Node(nodes.pop(0))  # Pop the first element from the Iterable
            self.head = node
            self.len += 1 # Increment the length by 1
            for ele in nodes:
                node.next = Node(ele)
                self.len += 1 # Increment the length by 1

                # Point to Next Node
                node = node.next

    def __repr__(self):
        """
        Represent Linked List as String

        Complexity:
            TC: O(n)
            SC: O(n)
        """
        node = self.head

        # Traverse the Node
        nodes_values = []
        while node is not None:
            # Append the value of Current Node to the List
            nodes_values.append(node.data)

            # Update the Current Node
            node = node.next

        # Return the List
        nodes_values.append("None")
        return " -> ".join(nodes_values)

    def __iter__(self):
        """
        Return the Element of Node

        Complexity:
            TC: O(n)
            SC: O(n)
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self.len

    def insertBeg(self, data):
        # TC: O(1)
        # SC: O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        # Increment the Length
        self.len += 1

        return 

    def insertEnd(self, data):
        # TC: O(n)
        # SC: O(1)
        new_node = Node(data)

        # Check if self.head is None
        if not self.head:
            self.head = new_node
            return 
        
        # Travel till End of Node
        for current_node in self:
            pass

        current_node.next = new_node

        # Increment the Length
        self.len += 1

        return

    def insertBefore(self, data, index):
        # TC: O(n)
        # SC: O(1)
        # Check if the Index is within Range
        if (index < 0) or (index > self.len - 1):
            raise Exception(f"Index {index} is out of Range. Length of Linked List {self.len}")
        
        # If the Index is 0 then it same as inserting at beginning
        if index == 0:
            self.insertBeg(data)

        new_node = Node(data)

        # Travel to the Index -1
        current_node = self.head
        for _ in range(0, index-1):
            current_node = current_node.next
        
        # Adjust the Links
        new_node.next = current_node.next
        current_node.next = new_node

        # Increment the Length by 1
        self.len += 1

        return 

    def inserAfter(self, data, index):
        # TC: O(1)
        # SC: O(1)
        # Check if the Index is within Range
        if (index < 0) or (index > self.len - 1):
            raise Exception(f"Index {index} is out of Range. Length of Linked List {self.len}")
        
        new_node = Node(data)

        # Travel till the Index
        current_node = self.head
        for _ in range(0, index):
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

        # Increment the length by 1
        self.len += 1

        return 
    
    def insert_index(self, data, index):
        pass
                
    def remove(self, data):
        """Deletes the specific Data if found"""
        # TC: O(N)
        # SC: O(1)

        # Check if LL is Null
        if not self.head:
            raise Exception("Linked List is empty")

        # Check if the data is at head
        if self.head.data == data:
            self.head = self.head.next

            # Adjust the Length
            self.len -= 1

            return 
        
        # Travel till the data
        previous_node = self.head
        for current_node in self:
            if current_node.data == data:
                # Adjust the links
                previous_node.next = current_node.next
                
                # Adjust the Length
                self.len -= 1
                return
            previous_node = current_node 

        raise Exception(f"{data} not found in Linked List")
        

    def remove_index(self, index):
        """Removes the specific Index"""

        # Check if the Index is within Range
        if (index < 0) or (index > self.len - 1):
            raise Exception(f"Index {index} is out of Range. Length of Linked List {self.len}")
        
        # Check if first element has to be removed
        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return
        
        # Travel Till Index - 1
        current_node = self.head
        for _ in range(0, index-1):
            current_node = current_node.next

        # Adjust the Links
        current_node.next = current_node.next.next
        self.len -= 1
        return 


def main():

    # Instantiate a LinkedList
    linked_list = LinkedList(["1", "2", "3", "4"])
    print(f"Intial Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {10} at Beginning")
    linked_list.insertBeg("10")
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")
    
    print(f"Inserting {20} at End")
    linked_list.insertEnd("20")
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {40} before index 4")
    linked_list.insertBefore("40", 4)
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {100} at after Index 2")
    linked_list.inserAfter("100", 6)
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")
    
    print(f"Removing 40 from the Linked List")
    linked_list.remove("40")
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Removing from index 3")
    linked_list.remove_index(6)
    print(f"Linked List of length {len(linked_list)} {linked_list}")
    # for ele in linked_list:
    #     print(ele)


if __name__ == "__main__":
    main()
