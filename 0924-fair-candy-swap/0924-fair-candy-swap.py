class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        

        """
        SA + b - a == SB + a - b
        -2a + 2b == SB - SA
        -2(a - b) == SB - SA
        (a - b) == -(SB - SA) / 2 
        b = (SB - SA) / 2 + a
        """

        SA = sum(aliceSizes)
        SB = sum(bobSizes)
        delta = (SB - SA) / 2
        bob = sorted(bobSizes)

        for a in aliceSizes:
            need = delta + a
            i = bisect.bisect_left(bob, need)
            if i < len(bob) and bob[i] == need:
                return [a, need]
                