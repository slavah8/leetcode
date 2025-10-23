class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse(word):
            l = 0
            r = len(word) - 1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            return ''.join(word)
        
        word_list = s.split()
        print(word_list)

        result = ''
        for word in word_list:
            word = list(word)
            r_word = reverse(word)
            result += r_word
            result += ' '
        return result[:-1]