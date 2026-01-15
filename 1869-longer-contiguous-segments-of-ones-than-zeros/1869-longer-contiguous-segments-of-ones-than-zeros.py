class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        zeros = 0
        ones = 0
        longest_one = 0
        longest_zero = 0
        for ch in s:
            if ch == '0':
                zeros += 1
                ones = 0
            else:
                ones += 1
                zeros = 0
            longest_one = max(longest_one, ones)
            longest_zero = max(longest_zero, zeros)
        
        if longest_one > longest_zero:
            return True
        else:
            return False