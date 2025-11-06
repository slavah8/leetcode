# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        arr1 = []
        arr2 = []

        def inorder(node, arr):
            if not node:
                return

            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        inorder(root1, arr1)
        inorder(root2, arr2)
        print(arr1)
        print(arr2)
        n = len(arr1)
        m = len(arr2)
        for i in range(n):
            for j in range(m):
                if arr1[i] + arr2[j] == target:
                    return True
        return False