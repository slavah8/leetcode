class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        
        left = 0
        N = len(s)
        totals = Counter(s)
        if any(totals[c] < k for c in 'abc'):
            return -1
            
        # taken[c] >= k
        # total[c] - middle[c] >= k
        # middle[c] <= total[c] - k
        cap = [totals['a'] - k, totals['b'] - k, totals['c'] - k]
        print(cap)

        def idx(char):
            return ord(char) - ord('a')
        
        cnt = [0, 0, 0]
        left = 0
        longest = 0
        for right in range(N):
            char = s[right]
            cnt[idx(char)] += 1
            while cnt[0] > cap[0] or cnt[1] > cap[1] or cnt[2] > cap[2]:
                left_char = s[left]
                cnt[idx(left_char)] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return N - longest
            

        


