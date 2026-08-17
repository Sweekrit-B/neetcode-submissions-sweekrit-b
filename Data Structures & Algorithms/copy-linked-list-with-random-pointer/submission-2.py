"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmp = {}
        # first pass, add everything to hashmap
        curr = head
        while curr:
            hmp[curr] = Node(curr.val)
            curr = curr.next
        # second pass, link everything together
        curr = head
        while curr:
            next, random = curr.next, curr.random
            hmp[curr].next = hmp[next] if next else None
            hmp[curr].random = hmp[random] if random else None
            curr = curr.next
        
        return hmp[head] if head else None
        