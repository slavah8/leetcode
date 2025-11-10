# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # check nodes existence
        p_found = False
        q_found = False
        def dfs(node, p, q):
            nonlocal p_found, q_found
            if not node:
                return 
            
            if node.val == p.val:
                p_found = True

            if node.val == q.val:
                q_found = True
            
            dfs(node.left, p, q)
            dfs(node.right, p, q)

        dfs(root, p, q)
        print(p_found)
        print(q_found)
        if not p_found or not q_found:
            return None
        
        def lca(node, p, q):
            if not node or node.val == p.val or node.val == q.val:
                return node
            
            L = lca(node.left, p, q)
            R = lca(node.right, p, q)
            if L and R:
                return node
            return L or R
        
        LCA = lca(root, p, q)
        return LCA

        
