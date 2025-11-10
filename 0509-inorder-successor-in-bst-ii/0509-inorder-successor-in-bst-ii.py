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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None

        # if the node has a right child, go right then all the way to the left
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        
        # if no right subtree, need the lowest ancestor
        # # Case 2: climb up to the first ancestor where we came from its left side
        curr = node
        # While cur is a right child of its parent, the parent is less than this node
        # so keep going up
        # first time we are not a right child, we are the left child so return the parent
        while curr.parent and curr is curr.parent.right:
            curr = curr.parent
        return curr.parent

                