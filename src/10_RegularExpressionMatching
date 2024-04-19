class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D table rows as each char at s, columns as each char as p
        # First character we assume both are empty
        rows, columns = len(s) + 1, len(p) + 1
        states = [[False for j in range(columns)] for i in range(rows)]
        
        # If both are empty they are matching
        states[0][0] = True

        # Fix the states for the * (if * is in begining read from older states)
        for j in range(2, columns):
            if p[j - 1] == "*":
                states[0][j] = states[0][j - 2]
                
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '*':
                    if p[j - 1] == '.' or p[j - 1] == s[i]: # add previous charcter we read or it has * state after it 
                        states[i + 1][j + 1] = states[i][j + 1] or states[i + 1][j - 1]
                    else:
                        states[i + 1][j + 1] = states[i + 1][j - 1]
                elif p[j] == '.' or p[j] == s[i]:
                    states[i + 1][j + 1] = states[i][j]

        return states[rows - 1][columns - 1]
