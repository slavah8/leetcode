class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        ans = 0
        # i is the node
        def dfs(i):
            nonlocal ans
            if i > n:
                return 0
            if 2 * i > n: # leaf no children
                return cost[i - 1]
    
            left = dfs(2 * i)
            right = dfs(2 * i + 1)

            diff = abs(left - right)
            ans += diff

            return max(left, right) + cost[i - 1]


        dfs(1) # 1 is the root
        return ans