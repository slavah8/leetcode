class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        length = [1] * N # len[i] = length of the LIS ending at i
        count = [1] * N # cnt[i] = number of LIS ending at i with length len[i]



        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        max_length = max(length)
        return sum(c for l, c in zip(length, count) if l == max_length)