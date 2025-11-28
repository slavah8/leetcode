class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        if self.n == 0:
            self.tree = []
            return
        
        self.tree = [[] for _ in range(self.n * 4)]

        def build(idx, l, r):
            if l == r:
                self.tree[idx] = [arr[l]]
                return
            
            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            left_list = self.tree[idx * 2]
            right_list = self.tree[idx * 2 + 1]
            merged = []
            i = j = 0
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    merged.append(left_list[i])
                    i += 1
                else:
                    merged.append(right_list[j])
                    j += 1
            if i < len(left_list):
                merged.extend(left_list[i:])
            if j < len(right_list):
                merged.extend(right_list[j:])
            self.tree[idx] = merged
        
        build(1, 0, self.n - 1)
        

    def query(self, left: int, right: int, value: int) -> int:
        if self.n == 0:
            return 0

        def _query(idx, l, r, ql, qr, val):

            # no overlap
            if ql > r or qr < l:
                return 0
            
            # full overlap
            if ql <= l and r <= qr:
                arr = self.tree[idx]
                lo = bisect_left(arr, val)
                hi = bisect_right(arr, val)
                return hi - lo
            
            # partial overlap
            mid = (l + r) // 2
            return _query(idx * 2, l, mid, ql, qr, val) + _query(idx * 2 + 1, mid + 1, r, ql, qr, val)
        
        return _query(1, 0, self.n - 1, left, right, value)
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)