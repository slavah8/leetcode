class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        INF = 10 ** 15
        best = INF
        if word1 == word2:
            first = -1
            second = -1
            
            for i, word in enumerate(wordsDict):
                if first == -1 and second == -1 and word == word1:
                    first = i
                elif first != -1 and second == -1 and word == word1:
                    second = i
                print(first)
                print(second)
                if first != -1 and second != -1:
                    best = min(best, abs(first - second))
                    first = second
                    second = -1
            return best
        else:        
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