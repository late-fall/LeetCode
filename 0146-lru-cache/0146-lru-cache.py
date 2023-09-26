class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodemap = {}
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right
        
    def get(self, key: int) -> int:
        if key in self.nodemap:
            self.remove(self.nodemap[key])
            self.insert(self.nodemap[key])
            return self.nodemap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodemap:
            self.remove(self.nodemap[key])
        self.nodemap[key] = Node(key,value)
        self.insert(self.nodemap[key])
        
        if len(self.nodemap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.nodemap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)