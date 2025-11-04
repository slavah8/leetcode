class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heap = []

        for x in sticks:
            heapq.heappush(heap, x)
        
        min_cost = 0
        heapify(heap)
        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            cost = x + y
            heapq.heappush(heap, cost)
            min_cost += cost

        
        return min_cost
