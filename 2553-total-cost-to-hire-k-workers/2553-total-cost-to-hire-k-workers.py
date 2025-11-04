class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap1, heap2 = [], []

        # ----- Build two fronts WITHOUT overlap -----
        left_end = min(candidates, n)
        right_start = max(candidates, n - candidates)   # start index for right side
        for i in range(left_end):
            heapq.heappush(heap1, (costs[i], i))        # left heap: (cost, idx)
        for j in range(right_start, n):
            heapq.heappush(heap2, (costs[j], j))        # right heap: (cost, idx)

        # Next indices to pull from each side
        l = left_end            # next left index not yet in heap1
        r = right_start - 1     # next right index not yet in heap2

        total = 0
        
        INF = 10 ** 10
        while k > 0 and (heap1 or heap2):
            # Peek both sides; pick the min by (cost, index) as required by the problem
            left_top  = heap1[0] if heap1 else (float('inf'), float('inf'))
            right_top = heap2[0] if heap2 else (float('inf'), float('inf'))

            if right_top < left_top:
                cost, idx = heapq.heappop(heap2)
                total += cost
                k -= 1
                # Refill from the right if available (avoid overlap: only if l <= r)
                if l <= r:
                    heapq.heappush(heap2, (costs[r], r))
                    r -= 1
            else:
                cost, idx = heapq.heappop(heap1)
                total += cost
                k -= 1
                # Refill from the left if available (avoid overlap)
                if l <= r:
                    heapq.heappush(heap1, (costs[l], l))
                    l += 1

        return total

