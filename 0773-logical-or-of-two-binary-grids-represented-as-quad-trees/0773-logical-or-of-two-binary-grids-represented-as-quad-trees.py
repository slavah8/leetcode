"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, t1: 'Node', t2: 'Node') -> 'Node':
        
        if t1.isLeaf and t1.val:
            return Node(True, True, None, None, None, None)
        if t2.isLeaf and t2.val:
            return Node(True, True, None, None, None, None)

        # if a leaf is false then the result is just the other subtree
        if t1.isLeaf and not t1.val:
            return t2
        if t2.isLeaf and not t2.val:
            return t1

        tl = self.intersect(t1.topLeft, t2.topLeft)
        tr = self.intersect(t1.topRight, t2.topRight)
        bl = self.intersect(t1.bottomLeft, t2.bottomLeft)
        br = self.intersect(t1.bottomRight, t2.bottomRight)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val and tr.val and bl.val and br.val:
            return Node(True, True, None, None, None, None)
        
        return Node(True, False, tl, tr, bl, br)
    
        

        