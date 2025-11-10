# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 10
        queue = deque([root])
        best_level = 1
        minn = INF
        l = 1
        while queue:
            level_len = len(queue)
            level_sum = 0
            for _ in range(level_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum < minn:
                minn = level_sum
                best_level = l
            l += 1
        return best_level
            
