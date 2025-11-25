class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        INF = 10 ** 10
        best_cost = None
        best_diff = INF
        m = len(toppingCosts)
        def dfs(i, curr_cost):
            nonlocal best_cost, best_diff
            diff = abs(target - curr_cost)
            if diff < best_diff or (diff == best_diff and curr_cost < best_cost):
                best_cost = curr_cost
                best_diff = diff
            
            if i == m:
                return
            
            if curr_cost >= target and curr_cost - target > best_diff:
                return
            
            
            dfs(i + 1, curr_cost + 2 * toppingCosts[i])

            dfs(i + 1, curr_cost)

            dfs(i + 1, curr_cost + toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)
        return best_cost
