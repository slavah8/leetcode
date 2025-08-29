# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_root_val = preorder[1] # marks end of left subtree in post order
        k = postorder.index(left_root_val)
        len_left = k + 1

        root.left = self.constructFromPrePost(preorder[1:len_left + 1], postorder[:len_left])
        root.right = self.constructFromPrePost(preorder[len_left + 1:], postorder[len_left:-1])
        return root

        """
        root = 1
        root.left = [2,4,5,3,6,7] [4,5,2,6,7,3]
        root = 2 [4,5,3,6,7] [4,5,2,6,7]
        root = 4 [5,3,6,7] [4,5,2,6,7]

        """