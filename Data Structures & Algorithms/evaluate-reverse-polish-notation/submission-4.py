class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integers = [] # stores integers as a stack

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                integers.append(int(token)) # add to stack
            else:
                n2, n1 = integers.pop(), integers.pop()
                result = self.operation(n1, n2, token) # calculates result from two elements ontop of stack

                integers.append(result)
                

        return integers[0] # last item left in stack is result




    def operation(self, n1, n2, operand):
        if operand == "+":
            return n1 + n2
        if operand == "-":
            return n1 - n2
        if operand == "*":
            return n1 * n2
        if operand == "/":
            return int(n1 / n2) # truncates towards zero
