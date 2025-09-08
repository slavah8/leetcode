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
            roota, rootb = rootb, roota

        self.parent[rootb] = roota
        self.size[roota] += self.size[rootb]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        n = len(nums)
        dsu = DSU(n)
        M = max(nums)
        spf = list(range(M + 1))

        for i in range(2, int(M ** 0.5) + 1):
            if spf[i] == i: # prime
                for j in range(i * i, M + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_primes(x):
            primes = set()
            while x > 1:
                p = spf[x]
                primes.add(p)
                while x % p == 0:
                    x = x // p
            return primes
        
        first = {} # {prime : index}
        for i, val in enumerate(nums):
            for p in get_primes(val):
                if p in first:
                    dsu.union(first[p], i)
                else:
                    first[p] = i
        
        count = collections.defaultdict(int)
        ans = 1
        for i in range(n):
            root = dsu.find(i)
            count[root] += 1
            ans = max(count[root], ans)
        
        return ans
        
