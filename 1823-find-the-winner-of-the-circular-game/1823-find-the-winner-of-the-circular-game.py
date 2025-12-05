class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        circle = [(i + 1) for i in range(n)]
        print(circle)

        friend = 1
        while len(circle) > 1:
            idx = circle.index(friend)
            next_idx = (idx + (k - 1)) % len(circle)
            next_start = (next_idx + 1) % len(circle)
            friend = circle[next_start]
            del circle[next_idx]
            print(circle)

        return circle[0] 

            

            
        
        
        


