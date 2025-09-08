# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        before_a = None
        after_b = None
        dummy = ListNode(-1)
        dummy.next = list1

        count1 = 0
        ptr1 = list1
        while count1 + 1 < a:
            ptr1 = ptr1.next
            count1 += 1
        before_a = ptr1

        for _ in range(b - a + 2):
            ptr1 = ptr1.next
        after_b = ptr1

        before_a.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = after_b
        return dummy.next
    



        

