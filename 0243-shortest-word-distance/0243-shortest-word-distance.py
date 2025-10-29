class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        INF = 10 ** 15
        best = INF
        idx1 = -1 # index of word1
        idx2 = -1 # index of word2
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            elif word == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                best = min(best, abs(idx1 - idx2))
        return best

            
