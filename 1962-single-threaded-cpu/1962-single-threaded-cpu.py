class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        arr = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        arr.sort() # sort by enqueue time

        res = []
        heap = [] # (processingTime, index)
        t = 0
        i = 0

        while i < n or heap:
            # if no available tasks jump time to next arrival
            if not heap and i < n and t < arr[i][0]:
                t = arr[i][0]
            
            while i < n and arr[i][0] <= t:
                et, pt, idx = arr[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            
            if heap:
                pt, idx = heapq.heappop(heap)
                t += pt
                res.append(idx)
        return res