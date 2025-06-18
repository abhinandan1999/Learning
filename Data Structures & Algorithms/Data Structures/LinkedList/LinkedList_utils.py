# Create a Node Class
class Node:
    def __init__(self, value):
        """Initialize the Node"""
        self.data = value  # TC: O(1), SC: O(1)
        self.next = None  # TC: O(1), SC: O(1)

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

    def insert(self, data, index):
        """Insert the Element at a specific Index"""
        
        # Check if the Index is greater than Length of Linked List + 1
        if index > self.len:
            raise Exception(f"Index {index} is greater than Linked List of length {self.len}")
        
        else:
            
            # Create an instance of Node
            node_to_insert = Node(data)  

            # Travel to the Index
            node = head = self.head
            curr_pos = 0
            while curr_pos < index-1:
                node = node.next
                curr_pos += 1

            # Set the Next Node
            if index == 0:
                self.head = node_to_insert
                node_to_insert.next = node
            else:
                node_to_insert.next = node.next
                node.next = node_to_insert


            # Increment the Length of Linked List by 1
            self.len += 1
                
    def remove(self, data):
        """Deletes the specific Data if found"""
        pass

    def remove_index(self, index):
        """Removes the specific Index"""
        pass


def main():

    # Instantiate a LinkedList
    linked_list = LinkedList(["1", "2", "3", "4"])
    print(f"Intial Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {10} at Index {0}")
    linked_list.insert("10", 0)
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")
    
    print(f"Inserting {20} at Index {1}")
    linked_list.insert("20", 1)
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {40} at Index {4}")
    linked_list.insert("40", 4)
    print(f"Linked List of length {len(linked_list)} {linked_list}\n")

    print(f"Inserting {100} at Index {len(linked_list)}")
    linked_list.insert("100", len(linked_list))
    print(f"Linked List of length {len(linked_list)} {linked_list}")
    
    # for ele in linked_list:
    #     print(ele)


if __name__ == "__main__":
    main()
