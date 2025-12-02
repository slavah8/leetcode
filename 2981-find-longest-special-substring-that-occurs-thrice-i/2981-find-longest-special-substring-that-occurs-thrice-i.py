class Solution:
    def maximumLength(self, s: str) -> int:
        subs = []
        n = len(s)
        sub_count = defaultdict(int)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                sub_count[sub] += 1

        print(sub_count)
        best = -1
        for sb, cnt in sub_count.items():
            if cnt >= 3:
                if len(sb) > best and len(set(sb)) == 1:
                    best = len(sb)
        return best