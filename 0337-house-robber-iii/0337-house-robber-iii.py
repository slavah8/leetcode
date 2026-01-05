# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            
            if not node:
                return (0, 0)
            L_rob, L_skip = dfs(node.left)
            R_rob, R_skip = dfs(node.right)

            # if we rob this node

            rob = node.val + L_skip + R_skip
            skip = max(L_rob, L_skip) + max(R_rob, R_skip)
            return (rob, skip)

        r_rob, r_skip = dfs(root)
        return max(r_rob, r_skip)