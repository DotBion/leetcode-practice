class Node :
    def __init__(self, k:int, v:int, p=None, n=None) :
        self.key = k
        self.value = v
        self.prev = p
        self.next = n

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = None  # LRU
        self.tail = None  # MRU

    def remove(self, node) :
        #detach node from DLL
        if node.prev :
            #there exists a previous node
            node.prev.next = node.next
        else :
            #no prev node hence head
            self.head = node.next
        if node.next :
            #there exists a next node
            node.next.prev = node.prev
        else :
            #no next node exists
            self.tail = node.prev

    def addtoMRU(self, node) :
        #append node at tail
        #present tail becomes the prev node to this node
        node.prev = self.tail
        node.next = None

        #update present tail 
        if self.tail :
            self.tail.next = node
        else :
            #only head
            self.head = node
        #update the new tail
        self.tail = node

    def get(self, key: int) -> int:
        #if key dne return -1
        if key not in self.hashmap :
            return -1
        #if exists return the node value and move node to addtoMRU
        node = self.hashmap[key]
        self.remove(node)
        self.addtoMRU(node)
        
        return node.value


    def put(self, key: int, value: int) -> None:
        #if key already present, update value and move to MRU
        if key in self.hashmap :
            node = self.hashmap[key]
            node.value = value
            #move to MRU
            self.remove(node)
            self.addtoMRU(node)
            return

        #if cache full - evict lru
        if len(self.hashmap) == self.capacity :
            #its always the head node
            lru = self.head
            #remove and delete the key from hashmap
            self.remove(lru)
            del self.hashmap[lru.key]

        #add to new node as MRU - create new node, addtoMRU and add key to hasmap
        mru = Node(key,value)
        self.addtoMRU(mru)
        self.hashmap[key] = mru


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)