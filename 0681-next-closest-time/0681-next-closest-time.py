class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(':', ''))
        curH = int(time[:2])
        curM = int(time[3:])
        now = curH * 60 + curM

        best_delta = 1441
        best = None

        for a in digits:
            for b in digits:
                hh = int(a) * 10 + int(b)
                if hh >= 24:
                    continue
                for c in digits:
                    for d in digits:
                        mm = int(c) * 10 + int(d)
                        if mm >= 60:
                            continue
                        cand = hh * 60 + mm
                        delta = (cand - now) % 1440
                        if 0 < delta < best_delta:
                            best_delta = delta
                            best = f"{hh:02d}:{mm:02d}"

        return best if best is not None else time