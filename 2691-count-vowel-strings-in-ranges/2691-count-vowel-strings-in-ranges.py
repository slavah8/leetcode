class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        

        vowels = {'a', 'e', 'i', 'o', 'u'}

        N = len(words)
        good = [0] * N

        for i, w in enumerate(words):
            if w and (w[0] in vowels and w[-1] in vowels):
                good[i] = 1
        
        prefix = [0] * (N + 1)

        for i in range(N):
            prefix[i + 1] = prefix[i] + good[i]

        
        answer = []
        for L, R in queries:
            total = prefix[R + 1] - prefix[L]
            answer.append(total)
        return answer

