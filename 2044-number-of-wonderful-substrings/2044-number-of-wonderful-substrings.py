class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        freq = defaultdict(int) # mask : number of times this mask has been seen
        freq[0] = 1
        mask = 0 # 10 bit mask 
        base = ord('a')
        ans = 0

        for char in word:
            mask ^= 1 << (ord(char) - base)

            # off by 1 (1 odd)
            for b in range(10):
                ans += freq[mask ^ (1 << b)]

            ans += freq[mask]
            freq[mask] += 1
        return ans




