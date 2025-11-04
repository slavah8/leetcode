class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        max_heap = []
        for idx, x in enumerate(gifts):
            heapq.heappush(max_heap, (-x, idx))
        

        seconds = 0

        while max_heap and seconds < k:
            pile, idx = heapq.heappop(max_heap)
            pile = -pile
            new = floor(math.sqrt(pile))
            gifts[idx] = new
            heapq.heappush(max_heap, (-new, idx))
            seconds += 1
        return sum(gifts)