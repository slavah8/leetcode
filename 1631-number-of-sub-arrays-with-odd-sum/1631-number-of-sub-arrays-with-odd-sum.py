class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        seen = defaultdict(int)
        seen[0] = 1

        parity = 0
        ans = 0

        for x in arr:
            parity ^= (x & 1) # if 1 then odd
            ans += seen[1 - parity]
            seen[parity & 1] += 1
            # If the current prefix is odd, you can pair it with all previous even prefixes → add even to ans
            # If the current prefix is even, you can pair it with all previous odd prefixes → add odd to ans.

        return ans % MOD