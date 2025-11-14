class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        p_to_d = sorted(zip(profit, difficulty), key = lambda x: (-x[0], x[1]))
        m = len(difficulty)

        i = 0
        n = len(worker)
        worker.sort(reverse = True)
        j = 0
        total = 0
        print(worker)
        print(p_to_d)
        while i < n:
            w = worker[i]
            print(w)
            # need to find greatest profit with appropriate difficulty
            while j < m and w < p_to_d[j][1]:
                j += 1
            if j < m:
                total += p_to_d[j][0]
            i += 1
            
        return total
            

