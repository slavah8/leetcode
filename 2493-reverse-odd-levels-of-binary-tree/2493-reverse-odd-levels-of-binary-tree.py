# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        queue = deque([root])
        level = 0
        prev = [root]
        while queue:
            level_len = len(queue)
            curr_level = []
            for _ in range(level_len):
                node = queue.popleft()
                curr_level.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1: # reverse
                l = 0
                r = len(curr_level) - 1
                
                while l < r:
                    curr_level[l].val, curr_level[r].val = curr_level[r].val, curr_level[l].val
                    l += 1
                    r -= 1

                
                
            level += 1 
            prev = curr_level

        return root



    