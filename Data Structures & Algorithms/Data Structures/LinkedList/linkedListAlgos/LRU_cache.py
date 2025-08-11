# python -m LinkedList.linkedListAlgos.LRU_cache
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache():

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {} # Initialise a empty cache
        self.head = None # Initialise a head to keep track of Most recent get and put operation
        self.tail = None # Initialise a tail to keep track of the element to be deleted when capacity is full

    def _add_to_head(self, node):
        """Helper function to add node to head"""
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

    def _remove_node(self, node):

        if node is None:
            self.tail = None

        elif node.next is None:
            prevnode = node.prev
            prevnode.next = None
            self.tail = prevnode
            
        else:
            prevnode = node.prev
            nextnode = node.next
            prevnode.next = nextnode
            nextnode.prev = prevnode

    def get(self, key):

        # Check for the key in cache
        if key not in self.cache:
            return -1
        
        node = self.cache.get(key)
        
        # Remove the node from its existing place and move to head
        self._remove_node(node)
        self._add_to_head(node)

        return node.value
    
    def put(self, key, value):

        # If key is already present then update its value and move it to head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)

        else:
            new_node = Node(key=key, value=value)

            # Check if capacity is reached
            if len(self.cache) > self.capacity-1:
                # Remove the LRU node
                lru_node = self.tail
                print(lru_node.key, lru_node.value)
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

            self.cache[key] = new_node
            self._add_to_head(new_node)
            




def main():

    # Create a LRU Cache
    cache = LRUCache(2)

    # Add Element to Cache
    cache.put(1, 10)      # DLL: 1 → 
    cache.put(2, 20)      # DLL: 2 → 1
    print(cache.get(1))   # returns 10, DLL: 1 → 2
    
    cache.put(3, 30)      # evicts 2, DLL: 3 → 1
    print(cache.get(2))   # returns -1


if __name__ == "__main__":
    main()