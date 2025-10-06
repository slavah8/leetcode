class Solution:
    def longestDupSubstring(self, s: str) -> str:
        B = 911382323
        a = [ord(c) - ord('a') for c in s]
        N = len(s)
        M1 = 1_000_000_007
        M2 = 1_000_000_009
        pow1 = [1] * (N + 1)
        pow2 = [1] * (N + 1)

        for i in range(1, N + 1):
            pow1[i] = (pow1[i - 1] * B) % M1
            pow2[i] = (pow2[i - 1] * B) % M2
        
        p1 = [0] * (N + 1)
        p2 = [0] * (N + 1)
        for i, v in enumerate(a):
            p1[i + 1] = (p1[i] * B + v + 1) % M1
            p2[i + 1] = (p2[i] * B + v + 1) % M2
        
        def sub_hash(l, r):
            h1 = (p1[r] - (p1[l] * pow1[r - l]) % M1) % M1
            h2 = (p2[r] - (p2[l] * pow2[r - l]) % M2) % M2
            return h1, h2
        
        # Does there exist any substring of length L that appears at least twice in s
        def check(L):
            
            seen = {}
            for i in range(N - L + 1):
                h = sub_hash(i, i + L)

                if h not in seen:
                    seen[h] = i
                
            for j in range(N - L + 1):
                h = sub_hash(j, j + L)
                if h in seen:
                    i = seen[h]
                    if s[i:i + L] == s[j:j + L] and i != j:
                        return s[i:i + L]
            
            return None
        
        low = 1
        high = N - 1
        best = ""
        while low <= high:
            mid = (low + high) // 2
            dup = check(mid)
            if dup is not None: # found a dup
                best = dup
                low = mid + 1
            else:
                high = mid - 1
        return best



        
