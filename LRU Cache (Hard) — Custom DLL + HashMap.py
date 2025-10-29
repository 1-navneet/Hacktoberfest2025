class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        
        self.left = Node(0,0)   # LRU
        self.right = Node(0,0)  # MRU
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def insert(self, node):
        p, n = self.right.prev, self.right
        p.next = n.prev = node
        node.prev, node.next = p, n

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
