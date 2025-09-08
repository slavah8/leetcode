# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        # first lets find the depth

        max_depth = 0

        def dfs(node, depth):
            nonlocal max_depth

            if not node:
                return
            
            if not node.left and not node.right: # found leaf
                max_depth = max(max_depth, depth)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)

        total = 0
        def calculate(node, depth):
            nonlocal total
            if not node:
                return
            
            if not node.left and not node.right and depth == max_depth:
                total += node.val
                return
            
            calculate(node.left, depth + 1)
            calculate(node.right, depth + 1)

        calculate(root, 0)
        return total
            

        