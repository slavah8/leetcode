# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        def lca(node, p, q):
            
            if not node or node.val == p or node.val == q:
                return node
            L = lca(node.left, p, q)
            R = lca(node.right, p, q)
            if L and R:
                return node
            return L or R
        
        LCA = lca(root, startValue, destValue)
        # path will travel upwards from s to LCA and then downwards to t

        def path_to(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            
            # try left
            path.append('L')
            if path_to(node.left, target, path):
                return True
            path.pop()

            # try right
            path.append('R')
            if path_to(node.right, target, path):
                return True
            path.pop()
            return False

        
        path_to_start = []
        path_to_dest = []
        path_to(LCA, startValue, path_to_start)
        path_to(LCA, destValue, path_to_dest)
        print(path_to_start)
        print(path_to_dest)
        return 'U' * len(path_to_start) + ''.join(path_to_dest)
