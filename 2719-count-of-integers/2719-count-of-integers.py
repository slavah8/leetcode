MOD = 10 ** 9 + 7
def count_up_to(S, min_sum, max_sum):
        # dfs(pos, sum, tight) = number of ways to fill positions pos..L-1
        # such that : resulting number ≤ S (respecting tight), and
        # final total digit sum ∈ [min_sum, max_sum].
        L = len(S)

        @lru_cache(None)
        def dfs(pos, cur_sum, tight):

            if cur_sum > max_sum:
                return 0
            
            if pos == L:
                return 1 if (min_sum <= cur_sum <= max_sum) else 0
            
            limit = int(S[pos]) if tight else 9
            res = 0

            for d in range(0, limit + 1):
                if cur_sum + d > max_sum:
                    break

                next_tight = tight & (d == limit)
                res = (res + dfs(pos + 1, d + cur_sum, next_tight)) % MOD
            
            return res

        return dfs(0, 0, True)

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
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
        num1 = minus_one(num1)
        count1 = count_up_to(num1, min_sum, max_sum)
        count2 = count_up_to(num2, min_sum, max_sum)
        return (count2 - count1) % MOD
        

