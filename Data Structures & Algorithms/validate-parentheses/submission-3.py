class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        # loop through each character
        for c in s:
            print(brackets)
            if c in ["(", "{", "["]:
                brackets.append(c)
            elif c == ")":
                if brackets and brackets[-1] == "(":
                    brackets.pop()
                else:
                    return False
            elif c == "}":
                if brackets and brackets[-1] == "{":
                    brackets.pop()
                else:
                    return False
            elif c == "]":
                if brackets and brackets[-1] == "[":
                    brackets.pop()
                else:
                    return False

        return not bool(brackets)
