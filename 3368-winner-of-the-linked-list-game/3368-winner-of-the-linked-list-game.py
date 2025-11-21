# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        curr = head
        even = 0
        odd = 0
        while curr and curr.next:
            if curr.val > curr.next.val: # even wins
                even += 1
            else:
                odd += 1
            curr = curr.next.next
        print(even)
        print(odd)
        if even > odd:
            return 'Even'
        elif even < odd:
            return 'Odd'
        else:
            return 'Tie'