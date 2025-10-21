class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        for num in range(a, b + 1):
            false = False
            count_digits = collections.Counter()
            while num:
                digit = num % 10
                count_digits[digit] += 1
                if count_digits[digit] > 1:
                    false = True
                    break
                num = num // 10
            if not false:
                count += 1
        return count
            
            
                

