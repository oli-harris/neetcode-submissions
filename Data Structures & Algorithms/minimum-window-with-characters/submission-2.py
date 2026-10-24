class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freqT = defaultdict(int)
        for c in t:
            freqT[c] += 1

        freqWindow = defaultdict(int)

        have = 0
        need = len(freqT)

        res = [0, len(s)] # left, right
        resLen = len(s) + 1

        l = 0
        for r in range(len(s)):
            if s[r] in freqT:
                freqWindow[s[r]] += 1

                if freqWindow[s[r]] == freqT[s[r]]:
                    have += 1
            
            while have == need:
                res = min([l, r], res, key=lambda x: x[1] - x[0])
                resLen = res[1] - res[0] + 1

                if s[l] in freqT:
                    freqWindow[s[l]] -= 1

                    if freqWindow[s[l]] < freqT[s[l]]:
                        have -= 1
                
                l += 1

        print(res)
        return s[res[0] : res[1] + 1] if resLen <= len(s) else ""