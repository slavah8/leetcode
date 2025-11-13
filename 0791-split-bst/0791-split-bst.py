# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if not node:
                return [None, None]

            if node.val <= target: # case 1 : all values to the left of node are definitely in the small subtree
            # but some nodes in the right might be > target and some might be < target
                small_right, big_right = dfs(node.right)
                node.right = small_right
                return [node, big_right]
            else: # node.val > target
                # case 2 : all values to the right of node are definitely in the big subtree
                # but some nodes in the left could be bigger and could be smaller
                small_left, big_left = dfs(node.left)
                node.left = big_left
                return [small_left, node]
        return dfs(root)