# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        
        sums = []
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(level_sum)
        
        queue = deque([(root, -1)]) # (node, parent)

        l = 0
        while queue:
            level_size = len(queue)
            parent_sum = defaultdict(int)
            level = []
            for _ in range(level_size):
                node, parent = queue.popleft()
                level.append((node, parent))
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
                parent_sum[parent] += node.val
            for node, parent in level:
                if len(parent_sum) == 1:
                    node.val = 0
                else:
                    node.val = sums[l] - parent_sum[parent]
            l += 1
        return root
            
                
