class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        diff = [0] * (N + 1)

        for L, R, direction in shifts:
            if direction == 0:
                direction = -1
            diff[L] += direction
            diff[R + 1] -= direction
        
        running = 0
        result = [0] * N
        for i, char in enumerate(s):
            running += diff[i]
            result[i] = running

        ans = ""
        base = ord('a')
        for index, char in enumerate(s):
            new_char = chr((ord(char) - base + result[index]) % 26 + base)
            print(new_char)
            ans += new_char
        return ans
