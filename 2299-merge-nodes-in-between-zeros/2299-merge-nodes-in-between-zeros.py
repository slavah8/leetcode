# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        prev = dummy
        

        curr = head.next
        total = 0
        while curr:
            
            if curr.val == 0:
                new_node = ListNode(val = total)
                dummy.next = new_node
                dummy = dummy.next
                total = 0
            else:
                total += curr.val
            curr = curr.next
        
        return prev.next
            
            