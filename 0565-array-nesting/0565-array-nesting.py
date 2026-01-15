class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        n = len(nums)

        visited = [False] * n

        def dfs(i):
            if visited[i]:
                return 0
            
            visited[i] = True
            return dfs(nums[i]) + 1
        best = 0
        for k in range(n):
            if not visited[k]:
                best = max(best, dfs(k))
        
        return best