class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        
        N = len(s)
        # prev2 most recent
        # prev1 second most recent
        def dfs(index, pieces, prev1, prev2):
            if index == N:
                return pieces >= 3
            num = 0
            for j in range(index, N):
                if j > index and s[index] == '0':
                    break # cant extend when we start with 0

                num = num * 10 + (ord(s[j]) - ord('0'))
                
                # if prev2 exists then prev1 exists
                if prev2 is None:
                    if dfs(j + 1, pieces + 1, None, num):
                        return True
                elif prev2 is not None and prev1 is None:
                    if dfs(j + 1, pieces + 1, prev2, num):
                        return True
                else:
                    if prev1 + prev2 == num:
                        if dfs(j + 1, pieces + 1, prev2, num):
                            return True
            return False

        

        return dfs(0, 0, None, None)
            
            
