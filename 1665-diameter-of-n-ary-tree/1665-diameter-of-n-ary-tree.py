"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        graph = defaultdict(list)

        def build(node):
            for child in node.children:
                graph[node].append(child)
                graph[child].append(node)
                build(child)
        build(root)

        # returns dist_map and farthest node
        def bfs(start):
            dist_map = {start : 0} # node : dist
            queue = deque([start])
            far = start
            while queue:
                node = queue.popleft()
                far = node
                for child in graph[node]:
                    if child not in dist_map:
                        dist_map[child] = dist_map[node] + 1
                        queue.append(child)
            return dist_map, far
        
        # find farthest node from root (u)
        _, u = bfs(root)
        print(u.val)
        # find  farthest node from u
        dist_u, v = bfs(u)
        return dist_u[v]
        
