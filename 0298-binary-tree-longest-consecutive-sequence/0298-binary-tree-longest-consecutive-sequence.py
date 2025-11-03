# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        best = 0
        def dfs(node, prev, cur_length):
            nonlocal best
            if cur_length > best:
                best = cur_length

            if not node:
                return 
            
            if prev is not None and node.val == prev + 1:
                dfs(node.left, node.val, cur_length + 1)
                dfs(node.right, node.val, cur_length + 1)
            else:
                dfs(node.left, node.val, 1)
                dfs(node.right, node.val, 1)


        dfs(root, None, 1)
        return best
            

            
