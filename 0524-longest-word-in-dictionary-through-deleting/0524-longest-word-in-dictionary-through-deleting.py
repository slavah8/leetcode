class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        

        # can i form word with s
        def can_form(s, word): 
            N = len(s)
            M = len(word)
            i = 0 # index in s
            j = 0 # index in word
            while i < N and j < M:
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            if j == M:
                return True

            if i == N and j != M:
                return False
            
        
        longest = 0
        best = ''
        for word in dictionary:
            if can_form(s, word):
                print(word)
                curr = word
                if len(curr) == longest:
                    if curr < best:
                        best = curr
                elif len(curr) > longest:
                    best = curr
                    longest = len(curr)
        return best


            



            
