class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxLength = 0
        maxFreq = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            
            subLen = (r - l + 1)
            
            if subLen - maxFreq <= k: # can replace all other characters
                maxLength = max(maxLength, subLen)
            else: 
                freq[s[l]] -= 1
                l += 1

        return maxLength
        
