class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        counts = defaultdict(int)
        curr_string = ""
        N = len(s)
        left = 0
        total = 0
        for right in range(N):
            char = s[right]
            counts[char] += 1
            curr_string += char
            while len(curr_string) > k or counts[char] > 1:
                curr_string = curr_string[1:]
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
            
            
            if len(curr_string) == k:
                total += 1
        return total




