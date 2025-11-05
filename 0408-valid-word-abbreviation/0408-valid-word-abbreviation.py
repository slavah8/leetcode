class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        n = len(word)
        m = len(abbr)
        i = 0 # word pointer
        j = 0 # abbr pointer

        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False

                k = j
                while k < m and abbr[k].isdigit():
                    k += 1
                num = int(abbr[j:k])
                j = k
                i += num
                if i > n:
                    return False
                continue
            else:
                return False
        if i == n and j < m:
            return False
        if i < n and j == m:
            return False
        if i > n:
            return False
        
        return True
            
        

        
