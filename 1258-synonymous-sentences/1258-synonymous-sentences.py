class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return root_a
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a

        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return root_a

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        word_id = {}
        next_id = 0
        for u, v in synonyms:
            if u not in word_id:
                word_id[u] = next_id
                next_id += 1
            if v not in word_id:
                word_id[v] = next_id
                next_id += 1
        print(word_id)
        dsu = DSU(next_id)

        for a, b in synonyms:
            dsu.union(word_id[a], word_id[b])
        
        print(dsu.parent)

        root_to_words = defaultdict(list)

        for w, idx in word_id.items():
            root = dsu.find(idx)
            root_to_words[root].append(w)
        
        words = text.split()
        options = []  # options[i] = list of possible words at position i


        for w in words:
            if w in word_id:
                root = dsu.find(word_id[w])
                opts = root_to_words[root]
                options.append(opts)
            else: # no synonyms
                options.append([w])

        # options[i] = list of possible words at position i

        print(options)
        res, curr = [], []
        def backtrack(i):
            
            if i == len(words):
                res.append(" ".join(curr))
                return
            
            for word in options[i]:
                curr.append(word)
                backtrack(i + 1)
                curr.pop()

        
        backtrack(0)
        res.sort()
        return res