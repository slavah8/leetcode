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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 26
        dsu = DSU(n)
        equals = []
        non_equals = []
        for e in equations:
            relationship = e[1:3]
            
            if relationship == '==':
                equals.append(e)
                
            elif relationship == '!=':
                non_equals.append(e)
                

        for e in equals:
            
            char1 = e[0]
            char2 = e[3]
            ch1 = ord(char1) - ord('a')
            ch2 = ord(char2) - ord('a')
            dsu.union(ch1, ch2)
            print(dsu.parent)
            print(dsu.rank)

        for e in non_equals:
            char1 = e[0]
            char2 = e[3]
            ch1 = ord(char1) - ord('a')
            ch2 = ord(char2) - ord('a')
            if dsu.find(ch1) == dsu.find(ch2):
                return False

        return True
        