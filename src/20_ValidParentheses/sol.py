class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for c in s:
            if c in pair.values():
                stack.append(c)
                continue

            if len(stack) <= 0: # stack is empty while it should not be
                return False

            if pair[c] != stack.pop(): # paranthesis correspondace is wrong
                return False
                
        return len(stack) == 0
