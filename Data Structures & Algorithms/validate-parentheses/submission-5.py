class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        openCloseBrackets = {")": "(", "}": "{", "]": "["}

        # loop through each character
        for c in s:
            # remove closing brackets from stack and verify
            if c in openCloseBrackets.keys():
                if brackets and brackets[-1] == openCloseBrackets[c]:
                    brackets.pop()
                else:
                    return False

            # add opening bracket to stack
            else:
                brackets.append(c)

        return not bool(brackets)
