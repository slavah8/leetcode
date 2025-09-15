class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        N = len(garbage)
        last = {"M": -1, "G": -1, "P": -1}
        pickups = 0
        for index, s in enumerate(garbage):
            pickups += len(s)
            for char in s:
                last[char] = index
        
        prefix = [0] * N

        for i in range(1, N):
            prefix[i] = prefix[i - 1] + travel[i - 1]
        print(prefix)
            
        travel_time = 0
        for char in ('M', 'P', 'G'):
            if last[char] != -1:
                travel_time += prefix[last[char]]
        
        return travel_time + pickups

