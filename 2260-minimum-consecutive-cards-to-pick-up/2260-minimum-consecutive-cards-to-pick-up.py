class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        n = len(cards)

        l = 0
        last_index = defaultdict(int)
        INF = 10 ** 10
        best = INF

        for r in range(n):
            x = cards[r]

            if x in last_index:
                cand = r - last_index[x] + 1
                if cand < best:
                    best = cand
            
            last_index[x] = r
        
        return best if best != INF else -1
            
