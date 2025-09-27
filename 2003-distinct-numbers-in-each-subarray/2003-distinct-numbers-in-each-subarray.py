class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        result = []
        counts = Counter()
        left = 0
        for right, x in enumerate(nums):
            counts[x] += 1
            while right - left + 1 > k:
                left_num = nums[left]
                counts[left_num] -= 1
                if counts[left_num] == 0:
                    del counts[left_num]
                left += 1
            if right - left + 1 == k:
                result.append(len(counts))
        
        return result
