class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        # binary seach on the max number of minutes u can run all n computers
        
        def feasible(T):
            usable = 0
            for x in batteries:
                usable += min(x, T)
            return usable >= n * T
            
        total_energy = sum(batteries)

        low = 0
        high = total_energy // n

        while low < high:
            mid = (low + high + 1) // 2
            if feasible(mid):
                low = mid
            else:
                high = mid - 1

        return low
            

                
