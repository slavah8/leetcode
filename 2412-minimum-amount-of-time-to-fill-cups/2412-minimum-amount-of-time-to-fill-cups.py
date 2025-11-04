class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        # cold , warm , hot

        cold = amount[0]
        warm = amount[1]
        hot = amount[2]
        max_heap = []
        if amount[0] != 0:
            heapq.heappush(max_heap, (-amount[0], 0)) # cold
        if amount[1] != 0:
            heapq.heappush(max_heap, (-amount[1], 1)) # warm
        if amount[2] != 0:
            heapq.heappush(max_heap, (-amount[2], 2)) # hot

        seconds = 0
        # always fill up 2 cups with most unfilled cups
        
        print(max_heap) # (cups, type)
        while len(max_heap) >= 2:
            cups, typee = heapq.heappop(max_heap)
            cups = -cups
            cups -= 1
            
            cups2, typee2 = heapq.heappop(max_heap)
            cups2 = -cups2
            cups2 -= 1

            if cups > 0:
                heapq.heappush(max_heap, (-cups, typee))
            if cups2 > 0:
                heapq.heappush(max_heap, (-cups2, typee2))
            seconds += 1

        while max_heap:
            cups, _ = heapq.heappop(max_heap)
            cups = -cups
            seconds += cups
        return seconds 

            