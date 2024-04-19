class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        
        res = 0
        for i in range(len(s)):
            if i == len(s) - 1: # last character always add value
                res += values[s[i]]
                break
            cur, nxt = values[s[i]], values[s[i + 1]]
            if cur < nxt: # If left char value is less than right char value then you must reduce it
                res -= cur
            else: # else you must add it
                res += cur
        return res
