class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            seen.add(n)

            n = self.sumSquaredDigits(n)
            
            if n in seen:
                return False
            

        return True

    def sumSquaredDigits(self, n: int):
        res = 0

        while n:
            digit = n % 10
            res += digit ** 2

            n = n // 10

        return res
