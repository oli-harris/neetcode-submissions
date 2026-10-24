class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def sumDigits(num):
            return sum([int(c)**2 for c in str(num)])

        while n not in seen:
            seen.add(n)
            n = sumDigits(n)

            if n == 1:
                return True

        return False
        

        