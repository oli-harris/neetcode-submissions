class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxLength = 0
        maxFreq = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)

        return maxLength
        
