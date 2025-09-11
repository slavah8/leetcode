class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        N = len(answerKey)

        counts = collections.Counter()
        longest = 0
        
        left = 0
        most_frequent_count = 0
        for right in range(N):
            char = answerKey[right]
            counts[char] += 1
            most_frequent_count = max(most_frequent_count, counts[char])
            window_size = right - left + 1
            if window_size > most_frequent_count + k: # need to shrink the window
                left_char = answerKey[left]
                counts[left_char] -= 1
                left += 1
                window_size -= 1
            longest = max(longest, window_size)
        return window_size

            

