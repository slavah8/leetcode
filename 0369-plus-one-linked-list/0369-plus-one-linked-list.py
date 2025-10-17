# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        prev = reverse(head)
        dummy1 = ListNode(-1, prev)
        curr = prev
        while curr:
            if curr.val < 9:
                curr.val += 1
                return reverse(dummy1.next)
            else:
                curr.val = 0
                curr = curr.next
        
        node1 = ListNode(1)
        dummy2 = ListNode(-1, node1)
        
        node1.next = dummy1.next
        return dummy2.next