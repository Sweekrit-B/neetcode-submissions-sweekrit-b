# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # step 0 - create dummy nodes
        dummy = ListNode()
        dummy.next = head
        
        # step 1 - get to the left value
        prev = dummy
        curr = head
        n = 1
        while n < left:
            prev = curr
            curr = curr.next
            n += 1

        # step 2 - reverse from left to right
        before = prev # store the point before the start point
        start = curr # store a start point, which can then reference the last curr
        while n <= right:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
            n += 1
        start.next = curr # link the start (end of reversed) to curr (first node after)
        before.next = prev # link the before (first node before) to prev (start of reversed)
        
        return dummy.next
             