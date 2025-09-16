class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[0])
        heap = []

        heapq.heappush(heap, intervals[0][1])

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if heap[0] <= start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)


