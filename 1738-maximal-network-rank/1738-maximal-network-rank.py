class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        outdegree = [0] * n
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            outdegree[v] += 1
            outdegree[u] += 1
        
        print(outdegree)
        best = 0
        def count(node1, node2):
            cnt1 = outdegree[node1]
            cnt2 = outdegree[node2]
            total = cnt1 + cnt2
            if node1 in graph[node2] or node2 in graph[node1]:
                total -= 1
            return total 

        for node1 in range(n):
            for node2 in range(n):
                if node1 == node2:
                    continue
                best = max(best, count(node1, node2))
        
        return best
                


