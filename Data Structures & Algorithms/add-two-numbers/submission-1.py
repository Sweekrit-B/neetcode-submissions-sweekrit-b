# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # idea:
            # go thorugh each node in the linked list for both l1 and l2
            # new value to final sum linked list = (l1.val + l2.val) % 10, and carryover is (l1.val + l2.val) // 10
            # add the carryover to the next result - keep it as a constant variable
        
        # edge cases
            # 1) there is a carryover but l1 and l2 are empty
            # 2) the sizes of l1 and l2 differ
                # in this case, while carryover exists (and continues to produce), will have to add iteratively
                # after that point, can just put in the next value
        
        dummy = ListNode()
        tail = dummy
        carryover = 0

        while l1 and l2:
            sum_nodes = l1.val + l2.val + carryover
            carryover = sum_nodes // 10
            val_appended = sum_nodes % 10
            # print(f"Appending {val_appended}, with carryover {carryover}")
            tail.next = ListNode(val_appended)
            
            # move all pointers forward
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while carryover and l1:
                sum_node = l1.val + carryover
                carryover = sum_node // 10
                val_appended = sum_node % 10
                tail.next = ListNode(val_appended)
                
                # move the pointers forward
                tail = tail.next
                l1 = l1.next
            # once there is no longer a carryover, you can just assign tail.next to the rest of l1
            tail.next = l1
        
        if l2:
            while carryover and l2:
                sum_node = l2.val + carryover
                carryover = sum_node // 10
                val_appended = sum_node % 10
                tail.next = ListNode(val_appended)
                
                # move the pointers forward
                tail = tail.next
                l2 = l2.next
            # once there is no longer a carryover, you can just assign tail.next to the rest of l1
            tail.next = l2
        
        if not l1 and not l2 and carryover:
            tail.next = ListNode(carryover)
            tail = tail.next
        
        return dummy.next
