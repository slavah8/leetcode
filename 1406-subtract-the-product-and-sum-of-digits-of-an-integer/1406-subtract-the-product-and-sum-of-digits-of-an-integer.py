class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        while n > 0:
            digit = n % 10
            summ += digit
            product *= digit
            n = n // 10
        return product - summ
