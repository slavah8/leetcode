class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        score = 0

        heap = []

        heapq.heappush(heap, -a)
        heapq.heappush(heap, -b)
        heapq.heappush(heap, -c)

        avail = 3

        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            x = -x
            y = -y
            x -= 1
            y -= 1

            if x > 0:
                heapq.heappush(heap, -x)
            if y > 0:
                heapq.heappush(heap, -y)
            
            score += 1
        return score
            