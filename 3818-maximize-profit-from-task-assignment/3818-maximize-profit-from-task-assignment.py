class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        
        profit_map = defaultdict(list) # skill : profits
        for i, (s, p) in enumerate(tasks):
            profit_map[s].append((-p, i))
        
        for s in profit_map:
            heapq.heapify(profit_map[s])


        total = 0
        seen = set() # tasks completed
        for w in workers:
            if w in profit_map:
                heap = profit_map[w]
                if not heap:
                    continue

                p, idx = heapq.heappop(heap)
                seen.add(idx)
                total += -p

        max_p = 0
        for i, (s, p) in enumerate(tasks):
            if i not in seen:
                max_p = max(max_p, p)

        return total + max_p
