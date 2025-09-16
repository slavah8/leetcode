class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_end = 0
        wait = 0
        for arrival, time in customers:
            
            if curr_end < arrival:
                wait += time
                curr_end = (time + arrival)
            else:
                wait += (curr_end - arrival)
                wait += time
                curr_end += time
            
        return wait / len(customers)
            

            