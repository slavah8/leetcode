class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
    
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
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        words = set()
        for a, b in similarPairs:
            words.add(a)
            words.add(b)
        words.update(sentence1)
        words.update(sentence2)
        idx_of = {} # string to index so dsu works
        for index, word in enumerate(words):
            idx_of[word] = index
        print(idx_of)

        dsu = DSU(len(words))
        for a, b in similarPairs:
            dsu.union(idx_of[a], idx_of[b])
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if dsu.find(idx_of[w1]) != dsu.find(idx_of[w2]):
                return False
        return True

        