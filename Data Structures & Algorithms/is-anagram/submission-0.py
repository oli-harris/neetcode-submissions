class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sorted = sorted([x for x in s])
        t_sorted = sorted([x for x in t])

        if s_sorted == t_sorted:
            return True
        
        return False