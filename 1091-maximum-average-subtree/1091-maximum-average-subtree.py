# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxx = 0
        # return (# of nodes, sum)

        def dfs(node):
            nonlocal maxx
            summ = 0
            if not node:
                return (0, 0)

            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)

            summ = node.val + left_sum + right_sum
            count = left_count + right_count + 1
            avg = summ / count
            maxx = max(maxx, avg)

            return (count, summ)
            

        dfs(root)
        return maxx