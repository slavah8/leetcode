class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        s, t = source, target
        src_set = set(s)

        for char in t:
            if char not in src_set:
                return -1
            
        
        
        i = 0 # pointer in target
        N = len(target)
        passes = 0

        while i < N:
            moved = False
            for char in s:
                if i < N and char == t[i]:
                    moved = True
                    i += 1
            if not moved:
                return False
            passes += 1
        return passes
