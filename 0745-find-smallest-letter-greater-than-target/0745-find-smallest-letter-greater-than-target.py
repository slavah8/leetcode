class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            char = letters[mid]
            if char > target:
                right = mid - 1
            elif char <= target:
                left = mid + 1
            
        if left >= len(letters):
            return letters[0]
        else:
            return letters[left]
        


