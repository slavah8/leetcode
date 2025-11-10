# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def lca(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            
            L = lca(node.left, p, q)
            R = lca(node.right, p, q)
            if L and R:
                return node
            return L or R
        
        LCA = lca(root, p, q)

        # need dist from lca to p and dist from lca to q
        INF = 10 ** 10
        def path_to(node, target, dist):
            if not node:
                return INF
            
            if node.val == target:
                return dist
            
            L = path_to(node.left, target, dist + 1)
            R = path_to(node.right, target, dist + 1)
            return min(L, R)
            
            
        
        pathP = []
        pathQ = []
        dist1 = path_to(LCA, p, 0)
        dist2 = path_to(LCA, q, 0)
        print(dist1)
        print(dist2)
        return dist1 + dist2