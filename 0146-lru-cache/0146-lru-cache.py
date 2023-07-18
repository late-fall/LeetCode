class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
#     NEETCODE solution
# to know the value right away (O(1)) with the key, we will use hashmap.
# make value to be the pointer to itself. 
# keep most recently used using two pointers.
# Left is least frequent
# Right is most frequent
# Use double linked list
# EAch node will look like (node, (key,val), prev, next)

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        # left = LRU, right = Most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        # self.cache = {}
        # self.length = capacity
        # self.h = []
        # heapq.heapify(h)

    # helper function, remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert at right helper function. 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
#         if key in self.cache:
            
#             return self.cache[key]
#         else:
#             return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove and delete LRU from the cache hashmap. 
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        # if len(self.cache) < self.length:
        #     self.cache[key] = value
        #     heapq.heappush(h, (1, key))
        # self.recent = key
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)