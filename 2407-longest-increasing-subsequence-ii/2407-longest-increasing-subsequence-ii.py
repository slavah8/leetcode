class SegTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size * 4)
    
    def _update(self, idx, l, r, pos, val):
        if l == r:
            if val > self.tree[idx]:
                self.tree[idx] = val
            return
        
        mid = (l + r) // 2
        if pos <= mid:
            self._update(idx * 2, l, mid, pos, val)
        else:
            self._update(idx * 2 + 1, mid + 1, r, pos, val)
        self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])
    
    def update(self, pos, val):
        self._update(1, 1, self.n, pos, val)
    
    def _query(self, idx, l, r, ql, qr):
        # no overlap
        if ql > r or qr < l:
            return 0
        # total overlap
        if l >= ql and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        left_max = self._query(idx * 2, l, mid, ql, qr)
        right_max = self._query(idx * 2 + 1, mid + 1, r, ql, qr)
        return max(left_max, right_max)
    
    def query(self, ql, qr):
        if ql > qr:
            return 0
        ql = max(1, ql)
        qr = min(self.n, qr)
        if ql > qr:
            return 0
        
        return self._query(1, 1, self.n, ql, qr)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:

        max_val = max(nums)
        seg = SegTree(max_val)

        ans = 0
        for x in nums:
            L = x - k
            R = x - 1
            best_prev = seg.query(L, R)
            dp_here = best_prev + 1
            seg.update(x, dp_here)
            if dp_here > ans:
                ans = dp_here
        return ans
        