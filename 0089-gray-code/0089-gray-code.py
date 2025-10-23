class Solution:
    def grayCode(self, n: int) -> List[int]:
        target = 1 << n

        result = []
        seq = [0]
        seen = set()
        seen.add(0)

        def one_bit(a, b):
            x = a ^ b
            return x != 0 and (x & (x - 1)) == 0

        def backtrack():
            if len(seq) == target:
                return one_bit(seq[0], seq[-1])
            
            x = seq[-1]
            for b in range(n):
                y = x ^ (1 << b)
                if y not in seen:
                    seq.append(y)
                    seen.add(y)
                    if backtrack():
                        return True
                    seq.pop()
                    seen.remove(y)
            return False
        backtrack()
        return seq
                     
            

                    
                    
                     


