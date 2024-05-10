class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n: # we reach the number of paranthesis we want so add it to result
                res.append("".join(stack))
                return

            if openN < n: # we can add an open paranthesis
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop() 

            if closeN < openN: # we can add a close paranthesis
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
            

