class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        print(prefix)

        count = 0
        for x in prefix:
            if x > 0:
                count += 1
        return count