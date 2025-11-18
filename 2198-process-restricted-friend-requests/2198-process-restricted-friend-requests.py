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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        dsu = DSU(n)
        ans = []
        for u, v in requests:
            
            ru = dsu.find(u)
            rv = dsu.find(v)
            can_merge = True
            if ru == rv:
                ans.append(True)
                continue
            
            for x, y in restrictions:
                rx = dsu.find(x)
                ry = dsu.find(y)

                # if u or v are same group as a restricted group and we try to merge it would violate
                if (ru == rx and rv == ry) or (ru == ry and rv == rx):
                    can_merge = False
                    break

            if can_merge:
                dsu.union(u, v)
                ans.append(True)
            else:
                ans.append(False)

            
        
        return ans
            

