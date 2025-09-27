class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        result = []
        N = len(nums)
        OFFSET = 50
        freq = [0] * 101
        left = 0
        def find_xth_negative():
            cnt = 0
            for idx in range(0, 50):
                cnt += freq[idx]
                if cnt >= x:
                    return idx - OFFSET
            return 0

        for right in range(N):
            freq[nums[right] + OFFSET] += 1
            while right - left + 1 > k:
                num_left = nums[left]
                freq[OFFSET + num_left] -= 1
                left += 1

            if right - left + 1 == k:
                result.append(find_xth_negative())
        return result
                