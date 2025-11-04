class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        heap = []
        for i, x in enumerate(nums):
            heapq.heappush(heap, (x, i))
        
        score = 0
        while len(visited) != len(nums):
            x, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            visited.add(idx)
            if idx - 1 >= 0:
                visited.add(idx - 1)
            
            if idx + 1 < n:
                visited.add(idx + 1)
            
            score += x
        return score
