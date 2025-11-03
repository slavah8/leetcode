# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(node):
            nonlocal best
            if not node:
                return (0, 0)
            
            li, ld = dfs(node.left)
            ri, rd = dfs(node.right)

            inc = 1
            dec = 1

            if node.left:
                if node.left.val == node.val + 1: # increasing
                    inc = max(inc, li + 1)
                if node.left.val == node.val - 1: # decreasing
                    dec = max(dec, ld + 1)
            
            if node.right:
                if node.right.val == node.val + 1:
                    inc = max(inc, ri + 1)
                if node.right.val == node.val - 1:
                    dec = max(dec, rd + 1)
            
            best = max(best, inc + dec - 1)
            
            return (inc, dec)
        dfs(root)
        return best
