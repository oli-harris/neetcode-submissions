class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def pos(c):
            return ord(c) - ord('a')

        freq1 = [0] * 26
        for c in s1:
            freq1[pos(c)] += 1
        
        freqCount = [0] * 26
        l, r = 0, 0 

        for r in range(len(s2)):
            if freq1[pos(s2[r])] == 0:
                while l < r:
                    freqCount[pos(s2[l])] = max(freqCount[pos(s2[l])] - 1, 0)
                    l += 1
                continue

            freqCount[pos(s2[r])] += 1

            while freqCount[pos(s2[r])] > freq1[pos(s2[r])]:
                freqCount[pos(s2[l])] -= 1
                l += 1

            if freq1 == freqCount:
                return True

        return False
