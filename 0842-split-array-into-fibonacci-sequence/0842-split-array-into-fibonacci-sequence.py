class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        UPPER = 2 ** 31
        n = len(num)
        ans = []
        
        def backtrack(i, curr):
            nonlocal ans

            if i == n:
                ok = True
                if len(curr) >= 3:
                    for idx in range(len(curr) - 2):
                        if int(curr[idx]) + int(curr[idx + 1]) != int(curr[idx + 2]):
                            ok = False
                            break
                    
                    if ok:
                        ans.append(curr[:])
                        return True
                return False

            
            for j in range(i, n + 1): # choose split point
                x = num[i:j + 1]
                if int(x) > UPPER:
                    return False
                if len(x) > 1 and x[0] == '0':
                    continue
                
                if len(curr) <= 2:
                    curr.append(x)
                    if backtrack(j + 1, curr):
                        return True
                    curr.pop()
                else:
                    summ = int(curr[-2]) + int(curr[-1]) 
                    if summ == int(x):
                        curr.append(x)
                        if backtrack(j + 1, curr):
                            return True
                        curr.pop()



        backtrack(0, [])
        if ans:
            res = list(map(int, ans[0]))
            return res
        else:
            return []