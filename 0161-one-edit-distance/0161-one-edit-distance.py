class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # make s the smaller string
        if len(s) > len(t):
            s, t = t, s
        N = len(s)
        M = len(t)

        if abs(M - N) > 1:
            return False
        
        i = 0 # index in s
        j = 0 # index in t
        used_edit = False
        while i < N and j < M:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if used_edit:
                    return False
                used_edit = True
                if N == M:
                    # replace so just move 
                    
                    i += 1
                    j += 1
                else:
                    # insert so just move the longer one
                    j += 1
        
        if not used_edit:
            return N + 1 == M
        
        return True

        
