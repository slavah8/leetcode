class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        start = 0
        end = math.isqrt(c)

        while start <= end:
            summ = (start ** 2) + (end ** 2)

            if summ == c:
                return True
            elif summ < c:
                start += 1
            else:
                end -= 1
        return False