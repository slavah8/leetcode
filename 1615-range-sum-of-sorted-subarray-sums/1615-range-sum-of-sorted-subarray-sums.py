class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7

        N = len(nums)
        subarray_sums = []
        for start in range(N):
            for end in range(start, N):
                subarray_sums.append(sum(nums[start:end + 1]))
        
        subarray_sums.sort()
        N = len(subarray_sums)
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + subarray_sums[i]

        return (prefix[right] - prefix[left - 1]) % MOD