class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        result = []

        prefix = [0] * (N + 1)

        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        total = prefix[N]

        for i in range(N):
            left_size = i
            right_size = N - i - 1
            left = i * nums[i] - prefix[i]
            right = (total - prefix[i + 1]) - (right_size * nums[i])
            result.append(left + right)
        return result