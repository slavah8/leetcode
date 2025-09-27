class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        diff = [0] * (N + 1)

        parity = 0
        effective = 0
        flips = 0
        for i in range(N):
            parity ^= diff[i]
            effective = nums[i] ^ parity
            if effective == 0: # need to flip greedily
                if i + k > N:
                    return -1 
                flips += 1
                parity ^= 1
                diff[i + k] ^= 1
        return flips