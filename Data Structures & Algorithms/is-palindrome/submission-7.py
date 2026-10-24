class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # get next alphanumeric char on l and r
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            
            # check palindrome
            if s[l].lower() != s[r].lower():
                return False
            
            # shift pointers
            l, r = l + 1, r - 1
        
        return True

    def isAlphaNumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


        
        