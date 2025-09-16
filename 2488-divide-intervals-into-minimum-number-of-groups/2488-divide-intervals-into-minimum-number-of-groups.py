class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        heap = []

        intervals.sort(key = lambda x: x[0])
        print(intervals)

        heapq.heappush(heap, intervals[0][1])
        for interval in intervals[1:]:
            start, end = interval
            if heap[0] < start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)