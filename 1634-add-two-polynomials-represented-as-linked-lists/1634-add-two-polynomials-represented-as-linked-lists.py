# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        curr = PolyNode()
        dummy = PolyNode(next = curr)
        head1 = poly1
        head2 = poly2
        while head1 and head2:
            if head1.power == head2.power:
                coeff = head1.coefficient + head2.coefficient 
                print(coeff)
                if coeff == 0:
                    head1 = head1.next
                    head2 = head2.next
                else:
                    new = PolyNode(x = coeff, y = head1.power)
                    curr.next = new
                    curr = curr.next
                    head1 = head1.next
                    head2 = head2.next     
            elif head1.power > head2.power:
                curr.next = head1
                curr = curr.next
                head1 = head1.next
            else:
                curr.next = head2
                curr = curr.next
                head2 = head2.next
            print(curr.coefficient, curr.power)
        
        if head2:
            curr.next = head2
        else:
            curr.next = head1

        return dummy.next.next
        

        


            