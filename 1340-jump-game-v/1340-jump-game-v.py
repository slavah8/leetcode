class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        n = len(arr)
        memo = [-1] * n
        # dp(i) = maximum number of indices you can visit if you start at index i
        @lru_cache(None)
        def dfs(i):

            if memo[i] != -1:
                return memo[i]

            best = 1

            # look left
            for step in range(1, d + 1):
                j = i - step
                if j < 0:
                    break
                
                if arr[j] >= arr[i]:
                    break
                
                best = max(best, 1 + dfs(j))
            

            # look right
            for step in range(1, d + 1):
                j = i + step
                if j >= n:
                    break
                
                if arr[j] >= arr[i]:
                    break
                
                best = max(best, 1 + dfs(j))
            
            memo[i] = best
            return best
        
        return max(dfs(i) for i in range(n))




