# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 10
        second = INF
        first = INF

        def dfs(node):
            nonlocal first, second
            if not node:
                return
            if first == INF:
                first = node.val
            if first != INF and node.val != first and node.val < second:
                second = node.val
                return

            dfs(node.right)
            dfs(node.left)
                    
        dfs(root)
        return second if second != INF else -1