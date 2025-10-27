class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = 0

        for x in bank:
            if x.count('1') == 0:
                continue

            devices = x.count('1')
            total += devices * prev
            prev = devices
        return total
