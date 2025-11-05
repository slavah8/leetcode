class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arr = [(s, e, i) for i, (s, e) in enumerate(times)]
        arr.sort(key = lambda x: x[0]) # sort by arrival time

        print(arr)
        heap = [] # (leave_time, chair)
        available = list(range(n)) # chairs avaialble
        heapify(available)
        for arrival, leave, idx in arr:

            while heap and arrival >= heap[0][0]:
                leave_time, chair = heapq.heappop(heap)
                heapq.heappush(available, chair)
            
            if available:
                chair = heapq.heappop(available)
                heapq.heappush(heap, (leave, chair))
            
            if idx == targetFriend:
                return chair



