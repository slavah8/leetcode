class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        count = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            answer += count[idx] + 1
            count[idx] += 1
        return answer