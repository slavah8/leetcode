class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        

        words = []
        n = len(word)
        curr = []
        def backtrack(i):
            nonlocal curr

            if i == n:
                words.append(''.join(curr[:]))
                return

            # abbrev
            if curr and curr[-1].isdigit(): # cant abbreviate
                curr.append(word[i])
                backtrack(i + 1)
                curr.pop()
            else:
                for abbrev in range(1, n - i + 1):
                    curr.append(str(abbrev))
                    backtrack(i + abbrev)
                    curr.pop()

                curr.append(word[i])
                backtrack(i + 1)
                curr.pop()
                
            
        backtrack(0)
        
        return words