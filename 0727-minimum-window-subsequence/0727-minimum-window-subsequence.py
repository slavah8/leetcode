class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        N = len(s1)
        M = len(s2)
        INF = 10 ** 10
        best_len = INF
        best_start = 0
        i = j = 0

        while i < N:
            if s1[i] == s2[j]:
                j += 1
            if j == M: # found substring now try to shrink
                end = i
                k = i
                j = M - 1
                while j >= 0:
                    if s1[k] == s2[j]:
                        j -= 1
                    k -= 1
                start = k + 1
                curr_len = end - start + 1
                if curr_len < best_len:
                    best_start = start
                    best_len = curr_len
                i = start + 1
                continue
            i += 1
        return "" if best_len == INF else s1[best_start:best_start + best_len]