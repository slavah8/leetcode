class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_list = []
        n = len(timePoints)
        for time in timePoints:

            new_time = time.split(":")
            print(new_time)
            hours = int(new_time[0])
            minutes = int(new_time[1])
            
            total = hours * 60 + minutes
            time_list.append(total)
        
        print(time_list)
        time_list.sort()

        full_cycle = 24 * 60
        print(full_cycle)
        INF = 10 ** 10
        best = INF
        for i in range(n - 1):
            if i == 0: # need to check the end time
                first = time_list[i]
                second = time_list[n - 1]
                diff = min(abs(first - second), abs(full_cycle - first) + second, abs(full_cycle - second) + first)
                best = min(diff, best)
                
            
            first = time_list[i]
            second = time_list[i + 1]
            diff = min(abs(first - second), abs(full_cycle - first) + second, abs(full_cycle - second) + first)
            best = min(diff, best)  

        return best
