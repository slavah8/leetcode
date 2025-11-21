# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        freq = defaultdict(int)
        curr = head
        while curr:
            x = curr.val
            freq[x] += 1
            curr = curr.next
        
        prev = ListNode(-1)
        new_head = prev
        curr = head
        while curr:
            x = curr.val
            if freq[x] > 1:
                prev.next = None
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next
        return new_head.next
        
        
