# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 10
        best = 0
        def traverse(node):
            nonlocal best
            if not node:
                return (True, 0, INF, -INF)
            # need to check if left is valid bst and right is valid bst
            # if both are valid then we can check if the root node passes
            L_is, left_count, l_minn, l_maxx = traverse(node.left)
            R_is, right_count, r_minn, r_maxx = traverse(node.right)
            total_count = left_count + right_count + 1
            
            if L_is and R_is and node.val > l_maxx and node.val < r_minn:
                best = max(best, 1 + left_count + right_count)
                mn = min(l_minn, node.val)
                mx = max(r_maxx, node.val)
                return (True, total_count, mn, mx)
            else:
                return (False, 0, -INF, INF)
            
        
        traverse(root)
        return best
