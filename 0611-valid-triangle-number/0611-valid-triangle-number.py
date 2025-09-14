class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        print(nums)
        count = 0
        for k in range(N - 1, -1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # any num i ... j will also be valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1 # need to increase i
        return count

            