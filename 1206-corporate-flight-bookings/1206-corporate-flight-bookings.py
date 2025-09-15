class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        diff = [0] * (n + 1)

        for L, R, seats in bookings:
            diff[L - 1] += seats
            diff[R] -= seats
        print(diff)

        ans = [0] * n
        running = 0
        for i in range(n):
            running += diff[i]
            ans[i] = running
        return ans