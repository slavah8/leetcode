class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(pattern, s):
            i = 0
            for char in s:
                if i < len(pattern) and char == pattern[i]:
                    i += 1
                    if i == len(pattern):
                        return True
            return i == len(pattern)
            
                
        # can you still make the subsequence p if you remove indices up to K from removable
        def can_remove(K):
            set_indices = set(i for i in removable[:K])

            out = ''.join(char for idx, char in enumerate(s) if idx not in set_indices)
            return is_subsequence(p, out)
        
        low = 0
        high = len(removable)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_remove(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans



        