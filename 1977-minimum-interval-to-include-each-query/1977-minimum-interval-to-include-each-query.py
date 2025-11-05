class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        qs = sorted([(q, i) for i, q in enumerate(queries)]) # (q, idx)

        ans = [-1] * len(queries)
        heap = [] # (size, right)
        j = 0

        for q, qi in qs:

            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heapq.heappush(heap, (r - l + 1, r))
                j += 1
            
            # discard any intervals that q has passed
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # top interval is the smallest
            if heap:
                ans[qi] = heap[0][0]
        return ans
            



            


