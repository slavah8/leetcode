class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        

        n = len(books)

        # dp[i] defined as min height to place first i books 
        INF = 10 ** 10
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            width = 0
            max_height = 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], max_height + dp[j])
        
        return dp[n]
                
                
            
                
                
