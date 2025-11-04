class Solution:
    def halveArray(self, nums: List[int]) -> int:
        S = sum(nums)
        target = S / 2

        ops = 0
        heap = []
        for idx, x in enumerate(nums):
            heapq.heappush(heap, (-x, idx))
        reduced = 0.0
        while reduced < target:
            x, idx = heapq.heappop(heap)
            x = -x
            y = x / 2
            reduced += y
            heapq.heappush(heap, (-y, idx))
            ops += 1
        
        return ops
