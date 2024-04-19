class Solution:
    def intToRoman(self, num: int) -> str:
        order = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
        temp = num
        result = ""
        for i in range(len(order)):
            # only who start with 1 is matter so skip whom start with 5
            if i % 2 != 0:
                continue
            
            # get remainder and quotient to have digits of them
            freq = temp // order[i][1]
            temp = temp % order[i][1]

            if freq < 4: # less than 4 (III)
                result += f"{order[i][0] * freq}"
            elif freq == 4: # it is 4  (IV)
                result += f"{order[i][0]}{order[i - 1][0]}"
            elif freq < 9: # between 4 and 9 (VII)
                result += f"{order[i - 1][0]}{order[i][0] * (freq - 5)}"
            else: # it is nine (IX)
                result += f"{order[i][0]}{order[i - 2][0]}"

        return result
