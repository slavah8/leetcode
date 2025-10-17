class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odds = []
        evens = []

        for x in nums:
            if x % 2 == 0:
                evens.append(x)
            else:
                odds.append(x)
        
        i = 0 # index in odds array
        j = 0 # index in evens array
        N = len(odds)
        M = len(evens)
        result = []
        parity = 0
        while i < N or j < M:
            if parity == 0: # even
                result.append(evens[j])
                j += 1
                parity = 1
            else:
                result.append(odds[i])
                i += 1
                parity = 0
        return result

