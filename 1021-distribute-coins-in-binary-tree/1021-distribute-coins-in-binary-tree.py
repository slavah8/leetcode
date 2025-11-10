# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)
            # total coins in subtree - total nodes in subtree
            moves += abs(L) + abs(R)
            return node.val + L + R - 1 # surplus of this node

        dfs(root) 
        return moves