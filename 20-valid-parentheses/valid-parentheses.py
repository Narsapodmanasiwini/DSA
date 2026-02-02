class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in bracket_map.values():
                stack.append(bracket)
            elif bracket in bracket_map.keys():
                if stack == [] or bracket_map[bracket] != stack.pop():
                    return False
        return stack == []


        