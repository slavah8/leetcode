class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        def reverse_front(k, new_string):
            # reverse first k characters
            l = 0
            r = k

            while l < r:
                new_string[l], new_string[r] = new_string[r], new_string[l]

                l += 1
                r -= 1
            
            return ''.join(new_string)
        
        def reverse_back(k, new_string):
            l = k
            r = n - 1

            while l < r:
                new_string[l], new_string[r] = new_string[r], new_string[l]

                l += 1
                r -= 1
            
            return ''.join(new_string)
        

        best = None
        for k in range(0, n):
            new_s = list(s)
            new_front = reverse_front(k, new_s)
            if best is None or new_front < best:
                best = new_front
            
            new_s = list(s)
            new_back = reverse_back(k, new_s)
            if new_back < best:
                best = new_back
        
        return best




