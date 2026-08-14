class Node:
    def __init__(self, val: Optional[int] = None, key: Optional[int] = None, prev: Optional[Node] = None, nxt: Optional[Node] = None):
        self.val = val
        self.key = key
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.hmp = {}
        # create the start and end nodes
        self.start = Node()
        self.end = Node()
        # set them to be doubly linked to each other
        self.start.nxt = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key in self.hmp:
            curr_node = self.hmp[key]
            self.move_to_front(curr_node)
            # return the value
            return self.hmp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmp:
            curr_node = self.hmp[key]
            curr_node.val = value
            self.move_to_front(curr_node)
        else:
            # create a new value in the hashmap
            curr_node = Node(value, key)
            self.hmp[key] = curr_node
            # if we are currently at capacity
            if self.curr_size == self.capacity:
                # remove the least recently used value
                lru_node = self.end.prev
                lru_node.prev.nxt = self.end
                self.end.prev = lru_node.prev
                del self.hmp[lru_node.key]
                # update current size to be decremented
                self.curr_size -= 1
            # update current size
            self.curr_size += 1
            # add this to the start
            self.add_to_front(curr_node)
    
    def move_to_front(self, curr_node):
        # grab the previous and the next node values
        prev_node = curr_node.prev
        next_node = curr_node.nxt
        # reassign them to look at each other
        prev_node.nxt = next_node
        next_node.prev = prev_node
        # send the curr_node to the front of the linked list
        self.add_to_front(curr_node)
    
    def add_to_front(self, curr_node):
        old_front = self.start.nxt
        curr_node.prev = self.start
        curr_node.nxt = old_front
        self.start.nxt = curr_node
        old_front.prev = curr_node