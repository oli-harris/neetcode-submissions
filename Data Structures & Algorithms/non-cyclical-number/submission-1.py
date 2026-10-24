class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquaredDigits(n)

        while fast != 1 and slow != fast:
            slow = self.sumSquaredDigits(slow)
            fast = self.sumSquaredDigits(fast)
            fast = self.sumSquaredDigits(fast)
        
        return fast == 1


    def sumSquaredDigits(self, n: int):
        res = 0

        while n:
            digit = n % 10
            res += digit ** 2

            n = n // 10

        return res
