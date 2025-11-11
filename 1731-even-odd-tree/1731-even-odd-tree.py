# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        l = 0
        while queue:
            level_len = len(queue)
            nodes = []
            for _ in range(level_len):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(nodes)
            print(sorted(nodes))
            if l % 2 == 1: # odd - increasing order
                i = 0
                while i < len(nodes):
                    if nodes[i] % 2 == 1 or (i + 1 < len(nodes) and nodes[i] <= nodes[i + 1]):
                        return False
                    i += 1
            else: # even - decreasing order
                i = 0
                while i < len(nodes):
                    if (i + 1 < len(nodes) and nodes[i] >= nodes[i + 1]) or nodes[i] % 2 == 0:
                        return False
                    i += 1   
            l += 1
        return True







        