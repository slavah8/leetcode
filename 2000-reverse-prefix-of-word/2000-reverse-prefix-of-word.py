class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        def reverse(word1, i, j):
            i = 0
            j = len(word1) - 1
            
            while i < j:
                word1[i], word1[j] = word1[j], word1[i]
                i += 1
                j -= 1
            return ''.join(word1)

        if ch not in word:
            return word
        
        idx = None
        for i, char in enumerate(word):
            if char == ch:
                rev = reverse(list(word[:i + 1]), 0, i)
                print(rev)
                idx = i
                break
        
        return rev + word[idx + 1:]
