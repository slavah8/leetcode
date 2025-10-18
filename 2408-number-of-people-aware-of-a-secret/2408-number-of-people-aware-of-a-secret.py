class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Let dp[i][j] be the number of people who have known the secret for exactly j + 1 days, at day i.

        # original problem : number of people who know the secret at day n
        # dp[]
        # person who learned on day t can share on days t + delay, t + delay + 1, …, t + forget − 1
        # They cannot share on day t + forget
        MOD = 10 ** 9 + 7
        
        # new[i] = number of people who first learn the secret on day i
        new = [0] * (n + 1)
        
        new[1] = 1
        sharers = 0 # number of people who are currently allowed to share on day i
        for i in range(2, n + 1):
            
            start = new[i - delay] if i - delay >= 0 else 0 # people who become sharers today
            stop = new[i - forget] if i - forget >= 0 else 0 # people who stop being sharers today

            sharers = sharers + start - stop

            # everyone who is allowed to share today creates exactly one new learner
            new[i] = sharers

        # people who still remember at day n: 
        left = max(1, n - forget + 1)
        ans = sum(new[left: n + 1]) % MOD
        return ans

