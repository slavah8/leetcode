class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        word_list = text.split()
        
        print(word_list)
        count = 0
        for word in word_list:
            for char in word:
                if char in brokenLetters:
                    count += 1
                    break
        return len(word_list) - count