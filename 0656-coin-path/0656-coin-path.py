class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        
        # dp[i] min cost to reach the ith index
        INF = 10 ** 15
        coins = [0] + coins
        N = len(coins) - 1

        dp = [INF] * (N + 1)
        paths = [None] * (N + 1)

        dp[1] = coins[1]
        paths[1] = [1]

        for i in range(2, N + 1):
            if coins[i] == -1:
                continue
            best_cost = INF
            best_path = None
            for j in range(1, maxJump + 1):
                prev = i - j
                if prev < 1:
                    break
                if dp[prev] == INF or paths[prev] is None:
                    continue
                
                cand_cost = dp[prev] + coins[i]
                cand_path = paths[prev] + [i]
                if cand_cost < best_cost or (cand_cost == best_cost and (best_path == None or cand_path < best_path)):
                    best_path = cand_path
                    best_cost = cand_cost
            dp[i] = best_cost
            paths[i] = best_path
        
        return paths[N] if dp[N] < INF and paths[N] is not None else []