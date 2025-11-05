class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        available = list(range(n))
        heapq.heapify(available) # tracks all rooms that are free
        busy = [] # (end_time, room)
        count = [0] * n

        meetings.sort(key = lambda x: x[0]) # sort by start time

        print(meetings)
        for s, e in meetings:
            d = e - s
            while busy and s >= busy[0][0]:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(busy, (s + d, room))
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + d, room))
                count[room] += 1

        best = max(range(n), key = lambda r: (count[r], -r))
        return best



