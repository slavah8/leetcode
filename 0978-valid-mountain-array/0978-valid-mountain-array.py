class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        peak = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                continue
            else:
                # i is the peak
                peak = i
                break
        print(peak)
        if peak == 0:
            return False
        
        for i in range(peak, len(arr) - 1):
            print(i)
            if arr[i] > arr[i + 1]:
                continue
            else:
                return False
        return True
        

            
