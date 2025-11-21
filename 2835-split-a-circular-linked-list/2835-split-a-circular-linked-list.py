# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, root: Optional[ListNode]) -> List[Optional[ListNode]]:
        

        first = root
        curr = root
        length = 1
        while curr.next != first:
            curr = curr.next
            length += 1
        print(length)

        half = math.ceil(length / 2)
        print(half)
        first_half = ListNode(-1)
        curr = root
        first = root
        first_list_head = first
        
        for _ in range(half):
            first_half.next = curr
            first_half = first_half.next
            curr = curr.next
        first_half.next = first

        curr = curr # curr is at the beginning of the second list
        second_list_head = curr
        first = root
        while curr.next != first:
            curr = curr.next
        curr.next = second_list_head
        print(first_half)
        result = []
        result.append(first_list_head)
        result.append(second_list_head)
        return result
         
            


        