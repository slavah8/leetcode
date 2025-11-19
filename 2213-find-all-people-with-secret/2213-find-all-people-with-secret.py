class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        meetings.sort(key = lambda x: x[2])

        i = 0
        m = len(meetings)
        dsu = DSU(n)
        dsu.union(0, firstPerson)

        while i < m:
            t = meetings[i][2]
            # collect all meetings with same time
            same_time = []
            people = set()
            while i < m and t == meetings[i][2]:
                x, y, _ = meetings[i]
                same_time.append((x, y))
                people.add(x)
                people.add(y)
                i += 1

            # build dsu with people with same meeting time
            for x, y in same_time:
                dsu.union(x, y)
            
            root_0 = dsu.find(0)
            can_keep = set()
            for p in people:
                if dsu.find(p) == root_0:
                    can_keep.add(p)
            
            for p in people:
                if p not in can_keep:
                    dsu.parent[p] = p
                    dsu.rank[p] = 1

        root0 = dsu.find(0)
        return [i for i in range(n) if dsu.find(i) == root0]

