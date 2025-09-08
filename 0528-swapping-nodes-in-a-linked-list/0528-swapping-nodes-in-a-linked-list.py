# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        count = 1
        curr = head
        while count != k:
            curr = curr.next
            count += 1

        swap1_val = curr.val
        swap1_node = curr

        slow = fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        swap2_val = slow.val
        swap2_node = slow
        slow.val = swap1_val
        swap1_node.val = swap2_val

        return head




        
        
        
