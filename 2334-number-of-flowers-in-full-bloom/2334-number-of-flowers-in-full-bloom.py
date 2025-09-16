class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        coords = set(people)
        
        for L, R in flowers:
            coords.add(L)
            coords.add(R + 1)
        
        T = sorted(coords)
        print(T)
        idx = {t: i for i, t in enumerate(T)}
        print(idx)

        diff = [0] * (len(T) + 1)
        for L, R in flowers:
            diff[idx[L]] += 1
            diff[idx[R + 1]] -= 1
        print(diff)

        active = [0] * len(T)
        running = 0
        for i in range(len(T)):
            running += diff[i]
            active[i] = running
        print(active)

        answer = [0] * len(people)

        for i, p in enumerate(people):
            k = bisect_right(T, p) - 1
            answer[i] = active[k]
        return answer

            