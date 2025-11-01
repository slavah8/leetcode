class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        #

        @lru_cache(None)
        def dfs(rem):
            # Baseline: buy all remaining items individually
            base = sum(price[i] * rem[i] for i in range(n))
            best = base
            # try all specials
            for sp in special:
                items, cost = sp[:n], sp[-1]

                # check fit (no overbuy)
                ok = True
                new_rem = []
                for i in range(n):
                    if items[i] > rem[i]:
                        ok = False
                        break
                    new_rem.append(rem[i] - items[i])
                if ok:
                    best = min(best, cost + dfs(tuple(new_rem)))
            return best
        
        return dfs(tuple(needs))