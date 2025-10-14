# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 10
        self.best = 0
        # returns is_bst, min, max, sum
        def dfs(node):

            if not node:
                return True, INF, -INF, 0
            
            left_is_bst, left_min, left_max, l_sum = dfs(node.left)
            right_is_bst, right_min, right_max, r_sum = dfs(node.right)

            x = node.val
            # BST validity at this node
            if left_is_bst and right_is_bst and (left_max < x < right_min):
                s = l_sum + r_sum + x
                self.best = max(self.best, s) 
                return True, min(left_min, x), max(right_max, x), s
            else:
                return False, INF, -INF, 0
        dfs(root)
        return self.best

