class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        
        N = len(s)
        bold = [False] * N

        for i in range(N):
            end = i
            for w in words:
                if s.startswith(w, i):
                    end = max(end, i + len(w))
            for j in range(i, end):
                bold[j] = True
        
        res = []
        i = 0
        while i < N:
            if not bold[i]:
                res.append(s[i])
                i += 1
            else:
                res.append('<b>')
                j = i
                while j < N and bold[j]:
                    res.append(s[j])
                    j += 1
                res.append('</b>')
                i = j
        return ''.join(res)

