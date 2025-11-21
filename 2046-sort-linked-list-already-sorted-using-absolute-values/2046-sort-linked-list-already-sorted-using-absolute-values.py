# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        positive_head = ListNode(-1)
        negative_head = ListNode(-1)
        head1 = positive_head
        head2 = negative_head
        curr = head
        while curr:
            x = curr.val
            if curr.val >= 0: # positive
                positive_head.next = ListNode(curr.val)
                curr = curr.next
                positive_head = positive_head.next
            else:
                negative_head.next = ListNode(curr.val)
                curr = curr.next
                negative_head = negative_head.next
        
        curr = head2.next
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        pos = head1.next
        neg = prev
        curr = ListNode(-1)
        new_head = curr
        while pos or neg:
            if neg:
                curr.next = neg
                neg = neg.next
                curr = curr.next
            else:
                curr.next = pos
                pos = pos.next
                curr = curr.next
        return new_head.next

        
