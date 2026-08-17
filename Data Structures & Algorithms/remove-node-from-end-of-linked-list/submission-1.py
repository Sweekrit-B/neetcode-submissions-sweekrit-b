# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two potential methods here
            # 1) iterate through the list once, finding its length, and then removing the length - nth pointer
            # 2) reverse the linked list, remove the nth pointer, reverse it again
        
        # step 0: create the dummy node
        dummy = ListNode(0)
        dummy.next = head

        # step 1: find the length of the linked list
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        # step 2: find the value to remove
        index_to_remove = length - n
        curr = dummy
        i = 0

        while i < index_to_remove:
            curr = curr.next
            i += 1
        
        # step 3: remove said value
        curr.next = curr.next.next

        return dummy.next
        