class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        heap = []

        for i, (p, t) in enumerate(classes):
            ratio = p / t
            new_ratio = (p + 1) / (t + 1)
            change = new_ratio - ratio
            heapq.heappush(heap, (-change, p, t))
        
        # heap holding the max change in pass ratio 
        
        while extraStudents > 0 and heap:
            change, p, t = heapq.heappop(heap)
            change = -change
            ratio = (p + 1) / (t + 1)
            new_ratio = (p + 2) / (t + 2)
            new_change = new_ratio - ratio
            heapq.heappush(heap, (-new_change, p + 1, t + 1))
            extraStudents -= 1
        
        summ = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            ratio = p / t
            summ += ratio
        
        return summ / n
        

