# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        ans = 0
        component = []
        c = []
        curr = head
        while curr:
            if curr.val in nums:
                component.append(curr.val)
                curr = curr.next
            else:
                c.append(component)
                component = []
                curr = curr.next
        if len(component) != 0:
            c.append(component)
        
        for comp in c:
            if len(comp) != 0:
                ans += 1
        return ans


            

            

            
        