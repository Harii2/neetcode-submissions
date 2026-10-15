class Node:
    def __init__(self, key=0, val=0):
        self.key = key 
        self.val = val 
        self.next = None 
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_key = {}
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left
    
        

    def get(self, key: int) -> int:
        if key not in self.cache_key:
            return -1 
        
        node = self.cache_key[key]
        self.remove(node)
        self.insert(node)

        return node.val 

        
    
    def remove(self, node):
        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node 
        next_node.prev = prev_node

    
    def insert(self, node):
        prev_node = self.right.prev 
        prev_node.next = node
        node.prev = prev_node 

        node.next = self.right
        self.right.prev = node 



    def put(self, key: int, value: int) -> None:
        if key in self.cache_key:
            self.remove(
                self.cache_key[key]
            )
        
        node = Node(key, value)
        self.cache_key[key] = node 
        self.insert(node)

        if len(self.cache_key) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache_key[lru.key]
        
