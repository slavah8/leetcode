class Solution:
    def maxSubstringLength(self, s: str) -> int:
        
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]

        for i, ch in enumerate(s):
            c = ord(ch) - 97
            prefix[i + 1] = prefix[i].copy()
            prefix[i + 1][c] += 1

        total = prefix[n]

        next_pos = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - 97
            next_pos[i] = next_pos[i + 1].copy()
            next_pos[i][c] = i
        
        def shrink(start, end):
            while end >= start:
                bad_char = -1
                for c in range(26):
                    cnt_in = prefix[end + 1][c] - prefix[start][c]
                    if cnt_in == 0:
                        continue
                    if cnt_in < total[c]:
                        bad_char = c
                        break
                if bad_char == -1:
                    return end
                # remove this bad char from the substring 
                pos = next_pos[start][bad_char] # first occurence of this char in this substring
                
                end = pos - 1
            return end
                    

        ans = -1
        for start in range(0, n):
            end = n - 1
            best_end = shrink(start, end)
            if start == 0 and best_end == n - 1:
                best_end = shrink(start, n - 2)
            if best_end >= start:
                length = best_end - start + 1
                if length < n:
                    ans = max(ans, length)
        return ans
            
            