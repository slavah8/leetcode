class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        print(mask)

        #nums[0] ^ nums[1] ^ nums[2] ^ nums[3]
        #nums[0] ^ nums[1]
        total = 0 # entire arrays bitmask
        for x in nums:
            total ^= x
        
        N = len(nums)
        ans = [0] * N
        for i in range(N):
            ans[i] = mask ^ total
            total = total ^ nums[N - i - 1]
        return ans




