class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def sumDigits(num):
            sumSquaredDigits = 0
            while num != 0:
                digit = num % 10
                num = num // 10
                sumSquaredDigits += digit ** 2
            
            return sumSquaredDigits

        while n not in seen:
            seen.add(n)
            n = sumDigits(n)

            if n == 1:
                return True

        return False
        

        