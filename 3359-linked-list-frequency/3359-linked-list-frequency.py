# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        freq = defaultdict(int)

        curr = head
        while curr:
            val = curr.val
            freq[val] += 1
            curr = curr.next
        print(freq)

        curr = ListNode(-1)
        dummy = ListNode(-1)
        dummy.next = curr
        for val, cnt in freq.items():
            x = ListNode(cnt)
            curr.next = x
            curr = curr.next
        return dummy.next.next


            