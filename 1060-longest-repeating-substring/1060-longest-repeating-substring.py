class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        
        N = len(s)
        a = [ord(c) - ord('a') for c in s]
        B = 1315423911
        M = 1_000_000_007

        powB = [1] * (N + 1)
        for i in range(1, N + 1):
            powB[i] = (powB[i - 1] * B) % M
        
        P = [0] * (N + 1)
        for i, v in enumerate(a):
            P[i + 1] = (P[i] * B + v) % M
        
        def sub_hash(l, r):
            return (P[r] - P[l] * powB[r - l]) % M
        
        # does a repeated substring of L exist
        def exists(L):
            if L == 0:
                return True
            seen = set()
            for i in range(N - L + 1):
                h = sub_hash(i, i + L)
                if h in seen:
                    return True
                seen.add(h)
            
            return False
        
        low = 0
        high = len(s) - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if exists(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
            
        return ans