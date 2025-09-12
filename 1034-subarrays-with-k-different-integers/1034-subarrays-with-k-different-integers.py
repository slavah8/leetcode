class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(nums, k):
            freq = defaultdict(int)
            left = 0
            distinct = 0
            ans = 0

            for right, x in enumerate(nums):
                if freq[x] == 0:
                    distinct += 1
                freq[x] += 1

                while distinct > k: # shrink window
                    left_num = nums[left]
                    freq[left_num] -= 1
                    if freq[left_num] == 0:
                        distinct -= 1
                    left += 1
                ans += right - left + 1
            return ans

        return at_most(nums, k) - at_most(nums, k - 1)