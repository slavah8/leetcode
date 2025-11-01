class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        total = 0
        for word1, cnt1 in c1.items():
            for word2, cnt2 in c2.items():
                if word1 == word2 and cnt1 == 1 and cnt2 == 1:
                    total += 1
        return total