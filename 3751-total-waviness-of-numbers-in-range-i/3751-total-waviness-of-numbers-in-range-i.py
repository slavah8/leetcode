class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            if num < 100:
                continue

            x = str(num)
            n = len(x)
            for i in range(1, n - 1):
                new_x = int(x[i])

                if int(x[i - 1]) < new_x and new_x > int(x[i + 1]):
                    waviness += 1
                
                if new_x < int(x[i - 1]) and new_x < int(x[i + 1]):
                    waviness += 1
            
        return waviness