# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)]) # (node, index)
        ans = 0
        while queue:
            level_len = len(queue)
            _, first_idx = queue[0]

            for _ in range(level_len):
                node, idx = queue.popleft()
                norm = idx - first_idx
                if node.left:
                    queue.append((node.left, 2 * norm + 1))
                if node.right:
                    queue.append((node.right, 2 * norm + 2))
                last_norm = norm
            ans = max(ans, last_norm + 1)
        
        return ans

            
