# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        inorder = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

        dfs(root)
        n = len(inorder)
        for i, x in enumerate(inorder):
            
            if x == p:
                idx = i + 1
                if idx >= n:
                    return None
                else:
                    res = inorder[idx]
                    return res 
