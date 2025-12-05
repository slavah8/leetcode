class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        L = len(s)
        D = sorted(digits)

        @lru_cache(None)
        def dfs(pos, tight, started):
            
            if pos == L:
                return 1 if started else 0


            res = 0
            limit_digit = s[pos]
            if not started:
                # option 1 dont start here "put leading zero"
                if tight:
                    next_tight = (limit_digit == '0')
                    res += dfs(pos + 1, next_tight, False)
                else:
                    res += dfs(pos + 1, False, False)
                
                # option 2 start here with some digit from D
                for d in D:
                    if tight and d > limit_digit:
                        break
                    
                    next_tight = tight and (d == limit_digit)
                    res += dfs(pos + 1, next_tight, True)
            
            else: # already started, must place a digit from D
                for d in D:
                    if tight and d > limit_digit:
                        break
                    next_tight = tight and (limit_digit == d)
                    res += dfs(pos + 1, next_tight, True)
            
            return res



        
        return dfs(0, True, False)