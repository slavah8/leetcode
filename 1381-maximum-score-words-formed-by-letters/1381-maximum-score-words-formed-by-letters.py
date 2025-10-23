class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - ord('a')] += 1
        
        N = len(words)
        freqs = []
        scores = []

        for w in words:
            s = 0
            f = [0] * 26
            for ch in w:
                idx = ord(ch) - ord('a')
                f[idx] += 1
                s += score[idx]
            freqs.append(f)
            scores.append(s)
        
        def can_take(i):
            f = freqs[i]
            for c in range(26):
                if f[c] > avail[c]:
                    return False
            return True
        
        def take_word(i):
            f = freqs[i]
            for c in range(26):
                avail[c] -= f[c]
        
        def untake_word(i):
            f = freqs[i]
            for c in range(26):
                avail[c] += f[c]

        best = 0
        def dfs(i, cur_score):
            nonlocal best
            if i == N:
                if cur_score > best:
                    best = cur_score
                return
            
            # skip word i
            dfs(i + 1, cur_score)
            
            # take word i
            if can_take(i):
                take_word(i)
                dfs(i + 1, cur_score + scores[i])
                untake_word(i)

        dfs(0, 0)
        return best



