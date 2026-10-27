class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def pos(c):
            return ord(c) - ord('a')

        k = len(s1)
        if k > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26
        for i in range(k):
            need[pos(s1[i])] += 1
            window[pos(s2[i])] += 1

        matches = sum(need[i] == window[i] for i in range(26))

        if matches == 26:
            return True

        for r in range(k, len(s2)):
            # add r
            i = pos(s2[r])
            window[i] += 1
            if window[i] == need[i]:
                matches += 1
            elif window[i] == need[i] + 1:
                matches -= 1
    
            # remove l
            i = pos(s2[r - k])
            window[i] -= 1
            if window[i] == need[i] - 1:
                matches -= 1
            elif window[i] == need[i]:
                matches += 1
            
            if matches == 26:
                return True

        return False
