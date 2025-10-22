class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        N = len(arr)
        ans = 0
        for i in range(N - 2):
            a = arr[i]
            need = target - a
            l = i + 1
            r = N - 1
            while l < r:
                s = arr[l] + arr[r]
                if s < need:
                    l += 1
                elif s > need:
                    r -= 1
                else: # s == need
                    if arr[l] != arr[r]:
                        left_val = arr[l]
                        cl = 1
                        l += 1
                        while l < r and arr[l] == left_val:
                            cl += 1
                            l += 1
                        right_val = arr[r]
                        cr = 1
                        r -= 1
                        while l <= r and arr[r] == right_val:
                            cr += 1
                            r -= 1
                        ans = (ans + cl * cr) % MOD
                    else: # entire block is the same
                        m = r - l + 1
                        ans = (ans + (m * (m - 1) // 2)) % MOD
                        break

        return ans