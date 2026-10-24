class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        openCloseBrackets = {")": "(", "}": "{", "]": "["}

        # loop through each character
        for c in s:
            # add opening bracket to stack
            if c in ["(", "{", "["]:
                brackets.append(c)

            # verify closing brackets match the stack and remove
            if c in openCloseBrackets.keys():
                if brackets and brackets[-1] == openCloseBrackets[c]:
                    brackets.pop()
                else:
                    return False

        return not bool(brackets)
