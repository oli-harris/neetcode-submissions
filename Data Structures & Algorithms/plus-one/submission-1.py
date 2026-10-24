class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while i >= 0 and carry:
            digit = digits[i]
            increment = digit + carry
            digits[i] = increment % 10

            carry = increment // 10

            i -= 1
            

        if carry:
            digits.insert(0, 1)

        return digits