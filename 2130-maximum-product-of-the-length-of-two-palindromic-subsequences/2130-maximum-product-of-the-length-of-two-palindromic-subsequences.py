class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        m = 1 << N
        pal_len = [0] * m # # pal_len[mask] = length if mask is palindromic subseq else 0

        def is_pal(mask):
            i, j = 0, N - 1
            while i < j:
                while i < j and (mask >> i) & 1 == 0:
                    i += 1
                while i < j and (mask >> j) & 1 == 0:
                    j -= 1
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for mask in range(1, m):
            if is_pal(mask):
                pal_len[mask] = bin(mask).count('1')
        
        ans = 0
        full = m - 1
        for A in range(1, m):
            if pal_len[A] == 0:
                continue
            rem = full ^ A
            sub = rem
            while sub:
                if pal_len[sub] != 0:
                    prod = pal_len[A] * pal_len[sub]
                    if prod > ans:
                        ans = prod
                sub = (sub - 1) & rem
        return ans
