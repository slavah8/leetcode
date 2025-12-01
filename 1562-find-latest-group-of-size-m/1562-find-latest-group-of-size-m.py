class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        length = [0] * (n + 2)
        last = -1
        count = [0] * (n + 1) # how many groups of 1s have length i count[i]
        for step, pos in enumerate(arr, 1):
            left_len = length[pos - 1]
            right_len = length[pos + 1]
            new_len = left_len + right_len + 1

            if left_len > 0:
                count[left_len] -= 1
            
            if right_len > 0:
                count[right_len] -= 1
            
            L = pos - left_len
            R = pos + right_len
            length[L] = length[R] = new_len
            count[new_len] += 1

            if count[m] > 0:
                last = step
            
        return last




            

