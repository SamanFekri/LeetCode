class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        for i in range(len(digits)):
            l = dMap[digits[i]]
            if i == 0:
                result = l
            else:
                result = self.listProduct(result, l)
        return result
        
    def listProduct(self, l1: List[str], l2: List[str]) -> List[str]: # make combination of 2 lists
        result = []
        for s1 in l1:
            for s2 in l2:
                result.append(f'{s1}{s2}')
        return result
