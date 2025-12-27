class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        # dp(city, fuel_left) = number of routes from city to finish using at most fuel_left fuel.
        @lru_cache(None)
        def dp(city, fuel_left):

            ans = 1 if city == finish else 0
            
            for j in range(n):
                if city == j:
                    continue
                cost = abs(locations[city] - locations[j])

                if fuel_left >= cost:
                    ans = (ans + dp(j, fuel_left - cost)) % MOD
            
            return ans



        return dp(start, fuel)