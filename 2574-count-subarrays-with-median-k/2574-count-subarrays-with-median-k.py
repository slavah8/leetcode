class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        

        m = nums.index(k)
        n = len(nums)
        balance = 0
        freq = defaultdict(int)
        freq[0] = 1 # how many left prefixes have a given balance
        for i in range(m - 1, -1, -1): # counting frequencies for left side of median
            if nums[i] < k:
                balance -= 1
            else:
                balance += 1
            freq[balance] += 1

        ans = 0
        balance = 0
        for i in range(m, n): # counting frequencies for right side of median
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

            # left_balance + right_balance == 0   → left_balance = -right_balance
            # left_balance + right_balance == 1   → left_balance = 1 - right_balance
            ans += freq[-balance] + freq[1 - balance]

        return ans

            
