class Solution:
    def countDistinct(self, s: str) -> int:
        
        set_sub = set()
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                set_sub.add(substring)

        return len(set_sub)