class Solution:
    def findIntegers(self, n: int) -> int:
        

        # 3 not valid
        # 6 not valid
        # 7 not valid 
        # 11 not valid
        # 12 not valid 
        # 13 not valid
        # 14 not valid

        # any square of 2 is valid
        # any 
        # 3 valid 1 not 2 valid 2 not 3 valid 4 not
        # F[i] number of valid binary strings of length i with no consecutive 1s

        F = [0] * 32
        F[0] = 1 # empty 
        F[1] = 2 # either 0 or 1

        for i in range(2, 32):
            # strings of length i either start with 0 and then any valid length i-1 string → F[i-1]
            # or start with 10 and then any valid length i-2 string → F[i-2]
            F[i] = F[i - 1] + F[i - 2]

        ans = 0
        prev_one = 0
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                ans += F[i]
                if prev_one == 1:
                    return ans
                prev_one = 1
            else:
                prev_one = 0
        return ans + 1