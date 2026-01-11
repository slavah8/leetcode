class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        

        char_count = Counter(s)

        heap = [(-cnt, ch) for ch, cnt in char_count.items()]  # store (-count, char)
        heapq.heapify(heap)


        cooldown = deque() # store (release_index, -count, char)

        res = []
        idx = 0

        while heap or cooldown:


            while cooldown and idx >= cooldown[0][0]:
                index, cnt, ch = cooldown.popleft()
                heapq.heappush(heap, (cnt, ch))
            
            if not heap:
                return ""

            neg_cnt, char = heapq.heappop(heap)
            res.append(char)

            neg_cnt += 1
            if neg_cnt < 0:
                cooldown.append((idx + k, neg_cnt, char))
            
            idx += 1

        return "".join(res)