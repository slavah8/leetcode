class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []

        remaining = finalSum
        curr = 2
        result = []
        while curr <= remaining:
            result.append(curr)
            remaining -= curr
            curr += 2
        
        print(result)
        if remaining > 0:
            result[-1] += remaining
        
        return result
        

