class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        node_map = defaultdict(list) # node : nodes that are weaker
        indegree = [0] * n
        for u, v in edges:
            node_map[u].append(v)
            indegree[v] += 1
        
        print(node_map)
        print(indegree)
        champ = None
        for node in range(n):
            if indegree[node] == 0 and champ is not None:
                return -1
            if indegree[node] == 0:
                champ = node
        
        return champ
            