# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        def dfs(node, cur_depth):
            nonlocal depth, val

            if cur_depth == depth - 1:
                left = node.left
                right = node.right
                new1 = TreeNode(val)
                new2 = TreeNode(val)
                node.left = new1
                node.right = new2
                new1.left = left
                new2.right = right
                return 
            else:
                if node.left:
                    dfs(node.left, cur_depth + 1)
                if node.right:
                    dfs(node.right, cur_depth + 1)
        dfs(root, 1)
        return root