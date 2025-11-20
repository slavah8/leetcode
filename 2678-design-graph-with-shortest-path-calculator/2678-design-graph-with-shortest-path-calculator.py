class Graph:

    

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def dijkstra(self, start, end):
        INF = 10 ** 10
        dist = [INF] * self.n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
                
            if u == end:
                return d
            for v, w in self.graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (d + w, v))
        return -1

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))
        
        

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)