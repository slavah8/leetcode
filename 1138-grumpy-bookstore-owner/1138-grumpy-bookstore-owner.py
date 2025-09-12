class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        baseline = 0
        for x, satisfied in zip(customers, grumpy):
            if satisfied == 0:
                baseline += x
        print(baseline)

        gain = [0] * N
        for i in range(N):
            if grumpy[i] == 1:
                gain[i] = customers[i]

        window_sum = 0
        best = 0
        left = 0
        for right in range(N):
            window_sum += gain[right]

            if right - left + 1 > minutes:
                window_sum -= gain[left]
                left += 1
            
            # valid window calculate best
            if right - left + 1 == minutes:
                if window_sum > best:
                    best = window_sum
        
        return best + baseline
        

