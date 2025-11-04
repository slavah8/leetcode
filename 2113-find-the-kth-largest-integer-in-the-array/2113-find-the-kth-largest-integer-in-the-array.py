class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for s in nums:
            key = (-len(s), tuple(-ord(c) for c in s))
            heapq.heappush(heap, (key, s))
        
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return heap[0][1]
        
