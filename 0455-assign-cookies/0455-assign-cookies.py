class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        N = len(g)
        M = len(s)

        i = 0 # greed index
        j = 0 # size index
        content = 0
        while i < N and j < M:
            if g[i] <= s[j]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1
        return content


