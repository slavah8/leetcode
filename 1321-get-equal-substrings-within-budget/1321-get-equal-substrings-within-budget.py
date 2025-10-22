class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        diff = [0] * N

        for i in range(N):
            char1 = ord(s[i]) - ord('a')
            char2 = ord(t[i]) - ord('a')

            diff[i] = abs(char1 - char2)
        print(diff)
        l = 0
        longest = 0
        cost = 0
        for r in range(N):
            cost += diff[r]

            while cost > maxCost:
                cost -= diff[l]
                l += 1
            print(r - l + 1)
            longest = max(longest, r - l + 1)
        return longest

