class Solution:
    def expand(self, s: str) -> List[str]:
        
        n = len(s)
        groups = []
        i = 0
        
            
                    
        while i < n:
            if s[i] == '{':
                options = []
                i += 1 # skip the }
                while i < n and s[i] != '}':
                    if s[i] == ',':
                        i += 1
                    options.append(s[i])
                    i += 1
                i += 1
                options.sort()
                groups.append(options)
            else:
                groups.append([s[i]])
                i += 1
        print(groups)

        words = []
        curr = []
        def backtrack(index):
            if index == len(groups):
                words.append(''.join(curr[:]))
                return
            
            for char in groups[index]:
                curr.append(char)
                backtrack(index + 1)
                curr.pop()


        backtrack(0)
        print(words)
        return words
        
                
                



        