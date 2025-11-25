class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                if 2 * arr[j] == arr[i]:
                    return True
        return False
                