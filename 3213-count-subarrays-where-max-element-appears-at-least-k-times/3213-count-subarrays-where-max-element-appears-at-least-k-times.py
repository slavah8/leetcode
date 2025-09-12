class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        maxx = max(nums)
        left = 0
        N = len(nums)
        count = 0
        ans = 0
        for right in range(N):
            num = nums[right]
            if num == maxx:
                count += 1
            while count >= k:
                ans += (N - right)
                num_left = nums[left]
                if num_left == maxx:
                    count -= 1
                left += 1
        return ans

            

