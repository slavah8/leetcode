class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        events = defaultdict(int)
        INF = 10 ** 10
        minn = INF
        maxx = -INF
        for pos, rng in lights:
            minn = min(minn, pos - rng)
            maxx = max(maxx, pos + rng)
        
        Lbound = min(minn, 0)
        Rbound = max(maxx, n - 1)
        offset = -Lbound
        size = (Rbound - Lbound + 2)
        diff = [0] * (size)
        for pos, rng in lights:
            L = (pos - rng) + offset
            R = (pos + rng) + offset
            diff[L] += 1
            diff[R + 1] -= 1
        print(diff)

        running = 0
        count = 0
        result = [0] * (size)
        for i in range(size):
            running += diff[i]
            result[i] = running
        print(result)

        for position, required in enumerate(requirement):
            idx = position + offset
            if result[idx] >= required:
                count += 1
        return count

        


