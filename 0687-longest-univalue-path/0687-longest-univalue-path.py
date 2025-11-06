# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        longest = 0
        
        # returns the maximum number of consecutive nodes that are present 
        # on either the left or right side of the root
        def dfs(node, parent):
            nonlocal longest
            if not node:
                return 0
            
            left = dfs(node.left, node.val) if node.left else 0
            right = dfs(node.right, node.val) if node.right else 0

            longest = max(longest, left + right)

            return (max(left, right) + 1) if node.val == parent else 0
            
    
        dfs(root, -1)
        return longest
            
