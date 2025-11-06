# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node):
            nonlocal total
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            summ = left_sum + right_sum
            tilt = abs(left_sum - right_sum)
            total += tilt

            return node.val + summ
        
        dfs(root)
        return total


        
