# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        
        targets = set(nodes)
        def lca(node, nodes):
            if not node:
                return None
            
            if node in targets:
                return node
    
            L = lca(node.left, nodes) 
            R = lca(node.right, nodes) 

            if L and R:
                return node
            if not L and R:
                return R
            if L and not R:
                return L
        
        return lca(root, nodes)

            
