class Solution:
    def countVowelStrings(self, n: int) -> int:
        # numerator : 
        # (n + 4)! ways to order these items n characters and 4 bars to separate the vowels

        # denominator : every partition has the same ordering so we need to subtract those ways from our answer
        #             ***** | ** | ***    same as ***** | ** | ***
        # swapping bars around gives the same arrangement so 4!
        # swapping characters around 

        return comb(n + 4, 4)