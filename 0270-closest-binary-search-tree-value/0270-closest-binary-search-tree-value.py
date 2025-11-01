# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = None
        INF = 10 ** 15
        best_diff = INF
        def dfs(node):
            if not node:
                return
            nonlocal ans, best_diff
            cand_diff = abs(node.val - target)
            if ans is None or cand_diff < best_diff or (cand_diff == best_diff and node.val < ans):
                best_diff = cand_diff
                ans = node.val
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        
        dfs(root)
        return ans
        