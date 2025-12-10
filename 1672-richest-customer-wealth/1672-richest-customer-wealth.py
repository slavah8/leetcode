class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        cols = len(accounts[0])

        wealth = 0
        for r in range(rows):
            customer_sum = 0
            for c in range(cols):
                customer_sum += accounts[r][c]

            wealth = max(wealth, customer_sum)

        return wealth  