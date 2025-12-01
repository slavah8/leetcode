class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        j = 0
        m = len(passengers)
        for bus in buses:
            taken = 0
            while j < m and passengers[j] <= bus and taken < capacity:
                taken += 1
                last_board_time = passengers[j]
                j += 1
            last_bus_taken = taken
        

        occupied = set(passengers)
        if last_bus_taken < capacity:
            t = buses[-1]
        else:
            t = last_board_time - 1
        
        while t in occupied:
            t -= 1
        return t

