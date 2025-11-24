class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

        target = (1 << n) 
        print(target)
        seq = [start]
        seen = {start}
        res = []
        def one_bit(a, b):
            x = a ^ b
            return x != 0 and (x & (x - 1)) == 0

        def backtrack():

            if len(seq) == target:
                return one_bit(seq[0], seq[-1])
                    

            x = seq[-1]  
            for b in range(n):
                y = x ^ (1 << b)
                if y in seen:
                    continue
                
                seq.append(y)
                seen.add(y)
                if backtrack():
                    return True
                seq.pop()
                seen.remove(y)
            return False
        backtrack()
        
        return seq





