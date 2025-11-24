# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)

        def build(node, parent):
            
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)

            build(node.left, node)
            build(node.right, node)


        
        build(root, None)
        print(graph)
        
        queue = deque()
        queue.append((target, 0))
        ans = []
        visited = set()
        while queue:
            node, d = queue.popleft()
            visited.add(node)
            if d == k:
                ans.append(node.val)
            
            
            for nei in graph[node]:
                if nei not in visited:
                    queue.append((nei, d + 1))

        return ans
