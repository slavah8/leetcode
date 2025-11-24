# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 10
        best = 0
        def dfs(node):
            nonlocal best
            if not node:
                return INF, -INF
            
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)

            if left_min != INF or right_min != INF:
                diff_min = abs(node.val - min(left_min, right_min))
                diff_max = abs(node.val - max(left_max, right_max))
                best = max(best, diff_min, diff_max)

            return min(left_min, right_min, node.val), max(left_max, right_max, node.val)

        
        dfs(root)
        return best