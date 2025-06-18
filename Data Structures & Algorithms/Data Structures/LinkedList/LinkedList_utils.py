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
        pass

    def remove(self, data):
        """Deletes the specific Data if found"""
        pass

    def remove_index(self, index):
        """Removes the specific Index"""
        pass


def main():

    # Instantiate a LinkedList
    linked_list = LinkedList(["1", "2", "3"])

    print(type(linked_list))
    print(linked_list)
    print(len(linked_list))

    # for ele in linked_list:
    #     print(ele)


if __name__ == "__main__":
    main()
