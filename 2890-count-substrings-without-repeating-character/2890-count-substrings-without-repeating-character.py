class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:

        counts = defaultdict(int)

        left = 0
        N = len(s)
        total = 0
        for right in range(N):
            right_char = s[right]
            counts[right_char] += 1
            while counts[right_char] > 1:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
            total += (right - left + 1)

        return total
            