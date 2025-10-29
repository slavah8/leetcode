class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.word_to_index = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_to_index[word].append(i)
        
        print(self.word_to_index)



    def shortest(self, word1: str, word2: str) -> int:
        INF = 10 ** 15
        idxs1 = self.word_to_index[word1]
        idxs2 = self.word_to_index[word2]
        idxs1.sort()
        idxs2.sort()
        best = INF
        i = 0 # index 1
        
        while i < len(idxs1):
            j = 0 # index 2
            while j < len(idxs2):
                cand = abs(idxs1[i] - idxs2[j])
                if cand < best:
                    best = cand
                j += 1  
            i += 1
        return best

        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)