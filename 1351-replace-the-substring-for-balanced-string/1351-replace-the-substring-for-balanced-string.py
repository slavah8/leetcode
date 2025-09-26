class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        target = N // 4
        counts = Counter(s)

        need = {c : max(0, counts[c] - target) for c in 'QWER'}
        if all(v == 0 for v in need.values()):
            return 0
        
        def covers():
            return all(window[c] >= need[c] for c in 'QWER')

        window = Counter()
        result = N
        left = 0
        for right in range(N):
            char = s[right]
            window[char] += 1
            while covers():
                # try to shrink window
                result = min(result, right - left + 1)
                left_char = s[left]
                window[left_char] -= 1
                left += 1
        return result

