# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        sums = []
        heapify(sums)

        queue = deque([root])
        l = 0
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
            heapq.heappush(sums, -level_sum)
            l += 1
        if l < k:
            return -1
        for _ in range(k - 1):
            x = heapq.heappop(sums)
        
        return -sums[0]

