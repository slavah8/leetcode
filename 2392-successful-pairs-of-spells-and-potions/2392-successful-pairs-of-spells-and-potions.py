class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        result = []
        potions.sort()
        N = len(potions)
        # lowest possible potion that can succeed
        def lowest_index(spell):
            low = 0
            high = len(potions) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if (potions[mid] * spell) >= success:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        for spell in spells:
            j = lowest_index(spell)
            print(j)
            if j != -1:
                result.append(N - j)
            else:
                result.append(0)
            
        return result



