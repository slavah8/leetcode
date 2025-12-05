class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        MOD = 10 ** 9 + 7
        inventory.sort()
        n = len(inventory)
        max_inv = inventory[-1]

        # Helper: how many balls can we sell with value > k?
        def balls_above(k):
            total = 0
            for c in inventory:
                if c > k:
                    total += c - k
            return total

        lo, hi = 0 , max_inv

        while lo < hi:
            mid = (lo + hi) // 2
            if balls_above(mid) >= orders:
                lo = mid + 1
            else:
                hi = mid
        
        k = lo  # We choose a k such that we sell every ball whose value > k

        # compute profit for selling all balls with value > k
        profit = 0
        total_full = 0

        for c in inventory:
            if c > k:
                count = c - k
                total_full += count
                first = k + 1
                last = c
                profit += (first + last) * count // 2
                profit %= MOD
        
        # now we still might not have enough sold as orders so we need to sell balls with value = k
        remaining = orders - total_full

        if remaining > 0:
            profit += remaining * k
            profit %= MOD
        
        return profit % MOD




            