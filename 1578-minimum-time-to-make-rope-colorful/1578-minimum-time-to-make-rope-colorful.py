class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(neededTime)

        run_sum = neededTime[0]
        run_max = neededTime[0]
        ans = 0
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                run_sum += neededTime[i]
                run_max = max(run_max, neededTime[i])
            else:
                ans += (run_sum - run_max)
                run_sum = neededTime[i]
                run_max = neededTime[i]
        
        ans += run_sum - run_max
        
        return ans


            

