class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        LDS = [1] * N # length of longest decreasing sequence starting at i

        for i in range(N - 1, -1, -1):
            for k in range(i + 1, N):
                if nums[k] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[k] + 1)

        best = 0
        for i in range(1, N - 1):
            if LIS[i] > 1 and LDS[i] > 1:
                best = max(best, LIS[i] + LDS[i] - 1)
        return N - best
                
