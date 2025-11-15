class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        print(indegree)
        ans = []
        for node in range(n):
            if indegree[node] == 0:
                ans.append(node)
        return ans
        
        
            



        


        
