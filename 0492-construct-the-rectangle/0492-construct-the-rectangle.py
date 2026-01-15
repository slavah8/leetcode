class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        L = area
        W = 1

        new_W = W
        new_L = L
        while W <= sqrt(area):
           
            
            if area % W == 0:
                new_L = area // W
                new_W = W
                if new_L == new_W:
                    break
            W += 1
            
            print(new_L)
            print(new_W)
        
        return [new_L, new_W]


            