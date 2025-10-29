class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        counts = collections.Counter(s)
        print(counts)
        # need all even and 1 odd

        odd = 0
        for cnt in counts.values():
            if cnt % 2 == 1:
                odd += 1
        
        if odd == 1 or odd == 0:
            return True
        else:
            return False