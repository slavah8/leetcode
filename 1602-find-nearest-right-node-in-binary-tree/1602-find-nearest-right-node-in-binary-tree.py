# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        queue = deque([root])
        rightmost = None
        
        while queue:

            level_size = len(queue)
            found = False
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if found and rightmost is None:
                    rightmost = node

                if node == u:
                    found = True
            
        
        return rightmost


