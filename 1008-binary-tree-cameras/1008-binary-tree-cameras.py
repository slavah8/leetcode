# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        HAS_CAM, COVERED, NEEDS_CAM = 0, 1, 2
        self.cams = 0

        def dfs(node):
            if not node:
                return COVERED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == NEEDS_CAM or right == NEEDS_CAM:
                self.cams += 1
                return HAS_CAM
            
            if left == HAS_CAM or right == HAS_CAM:
                return COVERED
            
            if left == COVERED and right == COVERED:
                return NEEDS_CAM
        
        if dfs(root) == 2:
            self.cams += 1
        return self.cams
            
            