class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        

        result = []
        N = len(code)
        for i in range(N):
            if k == 0:
                result.append(0)
            elif k > 0:
                summ = 0
                for j in range(k):
                    summ += code[(i + j + 1) % N]
                result.append(summ)
            else:
                summ = 0
                for j in range(-k):
                    summ += code[i - j - 1 % N]
                result.append(summ)
        return result