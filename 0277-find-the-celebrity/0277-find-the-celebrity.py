# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        cand = 0

        for i in range(1, n):

            if knows(cand, i): # cand cant be celeb
                cand = i
            # else cand can still be celeb
        
        print(cand)


        # check if everyone knows cand
        for i in range(n):
            if i == cand:
                continue

            if knows(i, cand) and not knows(cand, i):
                continue
            else:
                return -1
        
        return cand