class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota == rootb:
            return
        
        if self.size[roota] < self.size[rootb]:
            roota,rootb = rootb, roota
        
        self.parent[rootb] = roota
        self.size[roota] += self.size[rootb]

class Solution:
    def countPairs(self, N: int, edges: List[List[int]]) -> int:

        dsu = DSU(N)
        comp_size = collections.defaultdict(int)

        for u, v in edges:
            dsu.union(u, v)
        
        for i in range(N):
            root = dsu.find(i)
            comp_size[root] += 1
            
        answer = 0
        total_nodes = N

        for rt, nodes in comp_size.items():
            outside_nodes = total_nodes - nodes
            answer += outside_nodes * nodes
            
        return answer // 2




        