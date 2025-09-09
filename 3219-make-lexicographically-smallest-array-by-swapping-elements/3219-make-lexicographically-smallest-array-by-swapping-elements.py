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
        roota, rootb = self.find(a), self.find(b)
        if roota == rootb:
            return
        
        if self.rank[roota] < self.rank[rootb]:
            roota, rootb, = rootb, roota

        self.parent[rootb] = roota

        if self.rank[roota] == self.rank[rootb]:
            self.rank[roota] += 1
        
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        dsu = DSU(N)

        arr = [(nums[i], i) for i in range(N)]
        arr.sort()

        for j in range(1, N):
            prev_val, prev_idx = arr[j - 1]
            cur_val, cur_idx = arr[j]

            if cur_val - prev_val <= limit:
                dsu.union(prev_idx, cur_idx)
        
        groups = collections.defaultdict(list) # root : indices
        for i in range(N):
            root = dsu.find(i)
            groups[root].append(i)
        
        print(groups)
        res = nums[:]

        for idxs in groups.values():
            idxs.sort()
            vals = sorted(nums[i] for i in idxs)
            for i, v in zip(idxs, vals):
                res[i] = v
        return res


        