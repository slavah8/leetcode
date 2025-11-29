class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        S = 0
        step = 0

        while S < target or ((S - target) % 2 != 0):
            step += 1
            S += step
        return step

            

        