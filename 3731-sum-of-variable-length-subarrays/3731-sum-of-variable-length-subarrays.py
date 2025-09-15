class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        print(prefix_sum)
        ans = 0
        for i in range(N):
            start = max(0, i - nums[i])
            end = i
            ans += (prefix_sum[end + 1] - prefix_sum[start])
        return ans
