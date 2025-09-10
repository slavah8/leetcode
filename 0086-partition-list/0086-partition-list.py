# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = ListNode(-1)
        l2 = ListNode(-1)
        dummy1 = l1
        dummy2 = l2

        curr = head
        while curr:
            if curr.val < x:
                l1.next = ListNode(curr.val)
                l1 = l1.next
                curr = curr.next
            else:
                l2.next = ListNode(curr.val)
                l2 = l2.next
                curr = curr.next
        print(dummy1.next)
        print(dummy2.next)

        print(l1)
        print(l2)
        l1.next = dummy2.next
        return dummy1.next
