# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ''
        def dfs(node):
            nonlocal string
            if not node:
                return

            string += str(node.val)
            if not node.left and node.right: # empty () for left child
                string += '('
                string += ')'

            if node.left:
                string += '('
                dfs(node.left)
                string += ')'
            if node.right:
                string += '('
                dfs(node.right)
                string += ')'
        
        dfs(root)
        return string

            
