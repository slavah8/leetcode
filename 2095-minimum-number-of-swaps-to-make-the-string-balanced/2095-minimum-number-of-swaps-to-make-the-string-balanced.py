class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        left = 0
        right = N - 1
        openn = 0
        closed = 0
        swaps = 0
        s_list = list(s)
        while left < N:
            if s_list[left] == '[':
                openn += 1
            else:
                closed += 1
            if closed > openn: # need to swap
                swaps += 1
                while s_list[right] != '[':
                    right -= 1
                s_list[right] = ']'
                s_list[left] = '['
                right -= 1
                closed -= 1
                openn += 1
            
            left += 1
        return swaps
            


