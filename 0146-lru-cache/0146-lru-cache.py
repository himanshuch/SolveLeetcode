class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val = key, val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.tail= ListNode(0, 0)
        self.head = ListNode(0, 0, self.tail)
        self.tail.prev = self.head
        self.cache, self.capacity = {}, capacity

    def get(self, key: int) -> int:
        cache = self.cache
        if key in cache:
            self.update(key, cache[key])
            return cache[key].val
        else:
            return -1

    def update(self, key: int, node, newValue=None):
        cache, capacity, head, tail =  self.cache, self.capacity, self.head, self.tail

        #node = cache[key] 
        # deleting the node present between doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.insert(head, key, newValue if newValue else node.val)
        cache[key] = head.next
        #print("u", tail.prev.key, tail.prev.val, cache[key].val)   

    def insert(self, head, key, val):
        #connecting nodes by adding new node immediately after head i.e head->next
        n = head.next 
        head.next = ListNode(key, val)
        head.next.next = n
        head.next.prev = head
        head.next.next.prev = head.next

    def put(self, key: int, value: int) -> None:
        cache, capacity, head, tail =  self.cache, self.capacity, self.head, self.tail 
        if key in cache:
            self.update(key, cache[key], value)
            return
            
        if len(cache)>=capacity:
            # evict least recently used cache i.e tail->prev
            p = tail.prev # this is the node getting deleted.
            tail.prev = tail.prev.prev
            p.prev.next = tail
            del cache[p.key]
        
        self.insert(head, key, value)
        # update hashmap with key and node
        cache[key] = head.next
        #print("put", tail.prev.key, tail.prev.val)     


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)