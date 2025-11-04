class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        perm = list(range(1, n + 1))
        i = 0
        while i < len(s):

            if s[i] == 'D':
                j = i
                while j + 1 < len(s) and s[j + 1] == 'D':
                    j += 1
                perm[i: j + 2] = reversed(perm[i: j + 2])
                i = j + 1
            else:
                i += 1
        return perm