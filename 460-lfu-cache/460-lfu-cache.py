from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, k, v, cnt):
        self.k = k
        self.v = v
        self.cnt = cnt # Use cnt
        

class LFUCache:
    from collections import Counter, OrderedDict

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2Node = {}
        self.cnt2Nodes = defaultdict(OrderedDict) # count,key->node
        self.lfuPtr = None # Pointer in cnt2Nodes for lfu
        

    def get(self, key: int) -> int:
        if key not in self.key2Node:
            return -1
        
        # Otherwise, we need to update the usages
        
        # cnt2Nodes's count need to be updated
        
        node = self.key2Node[key]
        del self.cnt2Nodes[node.cnt][node.k]
        
        if len(self.cnt2Nodes[node.cnt]) == 0:
            del self.cnt2Nodes[node.cnt]
        
        node.cnt+=1
        self.cnt2Nodes[node.cnt][node.k] = node
        
        if self.lfuPtr not in self.cnt2Nodes: # checks if we need to update lfu in case we changed the value
            self.lfuPtr += 1
        
        return node.v
        

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return None
        
        # putting it in,
        if key in self.key2Node:
            self.key2Node[key].v = value
            self.get(key)
            return None
        
        # we need to remove an old one
        if len(self.key2Node) == self.cap:
            tmpK, _ = self.cnt2Nodes[self.lfuPtr].popitem(last=False)
            del self.key2Node[tmpK]
        
        
        # Make the key
        n = Node(key, value, 1)
        self.key2Node[key] = n
        self.cnt2Nodes[1][key] = n
        self.lfuPtr = 1
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)