class Solution:
    def countHousePlacements(self, N: int) -> int:
        MOD = 10 ** 9 + 7

        end0 = [0] * (N + 1) # number of ways for first i plots, ith is empty
        end1 = [0] * (N + 1) # number of ways for first i plots, ith has a house

        # base case i = 1
        end0[1] = 1
        end1[1] = 1

        for i in range(2, N + 1):
            end0[i] = (end0[i - 1] + end1[i - 1]) % MOD # if i is empty i - 1 can be anything
            end1[i] = end0[i - 1] % MOD # if i has house then i - 1 has to be empty
        
        return ((end0[N] + end1[N]) ** 2) % MOD


