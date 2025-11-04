class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = []

        for idx, x in enumerate(nums):
            heapq.heappush(heap, (x, idx))
        
        for _ in range(k):
            x, idx = heapq.heappop(heap)
            nums[idx] = x * multiplier
            heapq.heappush(heap, (x * multiplier, idx))
        
        return nums