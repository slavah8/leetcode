"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        head = None
        prev = None
        def inorder(node):
            nonlocal head, prev
            if not node:
                return
            
            inorder(node.left)
            
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node # first node is the head
            prev = node
            inorder(node.right)
        inorder(root)
        head.left = prev
        prev.right = head
        return head
