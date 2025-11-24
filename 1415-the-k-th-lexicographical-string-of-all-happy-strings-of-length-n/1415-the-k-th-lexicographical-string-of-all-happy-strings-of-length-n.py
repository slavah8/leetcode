class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

        happy_strings = []
        curr = []
        def backtrack():
            if len(curr) == n:
                happy_strings.append(''.join(curr[:]))
                return
            
            for char in ('a', 'b', 'c'):
                if curr and curr[-1] == char:
                    continue
                
                curr.append(char)
                backtrack()
                curr.pop()
        
        backtrack()
        print(happy_strings)
        if k > len(happy_strings):
            return ""
        return happy_strings[k - 1]