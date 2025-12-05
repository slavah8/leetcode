MOD = 10 ** 9 + 7
def count_up_to(S):
    
        L = len(S)
        @lru_cache(None)
        def dfs(pos, last, tight, started):

            if L == pos:
                return 1 if started else 0

            limit = int(S[pos]) if tight else 9

            res = 0
            if not started:
                # option 1 keep skipping 
                res += dfs(pos + 1, 0, tight & (limit == 0), False)
                res %= MOD

                # option 2 start the number here
                for d in range(1, limit + 1):
                    next_tight = tight & (limit == d)
                    res += dfs(pos + 1, d, next_tight, True)
                    res %= MOD
            else:
                for d in range(0, limit + 1):
                    step = abs(last - d)
                    if step != 1:
                        continue
                    next_tight = tight & (limit == d)
                    res += dfs(pos + 1, d, next_tight, True)
                    res %= MOD
            
            return res

        return dfs(0, 0, True, False)

def minus_one(num):
    num_list = list(num)
    i = len(num_list) - 1
    while i >= 0 and num_list[i] == '0':
        num_list[i] = '9'
        i -= 1

    if i >= 0:
        num_list[i] = str(int(num_list[i]) - 1)
    res = ''.join(num_list).lstrip('0')

    return res if res != '' else '0'

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        num1 = minus_one(low)
        count1 = count_up_to(num1)
        count2 = count_up_to(high)

        return (count2 - count1) % MOD
        
        
