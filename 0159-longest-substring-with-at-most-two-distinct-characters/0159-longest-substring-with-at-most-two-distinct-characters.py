class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        counts = defaultdict(int)
        N = len(s)
        left = 0
        longest = 0
        for right in range(N):
            right_char = s[right]
            counts[right_char] += 1
            while len(counts) > 2:
                left_char = s[left]
                counts[left_char] -= 1
                if counts[left_char] == 0:
                    del counts[left_char]
                left += 1
            longest = max(longest, right - left + 1)
        return longest
            
