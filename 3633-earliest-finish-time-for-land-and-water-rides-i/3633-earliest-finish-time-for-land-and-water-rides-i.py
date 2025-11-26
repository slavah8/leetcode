class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # find the earliest times you can finish either 
        INF = 10 ** 10
        earliest_water = INF
        earliest_land = INF

        land = list(zip(landStartTime, landDuration))
        water = list(zip(waterStartTime, waterDuration))
        
        n = len(land)
        m = len(water)
        INF = 10 ** 10
        best = INF
        print(land)
        print(water)
        for i in range(n):
                land_start, land_duration = land[i]
                for j in range(m):
                    water_start, water_duration = water[j]

                    # case 1 : land first
                    land_end = land_start + land_duration
                    start_water = max(water_start, land_end)
                    cand1 = start_water + water_duration
                    #case 2 : water first
                    water_end = water_start + water_duration
                    start_land = max(land_start, water_end)
                    cand2 = start_land + land_duration
                    best = min(best, cand1, cand2)

                    


        return best
                


            

            

