class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        parity_arr = []

        for x in nums:
            if x % 2 == 0:
                parity_arr.append(0)
            else:
                parity_arr.append(1)
        print(parity_arr)

        prefix = 0
        ans = 0
        freq = collections.Counter({0 : 1})

        for x in parity_arr:
            prefix += x
            ans += freq[prefix - k]
            freq[prefix] += 1

        return ans