class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32 # count of set bits in current window
        def add_bit(x):
            b = 0
            while x:
                if x & 1:
                    cnt[b] += 1
                x = x >> 1 # remove the bit we just inspected
                b += 1 # inspect next bit
        
        def remove_bit(x):
            b = 0
            while x:
                if x & 1:
                    cnt[b] -= 1
                x = x >> 1
                b += 1

                

        def window_or():
            val = 0
            for b in range(32):
                if cnt[b] > 0:
                    val |= (1 << b)
            return val

        ans = n + 1
        l = 0
        cur_or = 0

        for r, x in enumerate(nums):
            add_bit(x)
            cur_or = window_or()
            while l <= r and cur_or >= k:
                ans = min(ans, r - l + 1)
                left_x = nums[l]
                remove_bit(left_x)
                l += 1
                cur_or = window_or()
        return ans if ans != n + 1 else -1
            

                
