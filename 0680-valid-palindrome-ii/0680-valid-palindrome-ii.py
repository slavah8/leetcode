class Solution:
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        l = 0
        r = N - 1
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                remove_left = is_pal(l + 1, r)
                remove_right = is_pal(l, r - 1)
                if remove_left or remove_right:
                    return True
                else:
                    return False
        return True
