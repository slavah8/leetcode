class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        prefix = [0] * (n + 1)

        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        print(prefix)
        total = prefix[n]

        for i in range(n):
            if (prefix[i + 1] - (total - prefix[i + 1])) % 2 == 0:
                count += 1
        
        if count == 0:
            return 0
        else:
            return count - 1