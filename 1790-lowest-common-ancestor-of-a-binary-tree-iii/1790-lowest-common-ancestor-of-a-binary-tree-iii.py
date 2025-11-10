"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        cur = p
        pathP = [] # path from p to root
        while cur:
            pathP.append(cur.val)
            cur = cur.parent
        

        cur = q
        pathQ = []
        while cur:
            pathQ.append(cur.val)
            cur = cur.parent
        
    
        pathQ.reverse()
        pathP.reverse()
        print(pathP)
        print(pathQ)
        i = 0
        while i < len(pathQ) and i < len(pathP) and pathQ[i] == pathP[i]:
            i += 1
    
        return Node(pathQ[i - 1])
    
        
