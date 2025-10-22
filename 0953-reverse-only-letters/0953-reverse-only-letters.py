class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        N = len(s)
        l = 0
        r = N - 1
        s = list(s)
        while l < r:
            if not s[l].isalpha() and s[r].isalpha():
                l += 1
            elif not s[l].isalpha() and not s[r].isalpha():
                l += 1
                r -= 1
            elif s[l].isalpha() and not s[r].isalpha():
                r -= 1
            else: # valid
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)


