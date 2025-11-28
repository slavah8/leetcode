class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(1, 0, self.n - 1)
    
    def build(self, idx, l, r):
        if l == r:
            self.tree[idx] = self.nums[l]
            return 
        mid = (l + r) // 2
        self.build(idx * 2, l, mid)
        self.build(idx * 2 + 1, mid + 1, r)
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]
    
    def _update(self, idx, l, r, pos, val):
        if l == r:
            self.tree[idx] = self.nums[l]
            return
        mid = (l + r) // 2
        if pos <= mid:
            self._update(idx * 2, l, mid, pos, val)
        else:
            self._update(idx * 2 + 1, mid + 1, r, pos, val)
        
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def _query(self, idx, l, r, ql, qr):
        if ql > r or qr < l: # no overlap
            return 0
        if ql <= l and qr >= r: # total overlap
            return self.tree[idx]
        # partial overlap
        mid = (l + r) // 2
        return (self._query(idx * 2, l, mid, ql, qr) + self._query(idx * 2 + 1, mid + 1, r, ql, qr))

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self._update(1, 0, self.n - 1, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)