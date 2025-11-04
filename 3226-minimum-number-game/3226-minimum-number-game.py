class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        arr = []

        heapify(nums)
        heap = nums

        while heap:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            arr.append(y)
            arr.append(x)
        return arr