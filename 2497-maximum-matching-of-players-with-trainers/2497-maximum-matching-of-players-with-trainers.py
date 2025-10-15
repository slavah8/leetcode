class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        print(players)
        print(trainers)
        N = len(players)
        M = len(trainers)

        i = 0 # players index
        j = 0 # trainers index
        matches = 0
        while i < N and j < M:
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return matches
