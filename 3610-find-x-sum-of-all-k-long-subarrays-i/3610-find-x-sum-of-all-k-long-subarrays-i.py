class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        

        l = 0
        freq = defaultdict(int)
        arr = []
        answer = []
        for r, num in enumerate(nums):
            freq[num] += 1
            heapq.heappush(arr, (-freq[num], -num))
            if r - l + 1 > k:
                num_left = nums[l]
                freq[num_left] -= 1
                if freq[num_left] == 0:
                    del freq[num_left]
                l += 1
            
            if r - l + 1 == k:
                summ = 0
                tmp = arr[:]
                heapq.heapify(tmp)
                taken = 0
                used = set()
                while tmp and taken < x:
                    frq, nm = heapq.heappop(tmp)
                    
                    frq = -frq
                    nm = -nm
                    
                    if nm in used:
                        continue
                    if freq.get(nm, 0) != frq or frq == 0:
                        continue
                    summ += nm * frq
                    used.add(nm)
                    taken += 1
                answer.append(summ)
        return answer
            

            


