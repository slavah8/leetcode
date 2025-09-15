class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total = sum(nums)
        remain = total % p # needed remainder to make divisible
        print(remain)
        if remain == 0:
            return 0
        
        pos = {0: -1}     # Map pos[rem] = latest index where prefix % p == rem
        N = len(nums)
        ans = N
        # we need to find a subarray that sums up to the need (remainder to make divisible)
        # if we find it then it is a possible answer
        curr_sum = 0
        for j, x in enumerate(nums):
            curr_sum = (curr_sum + x) % p
            prefix = (curr_sum - remain) % p
            if prefix in pos:
                ans = min(ans, j - pos[prefix])
            pos[curr_sum] = j
        return -1 if ans == N else ans 

            

        
