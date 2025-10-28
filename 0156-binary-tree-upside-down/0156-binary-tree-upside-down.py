# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if not root:
            return 
        
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        # leftmost node becomes the root
        new_root = stack.pop()
        curr = new_root
        print(stack)
        while stack:
            parent = stack.pop()

            curr.left = parent.right
            curr.right = parent

            parent.left = None
            parent.right = None

            # Our invariant is: curr is the node whose left child we just processed,
            # and we’re building the flipped chain from bottom to top
            curr = parent
        return new_root
        