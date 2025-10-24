class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        # (monster_power, coin), sorted by power
        monster_coin = sorted(zip(monsters, coins), key=lambda x: x[0])

        # (hero_power, original_index), sorted by power
        heroes_sorted = sorted((h, i) for i, h in enumerate(heroes))

        N = len(heroes)
        M = len(monsters)
        i = 0
        j = 0
        total = 0
        ans = [0] * N
        while i < N:
            h, orig_idx = heroes_sorted[i]

            while j < M and monster_coin[j][0] <= h:
                total += monster_coin[j][1]
                j += 1
            ans[orig_idx] = total
            i += 1
        return ans