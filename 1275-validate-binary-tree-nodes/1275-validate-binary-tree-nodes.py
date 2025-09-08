class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

        return True

class Solution:
    def validateBinaryTreeNodes(self, N: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # use union find to verify that there is one connected component, no cycles, and each node has exactly one parent

        dsu = DSU(N)
        parent_of = [-1] * N
        
        # check that each node has exactly 1 parent
        for node in range(N):
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if parent_of[child] != -1:
                        return False
                    parent_of[child] = node

        

        # check if theres only 1 node with no parent (1 root)
        roots = [i for i in range(N) if parent_of[i] == -1]
        if len(roots) != 1:
            return False
        
        # detect any cycles
        # parent_of[i] - u -> v (u is the value parent_of[i] and v is the i)
        for node in range(N):
            parent = parent_of[node]
            if parent != -1:
                if not dsu.union(parent, node):
                    return False # cycle
        
        # check for only 1 connected component
        components = set(dsu.find(i) for i in range(N))

        if len(components) != 1:
            return False
        
        return True




        