class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        nums = []
        def is_prime(x):
            if x <= 1:
                return False
            
            if x <= 3:
                return True
            
            if x % 2 == 0 or x % 3 == 0:
                return False
            
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6

            return True 
            

        def traverse(r0, c0):
            nonlocal nums
            
            initial = mat[r0][c0]
            num = initial

            # east
            for c in range(c0 + 1, cols):
                num = num * 10 + mat[r0][c]
                nums.append(num)
            
            # south
            num = initial
            for r in range(r0 + 1, rows):
                num = num * 10 + mat[r][c0]
                nums.append(num)
            
            num = initial
            # south-east
            nc = c0 + 1
            nr = r0 + 1
            while nc < cols and nr < rows:
                num = num * 10 + mat[nr][nc]
                nums.append(num)
                nr += 1
                nc += 1
            
            # south-east
            num = initial
            nc = c0 - 1
            nr = r0 + 1
            while nr < rows and nc >= 0:
                num = num * 10 + mat[nr][nc]
                nums.append(num)
                nr += 1
                nc -= 1
            
            # north
            num = initial
            for r in range(r0 - 1, -1, -1):
                num = num * 10 + mat[r][c0]
                nums.append(num)
            
            # north-west
            num = initial
            nr = r0 - 1
            nc = c0 - 1
            while nr >= 0 and nc >= 0:
                num = num * 10 + mat[nr][nc]
                nums.append(num)
                nr -= 1
                nc -= 1
            
            # north-east
            num = initial
            nr = r0 - 1
            nc = c0 + 1
            while nr >= 0 and nc < cols:
                num = num * 10 + mat[nr][nc]
                nums.append(num)
                nr -= 1
                nc += 1
            
            # west
            num = initial
            for c in range(c0 - 1, -1, -1):
                num = num * 10 + mat[r0][c]
                nums.append(num)
            

        for r in range(rows):
            for c in range(cols):
                traverse(r, c)
        
        freq = defaultdict(int)
        for x in nums:
            if x > 10:
                if is_prime(x):
                    freq[x] += 1
        
        if not freq:
            return -1
        
        best = max(freq.items(), key = lambda x: (x[1], x[0]))[0]
        return best
        

