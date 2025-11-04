class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for idx, x in enumerate(nums):
            heapq.heappush(heap, x)
        ops = 0
        while len(heap) >= 2 and heap[0] < k:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            val = min(x, y) * 2 + max(x, y)
            heapq.heappush(heap, val)
            ops += 1
        return ops
        
