class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        bit = 0
        exps = []
        x = n
        while x > 0:
            if x & 1:
                exps.append(bit)
            x = x >> 1
            bit += 1
        
        print(exps)

        prefix = [0] * (len(exps) + 1)

        for i, e in enumerate(exps):
            prefix[i + 1] = prefix[i] + e
        
        answer = []
        for L, R in queries:

            product = prefix[R + 1] - prefix[L]
            answer.append((2 ** product) % MOD)
        return answer
