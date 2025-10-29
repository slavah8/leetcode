class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        diff = [0] * 52

        for L, R in ranges:
            diff[L] += 1
            diff[R + 1] -= 1
        

        prefix = [0] * 53
        for i, x in enumerate(diff):
            prefix[i + 1] = prefix[i] + x
        
        print(prefix)
        for i in range(left, right + 1):
            if prefix[i + 1] < 1:
                return False
        return True