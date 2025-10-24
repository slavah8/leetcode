class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        slots = [-1, -1, -1, -1]  # H1 H2 M1 M2
        used = [False] * 4

        best = -1
        best_str = ''

        def ok(pos, d):
            if pos == 0: # H1 : 0 ... 2
                return d <= 2
            if pos == 1: # H2 : 0 ... 9 or H2 = 0 or if H2 = 2 then 0 .. 4
                if slots[0] == 2:
                    return d <= 3
                else:
                    return d <= 9
            if pos == 2: # M1 : 0 ... 5
                return d <= 5
            return True
            
        
        def backtrack(pos):
            nonlocal best, best_str
            if pos == 4:
                h = slots[0] * 10 + slots[1]
                m = slots[2] * 10 + slots[3]
                total = h * 60 + m
                if total > best:
                    best = total
                    best_str = f'{h:02d}:{m:02d}'
                return
            
            for i in range(4):
                if not used[i] and ok(pos, arr[i]):
                    used[i] = True
                    slots[pos] = arr[i]
                    backtrack(pos + 1)
                    used[i] = False
                    slots[pos] = -1

        backtrack(0)
        return best_str
                    
                    


                

        