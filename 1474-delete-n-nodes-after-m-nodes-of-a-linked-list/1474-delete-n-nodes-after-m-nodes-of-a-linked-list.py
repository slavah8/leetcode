# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        curr = head
        dummy = ListNode(-1, curr)
        first = True
        while curr:
            if first:
                i = 1
                first = False
            else:
                i = 0
            while curr and i < m:
                curr = curr.next
                i += 1
            if not curr:
                break
            
            tmp = curr
            j = 0
            while tmp and j <= n:
                tmp = tmp.next
                j += 1
            if not tmp:
                curr.next = None
                break
            curr.next = tmp
        
        return dummy.next

