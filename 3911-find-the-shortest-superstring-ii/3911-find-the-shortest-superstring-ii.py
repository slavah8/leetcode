class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        
        if s1 in s2:
            return s2
        if s2 in s1:
            return s1
        
        # max overlap
        def overlap(a, b):
            maxk = min(len(a), len(b))
            for k in range(maxk, 0, -1):
                if a.endswith(b[:k]):
                    return k
            return 0

        k12 = overlap(s1, s2)
        k21 = overlap(s2, s1)

        cand12 = s1 + s2[k12:]
        cand21 = s2 + s1[k21:]

        if len(cand12) <= len(cand21):
            return cand12
        else:
            return cand21